icon:: ☕
created:: [[20240612]]
type:: java-version

- ## Feats
  - 二进制前缀`0b` / `0B`；
    collapsed:: true
    - 整型（byte, short, int, long）可以直接用二进制表示
    - ```JAVA
      //二进制字面值前缀0b / 0B
      int i = 0b010; //10进制值为2
      int j = 0B010;
      ```
  - 字面常量数字的下划线；
    collapsed:: true
    - 用下划线连接整数提升其可读性，自身无含义，不可用在数字的起始和末尾。
    - ```java
      //数字间的下划线不影响实际值
      int k = 1_1;//值为11
      ```
  - switch 支持String类型；
  - 泛型实例化类型自动推断；
    - ```java
      Map<String, List<String>> myMap = new HashMap<String, List<String>>();    // Before
      Map<String, List<String>> myMap = new HashMap<>();        				// Now
      ```
  - try-with-resources语句；
    - ```java
       /*
         * 声明在try括号中的对象称为资源，在方法执行完毕后会被自动关闭,
         * 相对与之前必须在finally关闭资源，这一特性大大提高了代码的简洁性。
         * 所有实现java.lang.AutoCloseable接口的类都作为资源被自动关闭。
        */
       try (BufferedReader reader=new BufferedReader(new FileReader("d:1.txt"))){
          return reader.readLine();
      }
      ```
  - 单个catch中捕获多个异常类型（用`|` 分割）并通过改进的类型检查重新抛出异常；
- ## ↩ Reference
  - [Java 5，6，7，8，9，10新特性吐血总结 | 拔剑少年的博客](https://it18monkey.github.io/2018/08/05/Java%E6%96%B0%E7%89%B9%E6%80%A7%E6%80%BB%E7%BB%93/)