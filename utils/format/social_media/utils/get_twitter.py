import requests
import json

from markdownify import markdownify as md
from datetime import datetime

from template import IMG_TEMPLATE, TWITTER_TEMPLATE
from utils import format_link, format_response

def get_tweet_from_tweetpik_v2(line):
  base_url = 'https://tweetpik.com/api/v2/tweets?url='
  url = base_url + format_link(line)

  try:
    res = requests.get(url, headers={
        'Accept-Encoding': 'gzip, deflate',
        "Accept": "application/json",
        'Connection': 'keep-alive',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
        "Referer": "https://tweetpik.com/"
    })
    responseText = format_response(res.text)
    res = json.loads(responseText)[0]
  except Exception as e:
    print(e)
    print(responseText)
    print("Handle " + url + " occur error")
    return ""

  tweetContent = md(res['textHtml'])
  if 'photos' in res:
    tweetContent += "\n" 
    for media in res['photos']:
      tweetContent += IMG_TEMPLATE.format(media)
  tweet = TWITTER_TEMPLATE.format(
            tweetContent,
            md(res['nameHtml']),
            str(datetime.strptime(res['datetime'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y%m%d, %H:%M:%S')),
            res['handler'], res['id'],
            str(res['likes']), str(res['retweets']), str(res['replies']))

  with open("backup_res_twitter.json", "a", encoding='UTF-8') as f:
    f.write(str(res)+"\n")
 
  print ("Handle Tweets {} Done. Congardulations! 🎉".format(url))
  return tweet

def get_tweet_from_tweetpik_thread(line):
  base_url = 'https://tweetpik.com/api/thread?tweetId='
  split_line = format_link(line).split('/')
  url = base_url + split_line[5]
  try:
    res = requests.get(url, headers={
        'Accept-Encoding': 'gzip, deflate',
        "Accept": "application/json",
        'Connection': 'keep-alive',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
        "Referer": "https://tweetpik.com/"
    })
    responses = json.loads(res.text)
  except Exception as e:
    print(e)
    print(responseText)
    print("Handle " + url + " occur error")
    return ""

  tweetContent = ""
  tweetMeidas = ""
  for response in responses:
    tweetContent += response['textHtml']
    if 'photos' in response and response['photos'] is not None:
      tweetMeidas += "\n"
      for media in response['photos']:
        tweetMeidas += IMG_TEMPLATE.format(media)
    if 'videos' in response and len(response['videos']) != 0 :
        tweetMeidas += IMG_TEMPLATE.format(response['videos'][0]['poster'])

  tweet = TWITTER_TEMPLATE.format(
            tweetContent + tweetMeidas,
            md(response['nameHtml']),
            str(datetime.strptime(response['datetime'], '%a %b %d %H:%M:%S %z %Y').strftime('%Y%m%d, %H:%M:%S')),
            response['url'],
            str(responses[0]['likes']), str(responses[0]['retweets']), str(responses[0]['replies']))

  with open("backup_res_twitter.json", "a", encoding='UTF-8') as f:
    f.write(str(res)+"\n")
 
  print ("Handle Tweets {} Done. Congardulations! 🎉".format(url))
  return tweet

if __name__ == "__main__":
  print(get_tweet_from_tweetpik_thread('https://twitter.com/pandazhq/status/1678395427899465728?s=52&t=LgI9ZHE1jAdamynKbX8X6w'))