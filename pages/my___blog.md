title:: my/blog
tags:: #blog #jekyll #vercel
mark:: [Home - bGZo's blog](http://blog.bgzo.cc)

- ## [[Issue]]
  - DONE Modify Font CSS (Solarized) in 20230128
    collapsed:: true
    - [chawyehsu/lxgw-wenkai-webfont: webfont package for the LXGW WenKai typeface](https://github.com/chawyehsu/lxgw-wenkai-webfont) #sucks #font/web
      collapsed:: true
      - 总耗时 2.1 min 😅
        
        ![firefox_103.png](../assets/firefox_103_1674914188465_0.png)
      - 对比 [Noto Serif Simplified Chinese - Google Fonts](https://fonts.google.com/noto/specimen/Noto+Serif+SC/about) 6s (当然也很慢)
        
        ![firefox_102.png](../assets/firefox_102_1674914603295_0.png)
      - 一开始从 [Chrome 版 WebFeed 简介](https://taoshu.in/webfeed/webfeed-for-chrome.html) 发现的, 它网站的加载速度更慢...
      - 仓库维护四个版本的字体
        - `lxgw-wenkai-webfont`
        - `lxgw-wenkai-lite-webfont`
        - `lxgw-wenkai-tc-webfont`
        - `lxgw-wenkai-screen-webfont`
      - 测试用的是 Screen 版本, 总共 10 M, 对比原版需要 30M, 感觉只有 Build-in App 才会用, 但这不标榜 Webfont 吗? Build-in 我直接去哪原版了, 来这里做什么?
    - 作者应该是下了幸苦, 按一定分区大小进行划分, 每个包差不多50多K, 合在一起的 CSS 差不多 100 多K, 但是要全部包加载完才能渲染完, 2分钟内一直在下载状态就非常不能忍;
  - DONE ~~Add support for CN characters~~ in 20230131 #deprecated #regex
    collapsed:: true
    - 1 , 替换
      2 . 替换
      3 结尾空格替换
      4 脚注替换
      5 | 替换
      6 链接转义
  - DONE Add dark theme in 20230228
    collapsed:: true
    - [prefers-color-scheme - CSS: Cascading Style Sheets | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme)
  - DONE Add comment in 20230304
    collapsed:: true
    - DONE [utterance/utterances: A lightweight comments widget built on GitHub issues](https://github.com/utterance/utterances)
    - [giscus/giscus: A comment system powered by GitHub Discussions.](https://github.com/giscus/giscus)
    - [gitalk/gitalk: Gitalk is a modern comment component based on Github Issue and Preact.](https://github.com/gitalk/gitalk/)
      collapsed:: true
      - Official Demo
        collapsed:: true
        - https://github.com/gitalk/gitalk.github.io/blob/master/index.html
        - https://github.com/gitalk/gitalk/issues/1
      - No because not support name matching;
  - TODO Add help menu (Keyboard shortcuts), like
    collapsed:: true
    - https://player.fm with `?`
    - https://github.com with `?`
  - TODO Add telegram article preview
  - TODO Fix twitter card image preview
-
-
- blog 支持加载GitHub评论