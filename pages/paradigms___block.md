title:: paradigms/block
- 块和子程序是结构化编程的基础
  collapsed:: true
  - 结构化所强调的控制结构是用块来形成的
- ## Syntax
  collapsed:: true
  - ALGOL blocks are delimited by the keywords "`begin`" and "`end`" or equivalent
    - ALGOL 68 uses parentheses.
  - [[lang/programming/system/c]], blocks are delimited by curly braces - "`{`" and "`}`".
  - MS-DOS Batch Lang
    - `()`
  - [[python]]
    - indentation (越位规则)
    - 源于 ISWIM 使用缩进表示块结构
    - Lang -> occam / Genie
  - Lisp s-expressions
    - with a syntactic keyword such as prog or let (as in the Lisp family)
  - 1974 年 Edsger W. Dijkstra 的守卫命令语言中，条件和迭代代码块可使用块保留字反写来终止
    - `if ~ then ~ elif ~ else ~ fi`
    - `case ~ in ~ out ~ esac`
    - `for ~ while ~ do ~ od`
- ## Refs
  collapsed:: true
  - [Block (programming) - Wikipedia](https://en.wikipedia.org/wiki/Block_(programming))