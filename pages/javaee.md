icon:: 📄
also:: java-enterprise-edition
created:: [[20240802]]
description:: 拓展 [[javase]] 
wikipedia:: https://en.wikipedia.org/wiki/Java_EE

- ## Why
- ## How
- ## What
  - Specifications
    - Web specifications 网络规格
      logseq.order-list-type:: number
      - [[servlet]]
      - Jakarta WebSocket
      - [Jakarta Faces](https://en.wikipedia.org/wiki/Jakarta_Faces)
      - [Jakarta Expression Language](https://en.wikipedia.org/wiki/Jakarta_Expression_Language)
    - Web service specifications 网络服务规格
      logseq.order-list-type:: number
      - [Jakarta RESTful Web Services](https://en.wikipedia.org/wiki/Jakarta_RESTful_Web_Services) => [[rest]]ful
      - Jakarta JSON
      - Jakarta JSON Binding
      - [Jakarta XML Binding](https://en.wikipedia.org/wiki/Jakarta_XML_Binding)
      - [Jakarta XML Web Services](https://en.wikipedia.org/wiki/Jakarta_XML_Web_Services) => SOAP
    - Enterprise specifications 企业规格
      logseq.order-list-type:: number
      - Jakarta Activation ( *JAF* )
        - 提供数据类型和此类类型的绑定来扩展组件 Bean
      - Jakarta Contexts and Dependency Injection ( [[cdi]] )
        - 提供[依赖注入](https://en.wikipedia.org/wiki/Dependency_injection)容器
      - [Jakarta Enterprise Beans](https://en.wikipedia.org/wiki/Jakarta_Enterprise_Beans) ([[ejb]])
        - 定义了一组轻量级 API，对象容器（EJB 容器）将支持这些 API，以便提供[事务](https://en.wikipedia.org/wiki/Transaction_processing)（使用[JTA](https://en.wikipedia.org/wiki/Jakarta_Transactions) ）、[远程过程调用](https://en.wikipedia.org/wiki/Remote_procedure_call)（使用[RMI](https://en.wikipedia.org/wiki/Java_remote_method_invocation)或[RMI-IIOP](https://en.wikipedia.org/wiki/RMI-IIOP) ）、[并发控制](https://en.wikipedia.org/wiki/Concurrency_control)、[依赖关系](https://en.wikipedia.org/wiki/Dependency_injection)业务对象的[注入](https://en.wikipedia.org/wiki/Dependency_injection)和[访问控制](https://en.wikipedia.org/wiki/Access_control)。该包包含 Jakarta Enterprise Beans 类和接口，它们定义企业 Bean 与其客户端之间以及企业 Bean 与 ejb 容器之间的契约。
      - [Jakarta Persistence](https://en.wikipedia.org/wiki/Jakarta_Persistence) ( [[jpa]] )
        - 关系数据库表和 Java 类之间的对象关系映射的规范
      - [Jakarta Transactions](https://en.wikipedia.org/wiki/Jakarta_Transactions) (*JTA*)
        - 包含与 Jakarta EE 提供的事务支持进行交互的接口和注释。尽管此 API 从真正的低级细节中抽象出来，但这些接口也被认为是低级的，并且 Jakarta EE 中的普通应用程序开发人员要么假定依赖于更高级别 EJB 抽象对事务的透明处理，要么使用此 API 与 CDI 托管 bean 结合提供的注释。
      - [Jakarta Messaging](https://en.wikipedia.org/wiki/Jakarta_Messaging) (*JMS*)
        - 提供了一种创建、发送、接收和读取企业消息传递系统消息的通用方法
    - Other specifications
      logseq.order-list-type:: number
      - Jakarta Validation
        - 此包包含[Jakarta Validation](https://en.wikipedia.org/w/index.php?title=Jakarta_Validation&action=edit&redlink=1) API 提供的声明性验证支持的注释和接口。 Jakarta Validation 提供了一种统一的方式来提供对可以跨层强制执行的 bean 的约束（例如 Jakarta Persistence 模型类）。在 Jakarta EE 中，Jakarta Persistence 在持久层中遵循 Bean 验证约束，而[JSF](https://en.wikipedia.org/wiki/JavaServer_Faces)在视图层中这样做。
      - Jakarta Batch
        - 提供了在应用程序中[进行批处理](https://en.wikipedia.org/wiki/Batch_processing)的方法，以运行可能涉及大量数据并且可能需要定期执行的长时间运行的后台任务。
      - [Jakarta Connectors](https://en.wikipedia.org/wiki/Jakarta_Connectors)
        - 基于 Java 的工具，用于连接应用程序服务器和企业信息系统 ( *EIS* )，作为企业应用程序集成 ( *EAI* ) 的一部分。这是一个针对普通应用程序开发人员通常不会接触的供应商的低级 API。
- ## Namespace
  - {{namespace java-ee}}
- ## ↩ Reference
  -
-