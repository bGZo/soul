tags:: #java

- [600+ 道 Java面试题及答案整理_牛客网](https://www.nowcoder.com/discuss/1023635)
  collapsed:: true
  - Java 基础
    - DONE 1、面向对象编程有哪些特征？（3）
    - DONE 2、JDK 与 JRE 的区别是什么？
    - DONE 3、Java 有哪几种基本数据类型？（4类8种）
    - ==`4、== 和 equals 比较有什么区别？`==
      collapsed:: true
      - [== 用于比较两个引用是否指向同一个对象，而 equals 用于比较两个对象是否相等](https://www.cnblogs.com/guoyafenghome/p/8542097.html)[1](https://www.cnblogs.com/guoyafenghome/p/8542097.html)[2](https://blog.csdn.net/yujing1314/article/details/105898947)。
      - [对于基本数据类型，== 比较的是它们的值是否相等，而对于引用数据类型，== 比较的是它们在堆内存中的地址是否相等](https://blog.csdn.net/meism5/article/details/89029475)[3](https://blog.csdn.net/meism5/article/details/89029475)。
      - [equals 方法存在于 Object 类中，所有类都继承自 Object 类，但是不同的类可以重写 equals 方法来定义自己的相等规则](https://zhuanlan.zhihu.com/p/121603364)[4](https://zhuanlan.zhihu.com/p/121603364)[5](https://zhuanlan.zhihu.com/p/78395057)。
      - [对于 String 类，如果使用字面量赋值，那么 == 和 equals 都会返回 true，因为字面量会被存储在字符串常量池中，共享同一个地址。但是如果使用 new 关键字创建字符串对象，那么 == 会返回 false，因为 new 会分配新的内存空间。equals 仍然会返回 true，因为 String 类重写了 equals 方法来比较字符串内容](https://www.cnblogs.com/guoyafenghome/p/8542097.html)[1](https://www.cnblogs.com/guoyafenghome/p/8542097.html)[5](https://zhuanlan.zhihu.com/p/78395057)。
    - DONE 5、public,private,protected,默认的区别？
    - ==`6、this 和 super 有什么区别？`==
      collapsed:: true
      - this 指代的是当前对象，super 指代的是父类对象。
      - this 可以用来区分成员变量和局部变量，super 可以用来访问父类的属性和方法。
      - this 可以用来调用本类的其他构造方法或普通方法，super 可以用来调用父类的构造方法或普通方法。
      - this 和 super 都必须放在构造方法内第一行，不能同时出现在一个构造方法里面。
        - [java规定，在执行构造函数之前必须执行父类的构造函数，直到这个类是java.lang.Object类的构造函数](https://blog.csdn.net/qq_42848910/article/details/104481271)
        - 然而函数的入口是子类构造函数，因此任何构造函数第一句,必须是执行父类构造函数，如果没有添加super关键字，那么编译器会为该构造函数第一句添加一个super()语句(你可以这么理解，当然编译以后并不是这样)。如果有super关键字显示的调用父类构造函数，就是用指定的那个父类构造函数，否则使用默认的无参构造函数。
        - 也有一种情况例外，就是存在this()，调用本类其它构造函数，但是按照递归调用，最终还是会调用父类构造函数;如果this()和super()都存在,那么就会出现:初始化父类两次的不安全操作，因为当super()和this()同时出现的时候，在调用完了super()之后 还会执行this()，而this()中又会自动调用super(),这就造成了调用两次super()的结果。
        - 如果你继承的父类没有无参数构造函数，那么你这个类第一句必须显示的调用super关键字,来调用父类对应的有参构造函数，否则不能通过编译。
    - DONE 7、short s1 = 1; s1 += 1;有错吗？
      collapsed:: true
      - 因为s1 += 1是一个赋值表达式，Java编译器会对它进行特殊处理，不会改变s1的类型。但是如果写成s1 = s1 + 1，就会出错，因为s1 + 1的结果是int类型，需要强制转换才能赋值给short类型的s1。
    - DONE 8、short s1 = 1; s1 = s1 + 1;有错吗？
    - ==`9、float n = 1.8 有错吗？`==
      collapsed:: true
      - 如果你使用的是 Java，那么 float n = 1.8 有错，因为 1.8 是一个 double 类型的字面量，不能直接赋值给 float 类型的变量。你需要在 1.8 后面加上 f 或 F，表示它是一个 float 类型的字面量，例如：
      - float n = 1.8f;
      - 或者你可以用强制类型转换，将 double 类型转换为 float 类型，例如：
      - float n = (float) 1.8;
      - 但是这样可能会损失一些精度。
    - DONE 10、i++ 和 ++i 的区别？
    - DONE 11、while 和 do while 有啥区别？
    - DONE 12、如何跳出 Java 中的循环？
    - DONE 13、如何跳出 Java 中间的多层嵌套循环？
    - DONE 14、& 和 && 的区别？
    - DONE 15、2 * 8 最有效率的计算方法是什么？
    - DONE 16、数组有没有 length 方法？String 呢？
      collapsed:: true
      - [在 Java 中，数组没有 length 方法，而是有一个公开的 length 属性，可以用来获取数组中元素的个数](https://www.javatpoint.com/how-to-find-array-length-in-java)
    - DONE 17、怎么理解价值传递和引用传递？
      - [在 Java 中，参数传递的方式只有一种，就是值传递。](https://stackoverflow.com/questions/2504523/passing-by-reference-in-java)[1](https://stackoverflow.com/questions/2504523/passing-by-reference-in-java)[2](https://www.baeldung.com/java-pass-by-value-or-pass-by-reference)[3](https://stackoverflow.com/questions/40480/is-java-pass-by-reference-or-pass-by-value)
      - [值传递的意思是，在方法调用时，会在栈内存中创建每个参数的副本，无论是基本类型的值还是引用类型的地址，这些副本会被传递给方法。](https://www.baeldung.com/java-pass-by-value-or-pass-by-reference)[2](https://www.baeldung.com/java-pass-by-value-or-pass-by-reference)
      - [如果参数是基本类型的值，那么方法中对参数的修改不会影响到原始变量。](https://www.javatpoint.com/java-pass-by-value)[4](https://www.javatpoint.com/java-pass-by-value)
      - [如果参数是引用类型的地址，那么方法中对参数的修改会影响到同一个对象，但是如果参数被赋予了新的对象地址，那么原始变量仍然指向旧的对象。](https://stackoverflow.com/questions/2504523/passing-by-reference-in-java)[1](https://stackoverflow.com/questions/2504523/passing-by-reference-in-java)[5](https://stackoverflow.com/questions/2504523/passing-by-reference-in-java)[6](https://www.softwaretestinghelp.com/java/java-pass-by-reference-and-pass-by-value/)
    - DONE 18、Java 到底是值传递还是引用传递？ （**没有引用！**）
    - 19、一个 ".java" 源文件的类型有什么限制？
    - 20、Java 中的注释有哪些写法？
    - 21、static 关键字有什么用？
    - 22、static 变量和普通变量的区别？
    - 23、static 可以修饰局部变量么？
    - 24、final 关键字有哪些用法？
    - 25、final、finally、finalize 有什么区别？
    - 26、void 和 Void 有什么区别？
    - DONE 27、为什么 byte 取值范围为 -128～127？
      collapsed:: true
      - [byte 是 Java 中的一个基本数据类型，它是一个 8 位的有符号整数。](https://howtodoinjava.com/java/basics/primitive-data-types-in-java/)[1](https://howtodoinjava.com/java/basics/primitive-data-types-in-java/)[2](https://howtodoinjava.com/java/basics/primitive-data-types-in-java/)[3](https://www.w3schools.com/java/java_data_types.asp)
        [8 位表示 byte 类型可以用 8 个二进制位（0 或 1）来表示。](https://www.w3schools.com/java/java_data_types.asp)[3](https://www.w3schools.com/java/java_data_types.asp)
        [有符号表示 byte 类型可以表示正数和负数，以及零。](https://stackoverflow.com/questions/3621067/why-is-the-range-of-bytes-128-to-127-in-java)[4](https://stackoverflow.com/questions/3621067/why-is-the-range-of-bytes-128-to-127-in-java)
        [Java 中的 byte 类型使用二进制补码来表示整数。](https://howtodoinjava.com/java/basics/primitive-data-types-in-java/)[2](https://howtodoinjava.com/java/basics/primitive-data-types-in-java/)[5](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)
        [二进制补码是一种编码方式，它可以使正数和负数的运算更加方便。](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[5](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)
        二进制补码的规则是：
      - 如果最高位（第 8 位）是 0，表示这个数是正数或零，其余 7 位就是它的原码（即正常的二进制表示）。
      - 如果最高位（第 8 位）是 1，表示这个数是负数，其余 7 位就是它的反码（即原码取反，每个位都变成相反的值）加上一。
        例如：
      - 数字 +127 的原码和补码都是 `01111111`。
      - 数字 -127 的原码是 `10000001`，反码是 `01111110`，补码是 `01111110 + 1 = 01111111`。
      - 数字 +1 的原码和补码都是 `00000001`。
      - 数字 -1 的原码是 `10000001`，反码是 `01111110`，补码是 `01111110 + 1 = 01111111`。
        [由于 byte 类型只有一个字节（8 比特），所以它能表示的整数范围就受到了限制。](https://howtodoinjava.com/java/basics/primitive-data-types-in-java/)[2](https://howtodoinjava.com/java/basics/primitive-data-types-in-java/)[3](https://www.w3schools.com/java/java_data_types.asp)[5](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)
        如果我们从最小的负数开始计算：
      - 最小的负数的补码是 `10000000`，对应十进制 -128。
      - 加一后得到 `10000001`，对应十进制 -127。
      - 再加一后得到 `10000010`，对应十进制 -126。
      - …
      - 直到加到 `01111111`，对应十进制 +127。
        [再加一后就会发生溢出（overflow），即超出了 byte 类型能表示的范围。](https://howtodoinjava.com/java/basics/primitive-data-types-in-java/)[2](https://howtodoinjava.com/java/basics/primitive-data-types-in-java/)[5](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)
        溢出后得到的结果会回到最小值 `-128`。
        因此，byte 类型能表示的整数范围就是 `-128 ~ +127`。
        您还有其他关于 Java 数据类型或运算符的问题吗？
    - 28、char 类型可以存储中文汉字吗？
    - DONE 29、重载和重写有什么区别？
    - 30、构造器可以被重写和重载吗？
    - 31、main 方法可以被重写和重载吗？
    - 32、私有方法能被重载或者重写吗？
    - 33、Java 中的断言（assert）是什么？
    - 34、Java 异常有哪些分类？
    - 35、Error 和 Exception 有什么区别？
    - 36、Java 中常见的异常有哪些？
    - 37、Java 中常见的运行时异常有哪些？
    - 38、运行时异常与受检查时异常有什么区别？
    - 39、什么时候会发生空指针异常？
    - 40、你知道有哪些避免空指针的方法？
    - DONE 41、throw 和 throws 的区别？
      collapsed:: true
      - [throw用于方法内部，显式地抛出一个异常对象](https://blog.csdn.net/legendaryhaha/article/details/88397984)[2](https://blog.csdn.net/legendaryhaha/article/details/88397984)[3](http://c.biancheng.net/view/6751.html)[，而throws用于方法头，声明该方法可能抛出的异常类型](https://www.geeksforgeeks.org/difference-between-throw-and-throws-in-java/)[1](https://www.geeksforgeeks.org/difference-between-throw-and-throws-in-java/)[2](https://blog.csdn.net/legendaryhaha/article/details/88397984)。
      - [throw只能抛出一个异常对象，而throws可以声明多个异常类型](https://blog.csdn.net/legendaryhaha/article/details/88397984)[2](https://blog.csdn.net/legendaryhaha/article/details/88397984)[4](https://www.javatpoint.com/difference-between-throw-and-throws-in-java)。
      - [throw抛出的异常需要在方法内部或者调用者处进行捕获或者声明](https://blog.csdn.net/legendaryhaha/article/details/88397984)[2](https://blog.csdn.net/legendaryhaha/article/details/88397984)[5](https://blog.csdn.net/meism5/article/details/90414147)[，否则编译报错。如果是运行时异常，则不需要捕获或者声明](https://blog.csdn.net/meism5/article/details/90414147)
    - 42、try-catch-finally 中哪个部分可以省略？
    - DONE 43、try 里面 return，finally还会执行吗？（会）
      collapsed:: true
      - [是的，finally还会执行。根据Java文档](https://juejin.cn/post/6844904016170713096)[1](https://juejin.cn/post/6844904016170713096)[，finally语句块是在try语句块执行完成之后一定会执行的，即使try中有return，continue或者break关键字](https://juejin.cn/post/6844904016170713096)[1](https://juejin.cn/post/6844904016170713096)[2](https://juejin.cn/post/6844904016170713096)[。但是要注意的是，如果try中有return语句，那么它会先把返回值保存到一个本地变量中，然后再执行finally语句块，最后再返回保存的值](https://juejin.cn/post/6844904016170713096)[2](https://juejin.cn/post/6844904016170713096)[3](https://www.cnblogs.com/LoveBell/p/12007181.html)[。如果finally中也有return语句，那么它会覆盖掉try中的返回值](https://www.cnblogs.com/LoveBell/p/12007181.html)[3](https://www.cnblogs.com/LoveBell/p/12007181.html)。
    - 44、int 和 Integer 有什么区别？
    - 45、什么是包装类型？有什么用？
    - 46、什么是自动装厢、拆厢？
    - 47、你怎么理解 Java 中的强制类型转换？
    - 48、你怎么理解 Java 中的自动类型转换？
    - 49、你怎么理解 Java 中的类型提升？
    - 50、switch 是否能用在 long 上？
    - 51、switch 是否能用在 String 上？
    - 52、switch case 支持哪几种数据类型？
    - 53、String 属于基础的数据类型吗？
    - 54、String 类似的常用方法都有哪些？
    - 55、String 的底层实现是怎样的？
    - 56、String 是可变的吗？为什么？
    - 57、String 类可以被继承吗？
    - 58、String 真的是不可变的吗？
    - 59、String 字符串如何进行反转？
    - 60、String 字符串如何实现编码转换？
    - 61、String 有没有长度限制？是多少？
    - ==`62、为什么不能用 + 拼接字符串？`==
      collapsed:: true
      - [Java中的String类是不可变的，每次用 + 拼接字符串时，都会创建一个新的String对象，并把原来的字符串复制到新对象中](https://blog.csdn.net/q5706503/article/details/82954200)[1](https://blog.csdn.net/q5706503/article/details/82954200)[。这样会占用大量的堆空间，并增加垃圾回收的负担](https://blog.csdn.net/q5706503/article/details/82954200)[1](https://blog.csdn.net/q5706503/article/details/82954200)。
      - [如果要频繁地拼接字符串，建议使用StringBuilder类](https://docs.oracle.com/javase/7/docs/api/java/lang/StringBuilder.html)[2](https://docs.oracle.com/javase/7/docs/api/java/lang/StringBuilder.html)[，它是一个可变的字符序列，可以通过append方法来添加字符串，并且不会产生多余的对象](https://docs.oracle.com/javase/7/docs/api/java/lang/StringBuilder.html)[2](https://docs.oracle.com/javase/7/docs/api/java/lang/StringBuilder.html)[。StringBuilder类也提供了toString方法来转换成String类型](https://docs.oracle.com/javase/7/docs/api/java/lang/StringBuilder.html)[2](https://docs.oracle.com/javase/7/docs/api/java/lang/StringBuilder.html)。
    - 63、StringBuffer 和 StringBuilder 的区别？
    - ==`64、StringJoiner 有什么用？`==
      collapsed:: true
      - [StringJoiner是Java 8中引入的一个类，它用于构造一个由分隔符分隔的字符序列，并且可以选择性地添加前缀和后缀](https://docs.oracle.com/javase/8/docs/api/java/util/StringJoiner.html)[1](https://docs.oracle.com/javase/8/docs/api/java/util/StringJoiner.html)[。它可以方便地拼接字符串，而不需要自己处理分隔符的位置和数量](https://www.javatpoint.com/java-stringjoiner)[2](https://www.javatpoint.com/java-stringjoiner)[。它也可以与Collectors类配合使用，将集合或流中的元素拼接成字符串](https://www.baeldung.com/java-string-joiner)[3](https://www.baeldung.com/java-string-joiner)[2](https://www.javatpoint.com/java-stringjoiner)。
      - ```java
        // 创建一个以逗号分隔的字符串，并添加前缀和后缀
        StringJoiner sj = new StringJoiner(",", "[", "]");
        sj.add("a");
        sj.add("b");
        sj.add("c");
        System.out.println(sj.toString()); // 输出 [a,b,c]
        // 合并两个StringJoiner对象
        StringJoiner sj2 = new StringJoiner(";");
        sj2.add("d");
        sj2.add("e");
        sj.merge(sj2);
        System.out.println(sj.toString()); // 输出 [a,b,c;d;e]
        // 使用Collectors类将列表中的元素拼接成字符串
        List<String> list = Arrays.asList("Java", "Python", "C++");
        String result = list.stream().collect(Collectors.joining("|", "{", "}"));
        System.out.println(result); // 输出 {Java|Python|C++}
        ```
    - 65、Java 所有的祖先类是哪个？
    - 66、Object 类有哪些常用的方法？
    - 67、普通类和抽象类有什么区别？
    - 68、静态内部类和普通内部类有什么区别？
    - 69、静态方法可以直接调用非静态方法吗？
    - 70、静态变量和实例变量有什么区别？
    - 71、内部类可以访问其外部类的成员吗？
    - 72、接口和抽象类有什么区别？
    - 73、接口是否可以继承接口？
    - 74、接口里面可以写方法实现吗？
    - 75、抽象类必须要有抽象方法吗？
    - 76、抽象类能使用 final 修饰吗？
    - 77、抽象类是否可以继承具体类？
    - 78、抽象类是否可以实现接口？
    - 79、怎么查看一个 Java 类的字节码？
    - ==`80、Java 中的 UUID 是什么?`==
      collapsed:: true
      - [UUID 是 Universally Unique Identifier 的缩写，意思是通用唯一标识符。](https://www.javatpoint.com/java-uuid)[1](https://www.javatpoint.com/java-uuid)[2](https://www.javatpoint.com/java-uuid)[3](https://kodejava.org/how-do-i-generate-uuid-guid-in-java/)
      - [UUID 是一种 128 位长的值，由十六进制数字和四个连字符（-）组成。](https://www.javatpoint.com/java-uuid)[1](https://www.javatpoint.com/java-uuid)[2](https://www.javatpoint.com/java-uuid)
      - [UUID 的格式是 `xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx`，其中 x 是任意十六进制数字，M 是 UUID 的版本号（从 1 到 5），N 是 UUID 的变体号（通常是 8、9、a 或 b）。](https://www.baeldung.com/java-uuid)[4](https://www.baeldung.com/java-uuid)
      - 例如：`f47ac10b-58cc-4372-a567-0e02b2c3d479` 就是一个有效的 UUID。
      - [UUID 的目的是在分布式系统中生成一个全局唯一的标识符，用于识别信息、资源或实体。](https://www.javatpoint.com/java-uuid)[2](https://www.javatpoint.com/java-uuid)[3](https://kodejava.org/how-do-i-generate-uuid-guid-in-java/)[4](https://www.baeldung.com/java-uuid)
      - [UUID 可以用于创建随机文件名、会话 ID、事务 ID、数据库记录的主键等场景。](https://kodejava.org/how-do-i-generate-uuid-guid-in-java/)[3](https://kodejava.org/how-do-i-generate-uuid-guid-in-java/)
      - [Java 中提供了 java.util.UUID 类来表示和操作 UUID。](https://www.javatpoint.com/java-uuid)[2](https://www.javatpoint.com/java-uuid)[4](https://www.baeldung.com/java-uuid)[5](https://docs.oracle.com/javase/7/docs/api/java/util/UUID.html)
      - [您可以使用 UUID 类的 randomUUID() 方法来生成一个随机的 UUID 对象，也可以使用 fromString(String name) 方法来根据字符串形式的 UUID 来创建一个 UUID 对象。](https://www.baeldung.com/java-uuid)[4](https://www.baeldung.com/java-uuid)[5](https://docs.oracle.com/javase/7/docs/api/java/util/UUID.html)
    - 81、Java 类初始化顺序是怎样的？
    - 82、为什么成员变量命名不建议用 isXXX？
    - ==`83、hashCode 有什么用？`==
      collapsed:: true
      - [hashCode是Java中的一个方法，它用于返回一个对象的数值表示](https://codegym.cc/groups/posts/java-hashcode)[1](https://codegym.cc/groups/posts/java-hashcode)[2](https://stackoverflow.com/questions/3563847/what-is-the-use-of-hashcode-in-java)[。这个数值可以用来在集合中更高效地存储和访问数据](https://codegym.cc/groups/posts/java-hashcode)[1](https://codegym.cc/groups/posts/java-hashcode)[3](https://www.baeldung.com/java-hashcode)[。默认情况下，hashCode方法返回的是对象存储的内存地址的数字](https://codegym.cc/groups/posts/java-hashcode)[1](https://codegym.cc/groups/posts/java-hashcode)。
      - [根据Java的规范，如果两个对象相等（根据equals方法判断），那么它们的hashCode也必须相等](https://www.baeldung.com/java-hashcode)[3](https://www.baeldung.com/java-hashcode)[。反之，如果两个对象不相等，它们的hashCode不一定要不同](https://www.baeldung.com/java-hashcode)[3](https://www.baeldung.com/java-hashcode)。
      - [你可以根据自己的需要重写hashCode方法，但要保证和equals方法保持一致](https://www.baeldung.com/java-hashcode)[3](https://www.baeldung.com/java-hashcode)[。你也可以使用IDE或者Objects.hash方法来生成自定义的hashCode](https://www.baeldung.com/java-hashcode)[3](https://www.baeldung.com/java-hashcode)。
    - 84、hashCode 和 identityHashCode 的区别？
      collapsed:: true
      - [hashCode()是一个非final的实例方法，可以被重写，通常应该在重写equals(Object)的类中也重写hashCode()](https://stackoverflow.com/questions/4930781/how-do-hashcode-and-identityhashcode-work-at-the-back-end)[1](https://stackoverflow.com/questions/4930781/how-do-hashcode-and-identityhashcode-work-at-the-back-end)[2](https://blog.csdn.net/tbdp6411/article/details/46915981)。
      - [identityHashCode()是一个静态方法，不能被重写，它总是返回对象的物理内存地址的哈希值](https://stackoverflow.com/questions/4930781/how-do-hashcode-and-identityhashcode-work-at-the-back-end)[1](https://stackoverflow.com/questions/4930781/how-do-hashcode-and-identityhashcode-work-at-the-back-end)[2](https://blog.csdn.net/tbdp6411/article/details/46915981)[3](https://stackoverflow.com/questions/4930781/how-do-hashcode-and-identityhashcode-work-at-the-back-end)。
      - [对于String对象，如果内容相同，那么hashCode()返回的值也相同，但是identityHashCode()返回的值不同](https://stackoverflow.com/questions/4930781/how-do-hashcode-and-identityhashcode-work-at-the-back-end)[3](https://stackoverflow.com/questions/4930781/how-do-hashcode-and-identityhashcode-work-at-the-back-end)。
    - 85、什么是 hash 冲突？
    - 86、equals 和 hashCode 的区别和联系？
    - 87、两个对象 equals 相等， hashCode 也相等么？
    - 88、两个对象 hashCode 相等，equals 也相等么？
    - ==`89、为什么重写 equals 就要重写 hashCode 方法？`==
      collapsed:: true
      - [如果两个对象相等（即：用equals比较返回true），那么它们的hashCode值一定要相同](https://blog.csdn.net/weixin_44259720/article/details/88414828)[1](https://blog.csdn.net/weixin_44259720/article/details/88414828)[2](https://cloud.tencent.com/developer/article/1910930)[3](https://bing.com/search?q=%E4%B8%BA%E4%BB%80%E4%B9%88%E9%87%8D%E5%86%99+equals+%E5%B0%B1%E8%A6%81%E9%87%8D%E5%86%99+hashCode+%E6%96%B9%E6%B3%95)。
      - [如果不重写hashCode()，那么默认的hashCode()会根据对象的内存地址来生成哈希值，这样可能导致相等的对象有不同的哈希值](https://blog.csdn.net/xl_1803/article/details/80445481)[4](https://blog.csdn.net/xl_1803/article/details/80445481)[1](https://blog.csdn.net/weixin_44259720/article/details/88414828)[2](https://cloud.tencent.com/developer/article/1910930)。
      - [这会影响到一些基于哈希值来存储和查找对象的数据结构，例如HashMap、HashSet等](https://blog.csdn.net/xl_1803/article/details/80445481)[3](https://bing.com/search?q=%E4%B8%BA%E4%BB%80%E4%B9%88%E9%87%8D%E5%86%99+equals+%E5%B0%B1%E8%A6%81%E9%87%8D%E5%86%99+hashCode+%E6%96%B9%E6%B3%95)[4](https://blog.csdn.net/xl_1803/article/details/80445481)[5](https://zhuanlan.zhihu.com/p/295017220)。如果相等的对象有不同的哈希值，那么它们可能被放在不同的位置，导致无法正确地找到或删除它们。
    - ==`90、Java 常用的元注解有哪些？`==
      collapsed:: true
      - [@Documented：表示注解会被包含在 Java 文档中](http://c.biancheng.net/view/7009.html)[1](http://c.biancheng.net/view/7009.html)
      - [@Target：表示注解可以用于什么地方，如类，方法，变量等](http://c.biancheng.net/view/7009.html)[1](http://c.biancheng.net/view/7009.html)[2](https://www.cnblogs.com/kingsonfu/p/10634174.html)。
      - [@Retention：表示注解在什么级别保存，如源码，类文件，运行时](http://c.biancheng.net/view/7009.html)[1](http://c.biancheng.net/view/7009.html)[2](https://www.cnblogs.com/kingsonfu/p/10634174.html)。
      - [@Inherited：表示注解可以被子类继承](http://c.biancheng.net/view/7009.html)[1](http://c.biancheng.net/view/7009.html)[2](https://www.cnblogs.com/kingsonfu/p/10634174.html)。
      - [@Repeatable：表示注解可以重复使用](http://c.biancheng.net/view/7009.html)[1](http://c.biancheng.net/view/7009.html)。
      - [@Native：表示注解和一个常量关联](http://c.biancheng.net/view/7009.html)[1](http://c.biancheng.net/view/7009.html)。
    - ==`91、Java 泛型中的 T、R、K、V、E 分别指什么？`==
      collapsed:: true
      - [R (result) 表示返回值的类型](https://zhuanlan.zhihu.com/p/381859667)[2](https://zhuanlan.zhihu.com/p/381859667)，例如 Function<T,R> 表示一个函数，接受一个 T 类型的参数，返回一个 R 类型的结果。
      - [K (key) 和 V (value) 分别代表 Map 中的键值 Key Value](https://zhuanlan.zhihu.com/p/381859667)[1](https://bing.com/search?q=Java+%E6%B3%9B%E5%9E%8B%E4%B8%AD%E7%9A%84+T%E3%80%81R%E3%80%81K%E3%80%81V%E3%80%81E+%E5%88%86%E5%88%AB%E6%8C%87%E4%BB%80%E4%B9%88)[2](https://zhuanlan.zhihu.com/p/381859667)，例如 Map<K,V> 表示一个泛型映射。
      - [E (element) 代表元素，例如 ArrayList 中的元素](https://zhuanlan.zhihu.com/p/381859667)[1](https://bing.com/search?q=Java+%E6%B3%9B%E5%9E%8B%E4%B8%AD%E7%9A%84+T%E3%80%81R%E3%80%81K%E3%80%81V%E3%80%81E+%E5%88%86%E5%88%AB%E6%8C%87%E4%BB%80%E4%B9%88)[2](https://zhuanlan.zhihu.com/p/381859667)[3](https://stackoverflow.com/questions/6008241/what-is-the-difference-between-e-t-and-for-java-generics)，例如 ArrayList<E> 表示一个泛型数组列表。
        [这些字母只是约定俗成的，并没有特殊的含义，你也可以用其他字母来定义泛型类型](https://zhuanlan.zhihu.com/p/381859667)[2](https://zhuanlan.zhihu.com/p/381859667)[3](https://stackoverflow.com/questions/6008241/what-is-the-difference-between-e-t-and-for-java-generics)。
    - 92、Java 金额计算怎么避免精通丢失？
    - 93、Java 语法糖是什么意思？
    - ==`94、transient 关键字有什么用？`==
      collapsed:: true
      - [transient关键字在Java中用于标记成员变量，在将其持久化为字节流时不进行序列化](https://www.edureka.co/blog/transient-keyword-in-java/)[1](https://www.edureka.co/blog/transient-keyword-in-java/)[2](https://appdividend.com/2022/01/12/transient-keyword-in-java/)[。这意味着当我们将数据写入文件时，可能有一些数据我们不想写入文件](https://appdividend.com/2022/01/12/transient-keyword-in-java/)[2](https://appdividend.com/2022/01/12/transient-keyword-in-java/)[。例如，如果一个程序接受用户的登录信息和密码，但我们不想在文件中存储原始密码，就可以使用transient关键字](https://www.javatpoint.com/transient-keyword)[3](https://www.javatpoint.com/transient-keyword)[。当JVM遇到transient关键字时，它会忽略变量的原始值，并保存该变量数据类型的默认值](https://www.edureka.co/blog/transient-keyword-in-java/)[1](https://www.edureka.co/blog/transient-keyword-in-java/)[4](https://codepumpkin.com/transient-keyword-java/)。
    - 95、如何实现对象克隆？
    - 96、对象克隆浅拷贝和深拷贝的区别？
    - 97、Java 反射机制有什么用？
    - 98、Java 反射机制的优缺点？
    - 99、Java 反射机制 Class 类有哪些常用方法？
    - 100、Java 反射可以访问私有方法吗？
    - 101、Java 反射可以访问私有变量吗？
    - 102、Class.forName 和 ClassLoader 的区别？
    - 103、什么是宏变量和宏替换？
    - ==`104、什么是逃逸分析？`==
      collapsed:: true
      - [一种编译器优化技术，它可以分析对象的作用域和存活时间，从而决定是否可以在栈上分配对象或者消除同步锁](https://zhuanlan.zhihu.com/p/401057707)[1](https://zhuanlan.zhihu.com/p/401057707)[2](https://zhuanlan.zhihu.com/p/59215831)[3](https://cloud.tencent.com/developer/article/1819358)。
      - 逃逸分析的好处是：
      - [减少堆内存的占用，避免GC的开销](https://zhuanlan.zhihu.com/p/401057707)[1](https://zhuanlan.zhihu.com/p/401057707)[2](https://zhuanlan.zhihu.com/p/59215831)[3](https://cloud.tencent.com/developer/article/1819358)。
      - [提高并发性能，减少锁竞争](https://zhuanlan.zhihu.com/p/401057707)[1](https://zhuanlan.zhihu.com/p/401057707)[2](https://zhuanlan.zhihu.com/p/59215831)[3](https://cloud.tencent.com/developer/article/1819358)。
    - 105、什么是伪共享？有什么解决方案？
    - 106、Java 有没有 goto 关键字？
    - 107、Java 中有没有指针的概念？
    - ==`108、Java 中的 classpath 环境变量作用？`==
      collapsed:: true
      - [指定 Java 程序搜索类的路径](https://blog.csdn.net/qq_33642117/article/details/52155505)[1](https://blog.csdn.net/qq_33642117/article/details/52155505)[2](https://www.php.cn/java-article-417736.html)[3](https://zhuanlan.zhihu.com/p/126323702)[，包括接口，类，包等](https://blog.csdn.net/qq_33642117/article/details/52155505)[1](https://blog.csdn.net/qq_33642117/article/details/52155505)。
      - [在编译和运行 Java 程序时使用](https://blog.csdn.net/qq_33642117/article/details/52155505)[1](https://blog.csdn.net/qq_33642117/article/details/52155505)[3](https://zhuanlan.zhihu.com/p/126323702)[，可以用分号分隔多个路径](https://blog.csdn.net/qq_33642117/article/details/52155505)[1](https://blog.csdn.net/qq_33642117/article/details/52155505)[4](https://stackoverflow.com/questions/2396493/what-is-a-classpath-and-how-do-i-set-it)。
      - [可以设置为临时或永久的](https://stackoverflow.com/questions/2396493/what-is-a-classpath-and-how-do-i-set-it)[4](https://stackoverflow.com/questions/2396493/what-is-a-classpath-and-how-do-i-set-it)[，也可以用 -classpath 参数代替](https://stackoverflow.com/questions/2396493/what-is-a-classpath-and-how-do-i-set-it)[4](https://stackoverflow.com/questions/2396493/what-is-a-classpath-and-how-do-i-set-it)。
    - 109、Math.round(1.5) 等于多少？
    - 110、Math.round(-1.5) 等于多少？
    - 111、Java 8 都新增了哪些新特性？
    - 112、Java 8 中的 Lambda 表达式有啥用？
    - 113、Java 8 中的 Optional 类有什么用？
    - 114、Java 8 中的 Stream 有啥用？
    - 115、Java 8 中的@Repeatable 注解有什么用？
    - 116、Java 8 中的方法引用是指什么？
    - 117、Java 8 中的函数式编程怎么用？
    - ==118、怎么创建一个 Stream 流？==
    - 119、Oracle JDK 和 OpenJDK 有啥区别？
  - Java 集合
    - 1、说说常见的集合有哪些？
    - 2、哪些集合类可对元素的随机访问？
    - 3、Comparable 和 Comparator 接口的区别？
    - 4、Collection 和 Collections 的区别？
    - 5、Enumeration 和 Iterator 接口的区别？
    - 6、集合使用泛型有什么优点？
    - 7、List、Set、Map 之间的区别是什么？
    - 8、为什么 Map 接口不继承 Collection 接口？
    - 9、常用的线程安全的 Map 有哪些？
    - 10、HashMap 与 Hashtable 的区别？
    - 11、HashMap 和 TreeMap 怎么选？
    - 12、HashMap 的数据结构是什么？
    - 13、HashMap 在 JDK 8 中有哪些改变？
    - 14、HashMap 的 put 方法逻辑？
    - 15、HashMap 的 get 方法逻辑？
    - 16、HashMap 是线程安全的吗？
      collapsed:: true
      - [HashMap是不是线程安全的，取决于你如何使用它](https://stackoverflow.com/questions/17220036/is-setting-a-hashmap-thread-safe)[1](https://stackoverflow.com/questions/17220036/is-setting-a-hashmap-thread-safe)[2](https://stackoverflow.com/questions/17220036/is-setting-a-hashmap-thread-safe)[。Java的HashMap类本身是不线程安全的，所以当多个线程同时读写时，没有任何保证](https://stackoverflow.com/questions/17220036/is-setting-a-hashmap-thread-safe)[1](https://stackoverflow.com/questions/17220036/is-setting-a-hashmap-thread-safe)[2](https://stackoverflow.com/questions/17220036/is-setting-a-hashmap-thread-safe)[。但是，如果你只是用一个新的HashMap替换一个旧的HashMap，并且不修改旧的HashMap，那么这种模式可能是线程安全的，因为Java中对引用的读写操作是原子的](https://stackoverflow.com/questions/17220036/is-setting-a-hashmap-thread-safe)
      - [但是，如果你需要在多个线程之间共享和修改一个HashMap，那么你需要使用适当的同步代码来保证线程安全](https://stackoverflow.com/questions/17220036/is-setting-a-hashmap-thread-safe)[2](https://stackoverflow.com/questions/17220036/is-setting-a-hashmap-thread-safe)[。或者，你可以使用一些提供了线程安全特性的类，比如Hashtable或ConcurrentHashMap](https://itexpertly.com/why-hashmap-is-not-thread-safe-in-java/)[3](https://itexpertly.com/why-hashmap-is-not-thread-safe-in-java/)[4](https://www.baeldung.com/java-concurrent-map)[5](https://www.geeksforgeeks.org/how-does-concurrenthashmap-achieve-thread-safety-in-java/)。
    - 17、HashMap 是怎么解决 hash 冲突的？
    - 18、HashMap 是怎么扩容的？
      collapsed:: true
      - [根据我的搜索结果，HashMap的扩容是指当HashMap中的元素数量超过了容量和负载因子的乘积时，就会对内部数组进行扩大两倍的操作](https://docs.oracle.com/javase/8/docs/api/java/util/HashMap.html)[1](https://docs.oracle.com/javase/8/docs/api/java/util/HashMap.html)[。在扩容过程中，HashMap会遍历原来的数组，将每个桶中的节点重新计算哈希值并分配到新的数组中](https://blog.csdn.net/weixin_39667787/article/details/86678215)[2](https://blog.csdn.net/weixin_39667787/article/details/86678215)[3](https://stackoverflow.com/questions/46056113/java-hashmap-resizing)[4](https://stackoverflow.com/questions/45404580/hashmap-resize-method-implementation-detail)。这样可以减少哈希冲突，提高查询效率。
    - 19、HashMap 如何实现同步?
      collapsed:: true
      - [HashMap可以使用Collections.synchronizedMap()方法来实现同步](https://www.geeksforgeeks.org/how-to-synchronize-hashmap-in-java/)[1](https://www.geeksforgeeks.org/how-to-synchronize-hashmap-in-java/)[2](https://www.geeksforgeeks.org/how-to-synchronize-hashmap-in-java/)[3](https://howtodoinjava.com/java/collections/hashmap/synchronize-hashmap/)[。这个方法会返回一个由指定的HashMap支持的同步（线程安全）的Map](https://www.geeksforgeeks.org/how-to-synchronize-hashmap-in-java/)[1](https://www.geeksforgeeks.org/how-to-synchronize-hashmap-in-java/)[2](https://www.geeksforgeeks.org/how-to-synchronize-hashmap-in-java/)[3](https://howtodoinjava.com/java/collections/hashmap/synchronize-hashmap/)[。为了保证串行访问，必须通过返回的Map来完成对后台HashMap的所有访问](https://www.geeksforgeeks.org/how-to-synchronize-hashmap-in-java/)[1](https://www.geeksforgeeks.org/how-to-synchronize-hashmap-in-java/)[2](https://www.geeksforgeeks.org/how-to-synchronize-hashmap-in-java/)[3](https://howtodoinjava.com/java/collections/hashmap/synchronize-hashmap/)。例如，下面这段代码就创建了一个同步的HashMap：
      - ```
        // Create a HashMap
        HashMap<Integer,String> map = new HashMap<>();
        - // Populate the HashMap
        map.put(1,"Java");
        map.put(2,"Python");
        map.put(3,"C++");
        - // Synchronize the HashMap
        Map<Integer,String> syncMap = Collections.synchronizedMap(map);
        ```
      - [但是，需要注意的是，Collections.synchronizedMap()方法只能保证单个操作的原子性，而不能保证复合操作（比如迭代）的原子性](https://www.java67.com/2015/02/how-to-synchronize-hashmap-in-java-with.html)[4](https://www.java67.com/2015/02/how-to-synchronize-hashmap-in-java-with.html)[5](https://stackoverflow.com/questions/20602008/hashmap-synchronization)[。因此，在进行复合操作时，还需要对整个Map进行额外的同步](https://www.java67.com/2015/02/how-to-synchronize-hashmap-in-java-with.html)[4](https://www.java67.com/2015/02/how-to-synchronize-hashmap-in-java-with.html)[5](https://stackoverflow.com/questions/20602008/hashmap-synchronization)
    - 20、HashMap 中的负载因子是什么？
      collapsed:: true
      - [负载因子（load factor）是一个表示 HashMap 满的程度的参数，它是哈希表中元素个数和容量的比值](https://blog.csdn.net/TaoTaoFu/article/details/78064932)[1](https://blog.csdn.net/TaoTaoFu/article/details/78064932)[2](https://www.jianshu.com/p/effb601f2c48)[。负载因子越高，表示哈希表越满，空间利用率越高，但是查询效率会降低；负载因子越低，表示哈希表越空，空间浪费多，但是查询效率会提高](https://blog.csdn.net/TaoTaoFu/article/details/78064932)[1](https://blog.csdn.net/TaoTaoFu/article/details/78064932)[3](https://blog.csdn.net/Life_s/article/details/106021860)[。默认的负载因子是 0.75，这是时间和空间成本上的一种折中](https://blog.csdn.net/TaoTaoFu/article/details/78064932)[1](https://blog.csdn.net/TaoTaoFu/article/details/78064932)[4](https://zhuanlan.zhihu.com/p/149687607)。
    - 21、Hashtable 为什么不叫 HashTable？
    - 22、ConcurrentHashMap 的数据结构？
    - ==`23、ArrayList 是线程安全的么？`==
      - [ArrayList 是线程不安全的](https://blog.csdn.net/u013750244/article/details/107758365)[1](https://blog.csdn.net/u013750244/article/details/107758365)[2](https://blog.csdn.net/bobshui/article/details/122440189)[3](https://www.cnblogs.com/zhouyuxin/p/11154771.html)[。如果需要保证线程安全，有以下几种方式](https://blog.csdn.net/bobshui/article/details/122440189)[2](https://blog.csdn.net/bobshui/article/details/122440189)[4](https://www.jianshu.com/p/bf92ce3a153a)：
      - [使用 Vector 替代 ArrayList，Vector 是线程安全的，但是效率较低](https://blog.csdn.net/u013750244/article/details/107758365)[1](https://blog.csdn.net/u013750244/article/details/107758365)。
      - [使用 Collections.synchronizedList() 方法将 ArrayList 包装成一个同步的 List](https://blog.csdn.net/bobshui/article/details/122440189)[2](https://blog.csdn.net/bobshui/article/details/122440189)[4](https://www.jianshu.com/p/bf92ce3a153a)。
      - [使用 CopyOnWriteArrayList 类，它是一个并发容器，适合读多写少的场景](https://blog.csdn.net/bobshui/article/details/122440189)[2](https://blog.csdn.net/bobshui/article/details/122440189)[4](https://www.jianshu.com/p/bf92ce3a153a)。
    - 24、常用的线程安全的 List 集合有哪些？
    - 25、循环删除 List 集合可能会发生什么异常？
    - 26、ArrayList 和 LinkedList 的区别？
    - 27、ArrayList 和 Vector 的区别？
    - 28、什么是 CopyOnWriteArrayList？
      - CopyOnWriteArrayList 是 Java 内置的、线程安全的、基于数组的容器实现，继承自 ArrayList。这个容器可以被多线程访问而不需要同步，因为使用了“写时复制”机制。在读取操作（如遍历、获取指定元素等）非常频繁的场景中有效。 由于在读操作时，CopyOnWriteArrayList 对数组的拷贝是进行同步的，所以在读多写少的场合，其性能优于 Vector 和支持同步的 ArrayList。
    - 29、什么是 fail-safe？
      30、什么是 fail-fast？
      31、fail-fast 与 fail-safe 有什么区别？
      ((63fc3a6b-687c-4703-8381-62d56b41eae0))
    - 32、HashSet 的底层实现原理是什么？
    - 33、怎么确保一个集合不能被修改？
      - [使用 Collections.unmodifiableCollection() 方法将集合包装成一个不可修改的集合，这样任何对集合的修改操作都会抛出 UnsupportedOperationException 异常](https://blog.csdn.net/meism5/article/details/89922143)[1](https://blog.csdn.net/meism5/article/details/89922143)[2](https://blog.csdn.net/weixin_39620118/article/details/110682239)。
      - [使用 Guava 提供的 ImmutableCollection 类或其子类，如 ImmutableList、ImmutableSet、ImmutableMap 等，创建一个不可变的集合，这些集合在创建时就确定了元素，并且不提供任何修改元素的方法](https://blog.csdn.net/meism5/article/details/89922143)[1](https://blog.csdn.net/meism5/article/details/89922143)。
      - [使用 Java 9 提供的 List.of()、Set.of()、Map.of() 等静态方法，创建一个不可变的集合，这些集合也是在创建时就确定了元素，并且不支持任何修改元素的操作](https://blog.csdn.net/weixin_39620118/article/details/110682239)[2](https://blog.csdn.net/weixin_39620118/article/details/110682239)。
  - JVM
    - 1、Java 为什么能一次编写，处处运行？
    - 2、JVM 是什么？
    - 3、HotSpot 是什么？
    - 4、JVM 内存区域分类哪些？
    - 5、堆和栈区别是什么？
    - 6、JVM 哪块内存区别不会发生内存溢出？
    - 7、什么情况下会发生栈内存溢出？
    - 8、对象都是在堆上分配的吗？
    - 9、你怎么理解强、软、弱、虚引用？
    - 10、常用的 JVM 参数有哪些？
    - 11、Java 8 中的内存结构有什么变化？
    - 12、Java 8 中的永久代为什么被移除了？
    - 13、什么是类加载器？
    - 14、类加载器的分类及作用？
    - 15、什么是双亲委派模型？
      - [双亲委派模型是Java类加载机制的一种机制](https://programmer.help/blogs/jvm-series-parent-delegation-model-for-java-class-loading-mechanism.html)[1](https://programmer.help/blogs/jvm-series-parent-delegation-model-for-java-class-loading-mechanism.html)[2](https://www.ibm.com/docs/en/sdk-java-technology/7?topic=cl-parent-delegation-model)[3](https://programmer.help/blogs/jvm-series-parent-delegation-model-for-java-class-loading-mechanism.html)[。双亲委派模型的基本思想是，每个类加载器都有一个父类加载器](https://www.ibm.com/docs/en/sdk-java-technology/7?topic=cl-parent-delegation-model)[2](https://www.ibm.com/docs/en/sdk-java-technology/7?topic=cl-parent-delegation-model)[4](https://stackoverflow.com/questions/2642606/java-classloader-delegation-model)[。当加载一个类时，一个类加载器首先将搜索类的请求委托给它的父类加载器，然后再尝试自己找到这个类](https://www.ibm.com/docs/en/sdk-java-technology/7?topic=cl-parent-delegation-model)[2](https://www.ibm.com/docs/en/sdk-java-technology/7?topic=cl-parent-delegation-model)[4](https://stackoverflow.com/questions/2642606/java-classloader-delegation-model)[。这样的委托链一直延伸到引导类加载器（也称为原始或系统类加载器）](https://www.ibm.com/docs/en/sdk-java-technology/7?topic=cl-parent-delegation-model)[2](https://www.ibm.com/docs/en/sdk-java-technology/7?topic=cl-parent-delegation-model)[。双亲委派模型的优点是，它可以保证Java核心库的类型安全，避免出现同名但不同来源的类被重复加载](https://programmer.help/blogs/jvm-series-parent-delegation-model-for-java-class-loading-mechanism.html)[1](https://programmer.help/blogs/jvm-series-parent-delegation-model-for-java-class-loading-mechanism.html)[5](https://programmer.ink/think/java-virtual-machine-classloader-and-parent-delegation-mechanism.html)。
    - 16、为什么要打破双亲委派模型？
    - 17、可以自定义一个 java.lang.String 吗？
    - 18、什么是 JVM 内存模型？
    - 19、JVM 内存模型和 JVM 内存结构的区别？
    - 20、什么是指令重[排序](/jump/super-jump/word?word=%E6%8E%92%E5%BA%8F)？
    - 21、内存屏障是什么？
    - 22、什么是 Happens-Before 原则？
    - 23、GC 是什么？为什么需要 GC？
    - 24、什么是 MinorGC 和 FullGC？
    - 25、一次完整的 GC 流程是怎样的？
    - 26、JVM 如何判断一个对象可被回收？
    - 27、常用的垃圾收集器有哪些？
    - 28、常用的垃圾回收[算法](/jump/super-jump/word?word=%E7%AE%97%E6%B3%95)有哪些？
    - 29、什么是内存泄漏？
    - 30、为什么会发生内存泄漏？
    - 31、如何防止内存泄漏？
    - 32、什么是直接内存？
    - 33、直接内存有什么用？
    - 34、怎样访问直接内存？
    - 35、常用的 JVM 调优命令有哪些？
    - 36、常用的 JVM 问题定位工具有哪些？
    - 37、常用的主流 JVM 虚拟机都有哪些？
  - 多线程（并发编程）
    - 1、进程和线程的区别？
    - 2、什么是原子性、可见性、有序性？
    - 3、为什么要使用多线程？
    - 4、创建线程有哪几种方式？
    - 5、什么是守护线程？
    - 6、线程的状态有哪几种？怎么流转的？
    - 7、线程的优先级有什么用？
    - 8、我们常说的 JUC 是指什么？
    - 9、i++ 是线程安全的吗？
      - [i++不是线程安全的](https://stackoverflow.com/questions/680097/ive-heard-i-isnt-thread-safe-is-i-thread-safe)[1](https://stackoverflow.com/questions/680097/ive-heard-i-isnt-thread-safe-is-i-thread-safe)[2](https://stackoverflow.com/questions/6324085/what-is-thread-safe-in-java)[1](https://stackoverflow.com/questions/680097/ive-heard-i-isnt-thread-safe-is-i-thread-safe)[。这是因为i++和++i都涉及到三个操作：读取、修改和写入](https://stackoverflow.com/questions/680097/ive-heard-i-isnt-thread-safe-is-i-thread-safe)[1](https://stackoverflow.com/questions/680097/ive-heard-i-isnt-thread-safe-is-i-thread-safe)[。在多线程环境下，这些操作可能会被其他线程打断，导致数据不一致或者竞态条件](https://stackoverflow.com/questions/680097/ive-heard-i-isnt-thread-safe-is-i-thread-safe)[1](https://stackoverflow.com/questions/680097/ive-heard-i-isnt-thread-safe-is-i-thread-safe)[2](https://stackoverflow.com/questions/6324085/what-is-thread-safe-in-java)。例如，假设有两个线程A和B同时执行i++操作，初始时i的值为0，那么可能出现以下情况：
        - 线程A读取了i的值为0
        - 线程B读取了i的值为0
        - 线程A将i的值加1
        - 线程B将i的值加1
        - 线程A将新的值写入到i中，此时i为1
        - 线程B将新的值写入到i中，此时i仍然为1
      - 这样就造成了预期结果（2）和实际结果（1）之间的差异。[3](https://www.baeldung.com/java-thread-safety)[4](https://www.geeksforgeeks.org/thread-safety-and-how-to-achieve-it-in-java/)。例如，在Java中可以使用synchronized关键字或者AtomicInteger类来实现线程安全的自增操作。
    - 10、join 方法有什么用？什么原理？
    - 11、如何让一个线程休眠？
    - 12、启动一个线程是用 start 还是 run 方法？
    - 13、start 和 run 方法有什么区别？
    - 14、sleep 和 wait 方法有什么区别？
    - 15、Thread.yield 方法有什么用？
    - 16、yield 和 sleep 有什么区别？
    - 17、怎么理解 Java 中的线程中断？
    - 18、你怎么理解多线程分组？
    - 19、你怎么理解 wait、notify、notifyAll？
    - 20、同步和异步的区别？
    - 21、什么是死锁？
    - 22、怎么避免死锁？
    - 23、什么是活锁？
    - 24、什么是无锁？
    - 25、什么是线程饥饿？
    - 26、什么是 CAS？
    - 27、阻塞和非阻塞的区别？
    - 28、并发和并行的区别？
    - 29、为什么不推荐使用 stop 停止线程？
    - 30、如何优雅地终止一个线程？
    - 31、Synchronized 同步锁有哪几种用法？
    - 32、什么是重入锁（ReentrantLock）？
    - 33、Synchronized 与 ReentrantLock 的区别？
    - 34、synchronized 锁的是什么?
    - 35、什么是读写锁？
    - 36、公平锁和非公平锁的区别？
    - 37、有哪些锁优化的方式？
    - 38、什么是偏向锁？
    - 39、什么是轻量级锁？
    - 40、什么是自旋锁？
    - 41、什么是锁消除？
    - 42、什么是锁粗化？
    - 43、什么是重量级锁？
    - 44、什么是线程池？
    - 45、使用线程池有什么好处？
    - 46、创建一个线程池有哪些核心参数？
    - 47、线程池的工作流程是怎样的？
    - 48、Java 里面有哪些内置的线程池？
    - 49、为什么阿里不让用 Executors 创建线程池？
    - 50、线程池的拒绝策略有哪几种？
    - 51、如何提交一个线程到线程池？
    - 52、线程池 submit 和 execute 有什么区别？
    - 53、如何查看线程池的运行状态？
    - 54、如何设置线程池的大小？
    - 55、如何关闭线程池？
    - 56、AQS 是什么？
    - 57、AQS 的底层原理是什么？
    - 58、Java 中的 Fork Join 框架有什么用？
    - 59、ThreadLocal 有什么用？
    - 60、ThreadLocal 有什么副作用？
    - 61、volatile 关键字有什么用？
    - 62、volatile 有哪些应用场景？
    - 63、CyclicBarrier 有什么用？
    - 64、CountDownLatch 有什么用？
    - 65、CountDownLatch 与 CyclicBarrier 的区别？
    - 66、Semaphore 有什么用？
    - 67、Exchanger 有什么用？
    - 68、LockSupport 有什么用？
    - 69、Java 中原子操作的类有哪些？
    - 70、什么是 ABA 问题？怎么解决？
    - 71、Java 并发容器，你知道几个？
    - 72、什么是阻塞队列？
    - 73、阻塞队列有哪些常用的应用场景？
    - 74、Java 中的阻塞的队列有哪些？
    - 75、什么是幂等性？
  - IO（网络编程）
    collapsed:: true
    - 1、什么是 IO？
    - 2、常用的 IO 类有哪些？
    - 3、你怎么理解 IO、BIO、NIO、AIO？
    - 4、什么是比特(Bit)、字节(Byte)、字符(Char)？
    - 5、Java 有哪几种类型的流？
    - 6、字节流和字符流的区别？
    - 7、Java 序列化是什么？
    - 8、怎么序列化一个对象？
    - 9、Java 有哪两种序列化方式？
    - 10、怎么控制类中的某些变量不被序列化？
    - 11、静态变量能不能被序列化？
    - 12、OSI 的七层模型都有哪些？
    - 13、tcp 和 udp 协议的区别？
    - 14、tcp 为什么要三次握手，两次不行吗？
  - Web 编程
    collapsed:: true
    - 1、http 和 https 的区别？
    - 2、get 和 post 的区别？
    - 3、forward 和 redirect 的区别？
    - 4、Servlet 是什么？
    - 5、Servlet 生命周期是怎样的？
    - 6、Servlet 有哪些核心的方法？
    - 7、Servlet 是线程安全的么？
    - 8、Servlet 支持异步处理吗？
    - 9、Servlet 是单例还是多例？
    - 10、Servlet 和 JSP 有什么区别和联系？
    - 11、JSP 是什么？
    - 12、JSP 有哪些内置对象？
    - 13、JSP 有哪些基本动作？
    - 14、JSP 有哪几种作用域？
    - 15、JSP 有哪些常用指令？
    - 16、如何实现隐藏的表单域？
    - 17、AJAX 应用和传统 Web 应用有什么不同？
    - 18、怎么优化 Web 前端的性能？
    - 19、什么是 MVC？分别代表什么？
    - 20、拦截器和过滤器的区别？
    - 21、Cookie 和 Session 的区别？
    - 22、什么是跨域？有哪些解决方案？
  - Spring
    collapsed:: true
    - 1、Spring 框架是什么？
    - 2、Spring 常用的注解有哪些？
    - 3、Spring 框架的好处有哪些？
    - 4、Spring 由哪些主要模块组成？
    - 5、Spring IOC 容器是什么？
    - 6、Spring IOC 的好处有哪些？
    - 7、BeanFactory 和 ApplicationContext 的区别？
    - 8、Spring 依赖注入是什么意思？
    - 9、Spring 依赖注入有哪几种方式？
    - 10、Spring bean 支持哪几种作用域？
    - 11、Spring bean 生命周期是怎样的？
    - 12、Spring bean 为什么默认为单例？
    - 13、Spring bean 是线程安全的吗？
    - 14、Spring 这几个注解的区别？
    - 15、Spring @Autowired 注解有什么用？
    - 16、Spring @Required 注解有什么用？
    - 17、Spring @Qualifier 注解有什么用？
    - 18、Spring 怎么注入 Java 集合类型？
    - 19、Spring 装配是指什么？
    - 20、Spring 自动装配有哪些方式？
    - 21、Spring 自动装配有什么局限性？
    - 22、Spring AOP 是什么？
    - 23、Spring AOP 有什么作用？
    - 24、Spring AOP 有哪些实现方式？
    - 25、Spring AOP 和 AspectJ AOP 的区别？
    - 26、Spring 支持哪些事务管理类型？
    - 27、Spring 框架用到了哪些设计模式？
    - 28、Spring MVC 框架有什么用？
    - 29、Spring MVC DispatcherServlet 的工作流程？
    - 30、Spring MVC 常用的注解有哪些？
    - 31、Spring MVC @RequestMapping 有啥用？
  - Spring Boot
    collapsed:: true
    - 1、Spring Boot 是什么？
    - 2、Spring Boot 有哪些优缺点？
    - 3、Spring Boot 框架的核心思想是什么？
    - 4、Spring Boot 有哪些核心模块？
    - 5、Spring Boot 的核心配置文件有哪些？
    - 6、Spring Boot 的配置文件有哪几种格式？
    - 7、Spring Boot 的核心注解是哪个？
    - 8、SpringBootApplication 注解包含哪几个注解？
    - 9、Spring Boot 最核心的注解有哪些？
    - 10、Spring Boot 怎么根据指定条件注册 bean？
    - 11、Spring Boot 有哪些条件注解？
    - 12、Spring Boot 有哪两种方式集成？
    - 13、Spring Boot 需要独立的容器运行吗？
    - 14、Spring Boot 中的默认内嵌容器是？
    - 15、Spring Boot 中间的内嵌容器可以替换成别的么？
    - 16、Spring Boot 自动配置原理是什么？
    - 17、Spring Boot 开启自动配置的注解是？
    - 18、Spring Boot 自动配置的类型在哪注册？
    - 19、Spring Boot 自动配置报告怎么查看？
    - 20、Spring Boot 怎么排除某些自动配置？
    - 21、Spring Boot 怎么开启和关闭自动配置？
    - 22、Spring Boot 的目录结构是怎样的？
    - 23、Spring Boot 中的 Starters 是什么？
    - 24、Spring Boot Starters 有什么命名规范？
    - 25、Spring Boot Starters 官方有哪些分类？
    - 26、Spring Boot 怎么自定义一个 Starter？
    - 27、Spring Boot 有哪几种运行方式？
    - 28、Spring Boot 支持哪些应用打包方式？
    - 29、Spring Boot 应用怎么 Debug 调试？
    - 30、Spring Boot 可以配置随机端口吗？
    - 31、Spring Boot 怎么打一个可执行的 Jar 包？
    - 32、Spring Boot 支持 https 配置吗？
    - 33、Spring Boot 怎么注册 Servlet？
    - 34、Spring Boot Runner 是什么？
    - 35、Spring Boot 支持哪些模板引擎？
    - 36、Spring Boot 支持 Velocity 模板引擎吗？
    - 37、Spring Boot 怎么做单元测试？
    - 38、Spring Boot 支持哪些日志框架？
    - 39、Spring Boot 有哪几种部署方式？
    - 40、Spring Boot 配置加载顺序是怎样的？
    - 41、Spring Boot 如何定义不同环境的配置？
    - 42、Spring Boot 怎么兼容老 Spring 项目？
    - 43、Spring Boot 应用有哪些保护手法？
    - 44、Spring Boot 怎么注册事件监听器？
    - 45、Spring Boot 应用如何监控和健康检查？
    - 46、Spring Boot 怎么解决跨域问题？
    - 47、Spring Boot 2.X 有什么新特性？
    - 48、Spring Boot 怎么定制启动图案？
    - 49、Spring Boot 怎么关闭启动图案？
    - 50、Spring Boot 的默认编码是？
    - 51、Spring Boot 怎么指定编码格式？
    - 52、Spring Boot 应用如何优雅关闭？
  - Spring Cloud
    collapsed:: true
    - 1、Spring Cloud 是什么？
    - 2、Spring Cloud 和 Spring Boot 的关系？
    - 3、Spring Cloud 有哪些重要的组件？
    - 4、Spring Cloud 和 Dubbo 的区别？
    - 5、Spring Cloud 版本号怎么理解？
    - 6、Spring Cloud Eureka 保护机制是什么？
    - 7、Spring Cloud 注册中心有哪些实现方案？
    - 8、Spring Cloud 配置中心有哪些实现方案？
    - 9、Spring Cloud 如何保证微服务调用安全性？
    - 10、Spring Cloud 中的 Ribbon 是什么？
    - 11、Spring Cloud 中的 Feign 是什么？
    - 12、Spring Cloud Feign 和 ribbon 的区别？
    - 13、Spring Cloud Gateway VS Zuul 怎么选？
    - 14、Spring Cloud for Alibaba 是什么？
  - Dubbo
    collapsed:: true
    - 1、Dubbo 是什么框架？
    - 2、为什么要用 Dubbo？
    - 3、Dubbo 里面有哪几种节点角***r /> 4、Dubbo 停止维护了吗？
    - 5、Dubbo 必须依赖的包有哪些？
    - 6、Dubbo 支持哪些注册中心？推荐哪种？
    - 7、Dubbo 内置了哪几种服务容器？
    - 8、Dubbo 需要 Web 容器吗？
    - 9、Dubbo 的服务注册和发现流程？
    - 10、Dubbo 服务暴露的过程？
    - 11、Dubbo 有哪几种配置方式？
    - 12、Dubbo 核心的配置有哪些？
    - 13、Provider 可以配置 Consumer 哪些属性？
    - 14、Dubbo 启动时依赖的服务不可用会怎样？
    - 15、Dubbo 都支持什么协议，推荐用哪种？
    - 16、Dubbo 支持什么通信框架？默认哪种？
    - 17、Dubbo 支持的序列化框架有哪些？
    - 18、Dubbo 有哪些集群容错方案，默认哪种？
    - 19、Dubbo 有哪些负载均衡策略，默认哪种？
    - 20、有多个同名服务时，如果连接指定的服务？
    - 21、Dubbo 支持服务多协议吗？
    - 22、Dubbo 服务上线怎么兼容旧版本？
    - 23、Dubbo 一个服务接口有多种实现怎么区分？
    - 24、Dubbo 可以对结果进行缓存吗？
    - 25、Dubbo 服务之间的调用是阻塞的吗？
    - 26、Dubbo 支持分布式事务吗？
    - 27、Dubbo telnet 命令能做什么？
    - 28、Dubbo 支持服务降级吗？
    - 29、Dubbo 如何优雅停机？
    - 30、Dubbo 服务提供者失效自动下线是什么原理？
    - 31、Dubbo 服务调用链过长如何解决？
    - 32、Duboo 服务读写容错策略怎么做？
    - 33、Dubbo 的管理控制台能做什么？
    - 34、Dubbo 能集成 Spring Boot 吗？
    - 35、Dubbo 使用过程中都遇到了些什么问题？
    - 36、Dubbo 的源码你有读过吗？
    - 37、Dubbo 和 Spring Cloud 哪个好？
    - 38、Dubbo 你们的推荐用法有哪些？
    - 39、你怎么理解 Dubbo SPI？
    - 40、Dubbo 之外，你还了解别的 RPC 框架吗？
    - 41、Dubbox 是什么？和 Dubbo 有啥区别？
  - MySQL（数据库）
    - 1、主键、外键有什么区别？
    - 2、怎么理解三范式和反范式？
    - 3、范式和反范式的优缺点？
    - 4、什么是事务？
    - 5、事务有哪几个特性？
    - 6、什么是脏读、幻读、不可重复读？
    - 7、MySQL 有哪些事务隔离级别？
    - 8、MySQL 默认的事务隔离级别是？
    - 9、什么是索引？
    - 10、索引有什么用？
    - 11、索引为什么能提高查询效率？
    - 12、索引的设计有哪些原则？
    - 13、什么情况下应不建或少建索引？
    - 14、MySQL 索引的种类有哪些？
    - 15、MySQL 索引最左匹配原则怎么理解？
    - 16、MySQL 数据库引擎怎么选择？
    - 17、MySQL 默认数据库引擎是什么？
    - 18、MySQL 引擎 MyISAM 和 InnoDB 的区别？
    - 19、char 和 varchar 的区别？
    - 20、MySQL 的 drop、delete、truncate区别？
    - 21、MySQL 怎么实现分页查询？
    - 22、MySQL 的高可用方案有哪些？
    - 23、如何分析一条 SQL 语句的执行计划和性能？
    - 24、MySQL 查询优化有哪些方法？
    - 25、MySQL 为什么不建议默认 null 值？
    - 26、MySQL 为什么尽量选择最小数据类型？
    - 27、怎么理解数据库中的乐观锁和悲观锁？
    - 28、MySQL 中的 MVCC 是指什么？
    - 29、MySQL InnoDB 的 MVCC 实现机制？
    - 30、MySQL 中的 MVCC 支持哪些事务隔离级别？
    - 31、MySQL 支持哪三种级别的锁？
    - 32、MySQL InnoDB 支持什么锁？
    - 33、MySQL 中的表锁有哪些？
    - 34、MySQL 中的行锁有哪些？
    - 35、MySQL 中的意向锁有什么用？
    - 36、MySQL 中的意向锁的分类？
    - 37、MySQL 中的意向锁是表锁还是行锁？
    - 38、MySQL 中的自增锁有什么用？
    - 39、MySQL 行锁是锁的是什么？
    - 40、MySQL 行锁实现的几种算法？
    - 41、MySQL 什么情况会发生死锁？
    - 42、MySQL 死锁怎么排查？
    - 43、MySQL 如何解决死锁？
    - 44、MySQL 如何避免死锁？
    - 45、MySQL 和 MariaDB 的区别？
    - 46、MySQL 日志 undo 和 redo 的区别？
    - 47、什么是表分区？
    - 48、表分区有什么好处？
    - 49、表分区与分表的区别？
    - 50、MySQL 支持的分区类型有哪些？
    - 51、MySQL 分区表有哪些限制因素？
    - 52、MySQL 为什么要分库分表？
    - 53、MySQL 分库分表怎么做？
    - 54、MySQL 分库分表工具有哪些？
    - 55、MySQL 分库分表会产生哪些问题？
    - 56、MySQL 批量插入，如何不插入重复数据？
  - Redis（缓存）
    collapsed:: true
    - 1、Redis 是什么？
    - 2、Redis 有哪些应用场景？
    - 3、Redis 有什么优势？
    - 4、Redis 为什么这么快？
    - 5、Redis 主要消耗什么物理资源？
    - 6、Redis 到底是单线程还是多线程？
    - 7、Redis 和 Memcache 有什么区别？
    - 8、Redis 支持哪些数据类型？
    - 9、Redis 默认支持多少个数据库？怎么修改？
    - 10、Redis 最大 key 大小？
    - 11、Redis String 值最大存储多少？
    - 12、Redis 事务有什么用？
    - 13、Redis 事务相关的命令有哪几个？
    - 14、Redis 持久化有什么用？
    - 15、Redis 有哪几种持久化方式？
    - 16、Redis 持久化方式如何选择？
    - 17、Redis 内存满了怎么办？
    - 18、Redis 有哪些淘汰策略？
    - 19、Redis 如何提高多核 CPU 利用率？
    - 20、Redis 如何实现大量数据插入？
    - 21、Redis 的回收进程如何工作的？
    - 22、Redis 中的管道有什么用？
    - 23、Redis 有哪些高可用方案？
    - 24、Redis 集群如何选择数据库？
    - 25、Redis 哈希槽怎么理解？
    - 26、Redis 支持的 Java 客户端有哪些？
    - 27、Redisson 是什么框架？
    - 28、Redis 和 Redisson 有什么关系？
    - 29、Jedis 和 Redisson 对比有什么优缺点？
    - 30、Redis 为什么不提供 Windows 版本？
    - 31、Redis 如何设置密码访问？
    - 32、Redis 如何分析慢查询操作？
    - 33、什么是缓存预热和热备？
    - 34、什么是缓存雪崩，如何解决？
    - 35、什么是缓存穿透，如何解决？
    - 36、什么是缓存击穿，如何解决？
    - 37、什么是缓存抖动，如何解决？
    - 38、什么是缓存无底洞现象，如何解决？
    - 39、Redis 和数据库双写一致性问题如何解决？
    - 40、Redis 有哪些危险命令？如何防范？
    - 41、Redis 如何统计独立用户访问量？
  - Zookeeper
    collapsed:: true
    - 1、ZooKeeper 是什么？
      2、ZooKeeper 有哪些特性？
      3、ZooKeeper 有哪些应用场景？
      4、Zookeeper 支持哪些数据节点类型？
      5、Zookeeper 常用的命令有哪些？
      6、Zookeeper 服务器有哪几种角***r /> 7、Zookeeper 服务器有哪几种工作状态？
      8、Zookeeper 支持哪些 Java 客户端？
      9、ZooKeeper 有几种部署模式？
      10、Zookeeper 集群最少要几台机器，为什么?
      11、Zookeeper 集群支持动态添加机器吗？
      12、ZooKeeper 是如何实现分布式事务的？
      13、ZooKeeper 是如何实现分布式锁的？
      14、Zookeeper 中的文件系统怎么理解？
      15、Zookeeper 和 Chubby 的区别？
      16、怎么理解 ZAB 协议？
      17、ZAB 和 Paxos 算法的联系与区别？
    -
  - 分布式
    collapsed:: true
    - 1、什么是 SOA？
    - 2、SOA 和微服务架构有什么区别？
    - 3、什么是 CAP 原则？
    - 4、什么是 BASE 原则？
    - 5、什么是 RMI？
    - 6、什么是 RPC？
    - 7、RMI 和 RPC 有什么区别？
    - 8、分布式系统下会遇到哪些问题？
    - 9、分布式 Session 共享怎么实现？
    - 10、分布式唯一 ID 怎么实现？
    - 11、什么是分布式事务？
    - 12、分布式事务的解决方案有哪些？
    - 13、什么是微服务？
    - 14、微服务架构有什么优势？
    - 15、微服务架构有什么缺点？
    - 16、什么是服务治理？
    - 17、什么是服务降级？
    - 18、服务降级的方案有哪些？
    - 19、什么是服务雪崩？
    - 20、什么是服务熔断？
  - MyBatis
    collapsed:: true
    - 1、MyBatis 是什么框架？
    - 2、MyBatis 和 ORM 的区别？
    - 3、MyBatis 为什么是半自动 ORM 映射？
    - 4、MyBatis 框架的应用场景？
    - 5、MyBatis 有哪些优点？
    - 6、MyBatis 有哪些缺点？
    - 7、MyBatis 和 Hibernate 的区别？
    - 8、MyBatis 和 JPA 的区别？
    - 9、MyBatis 有哪几种 SQL 编写形式？
    - 10、MyBatis 支持哪些传参数的方法？
    - 11、MyBatis 的 $ 和 # 传参的区别？
    - 12、MyBatis 可以映射到枚举类吗？
    - 13、MyBatis 怎么封装动态 SQL？
    - 14、Mybatis trim 标签有什么用？
    - 15、MyBatis 怎么实现分页？
    - 16、MyBatis 流式查询有什么用？
    - 17、MyBatis 模糊查询 like 语句该怎么写？
    - 18、MyBatis 配置文件中的 SQL id 是否能重复？
    - 19、MyBatis 如何防止 SQL 注入？
    - 20、MyBatis 如何获取自动生成的主键id？
    - 21、MyBatis 使用了哪些设计模式？
    - 22、MyBatis 中的缓存机制有啥用？
    - 23、MyBatis 一级缓存和二级缓存的区别？
    - 24、MyBatis-Plus 是什么框架？
  - 消息队列
    collapsed:: true
    - 1、消息队列有什么用？
    - 2、消息队列有哪些应用场景？
    - 3、消息队列有什么优缺点？
    - 4、消息队列怎么选型？
    - 5、有了多线程，为什么还要消息队列？
    - 6、消息队列和多线程应该怎么选择呢？
    - 7、使用消息队列会遇到哪些问题？
    - 8、消息队列如何处理消息重复消费问题？
    - 9、消息队列为什么会产生消息丢失？
    - 10、消息队列如何解决消息丢失问题？
    - 11、消息队列如何保证消息顺序消费？
    - 12、消息延迟推送有哪些应用场景？
    - 13、什么是拉模式和推模式？
    - 14、什么是消息持久化？
    - 15、消息持久化有什么缺点？
    - 16、什么是 JMS？
    - 17、什么是 RabbitMQ？
    - 18、RabbitMQ 有哪些优点？
    - 19、RabbitMQ 有哪些重要的组件？
    - 20、RabbitMQ 有哪些重要的角***r /> 21、RabbitMQ 交换器类型有哪些？
    - 22、RabbitMQ 消息基于什么传输？
    - 23、RabbitMQ 怎么避免消息丢失？
    - 24、RabbitMQ 怎么保证消息的稳定性？
    - 25、RabbitMQ 支持事务消息吗？
    - 26、RabbitMQ 事务消息在什么情况下无效？
    - 27、RabbitMQ 接收到消息之后必须消费吗？
    - 28、RabbitMQ 如何确保每个消息能被消费？
    - 29、RabbitMQ 消息持久化的条件？
    - 30、RabbitMQ 中的死信队列是什么？
    - 31、RabbitMQ 队列中的消息是否有数量限制?
    - 32、RabbitMQ 怎么实现消息延迟推送？
  - DONE Linux
    collapsed:: true
    - 1、Linux 是什么？
    - 2、Linux 和 Unix 的区别？
    - 3、Linux 系统有哪些优势？
    - 4、Linux 怎么查看内核版本？
    - 5、RedHat、CentOS、Ubuntu 有什么区别？
    - 6、Linux 和 Windows 正反斜杠的区别？
    - 7、Linux 环境变量配置有哪几种方式？
    - 8、Linux 安装软件有哪几种方式？
    - 9、Linux 普通用户怎么以管理员身份执行指令？
    - 10、Linux 的 root 和 home 目录有什么不同？
    - 11、Linux 系统 root 和普通用户的区别？
    - ==`12、Linux 怎么区分 root 和普通用户？`==
      collapsed:: true
      - ```
        在Linux中，root用户是拥有系统管理员权限的超级用户，而普通用户则只拥有系统中分配给他们的权限。以下是区分root和普通用户的一些常见方法：
        1. 用户名：root用户的用户名通常是“root”，而普通用户则是由系统管理员分配的其他名称。
        2. UID：每个用户在系统中都有一个唯一的用户标识符（UID），root用户的UID通常为0，而普通用户的UID则是大于0的数字。
        3. 权限：root用户拥有对系统中所有文件和目录的完全控制权限，而普通用户只能访问他们拥有权限的文件和目录。
        4. shell提示符：默认情况下，root用户的shell提示符通常是以“#”结尾的，而普通用户的提示符通常是以“$”结尾的。
        5. sudo权限：sudo是Linux中一种授权机制，允许普通用户在必要时以root用户身份运行特定的命令。通常，只有root用户和具有sudo权限的普通用户才能使用sudo命令。
        总之，通过用户名、UID、权限、shell提示符和sudo权限等方式，可以在Linux系统中区分root用户和普通用户。
        ```
    - 13、Linux 怎么切换用户？
    - 14、Linux 中的 bash 是什么？
    - 15、Linux 中的 Shell 是什么？
    - 16、Linux 怎么显示目录下的文件？
    - 17、Linux 中 ll 和 ls 命令的区别？
    - 18、Linux 怎么创建文件？
    - 19、Linux 怎么创建目录？
    - 20、Linux 怎么切换目录？
    - 21、Linux 怎么切换到上 N 级目录？
    - 22、Linux 怎么切换到之前所在的目录？
    - 23、Linux 怎么切换到当前用户主目录？
    - 24、Linux 怎么查看当前目录所在路径？
    - 25、Linux 下的权限有哪几种？
    - 26、Linux 文件调用权限分为哪 3 级？
    - 27、Linux 怎么修改文件权限？
    - 28、Linux 怎么修改文件所有者和所属组？
    - ==`29、Linux 怎么查看磁盘的使用情况？`== 
      collapsed:: true
      - df命令：显示磁盘空间使用情况的概述。可以使用以下命令来显示文件系统使用情况及剩余空间：
        ```
        df -h
        ```
      - du命令：查看目录和文件的磁盘空间使用情况。可以使用以下命令来查看当前目录下文件和目录的磁盘空间使用情况：
        ```
        du -sh *
        ```
      - ls命令：查看文件和目录的大小。可以使用以下命令来查看当前目录下的所有文件和目录的大小：
        ```
        ls -lh
        ```
      - ncdu命令：以交互方式查看磁盘使用情况。ncdu是一个交互式命令行工具，可以帮助您以图形化的方式查看磁盘使用情况。如果您没有安装该工具，可以使用以下命令进行安装：
        ```
        sudo apt-get install ncdu
        ```
        以上命令都是常用的用于查看磁盘使用情况的命令，在Linux系统中可以根据需要使用相应的命令。
    - ==`30、Linux 怎么查看内存的使用情况？`== 
      collapsed:: true
      - free命令：可以显示系统的内存使用情况，包括物理内存、交换空间等信息。可以使用以下命令来查看内存使用情况：
        ```
        free -h
        ```
        其中，选项“-h”表示以人类可读的方式显示结果，更加易读。输出结果中，第一行显示物理内存的使用情况，第二行显示交换空间的使用情况。
      - top命令：可以实时动态地查看系统进程的资源使用情况，包括CPU、内存等。可以使用以下命令来启动top命令：
        ```
        top
        ```
        在top命令的输出中，按下“Shift+M”键可以按内存使用率排序，可以看到占用内存最多的进程。
      - ps命令：可以列出当前系统中的进程列表，包括进程的PID、命令名称、CPU使用率、内存使用率等信息。可以使用以下命令来列出占用内存最多的前N个进程：
        ```
        ps aux --sort=-%MEM | head -n N
        ```
        其中，选项“--sort=-%MEM”表示按内存使用率逆序排序，选项“head -n N”表示只显示前N个结果。A（all）；U（uid, name）；X（processes without controlling ttys）
    - ==`31、Linux 怎么查看资源消耗最多的进程？`== 
      collapsed:: true
      - top命令：可以实时动态地查看进程的资源使用情况。可以使用以下命令来启动top命令：
        ```
        top
        ```
        在top命令的输出中，按下“Shift+P”键可以按CPU使用率排序，按下“Shift+M”键可以按内存使用率排序，可以看到资源消耗最多的进程。
      - ps命令：可以列出当前系统中的进程列表，包括进程的PID、命令名称、CPU使用率、内存使用率等信息。可以使用以下命令来列出资源消耗最多的前N个进程：
        ```
        ps aux --sort=-%CPU | head -n N
        ```
        其中，选项“--sort=-%CPU”表示按CPU使用率逆序排序，选项“head -n N”表示只显示前N个结果。可以将“%CPU”换成“%MEM”来按内存使用率排序。
      - htop命令：是一个交互式的进程查看工具，类似于top命令，但提供更多的功能和操作。可以使用以下命令来启动htop命令：
        ```
        htop
        ```
        在htop命令的输出中，按下“F6”键可以按CPU使用率或内存使用率排序，可以看到资源消耗最多的进程。
        以上三种方法都可以用来查看资源消耗最多的进程，可以根据需要选择合适的方法。
    - ==`32、Linux 怎么看端口被哪个进程占用？`==
      collapsed:: true
      - ~~Windows~~
        collapsed:: true
        - ```shell
          netstat -tnq | grep 端口号
            # -tlnp 表示显示所有TCP端口的监听状态
            # 最后输出结果中，第一个数字是进程ID（PID），最后一个字段是进程的名称;	
          ```
      - [GitHub - lsof-org/lsof: LiSt Open Files](https://github.com/lsof-org/lsof)
      - ```shell
        lsof -i:端口号
        # -i 表示显示所有打开的套接字（socket）
        ```
    - ==`33、Linux 怎么查找某个进程？`==
      collapsed:: true
      - 在Linux系统中，可以使用以下命令来查找某个进程：
      - ps命令：可以列出当前系统中的进程列表，包括进程的PID、命令名称、CPU使用率、内存使用率等信息。可以使用以下命令来查找某个进程：
        ```
        ps aux | grep 进程名
        ```
        其中，“进程名”是要查找的进程的名称，可以使用部分名称进行模糊匹配。
      - pgrep命令：可以通过进程名称来查找进程的PID，可以使用以下命令来查找某个进程：
        ```
        pgrep 进程名
        ```
        其中，“进程名”是要查找的进程的名称。
      - pstree命令：可以以树状结构的形式显示当前系统中的进程和它们之间的关系，可以使用以下命令来查找某个进程：
        ```
        pstree | grep 进程名
        ```
        其中，“进程名”是要查找的进程的名称。
        以上三种方法都可以用来查找某个进程，可以根据需要选择合适的方法。如果需要终止某个进程，可以使用kill命令，并指定该进程的PID。例如：
        ```
        kill -9 PID
        ```
        其中，“PID”是要终止的进程的PID。注意，使用kill命令需要谨慎，避免误操作。
    - 34、Linux 怎么结束某个进程？
    - 35、Linux 怎么清屏？
    - ==`36、Linux 控制台怎么设置超时自动注销？`==
      collapsed:: true
      - 在Linux系统中，可以通过修改控制台的配置文件来设置超时自动注销，具体步骤如下：
      - 打开控制台的配置文件/etc/profile，可以使用以下命令：
        ```
        sudo nano /etc/profile
        ```
      - 在文件的末尾添加以下内容：
        ```
        TMOUT=分钟数
        readonly TMOUT
        export TMOUT
        ```
        其中，“分钟数”表示空闲多少分钟后自动注销，可以根据需要自行设置，建议设置为5-15分钟。
    - 37、Linux vim 和 vi 命令的区别？
    - 38、Linux vim 命令怎么使用？
    - 39、Linux 软链接和硬链接区别？
    - 40、Linux 怎么创建软、硬链接？
    - 41、Linux 中的零拷贝是指什么？
    - 42、Linux 下 select,poll,epoll 的区别？
- [Java校招面试题目合集_Java工程师/Java开发_牛客网](https://www.nowcoder.com/ta/review-java)
  collapsed:: true
  - DONE [什么是Java虚拟机？为什么Java被称作是“平台无关的编程语言”？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21069&query=&asc=true&order=&page=1)
  - DONE [JDK和JRE的区别是什么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21070&query=&asc=true&order=&page=2)
  - [”static”关键字是什么意思？Java中是否可以覆盖(override)一个private或者是static的方法？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21071&query=&asc=true&order=&page=3)
    collapsed:: true
    - ((63e72783-9c4d-4975-8316-8eefaa9e9f64))
    - 两个都不可以
      collapsed:: true
      - Private 只可以被本类成员和方法访问，所以无法被 Override
      - Override 是基于运行时动态绑定的，而 Static 早在编译期就已经静态绑定，与任何类的实例再不相关，因此无法 Override
  - [是否可以在static环境中访问非static变量？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21072&query=&asc=true&order=&page=4)
    collapsed:: true
    - 没有实例就不能访问 非static 变量，除非是在 static 环境中初始化一个实例；
  - DONE [Java支持的数据类型有哪些？什么是自动拆装箱？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21073&query=&asc=true&order=&page=5)
  - DONE [Java中的方法覆盖(Overriding)和方法重载(Overload)是什么意思？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21074&query=&asc=true&order=&page=6)
  - [Java中，什么是构造方法？什么是构造方法重载？什么是复制构造方法？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21075&query=&asc=true&order=&page=7)
    collapsed:: true
    - Java不支持像C++中那样的复制构造方法，这个不同点是因为如果你不自己写构造方法的情况下，Java不会创建默认的复制构造方法。（对任何对象都使用引用机制）
  - DONE [Java支持多继承么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21076&query=&asc=true&order=&page=8)
  - [接口和抽象类的区别是什么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21077&query=&asc=true&order=&page=9)
    collapsed:: true
    - ((63e7791a-04a5-425e-a98b-9c35bd1f7400))
  - [什么是值传递和引用传递？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21078&query=&asc=true&order=&page=10)
    collapsed:: true
    - Java 只有值传递参数；
      collapsed:: true
      - 当一个对象实例作为一个参数被传递到方法中时，参数的值就是该对象的引用一个副本
    - Related: [Java中只有按值传递，没有按引用传递！ - - ITeye博客](https://www.iteye.com/blog/guhanjie-1683637) & [Java 到底是值传递还是引用传递？ - 知乎](https://www.zhihu.com/question/31203609)
  - [进程和线程的区别是什么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21079&query=&asc=true&order=&page=11) #process
    collapsed:: true
    - 进程是执行着的应用程序，而线程是进程内部的一个执行序列
    - 线程又叫做轻量级进程
    - 一个进程可以有多个线程
    - **线程与进程的区别归纳：**
      collapsed:: true
      - **a.地址空间和其它资源**
        collapsed:: true
        - 进程间相互独立，同一进程的各线程间共享。某进程内的线程在其它进程不可见。
      - **b.通信**
        collapsed:: true
        - 进程间通信IPC，线程间可以直接读写进程数据段（如全局变量）来进行通信——需要进程同步和互斥手段的辅助，以保证数据的一致性。
      - **c.调度和切换**
        collapsed:: true
        - 线程上下文切换比进程上下文切换要快得多
      - d.在多线程OS中，进程不是一个可执行的实体
    - ((63e72768-1f77-4542-9d9b-aa3e724b7bce))
  - [创建线程有几种不同的方式？你喜欢哪一种？为什么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21080&query=&asc=true&order=&page=12)
    collapsed:: true
    - 继承Thread类
    - 实现Runnable接口
      collapsed:: true
      - 实现Runnable接口这种方式更受欢迎，因为这不需要继承Thread类
    - 应用程序可以使用Executor框架来创建线程池
      collapsed:: true
      - 线程池也是非常高效的，很容易实现和使用
    - 还有一种方式是实现Callable接口
  - [概括的解释下线程的几种可用状态。](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21081&query=&asc=true&order=&page=13)
    collapsed:: true
    - 1.新建 (new)
      collapsed:: true
      - 新创建了一个线程对象。
    - 2.可运行 (runnable)
      collapsed:: true
      - 线程对象创建后，其他线程(比如main线程）调用了该对象的start()方法。该状态的线程位于可运行线程池中，等待被线程调度选中，获取cpu的使用权。
    - 3.运行(running)
      collapsed:: true
      - 可运行状态(runnable)的线程获得了cpu时间片(timeslice)，执行程序代码
    - 4.阻塞(blocked)
      collapsed:: true
      - 阻塞状态是指线程因为某种原因放弃了cpu使用权，也即让出了cputimeslice，暂时停止运行
        直到线程进入可运行(runnable)状态，才有机会再次获得cputimeslice转到运行(running)状态
        阻塞的情况分三种：
      - (一).等待阻塞
        collapsed:: true
        - 运行(running)的线程执行o.wait()方法，JVM会把该线程放入等待队列(waittingqueue)中。
      - (二).同步阻塞
        collapsed:: true
        - 运行(running)的线程在获取对象的同步锁时，若该同步锁被别的线程占用，则JVM会把该线程放入锁池(lockpool)中。
      - (三).其他阻塞
        collapsed:: true
        - 运行(running)的线程执行Thread.sleep(longms)或t.join()方法，或者发出了I/O请求时，JVM会把该线程置为阻塞状态
        - 当sleep()状态超时、join()等待线程终止或者超时、或者I/O处理完毕时，线程重新转入可运行(runnable)状态。
        - 即让出了cputimeslice，
    - 5.死亡 (dead)
      collapsed:: true
      - 线程run()、main()方法执行结束，或者因异常退出了run()方法，则该线程结束生命周期。死亡的线程不可再次复生
    - ![](http://uploadfiles.nowcoder.com/images/20151217/149974_1450349079825_4697A22AC611680A692472687DEC1CFD)
    - ？**time_waiting** / **terminated** / **waiting**
  - [同步方法和同步代码块的区别是什么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21082&query=&asc=true&order=&page=14)
    collapsed:: true
    - 同步方法默认用this或者当前类class对象作为锁；
    - 同步代码块可以选择以什么来加锁，比同步方法要更细颗粒度，我们可以选择只同步会发生同步问题的部分代码而不是整个方法；
  - [在监视器(Monitor)内部，是如何做线程同步的？程序应该做哪种级别的同步？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21083&query=&asc=true&order=&page=15)
    collapsed:: true
    - 监视器和锁在Java虚拟机中是一块使用的。监视器监视一块同步代码块，确保一次只有一个线程执行同步代码块。每一个监视器都和一个对象引用相关联。线程在获取锁之前不允许执行同步代码。
  - DONE [什么是死锁(deadlock)？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21084&query=&asc=true&order=&page=16)
    collapsed:: true
    - 多个进程因竞争资源而造成的一种僵局（互相等待），若无外力作用，这些进程都将无法向前推进
    - 4个必要条件：
      collapsed:: true
      - 互斥条件
        collapsed:: true
        - 进程要求对所分配的资源（如打印机）进行排他性控制，即在一段时间内某 资源仅为一个进程所占有。此时若有其他进程请求该资源，则请求进程只能等待。
      - 不剥夺条件
        collapsed:: true
        - 进程所获得的资源在未使用完毕之前，不能被其他进程强行夺走，即只能 由获得该资源的进程自己来释放（只能是主动释放)。
      - 请求和保持条件
        collapsed:: true
        - 进程已经保持了至少一个资源，但又提出了新的资源请求，而该资源 已被其他进程占有，此时请求进程被阻塞，但对自己已获得的资源保持不放。
      - 循环等待条件
        collapsed:: true
        - 存在一种进程资源的循环等待链，链中每一个进程已获得的资源同时被 链中下一个进程所请求
  - [如何确保N个线程可以访问N个资源同时又不导致死锁？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21085&query=&asc=true&order=&page=17)
    collapsed:: true
    - 指定获得锁的顺序 （破环循环等待条件）
      collapsed:: true
      - 保证在获得第一个锁之前，不会请求第二个锁，保证每一个线程都以同样的顺序加锁和释放锁。
  - DONE [Java集合类框架的基本接口有哪些？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21086&query=&asc=true&order=&page=18)
    collapsed:: true
    - [[java-2/collections]]
    - 两大接口，容器和图，集合的父类是可迭代接口，下分列表，队列，集合；图下分哈希表实现，哈希图实现，有序图接口；
  - [为什么集合类没有实现Cloneable和Serializable接口？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21087&query=&asc=true&order=&page=19)
    collapsed:: true
    - 克隆和序列化的语义是根据具体实现走的，应该由具体实现决定是否由这些属性；
  - [什么是迭代器(Iterator)？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21088&query=&asc=true&order=&page=20)
    collapsed:: true
    - 迭代器接口提供对集合元素的迭代方法；
    - 每一个集合都有一个返回了迭代器的迭代方法；
    - 迭代过程甚至可以用非直接方法删除元素（迭代器提供的remove方法）；
  - [Iterator和ListIterator的区别是什么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21089&query=&asc=true&order=&page=21)
  - [快速失败(fail-fast)和安全失败(fail-safe)的区别是什么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21090&query=&asc=true&order=&page=22)
    id:: 63fc3a6b-687c-4703-8381-62d56b41eae0
    - 快速失败（fail—fast）
      description:: 在用迭代器遍历一个集合对象时，如果遍历过程中对集合对象的结构进行了修改（增加、删除），则会抛出Concurrent Modification Exception。
      collapsed:: true
      - 原理：迭代器在遍历时直接访问集合中的内容，并且在遍历过程中使用一个 modCount 变量。集合在被遍历期间如果结构发生变化，就会改变modCount的值。每当迭代器使用hashNext()/next()遍历下一个元素之前，都会检测modCount变量是否为expectedmodCount值，是的话就返回遍历；否则抛出异常，终止遍历。
      - 注意：这里异常的抛出条件是检测到 modCount！=expectedmodCount 这个条件。如果集合发生变化时修改modCount值刚好又设置为了expectedmodCount值，则异常不会抛出。因此，不能依赖于这个异常是否抛出而进行并发操作的编程，这个异常只建议用于检测并发修改的bug。
      - 场景：java.util包下的集合类都是快速失败的，不能在多线程下发生并发修改（迭代过程中被修改）
    - 安全失败（fail—safe）
      description:: 采用安全失败机制的集合容器，在遍历时不是直接在集合内容上访问的，而是先复制原有集合内容，在拷贝的集合上进行遍历。
      - 原理：由于迭代时是对原集合的拷贝进行遍历，所以在遍历过程中对原集合所作的修改并不能被迭代器检测到，所以不会触发Concurrent Modification Exception。
      - 缺点：基于拷贝内容的优点是避免了Concurrent Modification Exception，但同样地，迭代器并不能访问到修改后的内容，即：迭代器遍历的是开始遍历那一刻拿到的集合拷贝，在遍历期间原集合发生的修改迭代器是不知道的。
      - 场景：java.util.concurrent包下的容器都是安全失败，可以在多线程下并发使用，并发修改。
  - [Java中的HashMap的工作原理是什么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21091&query=&asc=true&order=&page=23) #[[java-2/collections]]
    collapsed:: true
    - hashmap是一个key-value键值对的数据结构，从结构上来讲在jdk1.8之前是用数组加链表的方式实现，jdk1.8 加了红黑树，hashmap数组的默认初始长度是16，hashmap数组只允许一个key为null，允许多个value为null
    - hashmap的内部实现，hashmap是使用数组+链表+红黑树的形式实现的，其中数组是一个一个Node[]数组，我们叫他hash桶数组，它上面存放的是key-value键值对的节点。HashMap是用hash表来存储的，在hashmap里为解决hash冲突，使用链地址法，简单来说就是数组加链表的形式来解决，当数据被hash后，得到数组下标，把数据放在对应下表的链表中。
    - 然后再说一下hashmap的方法实现
      - put方法
        - 计算出要put元素在hash桶数组中的索引位置（3）
          - 取put元素key的hashcode值
          - 高位运算
            collapsed:: true
            - 高位运算就是用第一步得到的值h，用h的高16位和低16位进行异或操作；
            - ```java
              /**
              * Computes key.hashCode() and spreads (XORs) higher bits of hash
              * to lower.  Because the table uses power-of-two masking, sets of
              * hashes that vary only in bits above the current mask will
              * always collide. (Among known examples are sets of Float keys
              * holding consecutive whole numbers in small tables.)  So we
              * apply a transform that spreads the impact of higher bits
              * downward. There is a tradeoff between speed, utility, and
              * quality of bit-spreading. Because many common sets of hashes
              * are already reasonably distributed (so don't benefit from
              * spreading), and because we use trees to handle large sets of
              * collisions in bins, we just XOR some shifted bits in the
              * cheapest possible way to reduce systematic lossage, as well as
              * to incorporate impact of the highest bits that would otherwise
              * never be used in index calculations because of table bounds.
              */
              static final int hash(Object key) {
                int h;
                return (key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16);
              }
              ```
            - 用 h 的高 16 位和低 16 位进行异或操作，就是将 h 的二进制表示分成两部分，每部分有 16 位，然后对应的位进行异或运算。例如，假设 h = 10000000000000001000000000000000（32位），那么 h 的高低位异或操作就是：
            - ![chrome_296.png](../assets/chrome_296_1676626462508_0.png)
            - 可以看到，这样的操作可以让 h 的哈希值更加分散，减少冲突的可能性。
          - 取模运算
            - 为了使hash桶数组元素分布更均匀，采用取模运算，取模运算就是用第二步得到的值和hash桶数组长度-1的值取与；
            - ```java
              public V computeIfAbsent(K key,
              	Function<? super K, ? extends V> mappingFunction) {
                  // ...
              	if ((first = tab[i = (n - 1) & hash]) != null) {
              ```
            - 这样得到的结果和传统取模运算结果一致，而且效率比取模运算高
        - jdk1.8中put方法的具体步骤
          - 先判断hashmap是否为空，为空的话扩容，不为空计算出key的hash值i
          - 看table[i]是否为空，为空就直接插入，不为空判断当前位置的key和table[i]是否相同，相同就覆盖，不相同就查看table[i]是否是红黑树节点
          - 如果是的话就用红黑树直接插入键值对，如果不是开始遍历链表插入，如果遇到重复值就覆盖，否则直接插入
          - 如果链表长度大于8，转为红黑树结构；
          - 执行完成后看size是否大于阈值threshold，大于就扩容，否则直接结束
      - get方法：计算出要获取元素的hash值，去对应位置取即可。
    - 扩容机制（2）
      - 把数组长度变为原来的两倍；
      - 把旧数组的元素重新计算hash插入到新数组中，在jdk1.8时，不用重新计算hash，只用看看原来的hash值新增的一位是零还是1，如果是1这个元素在新数组中的位置，是原数组的位置加原数组长度，如果是零就插入到原数组中
        - 扩容过程第二部一个非常重要的方法是transfer方法，采用头插法，把旧数组的元素插入到新数组中。
    - hashmap大小为什么是2的幂次方？
      - 在计算插入元素在hash桶数组的索引时第三步，为了使元素分布的更加均匀，用取模操作，但是传统取模操作效率低，然后优化成 h&(length-1)，设置成2幂次方，是因为2的幂次方-1后的值每一位上都是1，然后与第二步计算出的h值与的时候，最终的结果只和key的hashcode值本身有关，这样不会造成空间浪费并且分布均匀，如果不是2的幂次方
      - 如果length不为2的幂，比如15。那么length-1的2进制就会变成1110。在h为随机数的情况下，和1110做&操作。尾数永远为0。那么0001、1001、1101等尾数为1的位置就永远不可能被entry占用。这样会造成浪费，不随机等问题。
    - Java中的HashMap是以键值对(key-value)的形式存储元素的。HashMap需要一个hash函数，它使用hashCode()和equals()方法来向集合/从集合添加和检索元素。当调用put()方法的时候，HashMap会计算key的hash值，然后把键值对存储在集合中合适的索引上。如果key已经存在了，value会被更新成新值。HashMap的一些重要的特性是它的容量(capacity)，负载因子(load factor)和扩容极限(threshold resizing)。
    -
    - https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21090&query=&asc=true&order=&page=22
  - [hashCode()和equals()方法的重要性体现在什么地方？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21092&query=&asc=true&order=&page=24)
    collapsed:: true
    - hashcode和equals组合在一起确定元素的唯一性。
    - 查找元素时，如果单单使用equals来确定一个元素，需要对集合内的元素逐个调用equals方法，效率太低。因此加入了hashcode方法，将元素映射到随机的内存地址上，通过hashcode快速定位到元素（大致）所在的内存地址，再通过使用equals方法确定元素的精确位置。
    - ```java
      public final int hashCode() {
        return Objects.hashCode(key) ^ Objects.hashCode(value);
      }
      ```
    - 比较两个元素时，先比较hashcode，如果hashcode不同，则元素一定不相等
    - 如果相同，再用equals判断。
    - HashMap采用这两个方法实现散列存储，提高键的索引性能。
    - HashSet是基于HashMap实现的。
      - ```java
        public class HashSet<E> extends AbstractSet<E>
            implements Set<E>, Cloneable, java.io.Serializable {
            private transient HashMap<E,Object> map;
            // Dummy value to associate with an Object in the backing Map
            private static final Object PRESENT = new Object();
            public HashSet() {
                map = new HashMap<>();
            }
            ...
        }
        ```
        而HashMap通过Entry实现，Entry是一个内部类，它存储table中每一个位置上的元素值和KEY。
        ```java
                static class Entry<K,V> implements Map.Entry<K,V> {
                    final K key;
                    V value;
                    Entry<K,V> next;
                    int hash;
                    ....
                }
        ```
        HashSet 通过HashMap的key去重（不允许添加重复的entry），HashMap的value使用了Object中的一个对象实例（PRESENT(final)），做了一个空的占位。可以理解HashSet的结构就是：key - value（占位符），这个value不需要具体的意义，只是为了定义这个entry而存在就可以了。
  - [HashMap和Hashtable有什么区别？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21093&query=&asc=true&order=&page=25)
    -
  - [数组(Array)和列表(ArrayList)有什么区别？...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21094&query=&asc=true&order=&page=26)
  - [ArrayList和LinkedList有什么区别？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21095&query=&asc=true&order=&page=27)
  - [Comparable和Comparator接口是干什么的？...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21096&query=&asc=true&order=&page=28)
  - [什么是Java优先级队列(Priority Queue)？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21097&query=&asc=true&order=&page=29)
  - [你了解大O符号(big-O notation)么？你能给出...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21098&query=&asc=true&order=&page=30)
  - [如何权衡是使用无序的数组还是有序的数组？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21099&query=&asc=true&order=&page=31)
  - [Java集合类框架的最佳实践有哪些？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21100&query=&asc=true&order=&page=32)
  - [Enumeration接口和Iterator接口的区别有哪些？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21101&query=&asc=true&order=&page=33)
  - [HashSet和TreeSet有什么区别？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21102&query=&asc=true&order=&page=34)
  - [Java中垃圾回收有什么目的？什么时候进行垃圾回收？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21103&query=&asc=true&order=&page=35)
  - [System.gc()和Runtime.gc()会做什么事情？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21104&query=&asc=true&order=&page=36)
  - [finalize()方法什么时候被调用？析构函数(fina...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21105&query=&asc=true&order=&page=37)
  - [如果对象的引用被置为null，垃圾收集器是否会立即释放对象...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21106&query=&asc=true&order=&page=38)
  - [Java堆的结构是什么样子的？什么是堆中的永久代(Perm...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21107&query=&asc=true&order=&page=39)
  - [串行(serial)收集器和吞吐量(throughput)...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21108&query=&asc=true&order=&page=40)
  - ---
  - [说出三种支持重绘(painting)的组件。](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21129&query=&asc=true&order=&page=61)
  - [什么是裁剪(clipping)？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21130&query=&asc=true&order=&page=62)
  - [MenuItem和CheckboxMenuItem的区别是什么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21131&query=&asc=true&order=&page=63)
  - [边缘布局(BorderLayout)里面的元素是如何布局的？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21132&query=&asc=true&order=&page=64)
  - [网格包布局(GridBagLayout)里面的元素是如何布局的？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21133&query=&asc=true&order=&page=65)
  - [Window和Frame有什么区别？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21134&query=&asc=true&order=&page=66)
  - [裁剪(clipping)和重绘(repainting)有什...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21135&query=&asc=true&order=&page=67)
  - [事件监听器接口(event-listener interf...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21136&query=&asc=true&order=&page=68)
  - [GUI组件如何来处理它自己的事件？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21137&query=&asc=true&order=&page=69)
  - [Java的布局管理器比传统的窗口系统有哪些优势？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21138&query=&asc=true&order=&page=70)
  - [Java的Swing组件使用了哪种设计模式？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21139&query=&asc=true&order=&page=71)
  - ### [[jdbc]]
    - [什么是JDBC？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21140&query=&asc=true&order=&page=72)
      collapsed:: true
      - JDBC是允许用户在不同数据库之间做选择的一个抽象层。JDBC允许开发者用JAVA写数据库应用程序，而不需要关心底层特定数据库的细节。
    - [解释下驱动(Driver)在JDBC中的角色。](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21141&query=&asc=true&order=&page=73)
      collapsed:: true
      - 提供了特定厂商对JDBC API接口类的实现，驱动必须要提供java.sql包下面这些类的实现
        collapsed:: true
        - Connection
        - Statement
        - PreparedStatement
        - CallableStatement
        - ResultSet
        - Driver
    - [Class.forName()方法有什么作用？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21142&query=&asc=true&order=&page=74)
      collapsed:: true
      - 初始化参数指定的类，并且返回此类对应的Class 对象
    - [PreparedStatement比Statement有什么优势？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21143&query=&asc=true&order=&page=75)
      collapsed:: true
      - PreparedStatements是预编译的，因此，性能会更好。同时，不同的查询参数值，PreparedStatement可以重用。
    - [什么时候使用CallableStatement？用来准备CallableStatement的方法是什么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21144&query=&asc=true&order=&page=76)
      collapsed:: true
      - CallableStatement用来执行存储过程。
      - 存储过程是由数据库存储和提供的。
      - 存储过程可以接受输入参数，也可以有返回结果。
      - 鼓励使用存储过程，因为它提供了安全性和模块化。
      - 准备一个CallableStatement的方法是：
        CallableStatement Connection.prepareCall();
    - [数据库连接池是什么意思？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21145&query=&asc=true&order=&page=77)
      collapsed:: true
      - 像打开关闭数据库连接这种和数据库的交互可能是很费时的，尤其是当客户端数量增加的时候，会消耗大量的资源，成本是非常高的
      - 可以在应用服务器启动的时候建立很多个数据库连接并维护在一个池中。连接请求由池中的连接提供。在连接使用完毕以后，把连接归还到池中，以用于满足将来更多的请求
  - [什么是RMI？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21146&query=&asc=true&order=&page=78)
    collapsed:: true
    - Java RMI，Remote Method Invocation，Java的远程方法调用
      description:: Java所特有的分布式计算技术，它允许运行在一个Java虚拟机上的对象调用运行在另一个Java虚拟机上的对象的方法，从而使Java编程人员可以方便地在网络环境中作分布式计算
    - 面向对象设计要求每个任务由最适合该任务的对象执行，RMI将这个概念更深入了一步，使任务可以在最适合该任务的机器上完成。
    - RMI定义了一组远程接口，可以用于生成远程对象。客户机可以象调用本地对象的方法一样用相同的语法调用远程对象。RMI API提供的类和方法可以处理所有访问远程方法的基础通信和参数引用要求的串行化
    - 使用RMI开发步骤：
      collapsed:: true
      - 1、定义一个远程接口（远程接口必须继承接口，每个方法必须抛出远程异常，方法参数和方法返回值都必须是可序列化的）
      - 2、实现远程接口
      - 3、定义使用远程对象的客户程序
      - 4、产生远程访问对象的桩和框   5、注册远程对象   6、运行服务器和客户程序
  - [RMI体系结构的基本原则是什么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21147&query=&asc=true&order=&page=79)
    collapsed:: true
    - 基本原则就是把对象的使用和对象的创建相分离，我们在服务器端定义类，定义开放哪些方法，并创建对象；在客户端调用对象的方法
  - [RMI体系结构分哪几层？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21148&query=&asc=true&order=&page=80)
    collapsed:: true
    - ![](https://uploadfiles.nowcoder.com/files/20190325/466357877_1553488666460_thumb525-Archilecture-of-RMI-c69de7547869dfcf6fee3a2bad5e25ae.jpg)
    - 存根和骨架层(Stub and Skeleton layer)
      collapsed:: true
      - 这一层对程序员是透明的，它主要负责拦截客户端发出的方法调用请求，然后把请求重定向给远程的RMI服务。
    - 远程引用层(Remote Reference Layer)
      collapsed:: true
      - RMI体系结构的第二层用来解析客户端对服务端远程对象的引用。这一层解析并管理客户端对服务端远程对象的引用。连接是点到点的。
    - 传输层(Transport layer)
      collapsed:: true
      - 这一层负责连接参与服务的两个JVM。这一层是建立在网络上机器间的TCP/IP连接之上的。它提供了基本的连接服务，还有一些防火墙穿透策略。
  - [RMI中的远程接口(Remote Interface)扮演了什么样的角色？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21149&query=&asc=true&order=&page=81)
    collapsed:: true
    - A remote object is an instance of a class that implements a remote interface. A remote interface extends the interface java.rmi.Remote and declares a set of remote methods. Each remote method must declarejava.rmi.RemoteException (or a superclass of RemoteException)
       来自：https://docs.oracle.com/javase/8/docs/technotes/guides/rmi/hello/hello-world.html
  - [java.rmi.Naming类扮演了什么样的角色？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21150&query=&asc=true&order=&page=82)
  - [RMI的绑定(Binding)是什么意思？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21151&query=&asc=true&order=&page=83)
  - [Naming类的bind()和rebind()方法有什么区别？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21152&query=&asc=true&order=&page=84)
  - [让RMI程序能正确运行有哪些步骤？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21153&query=&asc=true&order=&page=85)
  - [RMI的stub扮演了什么样的角色？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21154&query=&asc=true&order=&page=86)
  - [什么是分布式垃圾回收(DGC)？它是如何工作的？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21155&query=&asc=true&order=&page=87)
  - [RMI中使用RMI安全管理器(RMISecurityMan...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21156&query=&asc=true&order=&page=88)
  - [解释下Marshalling和demarshalling。](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21157&query=&asc=true&order=&page=89)
  - [解释下Serialization和Deserializat...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21158&query=&asc=true&order=&page=90)
  - [什么是Servlet？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21159&query=&asc=true&order=&page=91)
  - [说一下Servlet的体系结构。](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21160&query=&asc=true&order=&page=92)
  - [Applet和Servlet有什么区别？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21161&query=&asc=true&order=&page=93)
  - [GenericServlet和HttpServlet有什么区别？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21162&query=&asc=true&order=&page=94)
  - [解释下Servlet的生命周期。](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21163&query=&asc=true&order=&page=95)
  - [doGet()方法和doPost()方法有什么区别？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21164&query=&asc=true&order=&page=96)
  - [什么是Web应用程序？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21165&query=&asc=true&order=&page=97)
  - [什么是服务端包含(Server Side Include)？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21166&query=&asc=true&order=&page=98)
    collapsed:: true
    - 服务端包含(SSI)是一种简单的解释型服务端脚本语言，大多数时候仅用在Web上，用servlet标签嵌入进来。SSI最常用的场景把一个或多个文件包含到Web服务器的一个Web页面中。当浏览器访问Web页面的时候，Web服务器会用对应的servlet产生的文本来替换Web页面中的servlet标签。
    - 如果增加的动态内容少，就用SSI，如果整个页面大多数都需要动态加载，则可以使用cgi提供整个页面，或者使用其他的动态技术。
  - [什么是Servlet链(Servlet Chaining)？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21167&query=&asc=true&order=&page=99)
  - [如何知道是哪一个客户端的机器正在请求你的Servlet？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21168&query=&asc=true&order=&page=100)
  - [HTTP响应的结构是怎么样的？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21169&query=&asc=true&order=&page=101)
  - [什么是cookie？session和cookie有什么区别？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21170&query=&asc=true&order=&page=102)
  - [浏览器和Servlet通信使用的是什么协议？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21171&query=&asc=true&order=&page=103)
  - [什么是HTTP隧道？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21172&query=&asc=true&order=&page=104)
  - [sendRedirect()和forward()方法有什么区别？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21173&query=&asc=true&order=&page=105)
  - [什么是URL编码和URL解码？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21174&query=&asc=true&order=&page=106)
    collapsed:: true
    - URL编码是负责把URL里面的空格和其他的特殊字符替换成对应的十六进制表示，反之就是解码。
  - [什么是JSP页面？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21175&query=&asc=true&order=&page=107)
  - [JSP请求是如何被处理的？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21176&query=&asc=true&order=&page=108)
  - [JSP有什么优点？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21177&query=&asc=true&order=&page=109)
  - [什么是JSP指令(Directive)？JSP中有哪些不同...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21178&query=&asc=true&order=&page=110)
  - [什么是JSP动作(JSP action)？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21179&query=&asc=true&order=&page=111)
  - [什么是Scriptlets？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21180&query=&asc=true&order=&page=112)
  - [声明(Decalaration)在哪里？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21181&query=&asc=true&order=&page=113)
  - [什么是表达式(Expression)？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21182&query=&asc=true&order=&page=114)
  - [隐含对象是什么意思？有哪些隐含对象？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21183&query=&asc=true&order=&page=115)
  - [面向对象软件开发的优点有哪些？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21184&query=&asc=true&order=&page=116)
  - [封装的定义和好处有哪些？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21185&query=&asc=true&order=&page=117)
  - [多态的定义？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21186&query=&asc=true&order=&page=118)
  - [继承的定义？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21187&query=&asc=true&order=&page=119)
  - [抽象的定义？抽象和封装的不同点？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21188&query=&asc=true&order=&page=120)
  -
- source:: https://github.com/Snailclimb/JavaGuide
  created:: [[20221207]]
  collapsed:: true
   ![](https://img.shields.io/github/stars/Snailclimb/JavaGuide)
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
      - [[jvm]] vs jdk vs jre
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
        - ![image.png](../../soul/assets/javaguide/image_1670400578900_0.png)
          - 接口规则由接口调用方确定
            - 由不同的厂商去根据这个规则对这个接口进行实现，从而提供服务
      - SPI 的优缺点?
        collapsed:: true
        - 接口设计的灵活性UP
        - 局限
          - 需要遍历加载所有的实现类，不能做到按需加载，这样效率还是相对较低的。
          - 当多个  `ServiceLoader`  同时  `load`  时，会有并发问题
    - 序列化和反序列化
      - 什么是序列化? 什么是反序列化?
      - 如果有些字段不想进行序列化怎么办?
        -
      - 常见序列化协议有哪些?
        collapsed:: true
        - JDK 自带的序列化方式一般不用 (效率低 & 安全问题)
          collapsed:: true
          - TODO 基于二进制的序列化协议 #project
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