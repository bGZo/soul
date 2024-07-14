icon:: 📅
alias:: 年份

- ## Why
- ## How
- ## What
  - ### Template
    - CANCELED In new [[year]] page, I will sperate vertical page to two parts at least.  #Closed #deprecated
      created:: [[20221217]]
      closed:: [[20230218]]
      collapsed:: true
      - the more details are like this: #changelog/wiki #template
        collapsed:: true
        - ![](../assets/works/2023-new-page-design.png){:height 394, :width 275}
          via: `[[draws/2023-new-page-design.excalidraw]]`
      - template: page/year
        collapsed:: true
        template-including-parent: false
        - icon:: 📅
          title:: 
          alias:: year/
          desc:: 
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
        alias:: year/``{ c.page.name }``
        created:: ``{ ref(date.now.format('YYYYMMDD')) }``
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
      - 一些 #碎碎念
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