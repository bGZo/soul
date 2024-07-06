import re


##################
# format content #
##################
def format_link(link):
    link = re.sub(r" ", r"", link)
    link = re.sub(r"-", r"", link)

    link = re.sub(r"\?s=\d+&t=[-\w]+\n*", r"", link)
    link = re.sub(r"\?t=[-\w]+&s=\d+\n*", r"", link)
    link = re.sub(r"\?s=\d+\n*", r"", link)

    link = re.sub(r"\[(.*?)\]\((.*?)\)", r"\2", link)
    link = re.sub(r"/\?_i=.*\n", r"/", link)
    link = re.sub(r".*?http", r"http", link)
    return link


def format_response(response):
    response = re.sub(r'\n', r' ', response)

    response = re.sub(r'\\"', r'\'', response)
    return response


#################
# Format logseq #
#################
def get_line_spaces(line):
    count = 0
    for char in line:
        if char == ' ':
            count += 1
        elif char == '-':
            break

    first_line_spaces = ""
    others_line_spaces = "  "
    for i in range(count):
        first_line_spaces += " "
        others_line_spaces += " "

    return first_line_spaces, others_line_spaces


##############
# Judge Link #
##############
def is_link_match(pattern, link):
    name = list(dict(pattern=pattern).keys())[0]
    # via: https://www.zhihu.com/question/42768955
    if re.search(pattern, link):
        print("Seem like a {} link: {}".format(name, link))
        return True
    else:
        return False


##############
# Judge Done #
##############
def is_link_done(line):
    if re.search(r"\d{8}, \d{2}:\d{2}:\d{2}", line):
        return True
    else:
        return False


########
# Test #
########
def test_output(lines):
    with open("test_file.txt", 'w', encoding='UTF-8') as f:
        for line in lines:
            f.write(line)
