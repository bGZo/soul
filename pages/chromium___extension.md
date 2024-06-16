title:: chromium/extension

- [[develop]]
- [[issue]]
  - Version Choose
    - [Will my organization's Chrome extensions with manifest v2 run after Jan 2023? - Chrome Enterprise Community](https://support.google.com/chrome/a/thread/175260822/will-my-organization-s-chrome-extensions-with-manifest-v2-run-after-jan-2023?hl=en)
    - [巨坑：chrome extensions绝对不要升级到V3 - 掘金](https://juejin.cn/post/7094545901967900686)
    - ((d624bf81-db0f-49bd-b6d4-b5cac2c990f7))
      - ==这个拓展的配置文件不会刷新, 因为他的配置没有写在 Manifest 里面, 默认他是需要在页面内进行配置的, 也很合理==