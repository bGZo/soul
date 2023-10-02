mark:: [Java 5.0 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/Java_5.0)

- ## Feats #.ol
  - 泛型 (Generics)
  - 增强循环（Enhanced for Loop）
    - ```java
      int[] array = {1, 2, 3, 4, 5};
      for (int i : array) {
         System.out.println(i);
      }
      ```
  - 自动封箱拆箱(Autoboxing/Unboxing)
    - 八大基本类型和它们的包装类能够自动的相互转换
    - 自动装箱 (Autoboxing)
      define:: 把一个基本类型变量直接赋给对应的包装类变量，或者赋给Object变量 (Object是所有类的父类，子类对象可以直接赋给父类变量)
      - ```java
        public class AutoBoxingUnboxing{
          public static void main(String[] args){
            //直接把一个基本类型变量赋给Integer对象
            Integer inObj=5;
            //直接把一个boolean类型变量赋给一个Object类型变量
            Object boolObj=true;
            //直接把一个Integer对象赋给int类型变量
            int it=inObj;
            if (boolObj instanceof Boolean){
              //先把Object对象强制类型转换为Boolean类型，再赋给boolean变量
              boolean b=(Boolean)boolObj;
              System.out.println(b);
            }
          }
        }
        ```
      - int类型变量只能自动装箱成Integer对象（即使赋给Object类型变量，那也只是利用了Java的**向上自动转型特性**），不要试图装箱成Boolean对象
  - 枚举(Typesafe Enums)
    - ps:**枚举是一种实现线程安全的单例模式的好方式**
      - 单例模式
        - 因为 Java 中的枚举本质上是一个类，并且只有一个实例，所以没有多线程的问题
      - 线程安全
        - 此外，枚举在运行时不能被反射或序列化，从而额外的保证了单例的安全
          - 枚举是 Java 中特殊的类，它的实现机制与普通类有很大的不同。
            - 枚举类型是通过编译器生成一个类来实现的
              - 该类继承自 Java.lang.Enum，且构造函数是私有的
              - 通过反射创建枚举实例是不可能的
          - 枚举不能被序列化，因为它的实例在整个 JVM 范围内是唯一的，因此不需要序列化
    - ```java
      enum TestEnum{
        one,
        two;
        TestEnum() {
        }
      }
      ```
  - 可变参数 (Varargs)
    - 语法：`(type... arguments)`
    - 可变参数本质仍然是用一个数组存储参数，只是java隐藏了这一过程
    - 需要注意的是如果一个方法声明中含有可变参数，那必须放在最后一个位置。
  - 静态导入（Static Import）
    - 通过import类来使用类里的静态变量或方法（直接通过名字，不需要加上`类名.`）,简化了代码的书写
    - ps:过去的版本中只能通过继承类或实现接口才能使用。
  - 注解（Annotations）
    - 关键字`@interface`
  - 新的线程模型和并发库（`java.util.concurrent`)
  - 修改命名方式（1.5 -> 5）；
## ↩ Reference
  - [Java 5，6，7，8，9，10新特性吐血总结 | 拔剑少年的博客](https://it18monkey.github.io/2018/08/05/Java%E6%96%B0%E7%89%B9%E6%80%A7%E6%80%BB%E7%BB%93/)