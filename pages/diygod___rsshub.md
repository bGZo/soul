alias:: 
created::  [[20240324]]
tags:: #github/repo #rss
source:: https://github.com/DIYgod/RSSHub
![](https://img.shields.io/github/stars/DIYgod/RSSHub)

- ## Why
- ## How
- WAITING I really want to contribute [RSSHub](https://docs.rsshub.app/joinus/quick-start.html) 😭
  - ~~`JSON` to `RSS`~~
    collapsed:: true
    - 需求消失 -> 监控某些 API 的变化 -> 学习 RSSHUB 路由编写规则
    - [RSS--一个古老、小众的阅读方法_CrazyDragon_King的博客-CSDN博客](https://blog.csdn.net/qq_40734247/article/details/105416907)
      description:: 转换方法只针对某个版本的 RSS XML 文件, 适用性不强
      collapsed:: true
      - ```xml
        <?xml version="1.0" encoding="utf-8" ?>
        <?xml-stylesheet type="text/xsl" title="XSL Formatting" href="/static_files/rss/rss.xsl" media="all" ?>
        <rss version="2.0">
            <channel>
                <title>xxx</title>
                <image>
                  xxx
                </image>
                <description>xxx</description>
                <link>xxx</link>
                <language>zh-cn</language>
                <generator>xxx</generator>
                <ttl>5</ttl>
                <copyright>
                    <![CDATA[Copyright &copy; ]]>
                </copyright>
                <pubDate>2020/04/09 18:28:27</pubDate>
                <item>
                    <title>
                        <![CDATA[[原]HttpClient的Fluent API]]>
                    </title>
                    <link>xxx</link>
                    <guid>xxx</guid>
                    <author>xxx</author>
                    <pubDate>2020/04/01 18:10:39</pubDate>
                    <description>
                        <![CDATA[
                            Fluent API
                                As of version of 4.2 HttpClient comes with an easy to use facade API based on the concept of a fluent interface. Fluent facade API exposes only the most fundamental functions of HttpClient...                    <div>
                            ]]>
                    </description>
                    <category></category>
                </item>
            </channel>
        </rss>
        ```
      - ```xml
        <feed>
        <generator uri="https://jekyllrb.com/" version="4.3.2">Jekyll</generator>
        <link href="/feed.xml" rel="self" type="application/atom+xml"/>
        <link href="/" rel="alternate" type="text/html"/>
        <updated>2023-01-22T16:21:23+00:00</updated>
        <id>/feed.xml</id>
        <title type="html">bGZo’s blog</title>
        <subtitle>Small is beautiful, less is more.</subtitle>
        <author>
        <name>bGZo</name>
        </author>
        <entry>
        <title type="html">Existence is suffering</title>
        <link href="/existence-is-suffering.html" rel="alternate" type="text/html" title="Existence is suffering"/>
        <published>2023-01-21T00:00:00+00:00</published>
        <updated>2023-01-21T00:00:00+00:00</updated>
        <id>/existence-is-suffering</id>
        <content type="html" xml:base="/existence-is-suffering.html">
        xxx
        </content>
        <author>
        <name>bGZo</name>
        </author>
        <category term="thoughts"/>
        <summary type="html">
        xxx
        </summary>
        </entry>
        ```
    - via: [jsonfeed-to-rss - npm](https://www.npmjs.com/package/jsonfeed-to-rss)
- ## What
  - collapsed:: true
    > 为什么 RSSHub 里的图片 / 视频加载不出来？
    - RSSHub 里的图片 / 视频地址都是源站地址，部分有防盗链，所以 RSSHub 给图片加了`referrerpolicy="no-referrer"`  属性来**防止跨域问题**，但部分 RSS 服务会自作主张去掉这个属性，如 Feedly、Inoreader，在它们的网页端图片会触发跨域加载不出来。同时，视频目前没有类似的属性，因此大部分阅读器都无法通过防盗链检查。下面是一些解决方案：
      - 使用不发送 Referer 的阅读器，如 [Inoreader 网页版 (opens new window)](https://www.inoreader.com/)配合[禁用 Referer 的 user script (opens new window)](https://greasyfork.org/zh-CN/scripts/376884)、[RSS to Telegram Bot (opens new window)](https://github.com/Rongronggg9/RSS-to-Telegram-Bot)等。如果你的阅读器能够绕过防盗链成功播放内嵌视频，那么它就是不发送 Referer 的，请考虑添加到文档里帮助更多的人。
      - 设置反代，参考 [通用参数 -> 多媒体处理](https://docs.rsshub.app/parameter.html#duo-mei-ti-chu-li)。
      - 回到原网站查看相关资源
  - collapsed:: true
    > 没有我想订阅的网站怎么办嘤嘤嘤 QAQ
    - 如果你会写 JavaScript，请按照[规则](https://docs.rsshub.app/joinus/quick-start.html#ti-jiao-xin-de-rsshub-gui-ze)提交 pull request，否则按照要求[提交 issue (opens new window)](https://github.com/DIYgod/RSSHub/issues/new?template=rss_request_zh.md)，然后等待有缘人完成你的需求，也可以考虑[赞助项目](https://docs.rsshub.app/support)或附上一张你自己的女装照来获得更快的 issue 响应速度。
  - If the [official website](https://rsshub.app/) is blocked, we could try to use following site:
    collapsed:: true
    - https://plink.anyfeeder.com ![](https://img.shields.io/website.svg?label=&url=https://plink.anyfeeder.com)
      logseq.order-list-type:: number
    - https://rsshub.bgzo.cc ![](https://img.shields.io/website.svg?label=&url=https://rsshub.bgzo.cc)
      logseq.order-list-type:: number
    - https://rss.shab.fun  ![](https://img.shields.io/website.svg?label=&url=https://rss.shab.fun)
      logseq.order-list-type:: number
    - https://rss.injahow.cn ![](https://img.shields.io/website.svg?label=&url=https://rss.injahow.cn)
      logseq.order-list-type:: number
    - https://i.scnu.edu.cn/sub ![](https://img.shields.io/website.svg?label=&url=https://i.scnu.edu.cn/sub)
      logseq.order-list-type:: number
    - https://rssforever.com ![](https://img.shields.io/website.svg?label=&url=https://rssforever.com)
      logseq.order-list-type:: number
    - https://rsshub-gilt-nine.vercel.app ![](https://img.shields.io/website.svg?label=&url=https://rsshub-gilt-nine.vercel.app)
      logseq.order-list-type:: number
    - https://rsshub.uneasy.win ![](https://img.shields.io/website.svg?label=&url=https://rsshub.uneasy.win)
      logseq.order-list-type:: number
  - [通用参数 | RSSHub](https://docs.rsshub.app/parameter.html)
  - [常见问题 | RSSHub](https://docs.rsshub.app/faq.html)
-
-
-