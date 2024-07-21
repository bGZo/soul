alias:: Object-oriented programming, 面向对象, 面向对象编程
description:: [Object-oriented programming - Wikipedia](https://en.wikipedia.org/wiki/Object-oriented_programming)

- ## [[java]] #vs [[cpp]]
  - **虚函数**
    description:: 为了多态
    - Java 没有虚函数的概念 -> Java 普通函数 == C++ 虚函数
      - **动态绑定**是 Java 的默认行为
      - 如果 Java 中不希望某个函数具有虚函数特性，可以加上 final 关键字变成非虚函数
  - **抽象函数(纯虚函数)**
    description:: 为了定义接口
    - ```cpp
      virtual void print() = 0;
      ```
    - ```java
      abstract void print();
      ```
  - **抽象类**
    description:: "父类中既包括子类共性函数的具体定义，也包括需要子类各自实现的函数接口"
    - C++ 中抽象类只需要包括纯虚函数，既是一个抽象类。如果仅仅包括虚函数，不能定义为抽象类，因为类中其实没有抽象的概念。
    - Java 抽象类是用 abstract 修饰声明的类。
  - **接口**
    description:: "为了形成一种规约, 不能有 普通成员变量 + 非纯虚函数"
    - C++ 中接口其实就是全虚基类。
    - Java 中接口是用 interface 修饰的类。
  - **小结**
    - C++ 虚函数    ==  Java 普通函数
    - C++ 纯虚函数  ==  Java 抽象函数
    - C++ 抽象类    ==  Java 抽象类
    - C++ 虚基类    ==  Java 接口
  - [JAVA – 虚函数、抽象函数、抽象类、接口](https://www.runoob.com/note/40084)