-
  - > Java 是解释执行”,这句话正确吗?
  - 对于“Java是解释执行”这句话,这个说法不太准确。我们开发的Java的源代码,首先通过Javac编译成为字节码(bytecode),然后,在运行时,通过Java虚拟机(JVM)内嵌的解释器将字节码转换成为最终的机器码。但是常见的JVM,比如我们大多数情况使用的OracleJDK提供的HotspotJVM,都提供了JIT(Just-In-Time)编译器,也就是通常所说的动态编译器,JIT能够在运行时将热点代码编译成机器码,这种情况下部分热点代码就属于**编译执行**,而不是解释执行了
  - ![](https://raw.githack.com/bGZo/assets/dev/2024/image_1645981467170_0.png)
  - 编译 -> `Java` vs `C/C++`
    - `Javac` 的编译, 编译`Java`源码生成`.class`文件里面实际是字节码,而不是可以直接执行的机器码。
    - __[基础] Java通过字节码和Java虚拟机(JVM)这种跨平台的抽象,屏蔽了操作系统和硬件的细节__
  - 运行, JVM会通过类加载器(Class-Loader)加载字节码,解释或者编译执行。
    - > 主流Java版本中, 如`JDK8`实际是解释和编译混合的一种模式,即所谓的 __混合模式(-Xmixed)__ 。通常运行在server模式的JVM,会进行上万次调用以收集足够的信息进行高效的编译,client模式这个门限是1500次。OracleHotspotJVM内置了两个不同的JITcompiler,C1对应前面说的client模式,适用于对于启动速度敏感的应用,比如普通Java桌面应用;C2对应server模式,它的优化是为长时间运行的服务器端应用设计的。默认是采用所谓的分层编译(TieredCompilation) #hard-understand
    - Java虚拟机启动时,可以指定不同的参数对运行模式进行选择
      - `-Xint`=> 告诉 JVM 只进行解释执行,不对代码进行编译,这种模式抛弃了 JIT 可能带来的性能优势。毕竟解释器(interpreter)是逐条读入,逐条解释运行的。
      - `-Xcomp` => 告诉 JVM 关闭解释器,不要进行解释执行,或者叫作最大优化级别。那你可能会问这种模式是不是最高效啊?简单说,还真未必。
      - `-Xcomp` => 导致 JVM 启动变慢非常多,同时有些 JIT 编译器优化方式,比如分支预测,如果不进行 profiling,往往并不能进行有效优化。
  - 新的编译方式
    - AOT(Ahead-of-TimeCompilation)
      - 直接将字节码编译成机器代码
      - ```shell
        jaotc --output libHelloWorld.so HelloWorld.class
        jaotc --output libjava.base.so --module java.base
        java -XX:AOTLibrary=./libHelloWorld.so,./libjava.base.so HelloWorld
        ```
      - 避免了JIT预热等各方面的开销
        - 比如OracleJDK9就引入了实验性的AOT特性,并且增加了新的jaotc工具
        - 分层编译+AOT via: http://openjdk.java.net/jeps/295
      - AOT也不仅仅是只有这一种方式,业界早就有第三方工具(如GCJ、ExcelsiorJET)提供相关功能
- ## Exception vs Error
  - > 对比 Exception 和 Error,另外,运行时异常与一般异常有什么区别?
  - Exception是程序正常运行中，可以预料的意外情况，可能并且应该被捕获，进行相应处理
  - Error是指在正常情况下，不大可能出现的情况，绝大部分的Error都会导致程序（比如JVM自身）处于非正常的、不可恢复状态
  - Exception又分为**可检查**（checked）异常和**不检查**（unchecked）异常，可检查异常在源代码里必须显式地进行捕获处理，这是编译期检查的一部分
  - \[[Throwable]]
  - ![image.png](../../soul/assets/image_1646036640769_0.png)
  - 两个基本原则
    - **尽量不要捕获类似Exception这样的通用异常，而是应该捕获特定异常**，在这里是Thread.sleep()抛出的InterruptedException
    - 在日常的开发和合作中，我们读代码的机会往往超过写代码，软件工程是门协作的艺术，所以我们有义务让自己的代码能够直观地体现出尽量多的信息，而泛泛的Exception之类，恰恰隐藏了我们的目的
    - 除非深思熟虑了，否则不要捕获Throwable或者Error，这样很难保证我们能够正确程序处理OutOfMemoryError
  - **不要生吞（swallow）异常**。这是异常处理中要特别注意的事情，因为很可能会导致非常难以诊断的诡异情况
    - 如果我们不把异常抛出来，或者也没有输出到日志（Logger）之类，程序可能在后续代码以不可控的方式结束。没人能够轻易判断究竟是哪里抛出了异常，以及是什么原因产生了异常
  - 现在非常火热的反应式编程（ReactiveStream），因为其本身是异步、基于事件机制的，所以出现异常情况，决不能简单抛出去；另外，由于代码堆栈不再是同步调用那种垂直的结构，这里的异常处理和日志需要更加小心，我们看到的往往是特定executor的堆栈，而不是业务方法调用关系。对于这种情况，你有什么好的办法吗？