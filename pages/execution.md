icon:: 📄
also:: 执行
created:: [[20240814]]
description:: 
tags:: #programing

- ## Why
  -
- ## How
  -
- ## What
  - ### Outline
    id:: 6257f06a-733c-40cd-bb04-95c22975bb09
    collapsed:: true
    - General Concepts
      collapsed:: true
      - [[code]] 代码
      - 翻译器
        - [[compiler]] 编译器
        - [[compiler/optimize]] 优化编译器
      - [[intermediate-representation]] 中间语言
      - [[execution]] 程序执行
        - [[runtime-system]] 运行时系统
          - [[runtime]] 执行期
        - [[executable]] 可执行文件
        - [[interpreter]] 解释器
        - [[virtual/machine]] 虚拟机
    - [[code]] Types
      id:: 6257f14c-b3d2-4dc5-b1c2-70abca888540
      collapsed:: true
      - [[source-code]] 源代码
      - [[object-code]] 目标代码
      - [[code-byte]] 字节码
      - [[mechine-code]] 机器代码
      - [[micro-code]] 微程序
    - [[compilation]] Strategies
      collapsed:: true
      - [[just-in-time]] 即时编译 (JIT)
        collapsed:: true
        - 跟踪即时编译
      - [[ahead-of-time]] 提前编译 (AOT)
      - [[transcompilation]] 源代码至源代码编译器
      - [[recompilation]] 动态重编译
    - Notable [[runtime-system]]
      collapsed:: true
      - [[android/runtime]] Android Runtime（ART）
      - 通用语言运行库（CLR）
      - crt0
      - [[jvm]] Java虚拟机（JVM）
      - V8
        - Node.js
      - PyPy
      - Zend引擎
    - Notable Compilers & Toolchains
      collapsed:: true
      - GNU编译器套装 (GCC)
      - LLVM
        - Clang
  - ### Instruction Cycle 指令周期
    collapsed:: true
    - ![image.png](../assets/image_1649932522646_0.png)
      the cycle that the central processing unit (CPU) follows from boot-up until the computer has shut down in order to process instructions.
    - executed sequentially 按顺序执行
    - and in parallel , through an instruction pipeline 通过指令流水线同时并行执行
      id:: 6257f972-ecb5-415a-9e51-62bf0c6d8daa
    -
  - ### Context of Execution 执行上下文
    collapsed:: true
    - 执行时可用资源的隐式和显式假设。
    - 在操作系统和特定于源语言的运行时库的支持
      collapsed:: true
      - 库提供并非由计算机本身直接提供的关键服务
      - 这种支持性环境通常将程序与对计算机外围设备的直接操作分离，而是提供更通用、更抽象的服务。
- ## Namespace
  - {{namespace execution}}
- ## ↩ Reference
  -
-