icon:: 📄
also:: [[]], 
created:: [[20240816]]
description:: 
tags:: #Android

- ## Why
  -
- ## How
  -
- ## What
  -
- ## Namespace
  - {{namespace root}}
- ## ↩ Reference
  - ifw: Intent Firewall, via: https://cn.apkjam.com/blog/ifw.html
  - twrp
    collapsed:: true
    - 刷第三方Recovery: TeamWin Recovery Project; **全触控操作 + 操作便捷**(同等对比下的 CWM )
    - > 用CWM双清或者三清甚至是四清, 是一件很麻烦很痛苦的事情, 因为你要一个一个点, 非常不方便, 这时TWRP方便的地方就体现出来了, TWRP可以勾选多个选项, 一次性完成工作, 不需要一个一个清(当然如果你愿意, 一个一个清也是可以的)在刷机的时候, 可不单单只刷rom, 可能我还要刷补丁, 刷Gapps, 刷内核, 刷什么乱七八糟各种玩意儿, 这时用CWM又十分蛋疼了, 乖乖的一个一个选, 一个一个刷进去吧, 而TWRP也可以一次性选择多个包, 自动按顺序帮你刷进去, 十分方便. via: http://www.oneplusbbs.com/thread-942394-1-1.html
  - magisk
    collapsed:: true
    - > 随着SuperSu (XDA非常著名的开发者ChainFire维护的一款作品) 走向商业化(很久没有更新), 安卓5.0之后, 谷歌封堵了大量的漏洞, 一些以商业化模式运作的各种所谓的一键ROOT工具全都玩完!, 这些东西相对来说还非常危险, 因为基本任何商业化或者第三方机构给出的超级用户管理工具, 都等于是把你的手机变成别人的了, 甚至他们还可以比流氓还流氓!. 而SuperSU不一样, 它一直是保持着非商业化运作, 并且更新非常积极, 但遗憾的是在2017年10月, 开发者ChainFire发布声明不再参与维护SU, 好像是把SuperSU卖给了中国的一家商业化运作的公司, 自此更新节奏非常缓慢, 目前SuperSU已经不能实现安卓O(8.0)以上更高版本的ROOT了, 而取代这一切的, 是Magisk. Magisk 是一位中国台湾的学生 @topjohnwu 开发的 Android 框架, 它不但可以获取Root权限, 而且支持Magisk模块. 其第一个版本发布于2016年8月,  由于当时Magisk刚刚出现, 支持的模块并不多, 且SuperSu依然流行, Magisk还鲜为人知. 直到SuperSu的消亡, 人们才想起Magisk, 此后Magisk迅速流行起来, 成为每一个玩机爱好者的必备工具. via: https://www.coolapk.com/feed/17973123?shareKey=OTliMmY4NTlkMWNkNWY0NTExYTQ~
    - **原理** : Magisk 则另辟蹊径, 通过挂载一个与系统文件相隔离的文件系统来加载自定义内容, 为系统分区打开了一个通往平行世界的入口, 所有改动都只在那个世界(Magisk 分区)里发生, 并不直接修改系统分区, 这样大大减小了Magisk的变砖概率, 而且就算变砖也可以通过卸载Magisk来恢复原来的系统分区. 比如我们的/system/xbin中没有su, 我们可以通过刷入相应的模块, 在系统启动初期, 将su映射到/system/xbin下来获取root.
    - 教程
      - 通过rec刷入Magisk(推荐)
      - 直接安装(需要Root权限)(系统版本小于Android P, 你可能需要先解锁系统分区)
      - 通过修补boot安装 (选中Rom解压后的boot.img, 并在rec中直接刷入修补后的boot文件. )
      - 见 [教程](https://www.coolapk.com/feed/17697847?shareKey=ODg2YmRkZmRiNGRmNWY0NTExMTQ~) , [救砖](https://mp.weixin.qq.com/s/Os8j55GNmazqSt2UYrwy1g)
  - xpose-taiji
    collapsed:: true
    - > Magisk的原理简单的说就是在系统boot时将其img挂载到自己的分区下, 构建一个虚拟文件系统, 和system分区无关, 以不修改系统文件为前提, 从而达到修改系统文件的效果. 通过这种方式绕过谷歌安全机制, 系统OTA升级, 部分"被禁"软件都可以正常使用. 而Xposed相反, 框架一旦被加载就会修改系统, 改动会影响在安全机制保护下的APP, 所以一些理财软件,比如某某银行可能就无法使用, 这些应用对root权限非常敏感. 总的来说Magisk是通过systemless方式获取root, xposed则需要root才可以工作. 所以magisk虽然集合了各种功能, 但延展性上不如Xposed, 两者虽有一些相似之处, 但本质上完全不同, Magisk是创建新的分区而Xposed是直接修改系统文件. 现在最好的结果就是二者相辅相成, 按自己需要. via: https://www.coolapk.com/feed/19489640?shareKey=MDUzNjMzMzk2ZTVmNWY0NTExNTA~
    - **Xpose**: Xposed框架的原理就是替换安卓系统的app_process文件, 从而实现对系统的接管, 通过回调模块的方式来达到不用修改APK就能改变其表现行为的目的. 用通俗的话来说就是是在任意进程启动之前, 能加载特定Xposed模块的代码, 从而控制任意进程的行为. 这些特定的Xposed模块, 能在App进程启动之前执行特定代码. app_process其实是存放在systen/bin目录下的一个程序, 其作用就是启动zygote, 在Android中, zygote是整个系统创建新进程的核心进程. Xposed框架Hook了核心进程Zygote, 而其他应用启动都是从Zygote进程fork而来, 就够达到针对系统上所有的应用程序进程的Hook. 举个例子, 比如很著名的某微信模块, 就是你在启动微信之前, 首先要运行模块内的一些脚本, 这些脚本会劫持微信这个APP里的所有行为, 所以最终能够实现微信内容防撤回, 自定义微信摇骰子和石头剪刀布.
    - **Taiji**: 详见[Taiji](https://github.com/taichi-framework/TaiChi) [Doc](https://taichi.cool/), 更加稳定. via: https://www.zhihu.com/question/316497403
    - **MODULE**:
      - [QNotified|QQ辅助性功能增强](https://github.com/ferredoxin/QNotified)
      - [Zhiliao|知乎去广告Xposed模块](https://github.com/shatyuka/Zhiliao)
      - [ChiMi|MIUI扩展插件(xposed)](https://github.com/yonghen/chimi-)
      - [其他](https://repo.xposed.info/module-overview)
  - Application
    collapsed:: true
    - 绿色守护
    - 黑域
    - Amplify
    - 写轮眼
    - 黑白门
    - more via: https://cn.apkjam.com/blog/bs.html
-