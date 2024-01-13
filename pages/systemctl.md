alias:: commands/systemctl
created:: 20231005
icon:: ⌘

- ## Why
- ## How
- ## What
  - <iframe src="https://wangchujiang.com/linux-command/c/systemctl.html" style="height: 400px"></iframe>
    #+BEGIN_CENTER
    via: [Linux 命令搜索引擎 by wangchujiang](https://wangchujiang.com/linux-command/c/systemctl.html)
    #+END_CENTER
  - **systemctl命令** 是系统服务管理器指令，它实际上将 [[service]] 和 [[chkconfig]] 这两个命令组合到一起。
  - ### 查看所有已启动的服务
    - ```shell
      systemctl list-units --type=service # same as `chkconfig --list` 
      ```
  - [systemctl 服务被锁定 masked_systemctl masked-CSDN博客](https://blog.csdn.net/PPlluuttoo/article/details/126781725)
    - ```shell
      systemctl mask sleep.target
      systemctl unmask sleep.target
      ```