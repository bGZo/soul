also:: RDF Site Summary, Really Simple Syndication
description:: a web feed that allows users and applications to access updates to websites in a standardized. computer-readable format
released-date:: 19990315
wikipedia:: https://en.wikipedia.org/wiki/RSS
tags:: #info

- The first time icon of RSS I see is in the CD show. I even don't know what exactly is it. It appeared in the product birthed in last 10 years in China mainland.
- And then, when I have some spare time in 2020, I notice it again. I wonder whether it have some interesting story or not. And at that point, I use a simple and not well reader to subscribe RSS. And just feeling amazing, and feel sad as well, like (by the way, they're sucks)
- If you host a RSS link, you've well done. I would appreciate you 😘
  -
- ## Why
  - Build self host info flow => only focus on some fields.
- ## How
  - TODO Backup and share your subscription.
    collapsed:: true
    SCHEDULED: <2024-05-01 Wed .+1m>
    :LOGBOOK:
    * State "DONE" from "DOING" [2023-02-05 Sun 00:51]
    * State "DONE" from "TODO" [2023-02-05 Sun 11:15]
    * State "DONE" from "TODO" [2023-02-05 Sun 11:23]
    * State "DONE" from "TODO" [2023-03-04 Sat 21:55]
    * State "DONE" from "TODO" [2023-04-01 Sat 21:47]
    * State "DONE" from "TODO" [2023-05-02 Tue 22:42]
    * State "DONE" from "TODO" [2023-06-02 Fri 15:51]
    * State "DONE" from "TODO" [2023-07-16 Sun 17:25]
    * State "DONE" from "TODO" [2023-08-05 Sat 19:06]
    * State "DONE" from "TODO" [2023-09-03 Sun 18:12]
    * State "DONE" from "TODO" [2023-10-03 Tue 00:39]
    * State "DONE" from "TODO" [2023-10-03 Tue 12:02]
    * State "DONE" from "WAITING" [2024-03-09 Sat 15:57]
    * State "DONE" from "WAITING" [2024-04-08 Mon 07:21]
    :END:
    - {{iframe https://gist.github.com/bGZo/f16fbc8d22cb77ae8078f8ac09234e03,300}}
      #+BEGIN_CENTER
      via: https://gist.github.com/bGZo/f16fbc8d22cb77ae8078f8ac09234e03/edit
      #+END_CENTER
  - DONE The amount of RSS feed supported by socal media is very few, no matter they are.
    collapsed:: true
    - We have [[RSSHub]]
  - WAITING Overdesign / design deliberatly, which is hard to fetch normally.
    collapsed:: true
    - 爬取方式
      - RSS 订阅（关闭全文输出）
      - [sawhney17/logseq-web-parser (github.com)](https://github.com/sawhney17/logseq-web-parser) #Logseq/plugin
    - Some website not support output full-text RSS, so we have to open in browser to read. Luckily, we could get full-text RSS through parse url, most rss reader support that. But even more, they change the output format of HTML, and they wouldn't support full-text fetch. You will always see following page:
    - I know they want to get more actual views, to get more money ads brings. But it's really likely say:
      > "Do you want me to tell this stuff?"
      "Suck my dick first, reader 😝"
    - They're not solving anything, and having put the situation more complex!
      collapsed:: true
      - ![https://blog.skk.moe/post/say-no-to-meta-keywords/](https://raw.githack.com/bGZo/assets/dev/2024/rss_close_full_text_example.png){:height 476, :width 579}
        via: [Sukka's Blog](https://blog.skk.moe/atom.xml)
  - How I connect each other tools and build [[workflow]]?
    collapsed:: true
    - ![](https://raw.githack.com/bGZo/assets/dev/2024/infoflow.excalidraw-fs8.png)
      #book #reading #writing #flow
      `[[draws/flow.book.excalidraw]]`
      - When rss failed/[[404]], go to [Inoreader - Take back control of your news feed](https://www.inoreader.com/). Subscribe, and find the old articles.
      - When you seeing a good source, you shouldn't subscribe immediately, you should save a read latter and done it as soon as possible. Because it will accumulate while  you don't care it. Yet it might be a instant source, so it will be spam in the future.
        collapsed:: true
        In deeper, *I take rss more than a reading tool, but their origional purpose, __notification__*.
        #thought
        - TODO How to build a good flow of reading latter? When I meet a good blog.
    - RSS  + **Raindrop + Export to Each Platform**
      - 依赖 Raindrop 的高亮导致无法在 RSS Reader 内阅读;
        - 我想划线高亮, 我就必须跳转到原网站去阅读,
          传统的 Rss Reader 全文抓取失去了意义
        - 稍后读 Read Latter 无所谓, 因为本来就打算在后者阅读
      - 参考同类竞品 [[Alternative]] [[tools]]
        - [简悦 SimpRead - 如杂志般沉浸式阅读体验的扩展](http://ksria.com/simpread/)
        - [Readwise](https://readwise.io/)
        - [Pocket: Home](https://getpocket.com/en/)
        - [Instapaper](https://www.instapaper.com/)
        - No more free 😭 I only could use raindrop.
  - How I handle the trash message?
    id:: 646a045c-74f6-49d4-bbce-78ec1484d73c
    - I devided the feed to 2 parts, including:
      - Instant messages, which would never take much time(See ((646a045c-74f6-49d4-bbce-78ec1484d73c)))
      - Uninstant messages, which I should read it alone. (moonight would be better)
        - I archived article without images using rsstt telegram bot.
        - I browser social media and most blog on another channel.
    - They have some general features:
      - Comments more than article
      - All page just worth a share link.
    - What I collect it
      collapsed:: true
      - [绅士之庭订阅源](https://gmgard.moe/rss)
      - [豆瓣 - 书评](https://www.douban.com/feed/review/book)
      - [Solidot](https://www.solidot.org/index.rss)
      - [ONE · 一个](https://rsshub.app/one)
      - [4Gamers](https://www.4gamers.com.tw/rss/latest-news)
      -
      - [游戏 – 琉璃神社 ★ HACG.me](https://www.hacg.mom/wp/game.html/feed)
      - [V2EX热门](https://rsshub.app/v2ex/topics/hot)
- ## What
  - Now when I looked back, I have used a lot of tools(See ((4dd1229b-d8a7-4599-b042-8e767800317e))), and have a lot of demands, I want to rebuild a tool, just like other tool in market.
    collapsed:: true
    - TODO Build yourself RSS reader
  - Some websites will include element whose type is `application/atom+xml` or `application/rss+xml`. They would include RSS link.
    - ```xml
      <link rel="alternate" type="application/atom+xml" title="${source.title}" href="${source.url}">
      ```
    - And following are some address they mostly used:
      - ```xml
        ./feed
        ./rss.xml
        ./feed.xml
        ./atom.xml
        ./rss/index.xml
        ./index.xml
        ./rss
        ./rss/rss
        ./rss/rss.xml
        <!-- Z-Blog via: https://bbs.zblogcn.com/thread-3527.html-->
        ./feed.asp?user=userID
        ./feed.asp?tags=TagID
        <!-- Youtube -->
        https://www.youtube.com/feeds/videos.xml?channel_id=<channel_id>
        https://www.youtube.com/feeds/videos.xml?playlist_id=<playlist_id>
        ```
  - RSS standards
    id:: 6469fd40-72d9-40e9-a326-528683ed0889
    - [RFC 4287 - The Atom Syndication Format](https://datatracker.ietf.org/doc/html/rfc4287)
    - [[opml]]
      collapsed:: true
      - Group with
        - Tags
          ```xml
          <?xml version="1.0" encoding="UTF-8"?>
            <opml version="1.0">
               <head>
                  <title>Opml Template</title>
               </head>
               <body>
                 <outline title="News" text="News">
                   <outline type="rss" text="title" xmlUrl="url" />
                 </outline>
               </body>
            </opml>
          ```
        - Attributes
          ```xml
          <?xml version="1.0" encoding="UTF-8"?>
            <opml version="2.0">
               <head>
                  <title>Opml Template</title>
               </head>
               <body>
                  <outline type="rss" text="title" xmlUrl="url" group="group/name" />
               </body>
            </opml>
          ```
    - XML like https://www.tiangal.com/feed
    - Atom like https://gmgard.moe/rss
  - What I used in past and recommand now
    id:: 4dd1229b-d8a7-4599-b042-8e767800317e
    - ✨ [GitHub - Rongronggg9/RSS-to-Telegram-Bot: A Telegram RSS bot that cares about your reading experience](https://github.com/Rongronggg9/RSS-to-Telegram-Bot)
    - ✨ [Feedbro - Chrome Web Store (google.com)](https://chrome.google.com/webstore/detail/feedbro/mefgmmbdailogpfhfblcnnjfmnpnmdfa?hl=en)
      collapsed:: true
      - But I prefer like the brave build-in RSS reader😭😭
    - ✨ [期待 V2RSS by angelia](https://v2rss.com)
    - ✨ Inoreader to browser feed history.
    - ---
      - [yang991178/fluent-reader: Modern desktop RSS reader built with Electron, React, and Fluent UI (github.com)](https://github.com/yang991178/fluent-reader)
      - [HenryQW/Awesome-TTRSS: [maintainer wanted] 🐋 Awesome TTRSS, a powerful Dockerised all-in-one RSS solution. (github.com)](https://github.com/HenryQW/Awesome-TTRSS)
      - [zhaoolee/garss: Github Actions采集RSS, 打造无广告内容优质的头版头条超赞宝藏页](https://github.com/zhaoolee/garss) ![](https://img.shields.io/github/stars/zhaoolee/garss)
      - [己思](https://ohmyrss.com/#)
      - ~~[gandf/slick-rss](https://github.com/gandf/slick-rss)~~
        - DONE with some userscripts due to some issues
          - When address is begin with `//xxx.com`, the final address will be `chrome-extension://xxx.com`, while it should be `http`. I try some ways but I am novice in javascript.
          - `//` only supported with server and extension actually run at local. `//` img cannot loaded and the http url is wrong as well.
            collapsed:: true
            - ```
              foo://example.com:8042/over/there?name=ferret#nose
              \_/   \______________/\_________/ \_________/ \__/
              |           |            |            |        |
              scheme     authority       path        query   fragment
              ```
              via: [Is it valid to replace http:// with // in a <script src="http://...">?](https://stackoverflow.com/questions/550038/is-it-valid-to-replace-http-with-in-a-script-src-http)
        - TODO I cannot replace target when all data has loaded. So I try to add a button to replace the RSS content, with [Content Security Policy - Chrome Developers](https://developer.chrome.com/docs/apps/contentSecurityPolicy/#relaxing-inline-script).
          ([cordova - The Content Security Policy 'default-src * data:;' was delivered via a  element outside the document's  - Stack Overflow](https://stackoverflow.com/questions/39657544/the-content-security-policy-default-src-data-was-delivered-via-a-meta-el))
          - Cannot run inline javescript
            - [How does inline JavaScript work with HTML ? - GeeksforGeeks](https://www.geeksforgeeks.org/how-does-inline-javascript-work-with-html/)
            - Solution
              - ```html
                <button id="myButton">Click me</button>
                <script src="script.js"></script>
                ```
                ```js
                document.getElementById("myButton").addEventListener("click", myFunction);
                function myFunction(){
                  console.log('asd');
                }
                ```
              - > In chrome apps, Content Security Policy does not allow inline javascript. So you have to put your javascript in a .js file and include it in your HTML.
                Further reading: [https://developer.chrome.com/extensions/contentSecurityPolicy](https://developer.chrome.com/extensions/contentSecurityPolicy)
                via: [javascript - Refused to execute inline event handler because it violates CSP. (SANDBOX) - Stack Overflow](https://stackoverflow.com/questions/36324333/refused-to-execute-inline-event-handler-because-it-violates-csp-sandbox)
        - Extra
          - [What are Bookmarklets? How to Use JavaScript to Make a Bookmarklet in Chromium and Firefox](https://www.freecodecamp.org/news/what-are-bookmarklets/)
          - TODO [异步 JavaScript 简介 - 学习 Web 开发 | MDN](https://developer.mozilla.org/zh-CN/docs/Learn/JavaScript/Asynchronous/Introducing)
          - JavaScript regex group replace?
            [regex - Javascript replace with reference to matched group? - Stack Overflow](https://stackoverflow.com/questions/1234712/javascript-replace-with-reference-to-matched-group)
            - ```js
              /**
              <div class="feedPreviewSummaryContent" style="max-height: 480px;">[img]https://img.imoutomoe.net/images/2022/12/06/35c17455f54a12950.jpg[/img]
              [img]https://img.imoutomoe.net/images/2022/12/06/4c015ed6fd28b52d2.jpg[/img]
              [img]https://img.imoutomoe.net/images/2022/12/06/52168fd40a039b8b4.jpg[/img]
              [img]https://cdn.cloudflare.steamstatic.com/steam/apps/1924680/heade ..</div>
              **/
              ```
  -