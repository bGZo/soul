alias:: architecture/pattern/serverless, pattern/architecture/serverless
tags:: TODO

-
- 现实问题
  collapsed:: true
  - 说来说去，到底 Serverless 要解决什么问题？
    - 咱们就拿自己部署一套博客来说吧，常见的 Node.js MVC 架构，需要购买云服务商的 Linux 虚拟机、RDS 关系型数据库，做得好的话还要购买 Redis 缓存、负载均衡、CDN 等等。再专业一点，可能还会考虑容灾和备份，这么算下来一年最小开销都在 1 万元左右。但如果你用 Serverless 的话，这个成本可以直接降到 1000 元以下。
    - Serverless 是对运维体系的极端抽象
    - 它给应用开发和部署提供了一个极简模型。这种高度抽象的模型，可以让一个零运维经验的人，几分钟就部署一个 Web 应用上线，并对外提供服务。
  - 为什么阿里巴巴、腾讯这样的公司都在关注 Serverless？
    - 首先，Serverless 可以有效降低企业中中长尾应用的运营成本
    - 中长尾应用就是那些每天大部分时间都没有流量或者有很少流量的应用，你可以想想你们公司是不是也有很多
    - 其次，Serverless 可以提高研发效能
    - SFF（Serverless For Frontend）可以让前端同学自行负责数据接口的编排，微服务 BaaS 化则让我们的后端同学更加关注领域设计。可以说，这是一个颠覆性的变化，它能够进一步放大前端工程师的价值。
    - 我看到有创业公司用 FaaS 来做基础设施编排和云服务编排；也有外包公司利用 Serverless 应用架构的快速迭代能力，提升开发效率，降低出错率，还可以给自己沉淀领域的解决方案；还有包括风险投资方也在逐渐开始关注 Serverless 领域，毕竟这也是一个新的风口
  - Serverless 对前端工程师来说会有什么机遇？为什么我们要学习 Serverless？
    - 云服务的红利
    - 基础篇，我会继续带你理解 Serverless 要解决什么问题，以及 Serverless 的边界和定义。搞清楚了来龙去脉，我们会进入动手环节，我会通过一个例子来给你讲解 Serverless 引擎盖下的工作原理，以及 FaaS 的一些应用场景。
    - 进阶篇，我们将一起学习 FaaS 的后端解决方案 BaaS，以及我们自己现有的后端应用如何 BaaS 化。为了更好地展现 Serverless 的发展历程和背后的思考，我也为你准备了一个基于 Node.js 的待办任务的 Web 应用，你要做好准备，这里我会给你布置很多动手作业。
    - 实战篇，我会通过 Google 开源的 Kubernetes 向你演示本地化 Serverless 环境如何搭建，并根据我的经验，和你聊聊 Serverless 架构应该如何选型，以及目前 Serverless 开发的最佳实践。
