alias:: browser/chromium, chrome
description:: uGc
icon:: 
source:: [Home](https://www.chromium.org/chromium-projects/); [ungoogled-software/ungoogled-chromium: Google Chromium, sans integration with Google](https://github.com/ungoogled-software/ungoogled-chromium) ![](https://img.shields.io/github/stars/ungoogled-software/ungoogled-chromium)

  - Gc with [Hibbiki/chromium-win64: Chromium builds for Windows x64](https://github.com/Hibbiki/chromium-win64) ![](https://img.shields.io/github/stars/Hibbiki/chromium-win64)
- [[Backup]]
  collapsed:: true
  - `User Data/Default`
    - Cache 大头
      - `Service Worker\CacheStorage`
      - `Cache`
      - `Code Cache`
      - `IndexedDB`
      - ...
    - `History`
    - `Bookmarks`
- [[issue]]
  - Web notification cannot use (+Brave) #[[wontfix]]
    collapsed:: true
    - **Google Cloud Message / Firebase Cloud Messaging** 无法在 ungoogle 的浏览器使用...
    - [Notification Examples - Base Site](https://web-push-book.gauntface.com/demos/notification-examples/) #testing #develop
    - more via
      collapsed:: true
      - [Facebook Push notification not working · Issue #589 · ungoogled-software/ungoogled-chromium](https://github.com/ungoogled-software/ungoogled-chromium/issues/589)
        collapsed:: true
        - collapsed:: true
          > Push Notifications used GCM service for client notification.For example user get unique ID for future notifications. In chrome/browser/push_messaging is located Push notifications implementation. Impossible to have client Push API notification without cloud services by Google (or Mozilla in case of Firefox browser).
          By the way, currently they migrate to FCM.
      - [Implement Push API using Mozilla's servers · Issue #1020 · ungoogled-software/ungoogled-chromium](https://github.com/ungoogled-software/ungoogled-chromium/issues/1020)
        collapsed:: true
        - > Rather than use Mozilla servers, [roll your own](https://github.com/mozilla-services/autopush). I don't know if anyone has audited the source for connections to other Mozilla services.
  - Chrome Extensions 无法使用
    collapsed:: true
    - 1. `chrome://flags/#extension-mime-request-handling` -> **Always prompt for ins**
    - 2. Download Crx [NeverDecaf/chromium-web-store: Allows adding extensions from chrome web store on ungoogled-chromium. Also adds semi-automatic extension updating.](https://github.com/NeverDecaf/chromium-web-store) ![](https://img.shields.io/github/stars/NeverDecaf/chromium-web-store)
    - via: [How to Manually Install Extensions (Ungoogled Chromium) | avoidthehack!](https://avoidthehack.com/manually-install-extensions-ungoogled-chromium)
  - New Tab
    collapsed:: true
    - `chrome://flags/#custom-ntp`
    - `chrome://new-tab-page`
    - `chrome://newtab`
    - more via
      collapsed:: true
      - [Can't customize new tab · Issue #153 · ungoogled-software/ungoogled-chromium-archlinux](https://github.com/ungoogled-software/ungoogled-chromium-archlinux/issues/153)
      - [Add flag for setting a custom new tab page by Ahrotahn · Pull Request #1686 · ungoogled-software/ungoogled-chromium](https://github.com/ungoogled-software/ungoogled-chromium/pull/1686)
    - RSS Start Page #project
      collapsed:: true
      - Extension show rss feed recently like Brave
      - [deepjyoti30/startpage: A minimal starpage for Chrome and Firefox](https://github.com/deepjyoti30/startpage) #shoulders-of-giants
        id:: d624bf81-db0f-49bd-b6d4-b5cac2c990f7
        collapsed:: true
      - [Manganum: #1 New Tab for Chrome™ - Chrome Web Store](https://chrome.google.com/webstore/detail/manganum-1-new-tab-for-ch/jbfeongihppeenfnaofmdeikahaefljd?hl=en-US)
  - Google translate web always CPU high usage
    collapsed:: true
    - 拉到底一次性翻译完就不会持续占用 CPU 了
  - Playback of protected content is not enabled #spotify
    collapsed:: true
    - [spotify doesn't work · Issue #1849 · ungoogled-software/ungoogled-chromium](https://github.com/ungoogled-software/ungoogled-chromium/issues/1849)
  - Cookies always
    collapsed:: true
    - My cookies
      collapsed:: true
      ```html
      [*.]leetcode.cn
      [*.]bilibili.com
      [*.]discord.com
      [*.]duolingo.com
      [*.]github.com
      [*.]gmgard.com
      [*.]google.com
      [*.]inoreader.com
      [*.]leetcode.com
      [*.]live.com
      [*.]logseq.com
      [*.]nowcoder.com
      [*.]openai.com
      [*.]spotify.com
      [*.]steampowered.com
      [*.]v2ex.com
      [*.]youtube.com
      [*.]player.fm
      [*.]steamdb.info
      [*.]raindrop.io
      [*.]gmgard.moe
      [*.]anki.net
      [*.]pixiv.net
      [*.]south-plus.net
      [*.]mastodon.social
      [*.]zodgame.xyz
      ```
    - Keep going
      collapsed:: true
      - Never Social Media
        ```
        [*.]twitter.com
        [*.]mastodon.social
        [*.]bgm.tv
        ```
      - Garbage
        ```
        [*.]jp
        [*.]csdn.net
        [*.]weibo.com
        [*.]zhihu.com
        [*.]youdao.com
        [*.]toutiao.com
        [*.]qq.com
        [*.]douban.com
        [*.]baidu.com
        [*.]aliyundrive.com
        [*.]alipay.com
        [*.]51cto.com
        [*.]163.com
        [*.]sina.com.cn
        ```
  - [3 月 15 日谷歌就要停止第三方 chrome 浏览器的同步功能了，我该怎么办？ - V2EX](https://www.v2ex.com/t/761099)