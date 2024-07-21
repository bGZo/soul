icon:: 📂
description:: 变态阅读器
tags:: #rss #[[github action]] #crawler #hentai
created:: 20230614

- ## Project Meta
  - CANCELED #project Hentai Reader
  - query-table:: false
    #+BEGIN_QUERY
    {:title [:h3 "Tasks related to Hentai Reader"]
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
     :query (and (todo todo) (page [[Hentai Reader]]))
    :result-transform (fn [result]
                        (sort-by (fn [b]
                                   (get b :block/priority "Z")) result))
    :breadcrumb-show? false
    :table-view? false
    }
    #+END_QUERY
- ## Why
  - No money. No time. Lazy.
- ## How
  - ~~Give the full-text output;~~ #Closed
    collapsed:: true
    - How to deal with the content only show for the user login?
      collapsed:: true
      - So the way RSS is bankruptcy, how does you request content using common method? How do you recognize the different websites? There are too much details. So why not design a module build for them directly?
  - ~~Git push to [Github - bGZo/bgzo at rss_reader](https://github.com/bGZo/bgzo/tree/rss_reader)~~ #Closed
    collapsed:: true
    - {{twitter https://twitter.com/imbGZo/status/1668952517408075776}}
  - WAITING How to deal with the copyright? #crawler
    collapsed:: true
    - #+BEGIN_WARNING
      Considered the copyright,
      I **should not build a mirror site for business content**!
      #+END_WARNING
  - TODO 具有防盗链的一些订阅源： \#.ol
    collapsed:: true
    - [灵梦御所](https://blog.reimu.net/feed)
      collapsed:: true
      - `Referer: https://blog.reimu.net`
      - #+BEGIN_EXAMPLE
        https://img.reimu.net/uploads/2023/06/6499957d1a902.png
        #+END_EXAMPLE
    - [天遊二次元](https://www.tiangal.com/feed)
      collapsed:: true
      - `Referer: https://www.tiangal.com/`
      - #+BEGIN_EXAMPLE
        https://ds.tianshi.info/uploads/2022/04/cropped-2022042217411468-32x32.png
        #+END_EXAMPLE
- ## What
  - ### \# Program Description
    - Functions
      - Fetch Rss and keep the newer data daily;
      - Save all data in repo;
      - Support APIs. (See #### **APIs**);
        collapsed:: true
        - Request Address: `http://rss.bgzo.cc`
        - | Name | Route | Description | Method | Note |
          |-------|------|------|------|------|
          | Feed  | `/feeds/${tag_name_with_hyphen_and_lower}` | RSS feed, return xml | `GET` | `${tag_name_with_slash_and_lower}` is the url string handle by `lower()` and hyphen(`-`). <br/>For example, we have a `DLsite Game Ranking.xml` file in server, then the correct full url address will be `http://rss.bgzo.cc/feeds/alsite-game-ranking.xml`; |
          | Contents | `/archives/${year}/${month}/${day}.json` | Contents, return JSON response | `GET` | **NOTE**: The timezone of response is GMT, format it whatever you want |
      - Support more sources, like DLSITE & 4GAMER.
        collapsed:: true
        - DONE Build the module supporting more websites;
        - Any good website welcome to post on issues )
      - TODO More usable.
        collapsed:: true
        - WAITING The configure of the whole sources is not usable, which is written in code. You should put it in a configuration file.
    - #### Input
      - Give Rss feed address;
    - #### Output
      - Give the short post about every source.
  - ### \# Alternatives
    - Feedbro
  - ### \# Notes
    - The project tech stack is [[python]], [[jekyll]], [[tailwind]] and few [[lang/programming/javascript]];
    - The libraries I used is
      - [[pyyaml]]
        collapsed:: true
        - [What is YAML?](https://www.redhat.com/en/topics/automation/what-is-yaml)
      - [[opml]]
        collapsed:: true
        - [opml · PyPI](https://pypi.org/project/opml/)
      - [[feedparser]]
        collapsed:: true
        - [Introduction — feedparser 6.0.10 documentation](https://feedparser.readthedocs.io/en/latest/introduction.html)
        - [python - AttributeError: module 'feedparser' has no attribute 'FeedParserDict' - Stack Overflow](https://stackoverflow.com/questions/46829474/attributeerror-module-feedparser-has-no-attribute-feedparserdict)
      - [[requests]]
      - [[feedgen]]
      - [[pytz]]
      - `pyyaml`, `opml`, `feedparser`, `requests`, `feedgen`, `pytz`
    - The work need to be more skilled.
      - Use the [[tailwind]], instead of writing CSS one by one.
        collapsed:: true
        - #+BEGIN_QUOTE
          backdrop-blur-md
          — [Blur Background Image in TailwindCSS - CSS Tailwind](https://csstailwind.com/blur-background-image-in-tailwindcss/)
          #+END_QUOTE
        - #+BEGIN_QUOTE
          @apply
          — [Reusing Styles - Tailwind CSS](https://tailwindcss.com/docs/reusing-styles)
          #+END_QUOTE
        - Pure HTML & CSS
          collapsed:: true
          - TODO [七种CSS方式让一个容器水平垂直居中_css相对容器居中_u013063153的博客-CSDN博客](https://blog.csdn.net/u013063153/article/details/52572489)
          - [How do I create an HTML button that acts like a link? - Stack Overflow](https://stackoverflow.com/questions/2906582/how-do-i-create-an-html-button-that-acts-like-a-link)
          - TODO [Tailwind CSS Tooltip - Free Examples & Tutorial (tailwind-elements.com)](https://tailwind-elements.com/docs/standard/components/tooltip/)
          - TODO [A Complete Guide to Flexbox | CSS-Tricks - CSS-Tricks](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
      - Python & JavaScript date module usage:
        collapsed:: true
        - [Python datetime (With Examples) (programiz.com)](https://www.programiz.com/python-programming/datetime)
        - [How to Create a Time Object in Python (learningaboutelectronics.com)](http://www.learningaboutelectronics.com/Articles/How-to-create-a-time-object-in-Python.php)
        - [Python Create Date Object (w3schools.com)](https://www.w3schools.com/python/gloss_python_date_create.asp)
        - [datetime — Basic date and time types — Python 3.11.4 documentation](https://docs.python.org/3/library/datetime.html#datetime.datetime.hour)
        - [python - How to subtract a day from a date? - Stack Overflow](https://stackoverflow.com/questions/441147/how-to-subtract-a-day-from-a-date)
        - #+BEGIN_QUOTE
          ```
          from datetime import datetime
          ts = int('1284101485')
          # if you encounter a "year is out of range" error the timestamp
          # may be in milliseconds, try `ts /= 1000` in that case
          print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
          ```
          — [python - Converting unix timestamp string to readable date - Stack Overflow](https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date)
          #+END_QUOTE
        - #+BEGIN_QUOTE
          http://strftime.org
          ```
          >>> from datetime import datetime
          >>> datetime.today().strftime('%Y-%m-%d')
          '2021-01-26'
          ```
          — [datetime - Getting today's date in YYYY-MM-DD in Python? - Stack Overflow](https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python)
          #+END_QUOTE
        - [Get Previous, Current and Next-Day System Dates in Python – Data to Fish](https://datatofish.com/get-previous-current-and-next-day-system-dates-in-python/)
        - [Python timestamp to datetime and vice-versa (With Examples) (programiz.com)](https://www.programiz.com/python-programming/datetime/timestamp-datetime)
        - ---
        - [Calculate the date yesterday in JavaScript - Stack Overflow](https://stackoverflow.com/questions/5511323/calculate-the-date-yesterday-in-javascript)
          collapsed:: true
          - ```js
            var date = new Date();
            date ; //# => Fri Apr 01 2011 11:14:50 GMT+0200 (CEST)
            date.setDate(date.getDate() - 1);
            date ; //# => Thu Mar 31 2011 11:14:50 GMT+0200 (CEST)
            ```
          - [Get Yesterday Date in JavaScript | HereWeCode](https://herewecode.io/blog/get-yesterday-date-javascript/#:~:text=The%20best%20way%20to%20get,setDate%20to%20update%20the%20date.)
            collapsed:: true
            - ```js
              // Create a date
              const todayDate = new Date()
              // Before subtracting 1 day
              console.log(todayDate.toString())
              // Output: "Tue Nov 15 2022 13:37:12 GMT+0100 (Central European Standard Time)"
              // Subtract one day to the current date
              todayDate.setDate(todayDate.getDate() - 1)
              // After removing 1 day
              console.log(todayDate.toString())
              // Output: "Mon Nov 14 2022 13:37:12 GMT+0100 (Central European Standard Time)"
              ```
        - TODO [html - How to mark::  width of :before pseudo element relative to containing element - Stack Overflow](https://stackoverflow.com/questions/39995303/how-to-mark:: -width-of-before-pseudo-element-relative-to-containing-element)
          collapsed:: true
          - `relative`?
        - TODO [HTML Entities (w3schools.com)](https://www.w3schools.com/html/html_entities.asp)
        - TODO [css - width and height doesn't seem to work on :before pseudo-element - Stack Overflow](https://stackoverflow.com/questions/20858587/width-and-height-doesnt-seem-to-work-on-before-pseudo-element)
        - [Compare two dates with JavaScript - Stack Overflow](https://stackoverflow.com/questions/492994/compare-two-dates-with-javascript)
          collapsed:: true
          - ```js
            var d1 = new Date();
            var d2 = new Date(d1);
            console.log(d1 == d2);   // prints false (wrong!)
            console.log(d1 === d2);  // prints false (wrong!)
            console.log(d1 != d2);   // prints true  (wrong!)
            console.log(d1 !== d2);  // prints true  (wrong!)
            console.log(d1.getTime() === d2.getTime()); // prints true (correct)
            ```
        - [javascript - Checking if two Dates have the same date info - Stack Overflow](https://stackoverflow.com/questions/4428327/checking-if-two-dates-have-the-same-date-info)
          collapsed:: true
          - ```js
            Date.prototype.isSameDateAs = function(pDate) {
              return (
                this.getFullYear() === pDate.getFullYear() &&
                this.getMonth() === pDate.getMonth() &&
                this.getDate() === pDate.getDate()
              );
            }
            ```
          - [How to check if two dates are the same day in JavaScript (flaviocopes.com)](https://flaviocopes.com/how-to-check-dates-same-day-javascript/)
            collapsed:: true
            - ```js
              const datesAreOnSameDay = (first, second) =>
                  first.getFullYear() === second.getFullYear() &&
                  first.getMonth() === second.getMonth() &&
                  first.getDate() === second.getDate();
              ```
        - [Format a JavaScript Date to YYYY MM DD - Mastering JS](https://masteringjs.io/tutorials/fundamentals/date-tostring-format-yyyy-mm-dd)
          collapsed:: true
          - ```js
            const date = new Date();
            date.toLocaleDateString('en-GB').split('/').reverse().join(''); // '20211124'
            ```
          - [Date.prototype.toLocaleDateString() - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleDateString)
        - #+BEGIN_QUOTE
          ```
           const date = new Date();
           console.log(date);
          ```
          — [How to Get the Current Date in JavaScript - Scaler Topics](https://www.scaler.com/topics/get-current-date-in-javascript/)
          #+END_QUOTE
        - #+BEGIN_QUOTE
          ```
          let yourDate = new Date()
          - yourDate.toISOString().split('T')[0]
          ```
          — [Format JavaScript date as yyyy-mm-dd - Stack Overflow](https://stackoverflow.com/questions/23593052/format-javascript-date-as-yyyy-mm-dd)
          #+END_QUOTE
      - Python dict
        collapsed:: true
        - [Adding to Dict in Python – How to Append to a Dictionary (freecodecamp.org)](https://www.freecodecamp.org/news/add-to-dict-in-python/)
        - [python字典遍历的几种方法 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/33033288)
        - [Python 按键(key)或值(value)对字典进行排序 | 菜鸟教程 (runoob.com)](https://www.runoob.com/python3/python-sort-dictionaries-by-key-or-value.html)
    - The tools need to be more skilled:
      - [[vscode]] with [[wsl]]
        collapsed:: true
        - Can't open the tabnine setting panel
          collapsed:: true
          - collapsed:: true
            #+BEGIN_QUOTE
            FWIW I was able to install 3.2.8 without issue.
            — [Tabnine Extension was unable to download its dependencies. · Issue #447 · codota/tabnine-vscode --- Tabnine Extension 无法下载其依赖项。 · 问题 #447 · codota/tabnine-vscode](https://github.com/codota/tabnine-vscode/issues/447)
            #+END_QUOTE
            - 降级到 3.2.8 #wsl
            - [can't open the setting panel · Issue #741 · codota/tabnine-vscode --- 无法打开设置面板 · Issue #741 · codota/tabnine-vscode (github.com)](https://github.com/codota/tabnine-vscode/issues/741)
            - [command 'TabNine.statusBar' not found · Issue #426 · codota/tabnine-vscode (github.com)](https://github.com/codota/tabnine-vscode/issues/426)
            - [hub not loading · Issue #643 · codota/tabnine-vscode (github.com)](https://github.com/codota/tabnine-vscode/issues/643)
            - [WSL2 Issue with TabNine::config · Issue #386 · codota/TabNine (github.com)](https://github.com/codota/TabNine/issues/386)
            - [visual studio code - Tabnine Extension was unable to download its dependencies - Stack Overflow](https://stackoverflow.com/questions/70565623/tabnine-extension-was-unable-to-download-its-dependencies)
        - Set ubuntu proxy without gui
          collapsed:: true
          - ```shell
            host_ip=$(cat /etc/resolv.conf | grep "nameserver" |cut -f 2 -d " ")
            gsettings set org.gnome.system.proxy.http host $host_ip
            gsettings set org.gnome.system.proxy.http port 7890
            gsettings set org.gnome.system.proxy.https host $host_ip
            gsettings set org.gnome.system.proxy.https port 7890
            gsettings set org.gnome.system.proxy.socks host $host_ip
            gsettings set org.gnome.system.proxy.socks port 7890
            ```
            via: [How to change system proxy settings from the command line on Ubuntu desktop (xmodulo.com)](https://www.xmodulo.com/change-system-proxy-settings-command-line-ubuntu-desktop.html)
          - ```shell
            gsettings set org.gnome.system.proxy mode 'none'
            ```
      - ```
        wsl hostname -i
        ```
        [networking - How to find WSL2 machine's IP address from windows - Super User](https://superuser.com/questions/1586386/how-to-find-wsl2-machines-ip-address-from-windows)
      - [[jekyll]]
        collapsed:: true
        - #+BEGIN_QUOTE
          ```
          exclude:
            - mydoc_writers_*
            - bower_components
            - Gemfile
          ```
          — [Excluding files | Jekyll theme for documentation](https://idratherbewriting.com/documentation-theme-jekyll/mydoc_exluding_files.html#exclude-strategies)
          #+END_QUOTE
        - #+BEGIN_QUOTE
          根据您要显示的内容类型，这会有所不同。但在最基本的层面上，这将输出最新帖子的标题和正文内容……没有循环……这对您的构建时间有好处。
          ```
          <h1>{{ site.posts.last.title }}</h1>
          {{ site.posts.last.content }}
          ```
          — [How to show the latest post as the homepage? - Help - Jekyll Talk --- 如何将最新的帖子显示为首页？ - 帮助 - Jekyll Talk](https://talk.jekyllrb.com/t/how-to-show-the-latest-post-as-the-homepage/2199/3)
          #+END_QUOTE
      - Python
        - [python - How to raise an AttributeError? - Stack Overflow](https://stackoverflow.com/questions/73853413/how-to-raise-an-attributeerror)
        - TODO [为什么产生 __pycache__ - Google Search](https://www.google.com/search?q=%E4%B8%BA%E4%BB%80%E4%B9%88%E4%BA%A7%E7%94%9F+__pycache__)
        - TODO [python函数如何传递多个参数_python传入多个参数_LLY_A_的博客-CSDN博客](https://blog.csdn.net/LLY_A_/article/details/119968335)
          collapsed:: true
          - [Python传入参数的几种方法-腾讯云开发者社区-腾讯云 (tencent.com)](https://cloud.tencent.com/developer/article/1567332)
        - [import - Python FileNotFoundError : - Stack Overflow](https://stackoverflow.com/questions/74953823/python-filenotfounderror)
        - [python - How do I create a directory, and any missing parent directories? - Stack Overflow](https://stackoverflow.com/questions/273192/how-do-i-create-a-directory-and-any-missing-parent-directories)
        - [File Handling in Python – How to Create, Read, and Write to a File (freecodecamp.org)](https://www.freecodecamp.org/news/file-handling-in-python/#:~:text=In%20Python%2C%20you%20use%20the,it%20will%20return%20an%20error.)
        - [python - Write a file to a directory that doesn't exist - Stack Overflow](https://stackoverflow.com/questions/23793987/write-a-file-to-a-directory-that-doesnt-exist)
        - [python - Converting dictionary to JSON - Stack Overflow](https://stackoverflow.com/questions/26745519/converting-dictionary-to-json)
        - [python - How to make a datetime object aware (not naive) - Stack Overflow](https://stackoverflow.com/questions/7065164/how-to-make-a-datetime-object-aware-not-naive)
        - [python - Is there a list of Pytz Timezones? - Stack Overflow](https://stackoverflow.com/questions/13866926/is-there-a-list-of-pytz-timezones)
      - JavaScript
        collapsed:: true
        - #+BEGIN_QUOTE
          ```
          window.location.href
          ```
          — [Get the current URL with JavaScript? - Stack Overflow](https://stackoverflow.com/questions/1034621/get-the-current-url-with-javascript)
          #+END_QUOTE
        - [javascript - Expanding all details tags - Stack Overflow](https://stackoverflow.com/questions/43008609/expanding-all-details-tags)
        - [javascript - Open closest Details element onclick - Stack Overflow](https://stackoverflow.com/questions/66076836/open-closest-details-element-onclick)
      - [lkiesow/python-feedgen: Python module to generate ATOM feeds, RSS feeds and Podcasts. (github.com)](https://github.com/lkiesow/python-feedgen)
        - ["ValueError: Required fields not set" when generating Atom feed · Issue #39 · lkiesow/python-feedgen --- 生成 Atom feed 时出现“ValueError：未设置必填字段” · 问题 #39 · lkiesow/python-feedgen (github.com)](https://github.com/lkiesow/python-feedgen/issues/39)
      - [git - How do I create a new GitHub repo from a branch in an existing repo? - Stack Overflow](https://stackoverflow.com/questions/9527999/how-do-i-create-a-new-github-repo-from-a-branch-in-an-existing-repo)