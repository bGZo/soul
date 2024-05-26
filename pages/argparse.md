icon:: 🐍
tags:: #[[Python Library]]
created:: 20230703
title:: argparse
- ## Why
- ## How
- ## What
  collapsed:: true
  - ### Quick Links for add_argument() via: [argparse — Python 3 documentation](https://docs.python.org/3/library/argparse.html#module-argparse)
    | Name | Description | Values |
    | ---- | ---- | ---- |
    | [action](https://docs.python.org/zh-cn/3/library/argparse.html#action) | Specify how an argument should be handled | 'store', 'store_const', 'store_true',[:br] 'append', 'append_const', 'count', [:br]'help', 'version' |
    | [choices](https://docs.python.org/zh-cn/3/library/argparse.html#choices) | Limit values to a specific set of choices | ['foo', 'bar'], range(1, 10), or [Container](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Container) instance |
    | [const](https://docs.python.org/zh-cn/3/library/argparse.html#const) | Store a constant value |  |
    | [default](https://docs.python.org/zh-cn/3/library/argparse.html#default) | Default value used when an argument [:br]is not provided | Defaults to None |
    | [dest](https://docs.python.org/zh-cn/3/library/argparse.html#dest) | Custom attribute name to be provided |  |
    | [help](https://docs.python.org/zh-cn/3/library/argparse.html#help) | Help message for an argument |  |
    | [metavar](https://docs.python.org/zh-cn/3/library/argparse.html#metavar) | Alternate display name for the argument [:br]as shown in help |  |
    | [nargs](https://docs.python.org/zh-cn/3/library/argparse.html#nargs) | Number of times the argument can be [:br]used | [int](https://docs.python.org/zh-cn/3/library/functions.html#int), '?', '*', or '+' |
    | [required](https://docs.python.org/zh-cn/3/library/argparse.html#required) | Indicate whether an argument is [:br]required or optional | True or False |
    | [**type**](https://docs.python.org/zh-cn/3/library/argparse.html#type) | Automatically convert an argument to [:br]the given type | [int](https://docs.python.org/zh-cn/3/library/functions.html#int), [float](https://docs.python.org/zh-cn/3/library/functions.html#float), argparse.FileType('w')[:br], or callable function |
  -
  - ### Notes
    - positional argument / options
      - ```python
        parser.add_argument('filename')       # positional argument
        parser.add_argument('-c', '--count')   # option that takes a value
        ```
  -
-
-
-