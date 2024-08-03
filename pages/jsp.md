icon:: 📄
also:: [[java-server-pages]] 
created:: [[20240802]]
description:: 
wikipedia:: https://en.wikipedia.org/wiki/Jakarta_Server_Pages

- ## Why
- ## How
- ## What
  - collapsed:: true
    >从架构上来说，JSP 可以被视为Jakarta [[servlet]] 的高级抽象。 JSP 在运行时被翻译成 servlet，因此 JSP 是一个 Servlet；每个 JSP servlet 都会被缓存并重新使用，直到原始 JSP 被修改。
    - https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/JSP_Model_2.svg/220px-JSP_Model_2.svg.png
  - 标准: https://jcp.org/en/jsr/detail?id=245
  - Template enginee alternatives
    - Adobe ColdFusion
      logseq.order-list-type:: number
    - Lucee
      logseq.order-list-type:: number
    - FreeMarker
      logseq.order-list-type:: number
    - JHTML
      logseq.order-list-type:: number
    - Thymeleaf
      logseq.order-list-type:: number
  - 语法
    - 内置对象 / 保留字(9)
      collapsed:: true
      - ![image.png](../assets/imu/java/image_1662376901724_0.png)
    - 域对象(4)
      collapsed:: true
      - 都能通过以下 3 个方法，对属性进行保存、获取和移除操作
        - | 返回值类型  | 方法                                  | 作用         |
          | ------ | ----------------------------------- | ---------- |
          | void   | setAttribute(String name, Object o) | 将属性保存到域对象中 |
          | Object | getAttribute(String name)           | 获取域对象中的属性值 |
          | void   | removeAttribute(String name)        | 将属性从域对象中移除 |
      - 作用域各不相同
        - ![image.png](../assets/imu/java/image_1662377086775_0.png)
    - JSP 标准标签库 (JSTL)
      collapsed:: true
      - 核心标签
        - ![image.png](../assets/imu/java/image_1662385290406_0.png)
      - 格式化标签, 格式化并输出文本、日期、时间、数字
        - ![image.png](../assets/imu/java/image_1662385384978_0.png)
      - SQL, 与关系型数据库（Oracle，MySQL，SQL Server等等）进行交互的标签
        - ![image.png](../assets/imu/java/image_1662385418119_0.png)
      - JSTL函数
        - ![image.png](../assets/imu/java/image_1662385498017_0.png)
- ## Namespace
  - {{namespace java-server-pages}}
