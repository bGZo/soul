icon:: ☕
created::  [[20240801]]
tags:: java
wikipedia:: https://en.wikipedia.org/wiki/Java_version_history

- ## What
  - Java's edition (3 main)
    - [[javase]] **Java SE** / Java Platform, Standard Edition / ~~J2SE~~
      logseq.order-list-type:: number
    - **Jakarta EE** / Java Platform, Enterprise Edition / ~~Java EE~~ / ~~J2EE~~
      logseq.order-list-type:: number
    - **Java ME** / Java Platform, Micro Edition / ~~J2ME~~
      logseq.order-list-type:: number
    - collapsed:: true
      #+BEGIN_NOTE
      有几点需要注意
      #+END_NOTE
      - SE 主要包含语言特性，标准库和虚拟机 [[jvm]]
        logseq.order-list-type:: number
      - EE 主要包含企业级 API，如 servlet、 jsp、EJB、JMS、JPA、 cdi等。
        logseq.order-list-type:: number
      - ME 主要面向移动设备进行开发，正转向其他平台；
        logseq.order-list-type:: number
        - 注意 JavaME != Android != 嵌入系统开发
      - [[javaee]] *J2SE / J2EE / J2ME* 均是 java02 时代的称呼，自 [[java05]] 之后集体更名为 *JavaSE / JavaEE / JavaME*； JavaEE 在 [[java08]] 之后被 Oracle 移交 eclipse 基金会管理，故更名为 Jakarta；
        logseq.order-list-type:: number
  - JDK version #jdk
    - ![](https://raw.githack.com/bGZo/assets/dev/2024/image_1652343742216_0-or8-or8-or8.png){:height 739, :width 515}
    - Oracle JDK vs OpenJDK
      collapsed:: true
      - | Items | Oracle JDK | OpenJDK |
        | Licences | BCL / OTN | GPL v2 |
      - BCL (Oracle Binary Code License Agreement)
        collapsed:: true
        - 可以使用 JDK (支持商用), 但是不能进行修改
      - OTN (Oracle Technology Network License Agreement)
        collapsed:: true
        - \>= JDK 11
        - 可以自己私下用，但是商用需要付费
      - ![](https://raw.githack.com/bGZo/assets/dev/2024/image_1652343266064_0.png){:height 164, :width 291}
    - `8u211` vs `8u202`
      collapsed:: true
      - Oracle JDK 关键补丁更新 (CPUs, Critical Patch Updates) 版本号
        - **奇数**编号
        - 安全漏洞修复和重要漏洞修复
      - Oracle JDK 补丁集更新 (PSUs, Patch Set Updates) 版本号
        - **偶数**编号
        - 包含相应CPUs中的所有修复以及其他非重要修复
        - 仅当受到Oracle JDK关键补丁更新(CPUs)版本之外的其他漏洞的影响时才用
- ## Namespace
  - {{namespace java/version}}
  - {{query (property :type java-version)}}
    query-sort-by:: page
    query-table:: true
    query-sort-desc:: false
    query-properties:: [:page :created :type :released-date :tags]
- ## ↩ Reference
  -