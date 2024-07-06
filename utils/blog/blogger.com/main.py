import logging

import lxml.etree
import pyperclip
import requests

import contant

logging.getLogger().setLevel(logging.INFO)


def get_file_by_url(url: str) -> str:
    """
    :param url: website url
    :return: filename stored on local
    """
    req = requests.get(url, headers=contant.HEADERS)
    if req.status_code == 200:
        filename = url.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(req.content)
        logging.info('write file %s success.',url.split('/')[-1])
        return filename
    else:
        logging.error('write file %s failed.', url.split('/')[-1])
        return ''


def is_xml_file(filename: str) -> bool:
    """
    todo: lxml seem like not have this function
    :param filename:
    :return:
    """
    return filename.endswith('.xml')


def get_url_from_xml_file(filename) -> []:
    """
    parse filename and get urls from xml file
    :param filename:
    :return:
    """
    with open(filename, 'r') as f:
        root = lxml.etree.fromstring(f.read().encode('utf-8'))
        # NOTE: encode otherwise, ValueError: Unicode strings with encoding declaration are not supported. Please use
        # bytes input or XML fragments without declaration. logging.info(lxml.etree.tostring(root))

        namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        loc_elements = root.xpath('//ns:loc', namespaces=namespaces)

        return [element.text for element in loc_elements]


if __name__ == '__main__':
    root = 'https://www.hecaitou.info'
    url = root + '/sitemap.xml'
    filename = get_file_by_url(url)
    # https://www.hecaitou.info/sitemap.xml
    if filename == '':
        logging.error('bad url: %s, please check your internet, or try another url! ', url)

    urls = get_url_from_xml_file(filename)

    cli_content = ''
    for url in urls:
        cli_content += '- ' + url + '\n'

    pyperclip.copy(cli_content)
    # 从剪切板获取文本
    clipboard_content = pyperclip.paste()
    logging.info('had written in clip: %s', clipboard_content)