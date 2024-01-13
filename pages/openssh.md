mark:: the premier connectivity tool for remote login with the SSH protocol. It encrypts all traffic to eliminate eavesdropping, connection hijacking, and other attacks. In addition, OpenSSH provides a large suite of secure tunneling capabilities, several authentication methods, and sophisticated configuration options. via: [OpenSSH](https://www.openssh.com/)
tags:: #tools


- ## Suite
  - Remote operations are done using [ssh](https://man.openbsd.org/ssh.1), [scp](https://man.openbsd.org/scp.1), and [sftp](https://man.openbsd.org/sftp.1).
  - Key management with [ssh-add](https://man.openbsd.org/ssh-add.1), [ssh-keysign](https://man.openbsd.org/ssh-keysign.8), [ssh-keyscan](https://man.openbsd.org/ssh-keyscan.1), and [ssh-keygen](https://man.openbsd.org/ssh-keygen.1).
  - The service side consists of [sshd](https://man.openbsd.org/sshd.8), [sftp-server](https://man.openbsd.org/sftp-server.8), and [ssh-agent](https://man.openbsd.org/ssh-agent.1).
- ## Issue
  - DONE Termux (Android) connect to the computer
    collapsed:: true
    - Path
      - `C:\ProgramData\ssh`
      - `C:\User\xxx\.ssh`
    - Windows -> Manage optional features ->Install OpenSSH
    - `ssh usr@ip -p 22`
      - `usr` 是**电脑用户名**! 不是计算机名! 目前不知道中文用户名会发生什么😂
      - `IP`: 内网 IP.
      - `22`: 端口号
      - 要求输入的密码对于我来说是自己的电脑密码. 这里容易和 PIN码 搞混, windows 肯定是设置过一个复杂密码, 后来才有 PIN 码的替代
    - **Reference**
      - [Windows 支持 OpenSSH 了！ - sparkdev - 博客园](https://www.cnblogs.com/sparkdev/p/10166061.html)
      - [Key-based authentication in OpenSSH for Windows | Microsoft Learn](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement)
      - **fix SSH Permission denied** via [How to Fix SSH Failed Permission Denied (publickey,gssapi-keyex,gssapi-with-mic)](https://phoenixnap.com/kb/ssh-permission-denied-publickey) and https://stackoverflow.com/questions/1556056/permission-denied-publickey-keyboard-interactive
      - [Remote Access - Termux Wiki](https://wiki.termux.com/wiki/Remote_Access#OpenSSH)
  - DONE 延长会话
    collapsed:: true
    - `ClientAliveInterval 30` 
      `ClientAliveCountMax 3`
      via https://15tar.com/linux/2017/07/31/ssh-session-timeout.html
  - DONE 关闭终端?
    collapsed:: true
    - 继续执行 `ssh -f`
      - *nix via [it-swarm](https://www.it-swarm.cn/zh/ssh/%E5%A6%82%E4%BD%95%E5%9C%A8%E7%BB%93%E6%9D%9Fssh%E4%BC%9A%E8%AF%9D%E5%90%8E%E4%BF%9D%E6%8C%81%E8%BF%9B%E7%A8%8B%E8%BF%90%E8%A1%8C%EF%BC%9F/957254945/)
  - 挂断程序
  - Run in background
    - On Windows
      collapsed:: true
      - ```powershell
        Start-Process
        Start Job { & C:\Full\Path\To\my.exe }
        ```
      - via: [What is the equivalent of 'nohup' in linux PowerShell? - Stack Overflow](https://stackoverflow.com/questions/64707869/what-is-the-equivalent-of-nohup-in-linux-powershell)
        [Start-Process (Microsoft.PowerShell.Management) - PowerShell | Microsoft Learn](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/start-process)
        [What is the equivalent of 'nohup' in PowerShell? - Stack Overflow](https://stackoverflow.com/questions/19321903/what-is-the-equivalent-of-nohup-in-powershell)
        [Start-Job (Microsoft.PowerShell.Core) - PowerShell | Microsoft Learn](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/start-job)
      - ```cmd
        start
        ```
        via: [What's the nohup on Windows? - Stack Overflow](https://stackoverflow.com/questions/3382082/whats-the-nohup-on-windows)
    - On Linux
      - `tmux`
      - `nohup`
      - `bg`
-