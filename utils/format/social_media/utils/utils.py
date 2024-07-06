import re

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
