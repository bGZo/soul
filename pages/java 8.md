icon:: ☕
created:: [[20240612]]

- ## Feats
  - **Lambda 表达式 (Lambda Expressions)**
    collapsed:: true
    - Lambda 允许把函数作为一个方法的参数（函数作为参数传递到方法中）
  - **方法引用 (Method references)**
    collapsed:: true
    - 方法引用提供了非常有用的语法，可以直接引用已有Java类或对象（实例）的方法或构造器。与lambda联合使用，方法引用可以使语言的构造更紧凑简洁，减少冗余代码。
  - **默认方法(Default methods)**
    collapsed:: true
    - 默认方法就是一个在接口里面有了一个实现的方法。
  - **新工具**
    collapsed:: true
    - 新的编译工具，如：Nashorn引擎 jjs、 类依赖分析器jdeps。
  - **Stream API**
    collapsed:: true
    - 新添加的Stream API（java.util.stream） 把真正的函数式编程风格引入到Java中。
  - **Date Time API**
    collapsed:: true
    - 加强对日期与时间的处理。
  - **Optional 类**
    collapsed:: true
    - Optional 类已经成为 Java 8 类库的一部分，用来解决空指针异常。
  - **Nashorn, JavaScript 引擎**
    collapsed:: true
    - Java 8提供了一个新的Nashorn javascript引擎，它允许我们在JVM上运行特定的javascript应用。
  - ---
  - 重复注解（Repeating Annotations）。重复注解提供了在同一声明或类型中多次应用相同注解类型的能力。
  - 类型注解（Type Annotation）。在任何地方都能使用注解，而不是在声明的地方。
  - 类型推断增强。
  - 方法参数反射（Method Parameter Reflection）。
  -
  - HashMap改进，在键值哈希冲突时能有更好表现。
  -
  - java.util 包下的改进，提供了几个实用的工具类。
    - 并行数组排序。
    - 标准的Base64编解码。
    - 支持无符号运算。
  - java.util.concurrent 包下增加了新的类和方法。
    - `java.util.concurrent.ConcurrentHashMap` 类添加了新的方法以支持新的StreamApi和lambada表达式。
    - `java.util.concurrent.atomic` 包下新增了类以支持可伸缩可更新的变量。
    - `java.util.concurrent.ForkJoinPool`类新增了方法以支持 common pool。
    - 新增了`java.util.concurrent.locks.StampedLock`类，为控制读/写访问提供了一个基于性能的锁，且有三种模式可供选择。
  - HotSpot
    - 删除了 永久代（PermGen）.
    - 方法调用的字节码指令支持默认方法。
-
- ## ↩ Reference
  - [Java 5，6，7，8，9，10新特性吐血总结 | 拔剑少年的博客](https://it18monkey.github.io/2018/08/05/Java%E6%96%B0%E7%89%B9%E6%80%A7%E6%80%BB%E7%BB%93/)
    - [JDK Release Notes](http://www.oracle.com/technetwork/java/javase/jdk-relnotes-index-2162236.html)
    - [What’s New in JDK 8](http://www.oracle.com/technetwork/java/javase/8-whats-new-2157071.html)
    - [What’s New in JDK 9](https://docs.oracle.com/javase/9/whatsnew/toc.htm#JSNEW-GUID-C23AFD78-C777-460B-8ACE-58BE5EA681F6)
    - [JDK 10 Release Notes](http://www.oracle.com/technetwork/java/javase/10-relnote-issues-4108729.html#NewFeature)
    - [JDK 11 Release Notes](https://www.oracle.com/technetwork/java/javase/11-relnote-issues-5012449.html#NewFeature)
  - [Java 8 新特性 | 菜鸟教程](https://www.runoob.com/java/java8-new-features.html)