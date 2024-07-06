import requests

from markdownify import markdownify as md

from template import IMG_TEMPLATE, MASTODON_TEMPLATE
from utils import format_link, format_response


def get_mastodon_from_api(line):
  split_line = format_link(line).split('/')
  url = 'https://' + split_line[2] + '/api/v1/statuses/' + split_line[4]

  try:
    res = requests.get(url, headers={
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
    }).json()
  except Exception as e:
    print(e)
    print("Handle " + line + " occur error")
    return ""

  post_content = format_response(md(res['content']))
  if 'media_attachments' in res:
    post_content += "\n"
    for media in res['media_attachments']:
      post_content += IMG_TEMPLATE.format(media['url'])
  post = MASTODON_TEMPLATE.format(
            post_content,
            res['account']['username'], res['created_at'], res['url'])
  
  with open("backup_res_mastodon.json", "a", encoding='UTF-8') as f:
    f.write(str(res)+"\n")

  print ("Handle Mastodon {} Done. Congardulations! 🎉".format(res['url']))
  return post

if __name__ == '__main__':
  url = 'https://o3o.ca/@dontworry@toot.mantyke.icu/110733676312713098'
  print(get_mastodon_from_api(url))