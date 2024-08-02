icon:: 📄
created:: [[20240802]]
description:: Web 服务器或 Web 浏览器的 API (web 类型的 API)
wikipedia:: https://en.wikipedia.org/wiki/Web_API

- ## Why
  -
- ## How
  -
- ## What
  - Client side 客户端
  - Server side 服务器端
    - Endpoints 端点 => 组成 Web APIs 的最小单位
      - Webhook 是用 URI 作为触发器，本地客户端请求，远程服务器执行回调，提供一种点对点IPC；
    - Resources versus services 资源与服务
      - Web 2.0 Web API 通常使用基于机器的交互，例如REST和SOAP 。
        collapsed:: true
        - RESTful Web API 使用 HTTP 方法通过 URL 编码的参数访问资源，并使用 JSON 或 XML 传输数据。
        - SOAP 协议由 W3C 标准化，并强制使用 XML 作为有效负载格式，通常通过HTTP进行。
          collapsed:: true
          - 此外，基于 SOAP 的 Web API 通过利用 WSDL 文档提供的XML 模式，使用XML 验证来确保结构消息的完整性。 WSDL文档准确地定义了Web 服务的 XML 消息和传输绑定。
  - Example 例子
    - https://api.nasa.gov/planetary/apod
- ## Namespace
  - {{namespace web-api}}
- ## ↩ Reference
  - ![image.png](../assets/wiki/image_1668337528771_0.png)
-