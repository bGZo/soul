blog:: [Logseq Blog](https://blog.logseq.com/)
changelog:: [Changelog](https://docs.logseq.com/#/page/changelog); [docs/Changelog.md](https://github.com/logseq/docs/blob/master/pages/Changelog.md?plain=1)
community:: [Logseq Community Hub](https://hub.logseq.com/);
document:: [Official Docs](https://docs.logseq.com/); [Unofficial Docs](https://mschmidtkorth.github.io/logseq-msk-docs)
created:: 20210801
tags:: #Tools
collapsed:: true
title:: Logseq

- ## Why
  - I hate some applications I used in past (See ((6474b5b1-ad1a-47c3-bc2c-4343950295a9))), they suck in a while, including [[Privacy]], [[censor]], with high [[price]] and bullshit user agreement.
    - ((64772db8-4367-4d35-b2ca-fed0e45bdd2c))
  - Basically, it's better that encoding with txt and search in [[vscode]]. I used it in the past but I was dropped in the category hell. When I finish a note last two months, and I have no idea where are they stored. The category I organized is terrible. And the ((6474b5f9-a287-48d9-a097-3400b8de53f7)). I like it.
  - I've learned a lot of things, not only how to note, how to remember, but also a few philosophy of organizing the whole [[knowledge]] system. (See ((646ad604-3548-4c57-a41a-4c551df8a8cc)))
- ## How
  - How to use logseq fully? What's the design they are? #.ol
    - The configuration, stored in `config.edu` file, which included  a few functions hidden: #.ol
      collapsed:: true
      - [Feature: add codemirror options by andelf · Pull Request #3699 · logseq/logseq](https://github.com/logseq/logseq/pull/3699) via: 
        collapsed:: true
        [Make it easy to configure syntax highlighting theme? - Questions & Help - Logseq](https://discuss.logseq.com/t/make-it-easy-to-configure-syntax-highlighting-theme/4617)
        - title:: [codemirror/codemirror5: In-browser code editor (version 5, legacy)](https://github.com/codemirror/codemirror5) ![](https://img.shields.io/github/stars/codemirror/codemirror5)
          tags:: #Github #opensource 
          created:: 20230531
      - [Specify Indentation Type & Changing The Default Font - Questions & Help - Logseq](https://discuss.logseq.com/t/specify-indentation-type-changing-the-default-font/2703/6)
        collapsed:: true
        - ```edu
           :export/bullet-indentation :two-spaces
          ```
        - collapsed:: true
          ```shell
          find . -name '*.md' ! -type d -exec bash -c 'expand -t 2 "$0" | sponge "$0"' {} \;
          ```
          - Required
            collapsed:: true
            - ```shell
              $ sudo apt install moreutils # sponge
              ```
          - Bug
            collapsed:: true
            - `Version GLIBC_2.33 not found` => package not correct installed
          - How to install package from source manually? #Issue
            collapsed:: true
            - Not possible... Seem like, need to install wget, then install manually...
              collapsed:: true
              - via: [apt - Install package from without adding PPA - Ask Ubuntu](https://askubuntu.com/questions/446774/install-package-from-without-adding-ppa)
            - sponge from https://joeyh.name/code/moreutils/
    - Tags [[vs]] Linked pages
      collapsed:: true
      - Basically, the page tagged is more special then linked pages. Then done. That's all. The sense I meet are the same thing.
      - Logseq change a lot, including the order shown by default, like hierarchy only could show one and they will not be the current page. It sucks a little.
        collapsed:: true
        - Property Format
          - Property will be parsed as delimiter in past and now it could be using \"\".
          - via: [Quote string properties still get comma delimiter when a page reference exists · Issue #3747 · logseq/logseq](https://github.com/logseq/logseq/issues/3747)
      - [The difference between ((page links)), #tags, and properties:: - Documentation - Logseq](https://discuss.logseq.com/t/the-difference-between-page-links-tags-and-properties/8393)
      - {{video https://www.youtube.com/watch?v=FQg52aN19w8}}
    - Filename specification logseq used.
      collapsed:: true
      - Basically, organize file structure & name is a difficult thing. Each time I change the page name and it would create the copied, so I have to delete it again. It's disappear in recent version.
      - Nouns is a awful suggestion, I lost many unlinked check...
      - use `___` or not
      - Which Version Change filename slash to `%2F`...
        collapsed:: true
        - [Is it possible change the encoded slah %2F character in the file names of names spaces? - Questions & Help - Logseq](https://discuss.logseq.com/t/is-it-possible-change-the-encoded-slah-2f-character-in-the-file-names-of-names-spaces/8037/5)
    - A few properties hidden by default.
      collapsed:: true
      - `collapsed`
      - `template-including-parent`
      - > `query-properties:: [:book-title :author :series]`
        via: [Specify column order in query table view - Questions & Help - Logseq](https://discuss.logseq.com/t/specify-column-order-in-query-table-view/8877)
      - >`:table-view`  can have one of the following values:
        nil — default, show property button
        true — table view, hide the button
        false — regular view, hide the bbutton
        more via: [(Partial Done) Hide query-table property heading - Feature Requests - Logseq](https://discuss.logseq.com/t/partial-done-hide-query-table-property-heading/4296/6)
    - Presentation
      background-image:: https://images.unsplash.com/photo-1498855926480-d98e83099315
      collapsed:: true
      - Logseq Plugin | 插件
        - title:: [shady2k/logseq-inbox-telegram-plugin](https://github.com/shady2k/logseq-inbox-telegram-plugin) ![](https://img.shields.io/github/stars/shady2k/logseq-inbox-telegram-plugin) 
          tags:: #Github #opensource 
          created:: 20221120
          - ~~Enable journals cause https://github.com/shady2k/logseq-inbox-telegram-plugin.~~
            collapsed:: true
            #Telegram #Deprecated
            - I think the journals more like tasks with #[[gtd]]
          - Sub block will gone #Issue
            - Test case:
              collapsed:: true
              - ```
                Test
                  * sub test
                    * sub test
                
                Here show something
                
                Test
                  + sub test
                    + sub test
                
                Here show something
                
                - Test
                  - sub test
                    - sub test
                
                Here show something
                ```
                Get:
            - Solution:
              collapsed:: true
              - Regex. Turn `(^[ ]*)-` to `$1\-`/`$1+`/`$1*`
              - Looking in logseq how to write original format.
      - [The HTML presentation framework | reveal.js](https://revealjs.com/)
      - But it only support show until **level 2**
    - title:: [shady2k/logseq-inbox-telegram-plugin](https://github.com/shady2k/logseq-inbox-telegram-plugin) ![](https://img.shields.io/github/stars/shady2k/logseq-inbox-telegram-plugin)
      tags:: #Github #opensource
      created:: 20221120
      collapsed:: true
      - ~~Enable journals cause https://github.com/shady2k/logseq-inbox-telegram-plugin.~~
        collapsed:: true
        #Telegram #Deprecated
        - I think the journals more like tasks with #[[gtd]]
      - Sub block will gone #Issue
        - Test case:
          collapsed:: true
          - ```
            Test
              * sub test
                * sub test
            
            Here show something
            
            Test
              + sub test
                + sub test
            
            Here show something
            
            - Test
              - sub test
                - sub test
            
            Here show something
            ```
            Get:
        - Solution:
          collapsed:: true
          - Regex. Turn `(^[ ]*)-` to `$1\-`/`$1+`/`$1*`
          - Looking in logseq how to write original format.
    - `/embed Youtube video` with **timestamp**
      collapsed:: true
      - URL with \#t=XhYmZs \?t=XhYmZs
      - Right click to select copy this position
    - [Online LaTeX Equation Editor - create, integrate, download](https://latex.codecogs.com) #[[latex]] #[[bookmark]]
    - `@@` use html code!
    - There are many tools [[Deprecated]] as following, #Closed  #.ol
      collapsed:: true
      - [Zotero | Your personal research assistant](https://www.zotero.org/)
        - **Alternatives**
          - **SingleFile**, (Fuck SingleFileZ)
          - [一个科研狗开发的文献管理软件 Paperlib - V2EX](https://www.v2ex.com/t/861794)
        - [Citation Needed: How to Use Logseq's Zotero Integration](https://blog.logseq.com/citation-needed-how-to-use-logseqs-zotero-integration/)
        - 1.Not Support **full-text search**, worse than VSCode🙄
          - [searching (Zotero Documentation)](https://www.zotero.org/support/searching)
        - 2.Note 功能 和 Logseq 高度**耦合**
        - 3.数据库同步数据会随知识库的增加而呈好几个数量级上涨;
          - 单文件 sql 会变得无比肿胀
        - 4.功能陈旧
          - 就拿个批量删除 RSS 数据源来说, 还需要自己写个脚本的; 
            via: [Feed clean-up - Zotero Forums](https://forums.zotero.org/discussion/comment/413650/);
        - 5.迁移成本巨大;
        - 6.常驻后台 + Extension;
      -
      - [简悦 + Logseq + Github Page 无代码全自动化知识管理发布方案 · Kenshin/simpread · Discussion #3426](https://github.com/Kenshin/simpread/discussions/3426)
        collapsed:: true
        - 常驻内存 + 功能付费 + markdown 输出模板
      - Hierarchies / HashTags | 层级 / 标签
        collapsed:: true
        - 这一功能只适用于进行快速搜索，一点也不适合把大段连续的知识打散的情况，因为如果一有要修改的想法，就要大刀阔斧地进行修改，VSCode 做起来还好，Logseq做起来就是受苦。
        - title + hierarchy **不会**出现在 Linked References 中
        - alias + hierarchy **会**出现在 Linked References 中
        - So... 这只是一个重新分配名空间 (Namepace) 的问题
          collapsed:: true
          - 在 [Namespaces](https://mschmidtkorth.github.io/logseq-msk-docs/#/page/namespaces) 中是整理知识 (当然他的 说明/文档 非常简单...)
          - 在 [Use Namespaces to Create a Dynamic Note Index in Logseq - YouTube](https://www.youtube.com/watch?v=fm45fG3A-Q4) 的更多的是 (层级)搜索
            collapsed:: true
            - 视频结尾说明一个更多的好处就是**在每次层级改变的时候, 只需要变更 Hashtag, 而不是将内容从一个文件搬运到另一个文件** (我是后者hhh)
  - The page exported by default is not included plugin setting. The better way is writing it in `custom.css`. I maintain a simple [Solarized](https://ethanschoonover.com/solarized/) [theme](https://gist.github.com/bGZo/b36c594b75499284d953bc2314d8e0b5). And here is my changelog: #changelog/wiki
    collapsed:: true
    - Font 
      created:: 20221015
      collapsed:: true
      - [Basic UI Settings e.g. Font Size - Feature Requests - Logseq](https://discuss.logseq.com/t/basic-ui-settings-e-g-font-size/2946/25)
      - [Specify Indentation Type & Changing The Default Font - Questions & Help - Logseq](https://discuss.logseq.com/t/specify-indentation-type-changing-the-default-font/2703/5)
    - Tags 
      created:: 20221118
      collapsed:: true
      - ```css
        a.tag[data-ref="star" i]::before {
          content: "⭐️";
          visibility: visible;
          border-radius: 2px;
          padding: 2px;
          background: red;
          box-shadow: 0 0 4px red;
        }
        
        a.tag[data-ref="star" i] {
          visibility: hidden;
          width: 24px;
          white-space: nowrap;
        }
        ```
        via: [Custom tags rendering with Emojis - Look what I built - Logseq](https://discuss.logseq.com/t/custom-tags-rendering-with-emojis/709)
      - [🙏 How do I change some tag colours? - Questions & Help - Logseq](https://discuss.logseq.com/t/how-do-i-change-some-tag-colours/637)
  - WAITING `equb` 全文搜索
    collapsed:: true
    - 连  Calibre 也不支持, 但是逆天的是 Weread 支持! 不知道之后市面上能不能出一款支持的, 目前有印象的还有 Google Book, 对关键词的搜集太急需了.
  - WAITING LS ==query function== count of rows (how to show results-count in variable)?
  - WAITING How to ==query== the number of sub blocks?
    collapsed:: true
    - `{{query block (page <% current page %>)}}`
    - How to logseq fuzzy query?
    - logseq query number of subblocks
    - [Queries](https://docs.logseq.com/#/page/queries)
    - [Advanced Queries](https://docs.logseq.com/#/page/advanced%20queries)
    - [The option to show block references on the graphview - Feature Requests - Logseq](https://discuss.logseq.com/t/the-option-to-show-block-references-on-the-graphview/3814/16)
    - [logseq variable current-block - Google Search](https://www.google.com/search?q=logseq+variable+current-block)
    - [Query for blocks with a specific parent on the current page - Questions & Help - Logseq](https://discuss.logseq.com/t/query-for-blocks-with-a-specific-parent-on-the-current-page/8284)
      collapsed:: true
      - ```
        #+BEGIN_QUERY
        { :title "Current Members"
          :query [:find (pull ?b [*])
                  :in $ ?current-page
                  :where
                  [?b :block/page ?p]
                  [?p :block/name ?current-page]
                  [?b :block/parent ?parent]
                  [?parent :block/content "Members"]]
          :inputs [:current-page] }
        #+END_QUERY
        ```
    - [Advanced queries and the database documentation? - Questions & Help - Logseq](https://discuss.logseq.com/t/advanced-queries-and-the-database-documentation/1542/3)
      collapsed:: true
      - Find all blocks referencing the page: `[Logseq]`, `_Logseq` or `tags`::` Logseq`.
      - `{{query [Logseq]}}`
      - Find all pages with page tags `tags`::` book` .
      - `{{query (page-tags book)}}`
      - Find all pages with both page tags `logseq` & `queries`.
      - `{{query (and (page-tags logseq) (page-tags queries))}}`
      - Find all pages with page tags `logseq` or `queries`
      - `{{query (page-tags logseq queries)}}`
      - Find all Todo blocks `doing` or `now`
      - `{{query (todo doing now)}}`
      - Find Todo blocks done in last 7 days.
      - `{{query (and (todo done) (between -7d today))}}`
      - Find all Todo/Doing Now/Later blocks in current page.
      - `{{query (and (todo todo doing now later) (page <% current page %>))}}`
      - Find all Todo/Doing Now/Later blocks where `tiensonqin` was tagged.
      - `{{query (and (todo todo doing now later) [tiensonqin]) }}`
    - [Query for co-occurences in property - Look what I built - Logseq](https://discuss.logseq.com/t/query-for-co-occurences-in-property/5448/10)
    - [Advanced Query: Blocks excluding certain tag - Questions & Help - Logseq](https://discuss.logseq.com/t/advanced-query-blocks-excluding-certain-tag/3173)
    -
  - WAITING How to ==query== with alias and tags?
    collapsed:: true
    - Multi Tags
      collapsed:: true
      - ```clojure
        {{query (and [[tag1]] [[tag2]] )}}
        ```
      - ```clojure
        #+BEGIN_QUERY
        {:title "All todos with tag project"
         :query  [:find (pull ?b [*])
             :where
             [?b :block/path-refs [:block/name "2021w34"]]
             [?b :block/path-refs [:block/name "prm"]]
            ]}
        #+END_QUERY
        ```
      - ```clojure
        #+BEGIN_QUERY
        {:title [:h2 "✔ Doing"]
         :query [:find (pull ?b [*])
               :where
               (task ?b #{"DOING"})]
        }
        #+END_QUERY✔ Focus On
        
        #+BEGIN_QUERY
        {:title [:h2 "✔ To Do"]
         :query [:find (pull ?b [*])
               :where
               (task ?b #{"TODO"})]
        }
        #+END_QUERY✔ Focus On
        
        {{query [[waiting-todo]] }}
        
        #+BEGIN_QUERY
        {:title [:h2 "Waiting ToDo"]
         :query  [:find (pull ?b [*])
             :where
             [?b :block/path-refs [:block/name "waiting-todo"]]
            ]}
        #+END_QUERY
        ```
    - [Logseq query with a custom view](https://www.loom.com/share/d007932e94db4b4981cca606bebdb54a)
    - [Logseq queries example (using properties) and custom view](https://gist.github.com/tiensonqin/b319e19e6a1ef4659f24bb3b71d3d025)
  - WAITING How to open the deleted page recently directly?
  - WAITING [Image asset as page icon - Feature Requests - Logseq](https://discuss.logseq.com/t/image-asset-as-page-icon/3826)
    collapsed:: true
    - [yoyurec/logseq-awesome-links: Icons for links. Logseq Plugin](https://github.com/yoyurec/logseq-awesome-links#-journal-icon)
    - ((6374947b-7716-4507-8561-f6c91e6d6fa4))
  - WAITING How to delete a unused file ?
    collapsed:: true
    - Plugin I think, cause just find wiki for file name is enough.
    - via: [How to clean unlinked files in an effective way - Questions & Help - Logseq](https://discuss.logseq.com/t/how-to-clean-unlinked-files-in-an-effective-way/2125)
  - WAITING Default template stored in `config.edu` is not supported for page, only for journal
    collapsed:: true
    - [I got the error message "Looks like you've been doing that a lot. Take a break for 5 minutes before trying again." when posting my first thread in 8 days. : help](https://www.reddit.com/r/help/comments/nh2tsy/i_got_the_error_message_looks_like_youve_been/)
    - [Can you create a template for your DAY page? : logseq](https://www.reddit.com/r/logseq/comments/q0ysh5/can_you_create_a_template_for_your_day_page/)
    - [How to Set Up an Automated Daily Template in Logseq](https://thinkstack.club/how-to-set-up-an-automated-daily-template-in-logseq/)
  - WAITING The "HTTP" will be crashed, how to avoid?
  - DONE Publish making web html 2022-05-12
    collapsed:: true
    - https://logseq.github.io/#/page/publishing%20(desktop%20app%20only)
- ## What
  - What I used in past #.ol
    id:: 6474b5b1-ad1a-47c3-bc2c-4343950295a9
    collapsed:: true
    - [onenote](https://www.onenote.com)
    - [youdao](https://note.youdao.com/web)
    - [wiz](https://note.wiz.cn/)
    - [yuque](https://www.yuque.com)
    - [cnblog](https://www.cnblogs.com/)
    - [csdn](https://blog.csdn.net)
    - [wordpress](https://cn.wordpress.org)
    - [typecho](http://typecho.org)
    - [bitcron](https://www.bitcron.com/)
    - [hexo](https://hexo.io/zh-cn)
    - [gitbook](https://www.gitbook.com/)
    - [mkdics](https://www.mkdocs.org)
    - [blogger](https://www.blogger.com)
    - [hugo](https://gohugo.io)
    - [notion](https://www.notion.so/)
    - [obsidian](https://obsidian.md)
    - [logseq](https://logseq.github.io)
  - Logseq gives us a vision we could organize
    id:: 6474b5f9-a287-48d9-a097-3400b8de53f7
    collapsed:: true
    - Journals in each day
    - Using bi-directional links and graph to connect.
      - Although it's really slow.
  - [笔记软件为何需要本地存储？ - Skywind Inside](https://www.skywind.me/blog/archives/2582) 
    id:: 64772db8-4367-4d35-b2ca-fed0e45bdd2c
    collapsed:: true
    - 不要忘记历史：
      - Evernote：导出备份的 .enex 文件， 再导入时提示有几篇日志图片 太多，没有会员无 法导入。
      - 印象笔记：用户因为从 Evernote 导入到印象笔记时触发了一个 BUG，五年笔 记丢失。新版本禁止导出公开格式的 .enex 文件，只能导出自己加密的 .note 格式，别的软件无法识别，只能映像笔记自己导出导入。
      - Notion：因为服务器在境外，偶尔会有无法访问的情况。未来有被墙的风险。
      - ==Wolai==：CEO 公开声称用户上传非法信息要报警。CEO 公开声称自己审查用户笔记。公开挂程面试序员的隐私信息。
      - 百度：百度盘扫描用户上传文件并做精准广告推送（上传证件图片的人被推荐电子证件钱包） 百度盘替换用户视频，换成净网行动的宣传视频。
      - 某在线文档：用户用在线编辑的文稿，因为保存到在线云盘，数日后触发关键字被删除。
      - 语雀：本来免费的，近期突然宣布新的收费策略，规定免费用户总文档数量不能超过 100 篇（包括小记、文档、数据表、表格、画板等），见这里：[如何看待语雀付费策略](https://www.zhihu.com/question/562238887)？遭到大量投诉后又改为：免费用户每月 100篇，还是无法分享。
    - 当年 github 就是天天被码云投诉，然后被墙掉了（不一定全是因为它，但它投诉了不少）；现在码云又在投诉仅有的 gitlab ，oschina 上天天看得到 gitlab 的黑文章，比如：
    - [扒一扒极狐 GitLab 的底裤 – OSCHINA – 中文开源技术交流社区](https://www.oschina.net/news/201455)
    - OSCHINA 和码云是一家，天天发这些，也不标注下 “利益相关”，兴许各位的 notion 最近经常不容易访问到，也是被国内的竞争对手天天举报吧？按某些公司的尿性，面试程序员的隐私可以挂，用户的笔记随便审核举报，投诉下它 notion 简直小儿科，也许哪天真的就完全用不了。
    - 因此，你的笔记如果打算保留十年以上，请选择支持本地存储+公开格式（最好文本）的软件，前者在于自己掌握数据，后者在于自己保留可以随时离开的权力。
  - What I learned about [[pkm]]?
    id:: 646ad604-3548-4c57-a41a-4c551df8a8cc
    - #+BEGIN_PINNED
      [^1] **Every page should have a [[Template]] page refer to parent class**.
      2 Everything could be page, which could linked somewhere else in graph.
      3 ((63bac790-01ec-4ada-a89b-89724b3041c4))
      #+END_PINNED
      - What's I mean? Even a `[[logseq]]` page I also should use `[[tool]]` template
  - Dynamic Variable `<%  %>`
    collapsed:: true
    - ```
      today => [[Today's journal page]]
      yesterday => [[Yesterday's journal page]]
      tomorrow => [[Tomorrow's journal page]]
      time => Current time, e.g. 22:44
      current page => [[Current page]]
      Natural language date
        - Today, Tomorrow, Yesterday, Last Friday, etc
        - 17 August 2013 - 19 August 2013
        - This Friday from 13:00 - 16.00
        - 5 days ago
        - 2 weeks from now
        - Sat Aug 17 2013 18:40:39 GMT+0900 (JST)
        - 2014-11-30T08:15:30-05:30
      Last Friday => [[Feb 12th, 2021]]
      ```
      via: [Dynamic Variables](https://docs.logseq.com/#/page/Dynamic%20Variables) by [Templates injecting dynamic dates (and placeholders/arguments) - Feature Requests - Logseq](https://discuss.logseq.com/t/templates-injecting-dynamic-dates-and-placeholders-arguments/833)
  - [Latest Look what I built topics - Logseq](https://discuss.logseq.com/c/look-what-i-built/11) #[[Kill Time]] #reading
  - [logseq/awesome-logseq: Awesome Logseq resources created by the community <3 (github.com)](https://github.com/logseq/awesome-logseq)
  - [Roadmap](https://trello.com/b/8txSM12G/roadmap)
  - [求推荐：知识管理-电子书阅读管理 APP？ - V2EX](https://www.v2ex.com/t/826204)
  - [知识信息组织索引工具推荐 - V2EX](https://www.v2ex.com/t/222874)
  - [有什么比较好的用于摘抄网页的工具吗 - V2EX](https://www.v2ex.com/t/797881)
  -