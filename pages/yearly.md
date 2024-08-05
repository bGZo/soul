also:: 年度, 年度总结, 复盘
icon:: 📅

created:: [[20230602]]

- ## Why
  - Work flow.
- ## How
  - 基本每一个平台都会有年度总结, 如果我要聚合所有的平台的链接, 那会永无止境, 我只能在入门的时候多看看这个平台的年度数据. Especially [[hobby]]
    - You know what, actually I don't give a fuck to this garbage ranking.
      - Only when **you are newer to fields or you are busy all years**, you would need this.
  - ### **Rules**: Not New Year Resolution, but Past Year Review(PYR)
    - [[狗熊有话说]] [ep. 400](https://voice.beartalking.com/400) 讲 [@Tim Ferriss](https://tim.blog/2021/12/27/past-year-review/) 的方法: **不要着急做做新一年的计划, 而是去回看过去一年的经历**. 以及以下的方法论:
    - > 1. Grab a notepad and create two columns: POSITIVE and NEGATIVE.
      2. Go through your calendar from the last year, looking at every week.
      3. For each week, jot down on the pad any people or activities or commitments that triggered peak positive or negative emotions for that month. Put them in their respective columns.
      4. Once you’ve gone through the past year, look at your notepad list and ask, “What 20% of each column produced the most reliable or powerful peaks?”
      5. Based on the answers, take your “positive” leaders and schedule more of them in the new year. Get them on the calendar now! Book things with friends and prepay for activities/events/commitments that you know work. It’s not real until it’s in the calendar. That’s step one. Step two is to take your “negative” leaders, put “NOT-TO-DO LIST” at the top, and put them somewhere you can see them each morning for the first few weeks of 2022. These are the people and things you *know* make you miserable, so don’t put them on your calendar out of obligation, guilt, FOMO, or other nonsense.
    - 我根据这个规则做了一些模板，供参考：
      template:: year/review/with/feedback
      template-including-parent:: false
      - | 正反馈的事情 | 负反馈的事情 |
        | ---------| ---------|
        |  |  |
      - 最值得你花时间去做的事情：
        - logseq.order-list-type:: number
      - 千万不要花时间 / 尽量不要花时间去做的事情：
        - logseq.order-list-type:: number
-
- ## What
  - coding
    - [Top Pens of 2022 on CodePen](https://codepen.io/2022/popular/pens/)
    - WAITING Github Trend
  - reading
    - 年度书单 #book
      - [纽约时报](https://nytimes.com/2022/11/29/books/best-books-2022.html)
      - [经济学人](https://economist.com/culture/2022/12/06/these-are-the-economists-best-books-of-2022)
      - [华尔街日报](https://wsj.com/articles/the-best-reading-of-2022-11670613727)
      - [卫报](https://theguardian.com/books/2022/dec/03/the-best-books-of-2022)
      - [金融时报](https://ft.com/content/2dd61d03-13ac-4278-8214-678c1d9a33c1)
      - [纽约客](https://newyorker.com/best-books-2022)
      - Via: https://www.chongbuluo.com/thread-14426-1-1.html
  - #### 今年发生了啥
    - WAITING Hacker News
  - We Media
    - ?
  - databases
    - [Bangumi 年鉴 | BEST OF 2022](https://bgm.tv/award/2022)
  - podcast
    - [2022小宇宙播客大赏](https://annual.podcast.xyz/2022)
    - [Most popular podcasts of 2022 - Apple Podcasts for Creators](https://podcasters.apple.com/4704-news-2022-eoy-charts)
      - Sucks, needs the client
  - music
    - spotify
  - Fun
    - [The 2022 Pornhub Year in Review | Pornhub Insights](https://www.pornhub.com/insights/2022-year-in-review)
  - ### Template
    - CANCELED In new [[year]] page, I will sperate vertical page to two parts at least.  \#Closed \#deprecated
      created:: [[20221217]]
      closed:: [[20230218]]
      collapsed:: true
      - the more details are like this: \#changelog/wiki \#template
        collapsed:: true
        - ![](../../soul/assets/works/2023-new-page-design.png){:height 394, :width 275}
          via: `[[draws/2023-new-page-design.excalidraw]]`
      - template: page/year
        collapsed:: true
        template-including-parent: false
        - icon:: 📅
          title:: 
          also:: year/
          tags:: #year
          description::
        - `{{query }}`
        - ## 💬 Topic
          collapsed:: true
          {{renderer :smartblock, thought, +Thought, false}}
          -
        - ## [[time line]]
          collapsed:: true
          {{renderer :smartblock, book, +Book, false}} {{renderer :smartblock, podcast/episode, +Episode, false}} {{renderer :smartblock, game, +Game, false}} {{renderer :smartblock, galgame, +Hentai, false}} {{renderer :smartblock, video, +Video, false}} {{renderer :smartblock, video/movie, +Movie, false}} {{renderer :smartblock, anime, +Anime, false}} {{renderer :smartblock, manga, +Manga, false}}
          -
        - ## [[archive]]
          collapsed:: true
          {{renderer :smartblock, archive(default: web), +Web, false}}
          -
        - ## 📃 Reference
          collapsed:: true
          -
    - #### Year [[award]]
      template:: year/review
      template-including-parent:: false
      - icon:: 🏆
        also:: year/``{ c.page.name }``
        created:: ``{ date.now.format('YYYYMMDD') }``
      - ## Anime Awards
        - ### Bangumi 班固米
          - {{iframe https://bgm.tv/award/``{ c.page.name }``, 40vh, iframe-radius}}
        - ### Animecorner
          - {{iframe https://animecorner.me/``{ c.page.name }``-anime-of-the-year-awards-winners/, 40vh, iframe-radius}}
      - ## Game Awards
        - ### Steam
          - {{iframe https://store.steampowered.com/steamawards/``{ c.page.name }``?l=schinese, 40vh, iframe-radius}}
        - ### TGA
          - {{iframe https://thegameawards.com/rewind/year-``{ c.page.name }``, 40vh, iframe-radius}}
        - ### Metacritic
          - {{iframe https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?view=detailed&sort=desc&year_selected=``{ c.page.name }``, 40vh, iframe-radius}}
      - ## Novel Awards
        - ### Douban
          - {{iframe https://book.douban.com/annual/``{c.page.name}``, 40vh, iframe-radius}}
      - ## Movie Awards
        - ### Douban
          - {{iframe https://movie.douban.com/annual/``{c.page.name}``, 40vh, iframe-radius}}
        - ### Academy
          - {{iframe https://www.imdb.com/event/ev0000003/``{c.page.name}``/1/, 40vh, iframe-radius}}
      - ## Music Awards
        - ### Douban
          - {{iframe https://music.douban.com/annual/``{c.page.name}``, 40vh, iframe-radius}}
      - ## Coding Awards
        - ### Product Hunt
          - {{iframe https://www.producthunt.com/golden-kitty-awards/hall-of-fame?year=``{ c.page.name }``, 40vh, iframe-radius}}
      - ## Mobile
        - ### Apple Store
          - {{iframe https://developer.apple.com/design/awards/``{ c.page.name }``, 40vh, iframe-radius}}
        - ### Google Play
          - {{iframe https://play.google.com/store/apps/editorial?id=mc_bestof``{ c.page.name }``_xfn_fcp&hl=en, 40vh, iframe-radius}}
      - ## Hentai Awards #nsfw
        - ### Moe Game
          - {{iframe https://moe-gameaward.com/prize/``{ c.page.name }``, 40vh, iframe-radius}}
        - ###  DLsite Game Sale Ranking
          - {{iframe https://www.dlsite.com/maniax/ranking/year?year=``{c.page.name}``&sort=sale&category=game, 40vh, iframe-radius}}
        - ### DLsite Voice Sale Ranking
          - {{iframe https://www.dlsite.com/maniax/ranking/year?year=``{c.page.name}``&sort=sale&category=voice, 40vh, iframe-radius}}
        - ### DLsite Comic Sale Ranking
          - {{iframe https://www.dlsite.com/maniax/ranking/year?year=``{c.page.name}``&sort=sale&category=comic, 40vh, iframe-radius}}
    - TODO 收集各大网站的年榜数据
      - 站长/网站已提供（有限）年榜数据将更新入模板；
      - 自己帮忙统计：
        - https://gmgard.com
        - https://www.v2ex.com
      - 一些碎碎念
        - myanimelist 年榜发布的形式居然是论坛发帖，学到了
          - https://myanimelist.net/forum/?topicid=2150162
        - 豆瓣前几年好像还有个东西榜单
          - https://www.douban.com/doulist/45606824/
        - 很少有网站能同时保留很多年的数据；
      - ## TODO Comic Review
        - https://nihonmangakakyokai.or.jp/about/about07
          - 只更新这一个页面，也是简陋的很
      - ### #nsfw Getchu Sale Ranking
        - {{iframe https://www.getchu.com/pc/salesranking``{c.page.name}``.html, 40vh, iframe-radius}}
-