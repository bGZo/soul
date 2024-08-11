icon:: ⌘
created:: [[20231005]]
description:: 系统服务管理器指令
type:: command/linux

- ## Why
  -
- ## How
  -
- ## What
  - {{iframe https://wangchujiang.com/linux-command/c/systemctl.html,40vh,iframe-radius}}
  - **systemctl命令** 是系统服务管理器指令，它实际上将 [[service]] 和 [[chkconfig]] 这两个命令组合到一起。
  - ### 查看所有已启动的服务
    - ```shell
      systemctl list-units --type=service # same as `chkconfig --list`
      ```
  - [systemctl 服务被锁定 masked_systemctl masked-CSDN博客](https://blog.csdn.net/PPlluuttoo/article/details/126781725)
    - ```shell
      systemctl mask sleep.target
      systemctl unmask sleep.target
      ```
- ## Namespace
  - {{namespace systemctl}}
- ## ↩ Reference
  -