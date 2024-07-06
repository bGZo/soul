import json
import requests
import re

import argparse
from argparse import RawTextHelpFormatter

from datetime import datetime
from markdownify import markdownify as md

TWITTER_TEMPLATE = ("- #+BEGIN_QUOTE\n"
                    "{}\n"
                    "— {} [{}](https://twitter.com/{}/status/{})\n"
                    "❤️ {} 🔁 {} 💬 {}\n"
                    "#+END_QUOTE\n")
MASTODON_TEMPLATE = ("- #+BEGIN_QUOTE\n"
                     "{}\n"
                     "— {} [{}]({})\n"
                     "#+END_QUOTE'\n")
IMG_TEMPLATE = "![🖼️]({}){{:width 300}} "


def from_twitter(line):
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
        responseTxt = format_response(res.text)
        res = json.loads(responseTxt)[0]
    except Exception as e:
        print(e)
        print(responseTxt)
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
        f.write(str(res) + "\n")

    print("Handle Tweets {} Done. Congardulations! 🎉".format(url))
    return tweet


def format_link(link):
    link = re.sub("\?s=\d+&t=[-\w]+\n*", "", link)
    link = re.sub("\?s=\d+\n*", "", link)
    link = re.sub(" ", "", link)
    link = re.sub("-", "", link)
    return link


def format_response(response):
    response = re.sub(r'\n', '', response)
    response = re.sub(r'\n\n', '\n', response)
    response = re.sub(r'\\"', '\'', response)
    return response


def get_info(file):
    posts_collection = []
    for line in file:
        if (re.search(r"twitter\.com", line)):
            # print("twitter")
            posts_collection.append(from_twitter(line))
        # else:
            # print("mastodon")
            # posts_collection.append(from_mastodon(line))
    return posts_collection


def output(file_name, lines):
    with open(file_name, 'w', encoding='UTF-8') as f:
        for line in lines:
            f.write(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="get_twitter_mastodon_content_with_logseq_format.py",
        description="Get the content of post of Twitter/Mastodon meantime.\n\nThe former depends \
        the API v2 by https://tweetpik.com, the latter use the Official API.\nThe script need the \
        input file(one link each line), with option output, which will\noverwrite the input file \
        by default. Besides, the whole success responses will be\nsaved in backup_res_xxx.json file",
        formatter_class=RawTextHelpFormatter)

    parser.add_argument("file", type=argparse.FileType('r', encoding='UTF-8'),
                        help="Add the source url links file to handle")
    parser.add_argument("-o", "--output", action="store",
                        help="Flag this would output instead of default file(output.md)")

    args = parser.parse_args()

    if args.file:
        response = get_info(args.file)

    if args.output is not None:
        output(args.output, response)
    else:
        output(args.file.name, response)
