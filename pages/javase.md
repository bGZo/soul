icon:: 📄
also:: java-standard-edition
created:: [[20240802]]
wikipedia:: https://en.wikipedia.org/wiki/Java_Platform,_Standard_Edition

- ## Why
- ## How
- ## What
  - Nomenclature, standards and specifications 术语、标准和规范
  - General purpose packages
    - contains [[java-library]]
      collapsed:: true
      - [Object](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Object.html) – the class that is the root of every class hierarchy.
        logseq.order-list-type:: number
      - [Enum](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Enum.html) – the base class for [enumeration classes](https://en.wikipedia.org/wiki/Enumerated_type) (as of J2SE 5.0).
        logseq.order-list-type:: number
      - [Class](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Class.html) – the class that is the root of the Java [reflection](https://en.wikipedia.org/wiki/Reflection_(computer_science)) system.
        logseq.order-list-type:: number
      - [Throwable](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Throwable.html) – the class that is the base class of the exception class hierarchy.
        logseq.order-list-type:: number
      - [Error](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Error.html), [Exception](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Exception.html), and [RuntimeException](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/RuntimeException.html) – the base classes for each exception type.
        logseq.order-list-type:: number
      - [Thread](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Thread.html) – the class that allows operations on threads.
        logseq.order-list-type:: number
      - [String](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/String.html) – the class for [strings](https://en.wikipedia.org/wiki/String_(computer_science)) and [string literals](https://en.wikipedia.org/wiki/String_literal).
        logseq.order-list-type:: number
      - [StringBuffer](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/StringBuffer.html) and [StringBuilder](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/StringBuilder.html) – classes for performing [string manipulation](https://en.wikipedia.org/wiki/StringBuffer_and_StringBuilder) (`StringBuilder` as of J2SE 5.0).
        logseq.order-list-type:: number
      - [Comparable](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Comparable.html) – the interface that allows generic comparison and ordering of objects (as of J2SE 1.2).
        logseq.order-list-type:: number
      - [Iterable](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Iterable.html) – the interface that allows generic iteration using the [enhanced `for` loop](https://en.wikipedia.org/wiki/Foreach#Java) (as of J2SE 5.0).
        logseq.order-list-type:: number
      - [ClassLoader](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/ClassLoader.html), [Process](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Process.html), [Runtime](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Runtime.html), [SecurityManager](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/SecurityManager.html), and [System](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/System.html) – classes that provide "system operations" that manage the [dynamic loading](https://en.wikipedia.org/wiki/Dynamically_loaded_library) of classes, creation of external [processes](https://en.wikipedia.org/wiki/Process_(computing)), host environment inquiries such as the time of day, and enforcement of [security policies](https://en.wikipedia.org/wiki/Security_policy).
        logseq.order-list-type:: number
      - [Math](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/Math.html) and [StrictMath](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/lang/StrictMath.html) – classes that provide basic math functions such as [sine](https://en.wikipedia.org/wiki/Sine), [cosine](https://en.wikipedia.org/wiki/Cosine), and [square root](https://en.wikipedia.org/wiki/Square_root) (`StrictMath` as of J2SE 1.3).
        logseq.order-list-type:: number
      - The [primitive wrapper classes](https://en.wikipedia.org/wiki/Primitive_wrapper_class) that [encapsulate](https://en.wikipedia.org/wiki/Encapsulation_(computer_science)) [primitive types](https://en.wikipedia.org/wiki/Primitive_type) as [objects](https://en.wikipedia.org/wiki/Object_(computer_science)).
        logseq.order-list-type:: number
      - The basic exception classes thrown for language-level and other common exceptions.
        logseq.order-list-type:: number
    - `java.lang`
      - `java.lang.ref`
        - 提供了比其他方式更灵活的[引用](https://en.wikipedia.org/wiki/Reference_(computer_science))类型，允许应用程序和[Java 虚拟机](https://en.wikipedia.org/wiki/Java_virtual_machine)(JVM)[垃圾收集器](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science))之间进行有限的交互。
        - `java.lang.ref`包定义了其他三种类型的引用——软引用、[弱引用](https://en.wikipedia.org/wiki/Weak_reference)和幻像引用 (soft, weak, and phantom references)。每种类型的参考都是针对特定用途而设计的。
      - `java.lang.reflect` [[java-reflection]]
        - basic techniques involved in reflection:
          - Discovery
          - Use by name
    - [`java.io`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/package-summary.html)
      - 中心类: 读取和写入字节流的抽象基类
        - [InputStream](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/InputStream.html)
        - [OutputStream](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/OutputStream.html)
      - 相关类
        - [Reader](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/Reader.html) 和 [Writer](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/Writer.html) 是分别用于读取和写入字符流的抽象基类
      - 杂项类来支持与主机文件系统的交互。
      - `Streams`
        - 流类遵循[装饰器模式](https://en.wikipedia.org/wiki/Decorator_pattern)，通过扩展基子类向流类添加功能。
        - | Source/Destination | Name | Stream types | In/out | Classes |
          | --- | --- | --- | --- | --- |
          | [`byte`](https://en.wikipedia.org/wiki/Byte) [array](https://en.wikipedia.org/wiki/Array_data_type) (`byte[]`) | `ByteArray` | `byte` | in, out | [`ByteArrayInputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/ByteArrayInputStream.html), [`ByteArrayOutputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/ByteArrayOutputStream.html) |
          | `char` array (`char[]`) | `CharArray` | `char` | in, out | [`CharArrayReader`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/CharArrayReader.html), [`CharArrayWriter`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/CharArrayWriter.html) |
          | [file](https://en.wikipedia.org/wiki/Computer_file) | `File` | `byte`, `char` | in, out | [`FileInputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/FileInputStream.html), [`FileOutputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/FileOutputStream.html), [`FileReader`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/FileReader.html), [`FileWriter`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/FileWriter.html) |
          | [string](https://en.wikipedia.org/wiki/String_(computer_science)) ([`StringBuffer`](https://en.wikipedia.org/wiki/StringBuffer_and_StringBuilder)) | `String` | `char` | in, out | [`StringReader`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/StringReader.html), [`StringWriter`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/StringWriter.html) |
          | [thread](https://en.wikipedia.org/wiki/Thread_(computer_science)) (`Thread`) | `Piped` | `byte`, `char` | in, out | [`PipedInputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/PipedInputStream.html), [`PipedOutputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/PipedOutputStream.html), [`PipedReader`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/PipedReader.html), [`PipedWriter`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/PipedWriter.html) |
          logseq.table.version:: 2
        -
        - | Operation | Name | Stream types | In/out | Classes |
          | --- | --- | --- | --- | --- |
          | [buffering](https://en.wikipedia.org/wiki/Buffer_(computer_science)) | `Buffered` | `byte`, `char` | in, out | [`BufferedInputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/BufferedInputStream.html), [`BufferedOutputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/BufferedOutputStream.html), [`BufferedReader`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/BufferedReader.html), [`BufferedWriter`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/BufferedWriter.html) |
          | "push back" last value read | `Pushback` | `byte`, `char` | in | [`PushbackInputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/PushbackInputStream.html), [`PushbackReader`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/PushbackReader.html) |
          | read/write [primitive types](https://en.wikipedia.org/wiki/Primitive_type) | `Data` | `byte` | in, out | [`DataInputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/DataInputStream.html), [`DataOutputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/DataOutputStream.html) |
          | [object serialization](https://en.wikipedia.org/wiki/Object_serialization) (read/write objects) | `Object` | byte | in, out | [`ObjectInputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/ObjectInputStream.html), [`ObjectOutputStream`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/ObjectOutputStream.html) |
          logseq.table.version:: 2
      - Random access
        - [`RandomAccessFile`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/RandomAccessFile.html)
      - File system
        - [`File`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/File.html)
        - [`FileDescriptor`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/io/FileDescriptor.html)
    - `java.nio`
      - 在 J2SE 1.4 中，添加了[`java.nio`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/nio/package-summary.html)包（NIO 或非阻塞 I/O）来支持[内存映射 I/O](https://en.wikipedia.org/wiki/Memory-mapped_I/O) ，使[I/O](https://en.wikipedia.org/wiki/Input/output)操作更接近底层硬件，有时性能显着提高。 `java.nio`包提供了对多种缓冲区类型的支持。子包[`java.nio.charset`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/nio/charset/package-summary.html)提供对字符数据的不同[字符编码](https://en.wikipedia.org/wiki/Character_encoding)的支持。子包[`java.nio.channels`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/nio/channels/package-summary.html)提供对_通道的支持，_通道表示与能够执行 I/O 操作的实体（例如文件和套接字）的连接。 `java.nio.channels`包还提供对文件细粒度锁定的支持。
    - `java.math`
      - [`BigDecimal`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/math/BigDecimal.html)
      - [`BigInteger`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/math/BigInteger.html)
      - [`MathContext`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/math/MathContext.html)
      - [`RoundingMode`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/math/RoundingMode.html)
    - `java.net`
      - 网络提供了特殊的 IO 例程(routines)，允许HTTP请求以及其他常见事务。
    - `java.text`
      - 字符串的解析例程，并支持各种人类可读的语言和特定于语言环境的解析。
    - `java.util`
      - [Collections API](https://en.wikipedia.org/wiki/Collections_API) ，这是一种受[设计模式](https://en.wikipedia.org/wiki/Design_pattern_(computer_science))考虑因素影响很大的有组织的数据结构层次结构。
  - Special purpose packages
    - `java.applet`
    - `java.beans` [[java-beans]]
      - [`java.beans`](https://docs.oracle.com/en/java/javase/19/docs/api/java.desktop/java/beans/package-summary.html)包中包含用于开发和操作 bean 的各种类，以及由[JavaBeans 体系结构](https://en.wikipedia.org/wiki/JavaBeans)定义的可重用组件。该架构提供了操纵组件属性并在这些属性更改时触发事件的机制。
    - `java.awt`
      - [`java.awt`](https://docs.oracle.com/en/java/javase/19/docs/api/java.desktop/java/awt/package-summary.html) （或抽象窗口工具包）提供对一组基本[GUI](https://en.wikipedia.org/wiki/GUI)小部件的访问，这些小部件基于底层本机平台的小部件集、GUI 事件子系统的核心以及本机窗口系统和 Java 应用程序之间的接口。它还提供了几个基本的[布局管理器](https://en.wikipedia.org/wiki/Layout_manager)、与[剪贴板](https://en.wikipedia.org/wiki/Clipboard_(software))和[拖放](https://en.wikipedia.org/wiki/Drag_and_drop)一起使用的数据传输包、[输入设备](https://en.wikipedia.org/wiki/Input_device)（例如[鼠标](https://en.wikipedia.org/wiki/Mouse_(computing))和[键盘）](https://en.wikipedia.org/wiki/Keyboard_(computing))的接口以及对支持系统上的[系统托盘](https://en.wikipedia.org/wiki/System_tray)的访问。该包与`javax.swing`一起包含 JDK 6 中最多数量的枚举（总共 7 个）。
    - `java.rmi`
      - [`java.rmi`](https://docs.oracle.com/en/java/javase/19/docs/api/java.rmi/java/rmi/package-summary.html)包提供[Java 远程方法调用，](https://en.wikipedia.org/wiki/Java_remote_method_invocation)以支持在不同[JVM](https://en.wikipedia.org/wiki/JVM)中运行的两个 Java 应用程序之间的[远程过程调用](https://en.wikipedia.org/wiki/Remote_procedure_call)。
    - `java.security`
      - 对安全性的支持（包括消息摘要算法）包含在[`java.security`](https://docs.oracle.com/en/java/javase/19/docs/api/java.base/java/security/package-summary.html)包中。
    - `java.sql` [[jdbc]]
    - `javax.rmi`
      - [`javax.rmi`](https://docs.oracle.com/javase/8/docs/api/javax/rmi/package-summary.html)包使用 RMI over IIOP 协议为应用程序之间的远程通信提供支持。该协议结合了 RMI 和 CORBA 功能。
      - http://java.sun.com/javase/technologies/core/corba/index.jsp
    - `javax.swing`
      - 基于`java.awt`构建的例程集合，用于提供独立于平台的[小部件工具包](https://en.wikipedia.org/wiki/Widget_toolkit)。 [`javax.swing`](https://docs.oracle.com/en/java/javase/19/docs/api/java.desktop/javax/swing/package-summary.html)使用 2D 绘图例程来呈现用户界面组件，而不是依赖于底层本机[操作系统](https://en.wikipedia.org/wiki/Operating_system)GUI 支持。
    - `javax.swing.text.html.parser`
      - 提供了容错 HTML 解析器，用于编写各种 Web 浏览器和 Web 机器人。
    - `javax.xml.bind.annotation`
      - 定义了用于自定义 Java 程序元素到 XML 模式映射的注释。
  - OMG packages -> remove on [[java11]]
    - `org.omg.CORBA`
    - `org.omg.PortableInterceptor`
- ## Namespace
  - {{namespace java-se}}
- ## ↩ Reference
  - ### `Object`
    collapsed:: true
    -
    -
    -
    - ```java
      /**
       * Returns the runtime class of this {@code Object}. The returned
       * {@code Class} object is the object that is locked by {@code
       * static synchronized} methods of the represented class.
       *
       */
      public final native Class<?> getClass()
        /**
           * Returns a hash code value for the object. This method is
           * supported for the benefit of hash tables such as those provided by
           * {@link java.util.HashMap}.
           * <p>
           * The general contract of {@code hashCode} is:
           * <ul>
           * <li>Whenever it is invoked on the same object more than once during
           *     an execution of a Java application, the {@code hashCode} method
           *     must consistently return the same integer, provided no information
           *     used in {@code equals} comparisons on the object is modified.
           *     This integer need not remain consistent from one execution of an
           *     application to another execution of the same application.
           * <li>If two objects are equal according to the {@code equals(Object)}
           *     method, then calling the {@code hashCode} method on each of
           *     the two objects must produce the same integer result.
           * <li>It is <em>not</em> required that if two objects are unequal
           *     according to the {@link java.lang.Object#equals(java.lang.Object)}
           *     method, then calling the {@code hashCode} method on each of the
           *     two objects must produce distinct integer results.  However, the
           *     programmer should be aware that producing distinct integer results
           *     for unequal objects may improve the performance of hash tables.
           * </ul>
           * <p>
           * As much as is reasonably practical, the hashCode method mark:: d by
           * class {@code Object} does return distinct integers for distinct
           * objects. (This is typically implemented by converting the internal
           * address of the object into an integer, but this implementation
           * technique is not required by the
           * Java&trade; programming language.)
           *
           * @return  a hash code value for this object.
           * @see     java.lang.Object#equals(java.lang.Object)
           * @see     java.lang.System#identityHashCode
           */
        public native int hashCode()
      /**
       * 用于比较 2 个对象的内存地址是否相等，String 类对该方法进行了重写以用于比较字符串的值是否相等
       */
      public boolean equals(Object obj)
      /**
       * 用于创建并返回当前对象的一份拷贝。
       */
      protected native Object clone() throws CloneNotSupportedException
      /**
       * 返回类的名字实例的哈希码的 16 进制的字符串。建议 Object 所有的子类都重写这个方法
       */
      public String toString()
      /**
       * 唤醒一个在此对象监视器上等待的线程(监视器相当于就是锁的概念); 如果有多个线程在等待只会任意唤醒一个。
       */
      public final native void notify()
      /**
       * 跟 notify 一样，唯一的区别就是会唤醒在此对象监视器上等待的所有线程，而不是一个线程。
       */
      public final native void notifyAll()
      /**
       * 暂停线程的执行。注意：sleep 方法没有释放锁，而 wait 方法释放了锁 ，timeout 是等待时间。
       */
      public final native void wait(long timeout) throws InterruptedException
      /**
       * 多了 nanos 参数，这个参数表示额外时间（以毫微秒为单位，范围是 0-999999）
       * 所以超时的时间还需要加上 nanos 毫秒
       */
      public final void wait(long timeout, int nanos) throws InterruptedException
      /**
       * 跟之前的 2个wait方法一样，只不过该方法一直等待，没有超时时间这个概念
       */
      public final void wait() throws InterruptedException
      /**
       * 实例被垃圾回收器回收的时候触发的操作
       */
      protected void finalize() throws Throwable { }
      ```
    -
    - `final`: 不能重写
    - `native`
      - java调用非java代码的接口
      - 该方法的实现由非java语言实现
    - `==` vs `equal()`
      - | Items | `==`| `equal` |
        | 判断基本类型 | ✔| ✖ |
        | 基本类型 / 引用类型 | 值 / 对象内存地址  | 是否重写(判断地址(`==`)/属性) |
        - 对象内存地址的本质也是值
        - ```java
          public boolean equals(Object anObject) {
              if (this == anObject) {
                  return true;
              }
              if (anObject instanceof String) {
                  String anotherString = (String)anObject;
                  int n = value.length;
                  if (n == anotherString.value.length) {
                      char v1[] = value;
                      char v2[] = anotherString.value;
                      int i = 0;
                      while (n-- != 0) {
                          if (v1[i] != v2[i])
                              return false;
                          i++;
                      }
                      return true;
                  }
              }
              return false;
          }
          ```
    - `hashCode`
      - `hashCode()` 和 `equals()` => 都是比较两个对象是否相等
        - >当你把对象加入 HashSet 时，HashSet 会先计算对象的 hashCode 值来判断对象加入的位置，同时也会与其他已经加入的对象的 hashCode 值作比较 ...
      - Why
        - hashCode 帮助我们大大缩小了查找成本
          id:: 627f46cb-603f-44dc-8e46-11e2c5fda18f
      - 为什么重写 equals() 时必须重写 hashCode() 方法
        - 避免 equals 判断相等的两个对象，hashCode 值却不相等
  - ### `String`
    collapsed:: true
    - DONE `String` vs `StringBuffer` vs `StringBuilder`
      collapsed:: true
      - |Items|`String` | `StringBuffer` | `StringBuilder`|
        | 可变 | ✖ | ✔|✔|
        | 安全 | ✔|✔|✖|
        | 性能 | 创建新`String`| 修改对象本身 | 较前者高|
        | 场景 | 少量的数据 | 多线程大量数据 | 单线程大量数据 |
      - String 和 StringBuffer 都是 JDK 1.0 引入的；StringBuilder 是 JDK1.5 引入的；
      - String 是常量（constant），即不可变类（immutable），但是可以被共享（shared）
        - String 的 Append, Concatenation 是通过后两者实现的；
          collapsed:: true
          - `+` 拼接实际上是通过 `StringBuilder` 调用 `append()`+`toString()` 拿到的
            collapsed:: true
            - ```java
              String str1 = "he";
              String str2 = "llo";
              String str3 = "world";
              String str4 = str1 + str2 + str3;
              ```
              ![image.png](../../soul/assets/image_1652511452678_0.png){:height 179, :width 422}
          - 注意**循环**
            - 编译器不会创建单个 StringBuilder 以复用，会导致创建过多的 StringBuilder 对象
          - 注意编译器优化 => 常量折叠(Constant Folding)
            - 基本数据类型 (byte / short / boolean / char / int / float / long / double)
            - 常量
              - final 修饰
                - 基本数据类型
                - 字符串变量
              - ...
            - 字符串通过 `+` 拼接得到的字符串
            - 基本数据类型之间算数运算（加减乘除）
            - 基本数据类型的位运算 (`<<` / `>>` / `>>>` )
            - 例外无法优化
              - 引用的值在程序编译期是无法确定的
              - ```java
                String str4 = new StringBuilder().append(str1).append(str2).toString();
                ```
              - 我们在平时写代码的时候，尽量避免多个字符串对象拼接，因为这样会重新创建对象。如果需要改变字符串的话，可以使用 StringBuilder 或者 StringBuffer。
              - 不过，字符串使用 final 关键字声明之后，可以让编译器当做常量来处理。
        - Immutable 体现在
          - 字符数组被 final 修饰 + 私有 + String 类没有提供/暴露修改这个字符串的方法
          - String 类被 final 修饰导致其不能被继承，进而避免了子类破坏 String 不可变
        - 字符串常量
          - [[jvm]] 为了提升性能和减少内存消耗针对字符串（String 类）专门开辟的一块区域
            id:: 627f533c-23e0-4a2d-95d2-ac1cc7d4b48a
          - 避免字符串的重复创建
      - ---
      - Java 9 之后，String 、StringBuilder 与 StringBuffer 的实现改用 **byte 数组** 存储字符串
        collapsed:: true
        - 新版的 String 支持两个编码方案 (Latin-1 / UTF-16)
          - 区别在 **包含的汉字 是否超过 Latin-1 可表示范围**
            collapsed:: true
            - 超过
              - UTF-16
              - 两者效率一样
            - 未超过
              - Latin-1
              - 节约一半内存 (char 两字节 vs byte 一字节)
        - 如果字符串中内的字符，byte 和 char 所占用的空间是一样的。
        - 这是官方的介绍: https://openjdk.java.net/jeps/254
      - More via: [Java基础常见面试题总结(中) | JavaGuide(Java面试+学习指南)](https://javaguide.cn/java/basis/java-basic-questions-02.html#string)
        - String s1 = new String("abc");这句话创建了几个字符串对象?
          collapsed:: true
          - 1
            - 字符串常量池中不存在字符串对象“abc”的引用
              id:: 627f53ab-3f52-48ab-a823-fd7556e2e219
            - 堆中创建 2 个字符串对象“abc”
            - ```java
              String s1 = new String("abc");
              ```
              ![image.png](../../soul/assets/image_1652511720975_0.png)
          - 2
            - 堆中创建 1 个字符串对象“abc”
            - id:: 627f53f0-8112-42d8-9d91-bc52dd28b4b6
              ```java
              // 字符串常量池中已存在字符串对象“abc”的引用
              String s1 = "abc";
              // 下面这段代码只会在堆中创建 1 个字符串对象“abc”
              String s2 = new String("abc");
              ```
              ![image.png](../../soul/assets/image_1652511728904_0.png)
        - `intern` 方法有什么作用?
          collapsed:: true
          - 如果字符串常量池中保存了对应的字符串对象的引用，就直接返回该引用
          - 如果字符串常量池中没有保存了对应的字符串对象的引用，那就在常量池中创建一个指向该字符串对象的引用并返回
          - ```java
            // 在堆中创建字符串对象”Java“
            // 将字符串对象”Java“的引用保存在字符串常量池中
            String s1 = "Java";
            // 直接返回字符串常量池中字符串对象”Java“对应的引用
            String s2 = s1.intern();
            // 会在堆中在单独创建一个字符串对象
            String s3 = new String("Java");
            // 直接返回字符串常量池中字符串对象”Java“对应的引用
            String s4 = s3.intern();
            // s1 和 s2 指向的是堆中的同一个对象
            System.out.println(s1 == s2); // true
            // s3 和 s4 指向的是堆中不同的对象
            System.out.println(s3 == s4); // false
            // s1 和 s4 指向的是堆中的同一个对象
            System.out.println(s1 == s4); //true
            ```
          -
    - DONE `Hashcode()`
      collapsed:: true
      - $$s[0]*31^{n-1} + s[1]*31^{n-2} + ... + s[n-1]$$
      - ```java
        /**
        * Returns a hash code for this string. The hash code for a
        * {@code String} object is computed as
        * <blockquote><pre>
        * s[0]*31^(n-1) + s[1]*31^(n-2) + ... + s[n-1]
        * </pre></blockquote>
        * using {@code int} arithmetic, where {@code s[i]} is the
        * <i>i</i>th character of the string, {@code n} is the length of
        * the string, and {@code ^} indicates exponentiation.
        * (The hash value of the empty string is zero.)
        *
        * @return  a hash code value for this object.
        */
        public int hashCode() {
          int h = hash;
          if (h == 0 && value.length > 0) {
            hash = h = isLatin1() ? StringLatin1.hashCode(value)
              : StringUTF16.hashCode(value);
          }
          return h;
        }
        /** 它首先检查是否已经计算过哈希值，
          * 如果没有，则根据字符串是 Latin1 编码还是 UTF16 编码，
          * 调用不同的方法来计算哈希值，并将结果保存在 hash 字段中。
          */
        ```
      - 假设有一个字符串 “Hello”，它的哈希值是这样计算的：
      - ```java
        "Hello".hashCode() =
          'H'*31^4 + 'e'*31^3 + 'l'*31^2 + 'l'*31^1 + 'o'*31^0 =
          72*923521 + 101*29791 + 108*961 + 108*31 + 111 =
          66430125 + 3007631 + 103788 + 3348 + 111 =
          69609603
        ```
      - 所以，“Hello” 的哈希值是 69609603。
    -
    - ### `String xxx=""` vs `String xxx=new String()`;
      collapsed:: true
      - 字符串来源不同; 前者可能是字符串常量池, 有使用隐患; 后者是显示声明, 没什么安全隐患.
        1. may reuse an instance from the string constant pool if one is available
        2. explicitly creates a new and referentially distinct instance of a String object
      - Like [[cpp/construct-function]] explicit constructor. 前者属于编译器的隐式转换
      - > String(String original) : Initializes a newly created String object so that it represents the same sequence of characters as the argument; in other words, the newly created string is a copy of the argument string. Unless an explicit copy of original is needed, use of this constructor is unnecessary since strings are immutable.
        > via: https://stackoverflow.com/questions/3052442/what-is-the-difference-between-text-and-new-stringtext
    - ### `Basic Type` -> `String` 基本数据类型转换成字符串
      - 包装类的 `toString()`
        id:: 8eaf0195-70c7-4f6f-b873-5483744b5a65
        - ```java
          int c = 10;
          String str1 = Integer.toString(c);
          ```
      - String类的 `valueOf()`
        - ```java
          String str2 = String.valueOf(c);
          ```
      - 一个空字符串加上基本类型
        - ```java
          String str3 = c + "";
          ```
    - ### String -> `Basic Type` 字符串转换成基本数据类型
      collapsed:: true
      - 包装类的 `parseXXX()` 方法
        id:: 62454172-94ba-4c50-9a48-8870059d6bd9
        - ```java
          String str = "10";
          int d = Integer.parseInt(str);
          ```
      - 包装类的 `valueOf()` 方法转换为基本数据类型的包装类
        - ```java
          int e = Integer.valueOf(str);
          ```
  - String
    collapsed:: true
    - `length()`
      id:: 624167fa-9604-4ebb-aa07-a292f402289d
    - `compareTo(String str)`
      - 相等，返回0。不相等时，从两个字符串第1个字符开始比较，返回第一个不相等的字符差；另一种情况，较长字符串的前面部分恰巧是较短的字符串，返回它们的长度差
    - `substring(int[, int])`
    - `indexOf(String str)`
    - `lastIndexOf(String str)`
    - `equals(` **`Object`** ` obj)`
    - `String trim()`: 取出了前后空格的字符串
    - `String[] split(String str)`
    - #code-logic 邮箱验证逻辑 -> 正则/ 有`.` & `@`+ 1 <`.` & 中间都非空
    - `StringBuffer`
      id:: 62418a62-9c50-43d7-a5fa-49af14faeca9
      - 字符串处理时，不生成新的对象，所以在内存使用上，StringBuffer类要优于String类
      - `append()`
      - `length()`
      - `capacity()`
      - `charAt(int index)`
      - `delete()`
      - `deleteCharAt(int index)`
      - `ensureCapacity(int capacity)`
        id:: 62418ce5-a2f2-4e46-9f11-806379d93f4a
      - `insert()`
      - `reverse()`
      - `replace()`
        id:: 62418cf8-10f1-4033-bf7f-2010d59fabe4
      - `appendCodePoint(int codePoint)`
      - `StringBuffer` -> `String`: `StringBuffer.toString()`
        id:: 62418853-57b2-49f2-bcad-3e2665be6420
      - `String` -> `StringBuffer`:`StringBuffer.append()`
-