icon:: 📄
also:: OSI应用层
created:: [[20240719]]
description::

- ## Why
- ## How
  - TODO 真想把里面的各种协议自己实现一遍
- ## What
  - Protocols
    collapsed:: true
    - **HTTP**, HyperText Transfer Protocol
      id:: 63305f34-8398-4775-94c5-fc82d6f40b5d
      description:: "超文本传输协议, 主要为 Web BS(浏览器/服务器) 之间的通信而设计的"
      source:: [Wikipedia](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_header_fields)
    - **HTTPS**, Hypertext Transfer Protocol Secure
      id:: 633065d1-de9c-4a67-b7ff-ec2036c3a3c1
      description:: ((63305f34-8398-4775-94c5-fc82d6f40b5d)) 的加强安全版本; 基于 ((63305f34-8398-4775-94c5-fc82d6f40b5d)); 用 TCP 作为底层协议; 并额外使用 ((63306685-01b5-4ab0-9d93-bf0f46710f9a)) 用作加密和安全认证
      source:: [Wikipedia](https://en.wikipedia.org/wiki/HTTPS)
      - **TLS/SSL**, Transport Layer Security/Secure Sockets Layer
        id:: 63306685-01b5-4ab0-9d93-bf0f46710f9a
        description:: "SSL 1996 首次发布, SSL 1.0 从未面世，SSL 2.0 则具有较大的缺陷 (DROWN 缺陷 —— Decrypting RSA with Obsolete and Weakened eNcryption), 1999 SSL 3.0 进一步升级，新版本被命名为 TLS 1.0。因此，TLS 是基于 SSL 之上的，但由于习惯叫法，通常把 HTTPS 中的核心加密协议混成为 SSL/TLS"
        source:: [Wikipedia](https://en.wikipedia.org/wiki/Transport_Layer_Security)
    - **SMTP**，Simple Mail Transfer Protocol
      id:: 633065eb-90dd-4ba4-9f3b-2e27fb4a4fae
      description:: "简单邮件传输(发送)协议, 用来发送电子邮件, 基于 TCP"
    - **POP3/IMAP**, Post Office Protocol/Internet Message Access Protocol
      id:: 63306043-53c8-40ef-96d0-b2d9df598499
      description:: 邮件接收的协议(POP3 协议); 不是 ((633065eb-90dd-4ba4-9f3b-2e27fb4a4fae))
    - **FTP**, File Transfer Protocol
      id:: 6330606b-ddcc-4bb3-903b-0e265f5c4f0b
      description:: "文件传输协议, 主要提供文件传输服务, 基于客户—服务器（C/S）模型而设计的，在客户端与 FTP 服务器之间建立两个连接"
      source:: [Wikipedia](https://en.wikipedia.org/wiki/File_Transfer_Protocol)
    - **Telnet**
      id:: 6330628e-3096-4c5c-abb4-cdc293a108e2
      description:: "远程登陆协议, 通过一个终端登陆到其他服务器"
      source:: [Wikipedia](https://en.wikipedia.org/wiki/Telnet)
      collapsed:: true
      - 缺点
        - 所有数据（包括用户名和密码）均以**明文形式发送**，这有潜在的安全风险
    - **SSH**, The Secure Shell Protocol
      id:: 6330644f-de3d-47c8-8d61-363c5b68652f
      description:: "安全的网络传输协议, 目前较可靠, 专为远程登录会话和其他网络服务提供安全性的协议"
      source:: [Wikipedia](https://en.wikipedia.org/wiki/Secure_Shell)
      collapsed:: true
      - 建立在 TCP
      - 优点
        collapsed:: true
        - 有效防止远程管理过程中的信息泄露问题
      - ((6330628e-3096-4c5c-abb4-cdc293a108e2)) #vs ((6330644f-de3d-47c8-8d61-363c5b68652f))
        - **SSH 协议会对传输的数据进行加密保证数据安全性**
      -
    - **DNS**, Domain Name System
      source:: [Wikipedia](https://en.wikipedia.org/wiki/Domain_Name_System)
    - **RIP**, Routing Information Protocol
      source:: [Wikipedia](https://en.wikipedia.org/wiki/Routing_Information_Protocol)
    - **BGP**, Border Gateway Protocol
      source:: [Wikipedia](https://en.wikipedia.org/wiki/Border_Gateway_Protocol)
    - WebSocket
      description:: 一种让客户端和服务器之间能进行双向实时通信的技术
      source:: [Wikipedia](https://en.wikipedia.org/wiki/WebSocket)
  - Process
    collapsed:: true
    - ((63305f34-8398-4775-94c5-fc82d6f40b5d))
      collapsed:: true
      - 概述
        collapsed:: true
        - 基于 TCP 协议
          collapsed:: true
          - 事先建立 TCP 连接 -> 经历 3 次握手
        - 大部分版本都是 1.1
          collapsed:: true
          - 默认是开启了 Keep-Alive 的
            collapsed:: true
            - 建立的连接就可以在多次请求中被复用
        - "无状态"(stateless) 协议 -> 无法记录客户端用户的状态
          collapsed:: true
          - 一般我们都是通过 Session 来记录客户端用户的状态
      - History
        collapsed:: true
        - ![image.png](../assets/network/image_1664174795463_0.png)
      - Request
        id:: 63314773-4bea-4356-b87b-6597fff37022
        collapsed:: true
        - Header
          collapsed:: true
          - `User-Agent`
            collapsed:: true
            - 产生请求的浏览器类型。
          - `Accept`
            collapsed:: true
            - 客户端可识别的响应内容类型列表;
          - `Accept-Language`
            collapsed:: true
            - 客户端可接受的自然语言;
          - `Accept-Encoding`
            collapsed:: true
            - 客户端可接受的编码压缩格式;
          - `Accept-Charset`
            collapsed:: true
            - 可接受的应答的字符集;
          - `Host`
            collapsed:: true
            - 请求的主机名，允许多个域名同处一个IP 地址，即虚拟主机;（必选）
          - `Connection`
            collapsed:: true
            - 连接方式(close 或  `keep-alive` );
          - `Cookie`
            collapsed:: true
            - 存储于客户端扩展字段，向同一域名的服务端发送属于该域的cookie;
          - `请求包体`
            collapsed:: true
            - 在 `POST` 方法中使用。
          - `Referer`
            collapsed:: true
            - 包含一个URL，用户从该URL代表的页面出发访问当前请求的页面。
          - `If-Modified-Since`
            collapsed:: true
            - 文档的最后改动时间
      - Response
        id:: 6331477a-b900-47d4-abb3-521bca278331
        collapsed:: true
        - Header
          collapsed:: true
          - `Allow`
            collapsed:: true
            - 服务器支持哪些请求方法（如GET、POST等）。
          - `Content-Encoding`
            collapsed:: true
            - 文档的编码（Encode）方法。
          - `Content-Length`
            collapsed:: true
            - 表示内容长度。只有当浏览器使用持久HTTP连接时才需要这个数据。
          - `Content-Type`
            collapsed:: true
            - 表示后面的文档属于什么MIME类型。
          - `Date`
            collapsed:: true
            - 当前的 GMT 时间。你可以用setDateHeader来设置这个头以避免转换时间格式的麻烦。
          - `Expires`
            collapsed:: true
            - 应该在什么时候认为文档已经过期，从而不再缓存它。
          - `Last-Modified`
            collapsed:: true
            - 文档的最后改动时间。
          - `Refresh`
            collapsed:: true
            - 表示浏览器应该在多少时间之后刷新文档，以秒计。
          - `Server`
            collapsed:: true
            - 服务器名字。
          - `Set-Cookie`
            collapsed:: true
            - 设置和页面关联的Cookie。
          - `ETag`
            collapsed:: true
            - 被请求变量的实体值。ETag是一个可以与Web资源关联的记号（MD5值）。
          - `Cache-Control`
            collapsed:: true
            - 这个字段用于指定所有缓存机制在整个请求/响应链中必须服从的指令。
          - > `Last-Modified` 与 `If-Modified-Since` 都是用来记录页面的最后修改时间。当客户端访问页面时，服务器会将页面最后修改时间通过 Last-Modified 标识由服务器发往客户端，客户端记录修改时间，再次请求本地存在的cache页面时，客户端会通过 If-Modified-Since 头将先前服务器端发过来的最后修改时间戳发送回去，服务器端通过这个时间戳判断客户端的页面是否是最新的，如果不是最新的，则返回新的内容，如果是最新的，则返回 304
        - Status, 状态码
          collapsed:: true
          - 今天网课平台炸了，报了`504 Gateway Time-out`的错误，上个月空闲的时候看过一些请求错误的原因，今天再次从网上整理过来。
          - 1XX
            description:: 临时响应并需要请求者继续执行操作的状态代码
            collapsed:: true
            - | **Number** | **State** |
              |---|---|
              | 100 | **继续**, 请求者应当继续提出请求。服务器返回此代码表示已收到请求的第一部分，正在等待其余部分 |
              | 101 | **切换协议**, 请求者已要求服务器切换协议，服务器已确认并准备切换 |
          - 2XX
            description:: 成功处理了请求的状态代码
            collapsed:: true
            - | **Number** | **State** |
              |---|---|
              | 200 | **成功**, 服务器已成功处理了请求。通常表示服务器提供了请求的网页，客户端请求已成功 |
              | 201 | **已创建**, 请求成功并且服务器创建了新的资源 |
              | 202 | **已接受**, 服务器已接受请求，但尚未处理 |
              | 203 | **非授权信息**, 服务器已成功处理了请求，但返回的信息可能来自另一来源 |
              | 204 | **无内容**, 服务器成功处理了请求，但没有返回任何内容 |
              | 205 | **重置内容**, 服务器成功处理了请求，但没有返回任何内容 |
              | 206 | **部分内容**, 服务器成功处理了部分 GET 请求 |
          - 3XX - 重定向
            description:: 要完成请求. 需要进一步重定向操作
            collapsed:: true
            - | Number | State |
              |---|---|
              | 300 | **多种选择**, 针对请求，服务器可执行多种操作。服务器可根据请求者 (user agent) 选择一项操作，或提供操作列表供请求者选择 |
              | 301 | **对象永久移动**, 请求的网页已永久移动到新位置。服务器返回此响应 (对 GET 或 HEAD 请求的响应) 时，会自动将请求者转到新位置 |
              | 302 | **对象临时移动**, 服务器目前从不同位置的网页响应请求，但请求者应继续使用原有位置来进行以后的请求 |
              | 303 | **查看其他位置**, 请求者应当对不同的位置使用单独的 GET 请求来检索响应时，服务器返回此代码 |
              | 304 | **未修改**,属于重定向, 自从上次请求后，请求的网页未修改过。服务器返回此响应时，不会返回网页内容 |
              | 305 | **使用代理**, 请求者只能使用代理访问请求的网页。如果服务器返回此响应，还表示请求者应使用代理 |
              | 307 | **临时重定向**, 服务器目前从不同位置的网页响应请求，但请求者应继续使用原有位置来进行以后的请求 |
          - 4XX - (请求错误)
            description:: "请求可能出错，妨碍了服务器的处理"
            collapsed:: true
            - | Number | State |
              |---|---|
              | 400 | **错误请求**, 服务器不理解请求的语法 |
              | 401 | **未授权**, 请求要求身份验证。 对于需要登录的网页，服务器可能返回此响应 |
              | 403 | **禁止**, 服务器拒绝请求 |
              | 404 | **未找到**, 服务器找不到请求的网页 |
              | 405 | **方法禁用**, 禁用请求中指定的方法 |
              | 406 | **不接受**, 无法使用请求的内容特性响应请求的网页 |
              | 407 | **需要代理授权**, 此状态代码与 401 (未授权) 类似，但指定请求者应当授权使用代理 |
              | 408 | **请求超时**, 服务器等候请求时发生超时 |
              | 409 | **冲突**, 服务器在完成请求时发生冲突。服务器必须在响应中包含有关冲突的信息 |
              | 410 | **已删除**, 如果请求的资源已永久删除，服务器就会返回此响应 |
              | 411 | **需要有效长度**, 服务器不接受不含有效内容长度标头字段的请求 |
              | 412 | **未满足前提条件**, 服务器未满足请求者在请求中设置的其中一个前提条件 |
              | 413 | **请求实体过大**, 服务器无法处理请求，因为请求实体过大，超出服务器的处理能力 |
              | 414 | **请求的 URI 过长**, 请求的 URI (通常为网址) 过长，服务器无法处理 |
              | 415 | **不支持的媒体类型**, 请求的格式不受请求页面的支持 |
              | 416 | **请求范围不符合要求**, 如果页面无法提供请求的范围，则服务器会返回此状态代码 |
              | 417 | **未满足期望值**, 服务器未满足"期望"请求标头字段的要求 |
          - 5XX - 服务器错误
            description:: "服务器在尝试处理请求时发生内部错误。 这些错误可能是服务器本身的错误，而不是请求出错"
            collapsed:: true
            - | Number | State |
              |---|---|
              | 500 | **服务器内部错误**, 服务器遇到错误，无法完成请求 |
              | 501 | **尚未实施**, 服务器不具备完成请求的功能。例如，服务器无法识别请求方法时可能会返回此代码 |
              | 502 | **错误网关**, 服务器作为网关或代理，从上游服务器收到无效响应 |
              | 503 | **服务不可用**, 服务器目前无法使用 (由于超载或停机维护) 。通常，这只是暂时状态 |
              | 504 | **网关超时**, 服务器作为网关或代理，但是没有及时从上游服务器收到请求 |
              | 505 | **HTTP 版本不受支持**, 服务器不支持请求中所用的 HTTP 协议版本 |
          - via: [常见HTTP错误代码大全 - 知乎](https://zhuanlan.zhihu.com/p/31674574)
      - ((63314773-4bea-4356-b87b-6597fff37022)) & ((6331477a-b900-47d4-abb3-521bca278331))
        collapsed:: true
        - ![image.png](../assets/network/image_1664174592123_0.png)
          collapsed:: true
          - `POST` 请求大小 和 `GET` 请求长度 都会被限制
            collapsed:: true
            - 两者 HTTP 协议都没有做出限制
            - 安全考虑, `POST` 服务器软件在实现时会做一定限制
            - **特定的浏览器及服务器对它的限制**对 `GET` 可提交的数据量受 URL 长度的限制
      - 条件 GET???
        collapsed:: true
        - HTTP 条件 GET 是  `HTTP`  协议为了减少不必要的带宽浪费，提出的一种方案。实际上就是利用 `If-Modified-Since` 做浏览器缓存
      - `Keep-Alive` 持久连接???
      - 跨站攻击???
        collapsed:: true
        - CSRF（Cross-site request forgery，跨站请求伪造）伪造请求，冒充用户在站内的正常操作，比如 爬虫 [[crawler]]
        - 防范的方法
          collapsed:: true
          - 关键操作只接受POST请求
          - 验证码
          - 检测 Referer
          - Token
            collapsed:: true
            - Token 要足够随机——只有这样才算不可预测
            - Token 是一次性的，即每次请求成功后要更新Token——这样可以增加攻击难度，增加预测难度
            - Token 要注意保密性——敏感操作使用 post，防止 Token 出现在 URL 中
      - 断点续传????
        collapsed:: true
        - 要实现断点续传的功能，通常都需要 **客户端记录下当前的下载进度，并在需要续传的时候通知服务端本次需要下载的内容片段**
        - HTTP1.1协议中定义了断点续传相关的HTTP头 Range 和 Content-Range 字段，一个最简单的断点续传实现大概如下
          collapsed:: true
          - 1. 客户端下载一个 `1024K` 的文件，已经下载了其中 `512K`
            2. 网络中断，客户端请求续传，因此需要在 HTTP Header 中申明本次需要续传的片段: `Range:bytes=512000-`，这个头通知服务端从文件的512K位置开始传输文件。
            3. 服务端收到断点续传请求，从文件的 512K 位置开始传输，并且在 HTTP Header 中增加: `Content-Range:bytes 512000-/1024000`，并且此时服务端返回的HTTP状态码应该是206，而不是200
        - 但是在实际场景中，会出现一种情况，即在终端发起续传请求时，URL对应的文件内容在服务端已经发生变化，此时续传的数据肯定是错误的。如何解决这个问题了？
        - 显然此时我们需要有一个标识文件唯一性的方法。在 RFC2616 中也有相应的定义，比如 实现 Last-Modified 来标识文件的最后修改时间，这样即可判断出续传文件时是否已经发生过改动。同时 RFC2616 中还定义有一个 ETag 的头，可以使用 ETag Header 来放置文件的唯一标识，比如文件的 MD5 值
        - 客户端在发起续传请求时应该在 HTTP Header 中申明 If-Match 或者 If-Modified-Since 字段，帮助服务端判别文件变化
      - 一次 HTTP 请求
        collapsed:: true
        - 域名解析
          collapsed:: true
          - 浏览器缓存
          - 系统缓存
          - hosts
          - ISP DNS 缓存
          - DNS 服务器搜索
        - 浏览器发送 HTTP 请求到目标服务器
        - 服务器永久重定向
        - 浏览器跟踪重定向地址
        - 服务器 "处理" 请求
        - 服务器发回一个HTML响应
        - 浏览器开始显示HTML
        - 浏览器请求获取嵌入在 HTML 中的对象（图片&脚本等）
        - 浏览器发送异步（AJAX）请求
      - HTTP Cache???
        collapsed:: true
        - HTTP 协议缓存的响应分析
          collapsed:: true
          - WEB 缓存: 在服务器-客户端之间搞监控，监控请求，并且把请求输出的内容（例如 HTML 页面、图片和文件）另存一份（统称为副本）；然后，如果下一个请求是相同的  URL ，则直接请求保存的副本，而不是再次访问资源服务器。
            collapsed:: true
            - 分类
              collapsed:: true
              - 浏览器缓存
              - 代理服务器缓存
              - 网关缓存
            - 好处
              collapsed:: true
              - 降低延迟：缓存离客户端更近，因此，从缓存请求内容比从源服务器所用时间更少，呈现速度更快，网站就显得更灵敏；
              - 降低网络传输：副本被重复使用，大大降低了用户的带宽使用，其实也是一种变相的省钱（如果流量要付费的话），同时保证了带宽请求在一个低水平上，更容易维护了
          - 过程
            collapsed:: true
            - 浏览器第一次请求流程如下图所示：
              ![img](https://data.educoder.net/api/attachments/543498)
            - 浏览器在第一次请求的时候不存在缓存，直接从浏览器请求，等请求返回结果之后再根据 HTTP 头信息将数据缓存在内存或者硬盘中。 浏览器再次请求同一 URL 时的流程如下图所示：
              ![img](https://data.educoder.net/api/attachments/543499)
            - 浏览器需要根据 HTTP 头信息来判断是否直接从缓存读取数据，还是交由服务器来判断是否从缓存读取数据。 **几种状态码的区别**如下图所示：
              ![img](https://data.educoder.net/api/attachments/543500)
          - HTTP 协议缓存是 WEB 缓存的一种，它是**通过 HTTP 头信息来控制缓存的**，HTTP 头信息可以让你对浏览器和代理服务器如何处理你的副本进行更多的控制。他们在 HTML 代码中是看不见的，一般由 Web 服务器自动生成。但是，根据你使用的服务器，你可以在某种程度上进行控制。相关字段如下
            collapsed:: true
            - HTTP 状态码（status code）
              collapsed:: true
              - 200 请求成功，浏览器会把响应回来的信息显示在浏览器端；
              - 304 第一次访问一个资源后，浏览器会将该资源缓存到本地；第二次再访问该资源时，如果该资源没有发生改变或失效，那么服务器响应给浏览器 304 状态码，告诉浏览器使用本地缓存的资源。
            - **Last-Modified：** 表示这个响应资源的最后修改时间。web 服务器在响应请求时，告诉浏览器资源的最后修改时间。
            - **If-Modified-Since**： 当资源过期时（使用 Cache-Control 标识的 max-age），发现资源具有 Last-Modified 声明，则再次向 WEB 服务器请求时，带上 If-Modified-Since，表示请求时间。WEB 服务器收到请求后发现有 If-Modified-Since 则与被请求资源的最后修改时间进行比对。若最后修改时间较新，说明资源有被改动过，则响应资源内容（写在响应消息包体内），HTTP 200 ；若最后修改时间较旧，说明资源无新修改，则响应 HTTP 304 (无需包体，节省流量)，告知浏览器继续使用缓存。
        - HTTP 协议缓存捕获操作方法与步骤
          collapsed:: true
          - 1.启动浏览器，确保浏览器的缓存被清除。在 Firefox 下执行此操作，请选择“工具” - > “清除最近历史记录”，然后检查缓存框； 2.启动 Wireshark 数据包嗅探，在浏览器中输入某一 URL ，浏览器应显示一个 HTML 文件； 3.再次快速地将相同的 URL 输入到浏览器中（或者只需在浏览器中点击刷新按钮）； 4.停止 Wireshark 数据包捕获，并在 display-filter-specification 窗口中输入“http”，以便只捕获 HTTP 消息，并在数据包列表窗口中显示。
    - ((63305f34-8398-4775-94c5-fc82d6f40b5d)) #vs ((633065d1-de9c-4a67-b7ff-ec2036c3a3c1))
      id:: 6330685f-d9ca-4f16-a2e0-fe8eaa82a611
      collapsed:: true
      - | **Items** | ((63305f34-8398-4775-94c5-fc82d6f40b5d)) | ((633065d1-de9c-4a67-b7ff-ec2036c3a3c1))|
        |-------| ------------------------------------------|-------------------------------------------|
        | **端口号** | 80                       | 443             |
        | **URL前缀** | `http://`              | `https://`|
        | **优点** | 扩展性强、速度快、跨平台支持性好| 保密性好、信任度高 |
    - ((633065d1-de9c-4a67-b7ff-ec2036c3a3c1))
      collapsed:: true
      - ((63306685-01b5-4ab0-9d93-bf0f46710f9a)) 工作原理
        collapsed:: true
        - 非对称加密
          description:: 采用两个密钥 —— 公钥 (加密者) + 私钥(解密者)
          id:: 390dc332-f2c5-4247-a422-132169542c78
          collapsed:: true
          - 公私钥对的生成算法依赖于单向陷门函数
            - 单向函数
              id:: 63306b1f-296b-4cf8-81ab-8409e4e14665
              - 已知单向函数 $f$，给定任意一个输入 $x$，易计算输出 $y=f(x)$；而给定一个输出 $y$，假设存在 $f(x)=y$，很难根据 $f$ 来计算出 $x$
            - 单向陷门函数
              - 一个较弱的 ((63306b1f-296b-4cf8-81ab-8409e4e14665))
              - 已知单向陷门函数 $f$，陷门 $h$，给定任意一个输入 $x$，易计算出输出 $y=f(x;h)$; 而给定一个输出 $y$，假设存在 $f(x;h)=y$，很难根据 $f$ 来计算出 $x$，但可以根据 $f$ 和 $h$ 来推导出 $x$
            - 函数 $f$ 的计算方法相当于公钥
            - 陷门 $h$ 相当于私钥
            - 公钥 $f$ 是公开的
            - 任何人对已有输入，都可以用 $f$ 加密，而要想根据加密信息还原出原信息，必须要有私钥才行
        - **(实际)** 对称加密
          description:: 通信双方共享唯一密钥 $k$. 加解密算法已知. 加密方利用密钥 $k$ 加密. 解密方利用密钥 $k$ 解密. 保密性依赖于密钥 $k$ 的保密性
          collapsed:: true
          - ((390dc332-f2c5-4247-a422-132169542c78)) 存在的必要吗 ???
            - 网络通信的信道是不安全, 传输报文对任何人是可见的
              - **密钥的交换肯定不能直接在网络信道中传输**
              - 使用 ((390dc332-f2c5-4247-a422-132169542c78)), 对对称加密的密钥进行加密，保护该密钥不在网络信道中被窃听
              - 通信双方只需要一次非对称加密，交换对称加密的密钥
            - 在之后的信息通信中, 使用绝对安全的密钥, 对信息进行对称加密，即可保证保密性
        - CA，Certificate Authority, 证书颁发机构
          description:: CA 默认是受信任的第三方; CA 会给各个服务器颁发证书. 证书存储在服务器上.并附有 CA 的**电子签名**
          id:: 63306dd5-61c0-46d5-8e5a-11097c6848dd
          collapsed:: true
          - 1. 当客户端 (浏览器) 向服务器发送 HTTPS 请求时，一定要先获取目标服务器的证书，并根据证书上的信息，检验证书的合法性
            2. 一旦客户端检测到证书非法，就会发生错误 ✖
            3. 客户端获取了服务器的证书后，由于证书的信任性是由第三方信赖机构认证的，而证书上又包含着服务器的公钥信息，客户端就可以放心的信任证书上的公钥就是目标服务器的公钥 ✔
          - 目的: **公钥传输的信赖性问题**
            - > 客户端 C 和服务器 S 想要使用 SSL/TLS 通信，由上述 SSL/TLS 通信原理，C 需要先知道 S 的公钥，而 S 公钥的唯一获取途径，就是把 S 公钥在网络信道中传输。要注意网络信道通信中有几个前提：
              1. 任何人都可以捕获通信包
              2. 通信包的保密性由发送者设计
              3. 保密算法设计方案默认为公开，而（解密）密钥默认是安全的
              >
              >因此，假设 S 公钥不做加密，在信道中传输，那么很有可能存在一个攻击者 A，发送给 C 一个诈包，假装是 S 公钥，其实是诱饵服务器 AS 的公钥。当 C 收获了 AS 的公钥（却以为是 S 的公钥），C 后续就会使用 AS 公钥对数据进行加密，并在公开信道传输，那么 A 将捕获这些加密包，用 AS 的私钥解密，就截获了 C 本要给 S 发送的内容，而 C 和 S 二人全然不知。
              >
              >同样的，S 公钥即使做加密，也难以避免这种信任性问题，C 被 AS 拐跑了！
            - ![image.png](../assets/network/image_1664118375309_0.png)
        - 数字签名
          description:: 是 ((63306dd5-61c0-46d5-8e5a-11097c6848dd)) 在给服务器颁发证书时. 使用散列+加密的组合技术. 在证书上盖个章. 以此来提供验伪的功能
          collapsed:: true
          - 1. ((63306dd5-61c0-46d5-8e5a-11097c6848dd)) 知道服务器的公钥，对该公钥采用散列技术生成一个摘要。((63306dd5-61c0-46d5-8e5a-11097c6848dd)) 使用 ((63306dd5-61c0-46d5-8e5a-11097c6848dd)) 私钥对该摘要进行加密，并附在证书下方，发送给服务器。
            2. 现在服务器将该证书发送给客户端，客户端需要验证该证书的身份。客户端找到第三方机构 ((63306dd5-61c0-46d5-8e5a-11097c6848dd))，获知 ((63306dd5-61c0-46d5-8e5a-11097c6848dd)) 的公钥，并用 ((63306dd5-61c0-46d5-8e5a-11097c6848dd)) 公钥对证书的签名进行解密，获得了 ((63306dd5-61c0-46d5-8e5a-11097c6848dd)) 生成的摘要。
            3. 客户端对证书数据（也就是服务器的公钥）做相同的散列处理，得到摘要，并将该摘要与之前从签名中解码出的摘要做对比，如果相同，则身份验证成功；否则验证失败
            - ![image.png](../assets/network/image_1664118744750_0.png)
              - 1. 设有服务器 S，客户端 C，和第三方信赖机构 CA。
                2. S 信任 CA，CA 是知道 S 公钥的，CA 向 S 颁发证书。并附上 CA 私钥对消息摘要的加密签名。
                3. S 获得 CA 颁发的证书，将该证书传递给 C。
                4. C 获得 S 的证书，信任 CA 并知晓 CA 公钥，使用 CA 公钥对 S 证书上的签名解密，同时对消息进行散列处理，得到摘要。比较摘要，验证 S 证书的真实性。
                5. 如果 C 验证 S 证书是真实的，则信任 S 的公钥（在 S 证书中）
                ![image.png](../assets/network/image_1664118940880_0.png)
          - 目的: 防止证书被伪造
        - 不用 ((63306685-01b5-4ab0-9d93-bf0f46710f9a))  的通信风险
          collapsed:: true
          - **窃听**风险（eavesdropping）：第三方可以获知通信内容。
          - **篡改**风险（tampering）：第三方可以修改通信内容。
          - **冒充**风险（pretending）：第三方可以冒充他人身份参与通信。
        - 希望达到
          collapsed:: true
          - 所有信息都是加密传播，第三方无法窃听。
          - 具有校验机制，一旦被篡改，通信双方会立刻发现。
          - 配备身份证书，防止身份被冒充。
        - TLS 运行过程 ???
          - ![image.png](../assets/network/image_1664177928239_0.png)
          - 客户端发出请求 (ClientHello)
          - 服务器回应（SeverHello）
          - 客户端回应
          - 服务器的最后回应
        - 中间人攻击 (MITM)
          - TLS对中间人攻击的抵御
            - 当然正常情况下，我们的网络安全肯定不会这么脆弱。得利于TLS证书体系，虽然我们能发起中间人攻击，不过浏览器察觉到了证书的异常。这是因为我们冒充了目标网站，但是并没有目标网站的证书，这样浏览器在校验证书时很容易发现证书错误。
          - 无法抵御中间人攻击的实例
            - **部分开发者忽视证书校验**，或对证书异常处理不当，导致本来十分有效LTS失去原本的防御能力。有许多APP存在类似的问题，包括个别金融类应用，还有部分APP部分模块的**流量存在被劫持**的风险
        - More
          collapsed:: true
          - [数字签名及数字证书原理](https://www.bilibili.com/video/BV18N411X7ty/)
            {{video https://www.bilibili.com/video/BV18N411X7ty/}}
    -
    - ((6330606b-ddcc-4bb3-903b-0e265f5c4f0b))
      collapsed:: true
      - 基于 TCP (**2条!!!**)
        - 控制连接：用于传送控制信息（命令和响应）
        - 数据连接：用于数据传送；
        - 这种将命令和数据分开传送的思想大大提高了 FTP 的效率。
      - 好处
        - 可以屏蔽操作系统和文件存储方式
      - ![image.png](../assets/network/image_1664115729199_0.png)
    - Email
      collapsed:: true
      - 发送过程
        - 通过 ((633065eb-90dd-4ba4-9f3b-2e27fb4a4fae)) 协议，我将我写好的邮件交给 Sender 的邮箱服务器（邮局）
        - Sender 邮箱服务器发现目标 Target 邮箱, 然后使用 ((633065eb-90dd-4ba4-9f3b-2e27fb4a4fae)) 将邮件转发到 Target 服务器
        - Target 服务器接收邮件之后, 通知 Target 邮箱的用户来收邮件, 用户就通过 ((63306043-53c8-40ef-96d0-b2d9df598499)) 将邮件取出
        - ![image.png](../assets/network/image_1664115124898_0.png)
      - 判断邮箱是真正存在的?
        description:: 利用 ((633065eb-90dd-4ba4-9f3b-2e27fb4a4fae)) 来检测
        - 查找邮箱域名对应的 ((633065eb-90dd-4ba4-9f3b-2e27fb4a4fae)) 服务器地址
        - 尝试与服务器建立连接
        - 连接成功后尝试向需要验证的邮箱发送邮件
        - 根据返回结果判定邮箱地址的真实性
        - [[tool]] Online
          - https://verify-email.org/
          - http://tool.chacuo.net/mailverify
          - https://www.emailcamel.com/
- ## Namespace
  - {{namespace osi/application}}
- ## ↩ Reference
  - [HTTP | Interview](https://hadyang.com/interview/docs/basic/net/http/)
  - [HTTPS | Interview](https://hadyang.com/interview/docs/basic/net/https/)
    - [HTTPS 精读之 TLS 证书校验](https://zhuanlan.zhihu.com/p/30655259)
    - [细说 CA 和证书](https://www.barretlee.com/blog/2016/04/24/detail-about-ca-and-certs/)
    - [HTTPS中间人攻击实践（原理·实践）](https://www.cnblogs.com/lulianqi/p/10558719.html)
  - [Internet protocol suite - Wikipedia](https://en.wikipedia.org/wiki/Internet_protocol_suite)
  - [应用层常见协议总结（应用层） | JavaGuide](https://javaguide.cn/cs-basics/network/application-layer-protocol.html)
  - [websocket和普通的socket有什么区别？ - 知乎](https://www.zhihu.com/question/302220040)
-