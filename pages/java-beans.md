icon:: ☕
also::  
created:: [[20240805]]
description:: 将一个或多个对象封装在单个标准化对象中的类
tags:: #java01
wikipedia:: https://en.wikipedia.org/wiki/JavaBeans

- #+BEGIN_NOTE
  Not Jakarta Enterprise Beans ([[ejb]])
  #+END_NOTE
- ## Why
  -
- ## How
  -
- ## What
  - Java Bean
    collapsed:: true
    - 约定 (conventions)
      - 公共无参构造函数，方便框架实例化；
        logseq.order-list-type:: number
      - 按标准命名方式提供 getter 和 setter 方法，允许框架自动检查和更新 Bean 状态；
        logseq.order-list-type:: number
      - 类可序列化 (实现 Serializable 接口)，允许框架保存、恢复 Bean 状态；
        logseq.order-list-type:: number
    - 特性
      - Introspection 内省 [[java-reflection]]
        logseq.order-list-type:: number
      - Properties 特性
        logseq.order-list-type:: number
      - Customization 定制化
        logseq.order-list-type:: number
      - Events 事件
        logseq.order-list-type:: number
        - Bean 可以与 EventObject EventListener 模型交互。
      - Persistence 持久化
        logseq.order-list-type:: number
      - Methods 方法
        logseq.order-list-type:: number
    - 优点
      - Bean 的属性(properties)，事件(events)和方法(method)可以暴露给其他应用
        logseq.order-list-type:: number
      - Bean 可以注册，来收发其他对象的事件；
        logseq.order-list-type:: number
      - 提供辅助软件来帮助配置 Bean；
        logseq.order-list-type:: number
      - bean 的配置可以持久化并恢复。
        logseq.order-list-type:: number
    - 缺点
      - 无参构造函数会让其他开发人员实例化无效对象，造成问题；
        logseq.order-list-type:: number
      - 不可变对象的优点点；
        logseq.order-list-type:: number
      - 大量样板代码；
        logseq.order-list-type:: number
  - Spring Beans #[[spring-framework]]
    collapsed:: true
    - 创建
      collapsed:: true
      - 实例化 Bean 对象。
      - 设置 Bean 属性。
      - 如果我们通过各种 Aware 接口声明了依赖关系，则会注入 Bean 对容器基础设施层面的依赖。具体包括 BeanNameAware、BeanFactoryAware 和 ApplicationContextAware，分别会注入 Bean ID、Bean Factory 或者 ApplicationContext。
      - 调用 BeanPostProcessor 的前置初始化方法 postProcessBeforeInitialization。
      - 如果实现了 InitializingBean 接口，则会调用 afterPropertiesSet 方法。
      - 调用 Bean 自身定义的 init 方法。
      - 调用 BeanPostProcessor 的后置初始化方法 postProcessAfterInitialization。
      - 创建过程完毕。
      - ![](https://raw.githack.com/bGZo/assets/dev/2024/Untitled_1722864586329_0.png)
    - 销毁
      collapsed:: true
      - DisposableBean 的 destroy 方法；
      - Bean 自身定制的 destroy 方法；
    - 作用域
      collapsed:: true
      - Singleton，这是 Spring 的默认作用域，也就是为每个 IOC 容器创建唯一的一个 Bean 实例。
        logseq.order-list-type:: number
      - Prototype，针对每个 getBean 请求，容器都会单独创建一个 Bean 实例。
        logseq.order-list-type:: number
        - 从 Bean 的特点来看，Prototype 适合有状态的 Bean，而 Singleton 则更适合无状态的情况。另外，使用 Prototype 作用域需要经过仔细思考，毕竟频繁创建和销毁 Bean 是有明显开销的。
      - Request，为每个 HTTP 请求创建单独的 Bean 实例。
        logseq.order-list-type:: number
      - Session，很显然 Bean 实例的作用域是 Session 范围。
        logseq.order-list-type:: number
      - GlobalSession，用于 Portlet 容器，因为每个 Portlet 有单独的 Session，GlobalSession 提供一个全局性的 HTTP Session。
        logseq.order-list-type:: number
      - #+BEGIN_NOTE
        后三种只支持 Web 容器
        #+END_NOTE
- ## Namespace
  - {{namespace beans}}
- ## ↩ Reference
-