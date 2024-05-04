icon:: 🌸
alias:: ギャルゲーム, ギャルゲー, ギャルゲ, 美少女游戏, 萌游戏, Visual Novel
moegirl:: [Galgame - 萌娘百科 萬物皆可萌的百科全書 (moegirl.org.cn)](https://zh.moegirl.org.cn/zh-hk/Galgame)
wikipedia:: [Bishōjo game - Wikipedia](https://en.wikipedia.org/wiki/Bish%C5%8Djo_game)
tags:: #Hobby #game
mark:: 主要以具有魅力的女性为卖点类型的游戏的俗称 / 乙女游戏 Otome Game, 冒险游戏 / [[hentai]]

  - cover:: ![🖼 ](../assets/``{ date.now.format('YYYY') }``/)
    title:: 
    alias:: 
    desc:: 
    tags:: #galgame
    released-created:: 
    developer:: 
    publisher:: 
    bangumi:: 
    douban:: 
    created:: ``{ date.now.format('YYYYMMDD') }``
    closed:: 
    template:: galgame
    template-including-parent:: true
- ## WHY
  - I know this kind of game from [*Oreimo*](https://bgm.tv/subject/5436), and I'm really drawn to it. I used to treat it like an alternative to [[Anime]], basically it's same except a little complex.
  - Then I know there is rating system for arts, expecially R18 game, which I almost have no education to [[sex]]. So I was addiacted in it deeper, and then find it's nothing if the story is bad.
  - A lot of things happened in [[China]] Internet, such as the policy is changed (to be more restrict, filling with recopy, report ( ((6463a921-47df-47b6-b7e6-971bee380898)) ) and sell again), Zh-Hans-Translation group disbanded appear more and more (See ((64625a01-b388-4404-91a9-baf438852bfe))).
  - Simply speaking, the whole market is exposed outside and turned to legal. Things is not turn good way to develop, because the rule of [[censor]] is not public. So I never touched a domestic galgame till now, because I don't think how deep in some topic they could reach, and that matters.
  - Yet the most friendly platform is [[Steam]], but they have the censor as well, including child porn or something else, which is different with [[Japan]]. I doubt, does it make sense? I don't know. I just dream a platform, which could give me all I want. But seemly it's just a dream. (See ((6463bf85-9f47-43a8-b65f-047dc1e2ebdf)))
  - In broad strokes, I devided it into two categories now, althougt they have more details. (See ((64625a01-1706-4e5d-ba30-e303492e8e84))) #.ol
    - [[galgame/jerk-off]] (See [[hentai]] details)
    - [[galgame/god]]
- ## HOW
  - DONE How to [[unpack]] a galgame, for getting their resource?
    collapsed:: true
    - ((63db96e5-053c-4978-8860-a305fa58f26c))
      id:: 63da20d9-3875-4191-a09a-735a0ca76cc5
    - DONE Mp4 No Loss Encode | MP4无损压缩 #Issue #ffmpeg
      collapsed:: true
      - ```bash
        ffmpeg -i $in -c:v libx264 -c:a libfaac -crf 20 -preset:v veryslow $out
        # then I chose 21;
        ```
      - `-crf` option
        - scale: 0 – 51 (0 is lossless, 23 is the default, and 51 is worst quality possible)
          - Consider 17 or 18 to be visually lossless or nearly so; it should look the same or nearly the same as the input but it isn't technically lossless
          - The range is exponential, so increasing the CRF value +6 results in roughly half the bitrate / file size, while -6 leads to roughly twice the bitrate.
        - 自己试了下0, 无损压缩, 文件大小从30M -> 300M
      - via: [shell - FFMPEG convert .mpg video to .mp4 without lose quality - Stack Overflow](https://stackoverflow.com/questions/33672960/ffmpeg-convert-mpg-video-to-mp4-without-lose-quality)
        - WAITING [Encode/H.264 – FFmpeg](https://trac.ffmpeg.org/wiki/Encode/H.264)
    - DONE Diff 2 compressed video info (size under different bitrate/High@L ...)? #Issue
      collapsed:: true
      - 比较两个命令的输出有何区别 (最好着色)? #diff
        - ```shell
           diff -u --color <(mediainfo --fullscan wbgm08.mp4) <(mediainfo --fullscan default.mp4)
          ```
          - `-u`
            - Git 比对
        - expanded
          - ```shell
            sudo apt install colordiff
            
            diff -u <(mediainfo --fullscan old.mp4) <(mediainfo --fullscan new.mp4) | colordiff
            colordiff <(mediainfo --fullscan old.mp4) <(mediainfo --fullscan new.mp4)
            ```
            - 着色 
              :LOGBOOK:
              CLOCK: [2022-08-20 Sat 16:41:06]--[2022-08-20 Sat 16:41:07] =>  00:00:01
              :END:
              - [colordiff](https://www.colordiff.org/) on [Github](https://github.com/daveewart/colordiff)
                - It's a **wrapper** around `diff` that produces the same output as diff, except that it augments the output using colored syntax highlighting to increase readability
                  - ```bash
                    # alias in .zshrc, remember install colordiff
                    alias diff=colordiff
                    ```
      - 比较两个目录的文件区别, 不 Care 内容
        - ```shell
          diff -rq dir1 dir2
          ```
      - 比较两个目录的文件区别, Care 内容
        - ```shell
          diff -r dir1 dir2
          ```
    - title:: [【技术】新人也能懂的galgame游戏解包方法 - 哔哩哔哩](https://www.bilibili.com/read/cv6488276)
      author:: Reca_ザキ
      tags:: #archive/web
      created:: 20221121
      archive:: [💾 Archived](assets/archived_web/【技术】新人也能懂的galgame游戏解包方法 - 哔哩哔哩 (11_21_2022 10_05_08 PM).html)
  - DONE How to play in different devices?
    collapsed:: true
    - [zeas2/Kirikiroid2](https://github.com/zeas2/Kirikiroid2)
    - [JoiPlay](https://joiplay.cyou/)
    - [Tyranor模拟器正式发布|个人日记 - 绯月ScarletMoon](https://bbs.kfmax.com/read.php?tid=912800&sf=233)
    - [Studio O.G.A.](https://onscripter.osdn.jp/)
      collapsed:: true
      - [onsshare/onscripter: onscripter clootection](https://github.com/onsshare/onscripter)
    - [xupefei/Locale-Emulator: Yet Another System Region and Language Simulator](https://github.com/xupefei/Locale-Emulator)
  - WAITING How to play without zh-has translation?
    collapsed:: true
    - title:: hanmin0822/MisakaTranslator
      author:: hanmin0822
      mark:: "御坂翻译器—Galgame/文字游戏/漫画多语种实时机翻工具"
      tags:: #Github
      source::  [hanmin0822/MisakaTranslator: 御坂翻译器—Galgame/文字游戏/漫画多语种实时机翻工具](https://github.com/hanmin0822/MisakaTranslator) ![](https://img.shields.io/github/stars/hanmin0822/MisakaTranslator)
      created:: 202012
      mark:: Doc with [GAL党的福音——开源生肉翻译器MisakaTranslator正式版发布 - 知乎](https://zhuanlan.zhihu.com/p/112895928)
    - title:: miaomiaosoft/PandaOCR
      author:: miaomiaosoft
      mark:: "多功能OCR图文识别+翻译+朗读+弹窗+公式+表格+图床+搜图+二维码"
      tags:: #Github
      source:: [miaomiaosoft/PandaOCR: PandaOCR - 多功能OCR图文识别+翻译+朗读+弹窗+公式+表格+图床+搜图+二维码](https://github.com/miaomiaosoft/PandaOCR) ![](https://img.shields.io/github/stars/miaomiaosoft/PandaOCR)
      created:: 202012
    - Windows 11 live caption
- ## WHAT
  - Categories with more details.
    id:: 64625a01-1706-4e5d-ba30-e303492e8e84
    collapsed:: true
    - 游戏内容
      collapsed:: true
      - 抜きゲー / 拔作
      - 糞ゲー / 粪作
      - 泣きゲー
        collapsed:: true
        - Key社
      - 鬱ゲー
      - 神ゲー / 神作
        collapsed:: true
        - 白色相簿2
        - Muv-Luv Alternative
        - 装甲恶鬼村正
        - 素晴日
      - キャラゲー / 角色作
        collapsed:: true
        - 苍之彼方的四重奏
        - 9-nine-
      - 萌えゲー / 萌作 / “废萌”
        collapsed:: true
        - 柚子社
    - 游戏展现
      collapsed:: true
      - TAVG / 文字冒险类游戏
        collapsed:: true
        - 妹调教日记
        - 秋之回忆系列
        - 女装山脉
      - VNG / 视觉小说类游戏
        collapsed:: true
        - Narcissu
        - 魔法使之夜
        - 月姬
        - Fate/stay night
        - Fate/hollow ataraxia
      - AAG / 动作冒险类游戏
      - ES / 养成类游戏
        collapsed:: true
        - LC系列
        - 心跳回忆系列
      - SLG / 策略类游戏
        collapsed:: true
        - 幻燐的姬将军
        - 战女神系列
      - RPG / 角色扮演
        collapsed:: true
        - 夏娃年代记系列
        - 兰斯系列
        - 多娜多娜
        - 封缄之都古拉塞斯塔
        - 天结Castle Meister
    - TODO [terminology - What are the differences between visual novel, eroge, gal game, and a dating sim? - Anime & Manga Stack Exchange](https://anime.stackexchange.com/questions/4926/what-are-the-differences-between-visual-novel-eroge-gal-game-and-a-dating-sim)
  - Zh-Hans Translation Group details.
    id:: 64625a01-b388-4404-91a9-baf438852bfe
    collapsed:: true
    - {{iframe https://zh.wikipedia.org/wiki/%E6%B1%89%E5%8C%96%E7%BB%84}}
    - collapsed:: true
      #+BEGIN_IMPORTANT
      R.I.P. 
      #+END_IMPORTANT
      - 脸肿汉化组
      - [巴比伦汉化组](https://bblacg.com/)
      - 哥布林汉化组
    - 字幕组
      - 极影字幕组
      - 澄空字幕组
      - 动漫国字字幕组
    - 汉化组
      - 默示汉化组
      - ACG汉化组
      - 萌你妹汉化组
      - [弥生月/善雅鸽 汉化组](https://esugugugu.com/)
      - [独占汉化组](https://dzhhz.wordpress.com/author/duzhanhanhua/)
      - [杏爱会](https://pooi.moe/)
    - Report #sucks
      - ⌈终焉无脑韛-单推水巴⌋ 举报汉化到柚子社 #2020
        id:: 6463a921-47df-47b6-b7e6-971bee380898
        - ((6463c4a4-6fc6-45a2-b266-56038e219ec0))
        - [如何评价录制汉化galgame视频上传哔哩哔哩的行为？ - 知乎](https://www.zhihu.com/question/62779037/answer/288546281)
        - [3月24日弥生月汉化组举报事件始末 我们究竟还要迫害为我们默默奉献的人多久](https://www.bilibili.com/read/cv5275470/)
        - [如何评价b站up主终焉无脑韛-单推水巴到柚子社官推举报某汉化组, 导致汉化组终止原有计划并提前解散?](https://www.zhihu.com/question/382070522/answer/1101695673)
      - ((6463ace1-77ef-4506-ba7f-0c3d9cf0e89a))
  - [[bookmark]]
    collapsed:: true
    - [月幕Galgame-最戳你XP的美少女游戏综合交流平台 | 来感受这绝妙的艺术体裁](https://www.ymgal.games/index)
    - [GAL必备 - ACG喵导航](https://www.miaoaaa.com/favorites/gal%e5%bf%85%e5%a4%87)
- collapsed:: true
  ----
  - DONE Should I build each page for every single galgame? Just like [[Book]], Is that necessary? ~~Pointful~~ Meaningful? @20221121
    collapsed:: true
    - **Unlike book**, they wont have a single page
      - But if, one day, the discuss about origin game increased a huge amount. I will turn it to page. But now, I just record the name I played, I don't have too interest and energy in it. #changelog/wiki
        - ==In a way, this is a decide about hierarchy for content, or just for category?==
        - And this decision is not limited to galgame, more adopt to items of [[2022]], like [[Hobby]] / [[archive]]. If they're huge, turn it to page, not build a single page immediately.