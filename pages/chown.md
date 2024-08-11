icon:: ⌘
created:: [[20240811]]
description:: 用来变更文件或目录的拥有者或所属群组
type:: command/linux

- ## Why
  -
- ## How
  -
- ## What
  - {{iframe https://wangchujiang.com/linux-command/c/chown.html,40vh,iframe-radius}}
  - 所有权转移
    - 所有**者**
      - ```shell
        chown <owner> <file>
        ```
    - 所有**组** (`chgrp`)
      - ```shell
        chown <owner>:<group> <file>
        ```
  -
  - Cases
    - 改变目录的所有权，同时遍历修改其中包含的文件、子目录以及子目录中的文件的所有权
      - ```shell
        chown -R <owner> <file>
        # chown flavio:users test.txt
        ```
- ## Namespace
  - {{namespace chown}}
- ## ↩ Reference
  -
-
-
-
-