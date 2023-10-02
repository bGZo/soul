alias:: 工具
icon:: 🛠
public:: true
start:: 20230531
tags:: #productivity
title:: Tool

  - template:: tool
    template-including-parent:: false
    collapsed:: true
    - alias:: 
      blog:: 
      changelog:: 
      community:: 
      document:: 
      icon::
      public:: true
      start:: ``{ date.now.format('YYYYMMDD') }``
      tags:: 
      title:: ``{ c.page.name }``
- ## Why
  - Creating thing more productive.
- ## How
  - Avoid the [[productivity pron]]
- ## What
  - What is different between [[bookmark]]s [[vs]] tools?
    collapsed:: true
    - > However, the term "tool" is often used more broadly to refer to physical devices or software programs that are used to perform specific tasks or functions. This could include hand tools, power tools, and digital tools like computer programs and apps. While a bookmark is a digital tool that is used in a web browser, it is not typically considered to be the same type of tool as a hammer or a screwdriver, for example.
      #chatGPT
    - 我发现很多存在 Logseq 中的工具都是 Bookmark 形式, 并且在 Build 的过程中, 总是把这两个概念混淆; Tool 和 Bookmark 是两个不用的东西, **Bookmark 作为工具的一种, 可不可以 More than a tool? 比如, 类 News 的网站算是一种工具吗?**
      - ==嗯, 好像不可以==, 但是可以这样看: Bookmark 记录 Tool Web App 更加合适, 相较于客户端, Bookmark 更加偏向于提供模糊的功能 (非专精); 而不是像某些 Small tool 去解决用户的痛点
  - What I learned in recent year:
    collapsed:: true
    - #+BEGIN_PINNED
      **开发人员要有意识地搭建自己的技术框架**;
      #+END_PINNED
      - #+BEGIN_QUOTE
        编写自己的工具库, 比如编码转换、网络通信等，还可以把阅读过并增加了很多注释的开源项目，如图形库、电驴源码、即时通讯源码等等放进去. 
        — [开发人员如何构建自己的学习笔记系统？ - 知乎](https://www.zhihu.com/question/273440522/answer/368778127)
        #+END_QUOTE
    - #+BEGIN_PINNED
      定期磨刀，但是禁止 **Productivity Pron**;
      #+END_PINNED
    - id:: 64772f1d-4e63-462e-8fbe-9e41e802b2c5
      #+BEGIN_PINNED
      [[opensource]] ≫ Paid Service;
      #+END_PINNED
      - 不要迷信付费付费去广告那一套, 对于使用频率极低的那一部分软件, 我觉得花一两分钟换取即时的服务完全值得.
        - 注意看作者有没有注明服务的服务周期，也就是说，服务明天就有可能被下架. 😁
      - 任何具有 DRM 的软件平台都不可太过信任, 因为你无法保证商业公司未来对不同用户的决策.
      - Is **DRM-FREE** the best? #non-standard
        collapsed:: true
        - My answer is yes, in the most case, IDGAF. While situation is always the same. Maybe the work will gone if they ever release a DRM FREE version.
        - > DRM-free, or digital rights management-free, refers to content (such as music, movies, or ebooks) that is not protected by DRM technology. DRM is a type of software that is designed to prevent unauthorized use or copying of digital content.
          >
          Whether or not DRM-free content is "best" is a subjective question and depends on your personal preferences and needs. Some people prefer DRM-free content because it gives them greater flexibility in how they can use and access the content. For example, DRM-free music can often be played on any device, whereas DRM-protected music may only be able to be played on certain devices or through certain apps.
          >
          On the other hand, DRM can help content creators and distributors protect their intellectual property and ensure that they are fairly compensated for their work. Some people may therefore prefer content that is protected by DRM in order to support the creators and ensure that they are able to continue producing high-quality content.
          >
          Ultimately, the decision of whether or not to purchase DRM-free content is a personal one and depends on your priorities and needs.
          #chatGPT
    - #+BEGIN_PINNED
      Product never has [[changelog]] will be in [[sucks]];
      #+END_PINNED
      - 我不需要看你的文档 (Intro Articles), 拜托, 只需要告诉我和上个版本有什么变化就可以(有一点点傲慢), 摆脱对他人搬运的依赖. 就像是处理内容农场一样
-
  - [[unlock]] ppt/pptx
    - pptx: `.pptx` rename to `.rar` -> edit `./ppt/presentation.xml` -> find `<p:modifyVerifier .../>` -> delete it.
    - ppt: https://products.aspose.app/pdf/zh-hant/unlock/ppt
  - 断点续传
    define:: "指的是在上传/下载时，将任务（一个文件或压缩包）人为的划分为几个部分，每一个部分采用一个线程进行上传/下载，如果碰到网络故障，可以从已经上传/下载的部分开始继续上传/下载未完成的部分，而没有必要从头开始上传/下载。 可以节省时间，提高速度。 via: https://blog.csdn.net/liang19890820/article/details/53215087"
  - 百度网盘秒传链接: https://cangku.io/pages/178105
  - [Mathematical Alphanumeric Symbols - Unicode 字符百科](https://unicode-table.com/cn/blocks/mathematical-alphanumeric-symbols/)
  - [傲梅产品下载：硬盘分区软件下载、轻松备份软件下载、微信恢复软件下载](https://www.aomeikeji.com/download.html)