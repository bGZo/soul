icon:: ⌘
created:: [[20240811]]
description:: 调用并执行指定的命令
type:: command/linux

- ## Why
  -
- ## How
  -
- ## What
  - {{iframe https://wangchujiang.com/linux-command/c/exec.html,40vh,iframe-radius}}
  - 一组函数
    collapsed:: true
    - ![image.png](../assets/image_1649661927239_0.png){:height 796, :width 747}
    - 包含 p 的函数（execvp, execlp）会在 PATH 路径下面寻找程序；
      - 不包含 p 的函数需要输入程序的全路径；
    - 包含 e 的函数（execve, execle）以数组的形式接收环境变量
    - 包含 v 的函数（execv, execvp, execve）以数组的形式接收参数；
    - 包含 l 的函数（execl, execlp, execle）以列表的形式接收参数；
- ## Namespace
  - {{namespace exec}}
- ## ↩ Reference
  -