icon:: 🤮
also:: 苹果做得恶
created:: [[20240714]]
status:: writing/idea
tags:: apple
type:: sucks
exclude-from-graph-view:: true

- Apple 的风格就是这样，当你面向中上产做产品的时候，你会丢掉非常多烦恼，用户群本身的高学历、高资产就像是拥有丰富羊毛的羊群，讨好商客，就能换来开发者，换来良好的生态。
- ## Fuck [[apple-music]]
  - 音乐库是会受审查的，因为你无法找到下面的歌手 / 歌曲，您可以试试：
    logseq.order-list-type:: number
    - logseq.order-list-type:: number
      ```diff
      - 童话镇 - 陈一发儿
      - 关于郑州的基于 - 李志
      - 差不多先生 - hotdog
      ```
  - 非会员和狗不得入内，是的，你没有权利访问你的歌单，除非开会员
    logseq.order-list-type:: number
    - 这对迁移数据的用户是恼人的，所以就算我开着 AM 的会员，我依然不会创建自己的歌单；
      logseq.order-list-type:: number
      - 我知道就算创建了，他也不属于我，而是库克 😅
        logseq.order-list-type:: number
  - 安卓直连网络很卡，不如 iOS，总是卡卡的，现象在登录之后会好转；
    logseq.order-list-type:: number
  - 跨国家分享是不可能的，或者说，折腾成本是非常高的；
    logseq.order-list-type:: number
    - https://discussionschinese.apple.com/thread/140136779
      logseq.order-list-type:: number
    - https://zhuanlan.zhihu.com/p/377114774
      logseq.order-list-type:: number
  - iTunes 锁区
    logseq.order-list-type:: number
- ## Fuck apple tv
  collapsed:: true
  - 为什么要嵌入 Safari 呢？
    logseq.order-list-type:: number
    - 为什么不呢？
      logseq.order-list-type:: number
    - 浏览器能做的事情，远远大于电视盒子吧？
      logseq.order-list-type:: number
      - 用户隐私、财产安全是一个问题，官方当然可以用协议撇开责任；
        logseq.order-list-type:: number
      - 生态破坏，讨好用户的话，只会打击商家做苹果生态的信心，是对生态的降维打击；
        logseq.order-list-type:: number
      - 交互的不好做，这是另一个操作系统；
        logseq.order-list-type:: number
    - 当然你可以用 `ayiVideo`，但依据苹果傲慢的态度，将永远不予上架，并且你还得用交每年 99 刀的保护费，所以为什么要做呢？
      logseq.order-list-type:: number
      collapsed:: true
      - {{video https://www.youtube.com/watch?v=n49lVxMM4YA}}
        logseq.order-list-type:: number
- ## Fuck app store
  collapsed:: true
  - 审查，比如从 Store 中下载的 Telegram 不支持 18+ Show content；
    - via: https://github.com/telegramdesktop/tdesktop/issues/16346
- ## Fuck iOS
  collapsed:: true
  - Input -> 与 Gboard 的差异
    - 26全键 + **独立数字键**
    - 简单直接的**逗号快捷键**
    - 完全的**剪贴板**历史
  - App settings
    - 系统应用的设置并不在对应应用里，而是系统设置中，非常反直觉，参考Safari、相机等；
  - Home Launcher
    - 整理桌面多个图标时候，需要用到两只手，一只手托住要移动的应用集合, 另一只手再执行选中操作；
  - Photo
    - 无法直接看到相片的详细信息，如文件大小、拍摄时间；
      - 保存文件到文件, 然后在文件下面看到详细信息
  - File system
    - iOS 默认看不到任何应用下载到手机里面的东西。
      - 百度网盘的产品设计，你只能通过百度网盘访问自己的下载文件。
      - 不像安卓，应用约定都下载到 `Download` / 自己的文件目录那样
      - 所以我永远不会买一台连自己下载的文件都访问不了的大容量 iPad，要买到手也一定要越狱。
        #your-next-pc-is-never-being-an-ipad-pro
    - 其他应用的下载地址，如 KDE Connection，即使是图片，也会存储在文件中，而不是相册。
      - 需要用户选择保存，才可以显示在图库，这一点非常反直觉。
    - 所以带来的另一种后果是，你没有办法通过自己清理臃肿的应用，来减少手机存储的占用。
      - 虽然安卓自 Android 11 就默认禁止访问 `Andorid/data` 目录，自己能做的事情也越来越少。但是在 iOS 上，情况一向如此。
  - Battery health
    - #+BEGIN_NOTE
      iOS 17.4 正式取消电芯的使用，健康度将从系统日志中读取；
      #+END_NOTE
      - ~~自 iPhone 11 开始，iOS 都是通过读取电芯来读取电池健康度。~~
      - 不是经过 Apple 官方渠道（跑过官方的系统诊断）的电池，是会持续强制弹窗的；
      - 即个人如果随便更换电池，电池健康度将无法显示，这并不利于第三方电池的充电循环；
        - 就算可以通过手工搬电芯骗过系统，但这样的尝试不免有更多安全隐患；
    - 电池健康是一个无法衡量、玄学的问题；
      - 有的人用了一年才掉下 100%，有的人两个月就做到了；
      - 即使我套了聪明壳一年，电池健康度还是从 86%，干到了 78%；
      - 一两天，或者半个月，是完全看不出来的；
  - iCloud
    - 应用文稿的数据可以直接上 iCloud，这点爆赞，比安卓方便多了；
    - 支持三方的同步([Android](https://play.google.com/store/apps/details?id=com.granita.caldavsync), [Windows](https://support.apple.com/en-us/HT204283))
    - 照片同步的上位替代：[[onedrive]]，不要被 Mac 的生态套牢；
    - Outlook 无法通过应用日历同步到系统日历，需要在系统设置中，单独添加 Outlook 账户才可以；