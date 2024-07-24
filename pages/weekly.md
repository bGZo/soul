icon:: 📅
created:: [[20230602]]
template:: weekly
template-including-parent:: false
exclude-from-graph-view:: true

  - also:: 
    icon:: 📅
  - ## Review
    collapsed:: true
    - ### A line about this week
      - 人生已走过了 天、 周、 个月。
    - ### A line about today
      -
    - ### What went well this week?
      -
    - ### What needs improvement?
      -
    - ### What could I have spent more or less time doing?
      -
    - ### What am I grateful for this week?
      -
    - ### What am I proud of this week?
      -
    - ### What brought me joy this week?
      -
    - ### What did I learn?
      -
    - ### What [[goals]] did I work towards?
      -
    - ### What [[goals]] will I focus on next week?
      -
  - ## [[weekly/]]
    collapsed:: true
    - icon:: 📅
      tags::
    - ## 这周发生了啥
      - ---
    - ## 对细小的声音，侧耳倾听
      - ---
    - ## 如果有天堂，那一定是图书馆的模样
      - ---
    - ## Not get more done, but rather to have less to do
      - ---
    - ## 人类一思考，上帝就发笑
      -
    - ## 沙发土豆的自我修养
      -
    - ## 这周有断舍离吗？
      -
    - ## 这周有什么多快好省的东西吗？
      -
    - ## 这周有吃什么好吃的吗？
      -
  - > What I need is not sex, instead of love, to be understood, and never feel alone.
- ## Why
  - 叙事疗法
    created:: [[20230304]]
    closed:: [[20230617]]
    collapsed:: true
    - #+BEGIN_NOTE
      「誇誇报」主张通过「誇誇」的形式记录自己的生活，对宏大叙事保持质疑，对个体的声音侧耳倾听，鼓励做自己，最终成为自己，像《你当像鸟飞往你的山》中说得那样：
      > Whomever you become, whatever you make yourself into, that is who you always were.
      无论你成为谁，无论你把自己变成了什么，那就是你本来的样子。
      「誇誇报」以月报的形式发布，上半部分相对固定，关注社会时事、社交媒体、阅读、播客与生产力，下半部分会有自己对生活的一些体会与理解，主张断舍离、多快好省，争取定期走出「舒适圈」、「同温层」。
      囿于笔者工科出身，水平有限，本报也摆脱不了「陈词滥调」、「信息茧房」的嫌疑，所以我只能写给不同时空的自己、写给我的朋友、写给我的爱人。如果路过的你也喜欢我的内容，希望我们能认识一下，谢谢你 ）
      #+END_NOTE#
    -
    - ## 侧耳倾听
      -
    - ## 保持质疑
      -
    - ## 这周发生了啥
      -
    - ## 二手知识
      -
    - ## Not get more done, but rather to have less to do
      -
    - ## 没关系，已经很厉害了👍
      - 截至完稿，人生走过 天、 周、 个月。
      - ### 沙发土豆的自我修养
        -
      - ### 人类一思考，上帝就发笑
        -
      - ### 断舍离
        -
      - ### 多快好省
        -
      - ### 这周有吃什么好吃的吗？
        -
- ## How
  - TODO Pull 工作摸🐟 [Gist](https://gist.github.com/bGZo/506b84a3a3e56bbf5b13e89fa4f9666f) 的笔记
    SCHEDULED: <2024-07-27 Sat 00:00 ++1w>
    collapsed:: true
    :LOGBOOK:
    * State "DONE" from "TODO" [2024-01-20 Sat 22:00]
    * State "DONE" from "TODO" [2024-01-27 Sat 21:38]
    * State "DONE" from "TODO" [2024-02-03 Sat 10:50]
    * State "DONE" from "TODO" [2024-02-24 Sat 10:45]
    * State "DONE" from "WAITING" [2024-03-10 Sun 16:32]
    * State "DONE" from "WAITING" [2024-03-16 Sat 14:52]
    * State "DONE" from "WAITING" [2024-03-23 Sat 16:28]
    * State "DONE" from "WAITING" [2024-03-30 Sat 20:09]
    * State "DONE" from "WAITING" [2024-04-08 Mon 07:21]
    * State "DONE" from "TODO" [2024-04-13 Sat 11:30]
    * State "DONE" from "TODO" [2024-04-20 Sat 23:30]
    * State "DONE" from "TODO" [2024-04-27 Sat 15:57]
    * State "DONE" from "TODO" [2024-05-04 Sat 09:14]
    * State "DONE" from "TODO" [2024-05-17 Fri 20:05]
    * State "DONE" from "TODO" [2024-05-26 Sun 22:40]
    * State "DONE" from "TODO" [2024-07-20 Sat 21:23]
    :END:
    - \{{iframe https://gist.github.com/bGZo/506b84a3a3e56bbf5b13e89fa4f9666f}}
      #+BEGIN_CENTER
      [Edit this gist](https://gist.github.com/bGZo/506b84a3a3e56bbf5b13e89fa4f9666f/edit)
      #+END_CENTER
    - [[logseq/sync]]
      collapsed:: true
      - ~~Android~~
        collapsed:: true
        - Google Drive: http://127.0.0.1:5244/gdrive/SamsungFiles/androidLogseq.md
      - ~~iOS (Download without coookie)~~
        collapsed:: true
        - https://www.icloud.com.cn/iclouddrive/0dfP2NK-LLjycO3mpP6-R7OSw#iOSLogseq
    - Combine week notes via ((66515680-e8b8-422b-8113-d79d42028cd4))
      - Windows
        - 合并一周
          - ```powershell
            Write-Host -NoNewline cat $($str=""; $format=", yyyyMMdd.\m\d"; $today = Get-Date; $startOfLastWeek = $today.AddDays(-($today.DayOfWeek.value__)); $endOfLastWeek = $startOfLastWeek.AddDays(5);$currentDate = $endOfLastWeek; while ($currentDate -ge $startOfLastWeek) { $str += $currentDate.ToString($format); $currentDate = $currentDate.AddDays(-1)}; echo $str.Substring(2);) "|" ac (Get-Date).AddDays(6 - [int](Get-Date).DayOfWeek).ToString("yyyyMMdd.\m\d")
            ```
        - 删除一周
          collapsed:: true
          - ```powershell
            Write-Host -NoNewline rm $($str=""; $format=", yyyyMMdd.\m\d"; $today = Get-Date; $startOfLastWeek = $today.AddDays(-($today.DayOfWeek.value__)); $endOfLastWeek = $startOfLastWeek.AddDays(5);$currentDate = $endOfLastWeek; while ($currentDate -ge $startOfLastWeek) { $str += $currentDate.ToString($format); $currentDate = $currentDate.AddDays(-1)}; echo $str.Substring(2);)
            ```
      - Linux
        collapsed:: true
        - ```
           seq -s", " 20231015 20231021 | xclip -selection clipboard
          ```
- ## What
  -
- icon:: 📅