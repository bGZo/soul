alias:: 项目
mark:: any undertaking, carried out individually or collaboratively and possibly involving research or design, that is carefully planned to achieve a particular goal.
icon:: 📂
title:: project
created:: 20230623
title:: project

  - template:: project
    template-including-parent:: false
    collapsed:: true
    - ---
      alias:
      mark:
      icon: 📂
      tags: #project
      created: ``{ date.now.format('YYYYMMDD') }``
      title: ``{ c.page.name }``
      ---
    - ## Project Meta
      collapsed:: true
      - \DOING #project [[``{ c.page.name }``]]
      - query-table:: false
        collapsed:: true
        #+BEGIN_QUERY
        {:title [:h3 "Tasks related to ``{ c.page.name }``"]
         :query [:find (pull ?b [*])
             :in $ ?current-page
             :where
             [?p :block/name ?current-page]
             [?b :block/marker ?marker]
        [?p :block/alias ?al]
        (or [?b :block/refs ?p] [?b :block/refs ?al])
        (or
             [(= "NOW" ?marker)]
             [(= "DOING" ?marker)]
             [(= "WAITING" ?marker)]
             [(= "LATER" ?marker)]
        )
        (not [?b :block/page ?p])
        ]
         :inputs [:current-page]
          :result-transform (fn [result]
                              (sort-by (fn [b]
                                         (get b :block/priority "Z")) result))
          :breadcrumb-show? false
          :table-view? false
        }
        #+END_QUERY
      - query-table:: false
        collapsed:: true
        #+BEGIN_QUERY
        {:title [:h3 "Checklist"]
         :query (and (todo todo) (page [[``{ c.page.name }``]]))
          :result-transform (fn [result]
                              (sort-by (fn [b]
                                         (get b :block/priority "Z")) result))
          :breadcrumb-show? false
          :table-view? false
        }
        #+END_QUERY
    - ## Why
      collapsed:: true
      -
    - ## How
      collapsed:: true
      -
    - ## What
      collapsed:: true
      - ### \# Program Description
        - #### Input
          -
        - #### Output
          -
      - ### \# Alternatives
        -
      - ### \# Notes
        -
- query-table:: false
  #+BEGIN_QUERY
  {:title [:h3 "Tasks related to project"]
   :query [:find (pull ?b [*])
     :in $ ?current-page
     :where
     [?p :block/name ?current-page]
     [?b :block/marker ?marker]
  [?p :block/alias ?al]
  (or [?b :block/refs ?p] [?b :block/refs ?al])
  (or
     [(= "NOW" ?marker)]
     [(= "DOING" ?marker)]
     [(= "WAITING" ?marker)]
     [(= "LATER" ?marker)]
  )
  (not [?b :block/page ?p])
  ]
   :inputs [:current-page]
  :result-transform (fn [result]
                      (sort-by (fn [b]
                                 (get b :block/priority "Z")) result))
  :breadcrumb-show? false
  :table-view? false
  }
  #+END_QUERY
- query-table:: false
  #+BEGIN_QUERY
  {:title [:h3 "Checklist"]
   :query (and (todo todo) (page [[project]]))
  :result-transform (fn [result]
                      (sort-by (fn [b]
                                 (get b :block/priority "Z")) result))
  :breadcrumb-show? false
  :table-view? false
  }
  #+END_QUERY
