- Java平台的理解？
  collapsed:: true
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
- Exception vs Error
  collapsed:: true
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
- final、finally、finalize有什么不同
  collapsed:: true
  - final 的好处
    - 方法 / 类 不可修改；
    - 值不可修改，避免意外；
    - 引入了不可变（immutable）的效果；
      - 用于保护只读数据，尤其是在并发编程中
      - 但是 final 不是 immutable
        - ```java
          final List<String> strList = new ArrayList<>();
          strList.add("Hello");
          strList.add("world");  
          // NOTE: 
          // final 只能约束 strList 这个引用不可以被赋值
          // strList 对象行为不被 final 影响
          
          List<String> unmodifiableStrList = List.of("hello", "world");
          unmodifiableStrList.add("again");
          // NOTE:
          // List.of http://openjdk.java.net/jeps/269
          // 创建的本身就是不可变 List，因此会抛出异常
          ```
        - Java 要实现不可变类
          - 将 class 自身声明为 final
            logseq.order-list-type:: number
            - 不能扩展来绕过限制
              logseq.order-list-type:: number
          - 将所有成员变量定义为 private 和 final，并且不要实现 setter 方法
            logseq.order-list-type:: number
          - logseq.order-list-type:: number
            通常构造对象时，成员变量使用深度拷贝来初始化，而不是直接赋值，这是一种防御措施，因为你无法确定输入对象不被其他人修改。
          - 如果确实需要实现 getter 方法，或者其他可能会返回内部状态的方法，使用 copy-on-write 原则，创建私有的 copy
            logseq.order-list-type:: number
          - TODO ？没看懂这个，原则也适合并发编程
            logseq.order-list-type:: number
    - JVM 将方法进行内联，提高性能；
  - finally 的代码块不一定会被全部执行
    - ```java
      try {
        // do something
        System.exit(1);
      } finally{
        System.out.println(“Print from finally”);
      }
      ```
  - finalize 是基础类 java.lang.Object 的一个方法，它的设计目的是保证对象在被垃圾收集前完成特定资源的回收。finalize 机制现在已经不推荐使用，并且在 JDK 9 开始被标记为 deprecated。
    - 这还是不可预测、不能保证的，所以本质上还是不能指望。实践中，因为 finalize 拖慢垃圾收集，导致大量对象堆积，也是一种典型的导致 OOM 的原因。你无法保证 finalize 什么时候执行，执行的是否符合预期。使用不当会影响性能，导致程序死锁、挂起等。
    - 一旦实现了非空的 finalize 方法，就会导致相应对象回收呈现数量级上的变慢，有人专门做过 benchmark，大概是 40~50 倍的下降。因为，finalize 被设计成在对象**被垃圾收集前**调用，这就意味着实现了 finalize 方法的对象是个“特殊公民”，JVM 要对它进行额外处理。finalize 本质上成为了快速回收的阻碍者，可能导致你的对象经过多个垃圾收集周期才能被回收。
    - finalize 还会掩盖资源回收时的出错信息
      - ```java
        private void runFinalizer(JavaLangAccess jla) {
          //  ... 省略部分代码
          try {
            Object finalizee = this.get(); 
            if (finalizee != null && !(finalizee instanceof java.lang.Enum)) {
              jla.invokeFinalize(finalizee);
              // Clear stack slot containing this variable, to decrease
              // the chances of false retention with a conservative GC
              finalizee = null;
            }
          } catch (Throwable x) { }
          super.clear(); 
        }
        ```
    - Java 平台目前在逐步使用 java.lang.ref.Cleaner 来替换掉原有的 finalize 实现。Cleaner 的实现利用了幻象引用（PhantomReference），这是一种常见的所谓 post-mortem 清理机制。我会在后面的专栏系统介绍 Java 的各种引用，利用幻象引用和引用队列，我们可以保证对象被彻底销毁前做一些类似资源回收的工作，比如关闭文件描述符（操作系统有限的资源），它比 finalize 更加轻量、更加可靠。
      - 吸取了 finalize 里的教训，每个 Cleaner 的操作都是独立的，它有自己的运行线程，所以可以避免意外死锁等问题。
      - 实践中，我们可以为自己的模块构建一个 Cleaner，然后实现相应的清理逻辑。下面是 JDK 自身提供的样例程序：
      - ```JAVA
        public class CleaningExample implements AutoCloseable {
          // A cleaner, preferably one shared within a library
          private static final Cleaner cleaner = <cleaner>;
          static class State implements Runnable { 
            State(...) {
              // initialize State needed for cleaning action
            }
            public void run() {
              // cleanup action accessing State, executed at most once
            }
          }
          private final State;
          private final Cleaner.Cleanable cleanable
            public CleaningExample() {
            this.state = new State(...);
            this.cleanable = cleaner.register(this, state);
          }
          public void close() {
            cleanable.clean();
          }
        }
        ```
      - 注意，从可预测性的角度来判断，Cleaner 或者幻象引用改善的程度仍然是有限的，如果由于种种原因导致幻象引用堆积，同样会出现问题。所以，Cleaner 适合作为一种最后的保证手段，而不是完全依赖 Cleaner 进行资源回收，不然我们就要再做一遍 finalize 的噩梦了。
      - 我也注意到很多第三方库自己直接利用幻象引用定制资源收集，比如广泛使用的 MySQL JDBC driver 之一的 mysql-connector-j，就利用了幻象引用机制。幻象引用也可以进行类似链条式依赖关系的动作，比如，进行总量控制的场景，保证只有连接被关闭，相应资源被回收，连接池才能创建新的连接。
      - 另外，这种代码如果稍有不慎添加了对资源的强引用关系，就会导致循环引用关系，前面提到的 MySQL JDBC 就在特定模式下有这种问题，导致内存泄漏。上面的示例代码中，将 State 定义为 static，就是为了避免普通的内部类隐含着对外部对象的强引用，因为那样会使外部对象无法进入幻象可达的状态。
