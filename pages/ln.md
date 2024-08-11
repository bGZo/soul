icon:: ⌘
created:: [[20240811]]
description:: 用来为文件创建链接
type:: command/linux

- ## Why
  -
- ## How
  -
- ## What
  - {{iframe https://wangchujiang.com/linux-command/c/ln.html,40vh,iframe-radius}}
  - On [[Windows]] its called [[mklink]]
  -
  - hard link
    - ```shell
      # ln <源文件路径> <链接路径>
      ln recipes.txt newrecipes.txt
      ```
  - soft link
    - ```shell
      # ln -s <源文件路径> <链接路径>
      ln -s recipes.txt newrecipes.txt
      ```
  -
- ## Namespace
  - {{namespace ln}}
- ## ↩ Reference
  -
-
-