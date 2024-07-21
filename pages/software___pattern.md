
- [[Quickref]]
  - UML
    id:: 634cd4bc-9950-4d3c-8057-466be4c059e3
  - Use Case
    id:: 634cd41e-7603-46d6-bf66-1c3e3fab1d9f
  - Tips
    id:: 634cd41e-4718-4114-9526-b255fc2d4bda
  - Effect
    id:: 634cf9cc-6b4f-48b7-9214-a8ad936a9672
-
- Outline
  - pattern
    - #vs [[algorithm]]
      collapsed:: true
      - 算法更像是菜谱: 提供达成目标的明确步骤
      - 模式更像是蓝图: 你可以看到最终的结果和模式的功能, 但需要自己确定实现步骤。
    - include
      collapsed:: true
      - **意图**部分简单描述问题和解决方案。
      - **动机**部分将进一步解释问题并说明模式会如何提供解决方案。
      - **结构**部分展示模式的每个部分和它们之间的关系。
      - **在不同语言中的实现**提供流行编程语言的代码， 让读者更好地理解模式背后的思想。
    -
  - Principles, 6, S.O.L.I.D + LoD
    collapsed:: true
    - [SRP] Single Responsibility Principle
      description:: **单一职责**; ==1 个类应该仅有 1 个引起它变化的原因. 任何修改只有 1 个原因==[ASD]
      collapsed:: true
      - Why
        - ==耦合会导致脆弱的设计==
        - $$类承担的职责过多(职责耦合) → 某个职责变化 → 削弱/抑制类完成其他职责$$
      - ((634cd41e-7603-46d6-bf66-1c3e3fab1d9f))
        - 分类信息 / ==垂直搜索==
      - ((634cd41e-4718-4114-9526-b255fc2d4bda))
        - 软件设计真正要做的许多内容 → ==发现职责并把那些职责相互分离==
          - 判断是否应该分离?
            - **如果你能够想到多于一个的动机去改变一个类，那么这个类就具有多于一个的职责**
    - [OCP] Open/Closed Principle
      description:: **开闭原则**; 开放扩展. 关闭修改 (软件实体 (类、模块、函数等等) )
      collapsed:: true
      - **==面向对象设计的核心==**
      - **扩展开放 (Open for extension)** / **更改封闭 (Closed for modification)**
      - ==面对需求，对程序的改动是通过增加新代码进行的，而不是更改现有的代码==[ASD]
      - Why
        - ==面对需求的改变却可以保持相对稳定==
      - ((634cd41e-4718-4114-9526-b255fc2d4bda))
        - 在开发工作展开不久就知道可能发生的变化。
          - 查明可能发生的变化所等待的时间越长，要创建正确的抽象就越困难
        - 猜测出最有可能发生的变化种类
          - 不完全封闭(总存在一些无法对之封闭的变化) → 模块应该对哪种变化封闭做出选择 → 构造抽象来隔离那些变化
        - 等到小变化发生时立即采取行动
          - 很难预先猜测 → 等到小变化发生时立即采取行动 -> 应对发生更大变化的可能
          - 假设变化不会发生。当**变化发生时，我们就创建抽象来隔离以后发生的同类变化**[ASD]
      - #+BEGIN_WARNING
        对于应用程序中的每个部分都刻意地进行抽象同样不是一个好主意。拒绝不成熟的抽象和抽象本身一样重要[ASD]
        #+END_WARNING
    - [DIP] Dependency Inversion Principle
      description:: **依赖倒置**; 高层与底层数据解耦. 只依赖抽象. 不依赖实现. **抽象不应该依赖细节. 细节应该依赖于抽象**
      collapsed:: true
      - 要针对接口编程，不要对实现编程
        - 高层模块不应该依赖低层模块。两个都应该依赖抽象
        - 抽象不应该依赖细节。细节应该依赖抽象
      - Why
        - 发现业务逻辑的高层模块都是一样的，但客户却希望使用不同的数据库或存储信息方式
          - 我们希望能再次利用这些高层模块，但高层模块都是与低层的访问数据库绑定在一起的，没办法复用这些高层模块，这就非常糟糕了
    - [LoD] Law of Demeter / Principle of Least Knowledge
      description:: **迪米特法则 / 得墨忒耳定律 / 最少知识原则**; 简单化模块间的通信. 最大程度地隐藏内部逻辑
      collapsed:: true
      - 如果两个类不必彼此直接通信，那么这两个类就不应当发生直接的相互作用。
        - 在类的结构设计上，每一个类都应当尽量降低成员的访问权限,
      - 本质
        - **类之间的松耦合**
          - 越松越有利于复用
      - 如果其中一个类需要调用另一个类的某一个方法的话，可以通过第三者转发这个调用
    - [LSP] Liskov Substitution Principle,
      description:: **里氏替换原则**; 父子类可替换
      id:: ef348d29-4248-4e81-8c6d-5c1e703883f8
      collapsed:: true
      - **子类型必须能够替换掉它们的父类型**
        - 一个软件实体如果使用的是一个父类的话，那么一定适用于其子类，而且**它察觉不出父类对象和子类对象的区别**
        - 在软件里面，把父类都替换成它的子类，程序的行为没有变化
        - Barbara Liskov女士在1988年发表
        - $$数学定义略$$
      - 尽管在生物学分类上，企鹅是一种鸟，但在编程世界里，企鹅不能以父类——鸟的身份出现，因为前提说所有鸟都能飞，而企鹅飞不了，所以，企鹅不能继承鸟类
      - Why
        - 继承复用成为了可能，只有当子类可以替换掉父类，软件单位的功能不受到影响时，父类才能真正被复用，而子类也能够在父类的基础上增加新的行为
      - Status
        - 面向对象设计的标志
          - 用哪种语言来编写程序不重要，如果编写时考虑的都是如何针对抽象编程而不是针对细节编程，即程序中所有的依赖关系都是终止于抽象类或者接口，那就是面向对象的设计，反之那就是过程化的设计了
    - [ISP] Interface Segregation Principle
      description:: **接口隔离原则**; 细粒度化接口(灵活Up)
  - ((63491e18-813e-466e-b6ca-72d05fedbaf2))
    - 创建 (c,5)
      description:: 提供创建对象的机制; 增加已有代码的灵活性和可复用性
      collapsed:: true
      - 单例 Singleton
        - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
          - ![https://user-images.githubusercontent.com/57313137/175233696-f5ac6fd0-d63e-4946-901e-b696e81bb004.png](../assets/book/秒懂设计模式/175233696-f5ac6fd0-d63e-4946-901e-b696e81bb004.png)
        - 作用
          - 使用单例，可以确保其它类只获取类的一份数据。
          - 保证某个类在程序运行过程中最多只有一个实例，也就是对象实例只占用一份内存资源
          - 由于单例模式中没有抽象层，因此单例很难进行类的扩展
          - via: https://www.nowcoder.com/questionTerminal/3b8718d3aaea4722ae34f5d38a771047
      - 原型 Prototype
        collapsed:: true
        - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
          collapsed:: true
          - ![https://user-images.githubusercontent.com/57313137/175233789-633f8fb7-a890-4d70-a03c-200857b3d91e.png](../assets/book/秒懂设计模式/175233789-633f8fb7-a890-4d70-a03c-200857b3d91e.png)
        - ((634cd41e-7603-46d6-bf66-1c3e3fab1d9f))
          collapsed:: true
          - 用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象
            collapsed:: true
            - 从一个对象再创建另外一个可定制的对象，而且不需知道任何创建的细节
          - UML
            collapsed:: true
            - ![image.png](../assets/book/大话设计模式/image_1648052972278_0.png)
            -
      - 工厂 (Simple)Factory
        id:: 9dd916a4-d1e3-40c7-82ae-834d035a8d54
        collapsed:: true
        - 到底要实例化谁，将来会不会增加实例化的对象，这是很容易变化的地方.
        - 用一个单独的类来做这个创造实例的过程，这就是**工厂**
        - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
          collapsed:: true
          - ![https://user-images.githubusercontent.com/57313137/175233865-5cf5e367-e980-4528-9b81-582f2196849a.png](../assets/book/秒懂设计模式/175233865-5cf5e367-e980-4528-9b81-582f2196849a.png)
        - ((634cd41e-7603-46d6-bf66-1c3e3fab1d9f))
          collapsed:: true
          - 计算器
            collapsed:: true
            - 扩容: 增加相应的运算子类 + 分支工厂
            - ![image.png](../assets/book/大话设计模式/image_1648016749205_0.png)
          - 定义一个用于创建对象的接口，让子类决定实例化哪一个类。工厂方法使一个类的实例化延迟到其子类。
          - UML
            collapsed:: true
            - ![image.png](../assets/book/大话设计模式/image_1648052051088_0.png)
            - 既然这个工厂类与分支耦合，那么我就对它下手，根据依赖倒转原则，我们把工厂类抽象出一个接口，这个接口只有一个方法，就是创建抽象产品的工厂方法。然后，所有的要生产具体类的工厂，就去实现这个接口，这样，一个简单工厂模式的工厂类，变成了一个工厂抽象接口和多个具体生成对象的工厂，于是我们要增加‘求M数的N次方’的功能时，就不需要更改原有的工厂类了，只需要增加此功能的运算类和相应的工厂类就可以了
        - ((634cf9cc-6b4f-48b7-9214-a8ad936a9672))
          collapsed:: true
          - 客户端, 实例化解耦
          - 抽象工厂可以通过堕胎创造更多的产品
      - 抽象工厂 Abstract Factory
        id:: 16c41589-8029-436b-be87-c27856742f77
        collapsed:: true
        - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
          collapsed:: true
          - ![https://user-images.githubusercontent.com/57313137/175233928-d2df1cf6-28f9-42d0-bf35-df28b4d9ade9.png](../assets/book/秒懂设计模式/175233928-d2df1cf6-28f9-42d0-bf35-df28b4d9ade9.png)
        - ((634cf9cc-6b4f-48b7-9214-a8ad936a9672))
          collapsed:: true
          - 基于**工厂族系划分**, 使布局, 产品相对固定(接口固定)
          - 族系之间通过 ((ef348d29-4248-4e81-8c6d-5c1e703883f8)) 可以创造更多的产品
      - 建造者 Builder
        collapsed:: true
        - 将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示
        - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
          collapsed:: true
          - ![https://user-images.githubusercontent.com/57313137/](../assets/book/秒懂设计模式/175233997-ee7c1f58-b2a5-48ab-8ec2-baf36f384ca2.png)
    - 结构 (s, 7)
      description:: 如何将对象和类组装成较大的结构; 并同时保持结构的灵活和高效
      - 门面 Facade
        collapsed:: true
        id:: 236dd848-1377-4002-a120-a5652b5b6ad8
        - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
          - ![image](../assets/book/秒懂设计模式/175234891-a4ad58d9-320f-4c0e-82c6-8a62dec228f9.png)
        - 为子系统中的一组接口提供一个一致的界面，此模式定义了一个高层接口，这个接口使得这一子系统更加容易使用
        - UML
          - ![image.png](../assets/book/大话设计模式/image_1648174605031_0.png)
        - When
          - ![image.png](../assets/book/大话设计模式/image_1648175008312_0.png)
          - 初期阶段
            - 有意识的将不同的两个层分离
            - 三层架构
              - 考虑在数据访问层和业务逻辑层、业务逻辑层和表示层的层与层之间建立外观Facade，这样可以为复杂的子系统提供一个简单的接口，使得耦合大大降低。
          - 开发阶段
            - 增加外观Facade可以提供一个简单的接口，减少 不断增多的小类与外部调用者 之间的依赖
          - 维护一个遗留的大型系统
            - 你可以为新系统开发一个外观Facade类，来提供设计粗糙或高度复杂的遗留代码的比较清晰简单的接口，让新系统与Facade对象交互，Facade与遗留代码交互所有复杂的工作。
      - 组合 Composite
        collapsed:: true
        - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
          - ![image](../assets/book/秒懂设计模式/175235009-9f97295b-ae3d-408b-8f93-768f8d639af4.png)
        - ((634cf9cc-6b4f-48b7-9214-a8ad936a9672))
          - 接口泛化所有的节点类, 使得整体部分达到统一 (由根到叶可完美实现树形结构)
      - Decorator / Wrapper / 装饰者 / 装饰器
        id:: d90919b5-0ba4-4c0b-aff7-8f376fa39ee9
        collapsed:: true
        - Inheritance(继承)
          - 问题
            - 继承是**静态**的
              - 你无法在运行时更改已有对象的行为, 只能使用由不同子类创建的对象来替代当前的整个对象。
            - **子类只能有一个父类**
              - 大部分编程语言不允许一个类同时继承多个类的行为。
          - *Inheritance(继承)* #vs *Aggregation(聚合)*
            - ![image.png](../assets/pattern/image_1665997671782_0.png)
            - 聚合: 对象 $A$ 包含对象 $B$; $B$ 可以独立于 $A$ 存在
            - 组合: 对象 $A$ 由对象 $B$ 构成; $A$ 负责管理 $B$ 的生命周期。$B$ 无法独立于 $A$ 存在
        - > 一个对象可以使用多个类的行为, 包含多个指向其他对象的引用, 并将各种工作委派给引用对象。 聚合 （或组合） 组合是许多设计模式背后的关键原则 （包括装饰在内）
        - Why
          - 把类中的装饰功能从类中搬移去除，简化原有的类
            - 有效地把类的核心职责和装饰功能区分开
            - 去除相关类中重复的装饰逻辑
        - 动态地给一个对象添加一些额外的职责
          - 就增加功能来说，装饰模式比生成子类更为灵活
        - 装饰模式把每个要装饰的功能放在单独的类中，并让这个类包装它所要装饰的对象
          - 当需要执行特殊行为时，客户代码就可以在运行时根据需要有选择地、按顺序地使用装饰功能包装对象了
        - #+BEGIN_WARNING
          装饰模式的装饰顺序很重要
          #+END_WARNING
        - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
          - ![image](../assets/book/秒懂设计模式/175235131-1af28001-1de6-4aed-98f5-0cea18ca9303.png)
          - ![image.png](../assets/book/大话设计模式/image_1648028747546_0.png)
            - `Component`: 定义一个对象接口，可以给这些对象动态地添加职责
            - `ConcreteComponent`: 定义了一个具体的对象，也可以给这个对象添加一些职责
            - `Decorator`: 装饰抽象类，继承了 `Component`，从外类来扩展 `Component` 类的功能，
              - `Component` 无需知道 `Decorator` 的存在的
            - `ConcreteDecorator`: 具体的装饰对象，起到给Component添加职责的功能
        - ((634cd41e-7603-46d6-bf66-1c3e3fab1d9f))
          -
      - 适配器 Adopter
        collapsed:: true
        id:: 86a41cdb-f7d3-4159-b616-0780d68c6a80
        - 对象适配器
          - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
            - ![image](../assets/book/秒懂设计模式/175235443-a2ff43e6-dfb1-4aec-bdac-beab83aac388.png)
        - 类适配器
          - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
            - ![image](../assets/book/秒懂设计模式/175235551-6418cf72-a9f3-41b0-a6c3-1bd73bb926d6.png)
        - ((634cf9cc-6b4f-48b7-9214-a8ad936a9672))
          - 不修改代码就可以满足不同的需求
      - 享元 Flyweight
        collapsed:: true
        - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
          - ![image](../assets/book/秒懂设计模式/175245048-9bc50001-9269-49e0-a071-eb0b9ef9f3c3.png){:height 278, :width 623}
      - 代理 Proxy
        description:: "当你希望在无需修改客户代码的前提下于已有类的对象上增加额外行为时， 该模式是无可替代的"
        collapsed:: true
        - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
          collapsed:: true
          - ![image.png](../assets/pattern/image_1666183902181_0.png)
          - collapsed:: true
            #+BEGIN_IMPORTANT
            从 **代理 (Proxy)** 到 **服务对象/业务(Service)**, 两者的关系是**聚合**, 我自己写代码生成的 Diagrams 是 **组合**, ~~但参考书本, 用到的是**关联**~~
            #+END_IMPORTANT
            - ![image](../assets/book/秒懂设计模式/186604309-8d5a34bb-dea2-4aff-b33c-c0f7d012f5f6.png)
            - ![image.png](../assets/book/大话设计模式/image_1648039927679_0.png)
            - `Subject` 类，定义了 `RealSubject` 和 `Proxy` 的共用接口，这样就在任何使用 `RealSubject` 的地方都可以使用 `Proxy`
        - ((634cd41e-7603-46d6-bf66-1c3e3fab1d9f))
          id:: 634ff438-7463-4dd2-a58c-42beb9005794
          collapsed:: true
          - 远程代理 -> **==本地执行远程服务==**
            - 为一个对象在不同的地址空间提供局部代表
            - 隐藏一个对象存在于不同地址空间的事实
          - 虚拟代理 -> **==延迟初始化==**
            - 根据需要创建开销很大的对象
            - 通过它来存放实例化需要很长时间的真实对象
          - 安全代理 -> **==访问控制==**
            - 用来控制真实对象访问时的权限
              - 一般用于对象应该有不同的访问权限的时候
            - Use Case: [[Spring]] AOP, Apache Shiro...
          - 日志记录代理 -> **==记录日志请求==**
            - 适用于当你需要保存对于服务对象的请求历史记录时
          - 缓存代理 -> **==缓存请求结果==**
            - **适用于需要缓存客户请求结果并对缓存生命周期进行管理时，特别是当返回结果的体积非常大时**
          - 智能指引
            - 当调用真实的对象时，代理处理另外一些事
            - 可在没有客户端使用某个重量级对象时立即销毁该对象
          - CopyOnWriteList
          - 防火墙
          - [[java]] Library
            - [ java.lang.reflect.Proxy ](http://docs.oracle.com/javase/8/docs/api/java/lang/reflect/Proxy.html)
            - [ java.rmi.\* ](http://docs.oracle.com/javase/8/docs/api/java/rmi/package-summary.html)
            - [ javax.ejb.EJB ](http://docs.oracle.com/javaee/7/api/javax/ejb/EJB.html) （[查看评论](http://stackoverflow.com/questions/25514361/when-using-ejb-does-each-managed-bean-get-its-own-ejb-instance)）
            - [ javax.inject.Inject ](http://docs.oracle.com/javaee/7/api/javax/inject/Inject.html) （[查看评论](http://stackoverflow.com/questions/29651008/field-getobj-returns-all-nulls-on-injected-cdi-managed-beans-while-manually-i/29672591#29672591)）
            - [ javax.persistence.PersistenceContext ](http://docs.oracle.com/javaee/7/api/javax/persistence/PersistenceContext.html)
        - 优缺点
          - ✔ 你可以在客户端毫无察觉的情况下控制服务对象。
          - ✔ 如果客户端对服务对象的生命周期没有特殊要求， 你可以对生命周期进行管理。
          - ✔ 即使服务对象还未准备好或不存在， 代理也可以正常工作。
          - ✔ *开闭原则*。 你可以在不对服务或客户端做出修改的情况下创建新代理。
          - ✖ 代码可能会变得复杂， 因为需要新建许多类。
          - ✖ 服务响应可能会延迟。
        - #vs ((86a41cdb-f7d3-4159-b616-0780d68c6a80)) & ((d90919b5-0ba4-4c0b-aff7-8f376fa39ee9))
          - 都提供接口
            - 代理模式提供相同接口
            - ((86a41cdb-f7d3-4159-b616-0780d68c6a80)) 提供不同的接口;
            - ((d90919b5-0ba4-4c0b-aff7-8f376fa39ee9)) 提供加强接口
        - #vs ((236dd848-1377-4002-a120-a5652b5b6ad8))
          - 两者都缓存了一个实体并进行初始化
          - 代理与其服务对象遵循同一接口， 使得自己和服务对象可以互换
        - #vs ((d90919b5-0ba4-4c0b-aff7-8f376fa39ee9))
          - 都基于 **组合模式**
          - 代理模式自行管理服务周期
          - 装饰的生成由客户端控制
        - Refs
          - [论坛权限控制设计：在一个论坛中已注册用户和游客的权限不同，已__牛客网](https://www.nowcoder.com/questionTerminal/f7981f3bbfd445ed8a15c0f7f929b924)
          - [Proxy](https://refactoring.guru/design-patterns/proxy); [代理设计模式](https://refactoringguru.cn/design-patterns/proxy)
      - 桥接 Bridge
        collapsed:: true
        - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
          - ![image](../assets/book/秒懂设计模式/175248031-19a8ae46-acef-4403-bc1a-1f2f2fcbb3d2.png)
        - ((634cf9cc-6b4f-48b7-9214-a8ad936a9672))
          - 抽象与实现解耦, 系统更加松散灵活
    - 行为 Behavior (v, 11)
      description:: 对象间的高效沟通和职责委派
      - 模板 Template
        collapsed:: true
        - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
          collapsed:: true
          - ![image](../assets/book/秒懂设计模式/186604650-97de9936-245e-4836-a677-65d565db5f70.png)
        - 定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。
          collapsed:: true
          - 子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。
        - UML
          collapsed:: true
          - ![image.png](../assets/book/大话设计模式/image_1648173042430_0.png)
        - #Why
          collapsed:: true
          - 模板方法模式是通过把不变行为搬移到超类，去除子类中的重复代码来体现它的优势
      - 迭代器 Iterator
        collapsed:: true
        - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
          collapsed:: true
          - ![album_temp_1661414673](../assets/book/秒懂设计模式/186610708-0c49cd74-8a09-4547-80a8-0ad776e06438.PNG)
      - 责任链 Chain Of Responsibility
        collapsed:: true
        id:: a36469b8-4cb6-4bf2-b158-6fce461dd255
        - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
          collapsed:: true
          - ![album_temp_1661414630](../assets/book/秒懂设计模式/186610903-4a50bb97-ac41-4973-9bd8-6d5b7e589840.PNG)
      - 策略 Strategy
        id:: cdf6366c-cfa6-4774-b3c7-148768daad74
        collapsed:: true
        - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
          collapsed:: true
          - ![epub_39201628_126](../assets/book/秒懂设计模式/186605879-43519237-4081-49c4-9886-64076d114e0c.jpg)
        - 策略模式定义了算法家族，分别封装起来，让它们之间可以互相替换，此模式让算法的变化，不会影响到使用算法的客户
        - 算法本身只是一种策略，最重要的是这些算法是随时都可能互相替换的，这就是变化点，而封装变化点是我们面向对象的一种很重要的思维方式
        - ((634cd41e-7603-46d6-bf66-1c3e3fab1d9f))
          collapsed:: true
          - ![image.png](../assets/book/大话设计模式/image_1648016980829_0.png)
        - ((634cf9cc-6b4f-48b7-9214-a8ad936a9672))
          collapsed:: true
          - 策略和系统环境解耦, 对策略的抽象拼接, 可塑系统行为
          - 算法分离, 系统更加灵活
      - 状态 State
        collapsed:: true
        - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
          collapsed:: true
          - ![image](../assets/book/秒懂设计模式/175469152-aaa1a25f-df13-4ef8-aab0-63a3cb5ed34e.png)
      - 备忘录 Mementor
        collapsed:: true
        - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
          collapsed:: true
          - ![album_temp_1661414704](../assets/book/秒懂设计模式/186610847-b3a47363-500a-4a32-9748-879236ae5a18.PNG)
      - 中介 Mediator
        collapsed:: true
        - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
          collapsed:: true
          - ![album_temp_1661414717](../assets/book/秒懂设计模式/186610802-fae9c0fa-86c2-455d-909e-95b05614287d.PNG)
      - 命令 Command
        id:: 63959dcc-1bd8-4fc7-b337-6123a2911057
        - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
          - ![image](../assets/book/秒懂设计模式/175478602-c225d26a-e4dc-441f-9008-0fe55b1d10ea.png)
      - 访问者 Visitor
        collapsed:: true
        - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
          collapsed:: true
          - ![image](../assets/book/秒懂设计模式/175480918-bd35048b-1029-460c-a3bb-9fec9e6db31f.png)
      - 观察者 Observer
        collapsed:: true
        id:: e0e4c4da-0a0d-41b3-b834-1dcd3c1344d9
        - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
          collapsed:: true
          - ![image](../assets/book/秒懂设计模式/175493320-8518aeec-3654-4d10-be27-a858ee2907a1.png)
        - ![image.png](../assets/book/大话设计模式/image_1648181263199_0.png){:height 435, :width 616}
        - java 委托不会写...
        - ((634cf9cc-6b4f-48b7-9214-a8ad936a9672))
          collapsed:: true
          - 以多态化弱化目标主题与观察者强指代;标准化接口, 主客反转
          - 效率提高
      - 解释器 Interpreter
        collapsed:: true
        - ((634cd4bc-9950-4d3c-8057-466be4c059e3))
          collapsed:: true
          - ![image](../assets/book/秒懂设计模式/175497324-bd4c8dbc-e7d4-406c-8993-b4408ee29a19.png)
    -
    - Tips
      collapsed:: true
      - ((9dd916a4-d1e3-40c7-82ae-834d035a8d54)) #vs ((cdf6366c-cfa6-4774-b3c7-148768daad74))
        collapsed:: true
        - [策略模式和工厂模式的区别 - 大CC - 博客园](https://www.cnblogs.com/me115/p/3790615.html)
      - Simple Factory #vs ((9dd916a4-d1e3-40c7-82ae-834d035a8d54)) #vs ((16c41589-8029-436b-be87-c27856742f77))
        - **Simple Factory**
          - 工厂类中包含了必要的逻辑判断，根据客户端的选择条件动态实例化相关的类，对于客户端来说，去除了与具体产品的依赖
            collapsed:: true
            - 修改运算工厂类的方法里加的分支条件的可不是好办法 == 扩展开放+修改开放 (违背开闭原则)
        - **Factory**
          - 不必修改工厂类了, 直接继承一个子类顺势写.
          - 工厂方法使用了多态性, 克服了简单工厂违背开放-封闭原则的缺点, 又保持了封装对象创建过程的优点
          - 缺点是由于每加一个产品，就需要加一个产品工厂的类，增加了额外的开发量
        - 当客户获取产品时，工厂模式作为获取产品的接口
          - 简单工厂模式：由接口直接负责获取产品
          - 工厂方法模式：客户必须清楚地指出想获取哪种产品；由接口的子类负责获取产品
          - 抽象工厂模式：客户不知道其想获取哪种产品；由接口中判断调用哪个子类，通过子类获取产品
        - Refs
          - https://www.nowcoder.com/questionTerminal/67b5b9bfe72d49ddb1712558aeeb8f63
      - [策略模式 VS 状态模式 | 菜鸟教程](https://www.runoob.com/w3cnote/state-vs-strategy.html)
      - All
        collapsed:: true
        - ![image.png](../assets/book/大话设计模式/image_1648052685023_0.png)
-
- [[Question]]
  - 如果在更改一个对象的时候，需要同时连带改变其他的对象，而且不知道究竟应该有多少对象需要被连带改变，应该使用何种设计模式 {{cloze 观察者模式}}
    - ((e0e4c4da-0a0d-41b3-b834-1dcd3c1344d9)) #vs ((a36469b8-4cb6-4bf2-b158-6fce461dd255))
-
- TODOs List
  - {{embed ((634ff438-7463-4dd2-a58c-42beb9005794))}}
  - 外观模式
    - [下列描述中，哪些是外观模式的特点（   _爱奇艺笔试题_牛客网](https://www.nowcoder.com/questionTerminal/19f6568a3fb749bbb8e29d0f7da3af6b)
    - [假设一个电源总开关可以控制四盏灯、一个风扇、一台空调和一台电__牛客网](https://www.nowcoder.com/questionTerminal/4f0db171e8a841e8b0a2c5f9b6707eb9)
  - 享元模式
    - [共享网络设备模拟：很多网络设备都是支持共享的，如交换机、集线__牛客网](https://www.nowcoder.com/questionTerminal/23dea24378aa4b78b29e1db8d08fdd3d)
  - 访问者模式
    - [购物车设计：顾客在超市中将选择的商品，如苹果、图书等放在购物__牛客网](https://www.nowcoder.com/questionTerminal/c2089761ca49436ebdd0cd347511275a)
    - [某高校奖励审批系统可以实现教师奖励和学生奖励的审批(Awar__牛客网](https://www.nowcoder.com/questionTerminal/faa18a74f99e42299cda7c81ad024821)
  - 装饰者模式
    - [系统中的文本显示类（TextView）和图片显示类（Pict__牛客网](https://www.nowcoder.com/questionTerminal/fa78ee64be454ba58c0d54b55788da47)
  - 行为型模式分为类行为模式和对象行为模式，前者采用继承机制来在类间分派行为，后者采用组合或聚合在对象间分配行为。由于组合关系或聚合关系比继承关系耦合度低，满足“合成复用原则”，所以对象行为模式比类行为模式具有更大的灵活性。via: https://www.nowcoder.com/questionTerminal/ec3bcc890d5e4a26b7cbbf67026166f1
-
- Refs
  - 大话设计模式
    alias:: book/大话设计模式
    tags:: #[[software/pattern]]
    author:: 程杰
    publisher:: 清华大学出版社
    published-date:: 20071201
    source:: [大话设计模式 (豆瓣)](https://book.douban.com/subject/2334288/)
  - 秒懂设计模式
    alias:: book/秒懂设计模式
    tags:: #[[software/pattern]]
    author:: 刘韬
    publisher::  人民邮电出版社
    published-date:: 20201100
    source:: [秒懂设计模式 (豆瓣)](https://book.douban.com/subject/35525040/); [demo/tasks/design-pattern/src](https://github.com/bGZo/demo/tree/main/tasks/design-pattern/src)
  -
  - [52 Design Principles](https://rpdc.xiaohongshu.com/52-design-principles)
  - [Refactoring and Design Patterns](https://refactoring.guru/); [免费在线学习代码重构和设计模式](https://refactoringguru.cn/)
  -
  - [23种设计模式的总结与思考 - rome753 - 博客园](https://www.cnblogs.com/rome753/p/16495597.html)
    - [Awesome-Android-Notebook/Android开发者必须掌握的设计模式.md at master · JsonChao/Awesome-Android-Notebook](https://github.com/JsonChao/Awesome-Android-Notebook/blob/master/notes/Android%E5%BC%80%E5%8F%91%E8%80%85%E5%BF%85%E9%A1%BB%E6%8E%8C%E6%8F%A1%E7%9A%84%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F.md)
    - [JAVA设计模式总结之23种设计模式 - pony1223 - 博客园](https://www.cnblogs.com/pony1223/p/7608955.html)
    - [Java设计模式汇总，超详细！ - 知乎](https://zhuanlan.zhihu.com/p/136592911)
  -
  - [设计模式 | 菜鸟教程](https://www.runoob.com/design-pattern/design-pattern-tutorial.html)
  - [單一功能原則 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/%E5%8D%95%E4%B8%80%E5%8A%9F%E8%83%BD%E5%8E%9F%E5%88%99)
  - [開閉原則 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/%E5%BC%80%E9%97%AD%E5%8E%9F%E5%88%99)
  - [依赖反转原则 - 维基百科，自由的百科全书](https://zh.wikipedia.org/zh-hans/%E4%BE%9D%E8%B5%96%E5%8F%8D%E8%BD%AC%E5%8E%9F%E5%88%99)
  - [策略模式 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/%E7%AD%96%E7%95%A5%E6%A8%A1%E5%BC%8F)
  - [修飾模式 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/%E4%BF%AE%E9%A5%B0%E6%A8%A1%E5%BC%8F)
  - [代理模式 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/%E4%BB%A3%E7%90%86%E6%A8%A1%E5%BC%8F)
  - [工厂方法 - 维基百科，自由的百科全书](https://zh.wikipedia.org/zh-hans/%E5%B7%A5%E5%8E%82%E6%96%B9%E6%B3%95)
  - [原型模式 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/%E5%8E%9F%E5%9E%8B%E6%A8%A1%E5%BC%8F)
  - [模板方法 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/%E6%A8%A1%E6%9D%BF%E6%96%B9%E6%B3%95)
  - [观察者模式 - 维基百科，自由的百科全书](https://zh.wikipedia.org/zh-cn/%E8%A7%82%E5%AF%9F%E8%80%85%E6%A8%A1%E5%BC%8F)
-