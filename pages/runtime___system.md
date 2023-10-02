title:: runtime/system
alias:: execution/runtime/system, runtime-system
define:: 运行时系统

  - 指一种半编译的执行码在目标机器上运行时的环境
    - [[runtime/environment]] 运行环境是一种介乎编译器及直译器的执行方式
      - Java运行环境 ("Java Runtime Environment", JRE)
      - 一个由C#，Visual Basic .NET，C++.Net之类的语言写的程序运行于Microsoft Windows上的.NET Common Language Runtime(CLR)
      - Linux上的Mono
    - 大多数编程语言都有某种形式的运行时系统, 提供 [[runtime/environment]]
      - 应用程序内存的管理
      - 程序如何访问变量
      - 在过程之间传递参数的机制
      - 与操作系统的接口
      - ......
    - [[compiler]] 根据特定的运行时系统做出假设以生成正确的代码, 运行时负责
      - 设置和管理堆栈和堆
      - 可能包括
        - 垃圾收集
        - 线程
        - 语言内置的其他动态特性
  - #vs [[runtime/environment]]
    - [[runtime-system]] 可定义为用于编程的应用软件 (IDE) 的特定部分
      - 该软件为程序员提供更方便的运行程序环境在他们的生产过程中(测试和类似的)
    - RTE 将是应用于已开发程序的执行模型的实例，该程序本身然后在上述运行时系统中运行
  - 高级功能
    id:: 6257fc70-1e67-4988-9267-b292c0672035
    - 允许应用程序代码直接与运行时系统交互的接口
      id:: 6257fddd-1ed7-4c9b-bd01-73dcfbd921a4
    - 多任务, 运行时系统被实现为抽象层，它将运行时系统的调用转换为操作系统的调用
      collapsed:: true
      - 隐藏了不同操作系统提供的服务的复杂性或变化
      - 操作系统内核本身可以被视为运行时系统
        - 调用操作系统行为的操作系统调用集可以被视为与运行时系统的交互
    - 提供如 [[p-code/machine]](P代码机) 或 [[virtual/machine]] (虚拟机) 之类的服务
      id:: 6257fde9-c1a0-43c1-a8ea-35d158dec86b
      collapsed:: true
      - 隐藏处理器的指令集
      - 许多解释型语言（例如AWK）和某些语言（例如Java ）所遵循的方法，
        - 这些语言旨在编译成一些与机器无关的中间表示代码（例如bytecode）
      - 简化了语言实现的任务及其对不同机器的适应，并提高了反射等复杂语言功能的效率
      - 它还允许在任何机器上执行相同的程序，而无需显式的重​​新编译步骤
    - 并行执行行为
      id:: 62580082-c338-4ed5-9c45-50c291241d63
- Refs
  id:: 62580166-4057-4229-a92b-33ea97160b8c
  collapsed:: true
  - [Runtime system - Wikipedia](https://en.wikipedia.org/wiki/Runtime_system)