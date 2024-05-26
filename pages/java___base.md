title:: java/base
mark:: java syntax
- ## Type (8)
  collapsed:: true
  - Keywords
    - ![](../assets/java_keywords.png)
      collapsed:: true
      - | 分类                 | 关键字   |            |          |              |            |           |        |
        | :------------------- | -------- | ---------- | -------- | ------------ | ---------- | --------- | ------ |
        | 访问控制             | private  | protected  | public   |              |            |           |        |
        | 类，方法和变量修饰符 | abstract | class      | extends  | final        | implements | interface | native |
        |                      | new      | static     | strictfp | synchronized | transient  | volatile  | enum   |
        | 程序控制             | break    | continue   | return   | do           | while      | if        | else   |
        |                      | for      | instanceof | switch   | case         | default    | assert    |        |
        | 错误处理             | try      | catch      | throw    | throws       | finally    |           |        |
        | 包相关               | import   | package    |          |              |            |           |        |
        | 基本类型             | boolean  | byte       | char     | double       | float      | int       | long   |
        |                      | short    |            |          |              |            |           |        |
        | 变量引用             | super    | this       | void     |              |            |           |        |
        | 保留字               | goto     | const      |          |              |            |           |        |
  -
  - Type 类型
    - | 內置/基本 类型 | 類型定義| 類型取值|`java.lang.`|
      |--|--|--|--|
      | boolean | 布尔| true/false | Boolean |
      | byte    | 8位整数| -128 ~ 127 | Byte |
      | short   | 16位整数          | -32768~32767|Short|
      | int     | 32位整数           | -2147483648($$-2^{31}$$) ~ 2147483647($$2^{31}$$-1) |**Integer**|
      | long    | 64位整数          | -263~(263-1)|Long|
      | float   | 32位浮点数       | 1.4E-45($$2^{-149}$$)~3.4028235E38($$2^{128}-1$$) |Float|
      | double  | 64位浮点数    | 4.9E-324~1.7976931348623157E308 |Double|
      | char      | 32位Unicode | 不適用(可以與int互相轉換)                            |**Character**|
    - 內置類型 / 基本類型 / Primitive Types
    - Java 默认不支持无符号数, 已经上线 API -> https://blogs.oracle.com/darcy/entry/unsigned_api
      id:: 6245b306-1212-4077-bb9e-4a0d3d3371b4
      - id:: 6245b438-bc5a-4329-ba1e-9b325d5ee9dd
        > Much of the relative simplicity of Java is - like for most new languages - partly an illusion and partly a function of its incompleteness. As time passes, Java will grow significantly in size and complexity. It will double or triple in size and grow implementation-dependent extensions or libraries. That is the way every commercially successful language has developed. Just look at any language you consider successful on a large scale. I know of no exceptions, and there are good reasons for this phenomenon. [I wrote this before 2000; now (2012), the language part of the Java 7 specification is slightly longer in terms of number of pages than the ISO C++11 language specification.]
        >  正如大多数其他新语言一样，Java的简洁性，一部分是幻觉，一部分是功能不完整。日后，Java必将大幅度（至少两到三倍地）增加其规模和复杂度，并采用很多实现相关的库。此乃每个商业上成功语言的必经之路，绝无例外。——以上预言是我2000年前说的， 现在，公元2012年，Java 7 的规范已经比 ISO C++11 的还要长那么一点点。
        via: https://www.stroustrup.com/bs_faq.html#Java & https://www.zhihu.com/question/39596383/answer/82267124
    - 传参
      - [Java/數據類型 - 維基教科書，自由的教學讀本](https://zh.wikibooks.org/wiki/Java/%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B)
        - 處理二進制數據塊使用byte
        - Java也提供了基本類型的類包裹(Wrapper)，這些類包裹都包括在了java.lang包裡面作為Java的語言基礎，比如對int的類包裹是Integer類。提供這些類包裹的原因主要是為了在某些接口上提供和類（對象）一致的接口，比如在泛型設計上的數據模板等等。
          - 相應的包裹類中還提供了對基本數據類型的操作，比如int Integer.parseInt(String s, int radix)將字符串轉化為相應進制的整型數
        - java
          - 基本類型 -> 傳值
          - 對象類型 -> 傳引用
    - 运算符的优先级
      - **一元运算符>算术运算符>比较运算符>逻辑运算符>位运算符>赋值运算符**
        - ![预览大图](https://data.educoder.net/api/attachments/189038){:height 233, :width 262}
        - [请问 C++ 运算符的优先级表需要背诵记忆吗？ - 知乎](https://www.zhihu.com/question/418086769)
      - **Java中一条语句可以分为多行（但是不能将一个字符串分在多行书写），正因为如此，Java的每条语句结尾必须有分号。**
      - 包装类 (wrapper)
        - 包装类对象一经创建，其内容（所封装的基本类型数据值）不可改变(类似于String类，可看源码)
        - Primitive vs Wrapper
          id:: 6d71a35b-f417-42ef-b7dd-b6c59c1bccad
          - 定义
            - 包装类属于对象
            - 基本数据类型不是
          - 声明和使用方式
            - 包装类使用new初始化，有些集合类的定义不能使用基本数据类型，例如 ArrayList<Integer>
          - 初始值
            - 包装类默认值为null
            - 基本数据类型则不同的类型不一样（具体见上表）
              id:: 6245b604-0e80-432d-955c-95e99b5e9008
          - 存储方式和位置不同，从而性能不同
            - 基本数据类型存储在栈（stack）中
            - 包装类则分成引用和实例，引用在栈（stack）中，具体实例在堆（heap）中
            - 可以通过程序来验证速度的不同
        - 自动装箱 / 拆箱 / Auto-Boxing / Unboxing.
          - From: Java 5.
          - ```java
             int int1 = 1;
             Integer integer2 = int1;     // 自動裝箱
             int int3 = integer2;         // 自動拆箱
            /**字節碼反編譯後，會還原出其隱式調用的轉換方法**/
             int int1 = 1;
             Integer integer2 = Integer.valueOf(int1);     // 自動裝箱的本质，通过调用valueOf将值对象化
             int int3 = integer2.intValue();               // 自動拆箱的本质，通过调用xxxValue将对象值化
            ```
-
- ## Method
  collapsed:: true
  - 静态方法为什么不能调用非静态成员? #[[jvm]]
    - 静态方法属于类，在类加载的时候就会分配内存，可以通过类名直接访问
    - 非静态成员属于实例对象，只有在对象实例化之后才存在，需要通过类的实例对象去访问。
    - 静态成员 早于 非静态成员 存在. 如果调用在内存中还不存在的非静态成员 => 非法操作
  - 静态方法 vs 实例方法
    - 调用方式: 创建对象\?
      - `类名.方法名` + `对象.方法名`
    - 限制访问:
      - 静态方法 => 静态成员; ✖类成员
  -
  - In [[Java]], between  [[overload]] #vs [[override]]
    - | **区别点**     | **Overload** | **Override** |
      | :--------- | :------- |:----------- |
      | **发生范围**   | 同一个类 | 子类 |
      | **参数列表**   | 必须修改 | 一定不能修改|
      | **返回类型**   | 可修改   | 子类方法返回值类型 \<= 父类方法返回值类型|
      | **异常**       | 可修改   | 子类方法声明抛出的异常类 \<= 父类方法声明抛出的异常类 |
      | **访问修饰符** | 可修改   | 一定不能做更严格的限制（可以降低限制）|
      | **发生阶段**   | 编译期   | 运行期|
    - 特殊
      - 子类方法的访问权限 \>= 父类方法的访问权限
      - 如果方法的返回类型是 void 和基本数据类型，则返回值重写时不可修改 ( 当然也没有必要改
        - 但是如果方法的返回值是引用类型，重写时是可以返回该引用类型的子类的。
-
- WAITING `class` -> `field` + `method`
- WAITING `field` -> 域 / 域变量 / 属性 / 成员变量 / **字段**
  - C++中, 有成员变量 (member variable) 及成员函数 (member function) 的叫法，成员变量属于data member. ([via](https://en.cppreference.com/w/cpp/language/classes)).
  - Java中则专门用field及method, (via: [java语言规范](https://docs.oracle.com/javase/specs/jls/se14/html/jls-8.html#jls-8.1.6)), 其中只用field及method，从来没有用过“member variable"或”member function"这样的说法。
    - Java中的field，一般译为"字段“（包括官方jdk文档的中译版，[这里](https://www.cjsdn.net/Doc/JDK60/java/lang/Math.html)有个早期的备份), 但是Sun公司被Oracle收购后就没有出过新版的官方中文API文档), 在这个官方的文档中, 也是将一个类的文档分成“字段 | 构造方法 | 方法”三个部分。
    - 阿里巴巴是Java的重度使用者，并且开发有专门的JDK实现版本，他们也都将field翻译为字段(via: https://github.com/alibaba/p3c) 其中的 阿里巴巴Java开发手册（泰山版）.pdf
  - C\#（csharp)语言，微软的国际化是做得比较完备的，它的语言规范中，都是将field译为”字段“，via: https://docs.microsoft.com/zh-cn/dotnet/csharp/language-reference/language-specification/classes#fields
  - Python语言的官方中文文档中，将称“数据成员”称为”属性“（注意它没有用过“成员变量”一词），via: https://docs.python.org/zh-cn/3/tutorial/classes.html#class-definition-syntax
  - 数据库领域中，field也无一例外地译为“字段”。
- `method` -> 功能/操作
-
-