-
- ## What
  - #+BEGIN_PINNED
    Wired Things Via [[geek]]
    #+END_PINNED
  - [[Issue]]
    - #Alternatives 替代品
      :LOGBOOK:
      CLOCK: [2022-11-05 Sat 15:42:51]
      :END:
      - WAITING Raindrop
        - [Matter](https://getmatter.app/)
        -
      - WAITING Mirror Site
        - Wikipedia
          - [维基媒体下载](https://dumps.wikimedia.org/)
          - [架设Wikipedia的本地镜像(Linux联盟收集整理)_CSDN博客](https://blog.csdn.net/zengxianghu/article/details/6472573)
        - via: [有一天物理断网，哪些东西是你要存储起来的 - V2EX](https://www.v2ex.com/t/876861)
      - WAITING [Browser History Unlimited](https://chromewebstore.google.com/detail/history-trends-unlimited/pnmchffiealhkdloeffcdnbgdnedheme)
        - > Will you make a version of the extension for Firefox?
          Yes, once it is possible to do so. Keep an eye on Firefox [issue 1673477](https://bugzilla.mozilla.org/show_bug.cgi?id=1673477). Once it is fixed, I should be able to port this extension to Firefox. And please see FAQ \#11: The extension is closed source, so forks are not allowed.
          >— [History Trends Unlimited - FAQ](https://sites.google.com/view/history-trends-unlimited/faq)
        - 两插件双向数据不互通，这个插件的数据无法导入 FF，FF上只有这个[替代](https://github.com/Christoph-Wagner/firefox-better-history-ng)
    - WAITING Music Studio
      - music.bgzo.cc -> My Favs
        - 完全静态的听歌网站
        - 版权问题?
    - WAITING [[MonthTopic]] Like Newsletter #[[writing]]
    - WAITING 完善 cms 系统
      - [韩剧tv-韩剧-韩剧网-韩剧TV官网-TSKS韩剧社-韩剧Tv](https://www.1vys.com/)
    - WAITING 聊天室 & 做一个匿名服务
      - [Volafile.org Live Filesharing & Chat](https://volafile.org/)
      - [hack.chat](https://hack.chat/)
      - 匿名社交媒体
        collapsed:: true
        - [Signal >> Home](https://signal.org/)
        - [MeWe - The Next-Gen Social Network](https://mewe.com/)
        - [Join the Premier Global Free Speech App | Parler](https://parler.com/)
        - [SafeChat – Build a better world](https://help.safechat.com/)
        - 匿名聊天室
        - 匿名邮箱
        - 匿名信息
    - WAITING [[sort]] 可视化
      - [如何可视化「排序算法」 - 知乎](https://zhuanlan.zhihu.com/p/31314248)
      - [数据结构和算法动态可视化 (Chinese) - VisuAlgo](https://visualgo.net/zh)
    - WAITING #ACGN Blog Theme / combine with origin blog?
      - 把 Git Blog 改造成为 Jekyll 博客
      - **重要特性**: 支持**搜索**
      - 博客 != 教程
        - 教程是需要长时间得到更新的, 因为东西总在变
        - 那到底要如何定义博客?
      - 支持更新时间排序
      - 信息半衰期时效提醒, "该信息已经过时"
      - 增加自动抓取的社交媒体的言论页面, 比如 Twitter, Github, BGM...
    - WAITING [BGM](https://bgm.tv) 全局通知
    - WAITING [[crawler]] JS
      - 优化正则爬虫, 使用 BeautifulSoup 库替换
      - [如何保存知乎某个问题的全部答案？ - 知乎](https://www.zhihu.com/question/24296318)
    - WAITING 贤者时间质问器
    - WAITING Imitate
      - 呼吸灯
      - 重力
      - VR
      - 全景
      - 横向展示
    - WAITING Convert BILIBILI video to podcast RSS to listen in background.
    - WAITING 物理控制器, 自己打碟
    - WAITING 各类 Generate 生成器构建
    - [[newsline]] #duplicate
    - ### ~~[[deprecated]]~~
      - DONE 常用文本管理. 随时调用
        mark:: 需求消失 / Bitwarden
        :LOGBOOK:
        CLOCK: [2021-09-26 Sun 22:16]
        :END:
      - **热词脚本**
        - 小鸡词典 https://jikipedia.com
        - 能不能好好说话？https://lab.magiconch.com/nbnhhsh/
      - **更新 Index 学习框架**
        - vue site https://v3.cn.vuejs.org/guide/introduction.html#%E8%B5%B7%E6%AD%A5
        - learning vue and create a nav guide site
        - source github: https://github.com/qq281113270/vue
      - **gui 关机程序**
        - C# Windows Client 关机小程序
      - **打包App => 压缩图片 输入到指定目录 脚本**
      - **拦截程序(火绒剑??) => 分析一下p2p修改书签恶意程序**
      - 缺省的表达式执行效率高: NULL & NULLPTR
      - 命令行参数 可能的含义
      - 磁盘显示情况的图片绘制
      - 研究 FF 的同步功能(API)
      - 感觉现在的网站都不会简单地把简单 API 暴露出来呀, 就单说知乎个人用户资料的 API 其实是抓不到的, 还是看别人提炼好的 API 才明白原来是这个😅, 这怎么解? via: [zhihu-api/url.py at 84d15bc7fc6fbf14fe4a170fb18aa0a132c213b3 · lzjun567/zhihu-api](https://github.com/lzjun567/zhihu-api/blob/84d15bc7fc6fbf14fe4a170fb18aa0a132c213b3/zhihu/url.py#L9)
      - Alias 命令其实应该把代理镜像地址全部加上... 这样就剩下偶尔需要查阅的必要了...
      - ((632088c6-5b31-4aca-8402-1fc71be7de8b))  ??? 纯虚类 是不是就是接口???
      - 怎么一键发布 Wordpress 站点, 官方不支持 Markdown 就很麻烦... 别人是怎么忍受的???
        - [我的主页 ‹ 生存日记 — WordPress.com](https://wordpress.com/home/bgzo.wordpress.com)
        - [WordPress+PublishMarkdown快速构建个人博客 - 知乎](https://zhuanlan.zhihu.com/p/105236218)
      - 单元测试
      - Mac虚拟机
        - 垃圾 Noteshelf, 为什么只给 Mac 做了适配, 更奇怪的是, 这好像是一个 windows 诅咒的怪圈, tm的几乎没有开发者对 windows 抱有好感. 这带来的软件的割裂真的让人非常匪夷所思和难受. 屮
        -
  -
  - TODO Lists
    collapsed:: true
    - https://cuvids.io/app/video/97/watch/ #[[books/algorithms4E]]
    - x86_64 Linux Assembly
      source:: https://www.youtube.com/playlist?list=PLetF-YjXm-sCH6FrTz4AQhfH6INDQvQSn
      collapsed:: true
      - {{video https://www.youtube.com/playlist?list=PLetF-YjXm-sCH6FrTz4AQhfH6INDQvQSn}}
    - Java源码盘起来！演示搭建JDK源码阅读环境，利用IDEA搭建Java源码阅读环境视频教程_哔哩哔哩_bilibili
      source:: https://www.bilibili.com/video/BV1V7411U78L
      collapsed:: true
      - {{video https://www.bilibili.com/video/BV1V7411U78L}}
    - 尚硅谷最新版JavaWeb全套教程,java web零基础入门完整版_哔哩哔哩_bilibili
      source:: https://www.bilibili.com/video/BV1Y7411K7zz?p=117
      collapsed:: true
      - {{video https://www.bilibili.com/video/BV1Y7411K7zz?p=117}}
      -
    - 5 ways to vertically center with CSS
      source:: https://www.youtube.com/watch?v=qJVVZYTYA9U
      collapsed:: true
      - {{video https://www.youtube.com/watch?v=qJVVZYTYA9U}}
    - 操作系统真相还原 via: [doctording/os: 《操作系统真相还原》笔记](https://github.com/doctording/os)
    - delftstack  https://www.delftstack.com/zh/tutorial/
    - 图论部分简介 https://oi-wiki.org/graph/
    - 闯关code GitHub - freeCodeCampfreeCodeCamp: freeCodeCamp.org's open-source codebase and curriculum. Learn to code for free. https://github.com/freeCodeCamp/freeCodeCamp
    - 学习路线图 GitHub - kamranahmedsedeveloper-roadmap: Roadmap to becoming a web developer in 2021 https://github.com/kamranahmedse/developer-roadmap
    - shellcode代码实战 https:/blog.csdn.net/u011569253/article/details/80529936
    - Fltk c++打包: https:/github.com/fltk/fltk
    - 30天js GitHub - Asabeneh-Days-Of-JavaScript: 30 days of JavaScript programming challenge is a step-by-step guide to learn JavaScript programming language in 30 days. https://github.com/Asabeneh/30-Days-Of-JavaScript
    - | Name | Url | Mark|
      |菜鸟教程|https://www.runoob.com||
      |Learn X in Y minutes|https://learnxinyminutes.com||
      |Learn to code|https://www.freecodecamp.org||
      |Exercism|https://exercism.org||
      ||https://javascript.info|JS|
      ||https://developers.google.com/web|JS|
      ||https://web.dev|JS|
      ||https://developer.mozilla.org|JS|
    - pixel 教程 MasterianoX制作的模型与材质教程 https://v2mcdev.com/posts/880.html
    - 怎么写读书报告？ - 知乎 https://www.zhihu.com/question/20937894/answer/702874466
    - SSH https://wangdoc.com/ssh/client.html
    - Go 编程 https://coolshell.cn/articles/21128.html
    - Css https://learnxinyminutes.com/docs/zh-cn/css-cn/
    - Webpack Document : https://webpack.docschina.org/guides/
    - TypeScript: https://learnxinyminutes.com/docs/zh-cn/typescript-cn/
      https://jspang.com/detailed?id=62
      https://learnxinyminutes.com/
    - telegram https://congcong0806.github.io/2019/04/11/Telegram/
    - 如果我买了一个树莓派，我能用这个树莓派干什么? http://39.97.9.130/card-zhihu-hot-list/view?id=3594
    - 如何选择适合的公共 DNS？  | Sukka's Blog https://blog.skk.moe/post/which-public-dns-to-use/
    - window  标签文档 http://cn.ejie.me/
    - Martyr2's Mega Project Ideas List! - Share Your Project | Dream.In.Code https://www.dreamincode.net/forums/topic/78802-martyr2s-mega-project-ideas-list/ 实现清单
    - 使用公共 DNS 上网的弊端（一） | Ephen‘s Blog https://web.archive.org/web/20181023062819/https://ephen.me/2017/PublicDns_1/
    - [violet7pan/XYplorer_Help: XYplorer使用教程-原创](https://github.com/violet7pan/XYplorer_Help) #[[Tool]]
    - https://github.com/mo-han/mo-han-toolbox/blob/f429a7d89d/__dump__/_x_segslice.py
    - mac 安装 在 virtualbox GitHub - myspaghettimacos-virtualbox: Push-button installer of macOS Catalina, Mojave, and High Sierra guests in Virtualbox for Windows, Linux, and macOS https://github.com/myspaghetti/macos-virtualbox
    - css集合 GitHub - QiShaoXuancss_tricks: Some CSS tricks,一些 CSS 常用样式 https://github.com/QiShaoXuan/css_tricks
    - git Flow https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
    - how to review code https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/
      https://google.github.io/eng-practices/review/reviewer/
    - github贡献图 https://www.sollrei.me/post/frontend/css-grid
      https://towardsdatascience.com/how-to-build-a-github-activity-dashboard-with-open-source-b3d60277e9a3
    - Javascript Game Foundations - Ten Essentials | Code inComplete js 开发游戏 https://codeincomplete.com/articles/javascript-game-foundations/
    - [FISHers6/CS-LogN: CS-LogN计算机知识思维导图](https://github.com/FISHers6/CS-LogN)
    - 安卓沙盒 https://github.com/asLody/VirtualApp
    - 命令监视器 学习协议 GitHub - aristocratosbtop: A monitor of resources https://github.com/aristocratos/btop
    - css 库 GitHub - necolasnormalize.css: A modern alternative to CSS resets https://github.com/necolas/normalize.css
    - Docs | Open-Meteo.com 天气免费API https://open-meteo.com/en/docs
  -