- ## ↩ Reference
  - [JSP 教程 | 菜鸟教程](https://www.runoob.com/jsp/jsp-tutorial.html)
  - [Servlet学习（五）使用Servlet过滤器实现登录权限校验-附源码下载_wangxin1248的博客-CSDN博客](https://blog.csdn.net/icarus_wang/article/details/51422364)
  - [Java多线程的实现和各自优缺点以及使用场景【补全上篇多线程文章的不详细】_Attacking_Ape的博客-CSDN博客](https://blog.csdn.net/Attacking_Ape/article/details/107183736)
  - [java+servlet+jsp查询所有信息及查询一条记录_z_victoria123的博客-CSDN博客](https://blog.csdn.net/z_victoria123/article/details/79884638)
  - [Java EE复习（一）_Vofhlwwwx的博客-CSDN博客](https://blog.csdn.net/goodgds/article/details/106303597)
  - [JavaEE简答题 - 百度文库](https://wenku.baidu.com/view/38faf61eed06eff9aef8941ea76e58fafab04534.html)
  - [【Java】- Servlet管理机制 - 一梦三千年 - 博客园](https://www.cnblogs.com/tar8087/p/14456647.html)
  - [关于JAVA的分页查询操作技术_alerx的博客-CSDN博客](https://blog.csdn.net/alerx/article/details/985699)
    - [分页公式以及分页导航栏总结_fxsjy的博客-CSDN博客](https://blog.csdn.net/fxsjy/article/details/772457)
  - 说明Java的包机制，并说明类成员在各种访问控制符修饰下在相应包、子类继承关系中的访问范围。
    collapsed:: true
    - package是java 中包机制。包机制的作用是为了方便程序的管理。
      不同功能的类分别存放在不同的包下。    
      package是一个关键字，后面加包名。
      一般都采用公司域名倒序的方式
    - | **访问修饰符** |
      | --- | --- | --- |
      | **名称** | **说明** | **备注** |
      | public | 可以被所有类访问（使用） | public类必须定义在和类名相同的同名文件中 |
      | protected| 可以被同一个包中的类访问（使用）可以被所有子类访问 | 默认的访问权限，可以省略此关键字，可以定义在和public类的同一个文件中, 子类没有在同一包中也可以访问 |
      | private | 修饰内部类,只能够被当前类的方法访问 |     |
      via: [java的访问控制（包、访问修饰符、修饰符） - 一念了了 - 博客园](https://www.cnblogs.com/liaoliao/p/5009123.html)
  - 说明JSP与Servlet的联系及各自适用的情况和优缺点
    collapsed:: true
    - JSP是Servlet技术的扩展，本质上就是Servlet的简易方式。JSP编译后是“类servlet”
    - Servlet的应用逻辑是在Java文件中，并且完全从表示层中的HTML里分离开来
      JSP的情况是Java和HTML可以组合成一个扩展名为.jsp的文件
      JSP侧重于视图，Servlet主要用于控制逻辑
    - Servlet在Java代码中通过HttpServletResponse对象动态输出HTML内容
      JSP在静态HTML内容中嵌入Java代码，Java代码被动态执行后生成HTML内容。
      Servlet能够很好地组织业务逻辑代码，但是在Java源文件中通过字符串拼接的方式生成动态HTML内容会导致代码维护困难、可读性差
      JSP虽然规避了Servlet在生成HTML内容方面的劣势，但是在HTML中混入大量、复杂的业务逻辑同样也是不可取的。
    - via: [jsp与servlet的区别与联系_癸酉金鸡的博客-CSDN博客_jsp和servlet区别和联系](https://blog.csdn.net/chinasi2012/article/details/87428361)
  - 说明Java EE组件-容器的编程思想，并画图说明servlet运行管理机制。
    collapsed:: true
    - JavaEE应用的基本单元是JavaEE组件，所有的javaEE组件都运行在特定的环境中。
    - 组件的运行环境被称为容器。
    - <img title="" src="https://gimg2.baidu.com/image_search/src=http:%2F%2Fcdn.bianchengquan.com%2F11b921ef080f7736089c757404650e40%2Fblog%2F5fa7c0de7b4fd.png&refer=http:%2F%2Fcdn.bianchengquan.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1662881914&t=e006e0f91748b406e7b36efe0db3cafc" alt="" width="622">
  - session对象的作用是什么? 它在什么范围内共享信息?
    collapsed:: true
    - 从客户端浏览器连接服务器开始，到客户端与服务器断开为止，这个过程就是一次会话。
    - session通常用于跟踪用户的会话信息，如判断用户是否登陆系统，或者在购物车应用中，用于跟踪用户购买的商品等。
    - session范围内的属性可以在多个页面的跳转之间共享用户会话状态相关的信息。一旦关闭浏览器，即session结束，session范围内的属性将全部丢失
    - via: [JSP的九个内置对象之session对象_Haobon的博客-CSDN博客](https://blog.csdn.net/qq_34342083/article/details/54237342)
  - 以购物车为例，说明如何采用HttpSession实现
    collapsed:: true
    - **HttpSession**：会话作用域对象。用于解决cookie存储类型单一，存储数量少的问题。
    - 当用户在购物页面index.html点击加入购物车时，商品参数会通过超链接发送给OneServlet，OneServlet通过request拿到商品参数并为用户建立session，通过goodsName的真实值确定商品数量，当前购物车此商品==null则令其为数量1，当前购物车此商品！=null则令其数量+1
    - 当用户点击购物页面的"查看购物车"时，浏览器将通过超链接发送到TwoServlet。TwoServlet通过request拿到session，对其中元素进行遍历并输出。
    - via: [HttpSession实例——购物车功能_进击小高的博客-CSDN博客](https://blog.csdn.net/Luna_A/article/details/106005142)
  - 如何用JSP、SERVLET、JAVABEAN/EJB实现MVC?
    collapsed:: true
    - via: [使用JSP，Servlet，JavaBean实现MVC模式_橘子夏的蓝的博客-CSDN博客_javabean+servlet+jsp构建mvc模式](https://blog.csdn.net/m0_50897734/article/details/109458596)
      - 搜到的都是代码, 怎么用言语表述...
  - 介绍一下数据库连接池的优点和原理？
    collapsed:: true
    - 连接池用于创建和管理数据库连接的缓冲池技术，缓冲池中的连接可以被任何需要他们的线程使用。当一个线程需要用JDBC对一个数据库操作时，将从池中请求一个连接。当这个连接使用完毕后，将返回到连接池中，等待为其他的线程服务。
    - 主要优点
      - 减少连接创建时间。连接池中的连接是已准备好的、可重复使用的，获取后可以直接访问数据库，因此减少了连接创建的次数和时间。
      - 简化的编程模式。当使用连接池时，每一个单独的线程能够像创建一个自己的JDBC连接一样操作，允许用户直接使用JDBC编程技术。
      - 控制资源的使用。如果不使用连接池，每次访问数据库都需要创建一个连接，这样系统的稳定性受系统连接需求影响很大，很容易产生资源浪费和高负载异常。连接池能够使性能最大化，将资源利用控制在一定的水平之下。连接池能控制池中的连接数量，增强了系统在大量用户应用时的稳定性。
    - 工作原理
      - 连接池技术的核心思想是连接复用，通过建立一个数据库连接池以及一套连接使用、分配和管理策略，使得该连接池中的连接可以得到高效、安全的复用，避免了数据库连接频繁建立、关闭的开销。
      - 第一、连接池的建立。一般在系统初始化时，连接池会根据系统配置建立，并在池中创建了几个连接对象，以便使用时能从连接池中获龋连接池中的连接不能随意创建和关闭，这样避免了连接随意建立和关闭造成的系统开销。Java中提供了很多容器类可以方便的构建连接池，例如Vector、Stack等。
      - 第二、连接池的管理。连接池管理策略是连接池机制的核心，连接池内连接的分配和释放对系统的性能有很大的影响。其管理策略是：
        当客户请求数据库连接时，首先查看连接池中是否有空闲连接，如果存在空闲连接，则将连接分配给客户使用；如果没有空闲连接，则查看当前所开的连接数是否已经达到最大连接数，如果没达到就重新创建一个连接给请求的客户；如果达到就按设定的最大等待时间进行等待，如果超出最大等待时间，则抛出异常给客户。
        当客户释放数据库连接时，先判断该连接的引用次数是否超过了规定值，如果超过就从连接池中删除该连接，否则保留为其他客户服务。
        该策略保证了数据库连接的有效复用，避免频繁的建立、释放连接所带来的系统资源开销。
      - 第三、连接池的关闭。当应用程序退出时，关闭连接池中所有的连接，释放连接池相关的资源，该过程正好与创建相反。连接池的工作原理主要由三部分组成，分别为连接池的建立、连接池中连接的使用管理、连接池的关闭。
    - via: [数据库连接池是什么？工作原理和优点是？ - 菜鸟学苑](https://www.cainiaoxueyuan.com/sjk/10713.html)
  - 请描述forward和redirect的区别。
    collapsed:: true
    - 请求方不同
      redirect：客户端发起的请求
      forward：服务端发起的请求
    - 浏览器地址表现不同
      redirect：浏览器地址显示被请求的
      urlforward：浏览器地址不显示被请求的url
    - 参数传递不同
      redirect：重新开始一个request,原页面的request生命周期结束。
      forward：forward另一个连接的时候。request变量是在其生命周期内的。另一个页面也可以使用，其实质是把目标地址include。
    - 底层运作不同
      redirect：发送的请求信息又回送给客户机，让客户机再转发到另一个资源上，需要在服务器和客户机之间增加一次通信。
      forward：服务器端直接找到目标，并include过来。
    - 定义不同
      直接转发方式（Forward）：客户端和浏览器只发出一次请求，Servlet、HTML、JSP或其它信息资源，由第二个信息资源响应该请求，在请求对象request中，保存的对象对于每个信息资源是共享的。
      间接转发方式（Redirect）实际是两次HTTP请求，服务器端在响应第一次请求的时候，让浏览器再向另外一个URL发出请求，从而达到转发的目的。
    - via: [forward和redirect的区别_百度知道](https://zhidao.baidu.com/question/1574962284977388260.html)
  - 请描述EJB和JAVA BEAN的区别。
    collapsed:: true
    - Java Bean 是可复用的组件，对Java Bean并没有严格的规范，理论上讲，任何一个Java类都可以是一个Bean。但通常情况下，由于Java Bean是被容器所创建（如Tomcat)的，所以Java Bean应具有一个无参的构造器，另外，通常Java Bean还要实现Serializable接口用于实现Bean的持久性。Java Bean实际上相当于微软COM模型中的本地进程内COM组件，它是不能被跨进程访问的。
    - Enterprise Java Bean 相当于DCOM，即分布式组件。它是基于Java的远程方法调用（RMI）技术的，所以EJB可以被远程访问（跨进程、跨计算机）。但EJB必须被布署在诸如Webspere、WebLogic这样的容器中，EJB客户从不直接访问真正的EJB组件，而是通过其容器访问。EJB容器是EJB组件的代理，EJB组件由容器所创建和管理。客户通过容器来访问真正的EJB组件。
    - via: [EJB与JAVA BEAN的区别？_变强不变秃的博客-CSDN博客](https://blog.csdn.net/w669600/article/details/83416186)
-