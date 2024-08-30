icon:: 🛠
created:: [[20240728]]
document:: commands/line, cli, 命令行
status:: tool/star
tags:: 
type:: tool

- [[terminal]] \#vs [[shell]] \#vs [[bash]]/[[zsh]]
  - terminal 提供一个命令的输入输出环境
    collapsed:: true
    - 普通 Linux 来说，终端的作用是一个**字符（或者模拟字符）的命令交互界面**，实现对计算机的控制。(动态交互以及静态交互)
  - shell 是一个**命令行解释器**，是**linux内核的一个外壳**,负责**外界与linux内核的交互**
    collapsed:: true
    - shell接收命令, 然后将这些命令转化成内核能理解的语言并传给内核, 内核执行命令完成后将结果返回给用户或者应用程序。
    - **当打开一个terminal时，操作系统会将terminal和shell关联起来，当在terminal中输入命令后，shell就负责解释命令。**
  - bash (Bourne Again shell) 是 shell 的一种，是增强的 shell
    - Bourne shell 的扩展, 增加和增强了很多特性, 包含了很多 C shell 和 Korn shell 中的优点，有灵活和强大的编程接口，同时又有很友好的用户界面
      collapsed:: true
      - 命令补全
      - 命令编辑
      - 命令历史表
      - ... 等等
    - bash 与 Bourne shell 完全向后兼容
- angle-brackets
  collapsed:: true
  - `>` -> 输出重定向
    `>>` -> 追加