- Serverless
  collapsed:: true
  - 能解决什么问题？
    - Server + Less
      - 较少关心服务端
  - 什么是 Server ?
    - MVC 架构
      - ![image.png](../assets/architecture/image_1654793834200_0.png)
        - 前端 (View)
          - 负责客户终端的体验
        - 后端 (Control & Model)
          - 负责商业的业务逻辑和数据处理 (数据流)
        - ![image.png](../assets/architecture/image_1654793952933_0.png)
          - 异地多活
          - 稳定地切换流量
            - 负载均衡服务
              - 负责将流量均衡地分配到各个应用机器上
            - 反向代理服务 (Nginx)
              - 从请求中解析出域名信息，并将请求转发到上游 upstream 的监听地址
        - Serverless 解决问题的边界，就是服务端的边界，即服务端运维
    - 服务端运维发展史，从 full 到 less
      - 对比 Serverfull 和 Serverless 之间的差别
        - Serverfull 就是服务端运维全由我们自己负责，Serverless 则是服务端运维较少由我们自己负责，大多数的运维工作交给自动化工具负责
    - **史前时代，Serverfull**
      - 缺陷也很明显：小服成了工具人，被困在了大量的运维工作中，处理各种发布相关琐碎的杂事。
      - 这个时代研发和运维隔离，服务端运维都交给小服一个人，纯人力处理，也就是 Serverfull
      - 像发布版本和处理线上故障这种工作这些是小程的职责，都要小服协助，是不是应该小程自己处理？
    - 农耕时代，[[devops]]
      - 小服渐渐发现日常其实有很多事情都是重复性的工作，尤其是发布新版本的时候，与其每次都等小程电话，线上出故障了还要自己抓日志发过去，效率很低，不如干脆自己做一套运维控制台 OpsConsole，将部署上线和日志抓取的工作让小程自己处理
      - 优化架构节省资源和扩缩容资源方案，还是需要小服定期审查。
      - 这个时代就是研发兼运维 DevOps，小程兼任了小服的部分工作。小服将部分服务端运维的工作工具化了，自己可以去做更加专业的事情。相对史前时代，小程负责的更多，看起来是不是小程负责的事情多（More）了？但实际这些事情本身就应该是小程负责的。版本控制、线上故障都是小程自己应该处理的。而且小服将这部分人力的工作工具化了，更加高效。其实已经有变少（less）的趋势了
    - 工业时代
      - 小服发现资源优化和扩缩容方案也可以利用性能监控 + 流量估算解决
      - OpsConsole 系统再进一步，帮小程做了一套代码自动化发布的流水线：代码扫描 - 测试 - 灰度验证 - 上线
      - 只要将最新的代码合并到 Git 仓库指定的 develop 分支，剩下的就都由流水线自动化处理发布上线了
      - 免运维 NoOps
      - 小服的服务端运维工作全部自动化了
      - 小程也变回到最初，只需要关心自己的应用业务就可以了
      - 对于小服来说，小程的角色存在感越来越弱，需要小程参与的事情越来越少，都由自动化工具替代了。这就是“Serverless”
    - 未来
      - 小服要转型
      - 转型去做更底层的服务，做基础架构的建设，提供更加智能、更加节省资源、更加周到的服务
      - 免运维 NoOps 并不是说服务端运维就不存在了，而是通过全知全能的服务，覆盖研发部署需要的所有需求，让研发同学小程对它的感知越来越少。
      - NoOps 是理想状态，因为我们只能无限逼近 NoOps，所以这个单词是 less，不可能是 Server Least 或者 Server Zero
      - Serverless 就应该叫做服务端免运维。这也就是 Serverless 要解决的问题
  - 为什么难定义?
    - 要解决的就是将小服的工作彻底透明化
    - 意味着需要对整个互联网服务端的运维工作进行极端抽象
    - 越抽象的东西，其实越难定义，因为蕴含的信息量太大了，这就是 Serverless 很难准确定义的根本原因
    - Serverless 对 Web 服务开发的革命之一，就是极度简化了服务端运维模型，使一个零经验的新手，也能快速搭建一套低成本、高性能的服务端应用
  - 什么是 Serverless ?
    - 狭义
      - id:: 62a1b27a-f837-4456-936b-1598547d4231
        collapsed:: true
        $$Serverless = Serverless\ Computing = FaaS = Trigger + FaaS + BaaS = FaaS + BaaS$$
        - Trigger: 事件驱动
        - **FaaS (Function as a Service) / Serverless Computing**: 函数即服务
          collapsed:: true
          - 随时随地创建、使用、销毁一个函数
          - 从代码加载到内存 (实例化)
          - 触发器 Trigger 或者被其它函数调用时执行
          - 预先设置好 [[runtime]], [[runtime]] 里面加载的函数和资源都是云服务商提供
            collapsed:: true
            - 临时，函数调用完后，这个临时 Runtime 和函数一起销毁
              collapsed:: true
              - FaaS 推荐无状态的函数
                collapsed:: true
                - 函数不可改变 Immutable
                  collapsed:: true
                  - 一个函数只要参数固定，返回的结果也必须是固定的
        - BaaS (Backend as a Service): 后端即服务，**持久化**或第三方服务
          collapsed:: true
          - 一个集合
            collapsed:: true
            - 具备高可用性和弹性
            - 免运维的后端服务
          -
        - XaaS (X as a Service): X 即服务
          collapsed:: true
          - 云服务商喜欢使用的一种命名方式
            collapsed:: true
            - SaaS、PaaS、IaaS 都是这样
      - ![image.png](../assets/architecture/image_1654794140348_0.png)
    - 广义
      collapsed:: true
      - collapsed:: true
        $$Serverless = 服务端免运维 = 具备 Serverless 特性的云服务$$
        - 无需用户关心服务端的事情 (容错, 容灾, 安全验证, 自动扩缩容, 日志调试等等)
        - 按使用量 (调用次数, 时长等) 付费, 低费用和高性能并行, 大多数场景下节省开支
        - 快速迭代 & 试错能力 (多版本控制, 灰度, CI&CD 等等)
    - #History 2014 年 11 月，亚马逊推出真正意义上的第一款 Serverless FaaS 服务: **Lambda**
      collapsed:: true
      - Serverless 的概念才进入了大多数人的视野，也因此 Serverless 曾经一度就等于 FaaS
    - 我们日常谈 Serverless 的时候，基本都是指狭义的 Serverless，但当我们提到某个服务 Serverless 化的时候，往往都是指广义的 Serverless。
    - MVC -> Faas + View + Baas
      - ![image.png](../assets/architecture/image_1654794176501_0.png)
        - View 层是客户端展现的内容，通常并不需要函数算力
        - Control 层，就是函数的典型使用场景
          - 我们完全可以用 **FaaS 函数** 来代替 Control 函数
            - 在 HTTP 的数据请求量大的时候，FaaS 函数会自动扩容多实例同时运行；
            - 在 HTTP 的数据请求量小时，又会自动缩容；
            - 当没有 HTTP 数据请求时，还会缩容到 0 实例，节省开支
          - 后端服务最好是将 FaaS 操作的数据库的命令，封装成 HTTP 的 OpenAPI，提供给 FaaS 调用，自己控制这个 API 的请求频率以及限流降级
            - 本身则可以通过连接池、MySQL 集群等方式去优化
          - 一个 HTTP 的数据请求对应一个 Control 函数，
        - Model 层，就需要我们用 BaaS 来解决
