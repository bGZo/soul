icon:: 🛠
created:: [[20221219]]
document:: https://github.com/mastodon/mastodon
status:: tool/star
tags:: #[[social-media]]
type:: tool

- ## Why
  -
- ## How
  - DONE MOVE OUT
    collapsed:: true
    - View HTML
      collapsed:: true
      - [slashyn/mastodon-archive-viewer-modified: python script to take a mastodon archive and convert it into a human-readable webpage for viewing](https://github.com/slashyn/mastodon-archive-viewer-modified)
    - [在长毛象跨实例搬家 — 灰色闪电⚡](https://writee.org/hui-se-shan-dian/zai-chang-mao-xiang-kua-shi-li-ban-jia)
  - DONE How to donate to mastodon？#donation/patreon
    collapsed:: true
    - [About - Mastodon](https://mastodon.social/about)
    - [Mastodon | Creating Mastodon | Patreon](https://www.patreon.com/mastodon)
    - [如何使用Patreon给外国创作者打钱？ - 哔哩哔哩](https://www.bilibili.com/read/cv3684028)
    - DONE [捐助O3O – O3O](https://o3o.foundation/donate/) #donation
  - WAITING Mastodon content still available when the source is closed. Does could I know which instance is the backup from?
    collapsed:: true
    - `@cyberbot@saibo.world`
    - [What Happens If My Mastodon Server Shuts Down? - All Things How](https://allthings.how/what-happens-if-my-mastodon-server-shuts-down/)
    - [Content I deleted in one instance is still showing up in others, years after the fact : Mastodon](https://www.reddit.com/r/Mastodon/comments/10mta5v/content_i_deleted_in_one_instance_is_still/)
  - WAITING CSS 不同语言切换不同字体的用法
    collapsed:: true
    - ```css
      <div class="status__content__text status__content__text--visible translate" lang="ja"><p>xxxx</p></div>
      ```
    - In source via: [mastodon/variables.scss at main · mastodon/mastodon · GitHub](https://github.com/mastodon/mastodon/blob/main/app/javascript/styles/mastodon/variables.scss)
      - ```css
        // Language codes that uses CJK fonts
        $cjk-langs: ja, ko, zh-CN, zh-HK, zh-TW;
        ```
  - 马斯克收购后转移到Mastodon的人更多了。这里有一些搜索/查找Mastodon的方法，如果您正在寻找想要的主题的话：
    https://search.noc.social
    https://fediverse.space
    https://mastodon.fediverse.observer/list
    https://the-federation.info/mastodon
    #tools
- ## What
  -
- ## Namespace
  - {{namespace mastodon}}
- ## ↩ Reference
  - ### [[shortcut]]
    collapsed:: true
    - |---|---|
      | p | Open author's profile |
      | m | Mention author |
      | s | Focus search bar |
      | ? | Display this legend |
      via: [Mastodon](https://mastodon.social/keyboard-shortcuts)
  - ### [[api]]
    collapsed:: true
    - `m.cmx.im`
      collapsed:: true
      - Contents
        - `api/v1/statuses/{post_id}`
      - Comments
        - `api/v1/statuses/{post_id}/context`
  -