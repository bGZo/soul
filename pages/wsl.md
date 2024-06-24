title:: wsl
alias:: Windows Subsystem For Linux
tags:: #Windows #Linux #-nix #tools #github #microsoft
github:: https://github.com/microsoft/WSL
created:: [[202104]]
![](https://img.shields.io/github/stars/microsoft/WSL)

- ## How
  - DONE WSL GUI
    collapsed:: true
    - Unstable Version: https://docs.microsoft.com/zh-cn/windows/wsl/tutorials/gui-apps
    - Windows X-server Version: https://blog.meathill.com/tools/install-wsl2-on-windows-10-and-config-gui-for-applications.html
  - DONE 重回 Windows
    collapsed:: true
    - 过去一年将 `Ubuntu` 作为自己的主力机, 期间滚更+修`BUGS`, 并收集并撰写了 维修日志. 在一次无法正常启动 `Oracle` 的经历后我正是卸载双系统的 `Ubuntu`, 开始用上了 `Windows Subsystem WSL2`, 一切仿佛回到了折腾的起点, 我不知道要说什么, 内心又不断地翻涌, 但工具就是工具, 不应该多说什么.
    - 工作的重心逐渐转移回 Windows, 除了命令行让人难以忍受的难用之外并没有什么不合心意的地方, 所以我又踏上了美化 Windows 命令行的道路. 一切都是源于被 *nix 惯坏的习惯.
    - ```shell
      # Maybe u should install scoop first from https://github.com/lukesampson/scoop
      # Dowmload powershell 7.x instead of default 5.x form
      # https://github.com/PowerShell/PowerShell/releases, then run the powershell 7.x
      Install-Module posh-git -Scope CurrentUser
      Install-Module oh-my-posh -Scope CurrentUser
      # If u are in China, please look up the proxy using the powershell or get help
      # from my gist: https://gist.github.com/82a76ecbebf81b556a1d20a91a6bd21a
      # Edit the Environment config
      $PROFILE
      if (!(Test-Path -Path $PROFILE )) { New-Item -Type File -Path $PROFILE -Force }
      notepad $PROFILE # code $PROFILE
      # U could input the path to freash the powershell
      # Add the config like this:
      Import-Module posh-git
      Import-Module oh-my-posh
      Set-PoshPrompt Paradox # could see more prompts from https://ohmyposh.dev/docs/themes
      # Notice its not "Set-Theme" from
      # https://github.com/microsoft/terminal/issues/9237#issuecomment-798913706
      # More color-schemes:
      # https://docs.microsoft.com/zh-cn/windows/terminal/customize-settings/color-schemes
      # Everything maybe all right but the frosted glass (blur background)
      # Edit your terminal profiles and add following json stmt. If its doesn't make sence,
      # Turn on your system -> presonalization settings -> color : Transparency effects. from
      # https://docs.microsoft.com/zh-cn/windows/terminal/custom-terminal-gallery/frosted-glass-theme
      "useAcrylic": true,
      "acrylicOpacity": 0.7,
      ```
- ## What
  - Open in `explore.exe` #PowerShell #Windows
    collapsed:: true
    - ```bash
      cd \\wsl$\Ubuntu
      ```
  - Difference 1.0 & 2.0
    collapsed:: true
    - | Feature(via: [mircosoft](https://docs.microsoft.com/en-us/windows/wsl/compare-versions)) | WSL 1 | WSL 2 |
      | :----------------------------------------------------------- | :---- | :---- |
      | Integration between Windows and Linux                        | ✅     | ✅     |
      | Fast boot times                                              | ✅     | ✅     |
      | Small resource foot print compared to traditional Virtual Machines | ✅     | ✅     |
      | Runs with current versions of VMware and VirtualBox          | ✅     | ✅     |
      | Managed VM                                                   | ❌     | ✅     |
      | Full Linux Kernel                                            | ❌     | ✅     |
      | Full system call compatibility                               | ❌     | ✅     |
      | Performance across OS file systems                           | ✅     | ❌     |
    - via: [WSL 和 WSL2 简单对比 - V2EX](https://v2ex.com/t/587642)
    - [🚀 为什么在 WSL 下项目的编译/运行/git 等等和 IO 相关的操作貌似很慢？ · Issue #17 · spencerwooo/dowww](https://github.com/spencerwooo/dowww/issues/17#issuecomment-457128479)
    - [你不需要花哨的命令提示符 - 知乎](https://zhuanlan.zhihu.com/p/51008087)