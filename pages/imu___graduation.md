also:: 基于 springcloud 的商城系统的设计与开发
tags:: #spring/cloud

  - [赵俊峰](https://ccs.imu.edu.cn/info/1152/4630.htm)`；`4994323`；`cszjf@imu.edu.cn`
  - 课题介绍：
    collapsed:: true
    - 随着互联网技术的迅猛发展，用户对于应用软件的各种功能，设计的要求越来越高。开发者在开发的过程中系统内部的耦合程度也越来越高，大大小小的模块都集中在同一个项目里，整个项目变得十分庞大，让开发者难以维护。而且每个功能模块依赖的是相同的数据库，内存等资源，当某个功能模块对项目资源使用不恰当，会使整个系统瘫痪。并且随着系统的用户访问量越来越多时，传统的单体系统虽然可以部署到多台机器上组成集群进行水平扩展。但是，这种扩展是对整个系统的扩展，只针对某一个模块是做不到的。微服务架构改变了单体应用的缺陷，将臃肿的单体系统拆分开来，使得程序易开发，理解和维护。支持应用根据需求进行模块划分，不同模块可以使用不同的编程语言，使用不同的数据存储技术，独立部署和启动。
    - 任务：
      - 通过使用微服务相关的技术和组件，实现一个完整的微服务系统。掌握微服务相关的基础知识，了解微服务相比于传统单体应用的优势和实现方式的不同。
    - 目标：
      - 通过让学生实现微服务系统，了解微服务的架构的优势与实现方式。
  - 主要内容
    collapsed:: true
    - 需求分析
    - 概要设计
    - 详细设计
    - 代码实现
    - 测试
  - 设计要求
    collapsed:: true
    - 开发的系统要有一定难度和新意。
    - 系统的每个模块设计要合理。
    - 程序要有一定的规模，不能少于 5000 行代码。
    - 能够根据导师要求做演示
  - 毕业论文（设计）课题所需环境和技术要求
    collapsed:: true
    - 环境：
      - win10 、IDEA
    - 技术要求：
      - 了解微服务相关知识，熟悉java、SSM、springcloud等。
  - 毕业论文（设计）课题相关数据和参考资料
    collapsed:: true
    - 相关数据：
      - 无
    - 参考论文：
      - [1] 杨宇,焦丽琴.基于微服务的企业应用设计与实现[J].电子科学技术,2016,03(05):623-625.DOI:10.16453/j.issn.2095-8595.2016.05.021.
      - [2] 洪华军,吴建波,冷文浩.一种基于微服务架构的业务系统设计与实现[J].计算机与数字工程,2018,46(01):149-154.
      - [3]赵龙,张云华.基于微服务理论的大中型医院门诊信息服务系统的设计与实现[J].软件工程,2019,22(08):31-33.DOI:10.19644/j.cnki.issn2096-1472.2019.08.010.
      - [4]李玉亮. 基于Spring Cloud的多语言问卷系统的设计与实现[D].中央民族大学,2021.DOI:10.27667/d.cnki.gzymu.2021.00014`3.
      - [5]刘佩妮. 自适应微服务系统软件体系结构的研究与实现[D].国防科技大学,2018.DOI:10.27052/d.cnki.gzjgu.2018.000623.
- ## DONE 开题报告
  collapsed:: true
  - [怎么写学位论文的开题报告_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1YE411p7HS/)
    collapsed:: true
    - {{video https://www.bilibili.com/video/BV1YE411p7HS}}
  - [课题开题报告与研究方案的撰写方法 - 教育科学研究网](http://jykxyj.com/nd.jsp?id=208)
  - [本科毕设，导师说我没创新、体现不出工作量说我毕不了业怎么办？ - 知乎](https://www.zhihu.com/question/458187448)
  - [毕设做的太简单会挂吗？ - 知乎](https://www.zhihu.com/question/387075635)
- ## DONE Paper
  collapsed:: true
  - **Format**
    - #### [内蒙古大学本科毕业论文(设计)撰写规范（试行）-内蒙古大学教务处 (imu.edu.cn)](https://uaa.imu.edu.cn/info/1026/1271.htm)
    - #### 三线表
    - #### Cite
      collapsed:: true
      - 就 [[software/engineering]] 而言，还是使用 IEEE 比较合适吧，因为是工科。 #STEM
      - APA (American Psychological Association) 是美国心理学，常用在教育、教育心理学中；
      - MLA (Modern Language Association) 是现代语言学，用在人文学中；
      - Chicago/Turabian是商业、历史、和艺术；
      - Vancouver 用于健康和物理学中；
      - Harvard用于人文、行为、哲学中；
      - [Overview - Citation Styles: APA, MLA, Chicago, Turabian, IEEE - Guides at University of Pittsburgh](https://pitt.libguides.com/citationhelp)
      - [论文的参考文献怎样标注？ - 知乎](https://www.zhihu.com/question/319857603)
  -
  - ### 查重 #[[navigation]]
    - [“中国知网”学位论文管理系统](https://pmlc.cnki.net/)
      collapsed:: true
      - https://pmlc.cnki.net/user/Help/知网大学生论文检测系统使用手册（学生）-2022年3月版.pdf
    - [知网查重-知网个人查重服务 (cnki.net)](https://cx.cnki.net/#/login)
      collapsed:: true
      - [上热搜！知网开放个人查重，1.5元/千字！研究生学位论文免费查3次 | 每经网](http://www.nbd.com.cn/articles/2022-06-12/2318324.html)
    - [学信网 • 万方数据文献相似性检测服务系统 (wanfangtech.net)](https://chsi.wanfangtech.net/)
    - [笔杆网_论文检测_论文查重_毕业论文抄袭检测 (bigan.net)](https://www.bigan.net/)
    - [PaperPass官网-论文查重-论文降重-论文检测-免费论文查重检测系统](https://www.paperpass.com/)
  - **Cite Format**
    - [Online BibTeX to IEEE converter - BibTeX.com](https://www.bibtex.com/c/bibtex-to-ieee-converter/)
- ## Leyou: notes
  collapsed:: true
  - ### SpringBoot
    - [Thymeleaf](https://www.thymeleaf.org/)
      description:: a modern server-side Java template engine for both web and standalone environments.
      - 类似
        - ~~JSP~~
        - Velocity
        - FreeMarker
      - 特性
        - 动静结合
          - Thymeleaf 在有网络和无网络的环境下皆可运行，即它可以让美工在浏览器查看页面的静态效果，也可以让程序员在服务器查看带数据的动态页面效果。这是由于它支持 html 原型，然后在 html 标签里增加额外的属性来达到模板+数据的展示方式。浏览器解释 html 时会忽略未定义的标签属性，所以 thymeleaf 的模板可以静态地运行；当有数据返回到页面时，Thymeleaf 标签会动态地替换掉静态内容，使页面动态显示。
        - 开箱即用
          - 它提供标准和spring标准两种方言，可以直接套用模板实现JSTL、 OGNL表达式效果，避免每天套模板、该jstl、改标签的困扰。同时开发人员也可以扩展和创建自定义的方言。
        - 多方言支持
          - Thymeleaf 提供spring标准方言和一个与 SpringMVC 完美集成的可选模块，可以快速的实现表单绑定、属性编辑器、国际化等功能。
        - SpringBoot提供了Thymeleaf的默认配置，并且为Thymeleaf设置了视图解析器，我们可以像以前操作jsp一样来操作Thymeleaf。代码几乎没有任何区别，就是在模板语法上有区别
      - 示例
        - 编写接口
          - ```java
            @GetMapping("/all")
            public String all(ModelMap model) {
                List<User> users = this.userService.queryAll();
                model.addAttribute("users", users);// 放入模型
                return "users"; // 返回模板名称
              	// 即 classpath:/templates/ 目录下的 html 文件名
            }
            ```
        - 引入启动器
          - ==SpringBoot会自动为Thymeleaf注册一个视图解析器 `ThymeleafViewResolver`==
          - Thymeleaf也会根据前缀和后缀来确定模板文件的位置
            - 默认前缀：`classpath:/templates/`
            - 默认后缀：`.html`
  -
  - ### 认识微服务
    - 架构演变（集中式 -> 垂直 -> 分布式 -> 面向服务 -> 微服务）
      collapsed:: true
      - |架构模式|场景|缺点|
        |集中式| 网站流量小；[:br]打包部署降低节点（成本）；[:br]ORM 是项目的核心 | 代码耦合，维护困难；[:br]业务优化困难；[:br]无法水平扩展；[:br]容错率低，并发差|
        |垂直拆分|业务分离分散流量 + 并发；[:br]针对业务进行优化；[:br]支持水平拓展、负载均衡；[:br]容错率较好；[:br]核心业务成为服务中心|重复系统的复用、开发效率较低|
        |分布式|提高业务复用（基础服务）；[:br]分布式调用与开发效率提高|耦合度反而变高；[:br]调用关系错综复杂，难以维护|
        |面向服务[:br]服务治理[:br]    Dubbo|服务太多导致的地址管理、[:br]调用关系梳理、[:br]服务状态动态调整等问题[:br]集群利用率有待提高|服务间会有依赖关系，出现问题，影响较大[:br]关系复杂，运维、测试部署困难，不符合DevOps思想|
        |微服务|单一职责[:br]拆分粒度小[:br]面向服务[:br]独立自治（团队、技术[:br]数据库、部署）||
      - 服务治理包括：
        collapsed:: true
        - 注册中心：服务自动注册和发现，无需人为记录服务地址
        - 自动订阅：服务列表自动推送，服务调用透明化，无需关心依赖关系
        - 动态监控服务：提供状态监控报告，人为控制服务状态
    - 远程调用实现 
      collapsed:: true
      - RPC：Remote Produce Call （RMI: Remote Method Call）
        - TCP based
        - 自定义数据格式
        - 允许运行于一台计算机的程序调用另一台计算机的子程序 
          collapsed:: true
          - 远程调用
            collapsed:: true
            - 采用何种网络通讯协议？
              collapsed:: true
              - TCP
            - 数据传输的格式怎样？
              collapsed:: true
              - 请求和响应
              - 序列化
          - 效果比拟本地调用
            collapsed:: true
            - RPC一定要对调用的过程进行封装
        - TODO [自己动手实现RPC](https://legacy.gitbook.com/book/huge0612/tour-of-rpc/details)
        - 典型框架
          collapsed:: true
          - webservice
          - dubbo
      - HTTP
        - TCP based
        - 规定了数据传输的格式
        - 局限
          collapsed:: true
          - 消息封装臃肿
        - RPC需要满足像调用本地服务一样调用远程服务，也就是对调用过程在API层面进行封装。Http协议没有这样的要求，因此请求、响应等细节需要我们自己去实现。
        - RPC方式更加透明，对用户更方便。Http方式更灵活，没有规定API和语言，跨语言、跨平台
        - RPC方式需要在API层面进行封装，限制了开发的语言环境。
        - 例如我们通过浏览器访问网站，就是通过Http协议
          collapsed:: true
          - 浏览器把请求封装，发起请求以及接收响应，解析响应的事情都帮我们做了
          - 如果是不通过浏览器，那么这些事情都需要自己去完成
      - #+BEGIN_IMPORTANT
        要效率，选 RPC；要灵活，选HTTP
        #+END_IMPORTANT
    - HttpClient?
    - 微服务要解决的问题（类似分布式）
      collapsed:: true
      - IP Address 硬编码到代码中；
      - Consumer 需要记忆 Producter 的 Address；
      - Producter 不是集群，不具备高可用性；
        - 即便形成了集群，但还是需要实现负载均衡；
      - 换个角度，抽象一下，即：
        - 服务管理
          - 自动注册和发现
          - 状态监管
          - 动态路由
        - 负载均衡
        - 容灾问题
        - 统一配置
    - Eureka 注册中心
      collapsed:: true
      - 组成部分
        - 服务注册中心：对外暴露自己的地址
        - 提供者：启动后向Eureka注册自己信息（地址，提供什么服务）
        - 消费者：向Eureka订阅服务，Eureka会将对应服务的所有提供者地址列表发送给消费者，并且定期更新
        - 心跳(续约)：提供者定期通过http方式向Eureka刷新自己的状态
      - 引入方法 
        - 服务器添加 `Eureka` 以后，在应用启动类中添加 `@EnableEurekaServer` 声明是一个 EurekaServer；再添加 Eureka 配置文件，包含端口、集群地址 `service-url` 和一些注册与订阅的配置。
          - `register-with-eureka`(注册信息到EurekaServer) 和 `fetch-registry`(拉取其它服务的信息) 默认为 True，因为只存在一台注册中心，所以无需告知自己的位置，应设置为 False
            id:: 646b638f-2553-4ecc-b243-56449d2c535a
        - 客户端添加 Spring Cloud 依赖`spring-cloud-dependencies` 和Eureka 客户端依赖 `spring-cloud-starter-netflix-eureka-client`；再在客户端启动类中添加 `@EnableDiscoveryClient` 开启客户端功能；这么些相关配置，包括 Eureka 实例的集群地址、与发现策略（IP）
          - ```java
            public List<User> queryUserByIds(List<Long> ids) {
              List<User> users = new ArrayList<>();
              List<ServiceInstance> instances = discoveryClient.getInstances("user-service");
              // 因为只有一个UserService,因此我们直接get(0)获取
              ServiceInstance instance = instances.get(0);
              // 获取ip和端口信息
              String baseUrl = "http://"+instance.getHost() + ":" + instance.getPort()+"/user/";
              //......
              return users;
            }
            ```
      - 高可用性：组建集群
        collapsed:: true
        - 数据同步：机器之间互相同步；
        - 要满足高可用性，就需要暴露自己的位置，即下述的设计就会失效；
          - ((646b638f-2553-4ecc-b243-56449d2c535a))
      - 服务注册与续约 (`eureka.client.register-with-erueka`)
        - 向EurekaServer发起一个Rest请求，并携带自己的元数据信息
        - Eureka Server会把这些信息保存到一个双层Map结构中
          collapsed:: true
          - 第一层Map的Key就是服务名称
          - 第二层Map的key是服务的实例id
        - 注册服务完成以后，Producter 会维持一个心跳
          collapsed:: true
          - 定时向EurekaServer发起Rest请求，表示自己没有宕机，服务的续约 (renew)；
        - 续约：配置
          collapsed:: true
          - ```yaml
            eureka:
              instance:
                lease-expiration-duration-in-seconds: 90
                lease-renewal-interval-in-seconds: 30
            # 默认情况下每个30秒服务会向注册中心发送一次心跳，证明自己还活着。
            # 如果超过90秒没有发送心跳，EurekaServer就会认为该服务宕机，会移除该服务
            ```
      - 实例id
        - UP(1)：代表现在是启动了1个示例，没有集群
        - DESKTOP-2MVEC12:user-service:8081：是示例的名称（instance-id），
          collapsed:: true
          - ```yaml
            eureka:
              instance:
                instance-id: ${spring.application.name}:${server.port}
            # default: ${hostname} + ${spring.application.name} + ${server.port}
            ```
      - `eureka.client`
        collapsed:: true
        - 获取服务列表 `fetch-registry`
          - 每隔 30 s 重新获取并更新数据
            collapsed:: true
            - ```yaml
              eureka:
                client:
                  registry-fetch-interval-seconds: 30
              ```
        - 失效剔除 `eviction-interval-timer-in-ms`
          - #+BEGIN_NOTE
            开发环境应该越小越好；
            #+END_NOTE
        - 自我保护 `enable-self-preservation`
          - #+BEGIN_NOTE
            开发环境应最好关闭；
            #+END_NOTE
          - `eviction-interval-timer-in-ms: 1000`：扫描失效服务的间隔时间（缺省为60*1000ms）
    - Robbin 负载均衡 (by Netflix)
      collapsed:: true
      - 有助于控制HTTP和TCP客户端的行为。为Ribbon 配置服务提供者地址列表后，Ribbon就可基于某种负载均衡算法，自动地帮助服务消费者去请求。Ribbon默认为我们提供了很多的负载均衡算法，例如轮询、随机等。当然，我们也可为Ribbon实现自定义的负载均衡算法。
      - 引入
        collapsed:: true
        - `restTemplate` 的作用？
        - ```java
          public List<User> queryUserByIds(List<Long> ids) {
            List<User> users = new ArrayList<>();
            // 地址直接写服务名称即可
            String baseUrl = "http://user-service/user/";
            ids.forEach(id -> {
                // 我们测试多次查询，
                users.add(this.restTemplate.getForObject(baseUrl + id, User.class));
                // 每次间隔500毫秒
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            });
            return users;
          }
          ```
        - `LoadBalancerInterceptor`??
        - 负载均衡策略?
        - 重试机制
    - [Hystix](https://github.com/Netflix/Hystrix/) 熔断 (by Netflix)
      description:: 容错管理工具，通过隔离、控制服务从而对延迟和故障提供更强大的容错能力，避免整个系统（级联失败）被拖垮。
      - 工作机制
        - Hystrix 使用自己的线程池，和主应用服务器线程池隔离
          - 如果调用花费很长时间，会停止调用
        - 服务调用方判断某些服务反应慢或者存在大量超时的情况时，能够主动熔断，防止整个系统被拖垮。
        - Hystrix可以实现弹性容错，当情况好转之后，可以自动重连
        - 通过断路的方式，可以将后续请求直接拒绝掉，一段时间之后允许部分请求通过，如果调用成功则回到电路闭合状态，否则继续断开
      - 引入 (`spring-cloud-starter-netflix-hystrix`)
        - `@HystrixCommand(fallbackMethod="queryUserByIdFallback")`
          - 声明一个失败回滚处理函数queryUserByIdFallback
            - 当queryUserById执行超时（默认是1000毫秒），就会执行fallback函数，返回错误提示。
      - 超时时间 (`hystrix.command.default.execution.isolation.thread.timeoutInMilliseconds`)
    - [Feign](https://github.com/OpenFeign/feign) Web Service 客户端 (by Netflix)
      description:: 声明式、模板化的HTTP客户端，用于更快捷地调用 HTTP API。
      - 工作原理
        - Feign 隐藏 Rest 请求，伪装成类似 SpringMVC 的 Controller
          - 不用再自己拼接url，拼接参数等等操作，一切都交给Feign去做。
          - Spring Cloud 让 Feign 支持了 SpringMVC，并整合了 Eureka 和 Ribbon，让其更加方便。
      - 导入 (`spring-cloud-starter-openfeign`)
        - Spring Cloud 中使用 Feign，需要在接口上方添加注释；
          - ```java
            @FeignClient("user-service")
            public interface UserFeignClient {
              @GetMapping("/user/{id}")
              User queryUserById(@PathVariable("id") Long id);
            }
            ```
        - 替代 DAO 层
          - 之前
            - ```java
              String baseUrl = "http://user-service/user/";
              User user = this.restTemplate.getForObject(baseUrl + id, User.class)
              ```
          - Feign会通过动态代理，帮我们生成实现类
            - 类似 mybatis 的 mapper
          - `@FeignClient`，声明这是一个Feign客户端，类似`@Mapper`注解。同时通过`value`属性指定服务名称
          - 接口中的定义方法，完全采用SpringMVC的注解，Feign会根据注解帮我们生成URL，并访问获取结果
        - ```java
          @SpringBootApplication
          @EnableDiscoveryClient
          @EnableHystrix
          @EnableFeignClients // 开启Feign功能
          public class UserConsumerDemoApplication {
              public static void main(String[] args) {
                  SpringApplication.run(UserConsumerDemoApplication.class, args);
              }
          }
          ```
          - Feign 中已经自动集成了 Ribbon 负载均衡，因此我们不需要自己定义 RestTemplate 了
      - 负载均衡 powered by Ribbon
        - 支持 全局配置(`ribbon.xx`) 和 服务配置(`service.ribbon.xx`)；
      - 服务熔断 powered by Hystix
        - Fallback 在注解中指定 Fallbak 处理函数
          - ```java
            @FeignClient(value = "user-service", fallback = UserFeignClientFallback.class)
            public interface UserFeignClient {
              //...
            }
            ```
      - 请求压缩？
      - 日志级别？
    - [Zuul](https://github.com/Netflix/zuul) 网关 (by Netflix)
      - 网关解决的问题（直接对外暴露服务接口可能出现的问题）： 
        - 无法保证 “服务无状态”
          - 开放服务的权限控制机制将会贯穿并污染整个开放服务的业务逻辑
        - 无法复用 既有接口
          - 不得不通过在原有接口上增加校验逻辑，或增加一个代理调用来实现权限控制，无法直接复用原有的接口。
      - Zuul的核心是一系列的过滤器，这些过滤器可以完成以下功能。
        - 身份认证与安全
          - 识别每个资源的验证要求，并拒绝那些与要求不符的请求。
        - 审查与监控
          - 在边缘位置追踪有意义的数据和统计结果，从而带来精确的生产视图。
        - 动态路由
          - 动态地将请求路由到不同的后端集群。
        - 压力测试
          - 逐渐增加指向集群的流量，以了解性能。
        - 负载分配
          - 为每一种负载类型分配对应容量，并弃用超出限定值的请求。
        - 静态响应处理
          - 在边缘位置直接建立部分响应，从而避免其转发到内部集群。
        - 多区域弹性
          - 跨越AWS Region进行请求路由，旨在实现ELB（Elastic Load Balancing） 使用的多样化，以及让系统的边缘更贴近系统的使用者。
      - Spring Cloud 对Zuul进行了整合与增强
        - Zuul 使用的默认 HTTP 客户端是 Apache HTTP Client，也可以使用RestClient (`ribbon.okhttp.enabled=true`) 或者 okhttp3.OkHttpClient (`ribbon.restclient.enabled＝true`)
      - ![1525675648881.png](C:\Users\15517\Desktop\review\乐优商城《项目笔记》\day03笔记\assets\1525675648881.png)
      - 导入
        - ```java
          @EnableZuulProxy // 开启Zuul的网关功能
          ```
        - ```yaml
          zuul:
            routes:
              user-service: # 这里是路由id，随意写
                path: /user-service/** # 这里是映射路径
                url: http://127.0.0.1:8081 # 映射路径对应的实际url
          ```
      - 路由配置？
        - 简化
        - 默认
      - 路由前缀？
      - 过滤器
        - ZuulFilter
          - ```java
            public apublic abstract ZuulFilter implements IZuulFilter{
              abstract public String filterType();
              // 返回字符串，代表过滤器的类型。包含以下4种
              // `pre`：请求在被路由之前执行
              // `routing`：在路由请求时调用
              // `post`：在routing和errror过滤器之后调用
              // `error`：处理请求时发生错误调用
              abstract public int filterOrder();
              // 通过返回的int值来定义过滤器的执行顺序
              // 数字越小优先级越高
              boolean shouldFilter();// 来自IZuulFilter
              //返回一个Boolean值判断该过滤器是否需要执行。
              // 返回true执行，返回false不执行。
              Object run() throws ZuulException;// IZuulFilter
              // 过滤器的具体业务逻辑。
            }
            ```
        - 过滤器执行生命周期
          - ![🖼 ](C:\Users\15517\Desktop\review\乐优商城《项目笔记》\day03笔记\assets\1525681866862.png)
          - 正常流程：
            - 请求到达首先会经过pre类型过滤器，而后到达routing类型，进行路由，请求就到达真正的服务提供者，执行请求，返回结果后，会到达post过滤器。而后返回响应。
          - 异常流程：
            - 整个过程中，pre或者routing过滤器出现异常，都会直接进入error过滤器，再error处理完毕后，会将请求交给POST过滤器，最后返回给用户。
            - 如果是error过滤器自己出现异常，最终也会进入POST过滤器，而后返回。
            - 如果是POST过滤器出现异常，会跳转到error过滤器，但是与pre和routing不同的时，请求不会再到达POST过滤器了。
        - 使用场景
          - 请求鉴权：一般放在pre类型，如果发现没有访问权限，直接就拦截了
          - 异常处理：一般会在error类型和post类型过滤器中结合来处理。
          - 服务调用时长统计：pre和post结合使用。
        - 自定义
          - ```java
            @Component
            public class LoginFilter extends ZuulFilter{
              @Override
              public String filterType() {
                // 登录校验，肯定是在前置拦截
                return "pre";
              }
              @Override
              public int filterOrder() {
                // 顺序设置为1
                return 1;
              }
              @Override
              public boolean shouldFilter() {
                // 返回true，代表过滤器生效。
                return true;
              }
              @Override
              public Object run() throws ZuulException {
                // 登录校验逻辑。
                // 1）获取Zuul提供的请求上下文对象
                RequestContext ctx = RequestContext.getCurrentContext();
                // 2) 从上下文中获取request对象
                HttpServletRequest req = ctx.getRequest();
                // 3) 从请求中获取token
                String token = req.getParameter("access-token");
                // 4) 判断
                if(token == null || "".equals(token.trim())){
                  // 没有token，登录校验失败，拦截
                  ctx.setSendZuulResponse(false);
                  // 返回401状态码。也可以考虑重定向到登录页。
                  ctx.setResponseStatusCode(HttpStatus.UNAUTHORIZED.value());
                }
                // 校验通过，可以考虑把用户信息放入上下文，继续向后执行
                return null;
              }
            }
            ```
        - 负载均衡和熔断（Zuul 内置 Ribbon 和 Hystix）
          - ```yaml
            zuul:
              retryable: true
            ribbon:
              ConnectTimeout: 250 # 连接超时时间(ms)
              ReadTimeout: 2000 # 通信超时时间(ms)
              OkToRetryOnAllOperations: true # 是否对所有操作重试
              MaxAutoRetriesNextServer: 2 # 同一服务不同实例的重试次数
              MaxAutoRetries: 1 # 同一实例的重试次数
            hystrix:
              command:
              	default:
                    execution:
                      isolation:
                        thread:
                          timeoutInMillisecond: 6000 # 熔断超时时长：6000ms
            ```
  - ### 商城搭建
    - 背景
      - 项目分类
        - |项目|传统项目|互联网项目|
          |----|----|----|
          |需求方|公司、企业用户|普通用户|
          |盈利模式|项目本身卖钱|虚拟货币、增值服务、广告收益...|
          |技术侧重点|业务功能|网站性能、业务功能|
      - 技术导向
        - 技术范围广
        - 技术新
        - 高并发（分布式、静态化技术、缓存技术、异步并发、池化、队列）
        - 高可用（集群、负载均衡、限流、降级、熔断）
        - 数据量大
        - 业务复杂
        - 数据安全
      - 常见的模式
        - B2C：商家对个人，如：亚马逊、当当等
        - C2C：个人对个人，如：咸鱼、拍拍网、ebay
        - B2B：商家对商家，如：阿里巴巴、八方资源网等
        - O2O：线上和线下结合，如：饿了么、电影票、团购等
        - P2P：在线金融，贷款，如：网贷之家、人人聚财等。
        - B2C：天猫、京东、一号店等
      - 术语
        - SaaS：软件即服务
        - SOA：面向服务
        - RPC：远程过程调用
        - RMI：远程方法调用
        - PV：(page view)，页面浏览量
          - 用户每1次对网站中的每个网页访问均被记录1次。
          - 用户对同一页面的多次访问，访问量累计
        - UV：(unique visitor)，独立访客
          - 指访问某个站点或点击某条新闻的不同IP地址的人数。在同一天内，uv只记录第一次进入网站的具有独立IP的访问者，在同一天内再次访问该网站则不计数。
        - PV与带宽：
          - 计算带宽大小需要关注两个指标：峰值流量和页面的平均大小。
          - 计算公式是：网站带宽= ( PV * 平均页面大小（单位MB）* 8 )/统计时间（换算到秒）
          - 为什么要乘以8？
            - 网站大小为单位是字节(Byte)，而计算带宽的单位是bit，1Byte=8bit
          - 这个计算的是平均带宽，高峰期还需要扩大一定倍数
        - PV、QPS、并发
          - QPS：每秒处理的请求数量。8000/s
          - 比如你的程序处理一个请求平均需要0.1S，那么1秒就可以处理10个请求。QPS自然就是10，多线程情况下，这个数字可能就会有所增加。
          - 由PV和QPS如何需要部署的服务器数量？
            - 根据二八原则，80%的请求集中在20%的时间来计算峰值压力：
            - （每日PV * 80%） / （3600s * 24 * 20%） * 每个页面的请求数  = 每个页面每秒的请求数量
          - 然后除以服务器的QPS值，即可计算得出需要部署的服务器数量
    - 内容
      - 预期
        - 乐优商城是一个全品类的电商购物网站（B2C）。
        - 用户可以在线购买商品、加入购物车、下单、秒杀商品
        - 可以品论已购买商品
        - 管理员可以在后台管理商品的上下架、促销活动
        - 管理员可以监控商品销售状况
        - 客服可以在后台处理退款操作
        - 希望未来3到5年可以支持千万用户的使用
      - ![](C:\Users\15517\Desktop\review\乐优商城《项目笔记》\day04笔记\assets\1525703759035.png)
        - 后台管理：
          - 后台系统主要包含以下功能：
            - 商品管理，包括商品分类、品牌、商品规格等信息的管理
            - 销售管理，包括订单统计、订单退款处理、促销活动生成等
            - 用户管理，包括用户控制、冻结、解锁等
            - 权限管理，整个网站的权限控制，采用JWT鉴权方案，对用户及API进行权限控制
            - 统计，各种数据的统计分析展示
          - 后台系统会采用前后端分离开发，而且整个后台管理系统会使用Vue.js框架搭建出单页应用（SPA）。
        - 前台门户
          - 前台门户面向的是客户，包含与客户交互的一切功能。例如：
            - 搜索商品
            - 加入购物车
            - 下单
            - 评价商品等等
          - 前台系统我们会使用Thymeleaf模板引擎技术来完成页面开发。出于SEO优化的考虑，我们将不采用单页应用。
        - 无论是前台还是后台系统，都共享相同的微服务集群，包括：
          - 商品微服务：商品及商品分类、品牌、库存等的服务
          - 搜索微服务：实现搜索功能
          - 订单微服务：实现订单相关
          - 购物车微服务：实现购物车相关功能
          - 用户中心：用户的登录注册等功能
          - Eureka注册中心
          - Zuul网关服务
          - Spring Cloud Config配置中心
    - 搭建
      - 创建父工程
      - 创建EurekaServer
      - 创建Zuul网关
      - 创建商品微服务
        - `ly-item` 是一个微服务，将来肯定会有其它系统需要来调用服务中提供的接口，当然也有接口中关联的实体类
          - 使用聚合工程，将要提供的接口及相关实体类放到独立子工程中，以后别人引用的时候，只需要知道坐标即可
          - ly-item中 创建两个子工程：
            - ly-item-interface
              - 主要是对外暴露的接口及相关实体类
            - ly-item-service
              - 所有业务逻辑及内部使用接口
          - ![](C:\Users\15517\Desktop\review\乐优商城《项目笔记》\day04笔记\assets\1525744281610.png)
  - ### Vue 入门
    - ES6 语法
    - Webpack
    - 跨域问题
      - 跨域不一定会有跨域问题。
        - 因为跨域问题是浏览器对于ajax请求的一种安全限制
          - **一个页面发起的ajax请求，只能是于当前页同域名的路径**，这能有效的阻止跨站攻击。
          - 因此：**跨域问题 是针对ajax的一种限制**。
      - **解决跨域问题的方案**
        - Jsonp
          - 最早的解决方案，利用script标签可以跨域的原理实现。
          - 限制：
            - 需要服务的支持
            - 只能发起GET请求
        - nginx反向代理
          - 思路是：利用nginx反向代理把跨域为不跨域，支持各种请求方式
          - 缺点：需要在nginx进行额外配置，语义不清晰
        - CORS (Cross-origin resource sharing)，跨域资源共享
          description:: W3C标准，它允许浏览器向跨源服务器，发出[`XMLHttpRequest`](http://www.ruanyifeng.com/blog/2012/09/xmlhttprequest_level_2.html)请求，从而克服了AJAX只能[同源](http://www.ruanyifeng.com/blog/2016/04/same-origin-policy.html)使用的限制。CORS需要浏览器（IE10以下不行）和服务器同时支持。
          - 原理
            - 浏览器将 ajax 请求分为两类
              - 简单请求
                collapsed:: true
                - 浏览器判断
                  - 请求方法是以下三种方法之一：
                    collapsed:: true
                    - HEAD
                    - GET
                    - POST
                  - HTTP的头信息不超出以下几种字段：
                    collapsed:: true
                    - Accept
                    - Accept-Language
                    - Content-Language
                    - Last-Event-ID
                    - Content-Type：只限于三个值`application/x-www-form-urlencoded`、`multipart/form-data`、`text/plain`
                  - If true:
                    collapsed:: true
                    - 在请求头中携带一个字段：`Origin` （协议+域名+端口）
                  - Else: 特殊请求
                - 服务器判断跨域
                  - If  true:
                    collapsed:: true
                    - 在返回的响应头中携带下面信息：
                      - ```html
                        Access-Control-Allow-Origin: http://manage.leyou.com
                        <!-- 可接受的域，具体域名 / * -->
                        Access-Control-Allow-Credentials: true
                        <!-- 是否允许携带cookie, 默认为 False
                        True 的话必须指定域名，不能为 * -->
                        Content-Type: text/html; charset=utf-8
                        ```
                    -
              - 特殊请求， 如 PUT
                collapsed:: true
                - 预检请求（preflight）
                  - 特殊请求会在正式通信之前，增加一次HTTP查询请求，称为"预检"请求
                  - 一个“预检”请求的样板：
                    ```http
                    OPTIONS /cors HTTP/1.1
                    Origin: http://manage.leyou.com
                    Access-Control-Request-Method: PUT
                    Access-Control-Request-Headers: X-Custom-Header
                    Host: api.leyou.com
                    Accept-Language: en-US
                    Connection: keep-alive
                    User-Agent: Mozilla/5.0...
                    ```
                    与简单请求相比，除了Origin以外，多了两个头：
                  - Access-Control-Request-Method：接下来会用到的请求方式，比如PUT
                  - Access-Control-Request-Headers：会额外用到的头信息
                    > 预检请求的响应
                    服务的收到预检请求，如果许可跨域，会发出响应：
                    ```http
                    HTTP/1.1 200 OK
                    Date: Mon, 01 Dec 2008 01:15:39 GMT
                    Server: Apache/2.0.61 (Unix)
                    Access-Control-Allow-Origin: http://manage.leyou.com
                    Access-Control-Allow-Credentials: true
                    Access-Control-Allow-Methods: GET, POST, PUT
                    Access-Control-Allow-Headers: X-Custom-Header
                    Access-Control-Max-Age: 1728000
                    Content-Type: text/html; charset=utf-8
                    Content-Encoding: gzip
                    Content-Length: 0
                    Keep-Alive: timeout=2, max=100
                    Connection: Keep-Alive
                    Content-Type: text/plain
                    ```
                    除了`Access-Control-Allow-Origin`和`Access-Control-Allow-Credentials`以外，这里又额外多出3个头：
                  - Access-Control-Allow-Methods：允许访问的方式
                  - Access-Control-Allow-Headers：允许携带的头
                  - Access-Control-Max-Age：本次许可的有效时长，单位是秒，**过期之前的ajax请求就无需再次进行预检了**
                  - 如果浏览器得到上述响应，则认定为可以跨域，后续就跟简单请求的处理是一样的了。
          - 服务端：
            - CORS通信与AJAX没有任何差别，因此你不需要改变以前的业务逻辑。只不过，浏览器会在请求中携带一些头信息，我们需要以此判断是否运行其跨域，然后在响应头中加入一些信息即可。这一般通过过滤器完成即可。
          - 规范化的跨域请求解决方案，安全可靠。
          - 优势：
            - 在服务端进行控制是否允许跨域，可自定义规则
            - 支持各种请求方式
          - 缺点：
            - 会产生额外的请求
            - 我们这里会采用cors的跨域方案。
    - 分页和过滤
  - ### [Nginx](https://www.nginx.com/)
    - Nginx是一个高性能的Web和反向代理服务器，它具有有很多非常优越的特性：
      - 作为Web服务器
        - 相比Apache，Nginx使用更少的资源，支持更多的并发连接，体现更高的效率，这点使Nginx尤其受到虚拟主机提供商的欢迎。能够支持高达50，000个并发连接数的响应，感谢Nginx为我们选择了 epoll and kqueue 作为开发模型.
      - 作为负载均衡服务器
        - Nginx既可以在内部直接支持Rails和PHP，也可以支持作为HTTP代理服务器 对外进行服务。Nginx用C编写，不论是系统资源开销还是CPU使用效率都比
          Perlbal 要好的多。
      - 作为邮件代理服务器
        - Nginx同时也是一个非常优秀的邮件代理服务器（最早开发这个产品的目的之一也是作为邮件代理服务器），Last.fm描述了成功并且美妙的使用经验。
      - Nginx 安装非常的简单，配置文件 非常简洁（还能够支持perl语法），Bugs非常少的服务器：Nginx启动特别容易，并且几乎可以做到7＊24不间断运行，即使运行数个月也不需要重新启动。你还能够在 不间断服务的情况下进行软件版本的升级。
    - NIO (not-blocking-io)：非阻塞IO
    - BIO (blocking-io)： 阻塞IO
    - 操作
      - ```shell
        start nginx
        nginx -s stop
        nginx -s reload
        ```
    - 配置
      - ```shell
        server { # 每个server就是一个反向代理配置
        	listen       80; 	     # 监听端口
            server_name  api.llh.com; # 监听域名
            # 头信息
            proxy_set_header Host $host;
            proxy_set_header X-Forwarded-Host $host;
            proxy_set_header X-Forwarded-Server $host;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        	location / {
        		proxy_pass http://127.0.0.1:10010; # 代理转发
        		proxy_connect_timeout 600;
        		proxy_read_timeout 600;
        	}
        }
        ```
  - ### 品牌管理
  - ### 商品规格管理
  - ### 商品管理
  - ### Elastic Search
    - [欢迎来到 Elastic — Elasticsearch 和 Kibana 的开发者 | Elastic](https://www.elastic.co/cn/)
      - Elastic有一条完整的产品线及解决方案：Elasticsearch、Kibana、Logstash等，前面说的三个就是大家常说的ELK技术栈。
      - Elasticsearch具备以下特点：
        - 分布式，无需人工搭建集群（solr就需要人为配置，使用Zookeeper作为注册中心）
        - Restful风格，一切API都遵循Rest原则，容易上手
        - 近实时搜索，数据更新在Elasticsearch中几乎是完全同步的。
    - kibana
      - Kibana是一个基于Node.js的Elasticsearch索引库数据统计工具，可以利用Elasticsearch的聚合功能，生成各种图表，如柱形图，线状图，饼图等。
      - 而且还提供了操作Elasticsearch索引数据的控制台，并且提供了一定的API提示，非常有利于我们学习Elasticsearch的语法。
    - 操作索引
      - Elasticsearch也是基于Lucene的全文检索库，本质也是存储数据，很多概念与MySQL类似的。
      - 对比关系：
        - 索引（indices）--------------------------------Databases 数据库
        -   类型（type）-----------------------------Table 数据表
        - 文档（Document）----------------Row 行
        - 字段（Field）-------------------Columns 列
        - | 概念 | 说明 |
          | -------------- | ---------------------------------------- |
          | 索引库（indices) | indices是index的复数，代表许多的索引，|
          | 类型（type） | 类型是模拟mysql中的table概念，一个索引库下可以有不同类型的索引，比如商品索引，订单索引，其数据格式不同。不过这会导致索引库混乱，因此未来版本中会移除这个概念 |
          | 文档（document） | 存入索引库原始的数据。比如每一条商品信息，就是一个文档|
          | 字段（field）| 文档中的属性 |
          | 映射配置（mappings） | 字段的数据类型、属性、是否索引、是否存储等特性|
      -
    - 搜索过滤
  - ### 商品详情
  - ### 静态化 (`leyou-goods-web`)
    - #+BEGIN_NOTE
      为什么不用缓存？比如 Redis
      #+END_NOTE
      - Redis 适合数据规模比较小的情况
        - 例如我们的商品详情页。每个页面如果10kb，100万商品，就是10GB空间，对内存占用比较大。此时就给缓存系统带来极大压力，如果缓存崩溃，接下来倒霉的就是数据库了
    - 思路
      - 先用模板引擎来生成，再保存到nginx服务器来部署，如：
        - Freemarker
        - Velocity
        - ==Thymeleaf==
    - 思路：Thymeleaf
      - Context：运行上下文
        - 用来保存模型数据，当模板引擎渲染时，可以从Context上下文中获取数据用于渲染。
        - 当与SpringBoot结合使用时，我们放入Model的数据就会被处理到Context，作为模板渲染的数据使用。
      - TemplateResolver：模板解析器
        - 用来读取模板相关的配置，例如：模板存放的位置信息，模板文件名称，模板文件的类型等等。
        - 当与SpringBoot结合时，TemplateResolver已经由其创建完成，并且各种配置也都有默认值，比如模板存放位置，其默认值就是：templates。比如模板文件类型，其默认值就是html。
      - TemplateEngine：模板引擎
        - 模板引擎：用来解析模板的引擎，需要使用到上下文、模板解析器。分别从两者中获取模板中需要的数据，模板文件。然后利用内置的语法规则解析，从而输出解析后的文件。来看下模板引擎进行处理的函数：
        - ```java
          templateEngine.process("模板名", context, writer);
          ```
        - 三个参数：
          - 模板名称
          - 上下文：里面包含模型数据
          - writer：输出目的地的流
        - 在输出时，我们可以指定输出的目的地，如果目的地是Response的流，那就是网络响应。如果目的地是本地文件，那就实现静态化了。
        - 而在SpringBoot中已经自动配置了模板引擎，因此我们不需要关心这个。现在我们做静态化，就是把输出的目的地改成本地文件即可！
      -
  - ### WAIT Rabbitmq及数据同步
    - RabbitMQ
    - WAITING 搜索服务、商品静态页的数据同步
    - 实现思路
      - 发送方：商品微服务
        - 什么时候发？
          - 当商品服务对商品进行写操作：增、删、改的时候，需要发送一条消息，通知其它服务
        - 发送什么内容？
          - 对商品的增删改时其它服务可能需要新的商品数据，但是如果消息内容中包含全部商品信息，数据量太大，而且并不是每个服务都需要全部的信息。因此我们**只发送商品id**，其它服务可以根据id查询自己需要的信息
        - 接收方：搜索微服务、静态页微服务
          - 接收消息后如何处理？
            - 搜索微服务：
              - 增/改：添加新的数据到索引库
              - 删：删除索引库数据
            - 静态页微服务：
              - 增：创建新的静态页
              - 删：删除原来的静态页
              - 改：创建新的静态页并删除原来的
  - ### 用户注册(`leyou-user`)
    - 基本逻辑：
      - 1）校验短信验证码
      - 2）生成盐
        - #+BEGIN_QUOTE
          我们通常会将用户的密码进行 Hash 加密，如果不加盐，即使是两层的 md5 都有可能通过彩虹表的方式进行破译。彩虹表就是在网上搜集的各种字符组合的 Hash 加密结果。而加盐，就是人为的通过一组随机字符与用户原密码的组合形成一个新的字符，从而增加破译的难度。就像做饭一样，加点盐味道会更好。
          — [什么叫给密码“加盐”？如何安全的为你的用户密码“加盐”？ - 知乎](https://zhuanlan.zhihu.com/p/144392745)
          #+END_QUOTE
      - 3）对密码加密
      - 4）写入数据库
      - 5）删除Redis中的验证码
    - 服务端数据校验：[Hibernate Validator](http://hibernate.org/validator/)
      - **hibernate Validator** 是 Bean Validation 的参考实现 。
        - Hibernate Validator 提供了 JSR 303 规范中所有内置 constraint（约束） 的实现，除此之外还有一些附加的 constraint。
        - 在日常开发中，Hibernate Validator经常用来验证bean的字段，基于注解，方便快捷高效
      - **Bean校验的注解**
        - | **Constraint** | **详细信息** |
          | -------------------------------------------------- | ------------------------------------------------------------ |
          | **@Valid** | 被注释的元素是一个对象，需要检查此对象的所有字段值 |
          | **@Null**| 被注释的元素必须为 null|
          | **@NotNull** | 被注释的元素必须不为 null|
          | **@AssertTrue**| 被注释的元素必须为 true|
          | **@AssertFalse** | 被注释的元素必须为 false |
          | **@Min(value)**| 被注释的元素必须是一个数字，其值必须大于等于指定的最小值 |
          | **@Max(value)**| 被注释的元素必须是一个数字，其值必须小于等于指定的最大值 |
          | **@DecimalMin(value)** | 被注释的元素必须是一个数字，其值必须大于等于指定的最小值 |
          | **@DecimalMax(value)** | 被注释的元素必须是一个数字，其值必须小于等于指定的最大值 |
          | **@Size(max, min)**| 被注释的元素的大小必须在指定的范围内 |
          | **@Digits (integer, fraction)**| 被注释的元素必须是一个数字，其值必须在可接受的范围内 |
          | **@Past**| 被注释的元素必须是一个过去的日期 |
          | **@Future**| 被注释的元素必须是一个将来的日期 |
          | **@Pattern(value)**| 被注释的元素必须符合指定的正则表达式 |
          | **@Email** | 被注释的元素必须是电子邮箱地址 |
          | **@Length**| 被注释的字符串的大小必须在指定的范围内 |
          | **@NotEmpty**| 被注释的字符串的必须非空 |
          | **@Range** | 被注释的元素必须在合适的范围内 |
          | **@NotBlank**| 被注释的字符串的必须非空 |
          | **@URL(protocol=,host=, port=,regexp=, flags=)** | 被注释的字符串必须是一个有效的url|
          | **@CreditCardNumber**| 被注释的字符串必须通过Luhn校验算法，银行卡，信用卡等号码一般都用Luhn计算合法性 |
    - [JWT](https://jwt.io) （Json Web Token）
      description:: JSON 风格轻量级的授权和身份认证规范，可实现无状态、分布式的Web应用授权
      - [GitHub - jwtk/jjwt: Java JWT: JSON Web Token for Java and Android](https://github.com/jwtk/jjwt)
      - 格式 
        - Header：头部，包含：
          - 声明类型，这里是JWT
          - 加密算法，自定义
          - 我们会对头部进行base64加密（可解密），得到第一部分数据
        - Payload：载荷，就是有效数据，包含：
          - 用户身份信息（注意，这里因为采用base64加密，可解密，因此不要存放敏感信息）
          - 注册声明：如token的签发时间，过期时间，签发人等
          - 这部分也会采用base64加密，得到第二部分数据
        - Signature：签名，是整个数据的认证信息。一般根据前两步的数据，再加上服务的的密钥（secret）（不要泄漏，最好周期性更换），通过加密算法生成。用于验证整个数据完整和可靠性
        - ![](C:\Users\15517\Desktop\review\乐优商城《项目笔记》\day17笔记\assets\1527322512370.png)
      - 交互流程 
        - 用户登录
        - 服务的认证，通过后根据 secret 生成token
        - 将生成的 token 返回给浏览器
        - 用户每次请求携带token
        - 服务端利用公钥解读jwt签名，判断签名有效后，从Payload中获取用户信息
        - 处理请求，返回响应结果
        - #+BEGIN_NOTE
          因为JWT签发的token中已经包含了用户的身份信息，并且每次请求都会携带，这样服务的就无需保存用户信息，甚至无需去数据库查询，完全符合了Rest的无状态规范。
          #+END_NOTE
    - 非对称加密
      description:: 对信息进行编码和解码的技术，编码是把原来可读信息（又称明文）译成代码形式（又称密文），其逆过程就是解码（解密）
      - 加密算法可以分为三类：
        - 对称加密，如AES
          - 基本原理：将明文分成N个组，然后使用密钥对各个组进行加密，形成各自的密文，最后把所有的分组密文进行合并，形成最终的密文。
          - 优势：算法公开、计算量小、加密速度快、加密效率高
          - 缺陷：双方都使用同样密钥，安全性得不到保证
        - 非对称加密，如RSA
          - 基本原理：同时生成两把密钥：私钥和公钥，私钥隐秘保存，公钥可以下发给信任客户端
            - 私钥加密，持有私钥或公钥才可以解密
            - 公钥加密，持有私钥才可解密
          - 优点：安全，难以破解
          - 缺点：算法比较耗时
        - 不可逆加密，如MD5，SHA
          - 基本原理：加密过程中不需要使用[密钥](https://baike.baidu.com/item/%E5%AF%86%E9%92%A5)，输入明文后由系统直接经过加密算法处理成密文，这种加密后的数据是无法被解密的，无法根据密文推算出明文。
      - RSA算法历史：
        - 1977年，三位数学家Rivest、Shamir 和 Adleman 设计了一种算法，可以实现非对称加密。这种算法用他们三个人的名字缩写：RSA
    - 结合 Zuul
      - 我们逐步演进系统架构设计。需要注意的是：secret是签名的关键，因此一定要保密，我们放到鉴权中心保存，其它任何服务中都不能获取secret。
      - ![](C:\Users\15517\Desktop\review\乐优商城《项目笔记》\day17笔记\assets\1527312464328.png)
        - 1、用户请求登录
        - 2、Zuul将请求转发到授权中心，请求授权
        - 3、授权中心校验完成，颁发JWT凭证
        - 4、客户端请求其它功能，携带JWT
        - 5、Zuul将jwt交给授权中心校验，通过后放行
        - 6、用户请求到达微服务
        - 7、微服务将jwt交给鉴权中心，鉴权同时解析用户信息
        - 8、鉴权中心返回用户数据给微服务
        - 9、微服务处理请求，返回响应
        - #+BEGIN_WARNING
          每次鉴权都需要访问鉴权中心，系统间的网络请求频率过高，效率略差，鉴权中心的压力较大。
          #+END_WARNING
      - ![](C:\Users\15517\Desktop\review\乐优商城《项目笔记》\day17笔记\assets\1527313765010.png)
        - 我们首先利用RSA生成公钥和私钥。私钥保存在授权中心，公钥保存在Zuul和各个微服务
        - 用户请求登录
        - 授权中心校验，通过后用私钥对JWT进行签名加密
        - 返回jwt给用户
        - 用户携带JWT访问
        - Zuul直接通过公钥解密JWT，进行验证，验证通过则放行
        - 请求到达微服务，微服务直接用公钥解析JWT，获取用户信息，无需访问授权中心
      -
        -
    - 创建授权中心
      - 用户鉴权：
        - 接收用户的登录请求，通过用户中心的接口进行校验，通过后生成JWT
        - 使用私钥生成JWT并返回
      - 服务鉴权：微服务间的调用不经过Zuul，会有风险，需要鉴权中心进行认证
        - 原理与用户鉴权类似，但逻辑稍微复杂一些（此处我们不做实现）4
      - ...
    - 网关的登录拦截器
      - 过滤器
        - 基本逻辑：
          - 获取cookie中的token
          - 通过JWT对token进行校验
          - 通过：则放行；不通过：则重定向到登录页
        - 白名单
          - ```yaml
            leyou:
              filter:
                allowPaths:
                  - /api/auth
                  - /api/search
                  - /api/user/register
                  - /api/user/check
                  - /api/user/code
                  - /api/item
            ```
  - ### 授权中心 (`leyou-auth-common`)
    - 无状态登录
      - 原理
        - 当客户端第一次请求服务时，服务端对用户进行信息认证（登录）
        - 认证通过，将用户信息进行加密形成token，返回给客户端，作为登录凭证
        - 以后每次请求，客户端都携带认证的token
        - 服务端对token进行解密，判断是否有效。
      - 状态
        description:: 服务端记录会话的客户端信息。从而识别客户端身份，再用于后续根据用户请求。
        - 有状态服务 （如 session ）
          - 缺点
            - 服务端保存大量数据，增加服务端压力
            - 服务端保存用户状态，无法进行水平扩展
            - 客户端请求依赖服务端，多次请求必须访问同一台服务器
        - 无状态服务 （如 token ）
          - 好处
            - 客户端请求不依赖服务端的信息，任何==多次请求不需要必须访问到同一台服务==
            - 服务端的集群和状态对客户端透明
            - 服务端可以任意的迁移和伸缩
            - 减小服务端存储压力
      - #+BEGIN_IMPORTANT
        加密：`JWT + RSA非对称加密`
        #+END_IMPORTANT
      -
      -
        -
  - ### WAIT 购物车
  - ### 下单
- ## Leyou: issues
  collapsed:: true
  - ```
    2023-04-01 13:09:47.327  WARN 9384 --- [nio-8081-exec-3] .w.s.m.s.DefaultHandlerExceptionResolver : Resolved [org.springframework.web.method.annotation.MethodArgumentTypeMismatchException: Failed to convert value of type 'java.lang.String' to required type 'java.lang.Long'; nested exception is java.lang.NumberFormatException: For input string: "swagger-ui.html"]
    2023-04-01 13:09:47.436  WARN 9384 --- [nio-8081-exec-4] .w.s.m.s.DefaultHandlerExceptionResolver : Resolved [org.springframework.web.method.annotation.MethodArgumentTypeMismatchException: Failed to convert value of type 'java.lang.String' to required type 'java.lang.Long'; nested exception is java.lang.NumberFormatException: For input string: "favicon.ico"]
    ```
  - https://796t.com/content/1546282827.html
  - 1 没有购物车数据库，没有持久化到数据库
  - 2 没有用户中心
  - 2.1 没有用户通知中心，它压根没有启动（消息队列）
  - 3 管理员只有一个人，一个人添加管理所有的产品
  - 3.1 参数表压根没有用，管理混乱。
  - 4 支付是一个问题
  - Proxy
    collapsed:: true
    - ```
      hosts:
        - 'zp.com':'127.0.0.1'
        - 'api.llh.com':'127.0.0.1'
        - 'www.llh.com':'127.0.0.1'
        - 'image.com':'127.0.0.1'
        - 'wg.com':'127.0.0.1'
      ```
- ## WAIT BV11N411Z7is （JWT??）
  collapsed:: true
  - ### [P2 锋迷商城项目互联网环境下问题分析](https://www.bilibili.com/video/BV11N411Z7is?p=2)
    collapsed:: true
    - 电商项目一定会有⾼并发访问的问题
    - **前端的高并发**访问？
      collapsed:: true
      - Nginx 集群负载均衡；
    - **后端接口的高并发**访问？
      collapsed:: true
      - Tomcat 集群负载均衡；
    - **数据库的并发访问**压力？
      collapsed:: true
      - Mycat 并发 Mysql 集群；
    - 业务处理
      collapsed:: true
      - ⾸⻚
        - **数据加载效率**
          - redis缓存
      - 商品搜索功能
        - 模糊查询（Like 数据库查询）
        - **查询效率低问题**
      - 订单查询
        - 订单的数据量会随着⽤户的增多⼤量增加
        - **查询效率低问题**
      - 商品购买
        - 分布并发访问 —— 产品超卖问题（事务锁）
          - redis分布式锁
    - SpringBoot 开发出来的商务系统其实问题是很多的，充其量当单体使用；
    - 架构问题
      collapsed:: true
      - 系统功能不断的增加
        - **单点故障问题**
    - 业务问题
      collapsed:: true
      - 登录功能
        - 缓存⽤户信息
        - ⽤户登录失效（redis 分布式会话—共享session）
      - 订单超时取消
        - 使⽤quartz定时任务进⾏轮询
          - **性能问题**
  - ### [P3 分布式系统涉及技术点](https://www.bilibili.com/video/BV11N411Z7is?p=3)
    collapsed:: true
    - Nginx集群\Tomcat集群
    - Redis缓存数据库
    - ElasticSearch搜索引擎
      - 模糊搜索问题
    - 分布式系统⽤户登录问题
      -
    - 分布式锁
      - 超卖问题
    - MyCat分布式数据库
    - 微服务架构
      - 单体故障问题
    - 分布式事务
      - 多个事务的集合
    - 消息队列
      - 延时任务 （订单取消，定时执行）
      - 服务通信
    - 容器化技术docker
      - 服务部署A
    - 优化（MySQ\Tomcat）
  - ### [P4 Redis-介绍](https://www.bilibili.com/video/BV11N411Z7is?p=4)
    - 可以解决的问题
      collapsed:: true
      - 数据库访问压⼒
        - 为了降低对数据库的访问压⼒，当多个⽤户请求相同的数据时，我们可以将第⼀次从数据库查询到数据进⾏缓存(存储在内存中)，以减少对数据库的访问次数
      - ⾸⻚数据的加载效率
        - 将⼤量的且不经常改变的数据缓存在内容中，可以⼤幅度提⾼访问速度
      - ---
      - 集群部署下的商品超卖
        - 分布式事务
      - ⽤户登录
        - 分布式会话
    - #### [[redis]]
      - 背景
        collapsed:: true
        - 2008年 萨尔瓦多——开发⼀个进⾏⽹站实时统计软件项⽬（LLOOGG）,项⽬的实时统计功能需要频繁的进⾏数据库的读写(对数据库的读写要求很⾼—数千次/s)，MySQL满⾜不了项⽬的需求，萨尔瓦多就使⽤C语⾔⾃定义了⼀个数据存储系统—Redis。后来萨尔瓦多不满⾜仅仅在LLOOGG这个项⽬中使⽤redis，就对redis进⾏ 产品化 并进⾏开源，以便让更多的⼈能够使⽤
      - 使⽤
        collapsed:: true
        - **Redis就是⼀个⽤C语⾔开发的、基于内存结构进⾏ 键值对 数据存储的、⾼性能的、⾮关系型NoSQL数据库**
      - 数据类型
        collapsed:: true
        - redis是基于键值对进⾏数据存储的，但是value可以是多种数据类型（5）
          - string 字符串
          - hash 映射
          - list 列表（队列）
          - set 集合
          - zset ⽆序集合
      - 特点
        collapsed:: true
        - 基于内存存储，数据读写效率很⾼
        - Redis本身⽀持持久化
        - Reids虽然基于key-value存储，但是⽀持多种数据类型
        - Redis⽀持集群、⽀持主从模式
      - 应⽤场景
        collapsed:: true
        [P5 Redis-应用场景](https://www.bilibili.com/video/BV11N411Z7is?p=5)
        - 缓存
          collapsed:: true
          - 为了提供数据的访问速度
          - 降低数据库的访问压⼒
        - 点赞、排⾏榜、计数器等功能
          collapsed:: true
          - 对数据实时读写要求⽐较⾼，但是对数据库的⼀致性要求并不是太⾼的功能场景
        - 分布式锁
          collapsed:: true
          - 基于redis的操作特性可以实现分布式锁功能
        - 分布式会话
          collapsed:: true
          - 在分布式系统中可以使⽤redis实现 session (共享缓存)
        - 消息中间件
          collapsed:: true
          - 可以使⽤redis实现应⽤之间的通信
      - Redis的优缺点
        collapsed:: true
        [P6 Redis-优缺点总结](https://www.bilibili.com/video/BV11N411Z7is?p=6)
        - 优点
          - 基于内存结构，性能极⾼（读 110000次/秒，写 81000次/秒）
          - 基于键值对存储，但是⽀持多种数据类型
          - 所有操作都是原⼦性，可以通过lua脚本将多个操作合并为⼀个原⼦操作（Redis的事务）
          - 基于单线程操作，但是其多路复⽤实现了⾼性能读写
        - 缺点
          - 缓存数据与数据库数据必须通过两次写操作才能保持数据的⼀致性
          - 使⽤缓存会存在**缓存穿透、缓存击穿及缓存雪崩**等问题，需要处理
          - redis可以作为数据库使⽤进⾏数据的持久存储，存在丢失数据的⻛险
      - [P7 Redis-基于Linux环境的安装](https://www.bilibili.com/video/BV11N411Z7is?p=7)
        collapsed:: true
        - ```shell
          wget http://download.redis.io/releases/redis-5.0.5.tar.gz
          yum -y install gcc
          tar -zxvf redis-5.0.5.tar.gz
          cd redis-5.0.5
          make MALLOC=libc
          make install
          #--------------------------------------------------------
          ## 当我们完成redis安装之后，就可以执⾏redis相关的指令
          redis-server ## 启动redis服务
          redis-server &
          redis-cli ## 启动redis操作客户端(命令⾏客户端)
          ```
      - [P8 Redis-配置文件](https://www.bilibili.com/video/BV11N411Z7is?p=8)
        collapsed:: true
        - 使⽤ redis-server 指令启动redis服务的时候，可以在指令后添加redis配置⽂件的路径，以设置redis 是以何种配置进⾏启动
          - ```shell
            redis-server redis-6380.conf & ## redis以redis-6380.conf⽂件中的配置来启动
            ```
        - 如果不指定配置⽂件的名字，则按照redis的默认配置启动（默认配置≠redis.conf）
        - 我们可以通过创建redis根⽬录下 redis.conf 来创建多个配置⽂件，启动多个redis服务
          - ```shell
            redis-server redis-6380.conf &
            redis-server redis-6381.conf &
            ```
        - ```shell
          ## 设置redis实例（服务）为守护模式,默认值为no，可以设置为yes
          daemonize no
          ## 设置当前redis实例启动之后保存进程id的⽂件路径
          pidfile /var/run/redis_6379.pid
          ## 设置redis实例的启动端⼝（默认6379）
          port 6380
          ## 设置当前redis实例是否开启保护模式
          protected-mode yes
          ## 设置允许访问当前redis实例的ip地址列表
          bind 127.0.0.1
          ## 设置连接密码
          requirepass 123456
          ## 设置redis实例中数据库的个数（默认16个，编号0-15）
          databases 16
          ## 设置最⼤并发数量
          maxclients
          ## 设置客户端和redis建⽴连接的最⼤空闲时间，设置为0表示不限制
          timeout 0
          ```
      - [P9 Redis-数据类型](https://www.bilibili.com/video/BV11N411Z7is?p=9)
        collapsed:: true
        - ![msedge_302.png](../assets/msedge_302_1676863183499_0.png)
        - [P10 Redis-string常用指令](https://www.bilibili.com/video/BV11N411Z7is?p=10)
          ```shell
          ## 设置值/修改值 如果key存在则进⾏修改
          set key value
          ## 取值
          get key
          ## 批量添加
          mset k1 v1 [k2 v2 k3 v3 ...]
          ## 批量取值
          mget k1 [k2 k3...]
          ## ⾃增和⾃减
          incr key ## 在key对应的value上⾃增 +1
          decr key ## 在key对应的value上⾃减 -1
          incrby key v ## 在key对应的value上+v
          decrby key v ## 在key对应的value上-v
          ## 添加键值对，并设置过期时间(TTL)
          setex key time(seconds) value
          ## 设置值，如果key不存在则成功添加，如果key存在则添加失败（不做修改操作）
          setnx key value
          ## 在指定的key对应value拼接字符串
          append key value
          ## 获取key对应的字符串的⻓度
          strlen key
          ```
        - [P11 Redis-hash常用指令](https://www.bilibili.com/video/BV11N411Z7is?p=11)
          ```shell
          ## 向key对应的hash中添加键值对
          hset key field value
          ## 从key对应的hash获取field对应的值
          hget key field
          ## 向key对应的hash结构中批量添加键值对
          hmset key f1 v1 [f2 v2 ...]
          ## 从key对应的hash中批量获取值
          hmget key f1 [f2 f3 ...]
          ## 在key对应的hash中的field对应value上加v
          hincrby key field v
          ## 获取key对应的hash中所有的键值对
          hgetall key
          ## 获取key对应的hash中所有的field
          hkeys key
          ## 获取key对应的hash中所有的value
          hvals key
          ## 检查key对应的hash中是否有指定的field
          hexists key field
          ## 获取key对应的hash中键值对的个数
          hlen key
          ## 向key对应的hash结构中添加f-v,如果field在hash中已经存在，则添加失败
          hsetnx key field value
          ```
        - [P12 Redis-list常用指令](https://www.bilibili.com/video/BV11N411Z7is?p=12)
          ```shell
          ## 存储数据
          lpush key value # 在key对应的列表的左侧添加数据value
          rpuhs key value # 在key对应的列表的右侧添加数据value
          ## 获取数据
          lpop key # 从key对应的列表的左侧取⼀个值
          rpop key # 从key对应的列表的右侧取⼀个值
          ## 修改数据
          lset key index value #修改key对应的列表的索引位置的数据（索引从左往右，从0开始）
          ## 查看key对应的列表中索引从start开始到stop结束的所有值
          lrange key start stop
          ## 查看key对应的列表中index索引对应的值
          lindex key index
          ## 获取key对应的列表中的元素个数
          llen key
          ## 从key对应的列表中截取key在[start,stop]范围的值，不在此范围的数据⼀律被清除掉
          ltrim key start stop
          ## 从k1右侧取出⼀个数据存放到k2的左侧
          rpoplpush k1 k2
          ```
        - [P13 Redis-set常用指令](https://www.bilibili.com/video/BV11N411Z7is?p=13)
          ```shell
          ## 存储元素 ：在key对应的集合中添加元素，可以添加1个，也可以同时添加多个元素
          sadd key v1 [v2 v3 v4...]
          ## 遍历key对应的集合中的所有元素
          smembers key
          ## 随机从key对于听的集合中获取⼀个值（出栈）
          spop key
          ## 交集
          sinter key1 key2
          ## 并集
          sunion key1 key2
          ## 差集
          sdiff key1 key2
          ## 从key对应的集合中移出指定的value
          srem key value
          ## 检查key对应的集合中是否有指定的value
          sismember key value
          ```
        - [P14 Redis-zset常用指令](https://www.bilibili.com/video/BV11N411Z7is?p=14)
          ```shell
          ## 存储数据(score存储位置必须是数值，可以是float类型的任意数字；
          ## member元素不允许重复)
          zadd key score member [score member...]
          ## 查看key对应的有序集合中索引[start,stop]数据——
          ## 按照score值由⼩到⼤（start 和 stop指的不是score，⽽是元素在有序集合中的索引）
          zrange key start top
          ##查看member元素在key对应的有序集合中的索引
          zscore key member
          ## 获取key对应的zset中的元素个数
          zcard key
          ## 获取key对应的zset中，score在[min,max]范围内的member个数
          zcount key min max
          ## 从key对应的zset中移除指定的member
          zrem key6 member
          ## 查看key对应的有序集合中索引[start,stop]数据——按照score值由⼤到⼩
          zrevrange key start stop
          ```
        - [P15 Redis-其他常用指令（key,db）](https://www.bilibili.com/video/BV11N411Z7is?p=15)
          ```shell
          ## KEY
          ## 查看redis中满⾜pattern规则的所有的key（keys *）
          keys pattern
          ## 查看指定的key谁否存在
          exists key
          ## 删除指定的key-value对
          del key
          ## 获取当前key的存活时间(如果没有设置过期返回-1，设置过期并且已经过期返回-2)
          ttl key
          ## 设置键值对过期时间
          expire key seconds
          pexpire key milliseconds
          ## 取消键值对过期时间
          persist key
          ```
          ---
          ```shell
          ## DB
          ## 切换数据库
          select index
          ## 将键值对从当前db移动到⽬标db
          move key index
          ## 清空当前数据库数据
          flushdb
          ## 清所有数据库的k-v
          flushall
          ## 查看当前db中k-v个数
          dbsize
          ## 获取最后⼀次持久化操作时间
          lastsave
          ```
      - **持久化**（因为基于内存操作，持久化未必即时，而是以一种策略）
        collapsed:: true
        - RDB（Redis DataBase，默认策略）
          description:: 在满⾜特定的redis操作条件时，将内存中的数据以数据快照的形式存储到rdb⽂件中
          description:: [P16 Redis-持久化策略-RDB](https://www.bilibili.com/video/BV11N411Z7is?p=16)
          collapsed:: true
          ![msedge_297.png](../assets/msedge_297_1676656761047_0.png)
          - 原理
            - 当redis中的写操作达到指定的次数、同时距离上⼀次持久化达到指定的时间就会将redis内存中的数据⽣成数据快照，保存在指定的rdb⽂件中
          - 默认触发持久化条件：
            - ```shell
              # 当操作次数达到1次，900s就会进⾏持久化
              save 900 1
              # 当操作次数达到10次，300s就会进⾏持久化
              save 300 10
              # 当操作次数达到10000次，60s就会就⾏持久化
              save 60 10000
              ```
          - ```shell
            ## rdb持久化开关 （RDB 压缩）
            rdbcompression yes
            ## 指定rdb数据存储的⽂件
            dbfilename dump.rdb
            ```
          - 缺点
            - 有数据丢失的风险（上⼀次持久化之后的操作数据）；
            - 数据快照（数据完全拷贝），实时性持久化性能差；
            - 基于第 2 点，数据量多的时候，⽣成快照的时可能卡顿，过长等问题；
          - 优点
            - 数据量⼩的时候很快；
            - 快照保存在 `rdb` 文件，迁移性较好；
          -
        - AOF（Apeend Only File）
          description:: 当达到设定触发条件时，将redis执⾏的**写操作指令**存储在aof⽂件中，Redis默认未开启aof持久化；默认采用增量存储；存在重复键的时候回执行优化操作；
          description:: [P17 Redis-持久化策略-AOF](https://www.bilibili.com/video/BV11N411Z7is?p=17)
          collapsed:: true
          ![msedge_298.png](../assets/msedge_298_1676656998594_0.png)
          - 原理
            - Redis将每⼀个成功的写操作写⼊到aof⽂件中，当redis重启的时候就执⾏aof⽂件中的指令以恢复数据
          - ```shell
            ## 开启AOF
            appendonly yes
            ## 设置触发条件（三选⼀）
            appendfsync always 		## 只要进⾏成功的写操作，就执⾏aof
            appendfsync everysec 	## 每秒进⾏⼀次aof
            appendfsync no 			## 让redis执⾏决定aof
            ## 设置aof⽂件路径
            appendfilename "appendonly.aof"
            ```
          - 优点：
            - 写操作命令存在 `AOF` 文件中，也方便迁移；
          - 比较
            - 数据量小的时候，RDB 比较快；
              - 数据量大的时候不一定；
                - 增量更新更适合实时持久化，所以**数据完整性**高，更加安全；
                  （实时 IO，所以会慢）
                - RDB 恢复要更快，但是容易丢数据，且生成较慢；
              - 比如对某一个键同时操作的频率高的时候，在AOF可能触发整理的次数就高；
            - 同时存在 `AOF` 和 `RDB` 两种策略的时候， `AOF` 优先；
      - Java 应用连接
        - [P18 Redis-Maven工程连接Redis](https://www.bilibili.com/video/BV11N411Z7is?p=18)
          collapsed:: true
          - 设置redis允许远程连接
            - 开启远程
            - 云控制台上放行端口
          - 在 普通 Maven ⼯程 连接Redis
            - ```xml
              <!-- https://mvnrepository.com/artifact/redis.clients/jedis -->
              <dependency>
               <groupId>redis.clients</groupId>
               <artifactId>jedis</artifactId>
               <version>2.9.0</version>
              </dependency
              ```
        - [P19 Redis-SpringBoot工程连接Redis](https://www.bilibili.com/video/BV11N411Z7is?p=19)
          collapsed:: true
          - Spring Data Redis
            description:: part of the larger Spring Data family, provides easy configuration and access to Redis from Spring applications. It offers both low-level and high-level abstractions for interacting with the store, freeing the user from infrastructural concerns.
          - Spring Data Redis依赖中，提供了⽤于连接redis的客户端：
            - RedisTemplate
            - StringRedisTemplat
          - Spring IOC & Spring AOP
          - 配置redis
            - application.yml⽂件配置redis的连接信息
            - ```yaml
              spring:
               redis:
               host: 47.96.11.185
               port: 6379
               database: 0
               password: 123456
              ```
          - 使⽤redis客户端连接redis
            - 直接在service中注⼊ RedisTemplate 或者 StringRedisTemplate ,就可以使⽤此对象完成redis操作
      - [P20 Redis-Spring Data Redis常用操作](https://www.bilibili.com/video/BV11N411Z7is?p=20)
        - 添加
          - ```java
            //1.string
            //添加数据 set key value
            stringRedisTemplate.boundValueOps(product.getProductId()).set( jsonstr);
            //2.hash
            stringRedisTemplate.boundHashOps("products").put(product.getProductId(),jsonstr);
            //3.list
            stringRedisTemplate.boundListOps("list").leftPush("ccc");
            //4.set
            stringRedisTemplate.boundSetOps("s1").add("v2");
            //5.zset
            stringRedisTemplate.boundZSetOps("z1").add("v1",1.2);
            ```
        - 取值
          - ```java
            //string
            String o = stringRedisTemplate.boundValueOps("103").get();
            //hash
            Object v = stringRedisTemplate.boundHashOps("products").get("101");
            //list
            String s1 = stringRedisTemplate.boundListOps("list").leftPop();
            String s2 = stringRedisTemplate.boundListOps("list").rightPop();
            String s3 = stringRedisTemplate.boundListOps("list").index(1);
            //set
            Set<String> vs = stringRedisTemplate.boundSetOps("s1").members();
            //zset
            Set<String> vs2 = stringRedisTemplate.boundZSetOps("z1").range(0, 5);
            ```
        - string类型的操作⽅法
          - ```java
            //添加数据 set key value
            stringRedisTemplate.boundValueOps(product.getProductId()).set(jsonstr);
            //添加数据时指定过期时间 setex key 300 value
            stringRedisTemplate.boundValueOps("103").set(jsonstr,300);
            //设置指定key的过期时间 expire key 20
            stringRedisTemplate.boundValueOps("103").expire(20, TimeUnit.SECONDS);
            //添加数据 setnx key value
            Boolean absent = stringRedisTemplate.boundValueOps("103").setIfAbsent(jsonstr);
            ```
      - [P21 Redis-使用Redis缓存数据操作流程](https://www.bilibili.com/video/BV11N411Z7is?p=21)
        -
      - [P22 Redis-锋迷商城-使用Redis缓存商品详情1](https://www.bilibili.com/video/BV11N411Z7is?p=22)
      - [P23 Redis-锋迷商城-使用Redis缓存商品详情2](https://www.bilibili.com/video/BV11N411Z7is?p=23)
      - [P24 Redis-页面静态化技术介绍（暂不实现）](https://www.bilibili.com/video/BV11N411Z7is?p=24)
      - [P25 Redis-锋迷商城-使用redis缓存首页轮播图](https://www.bilibili.com/video/BV11N411Z7is?p=25)
      - [P26 Redis-锋迷商城-使用redis缓存首页类别列表](https://www.bilibili.com/video/BV11N411Z7is?p=26)
      - [P27 Redis-缓存击穿](https://www.bilibili.com/video/BV11N411Z7is?p=27)
        - 缓存击穿
          description:: ⼤量的并发请求同时访问同⼀个在redis中不存在的数据，就会导致⼤量的请求绕过redis同时并发访问数据库，对数据库造成了⾼并发访问压⼒
          collapsed:: true
          - **Solution** -> ==双重检测锁==
            - ```java
              public ResultVO listIndexImgs() {
                List<IndexImg> indexImgs = null;
                try {
                  //1000个并发请求，请求轮播图
                  String imgsStr = stringRedisTemplate.boundValueOps("indexImgs").get();
                  //1000个请求查询到redis中的数据都是null
                  if (imgsStr != null) {
                    // 从redis中获取到了轮播图信息
                    JavaType javaType = objectMapper.getTypeFactory()
                      .constructParametricType(ArrayList.class, IndexImg.class);
                    indexImgs = objectMapper.readValue(imgsStr, javaType);
                  } else {
                    // 1000个请求都会进⼊else
                    // (service类在spring容器中是单例的，
                    // 1000个并发会启动1000个线程来处理，但是公⽤⼀个service实例)
                    synchronized (this){
                      // 第⼆次查询redis
                      String s = stringRedisTemplate.boundValueOps("indexImgs").get();
                      if(s == null){
                        // 这1000个请求中，只有第⼀个请求再次查询redis时依然为null
                        indexImgs = indexImgMapper.listIndexImgs();
                        System.out.println("----------------查询数据库");
                        stringRedisTemplate.boundValueOps("indexImgs")
                          .set(objectMapper.writeValueAsString(indexImgs));
                        stringRedisTemplate.boundValueOps("indexImgs")
                          .expire(1, TimeUnit.DAYS);
                      }else{
                        JavaType javaType = objectMapper.getTypeFactory()
                          .constructParametricType(ArrayList.class, IndexImg.class);
                        indexImgs = objectMapper.readValue(s, javaType);
                      }
                    }
                  }
                } catch (JsonProcessingException e) {
                  e.printStackTrace();
                }
                //返回数据
                if(indexImgs != null){
                  return new ResultVO(ResStatus.OK,"success",indexImgs);
                }else{
                  return new ResultVO(ResStatus.NO,"fail",null);
                }
              }
              ```
      - [P28 Redis-Jemeter测试缓存击穿](https://www.bilibili.com/video/BV11N411Z7is?p=28)
      - [P29 Redis-缓存穿透](https://www.bilibili.com/video/BV11N411Z7is?p=29)
        - 缓存穿透
          description:: ⼤量的请求⼀个数据库中不存在的数据，⾸先在redis中⽆法命中，最终所有的请求都会访问数据库，同样会导致数据库承受巨⼤的访问压⼒
          - **Solution** -> 当从数据库查询到⼀个null时，写⼀个⾮空的数据到redis，并设置过期时
          - ![msedge_341.png](../assets/msedge_341_1678707162726_0.png)
          -
      - [P30 Redis-缓存雪崩](https://www.bilibili.com/video/BV11N411Z7is?p=30)
      - [P31 Redis-主从介绍](https://www.bilibili.com/video/BV11N411Z7is?p=31)
      - [P32 Redis-主从配置](https://www.bilibili.com/video/BV11N411Z7is?p=32)
      - [P33 Redis-哨兵模式介绍](https://www.bilibili.com/video/BV11N411Z7is?p=33)
      - [P34 Redis-哨兵模式配置](https://www.bilibili.com/video/BV11N411Z7is?p=34)
      - [P35 Redis-集群介绍](https://www.bilibili.com/video/BV11N411Z7is?p=35)
      - [P36 Redis-集群配置](https://www.bilibili.com/video/BV11N411Z7is?p=36)
      - [P37 Redis-集群管理](https://www.bilibili.com/video/BV11N411Z7is?p=37)
      - [P38 Redis-SpringBoot应用连接集群](https://www.bilibili.com/video/BV11N411Z7is?p=38)
      - [P39 Redis-淘汰策略](https://www.bilibili.com/video/BV11N411Z7is?p=39)
      - [P40 Redis-高频面试题总结](https://www.bilibili.com/video/BV11N411Z7is?p=40)
      - [P41 Redis-使用Redis实现分布式会话流程](https://www.bilibili.com/video/BV11N411Z7is?p=41)
      - [P42 Redis-锋迷商城-使用redis实现分布式会话1](https://www.bilibili.com/video/BV11N411Z7is?p=42)
      - [P43 Redis-锋迷商城-使用Redis实现分布式会话2](https://www.bilibili.com/video/BV11N411Z7is?p=43)
  - [P44 服务器集群搭建-介绍](https://www.bilibili.com/video/BV11N411Z7is?p=44)
  - [P45 服务器集群搭建-架构说明](https://www.bilibili.com/video/BV11N411Z7is?p=45)
  - [P46 服务器集群搭建-Nginx负载均衡配置](https://www.bilibili.com/video/BV11N411Z7is?p=46)
  - [P47 服务器集群搭建-Nginx负载均衡策略](https://www.bilibili.com/video/BV11N411Z7is?p=47)
  - [P48 分布式并发问题-商品超卖](https://www.bilibili.com/video/BV11N411Z7is?p=48)
  - [P49 分布式并发问题-使用redis实现分布式锁-流程分析](https://www.bilibili.com/video/BV11N411Z7is?p=49)
  - [P50 分布式并发问题-使用redis实现分布式锁-代码实现1](https://www.bilibili.com/video/BV11N411Z7is?p=50)
  - [P51 分布式并发问题-使用redis实现分布式锁-问题分析（加锁成功之后出现故障导致无法释放锁）](https://www.bilibili.com/video/BV11N411Z7is?p=51)
  - [P52 分布式并发问题-使用redis实现分布式锁-解决因线程异常导致无法释放锁的问题](https://www.bilibili.com/video/BV11N411Z7is?p=52)
  - [P53 分布式并发问题-使用redis实现分布式锁-解决因t1过期释放t2锁的问题](https://www.bilibili.com/video/BV11N411Z7is?p=53)
  - [P54 分布式并发问题-看门狗机制介绍](https://www.bilibili.com/video/BV11N411Z7is?p=54)
  - [P55 分布式并发问题-使用Redission分布式锁](https://www.bilibili.com/video/BV11N411Z7is?p=55)
  - [P56 分布式并发问题-释放锁代码优化](https://www.bilibili.com/video/BV11N411Z7is?p=56)
  - [P57 分布式并发问题-释放锁代码优化的流程总结](https://www.bilibili.com/video/BV11N411Z7is?p=57)
  - [P58 分布式并发问题-Redission分布式锁实现原理](https://www.bilibili.com/video/BV11N411Z7is?p=58)
  - [P59 分布式并发问题-Redission分布式锁使用总结](https://www.bilibili.com/video/BV11N411Z7is?p=59)
  - [P60 ES-搜索引擎的介绍](https://www.bilibili.com/video/BV11N411Z7is?p=60)
  - [P61 ES-Luence全文检索流程](https://www.bilibili.com/video/BV11N411Z7is?p=61)
  - [P62 ES-分词器介绍](https://www.bilibili.com/video/BV11N411Z7is?p=62)
  - [P63 ES-lucene全文检索与数据库查询的比较](https://www.bilibili.com/video/BV11N411Z7is?p=63)
  - [P64 ES-ElasticSearch简介](https://www.bilibili.com/video/BV11N411Z7is?p=64)
  - [P65 ES-ElasticSearch安装配置及运行](https://www.bilibili.com/video/BV11N411Z7is?p=65)
  - [P66 ES-Kibana安装及配置](https://www.bilibili.com/video/BV11N411Z7is?p=66)
  - [P67 ES-分词器配置](https://www.bilibili.com/video/BV11N411Z7is?p=67)
  - [P68 ES-ES访问RESTful规范介绍](https://www.bilibili.com/video/BV11N411Z7is?p=68)
  - [P69 ES-基本指令操作](https://www.bilibili.com/video/BV11N411Z7is?p=69)
  - [P70 ES-数据类型介绍](https://www.bilibili.com/video/BV11N411Z7is?p=70)
  - [P71 ES-复杂查询](https://www.bilibili.com/video/BV11N411Z7is?p=71)
  - [P72 ES-高级查询(多条件、显示字段、分页、高亮)](https://www.bilibili.com/video/BV11N411Z7is?p=72)
  - [P73 ES-SpringBoot应用整合ES](https://www.bilibili.com/video/BV11N411Z7is?p=73)
  - [P74 ES-SpringBoot应用访问ES（创建索引、删除索引、添加文档）](https://www.bilibili.com/video/BV11N411Z7is?p=74)
  - [P75 ES-SpringBoot应用访问ES（检索操作）](https://www.bilibili.com/video/BV11N411Z7is?p=75)
  - [P76 ES-SpringBoot应用访问ES（检索结果封装）](https://www.bilibili.com/video/BV11N411Z7is?p=76)
  - [P77 ES-锋迷商城-使用ES实现商品检索（创建索引）](https://www.bilibili.com/video/BV11N411Z7is?p=77)
  - [P78 ES-锋迷商城-使用ES实现商品检索（导入数据1）](https://www.bilibili.com/video/BV11N411Z7is?p=78)
  - [P79 ES-锋迷商城-使用ES实现商品检索（导入数据2）](https://www.bilibili.com/video/BV11N411Z7is?p=79)
  - [P80 ES-锋迷商城-使用ES实现商品检索（检索数据）](https://www.bilibili.com/video/BV11N411Z7is?p=80)
  - [P81 SpringCloud-单体应用存在的问题](https://www.bilibili.com/video/BV11N411Z7is?p=81)
  - [P82 SpringCloud-微服务架构介绍](https://www.bilibili.com/video/BV11N411Z7is?p=82)
  - [P83 SpringCloud-微服务架构需要解决的问题](https://www.bilibili.com/video/BV11N411Z7is?p=83)
  - [P84 SpringCloud-服务之间如何相互发现-服务注册与发现中心](https://www.bilibili.com/video/BV11N411Z7is?p=84)
  - [P85 SpringCloud-服务之间如何进行通信](https://www.bilibili.com/video/BV11N411Z7is?p=85)
  - [P86 SpringCloud-被调用的服务出现故障如何处理](https://www.bilibili.com/video/BV11N411Z7is?p=86)
  - [P87 SpringCloud-客户端如何统一访问多个接口服务](https://www.bilibili.com/video/BV11N411Z7is?p=87)
  - [P88 SpringCloud-微服务框架介绍](https://www.bilibili.com/video/BV11N411Z7is?p=88)
  - [P89 SpringCloud-搭建服务注册与发现中心（Eureka）](https://www.bilibili.com/video/BV11N411Z7is?p=89)
  - [P90 SpringCloud-服务注册-添加订单业务开发](https://www.bilibili.com/video/BV11N411Z7is?p=90)
  - [P91 SpringCloud-服务注册-将服务注册到服务注册与发现中心](https://www.bilibili.com/video/BV11N411Z7is?p=91)
  - [P92 SpringCloud-服务消费-基于Ribbon的服务消费](https://www.bilibili.com/video/BV11N411Z7is?p=92)
  - [P93 SpringCloud-服务消费-Ribbon服务调用说明](https://www.bilibili.com/video/BV11N411Z7is?p=93)
  - [P94 SpringCloud-服务消费-Ribbon服务调用传参](https://www.bilibili.com/video/BV11N411Z7is?p=94)
  - [P95 SpringCloud-服务消费-基于Feign的服务调用](https://www.bilibili.com/video/BV11N411Z7is?p=95)
  - [P96 SpringCloud-服务消费-Feign服务调用参数传递](https://www.bilibili.com/video/BV11N411Z7is?p=96)
  - [P97 SpringCloud-Eureka集群搭建](https://www.bilibili.com/video/BV11N411Z7is?p=97)
  - [P98 SpringCloud-Eureka的安全配置（SpringSecurity）](https://www.bilibili.com/video/BV11N411Z7is?p=98)
  - [P99 SpringCloud-熔断器的状态](https://www.bilibili.com/video/BV11N411Z7is?p=99)
  - [P100 SpringCloud-基于Ribbon服务调用的熔断器使用（服务消费者）](https://www.bilibili.com/video/BV11N411Z7is?p=100)
  - [P101 SpringCloud-基于Ribbon服务调用的熔断器使用（服务提供者）](https://www.bilibili.com/video/BV11N411Z7is?p=101)
  - [P102 SpringCloud-Hystrix服务熔断配置](https://www.bilibili.com/video/BV11N411Z7is?p=102)
  - [P103 SpringCloud-基于Feign服务调用的熔断器使用](https://www.bilibili.com/video/BV11N411Z7is?p=103)
  - [P104 SpringCloud-Ribbon参数配置说明](https://www.bilibili.com/video/BV11N411Z7is?p=104)
  - [P105 SpringCloud-Ribbon参数配置](https://www.bilibili.com/video/BV11N411Z7is?p=105)
  - [P106 SpringCloud-Hystrix熔断器仪表盘监控1](https://www.bilibili.com/video/BV11N411Z7is?p=106)
  - [P107 SpringCloud-Hystrix熔断器仪表盘监控2](https://www.bilibili.com/video/BV11N411Z7is?p=107)
  - [P108 锋迷商城-微服务拆分介绍](https://www.bilibili.com/video/BV11N411Z7is?p=108)
  - [P109 锋迷商城-微服务架构设计](https://www.bilibili.com/video/BV11N411Z7is?p=109)
  - [P110 锋迷商城-项目运行环境准备（云主机）](https://www.bilibili.com/video/BV11N411Z7is?p=110)
  - [P111 锋迷商城-搭建服务注册与发现中心](https://www.bilibili.com/video/BV11N411Z7is?p=111)
  - [P112 锋迷商城-创建用户登录接口服务(api-user-login)](https://www.bilibili.com/video/BV11N411Z7is?p=112)
  - [P113 锋迷商城-创建查询用户信息服务（user-check）](https://www.bilibili.com/video/BV11N411Z7is?p=113)
  - [P114 锋迷商城-用户登录接口服务功能实现](https://www.bilibili.com/video/BV11N411Z7is?p=114)
  - [P115 锋迷商城-用户登录接口服务调用用户查询服务](https://www.bilibili.com/video/BV11N411Z7is?p=115)
  - [P116 锋迷商城-创建用户注册接口及保存用户信息服务](https://www.bilibili.com/video/BV11N411Z7is?p=116)
  - [P117 锋迷商城-用户注册接口服务实现](https://www.bilibili.com/video/BV11N411Z7is?p=117)
  - [P118 锋迷商城-创建订单提交业务相关服务](https://www.bilibili.com/video/BV11N411Z7is?p=118)
  - [P119 锋迷商城-订单提交业务-查询库存服务实现](https://www.bilibili.com/video/BV11N411Z7is?p=119)
  - [P120 锋迷商城-订单提交业务-保存订单快照服务实现](https://www.bilibili.com/video/BV11N411Z7is?p=120)
  - [P121 锋迷商城-订单提交业务-修改库存服务实现](https://www.bilibili.com/video/BV11N411Z7is?p=121)
  - [P122 锋迷商城-订单提交业务-删除购物车记录服务实现](https://www.bilibili.com/video/BV11N411Z7is?p=122)
  - [P123 锋迷商城-订单提交业务-保存订单服务实现](https://www.bilibili.com/video/BV11N411Z7is?p=123)
  - [P124 锋迷商城-订单提交业务-订单提交接口服务实现1](https://www.bilibili.com/video/BV11N411Z7is?p=124)
  - [P125 锋迷商城-订单提交业务-订单提交接口服务实现2](https://www.bilibili.com/video/BV11N411Z7is?p=125)
  - [P126 锋迷商城-订单超时取消-微服务拆分设计](https://www.bilibili.com/video/BV11N411Z7is?p=126)
  - [P127 锋迷商城-订单超时取消-创建相关服务](https://www.bilibili.com/video/BV11N411Z7is?p=127)
  - [P128 锋迷商城-订单超时取消-查询超时订单服务实现](https://www.bilibili.com/video/BV11N411Z7is?p=128)
  - [P129 锋迷商城-订单超时取消-修改订单状态服务实现](https://www.bilibili.com/video/BV11N411Z7is?p=129)
  - [P130 锋迷商城-订单超时取消-关闭订单服务实现1](https://www.bilibili.com/video/BV11N411Z7is?p=130)
  - [P131 锋迷商城-订单超时取消-查询订单快照服务实现](https://www.bilibili.com/video/BV11N411Z7is?p=131)
  - [P132 锋迷商城-订单超时取消-关闭订单服务实现2](https://www.bilibili.com/video/BV11N411Z7is?p=132)
  - [P133 锋迷商城-订单超时取消-定时取消订单服务实现](https://www.bilibili.com/video/BV11N411Z7is?p=133)
  - [P134 Gateway-网关介绍](https://www.bilibili.com/video/BV11N411Z7is?p=134)
  - [P135 Gateway-使用Nginx实现服务网关](https://www.bilibili.com/video/BV11N411Z7is?p=135)
  - [P136 Gateway-搭建Gateway服务器](https://www.bilibili.com/video/BV11N411Z7is?p=136)
  - [P137 Gateway-工作原理](https://www.bilibili.com/video/BV11N411Z7is?p=137)
  - [P138 Gateway-Predicate断言](https://www.bilibili.com/video/BV11N411Z7is?p=138)
  - [P139 Gateway-过滤器-内置过滤器](https://www.bilibili.com/video/BV11N411Z7is?p=139)
  - [P140 Gateway-过滤器-自定义网关过滤器（方式1）](https://www.bilibili.com/video/BV11N411Z7is?p=140)
  - [P141 Gateway-过滤器-自定义网关过滤器（方式2）](https://www.bilibili.com/video/BV11N411Z7is?p=141)
  - [P142 Gateway-过滤器-全局过滤器实现鉴权](https://www.bilibili.com/video/BV11N411Z7is?p=142)
  - [P143 Gateway-过滤器-动态路由配置](https://www.bilibili.com/video/BV11N411Z7is?p=143)
  - [P144 Gateway-网关限流介绍](https://www.bilibili.com/video/BV11N411Z7is?p=144)
  - [P145 Gateway-常见的网关限流算法](https://www.bilibili.com/video/BV11N411Z7is?p=145)
  - [P146 Gateway-网关限流](https://www.bilibili.com/video/BV11N411Z7is?p=146)
  - [P147 服务链路追踪-zipkin介绍](https://www.bilibili.com/video/BV11N411Z7is?p=147)
  - [P148 服务链路追踪-zipkin服务器搭建](https://www.bilibili.com/video/BV11N411Z7is?p=148)
  - [P149 服务链路追踪-运行演示说明](https://www.bilibili.com/video/BV11N411Z7is?p=149)
  - [P150 微服务架构-技术点总结](https://www.bilibili.com/video/BV11N411Z7is?p=150)
  - [P151 RabbitMQ-消息队列介绍](https://www.bilibili.com/video/BV11N411Z7is?p=151)
  - [P152 RabbitMQ-安装及配置](https://www.bilibili.com/video/BV11N411Z7is?p=152)
  - [P153 RabbitMQ-逻辑结构](https://www.bilibili.com/video/BV11N411Z7is?p=153)
  - [P154 RabbitMQ-用户管理](https://www.bilibili.com/video/BV11N411Z7is?p=154)
  - [P155 RabbitMQ-工作方式](https://www.bilibili.com/video/BV11N411Z7is?p=155)
  - [P156 RabbitMQ-虚拟主机、队列及交换机管理](https://www.bilibili.com/video/BV11N411Z7is?p=156)
  - [P157 RabbitMQ-Maven工程整合MQ](https://www.bilibili.com/video/BV11N411Z7is?p=157)
  - [P158 RabbitMQ-SpringBoot应用整合MQ](https://www.bilibili.com/video/BV11N411Z7is?p=158)
  - [P159 RabbitMQ-发送接收对象](https://www.bilibili.com/video/BV11N411Z7is?p=159)
  - [P160 RabbitMQ-在Maven工程使用Java代码创建队列](https://www.bilibili.com/video/BV11N411Z7is?p=160)
  - [P161 RabbitMQ-在SpringBoot应用配置队列与交换机](https://www.bilibili.com/video/BV11N411Z7is?p=161)
  - [P162 RabbitMQ-消息可靠性介绍及RabbitMQ事务](https://www.bilibili.com/video/BV11N411Z7is?p=162)
  - [P163 RabbitMQ-消息可靠性-消息确认及return机制、Maven工程监听](https://www.bilibili.com/video/BV11N411Z7is?p=163)
  - [P164 RabbitMQ-消息可靠性-SpringBoot监听消息确认和return机制返回结果](https://www.bilibili.com/video/BV11N411Z7is?p=164)
  - [P165 RabbitMQ-消息可靠性-消息消费者手动ACK](https://www.bilibili.com/video/BV11N411Z7is?p=165)
  - [P166 RabbitMQ-消息可靠性-消息消费的幂等性问题](https://www.bilibili.com/video/BV11N411Z7is?p=166)
  - [P167 RabbitMQ-使用死信队列实现消息延迟](https://www.bilibili.com/video/BV11N411Z7is?p=167)
  - [P168 锋迷商城-使用MQ取消超时未支付订单](https://www.bilibili.com/video/BV11N411Z7is?p=168)
  - [P169 RabbitMQ-应用场景总结](https://www.bilibili.com/video/BV11N411Z7is?p=169)
  - [P170 SpringCloud-微服务架构总结](https://www.bilibili.com/video/BV11N411Z7is?p=170)
  - [P171 SpringCloud-分布式配置中心介绍](https://www.bilibili.com/video/BV11N411Z7is?p=171)
  - [P172 SpringCloud-分布式配置中心-创建配置文件仓库](https://www.bilibili.com/video/BV11N411Z7is?p=172)
  - [P173 SpringCloud-分布式配置中心-搭建分布式配置中心](https://www.bilibili.com/video/BV11N411Z7is?p=173)
  - [P174 SpringCloud-分布式配置中心-服务通过配置中心加载配置文件](https://www.bilibili.com/video/BV11N411Z7is?p=174)
  - [P175 分布式事务-分布式事务场景介绍](https://www.bilibili.com/video/BV11N411Z7is?p=175)
  - [P176 分布式事务-分布式系统设计CAP定律和Base理论](https://www.bilibili.com/video/BV11N411Z7is?p=176)
  - [P177 分布式事务-锋迷商城订单提交业务的分布式事务场景分析](https://www.bilibili.com/video/BV11N411Z7is?p=177)
  - [P178 分布式事务-分布式事务管理的XA模型](https://www.bilibili.com/video/BV11N411Z7is?p=178)
  - [P179 分布式事务-XA模型-2PC](https://www.bilibili.com/video/BV11N411Z7is?p=179)
  - [P180 分布式事务-XA模型-3PC](https://www.bilibili.com/video/BV11N411Z7is?p=180)
  - [P181 分布式事务-XA模型-TCC](https://www.bilibili.com/video/BV11N411Z7is?p=181)
  - [P182 分布式事务-基于消息队列的分布式事务处理思想](https://www.bilibili.com/video/BV11N411Z7is?p=182)
  - [P183 分布式事务-分布式事务框架介绍（Tx-LCN）](https://www.bilibili.com/video/BV11N411Z7is?p=183)
  - [P184 分布式事务-Tx-LCN-搭建TM](https://www.bilibili.com/video/BV11N411Z7is?p=184)
  - [P185 分布式事务-Tx-LCN-锋迷商城订单提交分布式事务管理](https://www.bilibili.com/video/BV11N411Z7is?p=185)
  - [P186 分布式数据库-读写分离及主从复制](https://www.bilibili.com/video/BV11N411Z7is?p=186)
  - [P187 分布式数据库-分库分表及负载均衡](https://www.bilibili.com/video/BV11N411Z7is?p=187)
  - [P188 分布式数据库-MySQL主从配置1](https://www.bilibili.com/video/BV11N411Z7is?p=188)
  - [P189 分布式数据库-MySQL主从配置2](https://www.bilibili.com/video/BV11N411Z7is?p=189)
  - [P190 分布式数据库-MyCat【完结】](https://www.bilibili.com/video/BV11N411Z7is?p=190)
- ## Oral defense
  collapsed:: true
  - 你通过本次的毕业设计学到了什么？
    What did you learn through this graduation project?
    - 总的来说，我得到了一个将微服务理念应用于实际项目的重要机会。我在我的机器上设计、构建、调试和在运行它时学到了很多的细节。微服务并不是一个一开始就用于生产环境的架构。它是一点一点迭代的，我的项目也是如此。一开始我把它是一个集中式的系统。然后我尝试通过导入Spring Cloud相关组件来分割它，如 Eureka、Zuul、Robbin、Hystix、Feign等。我学习了这些组件的工作方式，它们的通信机制，如服务注册，发现，负载均衡等等。而且它帮助我在去年找到了一份工作!
    - In general, I get an important chance to apply microservice to actual project. I learned the more details in designing,  building, debugging and running it in my mechine. The microservice is not an architecture that apply to product environment at the beginning. It was iterated little by little, and so is my project. I build it as a centralized system at first. Then I try to split it by importing  components of Spring Cloud, Eureka, Zuul, Robbin, Hystix, Feign etc. I learned how these components work, their communication mechanism, service registration, discovery, loading balance and so much more. And It actually helped me land a job last year!
  - .
    collapsed:: true
    - 通过这个毕业设计，我学到了许多关于微服务架构和B2C购物商城的知识和技能。具体而言，我学会了如何设计和构建微服务架构，包括服务拆分、通信机制、服务注册和发现等。我还学习了如何设计和实现一个完整的B2C购物商城系统，涵盖了用户管理、商品管理、订单管理、支付处理等功能。在实际的开发过程中，我还学会了使用一些流行的开发框架和技术，如Spring Boot、Spring Cloud、Docker等。
  - 你觉得本次的毕业设计的意义在哪里？
    collapsed:: true
    What do you think is the significance of this graduation design?
    - 本次毕业设计的意义在于提供了一个实践的机会，让我能够将所学的理论知识应用到实际项目中。通过设计和实现一个基于微服务架构的B2C购物商城，我深入理解了微服务架构的优势和挑战，了解了B2C电商系统的核心功能和设计思路。此外，这个项目也锻炼了我的系统设计和开发能力，培养了我解决问题和团队合作的能力。
  - 你觉得本次的毕业设计你还有那些值得改进的地方？
    collapsed:: true
    What do you think are the areas for improvement in this graduation design?
    - 虽然我在毕业设计中取得了一些成果，但仍有一些地方可以改进。首先，我可以进一步优化系统的性能和可伸缩性，考虑引入缓存、负载均衡等技术来提高系统的吞吐量和响应时间。其次，我可以改进系统的容错和故障恢复能力，引入监控和日志记录等机制，以便及时发现和解决问题。此外，我还可以增加更多的功能和模块，如搜索引擎、推荐系统等，以提升用户体验和竞争力。最后，我可以进行更详细的测试和性能调优，确保系统在各种情况下都能稳定运行。
  -
- ## References
  - [(PDF) Microservices: yesterday, today, and tomorrow (researchgate.net)](https://www.researchgate.net/publication/315664446_Microservices_yesterday_today_and_tomorrow)
  - [SpringCloud版锋迷商城-微服务项目教程_千锋教育2021最新_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV11N411Z7is) [[BV11N411Z7is]]
  - 我在 B 站淘了 2 个 Java 实战项目! 小破站，YYDS！
    https://mp.weixin.qq.com/s/B-Gzw20xKIPC_w4b_8bJiA
  - Select Title
    collapsed:: true
    - [某宝上花2千去弄毕设被坑，学会自己找项目别花冤枉钱，推荐22套Java毕设源码_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1HT4y1Y76P/)
      collapsed:: true
      - 车位租赁
      - 段子发布平台
      - 房屋租赁ssm
      - 仿微博（ssm）
      - 酒店客房管理系统
      - 兼职论坛（ssm）
      - 教务管理-ssm
      - 酒店管理ssm.zip
      - 就业信息管理
      - 理财管理（spring
      - 流浪猫狗救助网站
      - 旅游网站（spring
      - 民宿网站
      - 汽车租赁
      - 学生毕业设计
      - 疫情数据查看
      - 音乐网站（spring
      - 在线问卷vue.zip
      - 在线选房
      - 在线招标
      - 桌面聊天室
      - oa(ssm-vue).zip
      - 外卖
      - 物联网家具
      - 进销存
      - 视频
      - 在线教育
      - 物流系统
    - [SiGuiyang/spring-cloud-shop: spring cloud 版分布式电商项目，全力打造顶级多模块，高可用，高扩展电商项目](https://github.com/SiGuiyang/spring-cloud-shop)
    - [pig-mesh/pig: ↥ ↥ ↥ 点击关注更新，基于 Spring Cloud 2021 、Spring Boot 2.7、 OAuth2 的 RBAC 权限管理系统](https://github.com/pig-mesh/pig)
  - [macrozheng/mall-swarm: mall-swarm是一套微服务商城系统，采用了 Spring Cloud 2021 & Alibaba、Spring Boot 2.7、Oauth2、MyBatis、Docker、Elasticsearch、Kubernetes等核心技术，同时提供了基于Vue的管理后台方便快速搭建系统。mall-swarm在电商业务的基础集成了注册中心、配置中心、监控中心、网关等系统功能。文档齐全，附带全套Spring Cloud教程。](https://github.com/macrozheng/mall-swarm)
  - [如何免费下载IEEE的论文 - 知乎](https://zhuanlan.zhihu.com/p/100885089)