- Principle
  - FaaS 运行
    collapsed:: true
    - How Run?
      collapsed:: true
      - Translate
        collapsed:: true
        - ![image.png](../assets/architecture/image_1663767846328_0.png)
      - FaaS
        collapsed:: true
        - ![image.png](../assets/architecture/image_1663768249512_0.png)
          collapsed:: true
          - 1. 用户第一次访问 HTTP 函数触发器时，函数触发器就会 Hold 住用户的 HTTP 请求，并产生一个 HTTP Request 事件通知函数服务
            2. 函数服务就会检查有没有闲置的函数实例；如果没有函数实例，就去函数代码仓库中拉取你的代码；初始化并启动一个函数实例，执行这个函数，传入这个 HTTP Request 对象作为函数的参数，执行函数
            3. 函数执行的结果 HTTP Response 返回函数触发器，函数触发器再将结果返回给等待的用户客户端
      - PaaS #vs FaaS
        id:: 632b160e-e374-41f5-8c9d-5fb142a6212b
        collapsed:: true
        - **资源利用率**
          collapsed:: true
          - FaaS 应用实例可以缩容到 0
          - PaaS 至少要维持 1 台服务器或容器
    - Why Fast?
      collapsed:: true
      - FaaS 冷启动 -> **从调用函数开始到函数实例准备完成的整个过程**
        define:: "冷启动, PC上关闭电源后，PC 再启动仍然需要重新加载 BIOS 表，也就是从硬件驱动开始启动，因此启动速度很慢"
        collapsed:: true
        - > 现在的云服务商，基于不同的语言特性，冷启动平均耗时基本在 100～700 毫秒之间。得益于 Google 的 JavaScript 引擎 Just In Time 特性，Node.js 在冷启动方面速度是最快的
        - ![image.png](../assets/architecture/image_1663768478236_0.png)
          collapsed:: true
          (蓝色厂商, 红色用户函数)
          - 响应时间足够小, 足够快 (1 秒以内，都算优秀)
        - **响应时间**敏感 -> **预热冷启动或预留实例策略**
          define:: "一旦你更新代码，云服务商就会偷偷开始调度资源，下载你的代码构建函数实例的镜像。请求第一次访问时，云服务商就可以利用构建好的缓存镜像，直接跳过冷启动的下载函数代码步骤，从镜像启动容器"
          url:: https://help.aliyun.com/document_detail/138103.html
        -
      - ((632b160e-e374-41f5-8c9d-5fb142a6212b))
        id:: 632b2ad7-d6b2-4419-9f24-d6826686d54a
        collapsed:: true
        - 应用托管平台 PaaS 为了适应用户的多样性，必须支持多语言兼容，还要提供传统后台服务
          collapsed:: true
          - 初始化环境时，有大量依赖和多语言版本需要兼容，而且兼容多种用户的应用代码往往也会增加应用构建过程的时间
        - FaaS 设计之初就牺牲了用户的可控性和应用场景，来简化代码模型，并且通过**分层结构**进一步提升资源的利用率
    - How 分层 (3)
      collapsed:: true
      - ![image.png](../assets/architecture/image_1663775012066_0.png)
        collapsed:: true
        - 容器
          id:: 632b1491-1149-4627-b902-a4c96cfa480d
        - 运行时 Runtime
          id:: 632b31fc-dc1d-4fbd-b5df-ee469cf847b8
        - 具体函数代码
      - 好处 -> **资源统筹优化，快速低成本地被执行**
        collapsed:: true
        - ((632b1491-1149-4627-b902-a4c96cfa480d))
          collapsed:: true
          - 适用性更广
            collapsed:: true
            - 云服务商预热大量的容器实例，将物理服务器的计算资源碎片化
        - ((632b31fc-dc1d-4fbd-b5df-ee469cf847b8))
          collapsed:: true
          - 实例适用性较低，可以少量预热
      - ![image.png](../assets/architecture/image_1663775432057_0.png)
  - FaaS 进程模型
    collapsed:: true
    - (2)
      collapsed:: true
      - 常驻进程
        collapsed:: true
        - 为了适应传统 MVC 架构设计的，它看起来并不自然
      - 用完即毁
        collapsed:: true
        - 可以最大限度发挥 FaaS 的优势
    - ((632b160e-e374-41f5-8c9d-5fb142a6212b))
      collapsed:: true
      - PaaS
        collapsed:: true
        - 启动 Web 服务时，主进程初始化连接 MongoDB
        - 初始化完成后，持续监听服务器的 80 端口，直到监听端口的句柄关闭或主进程接收到终止信号
        - 当 80 端口和客户端建立完 TCP 链接，有 HTTP 请求过来，服务器就会将请求转发给 Web 服务的主进程，这时主进程会创建一个子进程来处理这个请求
      - FaaS
        collapsed:: true
        - Node.js 的 Server 对象采用 FaaS Runtime 提供的 Server 对象，然后我们把监听端口改为监听 HTTP 事件。启动 Web 服务时，主进程初始化连接 MongoDB，初始化完成后，持续监听 HTTP 事件，直到被云服务商控制的父进程关闭回收。
        - 当 HTTP 事件发生时，我们的 Web 服务主进程跟之前一样，创建一个子进程来处理这个请求事件
        - 主进程就如我们上图中绘制的那个蓝色的圆点，当 HTTP 事件发生时，它创建的子进程就是蓝色弧形箭头，当子进程处理完后就会被主进程回收。
  - 数据编排
    collapsed:: true
    - BFF
      collapsed:: true
      - ![image.png](../assets/architecture/image_1663778024023_0.png)
    - SFF
      collapsed:: true
      - ![image.png](../assets/architecture/image_1663778075959_0.png)
  - 服务编排
  - 快速扩缩容
    id:: 632b3d34-34f1-4c97-b12c-db9269128813
    - GitHub 地址： https://github.com/pusongyang/todolist-backend
      - 用 Apache 提供的 ab 工具，压测一下我们的项目
        url:: http://httpd.apache.org/
      - ```shell
        # 模拟1000个请求，由200个用户并发访问我们启动的本地3001端口
        ab -n 1000 -c 200 http://localhost:3001/
        ```
    - 纵向扩缩容与横向扩缩容
      - ![image.png](../assets/architecture/image_1663778452374_0.png)
      - Stateful VS Stateless
      -
- Refs
  - Serverless入门课 - 蒲松洋
-
-