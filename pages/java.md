icon:: ☕
type:: lang/programming
description:: 静态强类型，但因为提供了类似反射等机制，也具备了部分动态类型语言的能力

- ## What
  -
- [[oop]]
  collapsed:: true
  - 封装 Encapsulation
    collapsed:: true
    - 明确接口
  - 继承 Composition, inheritance, and delegation (委托???)
    collapsed:: true
    - 继承基类, 做出扩展; 子类(完全)兼容基类
    - 继承 (泛化)
      - 实现继承
        collapsed:: true
        - 无需额外编码的能力
      - 可视继承
        collapsed:: true
        - 子窗体（类）使用基窗体（类）的外观和实现代码的能力
    - 组合 (聚合)
      - 接口继承
        collapsed:: true
        - 子类必须提供实现的能力
      - 纯虚类
  - 多态 Polymorphism
    collapsed:: true
    - 基于对象所属类的不同, 外部对同一个方法的调用, 实际执行的逻辑不同; 多态依赖继承
    - 重写/覆盖 Override
      collapsed:: true
      - 虚函数重写
      - 接口重写
      - 注意
        - 重写**范围**
          collapsed:: true
          - **只有实例方法可以被重写**，重写后的方法必须仍为实例方法
          - **成员变量和静态方法(static)都不能被重写，只能被隐藏**
            - ??? 形式上可以写，但本质上不是重写，属于下面要讲的隐藏
            - ??? 重写方法可以改变其它的方法修饰符，如 `final` , `synchronized` , `native` 。不管被重写方法中有无final修饰的参数，重写方法都可以增加、保留、去掉这个参数的 final 修饰符(**参数修饰符不属于方法签名**)。
        - **两同两小一大**原则
          - 方法名相同，参数类型相同
          - **返回类型** 子类 <= 父类方法
          - **抛出异常** 子类 <= 父类方法
          - **访问权限** 子类 >= 父类方法
    - 重载 Overload
      collapsed:: true
      - 同名函数
  - 接口 \vs 抽象类
    id:: 63e7791a-04a5-425e-a98b-9c35bd1f7400
    collapsed:: true
    - 1.接口的方法默认是public，所有方法在接口中不能有实现，抽象类可以有非抽象的方法
    - 2.接口中的实例变量默认是final类型的，而抽象类中则不一定
    - 3.非抽象类类可以实现多个接口，但最多只能实现一个抽象类
    - 4.一个类实现接口的话要实现接口的所有方法，而抽象类不一定
    - 5.接口不能用new实例化，但可以声明，但是必须引用一个实现该接口的对象
    - java 8 在接口中用default修饰的方法可以有函数体
  - 纯虚类 \vs 接口
    collapsed:: true
    - 同
      - 都是抽象类，都不能实例化
      - 接口实现类 & 抽象子类必须要实现已经声明的抽象方法
    - 异
      - 纯虚类
      - 接口
- ## References
  collapsed:: true
  - ~~java-swing~~
    collapsed:: true
    - Under [[jetbrains/idea]] Design UI Tools
      - [IntelliJ IDE 开发Java GUI 入门 - 简书](https://www.jianshu.com/p/cdca9a30b86b)
        - 拖完页面后, 在主页面函数中右键 Generate Form, 之后就可以生成调用代码.
    - [[为什么很多人说Java不适合编写桌面应用]]
    - [swing还有人用吗？ - 知乎](https://www.zhihu.com/question/26610345)
      - 如果你学习到了 JavaSE 的 Swing 部分，建议如下：
        collapsed:: true
        - Swing 学习，主要了解其事件监听机制、常用布局和组件关系
        - 初次学习，一定要自己写代码，学完常用布局后，自己写个小型 Swing 应用，例如计算器（你可以仿照 Windows 的计算器），然后就可以继续 JavaWeb 的其余内容了，不要再深究 Swing 本身，虽然这东西有点意思
        - 初次学习，不要安装 GUI 插件，因为拖拽式开发的前提是你自己能写的出来，之后如果希望快速开发 GUI 程序，可以使用 Netbeans 自带的 Swing 设计器拖拽出界面，自己写界面以外的逻辑即可
        - Eclipse 插件，除了 Spring Tool Suite 、 Hibernate Tools、Git 等常用插件外，别瞎折腾，会累死人，在线安装 Elipse 插件时不时被墙，而且安装还有各种兼容问题，管理起来也不方便
        - 企业开发现在基本没有 Swing 什么事，自己拿 Swing 做个小的界面程序还是挺有用的
        - Oracle 官方有个教你使用 Netbeans 开发 Swing 的教程，需要的可以参考下《Learning Swing with the NetBeans IDE》
        - http://docs.oracle.com/javase/tutorial/uiswing/learn/