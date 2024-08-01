icon:: 📄
created:: [[20240730]]
description:: HTML, HyperText Markup Language, 网页文档的标准标记语言, 但是 HTML 把不同类型的元素，如 描述性元素 color、i 等 和 结构性元素 div、table 等，以及元素属性放在一起，为以后的维护和管理埋下隐患
tags:: #web #domain-specific
type:: lang/programming

- ## Why
  -
- ## How
  -
- ## What
  -
- ## Namespace
  - {{namespace html}}
- ## ↩ Reference
  -
-
- Elements
  description:: everything from the start tag to the end tag
  collapsed:: true
  - | Start tag | Element content | End tag |
    | <h1> | My First Heading | </h1> |
    | <p> | My first paragraph. | </p> |
    | <br> | *none* | *none* |
  - Nested HTML Elements | 可嵌套
  - Never Skip the End Tag | 须闭合
  - Empty HTML Elements | 内容可为空
  - HTML is Not Case Sensitive | 大小写不敏感
  - HTML Tag Reference
    - ==Not supported in HTML5== (12) #[[deprecated]]
      collapsed:: true
      - ~~`<frame> <frameset> <noframes>`~~
      - ~~`<acronym>`~~
        collapsed:: true
        - Use `<abbr>` instead.
      - ~~`<applet>`~~
        collapsed:: true
        - Use `<embed>` or `<object>` instead
      - ~~`<basefont>`~~
        collapsed:: true
        - Use CSS instead.
      - ~~`<big>`~~
        collapsed:: true
        - Use CSS instead.
      - ~~`<center>`~~
        collapsed:: true
        - Use CSS instead.
      - ~~`<dir>`~~
        collapsed:: true
        - Use `<ul>` instead.
      - ~~`<font>`~~
        collapsed:: true
        - Use CSS instead.
      - ~~`<tt>`~~
        collapsed:: true
        - Use CSS instead.
      - ~~`<strike>`~~
        collapsed:: true
        - Use `<del>` or `<s>` instead.
      - more via: [HTML Reference](https://www.w3schools.com/tags/default.asp)
    - 🎉 New supported in HTML5 (30)
      collapsed:: true
      - `<article>`
      - `<aside>`
      - `<audio>`
      - `<canvas>`
      - `<command>`
      - `<datalist>`
      - `<details>`
      - `<dialog>`
      - `<embed>`
      - `<figcaption>`
      - `<figure>`
      - `<footer>`
      - `<header>`
      - `<keygen>`
      - `<mark>`
      - `<meter>`
      - `<nav>`
      - `<output>`
      - `<progress>`
      - `<rp>`
      - `<rt>`
      - `<ruby>`
      - `<section>`
      - `<source>`
      - `<source>`
      - `<time>`
      - `<template>`
      - `<track>`
      - `<video>`
      - `<wbr>`
      - more via: [HTML 标签列表(字母排序) | 菜鸟教程](https://www.runoob.com/tags/html-reference.html)
-
- Entities
  description:: Reserved characters(保留字符) in HTML must be replaced with character entities(字符实体).
  - | Result | Description | Entity Name | Entity Number |
    |  | non-breaking space | &nbsp; | &\#160; |
    | < | less than | &lt; | &\#60; |
    | > | greater than | &gt; | &\#62; |
    | & | ampersand | &amp; | &\#38; |
    | " | double quotation mark | &quot; | &\#34; |
    | ' | single quotation mark (apostrophe) | &apos; | &\#39; |
    | ¢ | cent | &cent; | &\#162; |
    | £ | pound | &pound; | &\#163; |
    | ¥ | yen | &yen; | &\#165; |
    | € | euro | &euro; | &\#8364; |
    | © | copyright | &copy; | &\#169; |
    | ® | registered trademark | &reg; | &\#174; | |
- Layout
  collapsed:: true
  - **块(block)状元素**
    description:: "在网页设计中，块状元素主要用来定义页面结构、布局网页、构建网页基本框架和结构。块状元素能够嵌套其他块状、行内等不同类型的元素，因此，它们主要负责网页结构的支撑和构建。HTML 4"
    collapsed:: true
    - html、body、frameset、frame、noframes、iframe：网页、框架基本结构块
    - form、fieldset、legend：表单结构块
    - div：布局结构块
    - p：段落结构块
    - h1、h2、h3、h4、h5、h6：标题结构块。
    - ol、ul、dl、dt、dd、menu、dir：列表结构块
    - col、colgroup：表格列结构块
    - center：居中结构块。虽然可以参与网页布局，但是可以使用 CSS 代替其功能，所以不建议选用元素
    - pre：预定义结构块
    - address：引用结构块
    - blockquote：特定信息结构块
      collapsed:: true
      - pre、address 和 blockquote 主要用于网页内容排版
    - hr：结构装饰线
    - isindex：交互提示框
    - title：网页标题框
    - 表格系列类型元素
      collapsed:: true
      - table：表格框显示
      - tr：表格行显示
      - td：单元格显示
      - th：表格标题显示
      - tbody：表格行组显示
      - tfoot：表格脚注组显示
      - thead：表格标题组显示
      - border：表格边框
      - cellpadding:内边框
      - cellspacing：外边框
      - width:像素百分比（最好是通过css来设置长宽）
      - rowspan：单元格竖跨多少
      - colspan：单元格横跨多少列
      - ---
      - hr、isindex 和 title 块状元素有点特殊，它们不直接参与到网页结构构建中
    - **性质**
      collapsed:: true
      - 默认宽度都是 100%，即块状元素会挤满一行显示
      - 末尾都会隐藏一个换行符，看不见,但有效果，也就是说，块状元素后面不能够再跟着显示其他行内元素或者块状元素
      - 列表显示列表也属于块状元素，但是它拥有项目符号等一些其他特性。借助 CSS 可以为元素定义更多的显示效果，这里不再深入介绍，感兴趣的读者可以参阅 CSS 部分章节内容
      - 总是在新行上开始
      - 高度，行高以及外边框和内边距都可控制
      - 宽度缺省是它的容器的100%，除非设定一个宽度
      - 它可以容纳内联元素和其他块元素
    - 内联标签
  - **行内元素 / 内联标签**
    description:: "定义特定语义信息**。行内元素是不能用来进行网页结构构建的，虽然这样操作不会影响页面的解析效果，但是它不符合 HTML 结构嵌套规范，不建议使用。同时，也不建议在行内元素中包含其他块状元素，这样会严重破坏结构的逻辑关系。 HTML4"
    collapsed:: true
    - span：行内包含框。
    - a、area：超链接和映射包含框。
      collapsed:: true
      - 有 4 个保留的目标名称用作特殊的文档重定向操作：
        collapsed:: true
        - target的属性–>_blank：浏览器总在一个新打开、未命名的窗口中载入目标_
        - target的属性–>_parent：这个目标使得文档载入父窗口或者包含来超链接引用的框架的框架集。如果这个引用是在窗口或者在顶级框架中，那么它与目标 _self 等效。
        - target的属性–>_self：这个目标的值对所有没有指定目标的 标签是默认目标，它使得目标文档载入并显示在相同的框架或者窗口中作为源文档。这个目标是多余且不必要的，除非和文档标题  标签中的 target 属性一起使用。
        - target的属性–>_top：这个目标使得文档载入包含这个超链接的窗口，用 _top 目标将会清除所有被包含的框架并将文档载入整个浏览器窗口。--><!--标签的 target 属性规定在何处打开链接文档。
    - img：图像包含框你插入图片 在img标签里面只设置宽，不设置高，图片就会等比例缩放。
      collapsed:: true
      - src：要显示图片的路径
      - alt：图片没有加载成功时的提示
      - title：鼠标悬浮时的提示信息
      - width：图片的宽
      - height：图片的高（宽高两个属性只用一个会自动等比缩放）
    - abbr、acronym、b、bdo、big、cite、code、del、dfn、em、font、i、ins、kbd、q、s、samp、small、strike、strong、sub、sup、tt、u、var：格式化信息包含框。
    - button、select、textarea、label：表单对象包含框。
    - applet、object：可执行的插件或对象包含框。 caption：表格标题包含框。
    - noscript：无脚本包含框。在行内元素中，使用最频繁的是 span 元素，该元素常用来作为修饰行内文本或对象的样式。
    - 行内块状元素
      collapsed:: true
      - input：输入框
      - optgroup：下拉项分组
      - option：下拉项
      - 列表项元素 li：列表项
      - 结构内隐藏元素 map：图像映射包含框
      - param：参数
      - br：换行
    - 性质:
      collapsed:: true
      - 行内显示 显示没有块状显示的轮廓，因此可以形象地把它联想为一个皮纸袋子。如果为行内元素描一个边，有时显示的是不规则的。同时，行内元素正如它的名字所说的那样，多个行内元素并列显示在同一行内。
      - 行内元素没有高度和宽度，即使为它定义高度，但是浏览器在解析时也不会显示
      - 行内元素的呈现效果与块状元素存在很大区别，这不仅仅体现在宽和高方面，它们可以并列显示，随行移动。
      - 和其他元素都在一行上
      - 高，行高以及外边距和内边距不可改变
      - 宽度就是它的文字或图片的宽度，不可改变
      - 内联元素只能容纳文本或者其他内联元素
    - 对行内元素注意如下：
      collapsed:: true
      - 设置宽度width无效，
      - 设置高度height无效，可以通过line-height设置
      - 设置margin只有左右margin无效，上下无效。
      - 特殊字符：`<>"©®　　<>"©®　　`对应的字符
    - 行内块状显示: 默认状态下，元素不会显示该状态，需要使用 CSS 声明。
    - 格显示表格也是一种块状元素，但是它还具有一些其他特性，如更严格的组织性，表格元素之间的严密协调性等。表格显示还包括表格、行、单元格、标题、列、组等不同的显示性质和效果。
  - **其他元素**
    collapsed:: true
    - 头部区域隐藏元素 head：头部包含框。 base：URL 基础。
    - basefont：默认基础字体属性。
    - link：链接。
      collapsed:: true
      - ```html
        <link rel="icon" href="https://common.cnblogs.com/favicon.ico">#做网页上面的小图标
        ```
    - **meta**(元信息)
      collapsed:: true
      - name属性主要用于描述网页，与之对应的属性是content，content中的内容，主要便于搜索引擎机器人查找信息和分类信息用的 。
      - http-equiv(=http的文件头): 它可以向浏览器传回一些有用的信息，以帮助正确和精确的显示网页内容，与之对应的属性为content，content中的内容其实就是各个参数的变量值。
            ```html
            <meta htt p-equiv="Refresh" content="2"> #每隔2秒刷新界面
            ```
      - [Viewport](https://www.w3schools.com/css/css_rwd_viewport.asp): take control over the viewport
      - collapsed:: true
        ```html
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        ```
        - The `width=device-width` part sets the width of the page to follow the screen-width of the device (which will vary depending on the device). 即调整页面宽度
        - The `initial-scale=1.0` part sets the initial zoom level when the page is first loaded by the browser. 即调整缩放比例.
    - script：脚本。
    - style：样式。
-
- Forms
  - HTML Forms
  - HTML Form Attributes
  - HTML Form Elements
  - HTML Input Types
  - HTML Input Attributes
  - HTML Input Form Attributes
  - **表单标签`<form>`:（29种）**
    - 表单用于向服务器传输数据，比如文本字段、复选框、单选框、提交按钮等等。HTML表单用于接收不同类型的用户输入，用户提交表单时向服务器传输数据，从而实现用户与web服务器的交互。表单标签，要提交的所有内容都应该在该标签中。
    - `<form>`
    - `<input>`（自动断掉）
      collapsed:: true
      - **name**：表单提交项的键，注意和id的区别；name属性是和服务器通信时使用的名称，而id属性是浏览器端使用的名称，该属性主要是为了方便客户端编程。
      - Type
        collapsed:: true
        - text
          collapsed:: true
          - 1. size：拓宽单行文本
          - 2. value：显式占位，表单提交项的值 , 对于不同的输入类型，value属性的用法也不同
          - 3. placeholder：隐式占位
          - 4. maxlength：最大长度
          - 5. readonly：文本属性
        - password：密码
        - textarea：多行文本框
          collapsed:: true
          - 1. rows
          - 2. cols
        - collapsed:: true
          4. submit:
          - collapsed:: true
            1. method：表单的提交方式post、get默认取值就是get（信封）
            - 1. get：1、提交的键值对，放在地址栏中url后面。2、安全性相对较差。3、对提交的内容的长度有限制
            - 2. post：1、提交的键值对不在地址栏。2、安全性相对较差。3、对提交内容的长度理论上无限制。
          - 2. action：表单提交到哪，一般指向服务器端一个程序，程序接收到表单提交过来的数据（即表单元素值）作相应处理.
        - button:
          collapsed:: true
          - Button > input button > input submit
        - range
        - file
          collapsed:: true
          - 1. multiple：一次允许上传多个文件
          - 2. required：一次只可以上传一个文件
      - Name
      - textarea
      - select
      - fieldset
      - label
- `iframe`
  collapsed:: true
  - Defines an inline frame
- `<video>`
  collapsed:: true
  - src
  - height
  - width
  - autoplay
  - preload
  - controls
  - loop
  - poster
  - muted
- **嵌入图片和创建分区式响应**
  collapsed:: true
  - `map`：响应图的关键元素
  - `area`：图片可被点击的元素
    collapsed:: true
    - 指定URL：href  和  Alt
    - shape和coords 属性，共同起作用
      collapsed:: true
      - shape值：
        collapsed:: true
        - rect：四个逗号相隔的左上右下的四个区域
        - circle：三个逗号相隔的左右边缘到圆心的距离和圆的半径
        - poly：多边形，至少六个逗号，代表一个顶点（6个数值，实际是三个坐标，完成之后是一个三角形）
        - dafault：代表默认区域，也就是说覆盖整个图片。不需要coords值。
-
-
- Tracks
  - 唤起QQ
    collapsed:: true
    - 加QQ群的话在QQ客户端就可以申请到链接，操作即可，或者在[这里](https://qun.qq.com/join.html)找到
    - ```html
      <body>
        <h1>jsdafjk</h1>
        <a href="http://wpa.qq.com/msgrd?v=3&uin=1551728654&site=qq&menu=yes">1551728654</a>
        <br/>
        <a href="tencent://AddContact/?fromId=50&fromSubId=1&subcmd=all&uin=1551728654">1551728654</a>
      </body>
      ```
  - 跳转邮箱
    collapsed:: true
    - ```html
      <a href="mailto:lfh010618@gmail.com">lfh010618@gmail.com</a>
      ```
-
- More
  - [多年前对 XHTML 和 HTML5 的预测为什么错的这么离谱？](https://www.zhihu.com/question/21452659/answer/18272397)
    collapsed:: true
    - > 那个时候正是W3C自信心爆棚的时候，整个业界都认为W3C联盟战胜了IE，IE受到越来越多浏览器的挑战，如Chrome、Firefox、Webkit，终于，内容提供商开始倾向于提供非IE兼容的内容，IE浏览器的绝对市场垄断地位被打破了。人们都以为这是民众的胜利，标准的胜利，W3C的胜利。同时，XML的成功也冲昏了W3C HTML工作小组的头脑，越来越多的协议选择XML作为底层接口。让我们全部都使用XML吧，W3C就这么愉快的决定了。但很显然的，W3C真是图样图森破。标准，永远是掌握在浏览器厂家手里的。事实上，IE的市场份额只是被WebKit核心蚕食了而已。市场标准只是从一个寡头手里到了另一个寡头手里。一意孤行的XHTML 2.0竟然大胆的与原先的HTML不再兼容，浏览器厂商终于怒了，Mozilla和苹果牵头，WHATWG小组成立。失去了厂商支持的W3C的XHTML2标准很快就成为了一个笑话。
  - [如何高效自学CSS？](https://www.zhihu.com/question/23547858/answer/163014761)
    collapsed:: true
    - > 初期不要急着自己去设计页面，直接仿站来让自己获得从0到1的能力。
      > 我个人应该主要是通过模仿WordPress模板入的门。当然找的都是一些比较有新意的，结构上稍有复杂度的，基本没切过有高相似度的页面，时间要花在刀刃上。当时国外应该有大量应用了css3动画以及响应式设计等较新技术的页面（2011年），也确实培养起了自己对CSS的兴趣。找份真实的工作来巩固深入学习。
      > 相信我，放低姿态去找份真实的开发工作，比你自己业余去摸索要高效10倍。我个人毕业后进入网易，经过公司的内部系统培训，理解了CSS模块化的思想，才发现**自己以前只能算是完成了一个页面，而不算是做好了它**。真实的产品开发才是自己的CSS能力真正落地的开始。工作后应继续关注相关一些例如Codrops 等这类能带来CSS使用灵感的网站，**去思考为什么，而不是copy它的代码去完成功能**。页面开发中有太多重复的工作，如果你一直用一个思路去解决问题，会有碍于经验和能力的积累，形成一个较低级舒适区的怪圈。平时也可以去codepen这类网站收集一些琐碎的灵感，增加知识面学习css过程中千万不要剥离HTML学习。
      > 当你什么时候理解了html的重要性（**从页面开发角度而言，它可以视为是后续良好css和js编码得以实施的基础，相当于程序中的数据结构，设计好了可以让你事半功倍**），你才可以称得上是一个合格的页面开发对于新人，我建议**除了几个关键概念，如布局、盒模型、单位等等，都不应该花大量去扣细节，甚至背书记忆，浏览性学习知道有这个东西就行，在实际应用时再去加深记忆**。算抛砖引玉吧，好久没有机会好好写写CSS了。虽然我一直认为纯粹的CSS页面开发并不适合作为前端领域里深入发展的方向，但不可否认，在学习玩耍css的过程中，带给了自己很多乐趣。
  - [HTML4，HTML5，XHTML 之间有什么区别？](https://www.zhihu.com/question/19818208/answer/13430829)
    collapsed:: true
    - > 我来从HTML的历史谈谈他们3者的区别。
      >
      > 在HTML的早期发展中，W3C成立之前，很多标准的制定都是在浏览器的开发者们互相讨论的情况下完成的，比如HTML 2.0, 3.2直到4.0, 4.01，这些标准大部分都是所谓的retro-spec，即先有实现后有标准。在这种情况下，HTML标准不是很规范，浏览器也对HTML页面中的错误相当宽容。这反过来又导致了HTML作者写出了大量的含有错误的HTML页面。据说，时至今日web上99%的页面都含有HTML错误。W3C随后意识到了这个问题，并认为这是互联网的一个基础性问题，应该加以解决。
      >
      > 为了规范HTML，W3C结合XML制定了XHTML 1.0标准，这个标准没有增加任何新的tag，只是按照XML的要求来规范HTML，并定义了一个新的MIME type，application/xhtml+xml。W3C的初衷是对这个MIME type浏览器要实行强错误检查，既如果页面有HTML错误，就要显示错误信息。
      >
      > 但是由于已有的web页面中已经有了大量的错误，很多开发者拒绝使用新的MIME type。W3C不得已，在XHTML 1.0的标准之后加了一个附录C，允许开发者使用XHTML语法来写页面，同时使用旧的MIME type，application/html，来分发页面。这个旧的MIME type不会触发浏览器的强错误检查。这就是我们今天看到的情况，很多网站宣称自己遵守XHTML 1.0标准，那只不过是说，他的页面中用了XHTML语法，但并不能保证完全没有错误。
      >
      > 要验证XHTML有没有真正起效，需要查看web服务器使用哪种MIME type来分发页面的。
      >
      > W3C随后在XHTML 1.1中取消了附录C，即使用XHTML 1.1标准的页面必须用新的MIME type来分发。于是这个标准并没有很多人采用。这种情况同样发生在尚未完成的XHTML 2.0身上，它要求强错误检查，于是没有人采用。XHTML的故事也告诉我们，有时候先有标准再来实现，是行不通的。有了XHTML的教训，WHAT Working Group和W3C在制定下一代HTML标准，也就是HTML5的时候，就将向后兼容作为了一个很重要的原则。HTML5确实引入了许多新的特性，但是它最重要的一个特性是，不会break已有的网页。你可以将任何已有的网页的第一行改成`<!DOCTYPE html>`，它就成也一个HTML5页面，并且可以照样在浏览器里正常的展示。
  - [为什么越来越多的网站域名不加「www」前缀？](https://www.zhihu.com/question/20414602/answer/1335418092)
    collapsed:: true
    - > 什么是www？
      >
      > 2010年以前开始使用电脑上网的人，都知道“www”的重要作用。要输入网址，首先得打出这三个字母来。这三个字母，就是英语的“World Wide Web”首字母的缩写形式，也就是万维网的意思。那个时候互联网不同的服务需要不同的工具来完成，主要服务有万维网（WWW）、文件传输（FTP）、电子邮件（E-mail）、远程登录（Telnet）等。说白了，那个时候的www（World Wide Web）是一个标识，这是一个需要你用浏览器来访问的网页服务，而不是需要你用telnet访问的bbs，或者ftp工具访问的文件传输服务。因此那个时候，网站主页的域名前面要用“www”。
      >
      > 所以与其说WWW是一种技术，倒不如说它是对信息的存储和获取进行组织的一种思维方式。
      >
      > ...
      >
      > 前文中提到互联网的初期，主要服务有万维网（WWW）、文件传输（FTP）、电子邮件（E-mail）、远程登录（Telnet）等，而能上网的都是大公司，电子邮件、文件、 FTP ，当然还有 HTTP，多种服务一样都不能少，一台服务器肯定是不行的。所以他们就把不同的任务交给不同的服务器去处理。为了区分，就用上了不同的子域名，也就是我们现在看到的 www.123.cn，ftp.123.cn，mail.123.cn 等等的子域名形式。而时代在发展，科技在进步，现在只需要把任务分布到多台服务器上就行了，不必非得用子域名来区分。比方说baidu，在 http://baidu.com 这个域名背后有无数的服务器支持着运行。现在继续用子域名，纯粹是为了给用户方便了。
  - [推荐的书籍](https://www.ituring.com.cn/article/509878)
    collapsed:: true
    - > 本文大致梳理了图灵在“成为前端工程师”之路上出版的重点好书，仅供大家参考。
      > 1. HTML与CSS
      > 2. JavaScript
      > 3. 网络协议&安全
      > 4. 迈向全端：Node.js
      > 5. 其他基础知识
      > HTML与CSS
    - 入门
      collapsed:: true
      - [HTML5与CSS3基础教程（第8版）](https://www.ituring.com.cn/book/1199)
      - [精通CSS：高级Web标准解决方案（第3版）](https://www.ituring.com.cn/book/1910)
    - 进阶
      collapsed:: true
      - [响应式Web设计：HTML5和CSS3实战（第2版）](https://www.ituring.com.cn/book/1817)
      - [深入解析CSS](https://www.ituring.com.cn/book/2583)
    - 高级
      collapsed:: true
      - [CSS揭秘](https://www.ituring.com.cn/book/1695)
    - JavaScript
      collapsed:: true
      - 入门
        collapsed:: true
        - [Head First JavaScript程序设计](https://www.ituring.com.cn/book/1556)
        - [JavaScript DOM编程艺术(第2版)](https://www.ituring.com.cn/book/42)
      - 进阶
        collapsed:: true
        - [JavaScript高级程序设计（第3版）](https://www.ituring.com.cn/book/946)
        - [深入理解JavaScript特性](https://www.ituring.com.cn/book/2452)
        - [JavaScript设计模式与开发实践](https://www.ituring.com.cn/book/1632)
      - 高级
        collapsed:: true
        - [你不知道的JavaScript（上卷）](https://www.ituring.com.cn/book/1488)
        - [你不知道的JavaScript （中卷）](https://www.ituring.com.cn/book/1563)
        - [你不知道的JavaScript （下卷）](https://www.ituring.com.cn/book/1666)
      - jQuery
        collapsed:: true
        - [jQuery基础教程（第4版）](https://www.ituring.com.cn/book/1169)
      - React
        collapsed:: true
        - [深入React技术栈](https://www.ituring.com.cn/book/1898)
      - Vue.js
        collapsed:: true
        - [深入浅出Vue.js](https://www.ituring.com.cn/book/2675)
    - 网络协议&安全
      collapsed:: true
      - [图解HTTP](https://www.ituring.com.cn/book/1229)
      - [HTTP权威指南](https://www.ituring.com.cn/book/844)
      - [HTTPS权威指南：在服务器和Web应用上部署SSL/TLS和PKI](https://www.ituring.com.cn/book/1734)
      - [Web安全开发指南](https://www.ituring.com.cn/book/1775)
      - [黑客攻防技术宝典 Web实战篇](https://www.ituring.com.cn/book/885)
    - 迈向全端：Node.js
      collapsed:: true
      - 入门
        collapsed:: true
        - [Node.js实战（第2版）](https://www.ituring.com.cn/book/1993)
      - 进阶
        collapsed:: true
        - [深入浅出Node.js](https://www.ituring.com.cn/book/1290)
    - 其他基础知识
      collapsed:: true
      - [Git小书](https://www.ituring.com.cn/book/1870)
      - [GitHub入门与实践](https://www.ituring.com.cn/book/1581)
      - [Linux Shell脚本攻略（第3版）](https://www.ituring.com.cn/book/2439)
      - [SQL基础教程（第2版）](https://www.ituring.com.cn/book/1880)
      - [网络是怎样连接的](https://www.ituring.com.cn/book/1758)
      - [我的第一本算法书](https://www.ituring.com.cn/book/2464)（日漫）
      - [算法图解：像小说一样有趣的算法入门书](https://www.ituring.com.cn/book/1864)（美漫）
-
- Refs
  id:: 62a33ccf-f2f1-4447-b314-cab0a2d14626
  - [W3schools.com](https://www.w3schools.com/)
  - [MDN Web 开发技术](https://developer.mozilla.org/zh-CN/docs/Web)
  - [MDN HTML](https://developer.mozilla.org/zh-CN/docs/Web/HTML)
  - [一份在 HTML 4 Strict 和 XHTML 1.0 Strict 下必须遵守的标签嵌套规则](http://www.cs.tut.fi/~jkorpela/html/strict.html)
  - [网页直接加QQ群/QQ好友](https://blog.csdn.net/qq_28975017/article/details/72898385) - coder丶赵
  - [想把文件直接放至服务器，通过http的url下载](https://blog.csdn.net/weixin_36586564/article/details/78774035?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)-严的博客
  - [提高网页打开速度的一些小技巧 [问题点数：100分]]( https://bbs.csdn.net/topics/230010297)
  - [不会再有 HTML6 了。 · Issue \#91 · chunpu/blog](https://github.com/chunpu/blog/issues/91)
-