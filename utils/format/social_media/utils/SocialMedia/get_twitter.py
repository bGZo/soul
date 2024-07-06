#!/usr/bin/python
#-*- coding: utf-8 -*-
import requests
import json

from markdownify import markdownify as md
from datetime import datetime

from .result import Result
from .template import IMG_TEMPLATE, TWITTER_TEMPLATE
from .utils import format_link, format_response, get_line_spaces, test_output


def get_tweet_from_tweetpik_v2(line):
    if line == "" or line == "\n":
        return Result()

    base_url = 'https://tweetpik.com/api/v2/tweets?url='
    first_line_spaces, others_line_spaces = get_line_spaces(line)
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
        return Result().failed(url, str(e))

    tweetContent = md(res['textHtml'])
    if 'photos' in res:
        tweetContent += "\n"
        for media in res['photos']:
            tweetContent += IMG_TEMPLATE.format(media)

    tweet = TWITTER_TEMPLATE.format(
        first_line_spaces,
        others_line_spaces, tweetContent,
        others_line_spaces, md(res['nameHtml']),
        str(datetime.strptime(res['datetime'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y%m%d, %H:%M:%S')), res['url'],
        others_line_spaces, str(res['likes']), str(res['retweets']), str(res['replies']),
        others_line_spaces)

    with open("backup_res_twitter.json", "a", encoding='UTF-8') as f:
        f.write(str(res) + "\n")

    return Result().success(url, tweet)


def get_tweet_from_tweetpik_thread(line):
    base_url = 'https://tweetpik.com/api/thread?tweetId='
    first_line_spaces, others_line_spaces = get_line_spaces(line)
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
        return Result().failed(url, str(e))

    tweetContent = ""
    tweetMeidas = ""
    for response in responses:
        tweetContent += format_response(md(response['textHtml']))
        if 'photos' in response and response['photos'] is not None:
            tweetMeidas += "\n"
            try:
                for media in response['photos']:
                    tweetMeidas += IMG_TEMPLATE.format(others_line_spaces, media)
            except Exception as e:
                print("Handle the photos occurs errors: " + e + "!")
        if 'videos' in response and len(response['videos']) != 0:
            try:
                tweetMeidas += IMG_TEMPLATE.format(response['videos'][0]['poster'])
            except Exception as e:
                print("Handle the photos occurs errors!")

    tweet = TWITTER_TEMPLATE.format(
        first_line_spaces,
        others_line_spaces, tweetContent + tweetMeidas,
        others_line_spaces, md(response['nameHtml']),
        str(datetime.strptime(response['datetime'], '%a %b %d %H:%M:%S %z %Y').strftime('%Y%m%d, %H:%M:%S')),
        response['url'],
        others_line_spaces, str(responses[0]['likes']), str(responses[0]['retweets']), str(responses[0]['replies']),
        others_line_spaces)

    with open("backup_res_twitter.json", "a", encoding='UTF-8') as f:
        f.write(str(res) + "\n")

    return Result().success(url, tweet)


if __name__ == "__main__":
    # test_output(get_tweet_from_tweetpik_thread('https://twitter.com/pandazhq/status/1678395427899465728?s=52&t=LgI9ZHE1jAdamynKbX8X6w'))
    print(get_tweet_from_tweetpik_thread(
        'https://twitter.com/HiTw93/status/1656811675994198017?t=zQiUf7xI-b5SKsv-MTK6NA&s=35'))
