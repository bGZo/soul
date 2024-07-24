also:: 浏览器
tags:: #tool

- ## [[issue]]
  - **浏览器内置通知**
    via: [Is there any way to view Chrome browser notifications history? - Super User](https://superuser.com/questions/1035042/is-there-any-way-to-view-chrome-browser-notifications-history)
    - Windows 无法转换为 Native Notifications
    - 需要去 `User Data\Default\Platform Notifications` 看 log
    - [Notification Examples - Base Site](https://web-push-book.gauntface.com/demos/notification-examples/) #[[tool]]
- ## [[thought]]
  - Brave meaningless
    collapsed:: true
    - 除了设计得好一点, 没有一点用处, 在 Chromium 的基础上绑定了 Brave Coins 的全套插件, 然后打包释出, 可以说真正的技术点就仅仅是表面套壳的几个插件罢了, 对比 `User Data` 下产生的数据, 多出来的目录屈指可数
    - ```
      /mnt/c/Users/15517/Desktop/browser/diff > tree -L 3
      .
      ├── BraveWallet
      │   └── 1.0.20
      │       ├── README.md
      │       ├── chainlist.json
      │       ├── contract-map.json
      │       ├── evm-contract-map.json
      │       ├── images
      │       ├── manifest.fingerprint
      │       ├── manifest.json
      │       └── solana-contract-map.json
      ├── BrowserMetrics-spare.pma
      ├── Default
      │   ├── Google Profile.ico
      │   ├── Rewards.log
      │   ├── ads_service
      │   │   ├── client.json
      │   │   ├── confirmations.json
      │   │   ├── database.sqlite
      │   │   └── database.sqlite-journal
      │   └── publisher_info_db
      ├── Greaselion
      │   └── Temp
      ├── Module Info Cache
      ├── SODA
      ├── SODALanguagePacks
      │   └── en-US
      ├── Webstore Downloads
      ├── afalakplffnnnlkncjhbmahjfjhmlkal
      │   └── 1.0.216
      │       ├── 1
      │       ├── manifest.fingerprint
      │       └── manifest.json
      ├── aoojcmojmmcbpfgoecoadbdpnagfchel
      │   └── 1.0.7
      │       ├── manifest.fingerprint
      │       ├── manifest.json
      │       └── photo.json
      ├── cffkpbalmllkdoenhmdmpbkajipdjfam
      │   └── 1.0.1521
      │       ├── manifest.fingerprint
      │       ├── manifest.json
      │       ├── regional_catalog.json
      │       ├── resources.json
      │       └── rs-ABPFilterParserData.dat
      ├── gccbbckogglekeggclmmekihdgdpdgoe
      │   └── 1.0.1026
      │       ├── 21062e05-6c2c-495a-bccb-b681e8bdfea2.jpeg
      │       ├── 3217128b-2500-4a44-857e-4340488fafd8.png
      │       ├── 3c255ec1-6fad-420f-b02c-779c874615d1.png
      │       ├── 51f1a8be-a766-46e9-beca-044cc10109e0.jpeg
      │       ├── manifest.fingerprint
      │       ├── manifest.json
      │       └── photo.json
      ├── iblokdlgekdjophgeonmanpnjihcjkjj
      │   └── 1.0.71
      │       ├── dnryisldmaqljgwaxeqbuuhuvrbboqlf
      │       ├── kkjipiepeooghlclkedllogndmohhnhi
      │       ├── manifest.fingerprint
      │       ├── manifest.json
      │       └── resources.json
      ├── lfgnenkkneohplacnfabidofpgcdpofm
      │   └── 1.0.897
      │       ├── manifest.fingerprint
      │       ├── manifest.json
      │       ├── resources.json
      │       └── rs-AC023D22-AE88-4060-A978-4FEEEC4221693.dat
      ├── ocilmpijebaopmdifcomolmpigakocmo
      │   └── 1.0.53
      │       ├── bvkgcaxyaitmhkbbqnqnqugrjeqzspxv
      │       ├── emgmepnebbddgnkhfmhdhmjifkglkamo
      │       ├── manifest.fingerprint
      │       ├── manifest.json
      │       └── resources.json
      └── oofiananboodjbbmdelgdommihjbkfag
          └── 1.0.120
              ├── 6.0
              ├── manifest.fingerprint
              └── manifest.json
      29 directories, 49 files
      ```
    - 可以看出多出来的只是 `Brave (Rewards)Wallet + Brave Ads + Ad Block`, 所以感觉 Meaningless. 之前看过的软文([How To Enable Or Disable Notifications On The Brave Web Browser | PC | *2022* 👍 - YouTube](https://www.youtube.com/watch?v=86xEqFtENB8) & [Brave浏览器看广告赚取BAT Token | 完美支持MetaMask钱包 | 比谷歌浏览器快3倍，高度保护用户隐私 - YouTube](https://www.youtube.com/watch?v=QGFJ_LbUFpM)), 号称打着边挖矿边保护隐私方面, 还把 Brendan Eich 的名号搬出来, 可笑可笑
      - Notification not for GCM/FCM, via: [Notification problem for some web sites - Browser Support / Desktop Support - Brave Community](https://community.brave.com/t/notification-problem-for-some-web-sites/223966/17)
- [[tool]] FullScreen
  - via: https://github1s.com/xieby1/fullscreen/blob/HEAD/fullscreen.js#L1-L9
  - ```js
    (function() {
      var elem = document.documentElement;
      var rfs =
             elem.requestFullscreen
          || elem.webkitRequestFullScreen
          || elem.mozRequestFullScreen
          || elem.msRequestFullScreen;
      rfs.call(elem);
    })();
    ```
  - More Call Usage via: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call