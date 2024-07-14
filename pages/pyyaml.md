icon:: 🐍
tags:: #[[Python Library]], #yaml
created:: [[20230718]]
- ## Why
- ## How [pyyaml.org/wiki/PyYAMLDocumentation](https://pyyaml.org/wiki/PyYAMLDocumentation)
  - ### Installation
    collapsed:: true
    - ```
      pip install --trusted-host pypi.tuna.tsinghua.edu.cn -i https://pypi.tuna.tsinghua.edu.cn/simple pyyaml
      ```
  - ### Frequently Asked Questions
    collapsed:: true
    - Dictionaries without nested collections are not dumped correctly
      **没有嵌套集合的字典无法正确转储**
  - ### Python 3 support
  - ### Tutorial
    - Loading YAML 加载 YAML 文件
      - #+BEGIN_WARNING
        **It is not safe to call `yaml.load` with any data received from an untrusted source! `yaml.load` is as powerful as `pickle.load` and so may call any Python function.** Check the `yaml.safe_load` function though.
        #+END_WARNING
      - The function `yaml.load` converts a YAML document to a Python object.
        函数 yaml.load 将YAML文档转换为Python对象。
      -
      - Params
        - String
        - File stream
      - Function
        - load
        - load_all
      - Result (Python Object)
        - Dict
        - Class Object
      -
      - `yaml.load` detects the encoding by checking the *BOM* (byte order mark) sequence at the beginning of the string/file. If no *BOM* is present, the *utf-8* encoding is assumed.
    - Dumping YAML
    - Constructors, representers, resolvers
  - ### YAML syntax
    - A good introduction to the YAML syntax is [Chapter 2 of the YAML specification](http://yaml.org/spec/1.1/#id857168).
    - You may also check [the YAML cookbook](https://yaml.org/YAML_for_ruby.html). Note that it is focused on a Ruby implementation and uses the old YAML 1.0 syntax.
    - #### Documents
      - An empty stream contains no documents.
      - Documents are separated with `---`.
      - Documents may optionally end with `...`.
      - A single document may or may not be marked with `---`.
    - #### Block sequences
    -
    - #### Block mappings
    - #### Flow collections
    - #### Scalars
    - #### Aliases
    - #### Tags
  - ## YAML tags and Python types
    - String conversion (Python 2 only)
    - String conversion (Python 3 only)
    - Names and modules
    - Objects
  - ## Reference
    - The yaml package
    - Mark
    - YAMLError
    - Tokens
    - Events
    - Nodes
    - Loader
    - Dumper
    - YAMLObject
  - Deviations from the specification
  -
  -
- ## What
  - [PyYAML · PyPI](https://pypi.org/project/PyYAML/)
    collapsed:: true
    - [pyyaml.org/wiki/PyYAMLDocumentation](https://pyyaml.org/wiki/PyYAMLDocumentation)
      collapsed:: true
      - [[draws/2023-06-14-21-57-38.excalidraw]]
-
-
-