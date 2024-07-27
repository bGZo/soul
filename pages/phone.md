also:: 手机
icon:: 📱
tags:: #3C
created:: [[20230719]]

- ## Why
- ## How
  - [[great/phone]]
- ## What
  - What's different with [[ios]] and [[android]]
    collapsed:: true
    - **硬件**:
      - CPU
        - 两者CPU型号分别为：A7和MSM8974. MSM8974拥有4核, 单核频率最高可达2.3GHz, 相比A7拥有2核, 最高频率为1.4GHz. 所以, 就单纯的CPU计算能力来讲, MSM8974要优于A7, 毕竟它单核频率比A7要高很多. 另外, 由于MSM8974有4核, 因此它处理多线程并发能力要强于A7. 工艺方面, 两者拥有相同的28nm制程, 但MSM8974频率高, 核心多, 所以密集计算情况下, 它的功耗和发热量应该要比A7高. 从CPU的Cache方面看, A7拥有64KB+64KB的L1 Cache, 1MB L2 Cache和4MB L3 Cache；相比较, MSM8974在这方面要差得多, 相信是为了节约成本, 仅仅配置了16KB+16KB L1 Cache, 2MB L2 Cache, 且没有L3 Cache. 如此小的Cache, 在实际运行过程中, 肯定会发生大量Cache Miss, 这就会导致CPU常常在“等待”外围IO(如内存), 从而白白浪费了CPU的高速计算能力. MSM8974在Cache的配置上, 犹如V8引擎的跑车, 却配置了一套四速变速箱, 让人无语.
      - GPU
        - A7集成PowerVR G6430 GPU, 而MSM8974集成了Adreno 330 GPU. 根据资料, G6430的图形处理性能GFLOPS为166.4-249.6, 而Adreno 330的图形处理性能GFLOPS仅为129.6-158.4. 所以, PowerVR G6430的图形性能要明显优于Adreno 330.
      - 内存(运存)
        - 设备配置的内存越大, 表示操作系统允许更多的应用程序驻留内存, 在不同的应用程序之间切换会更顺畅. 而且, 每个应用程序允许使用的内存也会越大, 相对来说会更流畅. 这方面Nexus的2GB内存要占优.
    - **OS**
      - Apple IOS, apple开发的移动设备操作系统. IOS的内核使用的是darwin os, 该内核与linux的宏内核操作系统不同, 是一个类似于windows的混合型内核. 有点类型微内核的感觉, 不过就性能而言, 与Linux相比应该没有什么优势. 但是, 因为ios的应用程序是使用objective c编码, 最终被直接编译为ARM指令集. 因此, 在实际设备运行过程中, 应用程序相当于直接在CPU上运行, 避免了虚拟机的指令翻译开销, 所以ios的应用程序执行效率相比android要高. Google Android, 是基于Linux操作系统的一个应用程序框架. 它大致由以下几个组件组成：Linux内核、Android运行库、通用组件库、应用程序框架和应用程序本身. 最终的用户应用程序均运行在一个个隔离的“沙箱”环境中, 彼此隔离. 其中, 最重要的是, Android应用程序的指令不是机器指令, 而是dalvik虚拟机指令. 也就是说, Android提供了一个Dalvik虚拟机, 将Android应用程序的dalvik指令翻译成最终的arm机器指令. 这中间虚拟机的翻译过程是有性能损耗的.
    - **Software**
      - IOS禁止应用程序在后台运行, 所有切换到后台的应用程序被操作系统自动休眠, 只有前台程序可以占用CPU；相比较, Android就开放得多, 它运行应用程序任意创建后台服务Service, 所有Service都可以在后台任意占用CPU和内存. 因此, 当Android安装的应用程序越来越多, 且应用程序毫无节制地创建后台服务的话, 系统前台应用就被迫和越来越多的后台服务共享CPU资源, 从而拖慢了整个系统的速度. 也不能说Android这种真正的多任务模式不好, 它是一把双刃剑, 给应用程序更广阔的发挥空间的前提下, 也给了应用程序滥用CPU的权限. 因此, 从这方面讲, IOS更有利于应用程序发挥流畅性, 但代价是应用程序无法再后台工作；Android更有利于发挥应用程序功能, 例如后台收离线消息, 后台下载等应用.
    - **Sceen**
      - IOS只有有限几种分辨率, 最高也就1136*640, 都没有达到1080P全高清的级别. 比较而言, Nexus5的分辨率达到了1080*1920全高清级别. 为此, 应用程序需要更多资源来渲染图像, 比较而言, IOS的应用程序就可以更容易达到流畅的帧数；但Nexus5的屏幕则可以达到更锐利, 更清晰的图像.
  - The [[CPU]] on phone by:
    - [[apple]]
      - A15
        |   | iPhone 13 mini / iPhone 13 | iPhone 13 Pro / iPhone 13 Pro Max |
        | SoC | **Apple A15 Bionic**[:br]2 × Avalanche[:br]4 × Blizzard[:br]4-core GPU | **Apple A15 Bionic**[:br]2 × Avalanche[:br]4 × Blizzard[:br]**5-core GPU** |
        via: [Apple Announces iPhone 13 Series: A15, New Cameras, New Screens](https://www.anandtech.com/show/16934/apple-announces-iphone-13-series)
      - A14
        | | iPad (2019) |  iPad Air (2019) / iPad (2020) **NEW** | iPad Air (2020) **NEW** |
        | SoC | Apple A10[:br]2x Hurricane[:br]4x Zephyr | **Apple A12**[:br]2 × Vortex @ 2.5GHz[:br]4 × Tempest @ 1.59GHz | **Apple A14**[:br]2 × Firestorm[:br]4 × Icestorm |
        via: [Apple Announces new 8th gen iPad with A12, iPad Air with 5nm A14 Chip](https://www.anandtech.com/show/16086/apple-announces-new-ipad-with-a12-ipad-air-with-5nm-a14-chip)
      - A13
        - |   | iPhone 11 Pro / iPhone 11 Pro Max / iPhone 11 |
          | SoC | **Apple A13 Bionic**[:br]2 × Lightning Performance Cores[:br]4 × Thunder Efficiency Cores |
          via: [Apple Announces New iPhone 11, iPhone 11 Pro, & iPhone 11 Pro Max ](https://www.anandtech.com/show/14859/apple-announces-new-iphone-11-iphone-11-pro-iphone-11-pro-max)
    - [[Snapdragon]] via: [List of Qualcomm Snapdragon systems on chips - Wikipedia](https://en.wikipedia.org/wiki/List_of_Qualcomm_Snapdragon_systems_on_chips)
      - Snapdragon 8 Gen2 (SM8550-AB)
        - Kryo Prime / Gold / Silver
          - 4 nm (TSMC N4)
          - **1 + 4 + 3 cores**
            collapsed:: true
            - 3.2 GHz Kryo Prime (Cortex-X3 based)
            - 2.8 GHz Kryo Gold (2× Cortex-A715, 2× Cortex-A710 based)
            - 2.0 GHz Kryo Silver (Cortex-A510 based)
        - Also: Snapdragon 8 Gen2 (SM8550-AC, 8 Gen 2 for Galaxy)
          collapsed:: true
          - 1 + 4 + 3 cores
            collapsed:: true
            - 3.36 GHz Kryo Prime (Cortex-X3 based)
            - 2.8 GHz Kryo Gold (2× Cortex-A715, 2× Cortex-A710 based)
            - 2.0 GHz Kryo Silver (Cortex-A510 based)
      - Snapdragon 8 Gen1 (SM8450)
        - **Kryo Prime / Gold / Silver**
          - **4 nm** (Samsung 4LPX) process
          - 1 + 3 + 4 cores
            collapsed:: true
            - 3.0 GHz Kryo Prime (Cortex-X2 based)
            - 2.5 GHz Kryo Gold (Cortex-A710 based)
            - 1.8 GHz Kryo Silver (Cortex-A510 based)
        - Also: 8+ (SM8475)
          collapsed:: true
          - 4 nm (TSMC N4)
          - 1 + 3 + 4 cores
            collapsed:: true
            - 3.2 GHz (Cortex-X2 based)
            - 2.75 GHz (Cortex-A710 based)
            - 2.0 GHz (Cortex-A510 based)
      - Snapdragon 888 (SM8350)
        - **Kryo 680**
          - **5 nm** (Samsung 5LPE)
          - 1+ 3 + 4 cores (2.84 GHz Cortex-X1 + 2.42 GHz Cortex-A78 + 1.80 GHz Cortex-A55)
        - Also: 888+
          collapsed:: true
          - 1 + 3 + 4 cores (3.0 GHz Cortex-X1 + 2.42 GHz Cortex-A78 + 1.80 GHz Cortex-A55)
      - Snapdragon 865 (SM8250)
        - **Kryo 585**
          - 7 nm (TSMC N7P)
          - 1 + 3 + 4 cores (2.84 GHz Cortex-A77 + 2.42 GHz Cortex-A77 + 1.80 GHz Cortex-A55)
        - Also: 865+ (SM8250-AB)
          collapsed:: true
          - 1 + 3 + 4 cores  (3.1 GHz Cortex-A77 + 2.42 GHz Cortex-A77 + 1.80 GHz Cortex-A55)
        - Also: 870 (SM8250-AC)
          collapsed:: true
          - 1 + 3 + 4 cores  (3.2 GHz Cortex-A77 + 2.42 GHz Cortex-A77 + 1.80 GHz Cortex-A55)
      - Snapdragon 855 (**SM8150**)
        collapsed:: true
        - **Kryo 485**
          collapsed:: true
          - 7 nm (TSMC N7)
          - 1 + 3 + 4 cores (2.84 GHz Cortex-A76 + 2.42 GHz Cortex-A76 + 1.8 GHz Cortex-A55)
        - Also 855+ / 860 (SM8150-AC / SM8150P)
          collapsed:: true
          - 1 + 3 + 4 cores (2.96 GHz Cortex-A76 + 2.42 GHz Cortex-A76 + 1.80 GHz Cortex-A55)
      - Snapdragon 845 (SDM845)
        collapsed:: true
        - **Kryo 385**
          collapsed:: true
          - 10 nm FinFET (Samsung 10LPP)
          - 4 + 4 cores (2.8 GHz Cortex-A75 + 1.8 GHz Cortex-A55)
      - Snapdragon 835 (MSM8998)
        collapsed:: true
        - **Kryo 280**
          collapsed:: true
          - 10 nm FinFET (Samsung 10LPE)
          - 4 + 4 cores (2.45 GHz Cortex-A73 + 1.9 GHz Cortex-A53)
    - [[Samsung]]
      collapsed:: true
      - ?
    - [[MediaTek]]
      collapsed:: true
      - ?
-
-