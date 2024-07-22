id:: 6254e947-b746-4586-8242-b17e9066ec55
icon:: ⊞
tags:: system

- ## Why
- ## How
  - ~~[BitDock比特工具栏-官方社区 - 首页](http://www.bitdock.cn/bbs/forum.php)~~ #deprecated #beautify
  - ### Shortcuts #Quickref
    - `Windows`
      collapsed:: true
      - |     Operation      |                      Effects                       |
        | :----------------: | :------------------------------------------------: |
        |        Win+E        |         打开资源管理器         |
        |       Win+t        |                   循环切换任务栏                   |
        |     Win+Ctrl+D     |                  创建虚拟Desktop                   |
        |        Win+Q        |              搜索              |
        |  Win + Ctrl + F4   |                  关闭虚拟Desktop                   |
        |        Win+R        |             对话框             |
        | Win + Ctrl + 左/右 |                左右切换虚拟Desktop                 |
        |        Win+X        |   “Windows移动中心”设置面板    |
        |       Win+F4       |                      关闭窗口                      |
        |       Win+m        |               最小化窗口（全部窗口）               |
        |   Win+Shift+M   |     还原窗口最小化（全部）     |
    - `Ctrl`
      collapsed:: true
      - |     Operation      |                      Effects                       |
        |       ctrl+w       |            关闭浏览器当前页（我的电脑）            |
        |       ctrl+t       |                    打开新标签页                    |
        |   ctrl+alt+delete   |         打开任务管理器         |
        |    ctrl+shift+t    |                恢复关闭的浏览器页面                |
        |      ctrl +      |                      放大页面                      |
        |       ctrl -       |                      缩小页面                      |
    - `Alt`
      collapsed:: true
      - |     Operation      |                      Effects                       |
        |       alt+F4        |            关闭窗口            |
        |      alt+enter      |        查看选中文件属性        |
        | alt+前进/后退方向键 |       浏览器页面后退前进       |
        |        alt+d        |        焦点固定到地址栏        |
        | alt+shief+num Lock |                   用键盘控制鼠标                   |
        |     alt+space+n     | 单个窗口最小化（配合Dock使用） |
    - `F Keyboard`
      collapsed:: true
      - |     Operation      |                      Effects                       |
        |         F1         |         显示当前程序或者windows的帮助内容          |
        |         F2          |  如果选中文件的话，进行重命名  |
        |         F3         |                        查找                        |
        |         F5          |         浏览器页面刷新         |
        |         F6         | 使用浏览器时，地址栏获得焦点（即光标移到了地址栏） |
        |         F11         |           浏览器全屏           |
        |        F12         |              浏览器审查元素/调试界面               |
        |        prtsc        |              截屏              |
- ## What
  - DONE Loction
    collapsed:: true
    - 鉴于Windows家庭版无法更改的中文环境, 特此备注.
    - 斜杠转换: 发现 Windows 的 `/` 和 `\` 都可以表示目录结构(主`\`, 文件管理及PS).
    - 开始菜单: `c:\Users\xxx\AppData\Roaming/Microsoft/Windows/Start Menu/Programs`
  - DONE NTFS & EXT* Film Rename
    collapsed:: true
    - **NTFS**(255) : `< > / \ | :  * ? 、` 不可命名,  大小写不敏感.
    - **EXT\***(256) : `/` 不可命名,  避免使用(歧义) `* ? > < ; & ! [ ] | \ ' " ``（ ） { } + -`. 大小写敏感
  - DONE 系统服务
    collapsed:: true
    - RuntimeBroker: RuntimeBroker.exe进程Win8或者Win8.1系统中才会出现的进程，是一个重要的系统核心进程，是Win8或者Win8.1用来进行Metro App权限管理的一个进程。该程序正常情况下位于C:\Windows\System32目录下，大小一般为32.7KB。用来进行开始屏幕磁贴与桌面的后台交互，如果没有运行任何磁贴程序应用的话，可能不会出现的进程中。一般占用内存不会超过3M，如果系统出现该进程内存占用太高，应该是此贴应用没有彻底关闭(特别是Win8.1)。
    - Diagnostic Policy Service
      collapsed:: true
      - **[Reasult]：**任务管理的历史记录无法使用
    - Microsoft Compatibility Telemetry
      collapsed:: true
      - **[loc]: **我的电脑 -> 管理计算机 -> Application组包—> 关闭
    - Host process for setting synchronization
      collapsed:: true
      - **[Affect]：**同步Win的电脑设置
    - Window Update
      collapsed:: true
      - **[Reasult]：** Mirco的软件商店会无法获取应用。
      - **定期检查更新服务。**每次重启电脑或者超过两天没有关机时，打开“服务”，并检查“Windows Update”状态，确保它仍然是禁用的。虽然Windows Update服务不会经常重启，但偶尔会重新启动。
      - 如果在“Windows Update”标题右侧看到“禁用”，那么Windows Update仍然是禁用的。
      - 如果在“Windows Update”标题右侧看到除“禁用”以外的其他内容，再次禁用Windows Update。
      - **Win10家庭版 使用组策略：** 保存为 CMD 或 BAT 以管理员模式运行，无报错情况下 Win+R 键入 gpedit.msc 打开组策略管理。
           ```cmd
           @echo off
           pushd "%~dp0"
           dir /b C:\Windows\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientExtensions-Package~3*.mum >List.txt
           dir /b C:\Windows\servicing\Packages\Microsoft-Windows-GroupPolicy-ClientTools-Package~3*.mum >>List.txt
           for /f %%i in ('findstr /i . List.txt 2^>nul') do dism /online /norestart /add-package:"C:\Windows\servicing\Packages\%%i"
           pause
           ```
    - Host process for setting synchronization
      collapsed:: true
      - [Affect]：**Win10的系统设置同步选项，可在设置-> 账户 ->同步里选择关闭
    - WMI Provider Host
      collapsed:: true
      - **[Affect]：**某些应用调用这个服务，一般几秒的事，持续占后台就有问题了。
      - **[loc]：**[参考网上的方法-知乎](https://www.zhihu.com/question/58459318)，个人不喜动防火墙（svhost），关闭了HP Audio Switch后，找到是由于小米互传这个软件占用后台 -> 更新 ，退出后发现即使运行也不用CPU了。
    - Windows Modules Installer Worker
      collapsed:: true
      - **[Affect]：**启用Windows更新和可选组件的安装。
    - Window恶意软件删除工具
      collapsed:: true
      - **[Affect]：**Windows Update 提供的该工具版本每月会在您的计算机后台运行一次。 如果找到感染，该工具将在您下一次启动计算机时显示一份状态报告。 如果您想要每月运行此工具多次，可以运行此网页提供的版本或者使用恶意软件删除工具网站上的版本。
    - HP System Info HSA Service
      collapsed:: true
      - **[Affect]：**
    - Xtuservice
      collapsed:: true
      - **[Affect]：**处理器进行超频 降频操作的控制程序
    - IP Helper
      collapsed:: true
      - **[Affect]：**IPV6 -> IPV4
    - SysinfoCap
      collapsed:: true
      - **[Loc]**：HPSysInfoCap(HP System Info HSA Service)
      - **[Affect]：**获取系统的相关信息，推测是风扇的驱动之类; 他会连带着下面的服务停止，我将他们设置了手动启动。
      - **[HPNetworkCap]** (HP Network HSA Service)、**[HPAppHelperCap]** (HP App Helper HSA Service)
      - 其他HP(系统品牌)的服务还有：
           ```
           HP Analytics service
           HP CASL Framework Service
           HP Comm Recovery
           HP Omen HSA Service
           ```
    - Software Reporter Tool
      collapsed:: true
      - **[Loc] :** Cmd下：——对应版本号里的Software Reporter Tool！
          ```powershell
          %localappdata%\Google\Chrome\User Data\SwReporter
          ```
          **[方法]：**“高级” -> “禁用继承” -> "从此对象中删除所有继承的权限".保证没有用户组可以访问SwReporter文件夹并启动Software Reporter Tool了。
        + Bluetooth Handsfree Service：没有蓝牙的用户可以关闭
        + Fax：计算机或网络上的可用传真资源发送和接收传真
        + Workstation：创建和维护到远程服务的客户端网络连接如果服务停止
        + Ssdp Discovery：启动家庭网络上的upnp设备自动发现具有upnp的设备还不多
        + Smart Card：管理计算机对智能卡的读取访问基本上用不上，没有安装UPS的用户可以禁用
        + Print Spooler：将文件加载到内存中以便稍后打印，如果没装打印机，可以禁止该服务
        + Application LayerGateway  Service：为Internet连接共享和Internet连接防火墙提供第三方协议插件的支持如果你没有启用Internet连接共享或Windows XP的内置防火墙，Windows必须禁止的10项服务。则可将其禁止
        + TCP/IP NetBIOS Helper：NetBIOS在Win 9X下就经常有人用它来进行攻击，然后将此数据写入日志或触发警报为了防止被远程计算机搜索数据，否则一定要禁止它
        + Performance Logs  Alerts：性能日志和警报根据预配置的计划参数从本地或远程计算机收集性能数据，然后将该数据写入日志或触发警报。如果停止此服务，将不收集性能信息。如果禁用此服务，则明确依赖它的所有服务将无法启动。
        + RemoteRegistry：使远程用户能修改此计算机上的注册表设置。如果此服务被终止，只有此计算机上的用户才能修改注册表。如果此服务被禁用，任何依赖它的服务将无法启动。
        + 组策略把windows defender关掉：随机高磁盘io 关掉自动维护，如果方便的话关掉自动更新，改成定时更新：随机出现高磁盘io superprefetch，这个服务*有可能*在开机时出现高磁盘io，罕见开机高内存占用，通常会在开机几分钟之后回到正常值 windows search，这个服务*有可能*随机出现高磁盘io
        + [解决win10系统CPU占用过高](https://blog.csdn.net/sky__god/article/details/77914698)
  - DONE **让右键菜单收紧**: 修改注册表
    collapsed:: true
    - Windows 10适应多种设备 -> 小尺寸移动触摸设备 + PC或其他大屏显示设备
    - 定位到`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\FlightedFeatures`项，在右侧窗格新建DWORD（32位）值; 然后将其命名为`ImmersiveContextMenu`，数值数据保持默认的`0`，点击“确定”。退出注册表编辑器，重启文件资源管理器，从中查看右键菜单，或到桌面上右键查看，会发现右键菜单比原来紧凑了.
    - **注册表修改具有一定的风险，因此建议在修改前先备份注册表**。
    - 由于右键菜单在不同位置的项目均有所不同，而又不局限于如上介绍的3个位置，因此如果要修改其他部位的右键菜单项目，还可以借助于一款专用的右键菜单定制软件RightMenuMgr来实现。在该软件窗口中，给出更多类别的右键菜单项目，只需选择对相应的项目执行去留优化即可。(Glary  Utilities)
  - DONE 取消开机密码
    collapsed:: true
    - 1. 设置密码就什么都不填.
      2. `Ctrl+Alt+Del`下更改密码, 重复1.
  - DONE `文件大小` 与 `占用内存` 不相同
  - DONE Net端口占用
    collapsed:: true
    - 1. 开机的部分时间内会短暂的占用部分端口，所以请稍后重试。
      2. Cmd 下命令：
       ```shell
       netstat -ano|findstr "XXX" #端口号，或者下面的命令
       netstat -aon|findstr :XXX|findstr LISTEN（netstat -ano | findstr “XXX” ）
       ```
      3. **[荐]**: 服务 -> 手动启动
  - DONE 投屏无法使用
    collapsed:: true
    - > Miracast是由Wi-Fi联盟于2012年所制定，以Wi-Fi直连（Wi-Fi Direct）为基础的无线显示标准。支持此标准的3C设备(如智能手机、电视、投影、电脑等)可透过无线方式分享视频画面，也就是说在此技术下，手机可以在不借助任何连接线的情况下实现与电视、电脑等大屏设备的画面投屏。
      资料可知，通过和手机间的投屏是使用无线网卡来实现的，所以，如果你的电脑有无线局域网（Wi-Fi）功能，你就可以使用投屏功能。
      1. **window+R**快捷键运行**dxdiag.exe** -> 保存所有信息 -> `Miracast`是否可用?(Available,withHDCP)
      2. 我的问题定位到**Microsoft Wi-Fi Direct Virtual Adapter**被禁用
      3. **window按钮->设备管理器->网络适配器**，找到你的网卡打开就OK
      4. 其他参考： **SSDP服务和WMPNetworkSvc服务** 是否被启用或者防火墙是否开启
  - DONE 默认应用误设
    collapsed:: true
    - ![154kEn.png](https://s2.ax1x.com/2020/02/10/154kEn.png)
      1. 用文本打开一个打不开的文件，会报错然后就完美了。
       1. **[推荐]**新建文本A — > 随便起个后缀 -> 用A选择默认打开误开的应用 -> 删掉A
      2. 用可卸载的软件打开一遍，然后卸载这个软件。
      3. 批处理代码，粘过来研究
       ```visual basic
       @echo off
       setlocal enabledelayedexpansion
       set "ext=%~x1"
       :loop
       if mark:: d ext set "ext=!ext:"=!"
       if mark:: d ext goto ok
       echo 如果你不知道文件的扩展名，关闭批处理然后把文件拖到批处理文件的图标上。
       set /p "v=请输入扩展名（如txt）然后回车："
       for /f "delims=" %%i in (".!v!") do set "ext=%%~xi"
       goto loop
       :ok
       echo 扩展名：!ext!
       pause
       reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\FileExts\!ext!"  /f
       reg query "HKCR\!ext!" /ve|find /i "!ext:~1!_auto_file">nul
       if not errorlevel 1 (
       reg delete "HKCR\!ext!" /ve /f
       reg delete "HKCR\!ext:~1!_auto_file" /f
       )
       taskkill /im explorer.exe /f
       start %windir%\explorer.exe
       pause
       goto :eo
       ```
  - DONE 电量持续显示在 92%
    collapsed:: true
    - 1. 控制面板(大图标)>**电源选项**>更改计划设置>更改高级电源设置>电池
      2. 说来有趣，嫌网上的方法太麻烦，直接选择了恢复默认，但是要**重新开机后**才可以回到100%。
  - DONE [谷歌浏览器Software Reporter Tool长时间占用CPU解决办法](https://www.cnblogs.com/ShaYeBlog/p/10224349.html)
    collapsed:: true
    - > 一个Chrome清理工具,用于清理谷歌浏览器中不必要或恶意的扩展，应用程序，劫持开始页面等等。当你安装Chrome时，Software_reporter_tool.exe也j就会被下载在SwReporter文件夹下的Chrome应用数据文件夹中。
      1. 默认它位于以下目录`C:\Users\[YourName]\AppData\Local\Google\Chrome\User Data\SwReporter\[版本]\software_reporter_tool.exe`
      2. 我们还可以通过`win+r`键打开运行命令窗口并输入以下命令快速找到它`%localappdata%\Google\Chrome\User Data\SwReporter`
      3. 右键单击software_reporter_tool.exe选择属性
      4. 转到“安全”选项卡
      5. 点击“高级”
      6. 点击“禁用继承”
      7. 选择"从此对象中删除所有继承的权限",之后一路点击“确定”“确定”。
  - DONE 音量的无限增高
    collapsed:: true
    - 播放器正常播放，为了喇叭的安全，所有的播放器一般只使用了喇叭【70%～75%】的功率，所以这样的声音没有开完，这种'功率不会损伤喇叭【这也是手机出厂的时候，设置过】
      而[酷狗](https://www.baidu.com/s?wd=酷狗&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)就是增加了个，打破这个播放功率，长时间使用，会对播放器造成损伤
  - DONE Bluetooth APTX Support
    collapsed:: true
    - 1. `设备管理器` -> 网卡(蓝牙)型号(AC9560).
      2. Google Search
       1. [英特尔9260 9560 9462 8265 8260 7265 3165蓝牙驱动程序](https://www.dell.com/support/home/zh-cn/drivers/driversdetails?driverid=2dfn9)
       2. [Intel 7265/3165/7260/3160 Bluetooth Audio Application (WBS/APTX)](https://www.dell.com/support/home/zh-cn/drivers/DriversDetails?driverId=90WTD)
      另外值得一提的是, 对耳机开启/关闭ATPX编码的位置在:`控制面板\声音\声卡设置\选择对应耳机`
  - DONE Cat serial number / 查看序列号
    collapsed:: true
    - ```powershell
      (Get-WmiObject -query 'select * from SoftwareLicensingService').OA3xOriginalProductKey
      ```
  - DONE Buy windows evalcenter
    collapsed:: true
    - Needs
      collapsed:: true
      - 纯英文的开发环境 #English
    - [坑] Windows 的绑定方式和 Office 的方式不同
      collapsed:: true
      - Windows 绑定主板 与 CPU, 在微软帐号里面无法查到, 但在 “设置”--“激活” 显示已经与帐号关联数字许可证激活
      - 大体有以下几个版本 
        collapsed:: true
        - OEM / Original Equipment Manufacturer / 原始设备制造商
        - COEM / Certificate Original Equipment Manufactures / 原始设备制造商证书
          collapsed:: true
          - 独立盒包装 (内含光盘).
          - COEM 与 OEM 其实是一样的东西
            collapsed:: true
            - OEM 是微软卖给大厂;
            - COEM 是面向店老板. 均不支持设备迁移
        - ==FPP / Full Packaged Product== / 零售版
          collapsed:: true
          - 从软件零售商处购买到的软件产品，可以设备迁移一次
          - Way
            collapsed:: true
            - 从激活的 [疑难故障] 进去
            - 选择我最近更改了设备硬件
            - 等待片刻，微软会列出当前微软账户层级关联激活的电脑
            - 选中，点击对应的激活，即可自行迁移授权。
            - via: [在更换硬件后重新激活 Windows - Microsoft 支持](https://support.microsoft.com/zh-cn/windows/%E5%9C%A8%E6%9B%B4%E6%8D%A2%E7%A1%AC%E4%BB%B6%E5%90%8E%E9%87%8D%E6%96%B0%E6%BF%80%E6%B4%BB-windows-2c0e962a-f04c-145b-6ead-fb3fc72b6665)
              collapsed:: true
              - [淘宝京东买的Windows/office秘钥是正版吗？ - 知乎](https://zhuanlan.zhihu.com/p/338805607)
              - [Win 10 正版专业版实际大概什么价？ - V2EX](https://www.v2ex.com/t/352588)
    - [No Split] 分盘在于文件存续, 但Win10鲜有崩坏, 希望可以学 `*nux` 那样只有一个系统盘 (当然需要一个盘备份重要资料).
  - DONE Add open terminal in right click menus #regedit
    collapsed:: true
    - 添加注册表
    - 保存 ASKII 编码
    - 运行
    - ```reg
      Windows Registry Editor Version 5.00
      ; 若原先有，先删除原来的
      [-HKEY_CLASSES_ROOT\Directory\Background\shell\OpenCmdHere]
      [-HKEY_CLASSES_ROOT\Directory\Background\shell\runas]
      [-HKEY_CLASSES_ROOT\Directory\Background\shell\PowershellAdmin]
      ; 1.右键：命令行
      [HKEY_CLASSES_ROOT\Directory\Background\shell\OpenCmdHere]
      @="在此处打开命令行窗口"
      [HKEY_CLASSES_ROOT\Directory\Background\shell\OpenCmdHere\command]
      @="cmd.exe -noexit -command Set-Location -literalPath \"%V\""
      ; 2.右键：命令行（管理员）
      [HKEY_CLASSES_ROOT\Directory\Background\shell\runas]
      @="在此处打开命令行窗口(管理员)"
      "ShowBasedOnVelocityId"=dword:00639bc8
      [HKEY_CLASSES_ROOT\Directory\Background\shell\runas\command]
      @="cmd.exe /s /k pushd \"%V\""
      ; 3.shift+右键：Powershell(管理员)
      [HKEY_CLASSES_ROOT\Directory\Background\shell\PowershellAdmin]
      @="在此处打开 Powershell 窗口(管理员)"
      "Extended"=""
      [HKEY_CLASSES_ROOT\Directory\Background\shell\PowershellAdmin\command]
      @="\"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe\" -windowstyle hidden -Command $stpath = pwd; Start-Process PowerShell -ArgumentList \\\"-NoExit\\\", \\\"-Command Set-Location -literalPath '%V'\\\" -verb RunAs"
      ; 4.设置右键 管理员打开cmd的另一种方法（可用来替换上面的2）
      ; 通过Powershell调起，会闪过一次Powershell的窗口，去掉下面几行的[; ]可以取消注释
      ; [-HKEY_CLASSES_ROOT\Directory\Background\shell\OpenCmdHereAdmin]
      ;
      ; [HKEY_CLASSES_ROOT\Directory\Background\shell\OpenCmdHereAdmin]
      ; @="在此处打开命令行窗口(管理员)"
      ;
      ; [HKEY_CLASSES_ROOT\Directory\Background\shell\OpenCmdHereAdmin\command]
      ; @="PowerShell -windowstyle hidden -Command \"Start-Process cmd.exe -ArgumentList '/s,/k, pushd,%V' -Verb Run
      ```
      via: [Win10添加右键打开cmd和Powershell窗口（管理员/非管理员）_cxrsdn的博客-CSDN博客](https://blog.csdn.net/cxrsdn/article/details/84538767)
  - DONE Shutdown unnecessary processes
    collapsed:: true
    - ```powershell
      $my_tasks = @(
        "AppleMobileDeviceService.exe",     # Apple
        "ATService.exe",                    # AnyText
        "BattMonSVC.exe",                   # BattMonUI
        "crashpad_handler.exe",             # IDGAF
        "DTShellHlp.exe",                   # DAEMON Tools Lite
        "Everything.exe",                   # Everything
        # "gamingservices.exe",               # [ALWAYS] XBOX
        "msedgewebview2.exe",               # Microsoft Edge
        "OriginWebHelperService.exe",       # Game/Origin
        # "RuntimeBroker.exe",                # [ALWAYS] IDGAF
        # "StartMenuExperienceHost.exe",      # [ALWAYS] IDGAF
        "TouchpointAnalyticsClientService.exe"  # FUCK HP
      )
      for ($i=0; $i -lt $my_tasks.Length; $i++) {
        taskkill /F /im  $my_tasks[$i]
      }
      pause
      ```
  - DONE Add input double pinyin with flypy
    collapsed:: true
    - Native input sucks #sucks
      collapsed:: true
      - 之前一直使用 QQ 输入法
      - [奇客Solidot | QQ 被发现扫描并上传用户的浏览器历史](https://www.solidot.org/story?sid=66679)
        collapsed:: true
        - [【白名单方式】限制腾讯系（微信、QQ等）文件读写@20210117-2 - 用户规则分享区 - 火绒安全软件](https://bbs.huorong.cn/thread-79373-1-1.html)
        - [Huorong-Rules/Tencent at main · tutugreen/Huorong-Rules · GitHub](https://github.com/tutugreen/Huorong-Rules/tree/main/Tencent)
    - `小鹤`  Support: `win+r` -> `regedit` -> `计算机\HKEY_CURRENT_USER\Software\Microsoft\InputMethod\Settings\CHS` -> New Create `UserDefinedDoublePinyinScheme0` -> `小鹤双拼*2*^*iuvdjhcwfg^xmlnpbksqszxkrltvyovt`. [reference_1](https://blog.zaihua.me/archives/379/), [reference_2](https://www.flypy.com/bbs/forum.php?mod=viewthread&tid=166&extra=page%3D1).
      collapsed:: true
      - BUG
        collapsed:: true
        - 命令行光标表示, 换成中文重新输入, 参见https://blog.csdn.net/leilei7407/article/details/101266801