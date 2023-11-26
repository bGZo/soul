title:: Snailclimb/JavaGuide
tags:: #Github #Java
url:: [Snailclimb/JavaGuide: 「Java学习+面试指南」一份涵盖大部分 Java 程序员所需要掌握的核心知识。准备 Java 面试，首选 JavaGuide！](https://github.com/Snailclimb/JavaGuide) ![](https://img.shields.io/github/stars/Snailclimb/JavaGuide)
start-date:: 20221207
end-date:: 
mark::

- Content
  - Java 基础常见知识点&面试题总结
    via: https://github.com/Snailclimb/JavaGuide/blob/main/docs/java/basis/java-basic-questions-01.md; https://github.com/Snailclimb/JavaGuide/blob/main/docs/java/basis/java-basic-questions-02.md; https://github.com/Snailclimb/JavaGuide/blob/main/docs/java/basis/java-basic-questions-03.md
    - 基础概念&常识
      collapsed:: true
      - Java 语言有哪些特点?
        collapsed:: true
        - 1. 简单易学
        - 2. 面向对象
        - 3. 跨平台 [[jvm]]
        - collapsed:: true
          4. 支持多线程 [[multithreading/java]]
          - C++11 之前没有内置的多线程机制 (调用操作系统的多线程功能)
        - 5. 可靠性
        - 6. 安全性
        - collapsed:: true
          7. 网络编程
          - Java 语言诞生本身就是为简化网络编程设计
        - 8. 编译与解释并存
      - [[jvm]] #vs [[jdk]] #vs [[jre]]
      - 什么是字节码? 采用字节码的好处是什么?
      - 为什么不全部使用 AOT 呢?
      - 为什么说 Java 语言“编译与解释并存”?
      - Oracle JDK vs OpenJDK
      - Java 和 C++ 的区别?
    - 基本语法
      collapsed:: true
      - 注释有哪几种形式?
      - 标识符和关键字的区别是什么?
      - Java 语言关键字有哪些?
      - 自增自减运算符continue、break 和 return 的区别是什么?
      - 变量方法
    - 基本数据类型
      collapsed:: true
      - Java 中的几种基本数据类型了解么?
      - 基本类型和包装类型的区别?
      - 包装类型的缓存机制了解么?
      - 自动装箱与拆箱了解吗? 原理是什么?
      - 为什么浮点数运算的时候会有精度丢失的风险?
      - 如何解决浮点数运算的精度丢失问题?
      - 超过 long 整型的数据应该如何表示?
    - 面向对象基础
      collapsed:: true
      - 面向对象和面向过程的区别?
      - 创建一个对象用什么运算符? 对象实体与对象引用有何不同?
      - 对象的相等和引用相等的区别
      - 类的构造方法的作用是什么?
      - 如果一个类没有声明构造方法，该程序能正确执行吗?
      - 构造方法有哪些特点? 是否可被 override?
      - 面向对象三大特征?
      - 接口和抽象类有什么共同点和区别?
      - 深拷贝和浅拷贝区别了解吗? 什么是引用拷贝?
    - Java 常见类
      collapsed:: true
      - Object
      - String
    - 异常
      collapsed:: true
      - Exception 和 Error 有什么区别?
      - Checked Exception 和 Unchecked Exception 有什么区别?
      - Throwable 类常用方法有哪些?
      - try-catch-finally 如何使用?
      - finally 中的代码一定会执行吗?
      - 如何使用 try-with-resources 代替try-catch-finally?
      - 异常使用有哪些需要注意的地方?
    - 泛型
      collapsed:: true
      - 什么是泛型?有什么作用?
      - 泛型的使用方式有哪几种?
      - 项目中哪里用到了泛型?
    - 反射
      collapsed:: true
      - 何谓反射?
      - 反射的优缺点?
      - 反射的应用场景?
    - 注解
      collapsed:: true
      - 何谓注解?
      - 注解的解析方法有哪几种?
    - SPI
      - 何谓 SPI?
        collapsed:: true
        - SPI / Service Provider Interface / 服务提供者的接口
          - 专门提供给 **开发者(服务提供者或者扩展框架功能)** 去使用的一个接口
          - 将服务接口和具体的服务实现分离开来，将服务调用方和服务实现者解耦
            - 修改或者替换服务实现并不需要修改调用方
          - 程序的**扩展性、可维护性** UP
          - 应用
            - Spring 框架
            - 数据库加载驱动
            - 日志接口
            - Dubbo 的扩展实现, via: [SPI 扩展实现 | Apache Dubbo](https://dubbo.apache.org/zh/docs/v2.7/dev/impls/)
            - ......
      - SPI 和 API 有什么区别? #api
        collapsed:: true
        - ![image.png](../assets/javaguide/image_1670400578900_0.png)
          - 接口规则由接口调用方确定
            - 由不同的厂商去根据这个规则对这个接口进行实现，从而提供服务
      - SPI 的优缺点?
        collapsed:: true
        - 接口设计的灵活性UP
        - 局限
          - 需要遍历加载所有的实现类，不能做到按需加载，这样效率还是相对较低的。
          - 当多个  `ServiceLoader`  同时  `load`  时，会有并发问题
    - 序列化和反序列化
      - 什么是序列化? 什么是反序列化?
      - 如果有些字段不想进行序列化怎么办?
        -
      - 常见序列化协议有哪些?
        collapsed:: true
        - JDK 自带的序列化方式一般不用 (效率低 & 安全问题)
          collapsed:: true
          - TODO 基于二进制的序列化协议 #Project
            - Hessian
            - Kryo
            - Protobuf
            - ProtoStuff
          - 文本类序列化方式
            - JSON
            - XML
            - 一般不会选择
              - 可读性较好, 但性能差
      - 为什么不推荐使用 JDK 自带的序列化?
        collapsed:: true
        - **不支持跨语言调用**
          - 如果调用的是其他语言开发的服务的时候就不支持了
        - **性能差**
          - 相比于其他序列化框架性能更低
            - 序列化之后的字节数组体积较大，导致传输成本加大
        - **存在安全问题**
          - 当输入的反序列化的数据可被用户控制，那么攻击者即可通过构造恶意输入，让反序列化产生非预期的对象，在此过程中执行构造的任意代码
    - I/O
      - Java IO 流了解吗?
      - I/O 流为什么要分为字节流和字符流呢?
        - 不管是文件读写还是网络发送接收，**信息的最小存储单元都是字节**
        - 字符流是由 Java 虚拟机将字节转换得到的，这个过程还算是比较耗时
        - 如果我们不知道编码类型的话，使用字节流的过程中很容易出现乱码问题
      - Java IO 中的设计模式有哪些?
      - BIO、NIO 和 AIO 的区别?
    - 语法糖
      - 什么是语法糖(**Syntactic sugar**, 糖衣语法)?
        - 英 Peter.J.Landin 发明
        - 编程语言为了方便程序员开发程序而设计的一种特殊语法
          - 对编程语言的功能并没有影响
          - 实现相同的功能，基于语法糖写出来的代码往往更简单简洁且更易阅读
        - JVM 其实并不能识别语法糖，Java 语法糖要想被正确执行，需要先通过编译器进行解糖，也就是在程序编译阶段将其转换成 JVM 认识的基本语法。
          - Java 中真正支持语法糖的是 Java 编译器而不是 JVM
            - 如果你去看 `com.sun.tools.javac.main.JavaCompiler` 的源码，你会发现在 `compile()` 中有一个步骤就是调用 `desugar()` ，这个方法就是负责解语法糖的实现的
        - More 语法盐, 语法糖精
      - Java 中有哪些常见的语法糖?
        - switch 支持 String 与枚举
          - **Java 7**
          -
        - 泛型
        - 自动装箱与拆箱
        - 可变长参数
        - 枚举
        - 内部类
        - 条件编译
        - 断言
        - 数值字面量
        - for-each
        - try-with-resource
        - Lambda 表达式
        - 可能遇到的坑
          - 泛型
          - 自动装箱与拆箱
          - 增强 for 循环
-
-
-