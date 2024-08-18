filters:: {"rss" true}
icon:: ✈️
created:: [[20200108]]
document:: https://core.telegram.org/api, https://desktop.telegram.org/changelog
status:: tool/star
tags:: #instant-message 
type:: tool

  - template:: telegram/channel
    template-including-parent:: false
    - icon:: ✈️
      also:: 
      created:: ``ref(date.now.format('YYYYMMDD'))``
      description:: 
      exclude-from-graph-view:: true
      source:: {{tg ``c.page.name``}}
      type:: ``'telegram/channel'``
- ## Why
  -
- ## How
  - ### Shortcuts
    collapsed:: true
    - 功能相关
      - **搜索 >> Ctrl+F**
        联系人 >> Ctrl+J
        锁屏  >> Ctrl+L
        最小化 >> Ctrl+M
        关闭窗口 >> Ctrl+W / Ctrl+F4
        结束进程 >> Crtl+Q
    - 聊天文件夹及对话相关
      - **已保存的消息 >> Ctrl+0**
        所有对话列表 >> Ctrl+1
        聊天文件夹1~6  >> Ctrl+1~6
        最后一个文件夹 >> Ctrl+8
        **已归纳的对话 >> Ctrl+9**
        **已读此对话 >> Ctrl+R**
        下一对话 >> Ctrl+Tab / Ctrl+PageDown / **Alt+下箭头**
        上一对话 >> Ctrl+Shift+Tab / Ctrl+Backtab / Ctrl+PageUp / **Alt+上箭头**
        第一个对话 >> Ctrl+Alt+Home
        最后一个对话 >> Ctrl+Alt+End
        下一文件夹  >> Ctrl+Shift+下箭头
        上一文件夹 >> Ctrl+Shift+上箭头
        回复对话内上一条消息 >> Ctrl+上箭头
        回复对话内下一条消息 >> Ctrl+下箭头
    - 媒体文件相关（如音乐）
      - 播放媒体 >> 播放键（需键盘支持）
        停止媒体 >> 停止键（需键盘支持）
        上一媒体 >> 上一首（需键盘支持）
        下一媒体 >> 下一首（需键盘支持）
        暂停媒体 >> 暂停键（需键盘支持）
        切换播放暂停 >> 播放暂停键（需键盘支持）
    - 文本格式快捷键
      - 在键入消息窗口单击右键即可查看，在此不再赘述。
    - 备注：默认快捷键列表可在 Telegram\tdata 目录下的 shortcuts-default.json 文件内查看，请勿修改此文件的内容。若您想自定义快捷键，请在同目录的 shortcuts-custom.json 文件内添加后重启客户端即可生效
  - ### Find contents
    - [Telegram channels, groups and bots catalog - TELEGRAM-CHANNEL.NET](https://telegram-channel.net/)
    - [telegram中文搜索](http://www.sssoou.com/)
- ## What
  - ### Clients
    - Web alternatives [^ruanyifeng]
      - {{nav https://web.telegram.org}}
        logseq.order-list-type:: number
      - {{nav https://webk.telegram.org}}
        logseq.order-list-type:: number
      - {{nav https://webz.telegram.org}}
        logseq.order-list-type:: number
    - Desktop alternatives
      - https://github.com/UnigramDev/Unigram
- ## Namespace
  - {{query (property :type "telegram/channel")}}
    query-table:: true
    query-properties:: [:page :also :created :description :type :source]
- ## 📃 References
  - tg, 电报, t.me, telegram.me, telegram.org, telesco.pe, tg.dev
  - [^ruanyifeng]: https://twitter.com/ruanyf/status/1386900067852816386
  - ![Telegram（电报）：新手指南、使用教程及频.pdf](../assets/Telegram（电报）：新手指南、使用教程及频_1645371954006_0.pdf)
  - ![微信难用？！不如找个备胎.pdf](../assets/微信难用？！不如找个备胎_1645431869680_0.pdf)
  - [Telegram 各个系统客户端地址 - Blog](https://congcong0806.github.io/2019/01/08/Telegram/)
-
-
-