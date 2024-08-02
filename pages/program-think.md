also:: 编程随想
exclude-from-graph-view:: true
tags:: #blog
author:: 编程随想
source:: [编程随想的博客](https://program-think.blogspot.com/)
created:: [[20221212]]

- Archives
  - Java 新手的通病[0]：概述
    collapsed:: true
    #java
    - collapsed:: true
      1. [对算法和数据结构不熟悉](https://program-think.blogspot.com/2009/01/defect-of-java-beginner-1-algorithm.html)
      collapsed:: true
      #algorithm
      - 几个问题：
        - 什么时候该用数组型容器、什么时候该用链表型容器？
        - 什么是散列函数？HashMap 的实现原理是什么？
        - 什么是递归？如果你以前从来没写过递归函数，尝试着写一个（比如用递归函数进行目录树遍历）。
        - 什么是算法复杂度？
        - 你是否理解空间换时间的思想？
        - 写一个针对整数数组的冒泡排序函数，看看你要修改几次才能跑通。
        - 写一个针对整数数组的二分查找函数，看看你要修改几次才能跑通。
    - 2. [缺乏面向对象的基本功](https://program-think.blogspot.com/2009/01/defect-of-java-beginner-2-oo.html)
      #oop
      - 几个问题：
        - 基于接口的继承和基于实现的继承各有什么优缺点？
        - 继承（包括 extend 和 implement）有什么【缺点】？
        - 多态（polymorphism）有什么【缺点】？
        - 为什么 Java 可以多继承 interface，而不可以多继承 class？
        - 假如让你写一个小游戏（比如人机对战的五子棋），你会如何设计类结构？
        - 类结构设计时，如何考虑可扩展性？
    - collapsed:: true
      3. [缺少良好的编程习惯](https://program-think.blogspot.com/2009/02/defect-of-java-beginner-3-code-style.html)
      collapsed:: true
      #programming
      - 随意地命名
      - 习惯于代码的 copy & paste
      - Magic Number 满天飞
      - 代码耦合度太大
        - 至于说到代码耦合分别由哪些情况引起？什么是正交的设计？（关于耦合与正交设计，我后面会专门讨论一下）能完全搞明白的人就更少了。
      - 被 GC 宠坏
    - 4. [异常处理使用不当](https://program-think.blogspot.com/2009/02/defect-of-java-beginner-4-exception.html)
    - collapsed:: true
      5. [对虚拟机（JVM）了解不足](https://program-think.blogspot.com/2009/05/defect-of-java-beginner-5-jvm.html)
      collapsed:: true
      #jvm
      - 关于基本类型和引用类型
      - 关于垃圾回收（Garbage Collection）
        - GC 是如何判断哪些对象已经失效？
        - GC 对性能会有哪些影响？
        - 如何通过 JVM 的参数调优 GC 的性能？
      - 关于字符串
        - 对于 Java 提供的 String 和 StringBuilder，想必很多人都知道：String 用于常量字符串，StringBuilder 用于可变字符串。那 Java 当初为什么要这样设计捏？为啥不用一个类来统一搞定捏？
      - 关于范型（Generic Programming）
        - GP 是在编译时实现的还是在运行时实现的？为什么要这么实现？
        - GP 的类型擦除机制是咋回事？有啥优点/缺点？
        - 使用范型容器（相对于传统容器）在性能上有啥影响？为什么？
      - 关于多线程
        - synchronized 关键字是怎么起作用滴？
        - synchronized 的颗粒度（或者说作用域）如何？是针对某个类还是针对某个类对象实例？
        - synchronized 对性能有没有影响？为什么？
        - volatile 关键字又是派啥用滴？啥时候需要用这个关键字捏？
  - title:: [计算机网络通讯的【系统性】扫盲——从“基本概念”到“==OSI 模型==”](https://program-think.blogspot.com/2021/03/Computer-Networks-Overview.html)
    author:: 
    tags:: #archive/web #web #networking
    created:: [[20221212]]
    description:: 
    archive:: [💾 Archived](../assets/archived_web/计算机网络通讯的【系统性】扫盲——从基本概念到OSI 模型 @ 编程随想的博客 (12_12_2022 2_18_47 PM).html)
    collapsed:: true
    - 本文的目标读者
    - 基本概念
      collapsed:: true
      - 信道（ [Communication_channel](https://en.wikipedia.org/wiki/Communication_channel) ）
        collapsed:: true
        - 类型
        - 带宽
          - 电气领域 ＆ 计算机领域都有“带宽”这个概念，但两者的定义不太一样。电气领域所说的“带宽”指的是“模拟带宽”，单位是“赫兹/Hz”；计算机领域所说的“带宽”指“数字带宽”，单位是“比特率”或“字节率”
          - 单位
            - 为了避免扯皮，后来国际上约定了一个规矩：对【2进制】的数量级要加一个小写字母 i。比如说：Ki 表示 1024；Mi 表示 1024x1024 ...... 以此类推。
            - 举例
              - 1Kbps 表示“1000比特每秒”
              - 1KiBps 表示“1024字节每秒”
          - 工作模式：单工 VS 半双工 VS 全双工
            - “电台”可以发信号给“收音机”，但“收音机”【不能】发信号给“电台”
            - 火车在单条铁轨上，可以有两种运行方向；但对于同一个瞬间，只能选其中一个方向（否则就撞车了）
            - 在同一根光导纤维中，可以有多个光束【同时相向】传播，互相不会干扰对方
      - 端点
      - 单播、组播/多播、广播、选播
      - 通讯协议（protocol）
    - 从“分层”到“参考模型”
      collapsed:: true
      - 分层
        - 在网络通讯领域，采用的是【分层】的设计思路
        - 多个层次的协议在一起协同工作，技术上称作“协议栈”（洋文叫做“protocol stack”）
      - 协议栈的原理
        - 这里所说的“服务”指某种“编程接口”，技术行话叫 API
      - 逻辑信道
        - 对上层而言，调用下层提供的 API 发送信息，其效果相当于在使用某种【信道】进行通讯，这也就是俺在 ★基本概念 那个章节所说的“逻辑信道”
      - 数据格式的原理
        - ```
          头部
          身体（也称作“有效载荷”）
          尾部（注：很多协议没有尾部）
          ```
        - 下层协议的【载荷】就是上层协议的【整体】
      - 网络分层的参考模型
        - OSI 模型
        - TCP/IP 模型
          - 对“TCP/IP 模型”的分层，不同的文章或书籍，说法不太一样（“3层、4层、5层”皆有），这就引发了一些争议。包括几位热心读者也在博客留言，表达不同意见。为了避免一家之言，贴出维基百科的“这个链接”，其中给出了几种比较有名的说法
    - OSI (Open System Interconnection) 概述
      collapsed:: true
      - 历史
        - ISO 与 ITU 就决定合作，两家一起干。这2个组织的2套班子，从上世纪70年代开始搞，搞来搞去，搞了很多年，一直到1984年才终于正式发布 OSI 标准
      - 两个组成部分
        - 其一，抽象的概念模型，也就是前面提到的【OSI model】；
        - 其二，针对这个概念模型的具体实现（具体的通讯协议），洋文叫做【OSI protocols】
          - 协议搞得很复杂，严重违背了 IT 设计领域的 KISS 原则
      - OSI 模型的7层
    - 物理层：概述
      collapsed:: true
      - 必要性
        - 屏蔽这些细节
          - “无线电通讯”需要关心“频率/波长”；
          - 电缆通讯需要跟“电压”打交道；
          - “光纤通讯”需要关心“玻璃的折射率＆光线的入射角”
      - 物理信道的类型
        - 1. 有线信道（比如：双绞线、同轴电缆、光纤、等等）
        - 2. 无线信道（比如：微波通讯、电台广播、卫星通讯、等等）
        - 3. 存储信道
          - 可以把信息先保存到某种【存储介质】（比如硬盘），然后再把存储介质用某种方式（比如快递）转交给对方。这就是所谓的“存储信道”
      - [信噪比](https://zh.wikipedia.org/wiki/%E4%BF%A1%E5%99%AA%E6%AF%94) （Signal-to-noise ratio）
        - “信道传输的有用信息”与“无用的干扰噪声”，这两者的比值就是“信噪比”
        - “信噪比”单位是【分贝】。“分贝”洋文叫做“decibel”（简写为 dB）。“deci”表示“十进制”；“bel”是为了纪念大名鼎鼎的贝尔（电话它爹）
      - 带宽的限制因素
        - 不管使用何种物理介质，都要受限于某些基本的物理学定律（比如“光速上限”）。另外，不管何种物理介质，总是会有或多或少的环境干扰（噪声）。这两个因素导致了：任何“物理信道”的最大传输率总是有限滴
        - “物理信道”的带宽上限也就是整个协议栈的带宽上限
      - [多路复用](https://zh.wikipedia.org/wiki/%E5%A4%9A%E8%B7%AF%E5%A4%8D%E7%94%A8) （Multiplexing）
    - 物理层：具体实例
      collapsed:: true
      - 物理层的【协议】
        - [USB 协议](https://en.wikipedia.org/wiki/Universal_Serial_Bus)
        - [蓝牙协议](https://en.wikipedia.org/wiki/List_of_Bluetooth_protocols)的一部分
        - [IEEE 802.11](https://en.wikipedia.org/wiki/IEEE_802.11) 的一部分（Wi-Fi）
        - [IEEE 802.16](https://en.wikipedia.org/wiki/IEEE_802.16)（WiMAX）
        - [IEEE 1394](https://en.wikipedia.org/wiki/IEEE_1394)（火线接口）
        - [RS-232 协议](https://en.wikipedia.org/wiki/RS-232)（串行接口/串口）
          ......
      - 物理层的【协议实现】
      - 物理层相关的【网络设备】
        - **[调制解调器](https://zh.wikipedia.org/wiki/%E8%B0%83%E5%88%B6%E8%A7%A3%E8%B0%83%E5%99%A8)（modem）**
          - “调制解调器”就是用来翻译“数字信号 ＆ 模拟信号”
        - **[中继器](https://en.wikipedia.org/wiki/Repeater)（repeater）**
        - **[集线器](https://zh.wikipedia.org/wiki/%E9%9B%86%E7%B7%9A%E5%99%A8)（hub）**
    - 链路层：概述
      collapsed:: true
      - 必要性
        collapsed:: true
        - **对信息的打包**
          - 物理层传输的信息，通俗地说就是【比特流】（也就是一长串比特）。但是对于计算机来说，“比特流”太低级啦，处理起来极不方便。“链路层”要干的第一个事情，就是把“比特流”打包成更大的一坨，以方便更上层的协议进行处理。在 OSI 模型中，链路层的一坨，称之为“帧”（frame）
        - **差错控制**
          - “校验算法”的原理类似于《[扫盲文件完整性校验——关于散列值和数字签名](https://program-think.blogspot.com/2013/02/file-integrity-check.html)》一文中提到的“散列算法/哈希算法”
        - **流量控制**
        - **信道复用**
      - [MAC 协议](https://en.wikipedia.org/wiki/Medium_access_control)
      - MAC 地址
        - 如果手工修改 MAC 地址，故意把两块网卡的 MAC 地址搞成一样，那确实就做不到唯一性了。并且会导致链路层的通讯出问题
        - MAC 地址包含6个字节（48个比特），分为两半。第一部分称作【OUI】，OUI 的24个比特中，其中2个比特有特殊含义，其它22个比特，用来作为网卡厂商的唯一编号。这个编号由国际组织 IEEE 统一分配。
    - 链路层：具体实例
      collapsed:: true
      - 链路层的【协议】
        - [MAC 协议](https://en.wikipedia.org/wiki/Media_access_control)（介质访问控制）
        - [LLC 协议](https://en.wikipedia.org/wiki/Logical_link_control)（逻辑链路控制）
        - [ARP 协议](https://en.wikipedia.org/wiki/Address_Resolution_Protocol)（解析 MAC 地址）
        - [IEEE 802.3](https://en.wikipedia.org/wiki/IEEE_802.3)（以太网）
        - [IEEE 802.11](https://en.wikipedia.org/wiki/IEEE_802.11) 的一部分（Wi-Fi）
        - [L2TP 协议](https://en.wikipedia.org/wiki/Layer_2_Tunneling_Protocol)（2层VPN）
        - [PPP 协议](https://en.wikipedia.org/wiki/Point-to-Point_Protocol)（拨号上网）
        - [SLIP 协议](https://en.wikipedia.org/wiki/Serial_Line_Internet_Protocol)（拨号上网）
        - ......
      - 链路层的【协议实现】
      - 链路层相关的【网络设备】
        - **[网络交换机](https://zh.wikipedia.org/wiki/%E7%B6%B2%E8%B7%AF%E4%BA%A4%E6%8F%9B%E5%99%A8)（network switch）**
        - **[网桥/桥接器](https://zh.wikipedia.org/wiki/%E6%A1%A5%E6%8E%A5%E5%99%A8)（network bridge）**
      - 链路层相关的【软件工具】
        - 嗅探抓包工具（Sniffer）
          - [Wireshark](https://en.wikipedia.org/wiki/Wireshark)（原先叫做 Ethereal）
        - ARP 命令
    - 网络层：概述
      - 必要性
        collapsed:: true
        - **路由机制（routing）**
          - 如何在这些【没有直连】的端点之间建立通讯捏？此时就需要提供某种机制，让其它端点帮忙转发数据。这就需要引入“路由机制”
          - **基于【路由】的地址编码方式**
          - **网际互联（[internetwork](https://en.wikipedia.org/wiki/Internetworking)）**
            collapsed:: true
            - 屏蔽不同类型的网络之间的差异，从而有利于【网际互联】（也就是建立“网络的网络”）
            - 一般来说，要想联通【异种】网络，就要求每个网络中都有一台主机充当【网关】（gateway）。【网关】起到“中介/翻译”的作用——帮不同的网络翻译协议，使得不同的网络可以互相联通
      - 网络拓扑（network topology）
        collapsed:: true
        - 再复杂的拓扑，也可以逐步分解为若干简单拓扑的组合
        - 对拓扑的研究，有专门一个数学分支（拓扑学）
      - 互联网的拓扑——从“历史”的角度看其健壮性
        collapsed:: true
        - 当时美国的电话网络是典型的【多级星形拓扑】。这种拓扑的优点是：简单、高效、便于管理；但缺点是：健壮性很差。从这个案例中，大伙儿可以再次体会到“效率”与“健壮性”之间的矛盾。俺写过一篇很重要的博文（这里）深入讨论了这个话题
        - 即使发生全面核大战，大量骨干节点被摧毁，整个网络也不会被分隔成几个孤岛，军方的指挥系统依然能正常运作
      - 路由的大致原理
        collapsed:: true
        - 当主机 A 向主机 B 发送网络层的数据时，大致会经历如下步骤：
        - 1. A 主机的协议栈先判断“A B 两个地址”是否在同一个子网（“子网掩码”就是用来干这事儿滴）。
          如果是同一个子网，直接发给对方；如果不是同一个子网，发给本子网的【默认网关】。
          （此处所说的“网关”指“3层网关/网络层网关”）
        - 2.对于“默认网关”，有可能自己就是路由器；也可能自己不是路由器，但与其它路由器相连。
          也就是说，“默认网关”要么自己对数据包进行路由，要么丢给能进行路由的另一台设备。
          （万一找不到能路由的设备，这个数据就被丢弃，于是网络通讯出错）
        - 3.当数据到达某个路由器之后，有如下几种可能——
          collapsed:: true
          - 3.1 该路由器正好是 B 所在子网的网关（与 B 直连），那就把数据包丢给 B，路由过程就结束啦；
          - 3.2 亦或者，路由器会把数据包丢给另一个路由器（另一个路由器再丢给另一个路由器） ...... 如此循环往复，最终到达目的地 B。
          - 3.3 还存在一种可能性：始终找不到“主机 B”（有可能该主机“断线 or 关机 or 根本不存在”）。为了避免数据包长时间在网络上闲逛，还需要引入某种【数据包存活机制】（洋文叫做“Time To Live”，简称 TTL）。
            通常会采用某个整数（TTL 计数）表示数据包能活多久。当主机 A 发出这个数据包的时候，这个“TTL 计数”就已经设置好了。每当这个数据包被路由器转发一次，“TTL 记数”就减一。当 TTL 变为零，这个数据包就死了（被丢弃）。
      - 由算法的演变史（以互联网为例）
        collapsed:: true
        - **第1阶段：静态全局路由表**
        - **第2阶段：动态全局路由表**
        - **第3阶段：动态分级路由表**
      - 互联网的路由——从“CAS”的角度看其健壮性
      - 网络层的两种交换技术——电路交换（circuit switching） VS 分组交换（packet switching）
    - 网络层：具体实例
      collapsed:: true
      - 网络层的协议有很多。由于“互联网”已经成为全球的事实标准，因此俺只列出属于“互联网协议族”的那些“网络层协议”：
        collapsed:: true
        - IP 协议（含 [IPv4](https://en.wikipedia.org/wiki/IPv4) ＆ [IPv6](https://en.wikipedia.org/wiki/IPv6)）
        - [ICMP](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol)
        - [IGMP](https://en.wikipedia.org/wiki/Internet_Group_Management_Protocol)
        - [IPSec](https://en.wikipedia.org/wiki/IPsec)
        - ......
      - 网络层相关的【网络设备】
        collapsed:: true
        - **[路由器](https://zh.wikipedia.org/wiki/%E8%B7%AF%E7%94%B1%E5%99%A8)（router）**
        - **3层交换机（Layer 3 switching）**
        - **[无线热点](https://zh.wikipedia.org/wiki/%E7%84%A1%E7%B7%9A%E6%8E%A5%E5%85%A5%E9%BB%9E)（Wireless Access Point）**
      - 网络层相关的【软件工具】
        collapsed:: true
        - **[ping](https://en.wikipedia.org/wiki/Ping_(networking_utility))**
        - **[traceroute](https://en.wikipedia.org/wiki/Traceroute)**
    - 传输层：概述
      collapsed:: true
      - 必要性
        collapsed:: true
        - **屏蔽“有连接 or 无连接”的差异**
          collapsed:: true
          - 网络层本身还有一个差异，也就是网络层的两种交换技术：电路交换（有连接） VS 分组交换（无连接）
          - 对于开发网络软件的程序员来说，当然不想操心“网络层用的是哪一种交换机制”。因此，需要对网络层的上述差异再加一个抽象层（也就是“传输层”
        - **从“主机”到“进程”**
          collapsed:: true
          - 而“传输层”是面向【进程】滴！因为传输层要提供给【网络软件】使用，而网络软件打交道的对象是【另一个网络软件】。因此，传输层必须在“网络层地址”的基础上，再引入某种新的标识，用来区分同一台主机上的不同【进程】
      - 特殊性
        collapsed:: true
        - 对于开发应用软件的程序猿/程序媛，“传输层”是他们能感知的最低一层
      - 传输层的【端口】
        collapsed:: true
        - 在 OSI 模型中，“端口”的官方称呼是“传输服务访问点”（洋文缩写 TSAP）
    - 传输层：具体实例
      collapsed:: true
      - 传输层的【协议】
        - TCP ＆ UDP（前者是“有连接”，后者是“无连接”）
      - 传输层的【协议实现】
      - 套接字（socket API）
        - 传输层的协议实现通常包含在操作系统自带的网络模块中（也就是“操作系统协议栈”）
        - 就需要提供一些封装传输层的【库】（API）。程序员只需要调用这些【库】，就可以使用传输层的协议进行通讯啦
        - 在互联网诞生初期，伯克利分校开发了一个 UNIX 操作系统的的变种，叫做“伯克利 UNIX 发行版”（BSD Unix），也就是如今 BSD 操作系统的前身。伯克利发行版内置了一套用来进行网络编程的 API，当时叫做“伯克利套接字”（（[Berkeley sockets](https://en.wikipedia.org/wiki/Berkeley_sockets)））。由于这套 API 用起来很方便，很多其它的 UNIX 变种也移植了这套 API，于是就逐渐成了业界的事实标准。到了上世纪90年代，Windows ＆ Linux 也都提供了这套 API
      - 传输层相关的【网络设备】
        - **4层交换机（Layer 4 switching）**
        - **状态防火墙（[stateful firewall](https://en.wikipedia.org/wiki/Stateful_firewall)）**
      - 传输层相关的【软件工具】
        - **[netcat](https://en.wikipedia.org/wiki/Netcat) 家族**——传输层的“瑞士军刀”
          关于 netcat，俺已经写过一篇比较详细的教程：《[扫盲 netcat（网猫）的 N 种用法——从“网络诊断”到“系统入侵”](https://program-think.blogspot.com/2019/09/Netcat-Tricks.html)》。看完这篇教程，你肯定能体会它功能的强大——很多与 TCP/UDP 相关的事情，都可以用 netcat 搞定。
          另外，netcat 还有很多衍生品（衍生的开源项目），构成一个丰富的 netcat 家族。在上述教程也有介绍。
        - **netstat ＆ ss**
          Windows 和 POSIX（Linux＆UNIX）都有一个 netstat 命令，可以查看当前系统的 TCP/UDP 状态（包括当前系统开启了哪些监听端口）。
          另外，Linux 上还有一个 ss 命令，功能更强（但这个命令在 Windows 上默认没有）
        - **[nmap](https://en.wikipedia.org/wiki/Nmap)**
          这是最著名的开源的扫描器，可以扫描远程主机监听了哪些传输层端口（注：前面提到的“netcat 家族”也可以干这事儿）
          nmap 的功能很强，“端口扫描”只是其功能之一。
    - 业务层（OSI 上三层）：概述
      collapsed:: true
      - 必要性
        - 有些软件只用一个协议来搞定所有的业务逻辑（只有一层）；有些软件会参考 OSI，把业务逻辑的协议分为三层；还有些软件可能会分出更多的层次
      - 会话层 ＆ 表示层 ＆ 应用层
    - 业务层（OSI 上三层）：具体实例
      collapsed:: true
      - 业务层的协议非常多。即使光把各种协议的名称列出来，也很费劲。所以俺就偷懒一下，只点评几个特别重要的协议。
        collapsed:: true
        - **HTTP 协议**
          如果让俺评选最重要的业务层协议，俺首推 HTTP 协议。互联网的普及推动了 Web 的普及，而 Web 的普及使得 HTTP 成为信息时代的重要支柱。当你上网的时候，你看到的网页（HTML 页面）就是通过 HTTP 协议传输到你的浏览器上。
          如今 HTTP 已经不仅仅用来展示网页，还有很多业务层的协议是建立在 HTTP 协议之上。比如说：如果你用 RSS 订阅俺的博客，RSS 阅读器需要调用 blogspot 博客平台提供的 RSS 接口，这些 RSS 接口就是基于 HTTP 协议传输滴。
          考虑到本文的篇幅，俺不可能在这里细聊 HTTP 协议的规格，有兴趣的同学可以去看《[HTTP 权威指南](https://docs.google.com/document/d/1TgujhFUzyVlf1W5e48lSMTIwJuCTElvXw2LgQ_Ng0Cs/)》这本书。
        - **SSL/TLS 协议**
          最早的 HTTP 协议是【明文】滴；为了强化安全性，后来又设计了 SSL 协议，用来【加密】HTTP 流量；再后来，SSL 升级为 TLS（这俩是同义词）。如今经常看到的 HTTPS 相当于“HTTP over TLS”。
          SSL/TLS 设计得比较优雅（很灵活），使得其它业务层的协议可以很方便地架构在 SSL/TLS 之上。这样的好处是：其它协议就不用自己再设计一套加密机制＆认证机制。
          SSL/TLS 对于安全性很重要，因此俺专门写了一个系列教程（如下），详细介绍该协议的技术细节。
          《[扫盲 HTTPS 和 SSL／TLS 协议](https://program-think.blogspot.com/2014/11/https-ssl-tls-0.html)》（系列）
        - **域名相关的协议（DNS 及其它）**
          域名相关的协议，也很重要。因为域名系统是整个互联网的基础设施。最早的域名查询协议是“DNS 协议”，由于这个协议【没有】加密，导致了一些安全隐患。比如 GFW 就利用 DNS 的这个弱点，搞“域名污染/域名投毒”。因此，后来又设计了一系列新的域名协议，引入了加密的机制。
          关于这些协议的扫盲教程，可以参考如下几篇博文：
          《[扫盲 DNS 原理，兼谈“域名劫持”和“域名欺骗／域名污染”](https://program-think.blogspot.com/2014/01/dns.html)》
          《[对比4种强化域名安全的协议——DNSSEC，DNSCrypt，DNS over TLS，DNS over HTTPS](https://program-think.blogspot.com/2018/10/Comparison-of-DNS-Protocols.html)》
      - 业务层相关的【网络设备】
        - **应用层防火墙（[application firewall](https://en.wikipedia.org/wiki/Application_firewall)）**
        - **入侵检测（[intrusion detection system](https://en.wikipedia.org/wiki/Intrusion_detection_system)）**
        - **GFW（Great Firewall）**
    - 杂项
      collapsed:: true
      - VPN（ [virtual private network](https://en.wikipedia.org/wiki/Virtual_private_network) ）
      - 代理（proxy）
      - 网关（ [gateway](https://en.wikipedia.org/wiki/Gateway_(telecommunications)) ）
      - 隧道协议（ [tunneling protocol](https://en.wikipedia.org/wiki/Tunnelling_protocol) ）
      - GFW（Great Firewall）
        collapsed:: true
        　　本博客已经写了很多翻墙教程，大伙儿肯定都知道 GFW 了。
        　　由于“Great Firewall”中有“Firewall”字样，很多天朝网民【误以为】GFW 是防火墙，其实不然！GFW 本质上就是 IDS——其部署方式类似于 IDS（旁路部署），其工作方式有很大一部分也类似于 IDS（当然啦，GFW 的功能比 IDS 更多）。
        　　大约七八年前，就有热心读者建议俺写一篇技术博文，介绍 GFW 的工作原理。由于俺比较懒，拖到今年（2021）都没动手，很惭愧 :(
      - 隧道协议（tunneling protocol）
        collapsed:: true
        - 用某种协议包裹另一种协议，以满足某些特殊的需求
        - “隧道协议”可以做到更灵活的包裹——既可以对层次相隔很远的协议进行包裹，也可以对同一层的协议进行包裹，甚至可以“倒挂”——所谓的“倒挂”就是让【上】层反过来包裹【下】层
  - title:: [天朝民众的心理分析：斯德哥尔摩综合症](https://program-think.blogspot.com/2012/06/stockholm-syndrome.html)
    author:: 
    tags:: #GFW #archive/web
    created:: [[20221212]]
    description:: 
    archive:: [💾 Archived](../assets/archived_web/天朝民众的心理分析：斯德哥尔摩综合症 @ 编程随想的博客 (12_12_2022 3_20_52 PM).html )
    collapsed:: true
    - 从一桩奇怪的抢劫案说起
      collapsed:: true
      - “斯德哥尔摩综合症”这个拗口的术语，来自于斯德哥尔摩（瑞典首都）的一桩银行抢劫案。1973年8月23日，两个劫匪去抢斯德哥尔摩的某家银行未遂，劫持了几名银行职员做人质。在与警方僵持6天之后，劫匪投降。
      - 本来这只是一个普通的抢劫未遂。但后来发生了一系列奇怪的事情：被劫持的职员不但不配合警察取证，而且还极力为劫匪开脱；其中一名女性人质还吵着要跟劫匪结婚......
      - “斯德哥尔摩综合症”（Stockholm Syndrome）因此而得名，因为跟人质有关，还有几个不太拗口的别称：“人质综合症”、“人质情结”。为了打字省力，俺后面都用“人质情结”来称呼。
    - 人质情结的心理学解释
      - 人质的【心理变化】过程
        - 先说说人质的心理变化。大概经过如下3阶段。
          - 1. 害怕 / 恐惧
            - 刚开始被劫持，人质比如处于极大的惊吓和恐惧中。这点好理解。
          - 2. 认同 / 同情
            - 人质被劫持期间，往往得不到外界的信息。在上述案件中，人质与劫匪一起被警方包围了6天。由于时间长，人质和劫匪都面临相同的困境（比如缺乏食物）。在共同的困境中，人质对劫匪会产生一种同甘共苦的认同感。这种认同心理会进一步演化为同情心理。
            - 从心理学的角度而言：性格比较脆弱的人、比较感性的人、比较容易受感动的人，会产生这个转变（认同和同情）。
          - 3. 依赖 / 崇拜
            - 一旦形成同情心理，后续就有可能再演化为依赖心理。
            - 因为劫匪掌握了生杀大权（劫匪可以随时处死人质，人质的食物靠劫匪来分配）。在这样一个极端环境中，劫匪相对于人质是强者。而崇尚强者、依赖强者是普遍的心理特征。
            - 顺便说一下：“依赖强者”的心理，可以从进化心理学得到解释——这是从咱们的老祖宗（猿）遗传来的——因为猿的群体具有严格的等级界定，崇尚强者有利于维持群体的稳定。
        - 形成人质情结的【必要条件】
          - 从刚才提到的人质的心路历程，心理学家总结了形成人质情结的必要条件：
            - **1. 人质相信绑匪会对自己构成威胁（尤其是生命威胁）**
            - **2. 劫持期间，绑匪提供给人质一些小恩小惠，而人质也认同并接受这些小恩小惠**
            - ==**3. 人质跟外界完全隔离，接触到的信息都来自绑匪**==
            - ==**4. 人质认为自己【不】可能逃脱**==
      - 哪种心理特质易产生人质情结？
        - 从刚才的分析，可以总结出：
          - 容易陷入人质情结的心理特质：脆弱、感性、易感动、依赖性强、易崇尚强者
          - 对人质情结有免疫的心理特质：坚强、理性、独立性强、喜欢对抗权威
    - 专制独裁导致的人质情结
    - 如何破解人质情结？
    - 结尾
  - [“心智模式”系列：如何面对【逆境】？——兼谈“斯托克代尔悖论”](https://program-think.blogspot.com/2012/01/stockdale-paradox.html)
    collapsed:: true
    - ```
      话说斯托克代尔是越战后的美国海军中将。他在参加越战时被俘，被关在战俘营长达八年，期间遭受越共的种种虐待。作为当时战俘营中军衔最高的军官，他带领同伴跟越共做各种斗争，以提高美军战俘的待遇并增加获释的机会。获释之后，斯托克代尔的事迹被广为宣传。著名的管理学家吉姆·柯林斯慕名找他做了一次访谈（以下是对话过程摘录）。
      柯林斯好奇地问：
      你为啥能熬过那8年悲惨的战俘生活，坚持到最后获释的？
      斯托克代尔给出的回答是：
      因为俺从不失去信心。俺坚信自己一定能活着出来。这个信念一直支撑着俺。
      （这个回答貌似挺普通的）
      柯林斯又问：
      哪些人没能活着出来？
      斯托克代尔说：
      这个简单，当然是那些乐观主义者啦。
      （这下柯林斯被彻底搞糊涂了。俺第一次读这个故事，也被搞糊涂了）
      斯托克代尔察觉到柯林斯的困惑，继续补充道：
      那帮乐观主义者会说：'圣诞节之前，我们一定出得去'。圣诞节会来临，然后过了。
      他们又说：'复活节之前，我们一定出得去'。复活节来了，又过了。
      然后是感恩节，再然后是下一个圣诞节......如此往复。最终，那些乐观主义者在郁闷中死去。
      最后，斯托克代尔总结说：
      这是一个非常重要的教训——你不能把信念和原则搞混。
      信念是：你一定能获得成功——这个信念千万不可失去。
      原则是：你一定要面对最残忍的现实——无论它们是什么。
      ```
    - > 大部分刚毕业或参加工作不久的年轻人，（在面对逆境时）也可以分化为乐观主义者和悲观主义者。
      那些容易悲观的人，往往也过于自卑。一旦碰到困境，首先选择逃避。他们通常没有太大的追求，更愿意维持现状。这类人在工作中多半是混日子，做一天和尚撞一天钟。
      而那些乐观主义者捏，通常过于自信。其特点之一就是：刚踏入社会就立下豪言壮语，妄图瞬间成名，快速致富。由于对现实的残酷缺乏认识，这类人往往在几次碰壁之后，梦想被粉碎，然后转变为悲观主义者。
      还有一种乐观主义者，之所以还保持乐观，是因为人生道路比较顺，一直没有碰到大的挫折。这类人的乐观和自信是建立在虚无之上，还没经受过考验，很脆弱。
      上述这几类人都不太可能有大的成就。能成大事者，往往是那些历经重大挫折而依然斗志昂扬之人——比如大伙儿很熟悉的乔布斯同学。
    - {{video https://www.youtube.com/watch?v=JJZH17UqbG8}}
      - 总体而言, 我们不能丧失生活的信心, 我们一定可以获得成功, 但是是不是这次不知道, 只要我们能把一切苦难熬过来. 最后成功的一定是我们. 我们不能完全做一个悲观的人, 认为每一次机会都不可能有转机, 也不能做一个乐观的人, 投机在某几次的机会中, 我们能做的就是把手头的锄刀, 磨亮一些, 再亮一些, 再亮, 再亮...
  - [“心智模式”系列：认识你自己——心智模式扫盲介绍](https://program-think.blogspot.com/2010/02/about-mental-model.html)
    collapsed:: true
    - 心智模式包含了你对自己及周围世界的一些看法、观念、定义；然后，在这些看法、观念、定义的基础上，会形成你自己的一些观察的套路、思维的套路、反馈的套路
    - 它就像那电脑软件，决定了信息获得的多寡（观察）、如何处理信息（思考）、如何保存信息（记忆）、如何做出反馈（行动）
  -