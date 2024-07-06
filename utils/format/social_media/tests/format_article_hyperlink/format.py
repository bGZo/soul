import argparse
import re

def proof(file):
  lines = file.readlines()
  reg_lines = []
  for line in lines:
    line = re.sub(r'([\u4e00-\u9fa5])\, ([\u4e00-\u9fa5])', '\g<1>，\g<2>', line)

    # Logseq
    line = re.sub(r'  \n', '\n', line)

    line = re.sub(r'( )(https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)([;, ])*', '\g<1><\g<2>>\g<3>\g<4>', line)
    line = re.sub(r'^(https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)', '<\g<1>>', line)


    reg_lines.append(line)
  return reg_lines

def output_lines(file_name, lines):
  # NOTE: <_io.TextIOWrapper name='input.md' mode='r' encoding='UTF-8'>
  with open(file_name, 'w' ) as f:
    for line in lines:
      f.write(line)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(
    description="Format text where copy as in logseq"
    )
  parser.add_argument("file", type=argparse.FileType('r', encoding='UTF-8'),
    help="Add the source file to format")
  #NOTE: open don't support GBK open
    # UnicodeDecodeError: 'gbk' codec can't decode byte 0x9d in position 8:
    # illegal multibyte sequence 
  parser.add_argument("-o", "--output", action="store"
  ,help = "Flag this will be output instead of origin file")

  args = parser.parse_args()

  if args.file:
    lines = proof(args.file)

  if args.output is not None:
    output_lines(args.output, lines)
  else:
    output_lines(args.file.name, lines)