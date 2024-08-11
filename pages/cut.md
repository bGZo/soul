icon:: ⌘
created:: [[20240811]]
description:: 连接文件并打印到标准输出设备上
type:: command/linux

- ## Why
  -
- ## How
  - 拿到文件的后缀
    - ```shell
      basename $file | rev | cut -d . -f 1- | rev
      ```
- ## What
  - {{iframe https://wangchujiang.com/linux-command/c/cut.html,40vh,iframe-radius}}
  -
- ## Namespace
  - {{namespace cut}}
- ## ↩ Reference
  -