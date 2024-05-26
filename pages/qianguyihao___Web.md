title:: qianguyihao/Web
tags:: #Github #opensource
created:: 20220628
- ## [qianguyihao/Web: 千古前端图文教程，超详细的前端入门到进阶知识库。从零开始学前端，做一名精致优雅的前端工程师。 (github.com)](https://github.com/qianguyihao/Web) ![](https://img.shields.io/github/stars/qianguyihao/Web)
  - 前端工具
    - 01-VS Code的使用
    - 02-Git的使用
    - 03-网络抓包和代理工具：Whistle
      - [GitHub - avwo/whistle: HTTP, HTTP2, HTTPS, Websocket debugging proxy](https://github.com/avwo/whistle) ![](https://img.shields.io/github/stars/avwo/whistle)
    - 04-解决 Git 不区分大小写导致的文件冲突问题
      - ```shell
        # 将本地的 test、Test 目录都删掉，并生成一个新的目录 Temp
        git mv Test Temp
        # 将 Temp 目录改成 Test 目录。此时，项目中只会存在 Test 目录，不会存在 test 目录。目标达成。
        git mv Temp Test
        ```
      - WAITING 我不理解的是，为什么远端的 test 也会在第一个命令执行之后消失？
    - Atom在前端的使用
    - Emmet in VS Code
    - GitHub的使用
    - Mac安装和配置iTerm2
    - Sublime Text在前端中的使用
    - VS Code的使用积累
    - WebStorm的使用
    - chrome浏览器
    - iconMoon
  - HTML
    - 01-认识Web和Web标准
      - Web 标准
        - 结构
        - 表现
        - 行为
    - 02-浏览器的介绍
      - High level structure #.ol
        - User Interface（UI界面）
          collapsed:: true
          - 包括地址栏、前进/后退按钮、书签菜单等。也就是浏览器主窗口之外的其他部分。
        - Browser engine （浏览器引擎）
        - Rendering engine（渲染引擎/浏览器内核）
          - 作用：解析网页 HTML 与 CSS 代码，计算网页的格式、显示方式，并显示在页面上
          - 常见：
            - | 浏览器 | 内核 |
              | ---- | ---- | ---- |
              | chrome | Blink |
              | Safari | Webkit |
              | Firefox 火狐 | Gecko |
              | IE | Trident |
        - Networking （网络模块）
          - 用于发送网络请求。
        - JavaScript Interpreter（JavaScript解析器）
          - 作用：解析网页 JS 代码，对其处理后再运行
            - JS 引擎逐行解释每一句源码（转换为机器语言），然后由计算机去执行
          - 常见：
            - | 浏览器 | JS 引擎 |
              | ---- | ---- | ---- |
              | chrome [:br]欧鹏 | V8 |
              | Safari | Nitro |
              | Firefox [:br]火狐 | SpiderMonkey（1.0-3.0）/ TraceMonkey（3.5-3.6）/ [:br]JaegerMonkey（4.0-） |
              | Opera | Linear A（4.0-6.1）/ Linear B（7.0-9.2）[:br] Futhark（9.5-10.2）/ Carakan（10.5-） |
              | IE | Trident |
        - UI Backend（UI后端）
          - 用于绘制组合框、弹窗等窗口小组件。它会调用操作系统的UI方法。
        - Data Persistence（数据存储模块）
          - 比如数据存储 cookie、HTML5中的localStorage、sessionStorage。
        - ![🖼 https://www.html5rocks.com/en/tutorials/internals/howbrowserswork ](../assets/2023/PgPX6ZMyKSwF6kB8zIhB.webp)
    - 03-初识HTML
    - 04-HTML标签：排版标签
    - 05-HTML标签：字体标签和超链接
    - 06-HTML标签：图片标签
    - 07-html标签图文详解（二）
    - 08-HTML5详解
    - 09-HTML5举例：简单的视频播放器
    - 10-HTML5详解（二）
    - 11-HTML5详解（三）
    - 12-HTML基础回顾
  - CSS基础
  - CSS进阶
  - JavaScript基础
  - JavaScript基础：ES6语法
  - JavaScript基础：异步编程
  - JavaScript进阶
  - 前端基本功：CSS和DOM练习
  - 移动Web开发
  - MySQL数据库
  - Node.js
  - Vue基础
  - React基础
  - 前端性能优化
  - 前端工程化
  - 前端综合
  - 17-资源推荐