- 强引用、软引用、弱引用、幻象引用
  collapsed:: true
  - 不同的引用类型，主要体现的是**对象不同的可达性（reachable）状态和对垃圾收集的影响**。
  - 强引用 Strong Reference
    - 最常见的普通对象引用
    - 只要还有强引用指向一个对象，就能表明对象还“活着”，垃圾收集器不会碰这种对象。
      - 只要超过了引用的作用域或者显式地将相应（强）引用赋值为 null
        - 就是可以被垃圾收集的了
        - 当然具体回收时机还是要看垃圾收集策略。
  - 软引用 Soft Reference
    - 相对强引用弱化一些的引用
    - 只有当 JVM 认为内存不足时 (OutOfMemoryError)，才会去试图回收软引用指向的对象
    - 实现内存敏感的缓存
      - 如果还有空闲内存，就可以暂时保留缓存
      - 当内存不足时清理掉，这样就保证了使用缓存的同时，不会耗尽内存。
  - 弱引用 Weak Reference
    - 用来构建一种没有特定约束的关系
      - 比如，
        - 维护一种非强制性的映射关系
          - 如果试图获取时对象还在，就使用它，否则重现实例化
        - 它同样是很多缓存实现的选择
    - 不能使对象豁免垃圾收集
  - 幻象引用 / 虚引用
    - 不能通过它访问对象
    - 提供了一种确保对象被 finalize 以后，做某些事情的机制
      - 比如
        - 通常用来做所谓的 Post-Mortem 清理机制，
        - Java 平台自身 Cleaner 机制等，也有人利用幻象引用监控对象的创建和销毁
  - 对象可达性状态流转分析 =>  JVM 垃圾收集器决定如何处理对象的部分考虑
    - ![](https://raw.githack.com/bGZo/assets/dev/2024/对象可达性状态流转分析.png)
      Java 定义的不同可达性级别（reachability level）
      - 强可达（Strongly Reachable）
        - 就是当一个对象可以有一个或多个线程可以不通过各种引用访问到的情况。
        - 比如，我们新创建一个对象，那么创建它的线程对它就是强可达。
      - 软可达（Softly Reachable）
        - 只能通过软引用才能访问到对象的状态。
      - 弱可达（Weakly Reachable）
        - 无法通过强引用或者软引用访问，只能通过弱引用访问时的状态
          - 这是十分临近 finalize 状态的时机，当弱引用被清除的时候，就符合 finalize 的条件了
      - 幻象可达（Phantom Reachable），
        - 没有强、软、弱引用关联，并且 finalize 过了，只有幻象引用指向这个对象的时候。
      - 不可达（unreachable）
        - 意味着对象可以被清除了
    -
  - #+BEGIN_NOTE
    充分理解这些引用，对于我们设计可靠的缓存等框架，或者诊断应用 OOM 等问题，会很有帮助。比如，诊断 MySQL connector-j 驱动在特定模式下（useCompression=true）的内存泄漏问题，就需要我们理解怎么排查幻象引用的堆积问题。
    #+END_NOTE
-