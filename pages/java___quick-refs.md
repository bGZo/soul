title:: java/quick-refs
alias:: quick-refs/java
- [Java 速成 - OI Wiki](https://oi-wiki.org/lang/java/)
  - `final` 含义是这是最终的、不可更改的结果，被 `final` 修饰的变量只能被赋值一次，赋值后不再改变
  - 可以对变量进行格式化输出
  - 第二种是类似 C++ 的 `foreach` 使用方法，用于循环数组或者集合中的数据，相当于把上一种方式中的循环变量隐藏起来了
  - 创建 Java 源程序需要类名和文件名一致才能编译通过，否则编译器会提示找不到类。通常该文件名会在具体 OJ 中指定
- [java中为什么给float类型变量赋值需要加F，而给byte、short赋值的时候却不需要呢？](https://www.zhihu.com/question/274137101)
  collapsed:: true
  - 在JVM看来，short,byte,int都是同一个东西。
    - JVM规范中所说，并没有说float，int,byte等占多少个字节，而是真正的有效位是多少。比如byte的有效位是1个字节，也就是-128到127。使用Java编程的时候，就只能用byte表示-128到127之间的数，而真正JVM实现，一般byte还是占用和int一样大小:4个字节。
    - 这也就解释了为什么byte,short使用int字面量赋值的时候会不用强制转型。
    - 同时在通过JVM在操作byte,short,int都是用的相同的指令：iconst,bipush等也能证明。
  - double 和 float 在JVM中存储是不一样的
    - double
      ![image.png](../assets/image_1650599505333_0.png)
    - float
      ![image.png](../assets/image_1650599512223_0.png)
  - 因此在使用 double 给 float 赋值的时候，会报错的
    - 0.1+0.2≠0.3
      - 由于float 和 double的精确度不一样，会带来确确实实的**精度损失**
      - ```java
        float a=5.8f
        ```
        - 使用 `IEEE754` 标准: $$1.45*2^{2}$$, 也就是：
        - $$0 (符号位 0) 10000001 (指数位129) 01 1100 1100 1100 1100 1100 1(尾数 0.45)$$
        - 单精度尾数: **23**位
        - 双精度尾数: **52**位
        - 所以如果和**整型一样如果让编译器帮你判断是不是有精度损失**就会出现一会需要加后缀
        - 必须使用 double 赋值给 float 就表示，我接收这种精度损失。
-
-
-
-