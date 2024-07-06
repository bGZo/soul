#!/usr/bin/python
#-*- coding: utf-8 -*-
import requests
import json

from bs4 import BeautifulSoup
from datetime import datetime

from .template import DOUBAN_TEMPLATE
from .utils import format_link, get_line_spaces
from .result import Result

# from result import Result
# from template import DOUBAN_TEMPLATE
# from utils import format_link,  get_line_spaces

headers = {
    "Host": "www.douban.com",
    "Referer": "http://www.douban.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.0.0"
}


# NOTE: The User-Agent is important!

def get_douban_status(line):
    first_line_spaces, others_line_spaces = get_line_spaces(line)

    url = format_link(line)
    url = url[:-1] + '?_i=foolyoudouban'

    res = requests.get(url, headers=headers)

    try:
        soup = BeautifulSoup(res.text, 'html.parser')
        json_rsp = soup.find('script', type='application/ld+json').text
        data = json.loads(json_rsp, strict=False)
    except Exception as e:
        return Result().failed(line, str(e))

    douban_post = data['headline']
    douban_author = data['author']['name']
    douban_published = str(datetime.strptime(data['datePublished'], '%Y-%m-%dT%H:%M:%S').strftime('%Y%m%d, %H:%M:%S'))
    douban_url = data['@id']

    response = DOUBAN_TEMPLATE.format(
        first_line_spaces,
        others_line_spaces, douban_post,
        others_line_spaces, douban_author, douban_published, douban_url,
        others_line_spaces
    )
    return Result().success(url, response)


if __name__ == '__main__':
    test1 = get_douban_stauts('- https://www.douban.com/people/76395844/status/4364620322/')
    print(test1.data)
