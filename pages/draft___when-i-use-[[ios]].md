title:: draft/when-i-use-[[ios]]
tags:: #[[iOS]]

- when I use [[iOS]], here some wired things I felt:
- 🌐 代理的爱恨纠葛
  collapsed:: true
  - 选择 via: [谈谈 iOS 平台上的几款代理软件 - Steven's Blog](https://blog.hly0928.com/post/talk-about-some-proxy-apps-on-ios/)
    - ShadowRocket
    - Quantumult X
    - Surge
    - Loon
    - Stash
    - Choc
    - 补充
      collapsed:: true
      - 其实我个人也是耗电敏感人员, 但查了一下好像没什么区别. via: [小火箭后台一直挂着耗电大嚒？ - V2EX](https://v2ex.com/t/641714)
    - WAITING iOS 小火箭 DNS 有时候有大病...
  - 使用
    collapsed:: true
    - 小火箭的分流策略需要在 Tab2 上面对应的配置详情里面设置. Index 的面板基本是没用的, 总体上和 Clash 差别不大.
  - 付费
    collapsed:: true
    - 因为对 AppleID 被风控的不确定性, 我排斥对 Apple Store 的付费, 能尽量避免就尽量避免.
      - 美区 Apple ID 购买礼品卡失败
        - 日区有人成功过, (自己的 Play 商店也是日区. via: [请问如何给港区APPLE ID充值](https://bgm.tv/group/topic/372135)
        - 我个人猜测是发行终止了和美区的交易, 这位也是2020年用美区非人哉借记卡突然被封. via: [美区 APPLE ID 被封 - V2EX](https://www.v2ex.com/t/720736)
        - 补充: 如果未来有需求, 会考虑把 AppleID 转回日区...
          - [中国区的Apple ID转地区到美国区会出现什么问题吗？ - 知乎](https://www.zhihu.com/question/31841333)
    - 读懂美国地址
      - ```
        John Smith (first name(given name), last name)
        via: https://www.zhihu.com/question/19864402
        
        (406) 443-4577
        10 Alta St
        Helena, Montana(MT), 59601
        
        电话
        道路地址
        市名, 州名(缩写), 邮编
        ```
    - 注册好了就不用挂代理了, 兑换, 购买, 下载全部可以在国内网络进行.
    - [ ] 我不理解为什么国内商店仍然存在诸多 VPN 软件, 明面直接写着国外访问加速的字样? 却只有这类正经代理的软件遭到下架?
    - [ ] 但是不知道为什么不能登录 iCloud? 一登听说就会封号?
  - 外区Store List
    collapsed:: true
    - Spotify
    - Github
    - Reddit
    - Discord
    - Bilibili
- 🤮 自认为傻逼的点
  collapsed:: true
  - 文件系统: 用户看不到任何应用下载到我手机里面的东西, 就像是 Android 11 之后无法访问 `android/data` 目录相似.
    collapsed:: true
    - KDE Connection (局域网传输工具) 传输的图片会保存在文件中, 而不会显示在图库中.
    - 基于上一点, 文件里面的图片需要保存到图库才可以显示在图库中.
    - QQ/WeChat 只能通过通过应用内置的空间清理工具.
  - 相册
    collapsed:: true
    - 查看图片信息
      - 如果你想精确地知道这张照片的拍摄时间, 你需要先 保存文件到文件, 然后在文件下面看到详细信息... via: [iPhone手机如何看图片属性（大小 拍摄时间等）？ - 知乎](https://www.zhihu.com/question/21087765)
  - 设置系统: 设置里的应用列表是可以设定权限, 但是把系统应用的设置塞进设置而不是嵌到对应应用还是很反直觉的.
    collapsed:: true
    - Safari 浏览器的设置就是在应用里找不到, 必须自己去设置里面设置才可以生效.
      - 而且只有当通过主窗口下载文件后, 下载按钮才会出现.
  - 输入法以及剪贴板
    collapsed:: true
    - 输入法我的刚需 (Gboard), 系统自带完全无法满足.
          ```diff
          - 26全键 + 独立数字键
          - 简单直接的逗号快捷键
          - 完全的剪贴板历史
          ```
  - 整理桌面多个图标
    collapsed:: true
    - 两只手: 一只手托住要移动的应用集合, 另一只手再执行选中操作.
  - 后台应用刷新
    collapsed:: true
    - 低电量模式自动禁用
    - close
      - 睡前将聊天软件置入后台, 聊天内容不更新. 起床后打开聊天软件, 更新所有聊天记录
    - open
      - 睡前将聊天软件置入后台, 聊天内容周期性更新. 起床后打开聊天软件, 更新部分聊天记录
  - iCloud
    collapsed:: true
    - 应用的文稿数据都可以同步到 iCloud, 也支持三方的同步([Android](https://play.google.com/store/apps/details?id=com.granita.caldavsync), [Windows](https://support.apple.com/en-us/HT204283)), 但总体来说不方便.
      - 需要单独去系统设置 -> 日历里单独添加 Outlook 账户才可以同步日历. 倒是联系人可以直接 Outlook 内设置同步. 但是拿到的也是残废数据, 需要一定的学习成本:
        - Reminder
          - MicrosoftTODO 的子任务会在 iPhone 上直接消失.
        - iCloud/Onedrive 数据不互通导致需要后期需要重新设置 via: [微软验证器 microsoft authenticator 弄丢了我所有的 2fa - V2EX](https://www.v2ex.com/t/805856)
    - 完全可以用价格更便宜, 跨平台支持更友好的 Onedrive 取代, 如果没有 Mac 生态的先入为主, 基本不会被绑架.
  - {{embed ((62ef584a-ffb1-4627-9ddf-e0d5c1af97f4))}}
  - 电池
    collapsed:: true
    - 不知道长时间使用背夹电池有什么坏处, 至少这 20 多天的使用是没有掉健康度的, 一直持续满电状态运行. 因为换第三方电池担心适配问题(不仅是弹窗问题), 很多地方我也不太清除, 系统底层对非原装电池进行了硬件级别的限制, 就算搬电芯骗过手机系统, 但是真的能一样吗?
    - 反过来说, 放弃大电池大容量的选择, 再花原机 1/3 的价钱去换一个电池吗? 官方多做的也只是进系统Boot, 激活一下的操作, 这真的值得吗?
- 💓 无与伦比的点
  collapsed:: true
  - Telegram 走的居然是系统通知...
- 🤯 旧版本焦虑
  collapsed:: true
  - {{embed ((63b0e36a-fa4c-455a-a22c-ec1087860249))}}
- Link
  collapsed:: true
  - [Random US Address | Best Random Tools](https://www.bestrandoms.com/random-address)
  - [ios15 夜间待机 wifi 比 5g 耗电 这个“偷偷”下载的是啥 求大佬分析 - V2EX](https://v2ex.com/t/855434)
  - [前两天申请了美区 Apple ID，日常使用如何防止被封？ - V2EX](https://v2ex.com/t/739530)
- More
  - [为什么iPhone充电从99%到100%特别慢？ - 知乎](https://www.zhihu.com/question/28689748)
  - [0202年了，全世界的旗舰都是OLED屏幕，为什么iPad Pro还是LCD？ - 知乎](https://www.zhihu.com/question/423238095)
  - [M1 芯片的 iPad Pro为什么不用OLED 屏幕，而是用mini-LED这种lcd屏幕呢？ - 知乎](https://www.zhihu.com/question/455830948)
  - [iPhone11的屏幕分辨率真的很低吗？ - 知乎](https://www.zhihu.com/question/368566743)
  - [苹果ios系统有哪些免费好用的阅读app？ - 知乎](https://www.zhihu.com/question/265181314)
  - [iPhone 官方售后换电池的价格是多少？ - 知乎](https://www.zhihu.com/question/22278345)
  - [如何在win10电脑上使用iphone的备忘录？ - 知乎](https://www.zhihu.com/question/374272966)
  - [iphone 7plus 从qq 上接收的文件储存在哪里？怎么删除？ - 知乎](https://www.zhihu.com/question/53759855)
  - [iPadOS 被从 iOS 中割裂出来是否合理？ - 知乎](https://www.zhihu.com/question/327998387)
  - [为什么淘宝上的苹果背夹电池是砍头的？ - 知乎](https://www.zhihu.com/question/323967346)
  -
  - [你有哪些珍藏的iOS应用历史版本？ - 知乎](https://www.zhihu.com/question/444349056/answer/1736687688) & [iOS 旧版 APP 推荐与降级方法（持续更新） | 千灵](https://qianling.pw/ios-app/)
  - [5分钟教你一键式安装iOS旧版APP（2020年有效） - 知乎](https://zhuanlan.zhihu.com/p/42947889)
  - [关于 iPhone App 降级/安装旧版本的一点发现 - V2EX](https://v2ex.com/t/854460)
    collapsed:: true
    - App Thinning
  - [苹果手机不小心点了全部更新怎样取消啊_百度知道](https://zhidao.baidu.com/question/752343517278296124.html)
  -