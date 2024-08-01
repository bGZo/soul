icon:: 📂
created:: [[20230614]]
description:: 一句
tags:: #quote 
type:: product

- ## Project Meta
  - DOING #project [[one-wisdom]]
    :LOGBOOK:
    CLOCK: [2024-07-21 Sun 22:36:48]
    :END:
  - query-table:: false
    #+BEGIN_QUERY
    {:title [:h3 "Tasks related to one-wisdom"]
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
    :query (and (todo todo) (page [[one-wisdom]]))
    :result-transform (fn [result]
                        (sort-by (fn [b]
                                   (get b :block/priority "Z")) result))
    :breadcrumb-show? false
    :table-view? false
    }
    #+END_QUERY
- ## V1.0 released at [[20230101]]
  collapsed:: true
  - {{iframe https://one.bgzo.cc,40vh,iframe-radius}}
  - {{iframe https://blog.bgzo.cc/one-wisdom-sentence-released.html,40vh,iframe-radius}}
    collapsed:: true
    - 2023 新年伊始, 整理 2022 的陈年笔记时发现有很多不知名, 但是又舍不得丢弃的句子, 想着干脆把他们做成引用得了. 连着建仓库, 设计页面, 写脚本一套下来也没花太多时间, 一个简单的静态自动部署的网站就建好了: [One](https://one.bgzo.cc/)[^2].
    - ![](https://unpkg.com/bgzo@23.1.1/img/one-preview.png)
    - ## Highlights
      - [x] Every single page for quote; Detail[^1] is following:
      - <p class="codepen" data-height="300" data-default-tab="html,result" data-slug-hash="wvxWKZb" data-user="bgzo" style="height: 300px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;">
        <span>See the Pen <a href="https://codepen.io/bgzo/pen/wvxWKZb">
        quotes</a> by bGZo (<a href="https://codepen.io/bgzo">@bgzo</a>)
        on <a href="https://codepen.io">CodePen</a>.</span>
        </p>
        <script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>
      - [x] Generate quote by syncing Github issues with metadata;
      - [x] Deploy with [Vercel](https://vercel.com)
      - [x] SEO supported by plugin.
- ## Why
  - 有大量的引用，来不及回顾，但是又希望分享出去，我相信这是中文互联网中文用户的普遍现状，市面上也存在着大量的产品，作为树洞收集者我们的话语，这只是我的一种实现方式而已。
- ## How
  - V1.0 Jekyll + Github Action
  -
- ## What
  - ### \# Program Description
    - TODO #feat 无需重新构建，首页的句子也可以随机变换；
    - TODO #feat 添加分析器 [Analytics](https://analytics.google.com/analytics/web/#/a252954726p347875136/admin/changehistory/account)
      :LOGBOOK:
      CLOCK: [2023-01-03 Tue 09:07:31]
      CLOCK: [2023-01-03 Tue 09:07:33]
      :END:
    - TODO #feat 支持拷贝分享链接；
    - TODO #feat 添加标签支持
      :LOGBOOK:
      CLOCK: [2023-01-03 Tue 09:07:51]
      :END:
      - [File: README — Documentation for jekyll-tagging (1.1.0)](https://rubydoc.info/gems/jekyll-tagging/frames)
      - [Jekyll Tags on Github Pages · Long Qian](https://longqian.me/2017/02/09/github-jekyll-tag/)
    - TODO #pref 适配手机显示；
    - TODO #pref 当后期引用数量激增，如何保证页面流畅，稳定？[^3]
      - Jekyll 天然支持分页较差（或者我不会写查询？）
  - ### \# Alternatives
    -
  - ### \# Notes
    -
- ## ↩ Reference
  -
-
-
- ## V 2.0
- ## Reference
  - [^1]: Page design parody for [Words of Wisdom](https://wordsofwisdom.app/);
    [^2]: Name inspired by [「ONE · 一个」](https://wufazhuce.com/);
    [^3]: Jekyll is just a static website generation. Seem like impossible to deliver value from jekyll to js. More discuss via: [Jekyll - display a random chosen post in index - Stack Overflow](https://stackoverflow.com/questions/31490789);
-