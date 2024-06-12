tags:: #lang/programming
icon:: ☕

- ## Why
  - Why use Java?
    - ...
- ## How
  - How use Java?
    - ...
- ## What
  - Java is what?
  - Java versions
    - [[java 1]]
    - [[java 2]]
    - [[java 5]]
    - [[java 6]]
    - [[java 7]]
    - [[java 8]]
    - ...
    - [[java 22]]
  - Java's roadmap (3 main)
    collapsed:: true
    - **Java SE** / Java Platform, Standard Edition / ~~J2SE~~
      logseq.order-list-type:: number
    - **Jakarta EE** / Java Platform, Enterprise Edition / ~~Java EE~~ / ~~J2EE~~
      logseq.order-list-type:: number
    - **Java ME** / Java Platform, Micro Edition / ~~J2ME~~
      logseq.order-list-type:: number
    - ---
    - 有几点需要说明：
      - SE 主要包含语言特性，标准库和虚拟机 [[jvm]]
        logseq.order-list-type:: number
      - EE 主要包含企业级 API，如 [[servlet]]、 [[jsp]]、EJB、JMS、JPA、 [[cdi]]等。
        logseq.order-list-type:: number
      - ME 主要面向移动设备进行开发，正转向其他平台；
        logseq.order-list-type:: number
        - 注意 JavaME != Android != 嵌入系统开发
      - *J2SE / J2EE / J2ME* 均是 [[java 2]] 时代的称呼，自 [[java 5]] 之后集体更名为 *JavaSE / JavaEE / JavaME*； JavaEE 在 [[java 8]] 之后被 Oracle 移交 [[eclipse]] 基金会管理，故更名为 Jakarta；
        logseq.order-list-type:: number
  - What's the difference with [[cpp]]?
    collapsed:: true
    - | Items | Java | [[cpp]] |
      | 面向对象(封装/继承/多态)|✔|✔|
      | 方法重载 |✔|✔|
      | 指针(直接访问内存)  | ✖ | ✔|
      | 类多继承 | ✖(接口替代) | ✔|
      | 操作符重载| ✖ |✔(复杂++)|
      | 内存管理垃圾回收机制(GC) / 内存安全 | ✔ | ✖ |
  - ## [[oop]]
    collapsed:: true
    - 封装 Encapsulation
      mark:: 明确接口
    - 继承 Composition, inheritance, and delegation (委托???)
      mark:: "继承基类, 做出扩展; 子类(完全)兼容基类"
      collapsed:: true
      - 继承 (泛化)
        - 实现继承
          mark:: 无需额外编码的能力
        - 可视继承
          mark:: 子窗体（类）使用基窗体（类）的外观和实现代码的能力
      - 组合 (聚合)
        - 接口继承
          mark:: 子类必须提供实现的能力
        - 纯虚类
    - 多态 Polymorphism
      mark:: "基于对象所属类的不同, 外部对同一个方法的调用, 实际执行的逻辑不同; 多态依赖继承"
      collapsed:: true
      - 重写/覆盖 Override
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
        - 同名函数
    - 接口 #vs 抽象类
      id:: 63e7791a-04a5-425e-a98b-9c35bd1f7400
      collapsed:: true
      - 1.接口的方法默认是public，所有方法在接口中不能有实现，抽象类可以有非抽象的方法
      - 2.接口中的实例变量默认是final类型的，而抽象类中则不一定
      - 3.非抽象类类可以实现多个接口，但最多只能实现一个抽象类
      - 4.一个类实现接口的话要实现接口的所有方法，而抽象类不一定
      - 5.接口不能用new实例化，但可以声明，但是必须引用一个实现该接口的对象
      - #[[java 8]] 在接口中用default修饰的方法可以有函数体
    - 纯虚类 #vs 接口
      collapsed:: true
      - 同
        - 都是抽象类，都不能实例化
        - 接口实现类 & 抽象子类必须要实现已经声明的抽象方法
      - 异
        - 纯虚类
        - 接口
-