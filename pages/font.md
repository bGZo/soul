alias:: 字体
icon:: 字
tags:: #designtags:: 

created:: 20230821
title:: font

- ## Why
- ## How
- ## What
  - Font collections
    - | Sence | Fonts |
      | Standard | Times New Roman |
      | Sans-serif | [Arial](https://zh.wikipedia.org/zh-cn/Arial) |
      | Serif | Times New Roman |
      | Monospaced | Sarasa Mono SC |
      | Cursive | Comic Sans MS|
      | Fantasy | Impact |
    - 微软雅黑
      collapsed:: true
      - > **微软公司斥巨资委托方正字体公司专门为Vista系统设计制作了微软雅黑(方正兰亭黑)**, 微软公司只拥有微软雅黑的使用权, 而版权在方正手中. 我们仅可以在Windows系统中使用微软雅黑！脱离Windows平台的一切商业行为, 都属于侵权行为, 同时在Windows系统下, 商业行为也不被允许, 包括网页设计中, 主动调用微软雅黑字体, 更不可以以图片的形式在网页中用到微软雅黑！
        via: [微软雅黑字体侵权？推荐20款无版权的开源字体！ - 知乎](https://zhuanlan.zhihu.com/p/49049779)
  -
  - DONE 中竖门 & 门
    collapsed:: true
    - ![](../assets/japan-men.webp)
    - 微软雅黑默认状态下部分字符显示为日文字符, 如`门`就会显示 '中间一竖的`门`'. 纠正方法换字体 --`文泉译米` 即可
      
      Profromence differences are related with [**CJK Unified Ideographs**](https://en.wikipedia.org/wiki/CJK_Unified_Ideographs), and relating to [CJK Font](https://en.wikipedia.org/wiki/List_of_CJK_fonts). And Some Font display the Japan Font as default pattern, such this `Mircosoft YaHei` in ubuntu when the sys encoding is `US_Utf-8`, but why the window is not such situation?<sup>[3](#j3)</sup>. Some more details [FAQ](https://www.unicode.org/faq/han_cjk.html) with it. By th way, Japan encodes CIJ and Chinese encodes GB.
    -
  -
  - DONE [[Linux]] [^linux]
    collapsed:: true
    - 单就字体渲染来说，Windows一直走在最前面。Linux因为其特殊的用途，在桌面方面一直落后于Windows。**在CRT时代，Windows有清晰的点阵字体，Linux使用的却是粗陋、显示为方框或乱码的中文字体。到了液晶屏时代，Windows花巨款买下微软雅黑字体版权，Linux却刚刚用上文泉驿点阵字体**。毕竟商业巨头，微软非常照顾自己用户的体验，在字体渲染方面，针对汉字过于复杂的“缺点”，豪掷百万美元买下1种针对PC显示器优化的微软雅黑字体，可谓用心良苦！
    - 由于中文字体笔画复杂的特点，在以前的低分屏和现在仍大量使用的中分屏上，中文字体显示一直是个难题。低分屏或中分屏的ppi都太低，肉眼可见屏幕像素颗粒，因此设计师精心设计的大量漂亮字体在电脑屏幕上几乎全都不好用，需要做大量优化、微调的工作，才能显示**“清晰易辨”**的中文字体。
    - 在宋体点阵字体横行的Win 95－XP时代，电脑屏幕显示的是Simsun宋体的位图点阵部分。在微软雅黑时代，虽然显示的是矢量部分，但是细心的人会发现它跟宋体点阵字一样，很多笔画复杂的汉字变成了“错字”——比如“着”“置”“幕”“需”“事”“剪”“属”“亮”“真”等等——这都是字体优化、微调的结果，这样做的目的是为了使汉字在中分屏上显示的更**清晰易认**。虽然感觉上有错字的嫌疑，但起码能让人感觉**美观清晰**，而不是模糊一团。在字体模糊一团和少量的“错字感”之间，成熟的Windows界面设计师果断的选择了后者。我们的体验也告诉我们，这样做真的很好。
  - WAIT 中文字体市场混乱
    collapsed:: true
    - 说实话中文字体界实在是太乱了, 在使用过 [Google Fonts](https://fonts.google.com) 之后一直想找替代的网站, 简中 SEO 较高的总是指向诸如 xxx下载站, pc下载站, 第一字体网 之类的质量较低下(缺乏**字体介绍**, **使用许可**, **作者详情**, **官方网站**等) 的网站, 这种资源德不配位真的让我有点受不了. 简中的铜臭气也渗透了出来.
      
      我们总是不把版权问题摆在前面, 总是先入为主地 "拿来就用", 也不问有什么代价, 乐于做伸手党, 久而久之真的沦为了理所当然的事情. 因为每一片雪花都很小, 所以雪崩不怪任何人, 甚至伸手党们拉帮结伙开始反攻作者, 真的让人啼笑皆非.
      2020
  - WAIT 用什么字体?
    collapsed:: true
    - 我将浏览器默认字体换成 LXGW 之后, 发现有很多网站混杂了相当多的字体, 当然阅读体验被毁得一团乱, 但是, 我发现绝大多数 网站都有在使用 Arial 这个字体, 尤其是在国外, 频率非常高. 之后查了查资料, 关于这个字体和非衬线字体有较大的争论, 尤其是人们在互相争论使用哪一个字体的时候. 
      collapsed:: true
      
      一个具体的研究表明在 12px 之下的阅读还是衬线字体比较好辨别, 但是随着字体大小的变化, 人对两者的阅读体验开始持平, 甚至可以说, 在字体大小非常大的时候, 两者的区别已经无所谓了.
      
      再者关于 阅读体验 是一个非常主观的东西, 目前这个东西还没有什么定论, 有的人面对美观的字体, 阅读速度反而可以升高, 但是有人则不然.
      - {{video https://www.youtube.com/watch?v=41i9EN9l8uc}}
    - 20221020
  - DOING 字体收集
    - id:: 6374947b-7716-4507-8561-f6c91e6d6fa4
      title:: [ryanoasis/nerd-fonts: Iconic font aggregator, collection, & patcher. 3,600+ icons, 50+ patched fonts: Hack, Source Code Pro, more. Glyph collections: Font Awesome, Material Design Icons, Octicons, & more](https://github.com/ryanoasis/nerd-fonts) ![](https://img.shields.io/github/stars/ryanoasis/nerd-fonts)
      mark:: "Nerd Fonts is a project that patches developer targeted fonts with a high number of glyphs (icons). Specifically to add a high number of extra glyphs from popular 'iconic fonts' such as Font Awesome, Devicons, Octicons, and others."
      tags:: #Github #opensource 
      mark::
      -
        - #+BEGIN_TIP
          MD > FA > CODI >...
          #+END_TIP
      - [[abbr]] Name Rule
        collapsed:: true
        - Nerd Font
          - Powerline Extra Symbols
          - Font Awesome
          - Font Awesome Extension
          - Material Design Icons
          - Weather Icons
          - Devicons
          - Octicons
          - Codicons
          - Font Logos (Formerly Font Linux)
          - Pomicons
          - IEC Power Symbols
          - Seti-UI + Custom
      - [Nerd Fonts: How and Why You Should Use Them - YouTube](https://www.youtube.com/watch?v=w9wqIEk5Cqo)
      - ==如果我的 General / Mono 字体没有打包 Nerd 字体, 怎么办?==
    - **英文字体**
      collapsed:: true
      - Press Start 2P: OFL, 位图字体, [Google](https://fonts.google.com/specimen/Press+Start+2P#standard-styles).
      - Lato Regular: OFL, [Google](https://fonts.google.com/specimen/Lato).
      - Roboto: AL, [Google](https://fonts.google.com/specimen/Roboto)
    - **中文兼容字体**
      collapsed:: true
      - 文泉驿的字体虽然是开放的，但似乎不可随便商用, 方正黑体、方正书宋、方正仿宋、方正楷体这四款方正的字体可以免费商用
      - 方正黑体
      - 方正楷体
      - 方正书宋
      - 方正仿宋
      - 思源黑体
      - 文泉驿字体
      - 华文黑体
      - Verdana: Microsoft Corporation, 需要购买
      - Yu Gothic UI: LM([License Microsoft fonts](https://www.fonts.com/content/microsoft-typography)), [MircoSoft](https://docs.microsoft.com/en-us/typography/font-list/yu-gothic).
    - **Mono/等宽字体**
      collapsed:: true
      - 挑选字体方面, 需留意对字体编码 Unicode 要优先考虑简中, 否则会出现字体变形的难受字样.
      - 版权方面, 微软雅黑是从Window上面提取的版本, 所以存在版权问题. 只可以个体使用, 不可用于商业环境; 更纱黑体由 兆邦中国(Zhaobang China) 在[微软商店免费下载](https://www.microsoft.com/zh-cn/p/%E6%9B%B4%E7%BA%B1%E9%BB%91%E4%BD%93/9mw0m424ncz7)使用.
      - [Microsoft Yahei Mono | 微软雅黑官方等宽字体 ](https://github.com/cheny-m/Microsoft-Yahei-Mono).
      - [Sarasa Gothic / 更纱黑体 / 更紗黑體](https://github.com/be5invis/Sarasa-Gothic).
      - [FiraCode | 符号连体](https://github.com/tonsky/FiraCode).
      - [Adobe Fonts-Source Code Pro | 全英文环境较好](https://github.com/adobe-fonts/source-code-pro).
  - Standards
    -
    -
    -
    -
  - [serif，sans-serif，monospace，cursive和**fantasy** | 黯羽轻扬](http://www.ayqy.net/blog/serif%EF%BC%8Csans-serif%EF%BC%8Cmonospace%EF%BC%8Ccursive%E5%92%8Cfantasy/)
  -
  -
  -
-
-
-
- [^linux]: via: [一条命令搞定Linux字体渲染——Ubuntu系发行版微软雅黑+宋体终极解决方案 | Linux区](https://linux.zone/278)
- [^Collection]: via: [「免版权字体」收集网站，已收藏了 45 款免费商用字体 - V2EX](https://v2ex.com/t/627989#; )
- [The Type — 文字 / 设计 / 文化 » Basics: 衬线](https://www.thetype.com/2010/01/1814/)
- [Opera's Fonts Problem: An Walkthrough](https://jedi.org/opera/FontTest/)