- {{renderer :tocgen2}}
- ## 概述
  - 2018年3月21日, Oracle官方宣布JAVA10正式发布
  - JAVA9和java10 都不是 LTS (Long-Term-Support)版本.和过去的JAVA大版本升级不同,这两个只有半年左右的开发和维护时间. 而JAVA11 也是就是18.9,才是JAVA之后的第一个长期支持版本
  - JAVA10 一共定义了109个新特性,其中包含JEP,对程序员来说,真正的新特性也就一个,还有一些新的API和JVM规范以及JAVA语言规范上的改动.
  - JAVA10 的12个JEP (JDK Enhancement Proposal特性加强协议) ,可参阅官方文档 http://openjdk.java.net/projects/jdk/10/
  - ![1630388526815](../assets/mashibing/1630388526815.png)
    - > 286: 局部变量类型推断
      > 296: JDK库合并
      > 304: 统一的垃圾回收接口
      > 307:为G1提供并行的Full GC
      > 310:应用程序类数据共享
      > 312: ThreadLocal握手交互
      > 313: 移除JDK中附带的javah工具
      > 314: 使用附加的Unicode语言标记拓展
      > 316:能将对内存占用分配给用户指定的备用内存设备
      > 317:使用基于JAVA的JIT编译器
      > 319: 根证书
      > 322:基于时间的发布版本
- ## 一 语法层次的变化
  - ### 1_局部变量的类型推断
    - > 局部变量的显示类型声明,常常认为是不必须的,给一个好听的名字经常可以很清楚的表达出下面应该怎样继续.减少了啰嗦和形式的代码,避免了信息的冗余,而且对齐了变量名,容易阅读
    - 作为JAVA程序员,在声明一个变量时,我们一般都是书写两次变量类型,第一次用于声明变量类型,第二次用于构造器
      - ``` java
        ArrayList<String> list =new ArrayList<>();
        ```
    - 变量的声明类型书写复杂且较长,尤其是加上泛型的使用
      - ``` java
        Iterator<Map.Entry<Integer,Student>> iterator=set.iterator();
        ```
    - 我们也经常声明一种变量,它只被使用一次,并且是在下一行代码中
      - ``` java
        URL url=new URL("http://www.mashibing.com");
        URLConnection connection= url.openConnection();
        Reader reader =new BufferedReader(new InputStreamReader( connection.getInputStream));
        ```
    - > **总之: 变量标识符(变量名)就可以让我清楚的知道变量如何使用,没必要前面加上一大串的类型声明**
    - 局部变量推断有点类似JavaScript中的弱变量类型的写法,通过后面的数据来推断前面的数据类型,数据类型的声明统一为var
      - ``` java
        public void test1(){
          // 局部变量,根据所赋的值,推断变量的类型
          var num =10;
          var arrayList =new ArrayList<String>();
          // 遍历操作
          for(var i : arrayList){
              System.out.println(i);
              System.out.println(i.getClass());
          }
          // 普通的遍历操作
          for(int i =0;i<100;i++){
              System.out.println(i);
          }
          // 推断类型的遍历操作
          for(var i =0;i<100;i++){
              System.out.println(i);
          }
          
        }
        ```
    - > 什么情况下不能使用类型推断
      - 1 变量的声明不能使用类型推断,因为无法推断
        - ``` java
          // 根据右边的数据推断类型,不赋值压根没给推断的机会,这是错的
          var name;
          ```
      - 2 初始值为null
        - ``` java
          // null值无法推断数据类型,这是不能使用类型推断
          var str =null;
          ```
      - 3 lambda表达式
        - ``` java
          // 这是OK的
          Supplier<Double> supplier=()-> Math.random();
          // 这是不OK的 lambda表达式需要显式数据类型,不然无法明确是哪个接口
          var supplier2=()->Math.random();
          ```
      - 4 方法引用
        - ``` java
          // 这是可以的进行方法引用的
          Consumer<String> consumer=System.out::println;
          // 这是不可以的,无法明确接口类型
          var consumer2=System.out::println;
          ```
      - 5 为数组静态初始化
        - ```java
          //动态初始化数据可以进行类型推断
          var arr =new String[10];
          //静态初始化数组不可以使用类型推断 
          var arr2 ={"asdf","qwer","zxcv","tyui","ghjk"};
          ```
      - 6 类型推断仅仅是局部变量,成员变量不可以使用类型推断
        - ``` java
          public class Test1 {
            // 成员变量不能使用类型推断
            var name="小明";
            public void testMethod1(){
              // 局部变量可以使用类型推断
              var localname="小明";
            }
          }
          ```
      - 7 其他不可以推断的情况
        - ```java
          // 情况1 没有初始化的局部变量声明
          var s; var x=null;
          // 情况2 方法的返回值类型
          public var test1()
          // 情况3 方法的参数类型
          public void test2(var a,var b)
          // 情况4 构造器的参数类型
          public Person(var name,var age)
          // 情况5 属性
          class Person{
            var name;
          }
          // 情况6 catch块
          try{
          }catch(var e){
          }
          ```
    - > 以下两点需要注意
      - 1 var不是一个关键字
        - > 我们无需担心变量名或者方法名会与var发生冲突,因为var实际上不是一个关键字,而是一个类型名,只有在编译器需要知道类型的地方法才会用到它.除此之外,他就是一个普通的合法标识符.也就是说,除了不能用它做类名,其他都可以.但是又有哪个傻瓜非要用var做类名呢?
      - 2 这毕竟不是JavaScript
        - > var并不会改变java是一门静态语言的事实,编译器负责推断出类型,并把结果写入字节码,也就是说,数据类型还是在字节码中的,java还是属于强类型的编程语言,开发人员没有明确写出来而已.而JavaScript是弱类型解释型的脚本语言,和这里的类型推断是两回事.
- ## 二 API层次的变化
  - ### 1_集合中新增copyOf创建只读集合
    - ``` java
      // JAVA9中新增创建只读的方法
      var strings1 = List.of("MCA", "JAVA", "Golang");
      // JAVA10中新增的创建只读集合的方法
      var strings2 = List.copyOf(strings1);
      // 判断两个集合在内存上是否是同一个,结果为true
      System.out.println(strings1==strings2);
      // 创建一个普通集合
      var strings3=new ArrayList<String>();
      // 通过copyOf方法创建一个只读集合
      var strings4 = List.copyOf(strings3);
      // 判断两个集合在内存上是否是同一个,结果为false
      System.out.println(strings3==strings4);
      ```
      - >  结论:copyOf方法的作用通过一个集合返回的是一个只读集合,如果参数本来就是只读集合,那么返回的就是参数,如果参数不是只读集合,就再创造一个只读集合返回