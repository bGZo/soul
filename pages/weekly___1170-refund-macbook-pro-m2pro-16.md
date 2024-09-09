also:: 祛魅 MBP 
icon:: 📝
created:: [[20240113]] / [[20240831]] 
exclude-from-graph-view:: true
status:: writing/draft
tags:: #macbook

- > 乔布斯最大的成就就是让一帮连 vi 都用不利索的人自以为是 geek
  https://www.v2ex.com/t/166440
- 时值春运回家，前前后后折腾了两次 arch Linux，均以失败告吹，ARM 笔记本还遥遥无期，10月极其昂贵的M3 MAX 发布后，M2Pro 翻新被一抢而空，病急乱投医，信用卡分期 ¥18799 万入手了 [16inch M2 Pro 32 + 512 的MBP](https://www.apple.com.cn/shop/product/G1770CH/A)。周六日使用两天后，决定退款。这注定是一场祛魅的体验。
-
- ## 首先，我来说一说买它的理由：
  id:: 66d2906b-7503-4d60-9e2b-93322b1e623d
  - ARM 架构；
    logseq.order-list-type:: number
    collapsed:: true
    - 能耗比；
      logseq.order-list-type:: number
      collapsed:: true
      - 续航非常长；
        logseq.order-list-type:: number
        background-color:: red
    - 无需转义，原生支持 iOS 应用；
      logseq.order-list-type:: number
      id:: 66d2930d-a974-406b-8323-85b8eafa646e
      collapsed:: true
      - 打破手机独占 APP 的设计；
        logseq.order-list-type:: number
  - 联合统一架构；
    logseq.order-list-type:: number
    id:: 66d292ca-5bd4-40ea-874c-52e6bf19bf6b
    collapsed:: true
    - 内存可以当显存使用；
      logseq.order-list-type:: number
  - 统一通知系统；
    logseq.order-list-type:: number
    collapsed:: true
    - Mac 也可以走统一消息平台而无需后台挂起；
      logseq.order-list-type:: number
  - 选 16 寸，是因为 14 寸有功耗墙的问题[^power_wall]；
    logseq.order-list-type:: number
    collapsed:: true
    - Mac 默认用充电器功率限制处理器功耗，14寸的功耗墙在 60w 左右，16寸的功耗墙在 140w 左右；
      logseq.order-list-type:: number
    - 14寸用 96w 的充电器只能提升充电速度，TDP是定死的；😆
      logseq.order-list-type:: number
    - logseq.order-list-type:: number
-
- ## 然后，我们可以来 Judge 一下 Apple 了：
  - Everything everywhere paid for me
    logseq.order-list-type:: number
    collapsed:: true
    - 与我在 [[your-next-pc-is-never-being-an-ipad-pro]] 中的体验如出一辙，一切都带有铜臭味。
      logseq.order-list-type:: number
      - 我也终于能对苹果的号召力有点体会了，因为这份用户是最能掏钱解决问题的，我无法肯定地说这是一个比较正确的方式，但是至少我所知的开发者们都很吃这一套，也愿意为这些事情掏腰包，毕竟穷可能只是我的问题。
        logseq.order-list-type:: number
  - ((66d292ca-5bd4-40ea-874c-52e6bf19bf6b))
    logseq.order-list-type:: number
    collapsed:: true
    - 因为不熟悉炼丹，拿到手后也没有测试跑 AI 的能力，但是逛论坛后发现，Mac 在训练 AI 上还是打不过 CUDA，只在部署和推理层面有优势，加上生态也没有建立起来（苹果只手写了一个 [tensorflow-metal](https://developer.apple.com/metal/tensorflow-plugin/) 的引擎，听说也是半死不活的，提 ISSUE 没有人管），基本没法和 NVIDIA 那边玩。对于这些点 「林亦」只字不提，已经把他拉黑了； [[20231202]]
      logseq.order-list-type:: number
      - https://v2ex.com/t/959841
        logseq.order-list-type:: number
      - https://v2ex.com/t/864729
        logseq.order-list-type:: number
  - ((66d2930d-a974-406b-8323-85b8eafa646e))
    logseq.order-list-type:: number
    collapsed:: true
    - 是的，这是当时我愿意掏钱买它的最大理由，但可以预见的是，Apple 会完全尊重开发者，把是否可以侧载的权力交给了开发者控制，并限制用户的使用范围，理所当然的事情发生了，Mac OS 开始阻止用户侧载 App，via: https://www.ithome.com/0/534/909.htm
      logseq.order-list-type:: number
      - 完全可以理解，如果一个开发者无法控制自己应用的分发渠道，那么将没有人愿意再为 Mac OS 开发软件；
        logseq.order-list-type:: number
  - 16 inch 并不轻便的 **体重**；
    logseq.order-list-type:: number
    id:: 66d29d71-3685-4d6e-bcb9-045e6256c024
    collapsed:: true
    - 我的旧游戏本，体重大约为 2.35kg，而我手上这台大概 2.1kg，
      logseq.order-list-type:: number
      - 相差无几，甚至只是一个 iPad 的重量！
        logseq.order-list-type:: number
    - 唯一可圈可点的期就只剩这块屏幕和扬声器了。
      logseq.order-list-type:: number
  - 苛刻的 **边角设计**；
    logseq.order-list-type:: number
    id:: 66d29be5-b6b4-49f6-81f9-2161eb396fcb
    collapsed:: true
    - 边角过渡的设计，非常硌手。尤其是触控板下方的凹槽处，给人一种能被划伤的感觉。很难想象这是两万块的笔记本所带来的用户体验，如果你在膝盖，或者肚皮上码字，配合 ((66d29d71-3685-4d6e-bcb9-045e6256c024)) 你将获得在钉板上打字的体验。胳膊会被勒出显而易见的红印，并且非常难受。
      logseq.order-list-type:: number
  - **文件系统** 驱动支持匮乏；
    logseq.order-list-type:: number
    id:: 66d29f06-a4b6-4cf0-8365-52f141ac16dd
    collapsed:: true
    - 无法读写 NTFS
      logseq.order-list-type:: number
      id:: 66d29d6c-ecd4-4a14-8038-c5f6af843bd9
    - WAITING 无法读写 EXT4
      logseq.order-list-type:: number
    - 基于以上两点，基本可以抛弃 Windows 和 Ext4 格式的硬盘。你可以推测出，在 Apple 定义的用户中，是不存在 Linux 和 Windows 的用户的，这可以理解，但最让人生气的是，在十多年前的 10.13 版本中，是可以支持写入的[^Old_Support]，这算是 Mac 的人为切割，决策非常令人迷惑，并拒绝给出任何解释。
    - >The real question is what would Microsoft/Apple gain?
      https://www.reddit.com/r/linuxquestions/comments/p3bxne/why_isnt_ext4_readablemountable_on_mac_nor_windows/
  - 无 **剪切板** 设计；
    logseq.order-list-type:: number
    id:: 66d2a3cb-ff53-44b9-80e6-22e252d51a8a
    collapsed:: true
    - 这真的是用了就回不去的设计，你很难想象如果你剪切错了一段文本，在无法撤销的情况下，你将永远丢失该文本。
      logseq.order-list-type:: number
  - **内存**管理
    logseq.order-list-type:: number
    collapsed:: true
    - 第一次拿到机器后体验一番后，打开内存一看已经占用 `20/32` 之多，内存压力虽然还是绿的，但还是有点吓坏了
      logseq.order-list-type:: number
    - 重启重新跑软件后，发现开了 Safari 用一段时间后，确实会这样。跟 FF 很像啊 ）
      logseq.order-list-type:: number
  - 早期 M1 M2 存在**硬件缺陷**问题，如
    logseq.order-list-type:: number
    collapsed:: true
    - 音响破音
      - https://v2ex.com/t/898759
      - https://v2ex.com/t/966194
  - 文件不支持直接 **剪切**；
    logseq.order-list-type:: number
    id:: 66d2a554-cc8b-4ba1-8ba8-a50070074e5a
-
- ## 有限的解决方案
  - ((66d29be5-b6b4-49f6-81f9-2161eb396fcb))
    logseq.order-list-type:: number
    collapsed:: true
    - {{video https://www.youtube.com/watch?v=NnGAlf1hjs4}}
      logseq.order-list-type:: number
  - ((66d29d6c-ecd4-4a14-8038-c5f6af843bd9))
    logseq.order-list-type:: number
    collapsed:: true
    - {{nav https://mounty.app}}
      logseq.order-list-type:: number
    - {{nav https://www.drbuho.com/buhontfs}} [[20240615]]
      logseq.order-list-type:: number
    - 虚拟机[^UTM]
      logseq.order-list-type:: number
  - ((66d2a3cb-ff53-44b9-80e6-22e252d51a8a))
    logseq.order-list-type:: number
    collapsed:: true
    - created:: [[20240831]]
      description:: Lightweight clipboard manager for macOS
      type:: github/repo
      source::  {{gh p0deje/Maccy}}
  - ((66d2a554-cc8b-4ba1-8ba8-a50070074e5a)) [^Move_File]
    logseq.order-list-type:: number
    collapsed:: true
    - 统一走复制
      logseq.order-list-type:: number
    - 在第二个目录选择移动到这里（快捷键 `command+option+v`）
      logseq.order-list-type:: number
  - 允许从任何来源下载软件 via: {{nav-ri https://zhuanlan.zhihu.com/p/51328476}}
    logseq.order-list-type:: number
    collapsed:: true
    - logseq.order-list-type:: number
      ```shell
      sudo spctl --master-disable
      ```
  - Download Proxy
    logseq.order-list-type:: number
    collapsed:: true
    - logseq.order-list-type:: number
      created:: [[20240831]]
      type:: github/repo
      source::  {{gh MetaCubeX/ClashX.Meta}}
  - `brew` 包管理器 via: {{nav-ri https://zhuanlan.zhihu.com/p/354385629}}
    logseq.order-list-type:: number
    collapsed:: true
    - logseq.order-list-type:: number
      ```shell
      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
      ```
  - 硬盘读写量查看 via: {{nav-ri https://zhuanlan.zhihu.com/p/354385629}}
    logseq.order-list-type:: number
    collapsed:: true
    - logseq.order-list-type:: number
      ```shell
      brew install smartmontools
      smartctl -s on disk0
      smartctl -a disk0
      ```
  - JDK Manage via: {{nav-ri https://sdkman.io/}}
    logseq.order-list-type:: number
    collapsed:: true
    - logseq.order-list-type:: number
      ```bash
      curl -s "https://get.sdkman.io" | bash
      source "$HOME/.sdkman/bin/sdkman-init.sh"
      ```
  - Apple Silicon 准备好了吗 via: {{nav-ri https://isapplesiliconready.com/for/productivity}}
    logseq.order-list-type:: number
    collapsed:: true
    - 阿里云盘
      logseq.order-list-type:: number
  - Safari 下载自动解压 ZIP via: {{nav-ri https://zhuanlan.zhihu.com/p/349504217}}
    logseq.order-list-type:: number
  - Dell 显示器控制驱动 via: {{nav-ri https://www.dell.com/support/home/zh-cn/product-support/product/dell-display-peripheral-manager/drivers}}
    logseq.order-list-type:: number
  - 快捷键
    logseq.order-list-type:: number
    collapsed:: true
    - 截图
      logseq.order-list-type:: number
      - 全屏，Shift、Command、3
        logseq.order-list-type:: number
      - 区域，Shift、Command、4
        logseq.order-list-type:: number
      - 窗口，Shift、Command、4、Space
        logseq.order-list-type:: number
    - https://support.apple.com/zh-cn/102646
      logseq.order-list-type:: number
-
- ## 期望未来会发生的变化
  - 更多侧载软件
    logseq.order-list-type:: number
    collapsed:: true
    - 拼多多；
      logseq.order-list-type:: number
    - 淘宝；
      logseq.order-list-type:: number
    - 美团；
      logseq.order-list-type:: number
    - Snpid；
      logseq.order-list-type:: number
    - ---
    - **已经支持并由衷的推荐**：
      - 微信读书
        logseq.order-list-type:: number
      - 酷安
        logseq.order-list-type:: number
      - 得到
        logseq.order-list-type:: number
-
- ## Alternatives
  - Dell https://www.dell.com/zh-cn/shop/
  - Surface https://www.microsoftstore.com.cn/surface/surface-pro-9
    - 品控堪忧，https://v2ex.com/t/911230
  - ThinkPad https://shop.lenovo.com.cn/
  - [Dell XPS 和 Surface Book 哪个替代 MBP 更好一些？ - V2EX](https://v2ex.com/t/570244)
-
- ## ↩ Reference
  - logseq.order-list-type:: number
    [^power_wall]: http://post.smzdm.com/p/az68nq70/
  - logseq.order-list-type:: number
    [^Old_Support]: https://www.zhihu.com/question/365552114, with official discuss on https://discussions.apple.com/thread/253707407
  - logseq.order-list-type:: number
    [^Move_File]: https://sspai.com/post/28389
  - logseq.order-list-type:: number
    [^UTM]: https://www.v2ex.com/t/894750, https://www.v2ex.com/t/896725, PD太贵，开源的 UTM 较好，使用文档 https://docs.getutm.app/guides/windows/
  - 清洁 Mac https://support.apple.com/zh-cn/HT204172
    logseq.order-list-type:: number
  - `.zshrc` 和 `.zprofile` 的区别
    logseq.order-list-type:: number
    - logseq.order-list-type:: number
      > For mac users running ZSH, the  ~/.zshrc file is evaluated every time a shell is launched. The ~/.zprofile file is only evaluated when you login to your mac user account.
      https://ss64.com/mac/syntax-profile.html
  - intel mac 生存记录 via: {{nav-ri https://www.v2ex.com/t/1008425}}
    logseq.order-list-type:: number
  - [我这个 16 寸 M1 Pro 的 MBP 续航很差 - V2EX](https://v2ex.com/t/925060)
    logseq.order-list-type:: number
  - [2021 款 16 寸 M1 Pro 钙版。续航只有 4 个半小时 - V2EX](https://v2ex.com/t/834059)
    logseq.order-list-type:: number
  - https://www.apple.com.cn/shop/product/G175BCH/A
    logseq.order-list-type:: number
    - 正好24499；
      logseq.order-list-type:: number
-
- #第二台电脑
  - ~~MBA 丐版SSH到服务器做开发，不知道是为了什么？为什么我一万块钱买了一台电脑还用不爽？~~
    - 最后我放弃购买 MBP M1Pro 64GB 的版本，大概需要2万，感觉不需要，未来如果大模型起来之后散热，功耗墙，能耗比会是一个巨大的问题，我更希望新款的MBP还是以前那种静音的状态，现在这个苹果让人非常不舒服，有点作呕。
    - https://strongbugman.github.io/
    - https://v2ex.com/t/807782
-