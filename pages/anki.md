icon:: 🛠
created:: [[20240728]]
document:: https://ankiweb.net
status:: tool/star
tags:: #learning 
type:: tool
wikipedia:: https://en.wikipedia.org/wiki/Anki_(software)

- ## Why
  - I was used to blame my hobbies except the study for forgotten knowledge in the past. And basically I picked up a wrong story from the first.
  - Now I have to recongnize, the forgetting things is prefactly normal, there's no bad habbies in judgement, only whether you like it or not!
  - So Anki is a power tool to help us to remember the knowledge. IDK how long [[logseq]] had worked for this, so I rather to use Anki again. (View some ((6469b1b9-9a75-4610-8580-1a049b7fed1d)) to interduce it)
- ## How
  - Firstly, I decided to use parent block ——— `anki` to include information I need to remember.
  - WAITING And try my best to remember them in the morning.
    \SCHEDULED: <2023-05-21 Sun 06:00 .+1d>
  - Then, I need a plugin to collect words in daily scenes. And [Online Dictionary Helper](https://chrome.google.com/webstore/detail/online-dictionary-helper/lppjdajkacanlmpbbcdkccjkdbpllajb) is a good extension to connect it, whose implement is interesting as well.
    - ```js
      /* https://github1s.com/ninja33/anki-dict-helper/blob/HEAD/ext/fg/js/client.js#L174-L181 */
      let url = `https://dict.youdao.com/dictvoice?audio=${encodeURIComponent(definition.expression)}`; //api of youdao audio
      const audio = this.audio[url] || new Audio(url); // awe new:
      ```
  - So I made a basic template `anki` to replace official one, although it has a little ugly and really simple, but it works well )
    - {{iframe https://gist.github.com/bGZo/b26301b0d528f41302f8d547f47f733f}}
  - And some add-ons deserved as following:
    - [AnkiConnect - AnkiWeb](https://ankiweb.net/shared/info/2055492159)
    - [AnkiConnect - AnkiWeb](https://ankiweb.net/shared/info/2055492159)
    - [AwesomeTTS - Add speech to your flashcards - AnkiWeb](https://ankiweb.net/shared/info/1436550454)
  - For using quickly, you could view shortcuts via ((6469cfdf-21b3-4c96-8a1a-a852de39f55e))
- ## What
  - DONE Donate Anki by purchasing in [app store](https://apps.apple.com/us/app/ankimobile-flashcards/id373493387) (￥163); #donation
    dollar:: 25
    closed:: [[20221029]]
    - > Use of the service is currently free, and the hosting costs are supported by sales of the [iPhone app](http://ankisrs.net/docs/AnkiMobile.html). As the hosting costs continue to grow, we may need to introduce a "freemium" model in the future, where basic accounts are free, and people can pay for accounts that support larger decks or extra features.
      — [Account Terms - AnkiWeb](https://ankiweb.net/account/terms)
  - Great manuals
    id:: 6469b1b9-9a75-4610-8580-1a049b7fed1d
    - [[基本概念]毕业间隔 简单间隔 开始简化 简单奖励 间隔修饰符 (douban.com)](https://www.douban.com/group/topic/79949605)
      collapsed:: true
      - 强项
        collapsed:: true
        - "艾宾浩斯曲线"
        - 随时复习
        - 自制卡
      - 难度 Level
        collapsed:: true
        - 生疏/错误
          - 没见过 / 见过也忘了
        - 困难/模糊
          - 用力想能记起来一点，但不完全
        - 犹豫/想起
          - 你仔细想，还是能够回忆出来
        - 顺利/正确
          - 没什么难度，基本熟悉了
        - 轻松/容易
          - 条件反射、一看便知
      - 搁置相关新卡片到隔日
        collapsed:: true
        - 1条笔记自动生成卡片1、2、3、搁置的话当你学完这条笔记的卡片1后，2和3就被搁置到明天再学习了也可以点击“取消隐藏”把搁置的显示出来
      - Note & Card
        collapsed:: true
        - Note 是 Fields 的集合
        - Card 由 Note 生成
          - 一条 Note 可以生成多个 Cards
          - 由同一条 Note 生成的 Cards 互为 Siblings
      - Time
        collapsed:: true
        - 毕业间隔
          - 当你回答Good时候，这张卡再次出现的延时时间
        - 简单间隔
          - 是当你回答是Easy时候，这张卡再次出现的延迟时间
        - 开始简化
          - 它控制着延迟时间因子。它通常在卡第一次出现时设置，如果第一次出现时，你的答案是good，正常延迟是1天，如果这个时间因子是250%，则下次再回答 good，延迟时间将是第一次延迟的2.5倍。如果最后一次延迟是1天，则当前延迟就是2.5天，如果上次延迟 是10天，则下次延迟就是25天。
        - 简单奖励
          - 答EASY 或 GOOD的时候，下次卡片，例如130%，就会乘以1.3之后再出现。百分比越高，卡片下次出现越晚——取决于你一开始简单间隔设定为几天
        - 间隔修饰符
          - 简单说就是调整卡片之后出现频率，越低下次出现时间越快
          - 公式
            - log(desired retention%) / log(current retention%)
            - Imagine we have a current retention rate of 85% and we want to increase it to 90%. We’d calculate the modifier as:
              - log(90%) / log(85%) = 0.65
    - [Intro - AnkiMobile Manual](https://docs.ankimobile.net/)
    - [Anki经验贴快速查询](https://www.douban.com/group/topic/80413417/) #deprecated
  - Shortcuts
    id:: 6469cfdf-21b3-4c96-8a1a-a852de39f55e
    - #+BEGIN_QUOTE
      Most of them are discoverable in the interface: menu items list their shortcuts next to them, and hovering the mouse cursor over a button will generally show its shortcut in a tooltip.
      — [Studying - Anki Manual (ankiweb.net)](https://docs.ankiweb.net/studying.html?highlight=shortc#keyboard-shortcuts)
      #+END_QUOTE
    - | Anki Keyboard Shortcut Windows | Function |
      | ---- | ---- | ---- |
      | CTRL+J | Toggle suspend or unsuspend cards |
      | CTRL+A | Select all cards in Anki while browsing |
      | CTRL+SHIFT+P | Switch profile |
      | CTRL+SHIFT+I | Import |
      | CTRL+E | Export |
      | CTRL+Q | Exit |
      | CTRL+Z | CTRL+Z to undo or return to the previous card |
      | / | Study deck |
      | F | Create filtered deck |
      | CTRL+SHIFT+A | Add-ons |
      | CTRL+SHIFT+N | Manage note types |
      | CTRL+P | Preferences |
      | F | Anki manual |
      | Space | Flip card |
      | 1 | Choose a “Fail” or “Again” response to a card. |
      | 2 | Choose a “Hard” response to a card. |
      | 3 | Choose a “Good” response to a card. |
      | 4 | Choose an “Easy” response to a card. |
      | A | Open a new card |
      | Tab | Switch from front of card to back |
      | Ctrl+Enter | Enter card into database |
      | Enter | Skip row |
      | Ctrl+N | Change note type |
      | Ctrl+D | Target deck |
      | Ctrl+L | Customize card template |
      | Ctrl+B | Bold text |
      | Ctrl+I | *Italic* text |
      | Ctrl+U | Underline text |
      | Ctrl+ + | SuperscriptSuperscript |
      | Ctrl+ = | SubscriptSubscript quick key |
      | Ctrl+ R | Remove formatting |
      | F7 | Set foreground color |
      | F8 | Change color |
      | Ctrl+Shift+C | Cloze deletion |
      | F3 | Attach Picture |
      | F5 | Record Audio |
      | Ctrl+M, M | MathJax inline |
      | Ctrl+M, E | MathJax block |
      | Ctrl+M, C | MathJax chemistry |
      | Ctrl+T, T | LaTeX |
      | Ctrl+T, E | LaTeX equation |
      | Ctrl+T, M | LaTeX math env. |
      | Ctrl+Shift+X | Edit HTML |
      | D | Decks |
      | B | Browse |
      | T | Stats |
      | Y | Sync |
      [49 Anki Keyboard Shortcuts for Win & Mac – LAYMN](https://laymn.com/anki-keyboard-shortcuts/) #quickref
-