icon:: ⌘
created:: [[20240811]]
description:: 给其他命令传递参数的一个过滤器 
type:: command/linux

- ## Why
  -
- ## How
  -
- ## What
  - {{iframe https://wangchujiang.com/linux-command/c/xargs.html,40vh,iframe-radius}}
  - 将标准输入的数据转换成命令的参数
    - 将一条命令的输出，用作另一条命令的输入
  -
  - ```shell
    command1 | xargs command2
    # 管道符（`|`）将输出传递给 `xargs`
    # 它将负责运行 `command2` 命令，使用 `command1` 的输出作为参数
    ```
  -
  - Options
    collapsed:: true
    - `-p`
      - 操作提醒确认
    - `-n`
      - 令 `xargs` 每次执行若干个迭代
      - 用 `-n1` 告诉 `xargs` 一次执行一个迭代
    - `-I`
      - 将输出内容放入占位符，之后你可以用来做各种事
  -
  - Cases
    - 删除文件中对应名字的包
      collapsed:: true
      - ```shell
        cat todelete.txt | xargs rm
        ```
        - 工作方式
          - `xargs` 会运行 `rm` 2次，为 `cat` 返回的每一行运行一次
    - 同时运行多个命令
      collapsed:: true
      - ```shell
        command1 | xargs -I % /bin/bash -c 'command2 %; command3 %'
        ```
        - 你可以将上方的 % 符号换成其他任何东西——它只是个占位符变量
  -
- ## Namespace
  - {{namespace xargs}}
- ## ↩ Reference
  -