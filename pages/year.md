icon:: 📅
title:: year

  - Year Review Template
    collapsed:: true
    - template:: year/review
      template-including-parent:: false
      - ## Anime
        - ### Bangumi
          - {{iframe https://bgm.tv/award/``{ c.page.name }``}}
      - ## Game Review
        - ### Steam Game
          - {{iframe https://store.steampowered.com/steamawards/``{ c.page.name }``?l=schinese}}
        - ### The Game Awards Rewind
          - {{iframe https://thegameawards.com/rewind/year-``{ c.page.name }``}}
        - ### Metacritic
          - {{iframe https://www.metacritic.com/browse/games/score/metascore/year/all/filtered?view=detailed&sort=desc&year_selected=``{ c.page.name }``}}
      - ## Hentai
        - ### Moe Game
          - {{iframe https://moe-gameaward.com/prize/``{ c.page.name }``}}
        - ### Getchu Sale Ranking
          - {{iframe https://www.getchu.com/pc/salesranking``{c.page.name}``.html}}
        - ### DLsite Game Sale Ranking
          - {{iframe https://www.dlsite.com/maniax/ranking/year?year=``{c.page.name}``&sort=sale&category=game}}
        - ### DLsite Voice Sale Ranking
          - {{iframe https://www.dlsite.com/maniax/ranking/year?year=``{c.page.name}``&sort=sale&category=voice}}
        - ### DLsite Comic Sale Ranking
          - {{iframe https://www.dlsite.com/maniax/ranking/year?year=``{c.page.name}``&sort=sale&category=comic}}
  -
  - DONE In new [[year]] page, I will sperate vertical page to two parts at least. #Closed #deprecated
    created:: [[20221217]]
    closed:: [[20230218]]
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
        mark:: 
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
- TODO 年榜缺少：
  - [GMgard - 紳士の庭 ♢绅士们的二次元资源分享交流平台♢](https://gmgard.com/)
-