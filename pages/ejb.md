icon:: 📄
also:: Jakarta Enterprise Beans, Enterprise JavaBeans
created:: [[20240805]]
description::

- ## Why
  -
- ## How
  -
- ## What
  - 用于企业软件模块化构建的几个Java API 之一。EJB 是封装应用程序业务逻辑的服务器端软件组件。 EJB Web 容器为 Web 相关软件组件提供运行时环境，包括计算机安全、 Java Servlet 生命周期管理、事务处理和其他Web 服务。 EJB 规范是Java EE规范的子集。
  - 规格 (Specification)
    collapsed:: true
    - EJB 规范提供了一种标准方法来实现通常在企业应用程序中找到的服务器端（也称为“后端”）“业务”软件（与“前端”用户界面软件相对）。此类软件解决相同类型的问题，并且这些问题的解决方案通常由程序员重复地重新实现。
    - EJB 旨在以标准方式处理持久性、事务完整性和安全性等常见问题，使程序员可以自由地专注于手头企业软件的特定部分。
  - 一般职责(General responsibilities)
    collapsed:: true
    - 事务处理 (Transaction processing)
      logseq.order-list-type:: number
      collapsed:: true
      - https://en.wikipedia.org/wiki/Transaction_processing
    - 集成 JPA (Jakarta Persistence) 提供的持久化服务；
      logseq.order-list-type:: number
      collapsed:: true
      - https://en.wikipedia.org/wiki/Jakarta_Persistence
    - 并发控制 (Concurrency control)；
      logseq.order-list-type:: number
      collapsed:: true
      - https://en.wikipedia.org/wiki/Concurrency_control
    - 利用 JMS (Jakarta Messaging) 和 JCA(Jakarta Connectors) 进行事件驱动编程 (Event-driven programming)；
      logseq.order-list-type:: number
      collapsed:: true
      - https://en.wikipedia.org/wiki/Event-driven_programming
      - https://en.wikipedia.org/wiki/Jakarta_Connectors
    - 异步方法调用 (Asynchronous method invocation)；
      logseq.order-list-type:: number
      collapsed:: true
      - https://en.wikipedia.org/wiki/Asynchronous_method_invocation
    - 作业调度 (Job scheduling)
      logseq.order-list-type:: number
      collapsed:: true
      - https://en.wikipedia.org/wiki/Job_scheduler
    - 通过[Java 命名和目录接口](https://en.wikipedia.org/wiki/Java_Naming_and_Directory_Interface)(JNDI) 的命名和[目录服务](https://en.wikipedia.org/wiki/Directory_service)
      logseq.order-list-type:: number
      collapsed:: true
      - Naming and [directory services](https://en.wikipedia.org/wiki/Directory_service) via [Java Naming and Directory Interface](https://en.wikipedia.org/wiki/Java_Naming_and_Directory_Interface) (JNDI)
    - 使用[RMI-IIOP](https://en.wikipedia.org/wiki/RMI-IIOP)和[Web 服务](https://en.wikipedia.org/wiki/Web_service)[进行进程间通信](https://en.wikipedia.org/wiki/Remote_procedure_call)
      logseq.order-list-type:: number
      collapsed:: true
      - [Interprocess Communication](https://en.wikipedia.org/wiki/Remote_procedure_call) using [RMI-IIOP](https://en.wikipedia.org/wiki/RMI-IIOP) and [Web services](https://en.wikipedia.org/wiki/Web_service)
    - [安全性](https://en.wikipedia.org/wiki/Computer_security)（ [JCE](https://en.wikipedia.org/wiki/Java_Cryptography_Extension)和[JAAS](https://en.wikipedia.org/wiki/Java_Authentication_and_Authorization_Service) ）
      logseq.order-list-type:: number
      collapsed:: true
      - [Security](https://en.wikipedia.org/wiki/Computer_security) ([JCE](https://en.wikipedia.org/wiki/Java_Cryptography_Extension) and [JAAS](https://en.wikipedia.org/wiki/Java_Authentication_and_Authorization_Service))
    - 在应用程序服务器中[部署](https://en.wikipedia.org/wiki/Software_deployment)[软件组件](https://en.wikipedia.org/wiki/Software_component)
      logseq.order-list-type:: number
      collapsed:: true
      - [Deployment](https://en.wikipedia.org/wiki/Software_deployment) of [software components](https://en.wikipedia.org/wiki/Software_component) in an application server
  - History 历史
    - EJB 2.0
      - 添加本地接口的概念解决了封装业务逻辑会带来性能损失问题
    - EJB 3.0
      - 使用普通 Java 对象以及支持依赖注入以简化异构系统的配置和集成 #[[spring-framework]]
      - EJB 3.0 规范严重依赖于 [注释](https://en.wikipedia.org/wiki/Java_annotation "Java annotation")（Java05）和 [约定优于配置的](https://en.wikipedia.org/wiki/Convention_over_configuration "Convention over configuration")
        - EJB 3.0 更加轻量级，几乎是一个全新的 API，与以前的 EJB 规范几乎没有相似之处
  - Types of Enterprise BeansEnterprise Bean 的类型
    - Session beans 会话bean
    - Stateful Session Beans 有状态会话 Bean
    - Stateless Session Beans 无状态会话 Bean
    - Singleton Session Beans 单例会话 Bean
    - Message driven beans 消息驱动 Bean
  - Execution 执行
    - Transactions 交易
    - Events 活动
    - Naming and directory services命名和目录服务
    - Remoting/distributed execution远程/分布式执行
  - Legacy 遗产
    - Home interfaces and required business interfaceHome接口和所需的业务接口
    - Required deployment descriptor所需的部署描述符
  - Container variations 容器变化
  - Version history 版本历史
- ## Namespace
  - {{namespace ejb}}
- ## ↩ Reference
  -
-
-
-