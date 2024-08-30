also:: central processing unit, 中央处理器,
description:: Its electronic circuitry executes instructions of a computer program, such as arithmetic, logic, controlling, and input/output (I/O) operations.
icon:: 📄
created:: [[20230719]]
wikipedia:: https://en.wikipedia.org/wiki/Central_processing_unit

- ## Why
- ## How
- ## What
  - Architecture
    collapsed:: true
    - **ARMv5**：(armeabi)(废弃),使用软件浮点运算, 兼容所有ARM设备, 通用性强, 速度慢(只支持armeabi)
    - **ARMv7**(2010+)：第7代 ARM v7, 使用硬件浮点运算, 具有高级扩展功能(支持 armeabi 和 armeabi-v7a)
    - **x86**(2011+)：一般用于平板,支持armeabi(性能有所损耗), 多见于 intel atom 处理器
    - **MIPS**(2012年):可能有些国产厂商在用(废弃)
    - **ARMv8**：第8代, 高端机型,64位
      - **AArch32**: 32bit
      - **AArch64**: 64bit(支持 armeabi-v7a、armeabi 和 arm64-v8a)
    - **MIPS64**(64位)
    - **x86_64**(2014+)：64位平板
    - References
      - [armv6、armv7、armv7s、armv8、armv64及其i386、x86_64区别_arm6和arm8有什么区别？_查里王的博客-CSDN博客](https://blog.csdn.net/tony_vip/article/details/105889734)
      - [ARMv7 与 ARMv8的区别_armv7和armv8_liguiyuan112的博客-CSDN博客](https://blog.csdn.net/u012505617/article/details/89205642)
      - [Intel和AMD 与 x86，ARM，MIPS有什么区别？ - 知乎](https://www.zhihu.com/question/63627218)
- ## References
  - 天梯图 | [[rank]]
    - 桌面CPU性能天梯图
      - {{nav https://www.mydrivers.com/zhuanti/tianti/cpu/index.html}}
    - 手机CPU性能天梯图
      - {{nav https://www.mydrivers.com/zhuanti/tianti/01/index.html}}
    - 桌面 CPU
      collapsed:: true
      - {{iframe https://www.mydrivers.com/zhuanti/tianti/cpu/index.html}}
        #+BEGIN_CENTER
        [桌面CPU性能天梯图](https://www.mydrivers.com/zhuanti/tianti/cpu/index.html)
        #+END_CENTER
      -
    - 笔记本 CPU （低压）
      collapsed:: true
      - {{iframe https://www.mydrivers.com/zhuanti/tianti/cpum/index.html}}
        #+BEGIN_CENTER
        [笔记本CPU性能天梯图](https://www.mydrivers.com/zhuanti/tianti/cpum/index.html)
        #+END_CENTER
      -
      -
    - 移动 CPU
      collapsed:: true
      - {{iframe https://www.mydrivers.com/zhuanti/tianti/01/index.html}}
        #+BEGIN_CENTER
        [手机CPU性能天梯图](https://www.mydrivers.com/zhuanti/tianti/01/index.html)
        #+END_CENTER
      - {{iframe https://www.socpk.com/cpu/}}
        #+BEGIN_CENTER
        [CPU性能排行 (socpk.com)](https://www.socpk.com/cpu/)
        #+END_CENTER
    - Another Way
      collapsed:: true
      - [PassMark Software - CPU Benchmark Charts](https://www.cpubenchmark.net/)
      - {{iframe https://browser.geekbench.com/processor-benchmarks}}
        #+BEGIN_CENTER
        via: [Home - Geekbench](https://browser.geekbench.com/)
        #+END_CENTER