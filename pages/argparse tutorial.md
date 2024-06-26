alias:: argparse/tutorial
tags:: #commandline #[[Python Library]]
document:: [argparse — Parser for command-line options, arguments and sub-commands — Python 3.11.1 documentation](https://docs.python.org/3/library/argparse.html#module-argparse)
description:: [Argparse Tutorial — Python 3.11.1 documentation](https://docs.python.org/3/howto/argparse.html)

- The basics
  - ```python
    import argparse
    parser = argparse.ArgumentParser()
    parser.parse_args()
    ```
  - `--help` argument FREE!
- Combination Positional & Optional arguments
  - ```python
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int,
                        help="display a square of a given number")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="increase output verbosity")
    	# action="store_true"
    	# store_true means if true was specified
        # then set param value but otherwise leave it to None.
        # If default was also specified
        # then param is set to that value instead of leaving it to None.
    args = parser.parse_args()
    answer = args.square**2
    if args.verbose:
        print(f"the square of {args.square} equals {answer}")
    else:
        print(answer)
    ```
- Fix bug and using multi values
  collapsed:: true
  - ```python
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int,
                        help="display a square of a given number")
    parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
                        help="increase output verbosity")
    args = parser.parse_args()
    answer = args.square**2
    if args.verbosity == 2:
        print(f"the square of {args.square} equals {answer}")
    elif args.verbosity == 1:
        print(f"{args.square}^2 == {answer}")
    else:
        print(answer)
    ```
- Another way more than before using flag
  collapsed:: true
  - ```python
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int,
                        help="display the square of a given number")
    parser.add_argument("-v", "--verbosity", action="count",
                        help="increase output verbosity")
    	# count the number of occurrences of specific options
        # 计算特定选项的出现次数
    args = parser.parse_args()
    answer = args.square**2
    if args.verbosity == 2:
        print(f"the square of {args.square} equals {answer}")
    elif args.verbosity == 1:
        print(f"{args.square}^2 == {answer}")
    else:
        print(answer)
    ```
- Fix arguments double bug (-VVV) using value scope
  collapsed:: true
  - ```python
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int,
                        help="display a square of a given number")
    parser.add_argument("-v", "--verbosity", action="count",
                        help="increase output verbosity")
    args = parser.parse_args()
    answer = args.square**2
    # bugfix: replace == with >=
    if args.verbosity >= 2:
        print(f"the square of {args.square} equals {answer}")
    elif args.verbosity >= 1:
        print(f"{args.square}^2 == {answer}")
    else:
        print(answer)
    ```
- FIX arguments none using `defaulf`
  - ```python
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int,
                        help="display a square of a given number")
    parser.add_argument("-v", "--verbosity", action="count", default=0,
                        help="increase output verbosity")
    args = parser.parse_args()
    answer = args.square**2
    if args.verbosity >= 2:
        print(f"the square of {args.square} equals {answer}")
    elif args.verbosity >= 1:
        print(f"{args.square}^2 == {answer}")
    else:
        print(answer)
    ```
- More advanced
  collapsed:: true
  - ```python
    import argparse
    parser = argparse.ArgumentParser(description="calculate X to the power of Y")
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    parser.add_argument("-v", "--verbosity", action="count", default=0)
    args = parser.parse_args()
    answer = args.x**args.y
    if args.verbosity >= 2:
        print(f"{args.x} to the power {args.y} equals {answer}")
    elif args.verbosity >= 1:
        print(f"{args.x}^{args.y} == {answer}")
    else:
        print(answer)
    ```
  - 条件从高到底判断，来展示更多文本；
    collapsed:: true
    Instead uses verbosity level to display *more* text instead
    - ```python
      import argparse
      parser = argparse.ArgumentParser()
      parser.add_argument("x", type=int, help="the base")
      parser.add_argument("y", type=int, help="the exponent")
      parser.add_argument("-v", "--verbosity", action="count", default=0)
      args = parser.parse_args()
      answer = args.x**args.y
      if args.verbosity >= 2:
          print(f"Running '{__file__}'")
      if args.verbosity >= 1:
          print(f"{args.x}^{args.y} == ", end="")
      print(answer)
      ```
  - Conflicting options
    - Lost some functionality for the sake of demonstration (演示)
      ```python
      import argparse
      parser = argparse.ArgumentParser()
      group = parser.add_mutually_exclusive_group()
      group.add_argument("-v", "--verbose", action="store_true")
      group.add_argument("-q", "--quiet", action="store_true")
      parser.add_argument("x", type=int, help="the base")
      parser.add_argument("y", type=int, help="the exponent")
      args = parser.parse_args()
      answer = args.x**args.y
      if args.quiet:
          print(answer)
      elif args.verbose:
          print(f"{args.x} to the power {args.y} equals {answer}")
      else:
          print(f"{args.x}^{args.y} == {answer}")
      ```
- Conclusion
  - The argparse module offers a lot more than shown here. Its docs are quite detailed and thorough, and full of examples. Having gone through this tutorial, you should easily digest them without feeling overwhelmed.
- ```
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
    if args.output:
      output_lines(args.output, lines)
    else:
      output_lines(args.file.name, lines)
  ```