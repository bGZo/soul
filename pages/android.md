alias:: 安卓
tags:: #Phone #google
created:: 2020-05-01T17:14:48+08:00
mark:: Android 是一个由 google 主导的移动设备开源系统, 根据Android开源项目(AOSP), 手机厂商可以创建定制的 Android 操作系统版本, 将设备和配件移植到 Android 平台.

- ## [[bookmark]]
  - [Download APK Fast, Free and Safe on Android](https://apkpure.com/)
  - [APKMirror - Free APK Downloads - Free and safe Android APK downloads](https://www.apkmirror.com/)
  - [下载Android应用程序-下载，恢复，在Uptodown分享](https://cn.uptodown.com/)
  - [豌豆荚手机精灵](https://www.wandoujia.com/)
- ## [[issue]]
  - WAITING 刷机
    collapsed:: true
    - 线刷 / fastboot刷机 / `.gz`
      - 分区镜像
    - 卡刷 / recovery刷机 / `.zip`
      - ota格式的包
    - ![Image](https://pbs.twimg.com/media/Fl2mdvQacAAkwNH?format=png&name=large){:height 368, :width 664}
-
- Install
  - [应用的安装路径和过程](https://cn.apkjam.com/blog/app-installation.html)
    - Android 应用涉及到的路径有：
      - `/system/app` 系统自带的应用程序，无法删除。root 后可以删除，
      - 注意
      - 可能造成系统崩溃
      - `/data/app` 用户程序安装的目录，有删除权限。安装应用时会把 apk 文件复制到此目录
      - `/data/data` 存放应用程序的数据
      - `/data/dalvik-cache` 将 apk 中的 .dex 文件安装到该目录下（.dex 文件是 dalvik 虚拟机的可执行文件)
    - 复制 apk 安装包到 `/data/app` 目录下，解压并扫描安装包
    - 把 .dex 文件（Dalvik 字节码）保存到 `/data/dalvik-cache` 目录，并在 `/data/data` 目录下创建对应的应用数据目录
- System
  - DIY
  - MIUI
    -
    - DIY
      - 魔改必须要Root, 灰色地带的 Root 可以薅一些隐藏的羊毛, Nice!
      - MIUI Root的两个条件：**[MI FLash](https://lanzous.com/id0jgad)解BL锁**,  + 开发版及以上/系统支持(虚拟)机, OV厂的手机可以退而求其次用虚拟机. IPhone用户越狱可以用 **[[Checkra1n](https://checkra.in/)]**
      - MIUI有两种刷机方式.  两种刷机方式不兼容, 各有各的包, 如今线刷包越来越少, 官方卡版本, 不循序进行降级操作, 卡刷包同样无法降级, 只能在开机的时候才可以刷入. 如果将卡刷包刷入线刷后会报错:`“couldn't find script”`. via: https://www.mobile01.com/topicdetail.php?f=634&t=5994087. 官方也有对应的教程. 如[通用线刷教程](http://www.miui.com/shuaji-393.html), [小米手机刷机教程(高通机型)](https://www.xiaomi.cn/post/5326872)
    - REPO
      - [MIUI官方ROM仓库](https://roms.miuier.com/weekly/)
      - [台湾镜像]( https://mirom.ezbox.idv.tw/)
  - Google
-
- Software
  - 国内软件大多走双标的路线. 开拓海外市场的 app 出了两个版本(国内版/国际版). 国际版上架 Goolge Play , 接受 Google 审核的版本, 所以上架 Google Play 的 app 软件包总是容量偏小, 而且基本没有需要获取用户隐私的流氓行为. 国内版就不然了.
  - **Fav List**
    - **APKPure**
      - Coolapk
    - Clash
    - Onedrive
      - Outlook
      - To Do
    - Bitwarden
    - Zarchiver Pro
    - Podcast Republic
    - [Termux](https://github.com/termux/termux-app)
      - **0.90及以上** 版本需要 **Android7.0 及以上版本的系统**. 此安装包由 **F-Droid 编译并签名**, 且**保证与此源代码 tarball 保持一致**.
    - [kiwibrowser/src](https://github.com/kiwibrowser/src).
    - Root:
      - [vtools](https://github.com/helloklf/vtools)
        - Sence.
  - Weread
    - 下载书的目录: `/data/data/com.tencent.weread/databases/210837723/book/database`
  - Emulator
    - Software
      - BlueStack
      - 海马王技术
        - > virtualbox+androidx86+intel libhoudini+host渲染加速
          >
          > **virtualbox解决emulator载体问题**,
          **android x86**使得guest是x86架构, 在系统层面确保gust host架构相同, 免除指令模拟,
          **intel libhoudini** 是intel提供的免费但不开源arm to x86指令翻译工具, 这个工具使得只提供了arm so的app在emulator成为可行且性能不错(由于不开源, 不知道翻译是发生在哪个阶段, 但我猜是运行时动态翻译, 文档显示翻译后性能接近直接跑x86指令, 实测的确如此！)
          **host渲染加速**基本原理是, 在guesthost间建立一条高速数据传输通道, 将guest端渲染命令打包传给host端, host端解包再执行命令, 最后把结果返回, 注意, 这里很多时候是要求同步的, 这也是为什么强调通道必须高速. 另外, 别说我为何知道这些细节, 因为我正在做这玩意！(?????说了我也不太了解,++)
      - XDroid
    - 为什么卡? via: https://www.zhihu.com/question/33423859/answer/57133469
      - Intel X86/64 上无法运行 ARM, 所以采用模拟, 模拟带来的时间损耗是数量级的. 利用QEMU转x86解释执行, 效率远低于hyper-v的x86硬件虚拟化.
        - > 这不同于virtualbox里跑linux, guest指令几乎不用模拟直接在host cpu上执行(?????)
      - 渲染软实现, 没有 Host 端硬件加速.
        - 对比iOS: 模拟了一个运行iOS环境的虚拟机, 所有iOS代码compiled之后都可以mac-native的速度运行. 而QE模拟了包括storage system, screen在内的几乎所有的硬件.
    - Method
      - 保存emulator的snapshot, 具体在AVD manager中勾选 "Store a snapshot for faster startup"；
      - 使用硬件加速, 比如你在使用的电脑是基于x86架构的, 而你需要模拟的android设备也是x86架构的, 那么使用硬件加速可以很大的提升emulator的速度, 此时你需要安装 Intel’s Hardware Accelerated Execution Manager (HAXM)；
-
- Tips
  - `.nomedia`
    - > Android 默认情况下会将每个多媒体文件的信息保存在一个数据库中，应用在需要读取设备内指定格式的多媒体文件信息时，可以直接读取这个数据库，相比于文件全盘检索效率会高很多。
    - 常用于
      - 一些应用的音效
      - 一些应用的介绍视频或者图片
      - 一些应用的缓存图片
    - locate in Android 的 `frameworks` 源码，会发现文件 `frameworks/base/media/java/android/media/MediaScanner.java` 里有 `isNoMediaPath` 函数
-
- More
  - [LearningNotes|Enjoy Learning.](https://github.com/francistao/LearningNotes)
  - [AndroidInterview-Q-A|The top Internet companies android interview questions and answers](https://github.com/JackyAndroid/AndroidInterview-Q-A)
  - [android|Smartisan open source code for full build.(repo manifest xml)](https://github.com/SmartisanTech/android)
  - [Markwon|Android markdown library (no WebView)](https://github.com/noties/Markwon)
  - [WeiXinMPSDK](https://github.com/JeffreySu/WeiXinMPSDK)
  - [Notes](https://github.com/coder-pig/Android-Storage-Box)
  - [是谁让安卓变卡了 - 简书](https://www.jianshu.com/p/f6d731683ca7)
-