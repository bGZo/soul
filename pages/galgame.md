icon:: 🎮
also:: ギャルゲーム, ギャルゲー, ギャルゲ, 美少女游戏, 萌游戏, Visual Novel, game/galgame
description:: 主要以具有魅力的女性为卖点类型的游戏的俗称 / 乙女游戏 Otome Game, 冒险游戏 / hentai
wikipedia:: https://en.wikipedia.org/wiki/Bish%C5%8Djo_game

- ## WHY
  - I know this kind of game from [*Oreimo*](https://bgm.tv/subject/5436), and I'm really drawn to it. I used to treat it like an alternative to anime, basically it's same except a little complex.
  - Then I know there is rating system for arts, expecially R18 game, which I almost have no education to sex. So I was addiacted in it deeper, and then find it's nothing if the story is bad.
  - A lot of things happened in china Internet, such as the policy is changed (to be more restrict, filling with recopy, report ( ((6463a921-47df-47b6-b7e6-971bee380898)) ) and sell again), Zh-Hans-Translation group disbanded appear more and more (See ((64625a01-b388-4404-91a9-baf438852bfe))).
  - Simply speaking, the whole market is exposed outside and turned to legal. Things is not turn good way to develop, because the rule of censor is not public. So I never touched a domestic galgame till now, because I don't think how deep in some topic they could reach, and that matters.
  - Yet the most friendly platform is steam, but they have the censor as well, including child porn or something else, which is different with Japan. I doubt, does it make sense? I don't know. I just dream a platform, which could give me all I want. But seemly it's just a dream. (See ((6463bf85-9f47-43a8-b65f-047dc1e2ebdf)))
  - In broad strokes, I devided it into two categories now, althougt they have more details. (See ((64625a01-1706-4e5d-ba30-e303492e8e84)))
    - galgame/jerk-off (See hentai details)
    - galgame/god
- ## HOW
  - DONE How to [[unpack]] a galgame, for getting their resource?
    collapsed:: true
    - ((63db96e5-053c-4978-8860-a305fa58f26c))
      id:: 63da20d9-3875-4191-a09a-735a0ca76cc5
    - DONE Mp4 No Loss Encode | MP4无损压缩
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
    - DONE Diff 2 compressed video info (size under different bitrate/High@L ...)?
      collapsed:: true
      - 比较两个命令的输出有何区别 (最好着色)?
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
    - [[新人也能懂的galgame游戏解包方法]]
  - DONE How to play in different devices?
    collapsed:: true
    - [zeas2/Kirikiroid2](https://github.com/zeas2/Kirikiroid2)
    - [JoiPlay](https://joiplay.cyou/)
    - [Tyranor模拟器正式发布|个人日记 - 绯月ScarletMoon](https://bbs.kfmax.com/read.php?tid=912800&sf=233)
    - [Studio O.G.A.](https://onscripter.osdn.jp/)
      collapsed:: true
      - [onsshare/onscripter: onscripter clootection](https://github.com/onsshare/onscripter)
    - [xupefei/Locale-Emulator: Yet Another System Region and Language Simulator](https://github.com/xupefei/Locale-Emulator)
  - DONE Should I build each page for every single galgame? Just like book, Is that necessary? ~~Pointful~~ Meaningful? @20221121
    collapsed:: true
    - **Unlike book**, they wont have a single page
      - But if, one day, the discuss about origin game increased a huge amount. I will turn it to page. But now, I just record the name I played, I don't have too interest and energy in it. \#changelog/wiki
        - ==In a way, this is a decide about hierarchy for content, or just for category?==
        - And this decision is not limited to galgame, more adopt to items of 2022, like hobby / archive. If they're huge, turn it to page, not build a single page immediately.
  - WAITING How to play without zh-has translation?
    collapsed:: true
    - title:: hanmin0822/MisakaTranslator
      author:: hanmin0822
      description:: "御坂翻译器—Galgame/文字游戏/漫画多语种实时机翻工具"
      source::  [hanmin0822/MisakaTranslator: 御坂翻译器—Galgame/文字游戏/漫画多语种实时机翻工具](https://github.com/hanmin0822/MisakaTranslator) ![](https://img.shields.io/github/stars/hanmin0822/MisakaTranslator)
      created:: 202012
      description:: Doc with [GAL党的福音——开源生肉翻译器MisakaTranslator正式版发布 - 知乎](https://zhuanlan.zhihu.com/p/112895928)
    - title:: miaomiaosoft/PandaOCR
      author:: miaomiaosoft
      description:: "多功能OCR图文识别+翻译+朗读+弹窗+公式+表格+图床+搜图+二维码"
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
  - bookmark
- ## Namespace
  - {{namespace galgame}}
- ## ↩ Reference
  - [月幕Galgame-最戳你XP的美少女游戏综合交流平台 | 来感受这绝妙的艺术体裁](https://www.ymgal.games/index)
  - [GAL必备 - ACG喵导航](https://www.miaoaaa.com/favorites/gal%e5%bf%85%e5%a4%87)
  - https://zh.moegirl.org.cn/zh-hk/Galgame
  - [我的galgame资源站--忧郁的loli_忧郁的弟弟](https://www.mmgal.com/)
  - [天遊二次元-非专业的PC及APP之Galgame情报，专攻汉化文字游戏，原天使二次元](https://www.tiangal.com/)
    - [天使二次元 — 本站专注ACG，主攻Galgame，兼攻Comic，Anime。以汉化版Galgame为主，为未来Gal中文界培养生力军。](https://www.tianshie.com/)
  - [GMgard ](https://gmgard.com/)
  - [琉璃神社★分享动漫快乐](https://acg.gy)
  - [南+ South Plus - powered by Pu!mdHd](https://www.south-plus.net/)
    - [北+ South Plus - powered by Pu!mdHd](https://www.north-plus.net/)
    - [西+ South Plus - powered by Pu!mdHd](https://www.east-plus.net/)
    - [夏+ South Plus - powered by Pu!mdHd](https://www.summer-plus.net/)
  - [紳士 - 4Gamers](https://www.4gamers.com.tw/gentlemen)
  - [ACG里世界](https://acgn.zone/)
  - [『澄空学园』 GalGame专题网](https://bbs.sumisora.net/)
  - [混沌心海 -](https://imcsea.club/)
  - [臭鼬娘 - 恋屁同好交流分享](https://www.skunkgirl.cc/)
  - [M社討論組](https://lt.gkdacg.com/)
  - [ようこそ、紳士会所へ！](https://www.sshs.pw/)
  - [Comici | 漫爱次元](https://www.comici.win/)
  - ~~[紳士向 | 搜尋標籤 | udn遊戲角落](https://game.udn.com/game/tag/紳士向)~~
-