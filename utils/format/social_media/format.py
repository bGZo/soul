# -*- coding: utf-8 -*-
# import os
# import sys
# sys.path.append('../')
# sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import argparse
import re
import yaml
import os
import re

from utils.SocialMedia.get_twitter import get_tweet_from_tweetpik_thread
from utils.SocialMedia.get_mastodon import get_mastodon_from_api
from utils.SocialMedia.get_douban import get_douban_status

from utils.SocialMedia.utils import is_link_match, is_link_done
from utils.SocialMedia.pattern import TWITTER_PATTERN, MASTODON_PATTERN, DOUBAN_PATTERN


def init_regex(configroot):
    reg_rules = []
    for root, dirs, files in os.walk(configroot):
        for file in files:
            filename = os.path.join(root, file)
            config = yaml.load(open(filename, 'r', encoding='utf-8'),
                               Loader=yaml.Loader)
            reg_rules.append(config)
    print("Scan the regex configuration successfully.")
    return reg_rules


def proof(file, reg_rules):
    # 1 一次全部读完;
    # lines = file.read()
    # for reg in reg_rules:
    #   regx   = re.sub(r"\\\\", r"\\", reg['regex'])
    #   rule  = re.sub(r"\\\\", r"\\", reg['rules'])
    #   lines = re.sub(regx, rule, lines)

    contents = []
    lines = file.readlines()
    for line in lines:
        if is_link_done(line):
            print("Found a post have done, check out:{}".format(line))
            contents.append(line)
            continue

        if is_link_match(TWITTER_PATTERN, line):
            rsp = get_tweet_from_tweetpik_thread(line)
            if rsp.code == 200:
                print(rsp.msg)
                contents += rsp.data
                continue
            elif rsp.code == 500:
                print(rsp.msg, rsp.data)


        elif is_link_match(MASTODON_PATTERN, line):
            rsp = get_mastodon_from_api(line)
            if rsp.code == 200:
                print(rsp.msg)
                contents += rsp.data
                continue
            elif rsp.code == 500:
                print(rsp.msg, rsp.data)


        elif is_link_match(DOUBAN_PATTERN, line):
            rsp = get_douban_status(line)
            if rsp.code == 200:
                print(rsp.msg)
                contents += rsp.data
                continue
            elif rsp.code == 500:
                print(rsp.msg, rsp.data)


        else:
            for reg in reg_rules:
                regx = re.sub(r"\\\\", r"\\", reg['regex'])
                rule = re.sub(r"\\\\", r"\\", reg['rules'])
                if re.search(regx, line):
                    line = re.sub(regx, rule, line)
                    continue
        contents.append(line)
    return contents


# def proof_social_media_link(file):

def output_lines(file_name, lines):
    with open(file_name, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Format journals in logseq"
    )
    # parser.add_argument("file", type=argparse.FileType('r', encoding='utf-8'),
    parser.add_argument("file", action="store",
                        help="Add the source file to format")

    parser.add_argument("-o", "--output", action="store"
                        , help="Flag this will be output instead of origin file")

    args = parser.parse_args()
    reg_rules = init_regex(r"config")

    if args.file:
        file = open(args.file, 'r', encoding='utf8')
        lines = proof(file, reg_rules)

    if args.output is not None:
        output_lines(args.output, lines)
    else:
        output_lines(args.file, lines)
