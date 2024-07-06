#!/usr/bin/python
#-*- coding: utf-8 -*-
import requests

from markdownify import markdownify as md
from datetime import datetime

from .result import Result
from .template import IMG_TEMPLATE, MASTODON_TEMPLATE
from .utils import format_link, format_response, get_line_spaces, test_output


def get_mastodon_from_api(line):
    first_line_spaces, others_line_spaces = get_line_spaces(line)
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
        return Result().failed(line, str(e))

    post_content = format_response(md(res['content']))
    post_media = res['media_attachments']

    if len(post_media) != 0:
        post_content += "\n"
        for media in post_media:
            post_content += IMG_TEMPLATE.format(media['url'])
    post = MASTODON_TEMPLATE.format(
        first_line_spaces,
        others_line_spaces, post_content,
        others_line_spaces, res['account']['username'],
        str(datetime.strptime(res['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y%m%d, %H:%M:%S')), res['url'],
        others_line_spaces)

    with open("backup_res_mastodon.json", "a", encoding='UTF-8') as f:
        f.write(str(res) + "\n")

    return Result().success(url, post)


if __name__ == '__main__':
    url = 'https://o3o.ca/@dontworry@toot.mantyke.icu/110733676312713098'
    print(get_mastodon_from_api(url))
