alias:: spring cloud
tags:: #microserver
-
- ## References
  - [微服务太难了, 学不会... - V2EX](https://www.v2ex.com/t/731988)
    collapsed:: true
    - > 别上来就追求整套整套。。。先自己写几个微服务用 IP 形式互相调用感受一下 然后搞个注册中心统一用服务名调用 再 然后搭个 docker 环境用镜像形式部署 其后再考虑搭个 k8s 单节点学习服务治理 最后再到 k8s 集群 上来就玩 k8s 你啥原理都不懂环境都能搭一个月
    - >大型传统企业的不同企业一般都是不同厂商实施的，之间更是彻彻底底的黑盒。甚至运维可以是不同国家的 team，正因为如此要解决各个系统间的孤岛问题。
      例如为了解决继承问题，有企业总线，消息中心, 内外 DNS 。
      例如为了解决用户问题，有统一认证中心。
      这些都是现有“病”，后“开药”的解决方式。
      因为企业不可能单靠自己或者某一个实施商解决自己的全部问题，所以必须要让很多厂商来做。
      现在如果把粒度放小，就也有了我们所说微服务的概念：一个团队没有能力完成一整个系统。
      而现在更多是为了拆而拆，用实践去套理念，把简单的问题搞复杂。已经有点用烂了。
  - [小团队 适合用 k8s +Spring cloud +微服务吗 - V2EX](https://www.v2ex.com/t/733080)
    collapsed:: true
    - > 有专职的人员维护这套基础设施吗？
      没有的话，公司愿意为这套基础设施投入人力成本和机器成本吗？
      要是都没有，谁来背这套基础设施玩不转的的锅？
      > 做为技术人员，碰到这种新技术能实践，应该感到兴奋才对。选择成本恰当的技术方案应该是架构师头疼的事情，普通开发难道不是恨不得把业界最新方案全用上，好堆简历背景吗
    - > 单体够用就单体，如果非得上 单独 k8s，如果非要熔断 限流这些 直接上 istio + spring boot 。 下下策是 spring cloud +k8s
    - > 我们团队现在运行维护着一整套的 k8s 平台和微服务平台，遍布全球十几个数据中心，拥有 20+套集群，最近还合并了另一个团队的 devops 平台，感觉应该有点发言权
      > 其实用 k8s 和团队大小没有强对应关系，团队小就找两三台虚拟机搭一套小集群满足需求即可。我理解微服务所利用的 k8s 特性主要是实现滚动更新、灰度发布以及 hpa 等，还可以利用 cicd 工具一键发布，这些特性不用 k8s 甚至不用 springcloud 都能实现，只是现有比较成熟的方案的确是 k8s+springcloud 微服务。我建议楼主从最小需求做起，切忌过度架构，构建出的组件稳定可用满足最低需求即可。
      > 可以理解基于 k8s 的模块是一套 paas 平台，基于 springcloud 微服务的模块是 saas 平台(当然我们也基于 istio 构建了一套 service mesh 模块，那个才是真正的 sass 平台）。如果从开发角度，专注实现 saas 平台的基本功能就可以了，往后团队大了，面临的问题还有日志采集，服务监控，链路追踪，网关路由，容器网络管理，底层计算资源维护等等等等。
      > TLDR：最小化架构的话只要能给开发部署和发布版本带来便利即可，比如使用 jenkins/搭建 k8s 进行容器化的初步集成 /使用 k8s 滚动更新 /进行微服务改造并搭建 eureka 和 gateway 管理所有的微服务等等；再发展下去就可以考虑构建一个微服务平台（ SAAS ）来管理整个微服务的生命周期，包括链路追踪 /API DOC/服务间调用 /配置中心 /分布式事务等等；最终就是一整套 k8s 管理 /微服务管理 /Devops 管理的覆盖开发全开发生命周期的工具链集合。
  - [6 个不容错过！质量超高的Spring Cloud 实战项目_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1aw411R7ki/)
    collapsed:: true
    - PiggyMetrics https://github.com/sqshq/piggymetrics
    - 分布式电商项目 https://github.com/SiGuiyang/spring-cloud-shop
    - 轻松阅读微服务项目 api https://github.com/Zealon159/light-reading-cloud
    - SpringBlade 微服务开发平台 https://gitee.com/smallc/SpringBlade
    - Cloud-Platform https://gitee.com/geek_qi/cloud-platform
    - 互联网云快速开发框架 https://gitee.com/JeeHuangBingGui/jeeSpringCloud
  - [微服务架构有哪些组件？Istio将替代Spring Cloud？系统设计面试系列 - YouTube](https://www.youtube.com/watch?v=cxgiEtCN6tk)
  - Expanded
    collapsed:: true
    - [少走99%的弯路！阿里大佬花费156个小时整理的SpringCloud框架开发教程，整整300集，零基础快速入门！_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1rB4y1v7HB/)
    - [价值29800元的SpringCloud全家桶，2021最新微服务架构完整版讲解_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV17q4y177yt/)
    - ~~[1. 000-SpringCloud+Spring Cloud Alibaba 微服务知识点详解_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1a3411b7c4?p=1)~~
    - [为什么不使用dubbo？非要使用springcloud_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1zB4y1k7ss/)
-