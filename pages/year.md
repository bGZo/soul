icon:: 📅
title:: year

  - Year Review Template
    template:: year/review
    template-including-parent:: false
    - icon:: 📅
    - ## Anime Review
      - ### Bangumi
        - {{iframe https://bgm.tv/award/``{ c.page.name }``, 400}}
      - ### Animecorner
        - {{iframe https://animecorner.me/``{ c.page.name }``-anime-of-the-year-awards-winners/, 400}}
      -
    - ## Comic Review
      - .
    - ## Game Review
      - ### Steam Game
        - {{iframe https://store.steampowered.com/steamawards/``{ c.page.name }``?l=schinese, 400}}
      - ### The Game Awards Rewind
        - {{iframe https://thegameawards.com/rewind/year-``{ c.page.name }``, 400}}
      - ### Metacritic
        - {{iframe https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?view=detailed&sort=desc&year_selected=``{ c.page.name }``, 400}}
      - ### #nsfw Moe Game
        - {{iframe https://moe-gameaward.com/prize/``{ c.page.name }``, 400}}
      - ### #nsfw Getchu Sale Ranking
        - {{iframe https://www.getchu.com/pc/salesranking``{c.page.name}``.html, 400}}
      - ### #nsfw DLsite Game Sale Ranking
        - {{iframe https://www.dlsite.com/maniax/ranking/year?year=``{c.page.name}``&sort=sale&category=game, 400}}
    - ## Novel Review
      - ### Douban
        - {{iframe https://book.douban.com/annual/``{c.page.name}``, 400}}
    - ## Movie Review
      - ### Douban
        - {{iframe https://movie.douban.com/annual/``{c.page.name}``, 400}}
    - ## Music Review
      - ### Douban
        - {{iframe https://music.douban.com/annual/``{c.page.name}``, 400}}
    - ## Hentai
      - ### DLsite Voice Sale Ranking
        - {{iframe https://www.dlsite.com/maniax/ranking/year?year=``{c.page.name}``&sort=sale&category=voice, 400}}
      - ### DLsite Comic Sale Ranking
        - {{iframe https://www.dlsite.com/maniax/ranking/year?year=``{c.page.name}``&sort=sale&category=comic, 400}}
  - DONE In new [[year]] page, I will sperate vertical page to two parts at least. #Closed #deprecated
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
-
- TODO 真希望拿到所有网站的年榜数据，所以收集吧 ）
  - 站长/网站已提供（有限）年榜数据
    -
  - 需要自己帮忙做，帮忙统计的年榜数据；
    - [GMgard ](https://gmgard.com/)
  - 一些 #碎碎念
    - myanimelist 年榜发布的形式居然是论坛发帖，学到了
      - https://myanimelist.net/forum/?topicid=2150162
    - 豆瓣前几年好像还有个东西榜单
      - https://www.douban.com/doulist/45606824/
-
-