import argparse
import logging
import os
import re
import time
from typing import IO

import yaml

logging.getLogger().setLevel(logging.INFO)


def init_regex(configurator: str):
    """
    init regex rule with yaml
    :param configurator: config path
    :return:
    """
    regex_rules_line = []
    regex_rules_all = []

    for root, dirs, files in os.walk(configurator):
        for file in files:
            filename = os.path.join(root, file)
            config = yaml.load(open(filename, 'r', encoding='utf-8'),
                               Loader=yaml.Loader)
            if config['type'] == 'line':
                regex_rules_line.append(config)
            else:
                regex_rules_all.append(config)
    regex_rules_line.sort(key=lambda x: x['sort'], reverse=False)
    regex_rules_all.sort(key=lambda x: x['sort'], reverse=False)

    logging.info("Scan the regex configuration success, regex_rules_line=%s, regex_rules_all=%s",
                 regex_rules_all, regex_rules_line)
    return regex_rules_line, regex_rules_all


def backup_file(backup_file_io: IO):
    backup_folder = 'backup'
    backup_line = backup_file_io.read()
    backup_filename = os.path.join(get_current_path(), backup_folder,
                                   file.name.split('\\')[-1].split('.')[0] + '.' + str(
                                       round(time.time() * 1000)) + '.bak.txt')
    os.makedirs(backup_folder, exist_ok=True)
    output(backup_filename, backup_line)
    logging.info('Backing up file %s', backup_filename)


def proof_readline(file: IO, regex_rules: []) -> []:
    # Readline
    contents = []
    lines = file.readlines()
    for line in lines:
        for reg in regex_rules:
            if re.search(reg['regex'], line):
                line = re.sub(reg['regex'], reg['rules'], line)

        contents.append(line)
    return contents


def proof_all(file: IO | None, content, regex_rules: []) -> str:
    if file is None:
        for reg in regex_rules:
            if re.search(reg['regex'], content):
                content = re.sub(reg['regex'], reg['rules'], content)  # , flags=re.MULTILINE

    else:
        content = file.read()
        for reg in regex_rules:
            if re.search(reg['regex'], content):
                content = re.sub(reg['regex'], reg['rules'], content)  # , flags=re.MULTILINE

    return content


def output(filename: str, line: str):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(line)
    logging.info('Write output file %s success', filename)


def output_lines(filename: str, lines: []):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
    logging.info('Write output file %s success', filename)


def get_current_path():
    return os.path.dirname(os.path.abspath(__file__))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Format weekly collected by rsstt on logseq")
    # parser.add_argument("file", type=argparse.FileType('r', encoding='utf-8'),
    parser.add_argument("file", action="store",
                        help="Add the source file to format")

    parser.add_argument("-o", "--output", action="store"
                        , help="Flag this will be output instead of origin file")

    args = parser.parse_args()

    config_path = os.path.join(get_current_path(), "config")
    regex_rules_line, regex_rules_all = init_regex(config_path)

    if args.file:
        file = open(args.file, 'r', encoding='utf8')

        backup_file(file)
        file.seek(0)

        lines = proof_readline(file, regex_rules_line)

        line = "".join(lines)
        line = proof_all(None, line, regex_rules_all)

        if args.output is not None:
            output(args.output, line)
        else:
            output(args.file, line)
    else:
        logging.error("Please add the source file to format")
