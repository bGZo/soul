tags:: #[[osi/application]]
- ![image.png](../assets/dev/image_1662468739910_0.png)
- (Resource) Representational state transfer, REST / 表现层状态转移, 资源在网络中以某种表现形式进行状态转移
  - **一种架构风格**
  - before: SOAP
  - > URL定位资源，用HTTP动词（GET,POST,DELETE,DETC）描述操作 from [@Ivony](https://www.zhihu.com/people/6ef2e77274cb0719253a577665cf690e)
  - REST描述的是在网络中client和server的一种交互形式；REST本身不实用，实用的是如何设计 RESTful API（REST风格的网络接口）；
  - Server提供的RESTful API中，URL中只使用名词来指定资源，原则上不使用动词。“资源”是REST架构或者说整个网络处理的核心。比如：
    - ```
      http://api.qc.com/v1/newsfeed   # 获取某人的新鲜;
      http://api.qc.com/v1/friends    # 获取某人的好友列表;
      http://api.qc.com/v1/profile    # 获取某人的详细信息;
      ```
  - 用 HTTP 协议里的动词来实现资源的添加，修改，删除等操作, 即通过HTTP动词来实现资源的状态扭转
    - GET 用来获取资源
    - POST 用来新建资源 (也可以用于更新资源)
    - PUT 用来更新资源
    - DELETE 用来删除资源
    - ```
      DELETE, http://api.qc.com/v1/     # friends: 删除某人的好友 (在http parameter指定好友id）
      POST, http://api.qc.com/v1/       # 添加好友
      UPDATE, http://api.qc.com/v1/profile  # 更新个人资料
      ```
  - Server和Client之间传递某资源的一个表现形式，比如用JSON，XML传输文本，或者用JPG，WebP传输图片等。当然还可以压缩HTTP传输时的数据（on-wire data compression）
  - 用 HTTP Status Code传递Server的状态信息。比如最常用的 200 表示成功，500 表示Server内部错误等
  - 解放思想，Web端不再用之前典型的PHP或JSP架构，而是改为前段渲染和附带处理简单的商务逻辑（比如AngularJS或者BackBone的一些样例）。Web端和Server只使用上述定义的API来传递数据和改变数据状态。格式一般是JSON。iOS和Android同理可得。由此可见，Web，iOS，Android和第三方开发者变为平等的角色通过一套API来共同消费Server提供的服务。
  - best practices
    - ```
      #1  URL root:
      https://example.org/api/v1/*
      https://api.example.com/v1/*
      #2  API versioning: 可以放在URL里面，也可以用HTTP的header：
      /api/v1/
      #3  URI使用名词而不是动词，且推荐用复数
      GET /products : will return the list of all products
      POST /products : will add a product to the collection
      GET /products/4 : will retrieve product #4
      PATCH/PUT /products/4 : will update product #4
      #4  保证 HEAD 和 GET 方法是安全的，不会对资源状态有所改变（污染）, 严格杜绝如下情况
      GET /deleteProduct?id=1
      #5  资源的地址推荐用嵌套结构
      GET /friends/10375923/profile
      UPDATE /profile/primaryAddress/city
      #6  警惕返回结果的大小。
      # 如果过大，及时进行分页（pagination）或者加入限制（limit）
      # HTTP协议支持分页（Pagination）操作，在Header中使用 Link 即可
      #7  使用正确的 HTTP Status Code 表示访问状态
      HTTP/1.1: Status Code Definitions
      #8  在返回结果用明确易懂的文本
        (String。注意返回的错误是要给人看的，避免用 1001 这种错误信息)，而且适当地加入注释
      #9  关于安全
        自己的接口就用https，加上一个key做一次hash放在最后即可
          考虑到国情，HTTPS在无线网络里不稳定，可以使用Application Level
          的加密手段把整个HTTP的payload加密。有兴趣的朋友可以用手机连上电脑的共享Wi-Fi
          然后用Charles监听微信的网络请求（发照片或者刷朋友圈）
      #10 如果是平台的API，可以用成熟但是复杂的OAuth2
      ```
  - 重要性/特点
    - **容易理解和实施**
      - 许多人知道 REST 和 HTTP, 所以他们会更容易理解和使用你的API
    - 使应用程序更具**可扩展性**
      - **无状态**
        - 在服务器端是无状态的 => **每个请求的处理都将独立于之前的请求**
        - 在具有服务器端状态或会话的应用程序中，可能为每个登录的用户存储一个 Session (会话)。这种会话数据很容易变得臃肿，并开始占用服务器上的大量资源。
        - 只在处理请求时占用资源（内存），一旦请求被处理完毕，就会释放资源
        - 负载均衡支持更好, 因为无需知道前夫在服务器端的会话信息.
      - **更快的数据交换格式**
        - 与XML相比，JSON更紧凑，尺寸更小。它也可以比XML更快地被解析
        - 虽然他们大多使用JSON操作，但也要记住，REST APIs仍然能够通过使用 [Accept header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept)来响应不同的格式
      - **缓存更容易**
        - 由于服务器是无状态的，每个请求都可以单独处理，GET请求通常应该返回相同的响应，而不考虑之前的请求和会话
      - 灵活
        - 很容易修改, 回答许多客户的要求, 他们可以要求不同的数据类型(XML, JSON等)
        - 客户端可以使用Accept头来指定类型（正如我前面提到的），REST API可以根据这一点返回不同的响应
        - 另一个值得一提的机制是 [HATEOAS](https://www.wikiwand.com/en/HATEOAS#:~:text=Hypermedia%20as%20the%20Engine%20of,provid%20information%20dynamically%20through%20hypermedia%E3%80%82)。如果你不知道这个词，不要担心，它的基本意思是。在服务器响应中返回某一特定资源的相关URLs。
          - 在HATEOAS链接的帮助下，客户端可以通过解析这个JSON来检查链接，并轻松提出请求。如果端点发生变化，他们将得到新的端点，而不需要改变客户端的代码。
-
- Refs
  - [怎样用通俗的语言解释REST，以及RESTful？- 覃超​ - 知乎](https://www.zhihu.com/question/28557115/answer/48094438)
  - [表现层状态转换（REST）是什么？有什么优点？](https://chinese.freecodecamp.org/news/benefits-of-rest/)
  - [Representational state transfer - Wikipedia](https://en.wikipedia.org/wiki/Representational_state_transfer)
  - [HATEOAS - Wikipedia](https://en.wikipedia.org/wiki/HATEOAS)
  - [REST接口设计规范](https://wangwei.info/about-rest-api/)
  - [RESTful API 设计指南 - 阮一峰的网络日志](https://www.ruanyifeng.com/blog/2014/05/restful_api.html)