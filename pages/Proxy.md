---
collapsed: true
alias: 代理, 翻墙, 科学上网
cost: 3
icon: ✈
created: 20230602
title: Proxy
---

- ## Why
  - Due to [[GFW]] )
- ## How
  - How to avoid the DNS cache pollution by IPS? (See ((64795467-e51f-45d9-ab92-8ce0e224ec71)))
    collapsed:: true
    - [ios - iOS 客户端对于运营商劫持的一点点对抗方式_个人文章 - SegmentFault 思否](https://segmentfault.com/a/1190000009049544)
    - [怎样在 Windows、macOS、Android 和 IOS 上刷新 DNS 缓存 | 月灯依旧](https://bynss.com/howto/818944.html)
    - [iOSBlog/防 DNS 污染方案.md at master · ChenYilong/iOSBlog](https://github.com/ChenYilong/iOSBlog/blob/master/Tips/%E5%9F%BA%E4%BA%8EWebsocket%E7%9A%84IM%E5%8D%B3%E6%97%B6%E9%80%9A%E8%AE%AF%E6%8A%80%E6%9C%AF/%E9%98%B2%20DNS%20%E6%B1%A1%E6%9F%93%E6%96%B9%E6%A1%88.md)
  - How to update GeoIP Database? (See ((64795467-3e96-450e-9145-58aa9310c2ec)))
    collapsed:: true
    - And *MAXMIND* change the access to database since 20191230, via: [Significant Changes to Accessing and Using GeoLite2 Databases](https://blog.maxmind.com/2019/12/significant-changes-to-accessing-and-using-geolite2-databases/)
      - > Starting **December 30, 2019,** we will be requiring users of our GeoLite2 databases **to [register for a MaxMind account](https://www.maxmind.com/en/geolite2/signup) and obtain a license key in order to download GeoLite2 databases**. We will continue to offer the GeoLite2 databases without charge, and with the ability to redistribute with proper attribution and in compliance with privacy regulations. In addition, we are **introducing a new [end-user license agreement to govern your use of the GeoLite2 databases](https://www.maxmind.com/en/geolite2/eula) **. Previously, GeoLite2 databases were accessible for download to the public on our developer website and were licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/) .
    - So here is some supported by github:
      - [Loyalsoldier/geoip: 🌚 🌍 🌝 GeoIP 规则文件加强版](https://github.com/loyalsoldier/geoip) ![](https://img.shields.io/github/stars/loyalsoldier/geoip)
      - [alecthw/mmdb_china_ip_list: Geoip MaxMind Database for china ip list](https://github.com/alecthw/mmdb_china_ip_list) ![](https://img.shields.io/github/stars/alecthw/mmdb_china_ip_list)
      - [clashdev/geolite.clash.dev: A MaxMind GeoLite Mirror.](https://github.com/clashdev/geolite.clash.dev) ![](https://img.shields.io/github/stars/clashdev/geolite.clash.dev)
    - [关于GeoIP的二三事|Clash/Surge如何更新GeoIP库 - Sabrina的万事屋](https://merlinblog.xyz/wiki/geoip.html)
  - How to convert proxy node subscription?
    collapsed:: true
    - First of all, we should know, the most important backend, [tindy2013/subconverter](https://github.com/tindy2013/subconverter), is only one service we need to self host;
      ![](https://img.shields.io/github/stars/tindy2013/subconverter)
      - No output `Allow Lan True`
    -
    - Then, let us see what a full url we would get：
      - ((63e5213d-5895-4ec1-8938-0cfb6933539f))
    - In some way, solution needs two parts: the subconverter configure and the convert link. The latter is a likely rss link, in most case. So our target is to figure out the former configuration.
    - The whole shorten configure is following, you could refer the official [Chinese document](https://github.com/tindy2013/subconverter/blob/master/README-cn.md):
    - |调用参数|解释|
      |-------------|---------|
      |target|指想要生成的配置类型|
      |url|指机场所提供的订阅链接或代理节点的分享链接|
      |[group]|用于设置该订阅的组名，多用于SSD/SSR|
      |[upload_path]|用于将生成的订阅文件上传至Gist后的名称|
      |[include]|指仅保留匹配到的节点|
      |[exclude]|指排除匹配到的节点|
      |[config]|指外部配置的地址(包含分组和规则部分)详见|
      |[dev_id]|用于设置QuantumultX的远程设备ID,以在某些版本上开启远程脚本|
      |[filename]|指定所生成订阅的文件名|
      |[interval]|用于设置托管配置更新间隔(秒)|
      |[rename]|用于自定义重命名|
      |[filter_script]|用于自定义筛选节点的js代码|
      |[strict]|如果设置为true，则Surge将在上述间隔后要求强制更新|
      |[upload]|用于将生成的订阅文件上传至Gist，需要填写gistconf.ini，(即不上传)|
      |[emoji]|用于设置节点名称是否包含Emoji|
      |[add_emoji]|用于在节点名称前加入Emoji|
      |[remove_emoji]|用于设置是否删除节点名称中原有的Emoji|
      |[append_type]|用于在节点名称前插入节点类型，如[SS],[SSR]等|
      |[tfo]|用于开启该订阅链接的TCPFastOpen|
      |[udp]|用于开启该订阅链接的UDP|
      |[list]|用于输出SurgeNodeList或者ClashProxyProvider或者[:br]Quantumult(X)的节点订阅或者解码后的SIP002|
      |[sort]|用于对输出的节点或策略组按节点名进行再次排序|
      |[sort_script]|用于自定义排序的js代码|
      |[script]|用于生成ClashScript|
      |[insert]|用于设置是否将配置文件中的insert_url插入|
      |[scv]|用于关闭TLS节点的证书检查|
      |[fdn]|用于过滤目标类型不支持的节点|
      |[expand]|用于在API端处理或转换Surge,QuantumultX,Clash的规则列表|
      |[append_info]|用于输出包含流量或到期信息的节点|
      |[prepend]|用于设置插入insert_url时是否插入到所有节点前面|
      |[classic]|用于设置是否生成Clashclassicalrule-provider|
      |[tls13]|用于设置是否为节点增加tls1.3开启参数|
      |[new_name]|如果设置为true，则将启用Clash的新组名称(proxies,proxy-groups,rules)|
    - Parameters `target` could be:
      | Type | As Source | As Target | Target Name |
      | ---- | ---- | ---- |
      | Clash | ✓ | ✓ | clash |
      | ClashR | ✓ | ✓ | clashr |
      | Quantumult | ✓ | ✓ | quan |
      | Quantumult X | ✓ | ✓ | quanx |
      | Loon | ✓ | ✓ | loon |
      | SS (SIP002) | ✓ | ✓ | ss |
      | SS Android | ✓ | ✓ | sssub |
      | SSD | ✓ | ✓ | ssd |
      | SSR | ✓ | ✓ | ssr |
      | Surfboard | ✓ | ✓ | surfboard |
      | Surge 2 | ✓ | ✓ | surge&ver=2 |
      | Surge 3 | ✓ | ✓ | surge&ver=3 |
      | Surge 4 | ✓ | ✓ | surge&ver=4 |
      | V2Ray | ✓ | ✓ | v2ray |
      | Telegram-liked HTTP/Socks 5 links | ✓ | × | Only as source |
    - The most important thing is point out a configuration address to match our url. You could find that `.acl` file in [ACL4SSR/ACL4SSR](https://github.com/ACL4SSR/ACL4SSR); By the way, the author of this repo also host a [website](https://sub.xeton.dev/) to convert subscription;
      ![](https://img.shields.io/github/stars/ACL4SSR/ACL4SSR)
    - Another is [CareyWang/sub-web](https://github.com/CareyWang/sub-web) ![](https://img.shields.io/github/stars/CareyWang/sub-web)
    - #+BEGIN_NOTE
      Check out repo under the master branch, which is not default branch. 
      #+END_NOTE
    - The most interesting thing is that, the Chinese document of [subconverter](https://github.com/tindy2013/subconverter) is really usefully and inspired ✨
      - > 在进行下一步操作前，十分推荐您阅读以下内容：
        与 调用地址 相关的：[什么是URL？](https://developer.mozilla.org/zh-CN/docs/Learn/Common_questions/What_is_a_URL)
        与 配置文件 相关的：[INI 语法介绍](https://zh.wikipedia.org/wiki/INI%E6%96%87%E4%BB%B6) 、 [YAML 语法介绍](https://zh.wikipedia.org/wiki/YAML#%E8%AA%9E%E6%B3%95) 以及 [TOML 语法介绍](https://toml.io/cn/v1.0.0)
        与 `Clash` 配置相关的：[YAML 语法介绍](https://zh.wikipedia.org/wiki/YAML#%E8%AA%9E%E6%B3%95) 以及 [官方文档](https://github.com/Dreamacro/clash/wiki/configuration)
        与 `模板` 配置相关的：[INJA 语法介绍](https://github.com/pantor/inja)
        会经常涉及到的： [正则表达式入门](https://github.com/ziishaned/learn-regex/blob/master/translations/README-cn.md)
        当遇到问题需要提交 ISSUE 时的：[提问的智慧](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md)
        当您尝试进行进阶操作时，即默认您有相关的操作能力，本程序仅保证在默认配置文件下能够正常运行。
    - Tools you might be used:
      - [URLEncode](https://www.urlencoder.org/)
    - #+BEGIN_WARNING
      We notice the backend have the function to upload subscription to gist;
      And there are more invisible actions, but actually we don't know;
      So this could be a risk worth noting when we use a free convert service.
      #+END_WARNING
      - [品云订阅转换](https://id9.cc/)
      - [Subscription Converter](https://agwa.page/)
      - [Subscription Converter](https://api.nameless13.com/)
      - [Subscription Converter](https://sub-web.wcc.best/)
    - Finally, you should have a dashboard to config, because clash only support API, and there are 2 projects about it.
      - [Dreamacro/clash-dashboard: web port of clash](https://github.com/Dreamacro/clash-dashboard)
        mark:: 去翻 [GA](https://github.com/Dreamacro/clash-dashboard/actions/runs/3965255781/jobs/6794824307) 才发现原来是他们家的： http://clash.razord.top 😂
        collapsed:: true
        - ```
          PS E:\download.vivaldi\clash-dashboard-master> npm start
          
          > clash-dashboard@0.1.0 start
          > vite
          
          failed to load config from E:\download.vivaldi\clash-dashboard-master\vite.config.ts
          error when starting dev server:
          Error: Cannot find module 'node:path'
          Require stack:
          - E:\download.vivaldi\clash-dashboard-master\node_modules\@vitejs\plugin-react\dist\index.cjs
          - E:\download.vivaldi\clash-dashboard-master\vite.config.ts
          - E:\download.vivaldi\clash-dashboard-master\node_modules\vite\dist\node\chunks\dep-3007b26d.js
              at Function.Module._resolveFilename (node:internal/modules/cjs/loader:924:15)
              at Function.Module._load (node:internal/modules/cjs/loader:769:27)
              at Module.require (node:internal/modules/cjs/loader:996:19)
              at require (node:internal/modules/cjs/helpers:92:18)
              at Object.<anonymous> (E:\download.vivaldi\clash-dashboard-master\node_modules\@vitejs\plugin-react\dist\index.cjs:3:14)
              at Module._compile (node:internal/modules/cjs/loader:1092:14)
              at Module._extensions..js (node:internal/modules/cjs/loader:1121:10)
              at Object._require.extensions.<computed> [as .js] (file:///E:/download.vivaldi/clash-dashboard-master/node_modules/vite/dist/node/chunks/dep-3007b26d.js:62324:17)
              at Module.load (node:internal/modules/cjs/loader:972:32)
              at Function.Module._load (node:internal/modules/cjs/loader:813:14)
          ```
      - [haishanh/yacd: Yet Another Clash Dashboard](https://github.com/haishanh/yacd)
        mark:: http://yacd.haishan.me
        collapsed:: true
        - ```
          PS E:\download.vivaldi\yacd-master> npm install axios --registry=http://registry.npm.taobao.org
          [..................] - idealTree:yacd-master: sill                                                    npm ERR! code ERESOLVE
          npm ERR! ERESOLVE unable to resolve dependency treenpm ERR!
          npm ERR! While resolving: yacd@0.3.8
          npm ERR! Found: react@18.2.0
          npm ERR! node_modules/react
          npm ERR!   react@"18.2.0" from the root project
          npm ERR!
          npm ERR! Could not resolve dependency:
          npm ERR! peer react@"^16.8.0 || 17.x" from @reach/menu-button@0.18.0
          npm ERR! node_modules/@reach/menu-button
          npm ERR!   @reach/menu-button@"0.18.0" from the root project
          npm ERR!
          npm ERR! Fix the upstream dependency conflict, or retry
          npm ERR! this command with --force, or --legacy-peer-deps
          npm ERR! to accept an incorrect (and potentially broken) dependency resolution.
          npm ERR!
          npm ERR! See C:\Users\15517\scoop\persist\nodejs\cache\eresolve-report.txt for a full report.
          
          npm ERR! A complete log of this run can be found in:
          npm ERR!     C:\Users\15517\scoop\persist\nodejs\cache\_logs\2023-02-09T10_36_34_551Z-debug.log
          ```
      - collapsed:: true
        #+BEGIN_NOTE
        They all need the \*nix environment, and don't support build in windows.
        #+END_NOTE
        - [如何在 Linux 上优雅的使用 Clash？ · Zs's Blog](https://blog.zzsqwq.cn/posts/how-to-use-clash-on-linux/)
        - [node.js - What is the difference between npm install and npm run build? - Stack Overflow](https://stackoverflow.com/questions/43664200/what-is-the-difference-between-npm-install-and-npm-run-build)
      - Former is better in closing connection; latter is better in select node;
    - [关于策略组的理解](https://github.com/Fndroid/jsbox_script/wiki/关于策略组的理解)
    - [神机规则](https://github.com/ConnersHua/Profiles/)
    - [ACL4SSR_在线订阅转换_停止服务](https://acl4ssr.netlify.app/)
  - How to open Proxy using references?
    collapsed:: true
    - [Proxy Command References · GitHub](https://gist.github.com/bGZo/82a76ecbebf81b556a1d20a91a6bd21a)
      {{iframe https://gist.github.com/bGZo/82a76ecbebf81b556a1d20a91a6bd21a}}
- ## What
  - >上机 3h，测试网络 2h，刚敲没半个小时，下课了，草 🤯 
    #joke
  - What is proxies? And how many specifications (protocols) they have?
    collapsed:: true
    - [SS](https://shadowsocks.org/) / [Shadowsocks](https://github.com/shadowsocks)
      wikipedia:: [Shadowsocks - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/Shadowsocks)
      collapsed:: true
      - What's socks5?
        collapsed:: true
        - 基于 Socks5 代理方式的网络数据加密传输包
          collapsed:: true
          - **SOCK5**
            - Practically, a SOCKS server proxies TCP connections to an arbitrary IP address, and provides a means for UDP packets to be forwarded.
            - SOCKS performs at Layer 5 of the OSI model (the session layer, an intermediate layer between the presentation layer and the transport layer)
            - It was approved by the IETF in 1996 as RFC 1928
            - Since SOCKS is very detectable, a common approach is to present a SOCKS interface for more sophisticated protocols:
            - see more in wikipedia
      - [写给非专业人士看的 Shadowsocks 简介 | 綠茶如是说](http://vc2tea.com/whats-shadowsocks)
        collapsed:: true
        - SSH Tunnel
          collapsed:: true
          ![🖼 ](../assets/2023/whats-shadowsocks-03.png)
          - 1) 首先用户和境外服务器基于 ssh 建立起一条加密（RSA）的通道
          - 2-3) 用户通过建立起的隧道进行代理，通过 ssh server 向真实的服务发起请求
          - 4-5) 服务通过 ssh server，再通过创建好的隧道返回给用户
        - Shadowsocks
          collapsed:: true
          ![🖼 ](../assets/2023/whats-shadowsocks-04.png)
          - #+BEGIN_NOTE
            简单理解的话，shadowsocks 是将原来 ssh 创建的 Socks5 协议拆开成 server 端和 client 端，所以下面这个原理图基本上和利用 ssh tunnel 大致类似
            #+END_NOTE
          - 6) 客户端发出的请求基于 Socks5 协议跟 ss-local 端进行通讯，由于这个 ss-local 一般是本机或路由器或局域网的其他机器，不经过 GFW，所以解决了上面被 GFW 通过特征分析进行干扰的问题
          - 5) ss-local 和 ss-server 两端通过多种可选的加密方法进行通讯，经过 GFW 的时候是常规的TCP包，没有明显的特征码而且 GFW 也无法对通讯数据进行解密
          - 4) ss-server 将收到的加密数据进行解密，还原原来的请求，再发送到用户需要访问的服务，获取响应原路返回
      - [关于最近 @clowwindy 事件的整理 - PRIN BLOG](https://printempw.github.io/about-clowwindy-archive)
        collapsed:: true
        - 有幸从事件初露端弥的时候就得知消息，这里整理了一下事件的时间轴。希望这点资料能帮助到别人。
        - 8.20：@clowwindy 就 @breakwa11 关于 shadowsocks-rss 开源协议问题发言
          collapsed:: true
          - 根据 @clowwindy 的发言可以确定的具体喝茶时间
            collapsed:: true
            - > Two days ago the police came to me and wanted me to stop working on this. Today they asked me to delete all the code from GitHub. I have no choice but to obey.
              > I hope one day I’ll live in a country where I have freedom to write any code I like without fearing.
              > I believe you guys will make great stuff with Network Extensions.
              > Cheers!
          - 晚：访问 V2EX shadowsocks 节点跳转到首页
            collapsed:: true
            - 根据 ＠livid 在 [这里](http://www.v2ex.com/t/215136#reply57) 32楼的发言来看，shadowsocks 节点并非被移除而是对注册时间少于 1000 天的用户隐藏了
            - @clowwindy 把他所维护的几个 shadowsocks 实现的代码仓库内的 Issue 面板全部关闭，所有帮助信息全部删除，所有的描述都改成了 Something happened。另外，他还清空了该组织的 membership，或者将所有成员全部转入隐私状态，不对外公开。
            - <https://typeblog.net/life/2015/08/21/long-live-shadowsocks.html>
        - 8.21：传出 @clowwindy 被请去喝茶的消息
          collapsed:: true
          - 他在 shadowsocks-windows 的 \#305 issue 下回复道
          - > I was invited for some tea yesterday. I won’t be able to continue developing this project.
          - 同时开启了 twitter 的隐私保护，除先前关注者外无法查看动态
          - 晚：@clowwindy 发布了 _thanks._ 后的推文，证明人没事
            - shadowsocksR 作者 @breakwa11 表示会继续开发新版本，@clowwindy 对其致谢
        - 8.22：@clowwindy 删除所有 github 上的 shadowsocks 仓库，之前在 twitter 上发布了删除的相关动态。同时 @clowwindy 明确表示不会继续开发 shadowsocks 项目
        - 8.24：@breakwa11 发布 ShadowsocksR C# v3.4.0
        - 8.25：@breakwa11 发布 SSR 更新计划
      - [https://github.com/shadowsocks/shadowsocks-iOS/issues/124](https://web.archive.org/web/20150822223925/https://github.com/shadowsocks/shadowsocks-iOS/issues/124) (web archive)
        collapsed:: true
        - [shadowsocks_install](https://github.com/teddysun/shadowsocks_install)
          collapsed:: true
          - Backup：[shadowsocks_install](https://github.com/heweiye/teddysunBackup)
          - [Docs](https://teddysun.com/486.html)
      - [KeiKinn/ShadowsocksBio: 记录一下Shadowsocks的前世今生，以及一个简单的教程总结 (github.com)](https://github.com/KeiKinn/ShadowsocksBio) ![](https://img.shields.io/github/stars/KeiKinn/ShadowsocksBio)
      - [shadowsocksr-rm/shadowsocks-rss: ShadowsocksR update rss, SSR organization https://github.com/shadowsocksr](https://github.com/shadowsocksr-rm/shadowsocks-rss)
        - [Home · shadowsocksrr/shadowsocks-rss Wiki](https://github.com/shadowsocksrr/shadowsocks-rss/wiki)
    - SSR / ShadowsocksR
    - [2dust/v2rayN: A V2Ray client for Windows, support Xray core and v2fly core](https://github.com/2dust/v2rayN) ![](https://img.shields.io/github/stars/2dust/v2rayN)
      collapsed:: true
      - 模块化的代理软件包，它的目标是提供常用的代理软件模块，简化网络代理软件的开发
      - [Loyalsoldier/v2ray-rules-dat: 🦄 🎃 👻 V2Ray 路由规则文件加强版，可代替 V2Ray 官方 geoip.dat 和 geosite.dat，兼容 Shadowsocks-windows、Xray-core、Trojan-Go 和 leaf](https://github.com/Loyalsoldier/v2ray-rules-dat) ![](https://img.shields.io/github/stars/Loyalsoldier/v2ray-rules-dat)
      - [v2ray](https://github.com/233boy/v2ray)
        - [v2ray 教程](https://github.com/vkuajing/v2ray).
        - Backup：[233boy-v2ray](https://github.com/PhenTse/233boy-v2ray)
    - Others by VPN provider: #.ol
      collapsed:: true
      - OpenVPN
      - IKEv2/IPsec
      - WireGuard
      - SSTP
      - L2TP/IPSec
      - PPTP
  - What is the difference with those circuits?
    collapsed:: true
    - $$ IPLC / IEPL > CN2_{GIA} > BGP > 中继_{隧道} > CN2_{GT} > 直连 > 普通$$
    - Leased line 不过墙
      wikipedia:: [Leased line - Wikipedia](https://en.wikipedia.org/wiki/Leased_line)
      - **IPLC** / International Private Leased Circuit
        - 国际私有租赁线路
      - **IEPL** / International Ethernet Private Line
        - 国际以太网专线
    - Public Internet Access 公网出口
      - **ChinaNet** / 163骨干网 / AS4134
        - 骨干网, 基建早, 带宽大, 便宜, 承载普通质量的互联网业务.
        - 接入国际 Tier1/2 运营商以及主流 OTT
      - **Chinatelecom Next Carrier Network** / CNCN / CN2 / AS4809
        - 后进骨干网, 稳定高速, 时延敏感
        - 直连国际网. 国际出口有单独线路
        - **CN2 GT** / Global Transit
          - 全球互联网资源转接
        - **CN2 GIA** / Global Internet Access
          - 为企业提供 **中国方向** 互联网专线接入.
          - GIA 单独回国线路, 高优先级, 高质量
          - 接入CN2，出口全程CN2, 但出口带宽小, 有网络波动.
          - **单程/单向 CN2**
            - **去CN2, 回ChinaNet**
              - 测试效果好, 实际体验无感.
            - **去ChinaNet, 回CN2**
              - 综合抗DDoS, 速度, 价格的最优解.
          - **双程/双向 CN2**
      - Telecom Global Internet Services / **GIS**
        - Global Transit (GT)
        - Global Internet Access(GIA)
        - ChinaNet Paid-Peer
        - China Access
      - more via: [浅谈中国电信出口网络的链路情况](https://www.oldking.net/751.html)
    - **BGP** / Border Gateway Protocol
      - 边界网关协议, 互联网AS间的互联
      - BGP多线机房相较于双IP双线机房更优
    - **中继**
      - 入口国内, 出国国外, 过墙会用隧道协议 (负载均衡 -> 防止被墙)
  - What is DNS?
    id:: 64795467-e51f-45d9-ab92-8ce0e224ec71
    collapsed:: true
    - [paulmillr/encrypted-dns: Configuration profiles for DNS HTTPS and DNS over TLS for iOS 14 and MacOS Big Sur](https://github.com/paulmillr/encrypted-dns)
  - What is the GeoIP database?
    id:: 64795467-3e96-450e-9145-58aa9310c2ec
    collapsed:: true
    - Another useful file is `GeoIP`, which is supported by [MAXMIND](https://www.maxmind.com/en/geoip2-country-database), to determine an Internet visitor's country based on their IP address. And this file is often used in your `config.yaml`. Check your configure )
      - ![Code_211.png](../assets/Code_211_1676435689409_0.png)
      - Check document in [Configuration · Dreamacro/clash Wiki](https://github.com/Dreamacro/clash/wiki/configuration)
        - > **Rules**
          `GEOIP`: `GEOIP,CN,policy` routes any requests to a China IP address to `policy`.
  - The clients recommended:
    collapsed:: true
    - iOS: Surge 4, Quantumult X, Quantumult, Loon, Shadowrocket
    - Android: Clash for Android, Surfboard
    - macOS: Surge for Mac, ClashX, Clash for Windows
    - Windows: Clash for Windows
    - Linux: Clash
    - ##### iOS 客户端 (全区可下载,包括中区)
    - [Loon](https://testflight.apple.com/join/23LA2tmX) (支持Surge 3的 RULESET 规则)
    - [Outline](https://apps.apple.com/cn/app/outline-app/id1356177741) (支持SS)
    - [Kitsunebi](https://testflight.apple.com/join/IdFRwmNy) (支持SS/Vmess)
    - [Potatso Lite](https://testflight.apple.com/join/NkF46PRd)
    - [A.BIG.T IV](https://testflight.apple.com/join/3aArQFMQ)
    - [BananaNet](https://testflight.apple.com/join/v5x8B81b)
    - [NetShuttle](https://testflight.apple.com/join/742YC03J)
    - ##### iOS 客户端 (仅国区下架,其他区可下载)
    - [Surge 4](https://apps.apple.com/us/app/id1442620678) 免费 + 内购 $49.99 (支持SS/Snell/Vmess) [官网购买](https://nssurge.com/buy_now) [教程](https://zhuangzhuang.cf/tags/#Surge)
    - [Quantumult X](https://apps.apple.com/us/app/quantumult-x/id1443988620) $7.99 (支持SS/SSR/Vmess) [教程](https://www.notion.so/kopshawn/Quantumult-X-1d32ddc6e61c4892ad2ec5ea47f00917) [视频教程](https://youtu.be/laqB-SMHO1w)
    - [Quantumult](https://apps.apple.com/us/app/quantumult/id1252015438) $4.99 (也叫:圈, 支持SS/SSR/Vmess) [教程](https://github.com/JasonLee-Go/Quantumult/wiki/Quantumult-Unofficial-Manual)
    - [Quantumult Bundle](https://apps.apple.com/us/app-bundle/quantumult-x-upgrade/id1482985563) $9.99 (Bundle包,包括Quantumult X和Quantumult)
    - [Loon](https://apps.apple.com/us/app/loon/id1373567447) $2.99 (支持SS/SSR/Vmess) [视频教程](https://youtu.be/v3gHdE5UEw8)
    - [Shadowrocket](https://apps.apple.com/us/app/shadowrocket/id932747118) $2.99 (也叫:小火箭, 支持SS/SSR/Vmess/Trojan/Snell/Lua) [教程](http://laob.me/2300)
    - [Pharos Pro](https://apps.apple.com/us/app/pharos-pro/id1456610173) $1.99 (支持SS/SSR/Vmess/Trojan)
    - [Kitsunebi](https://apps.apple.com/us/app/kitsunebi-proxy-utility/id1446584073) $4.99 (支持SS/Vmess)
    - [Pepi](https://apps.apple.com/us/app/pepi/id1283082051) $1.99
    - [Potatso 2](https://apps.apple.com/us/app/id1162704202) $2.99
    - [Potatso Lite](https://apps.apple.com/us/app/id1239860606) Free
    - [Ranger NetworkTool](https://apps.apple.com/us/app/ranger-networktool/id1330474376) $1.99
    - [Wingy](https://apps.apple.com/us/app/wingy-http-s-socks5-proxy-utility/id1178584911) $0.99
    - [ShadowPocket](https://apps.apple.com/us/app/shadowpocket/id1354988493) $1.99
    - [AnyFlow](https://apps.apple.com/us/app/anyflow-a-super-cool-network-tool/id1176894911) $4.99
    - [Shadowfish](https://apps.apple.com/us/app/shadowfish/id1220680757) $0.99
    - [Alice](https://apps.apple.com/us/app/alice-network-proxy-utility/id1135320992) $1.99
    - [Bedrock](https://apps.apple.com/us/app/bedrock/id1362340186) $3.99
    - [Mume VPN](https://apps.apple.com/us/app/mume-vpn/id1144787928) $0.99
    - [寒梅 · Mume Red](https://apps.apple.com/us/app/id1453275281) Free
    - [A.BIG.T](https://apps.apple.com/us/app/surfing-advanced-proxy/id1051326718) Free
    - [Skarp](https://apps.apple.com/us/app/skarp/id1300469689) Free
    - [FastSocks](https://apps.apple.com/us/app/id1388244800) Free
    - [ShadowLink](https://apps.apple.com/us/app/shadowlink-shadowsocks-tool/id1439686518) Free
    - [NetShuttle](https://apps.apple.com/us/app/netshuttle-shadowsocksr-tool/id982708939) Free
    - [Oriole](https://apps.apple.com/us/app/id1245170216) Free
    - [Brook](https://apps.apple.com/us/app/brook-brook-shadowsocks-vpn-proxy/id1216002642) Free
    - [Fugu2](https://apps.apple.com/us/app/fugu-2/id1215255916) Free
    - ##### macOS 客户端
    - [Surge for Mac](http://nssurge.com/) $49.99/$69.99/$99.99 (支持SS/Snell/Vmess)
    - [ClashX](https://github.com/yichengchen/clashX/releases) Clash的Mac图形客户端 (支持SS/Snell/Vmess) [教程](https://docs.nameless13.com/clashr)
    - [ClashX Pro](https://install.appcenter.ms/users/clashx/apps/clashx-pro/distribution_groups/public) 支持开启”增强模式的”ClashX
    - [Clash for Windows](https://github.com/Fndroid/clash_for_windows_pkg/releases) Clash的Windows/macOS图形客户端,简称:CFW (支持SS/Snell/Vmess/Trojan) [教程](https://docs.cfw.lbyczf.com/) [视频教程](https://youtu.be/21prqwxBg94)
    - [ClashXR](https://github.com/WhoJave/clashX/releases) Clash客户端(支持SS/Snell/Vmess/SSR) [教程](https://docs.nameless13.com/clashr)
    - [Clashy](https://github.com/SpongeNobody/Clashy/releases) Windows /Mac/Ubuntu适用的Clash客户端
    - [Clash 内核](https://github.com/Dreamacro/clash/releases) 一个Go语言开发的多平台代理客户端 (支持SS/Snell/Vmess/Trojan)
    - [ShadowClash](https://github.com/TheWanderingCoel/ShadowClash)
    - [Trojan-Qt5](https://github.com/TheWanderingCoel/Trojan-Qt5/releases) (支持SS/SSR/Snell/Vmess/Trojan)
    - [Mellow](https://github.com/eycorsican/Mellow/releases) (支持SS/Vmess)
    - [ShadowsocksX](https://github.com/shadowsocks/shadowsocks-iOS/releases)
    - [ShadowsocksX-NG](https://github.com/shadowsocks/ShadowsocksX-NG/releases) (支持SS)
    - [ShadowsocksX-NG-R8](https://github.com/qinyuhang/ShadowsocksX-NG-R/releases) (支持SS/SSR)
    - [ShadowsocksX-NG-R8](https://github.com/paradiseduo/ShadowsocksX-NG-R8/releases)
    - [ShadowsocksX-NG-R](https://github.com/leadscloud/ShadowsocksX-NG-R/releases)
    - [ShadowsocksX-NG-R](https://github.com/wzdnzd/ShadowsocksX-NG-R/releases)
    - [electron-ssr](https://github.com/qingshuisiyuan/electron-ssr-backup/releases)
    - [Outline](https://apps.apple.com/cn/app/outline-secure-internet-access/id1356178125) Free
    - [Reborn](https://github.com/langyanduan/Reborn/releases)
    - [Shuttle](https://github.com/sipt/shuttle/releases)
    - [SsrConnectPro](https://apps.apple.com/cn/app/ssrconnectpro/id1376924741) ¥3.00
    - [GoAgentX](https://pan.lanzou.com/i0dskef)
    - [非官方GoAgentX](https://github.com/mithril-global/GoAgentX/releases)
    - [Flora](https://github.com/huacnlee/flora-kit/releases)
    - [SpechtLite](https://github.com/zhuhaow/SpechtLite/releases)
    - [Buff](https://www.plutox.top/)
    - ##### Windows 客户端
    - [Clash for Windows](https://github.com/Fndroid/clash_for_windows_pkg/releases) Clash的Windows/macOS图形客户端,简称:CFW (支持SS/Snell/Vmess/Trojan) [教程](https://docs.cfw.lbyczf.com/) [视频教程](https://youtu.be/21prqwxBg94)
    - [Clash for Windows 中文版](https://github.com/kallydev/clash_for_windows_pkg_zh-cn/releases)
    - [ClashR for windows](https://t.me/yxbjx/411954) Clash客户端(支持SS/Snell/Vmess/SSR) [教程](https://docs.nameless13.com/clashr)
    - [Clash 内核](https://github.com/Dreamacro/clash/releases) 一个Go语言开发的多平台代理客户端 (支持SS/Snell/Vmess/Trojan)
    - [ClashR 内核](https://github.com/BROBIRD/clash/releases) 支持SS/Snell/Vmess/SSR的Clash客户端 [教程](https://docs.nameless13.com/clashr)
    - [ClashR 内核](https://github.com/frainzy1477/clashrdev/releases) 支持SS/Snell/Vmess/SSR的Clash客户端 [教程](https://docs.nameless13.com/clashr)
    - [Clashy](https://github.com/SpongeNobody/Clashy/releases) Windows /Mac/Ubuntu适用的Clash客户端
    - [ClashCS](https://github.com/Krazysdaki/ClashCS-Beta/releases) A Beta version Clash GUI built by C#
    - [Clash-Web-Bat](https://github.com/pcysanji/Clash-Web-Bat/releases) [文档](https://github.com/pcysanji/Clash-Web-Bat/blob/master/README.md)
    - [ClashCMD](https://github.com/tindy2013/clashcmd/releases) [文档](https://github.com/tindy2013/clashcmd/blob/master/README.md)
    - [ClashWeb](https://github.com/lzdnico/ClashWeb/releases) [文档](https://github.com/lzdnico/ClashWeb/blob/master/README.md)
    - [ShadowClash](https://github.com/TheWanderingCoel/ShadowClash)
    - [Trojan-Qt5](https://github.com/TheWanderingCoel/Trojan-Qt5/releases) (支持SS/SSR/Snell/Vmess/Trojan)
    - [Netch](https://github.com/netchx/Netch/releases) (支持SS/SSR/Vmess)
    - [Mellow](https://github.com/eycorsican/Mellow/releases) (支持SS/Vmess)
    - [Shadowsocks](https://github.com/shadowsocks/shadowsocks-windows/releases) (简称:SS)
    - [simple-obfs](https://github.com/shadowsocks/simple-obfs/releases) (SS的插件)
    - [Shadowsocks 2.3.1](https://github.com/shadowsocks/shadowsocks-windows/releases/tag/2.3.1)（XP 系统可用）
    - [ShadowsocksR](https://github.com/shadowsocksr-backup/shadowsocksr-csharp/releases) (简称:SSR)
    - [ShadowsocksR](https://github.com/HMBSbige/ShadowsocksR-Windows/releases) (HMBSbige 修改版)
    - [ShadowsocksR 4.7.0](https://github.com/congcong0806/congcong0806.github.io/raw/master/files/ShadowsocksR_4.7.0_Windows.7z) (@breakwa11 破娃最后一版)
    - [ShadowsocksR](https://github.com/congcong0806/congcong0806.github.io/raw/master/files/ShadowsocksR_rixCloud_Windows.7z) (SSR,rixCloud, Inc. 修改版)
    - [ShadowsocksRR](https://github.com/shadowsocksrr/shadowsocksr-csharp/releases) (简称:SSRR)
    - [SSRR](https://github.com/SoDa-GitHub/SSRR-Windows/releases)
    - [ShadowsocksD](https://github.com/SoDa-GitHub/SSD-Windows/releases) (简称:SSD)
    - [electron-ssr](https://github.com/qingshuisiyuan/electron-ssr-backup/releases)
    - [SScap](https://sourceforge.net/projects/sscap)
    - [SSTap](https://github.com/mayunbaba2/SSTap-beta-setup)
    - [SocksCap](https://www.sockscap64.com/sockscap-64-free-download)
    - [Outline](https://raw.githubusercontent.com/Jigsaw-Code/outline-releases/master/manager/Outline-Manager.exe)
    - [x2tap](https://github.com/hacking001/x2tap/releases)
    - [Shuttle](https://github.com/sipt/shuttle/releases)
    - [flora](https://github.com/huacnlee/flora-kit/releases)
    - [kcptun](https://github.com/shadowsocks/kcptun/releases)
    - ##### Android 客户端
    - [Clash for Android](https://github.com/Kr328/ClashForAndroid/releases) Clash的Android图形客户端 (支持SS/Snell/Vmess) [教程](https://wiki.kache.moe/2019/12/10/Andoird-Clash for Android)
    - [Clash for Android Google Play](https://play.google.com/store/apps/details?id=com.github.kr328.clash) Clash的Android图形客户端 (支持SS/Snell/Vmess)
    - [ClashR for Android](https://github.com/BROBIRD/ClashForAndroid/releases) Clash的Android图形客户端 (支持SS/Snell/Vmess/SSR) [教程](https://docs.nameless13.com/clashr)
    - [ClashA](https://github.com/ccg2018/ClashA/releases) Clash的Android图形客户端 (支持SS/Snell/Vmess)
    - [ClashAR](https://github.com/WhoJave/ClashA/releases) Clash客户端(支持SS/Snell/Vmess/SSR)
    - [Surfboard](https://manual.getsurfboard.com/cn/introduction)（Surfboard支持导入Surge配置,支持SS/Vmess）
    - [Surfboard Google Play](https://play.google.com/store/apps/details?id=com.getsurfboard)
    - [Pharos](https://github.com/PharosVip/Pharos-Android-Test/releases) (支持SS/SSR/Vmess/Trojan)
    - [Kitsunebi](https://github.com/eycorsican/kitsunebi-android/releases)
    - [Kitsunebi Google Play](https://play.google.com/store/apps/details?id=fun.kitsunebi.kitsunebi4android)
    - [SSRRAY](https://github.com/xxf098/shadowsocksr-v2ray-android/releases) A ShadowsocksR and V2Ray Client for Android
    - [Shadowsocks 影梭](https://github.com/shadowsocks/shadowsocks-android/releases)
    - [Shadowsocks 影梭 Google Play](https://play.google.com/store/apps/details?id=com.github.shadowsocks)
    - [Shadowsocks 影梭 Google Play Beta 版](https://play.google.com/apps/testing/com.github.shadowsocks)
    - [Simple Obfuscation](https://github.com/shadowsocks/simple-obfs-android/releases) (影梭的插件)
    - [Simple Obfuscation Google Play](https://play.google.com/store/apps/details?id=com.github.shadowsocks.plugin.obfs_local) (影梭的插件)
    - [ShadowsocksD](https://github.com/TheCGDF/SSD-Android/releases) (简称:SSD)
    - [ShadowsocksR](https://github.com/shadowsocksr-backup/shadowsocksr-android/releases) (简称:SSR)
    - [ShadowsocksR 3.4.0.6](https://github.com/congcong0806/congcong0806.github.io/raw/master/files/ShadowsocksR_3.4.0.6_Android.zip) (@breakwa11 破娃最后一版)
    - [ShadowsocksR](https://github.com/congcong0806/congcong0806.github.io/raw/master/files/ShadowsocksR_rixCloud_Android.zip) (SSR,rixCloud, Inc. 修改版)
    - [ShadowsocksR](https://github.com/congcong0806/congcong0806.github.io/raw/master/files/Maying_3.4.0.8.3.zip) (SSR,魅影修改版)
    - [ShadowsocksRR](https://github.com/shadowsocksrr/shadowsocksr-android/releases) (简称:SSRR)
    - [shadowsocksRb](https://github.com/shadowsocksRb/shadowsocksRb-android/releases)
    - [Maying](https://github.com/congcong0806/congcong0806.github.io/raw/master/files/Maying_1.1.6.zip) (ShadowsocksRR, Java修改版)
    - [ShadowIce Google Play](https://play.google.com/store/apps/details?id=com.github.shadowice)
    - [Outline](https://play.google.com/store/apps/details?id=org.outline.android.client)
    - [NetPatch](https://play.google.com/store/apps/details?id=co.netpatch.firewall)
    - [Postern](https://play.google.com/store/apps/details?id=com.tunnelworkshop.postern)（Postern 支持导入 Surge 配置）
    - [BifrostV](https://play.google.com/store/apps/details?id=com.github.dawndiy.bifrostv)
    - [kcptun-android](https://github.com/shadowsocks/kcptun-android/releases)
    - ##### Linux 客户端
    - [Clashy](https://github.com/SpongeNobody/Clashy/releases) Windows /Mac/Ubuntu适用的Clash客户端
    - [Clash 内核](https://github.com/Dreamacro/clash/releases) 一个Go语言开发的多平台代理客户端 (支持SS/Snell/Vmess/Trojan)
    - [ShadowClash](https://github.com/TheWanderingCoel/ShadowClash)
    - [Trojan-Qt5](https://github.com/TheWanderingCoel/Trojan-Qt5/releases) (支持SS/SSR/Snell/Vmess/Trojan)
    - [Mellow](https://github.com/eycorsican/Mellow/releases) (支持SS/Vmess)
    - [electron-ssr](https://github.com/qingshuisiyuan/electron-ssr-backup/releases)
    - [Shadowsocks-qt5](https://github.com/shadowsocks/shadowsocks-qt5)
    - [ShadowsocksR](https://github.com/ssrbackup/shadowsocksr) (简称:SSR)
    - [Outline](https://raw.githubusercontent.com/Jigsaw-Code/outline-releases/master/manager/Outline-Manager.AppImage)
    - [Avege](https://github.com/avege/avege)
    - [flora](https://github.com/huacnlee/flora-kit)
    - [Shuttle](https://github.com/sipt/shuttle)
    - [kcptun](https://github.com/shadowsocks/kcptun/releases)
    - ##### 路由器
    - [OpenClash](https://github.com/vernesong/OpenClash/wiki)
    - [Clash-Merlin](https://github.com/KOP-XIAO/Clash-Merlin/wiki)
    - [Koolshare OpenWrt/LED](https://koolclash.js.org/)
    - [KoolClash](https://github.com/SukkaW/Koolshare-Clash/releases)
    - [fancyss](https://github.com/hq450/fancyss)
    - [Clash for OpenWrt](https://github.com/frainzy1477/clash/releases)
    - [ClashR for OpenWrt](https://github.com/frainzy1477/clashr/releases)
    - [Luci For Clash - OpenWrt](https://github.com/frainzy1477/luci-app-clash/releases)
    - [OpenWRT-Shadowsocks](https://github.com/shadowsocks/openwrt-shadowsocks)
    - [Padavan](https://www.right.com.cn/forum/thread-161324-1-1.html)
    - ##### TV
    - [Shadowsocks 影梭](https://github.com/shadowsocks/shadowsocks-android/releases) (选择shadowsocks-tv)
    - ##### V2Ray 客户端
    - iOS
    - - Surge 4, Quantumult X, Quantumult, Shadowrocket, Pharos Pro, Kitsunebi, Loon ↑
      - [i2Ray](https://apps.apple.com/us/app/id1445270056) $3.99
    - Windows
    - - Clash for Windows ↑
      - [v2rayN](https://github.com/2dust/v2rayN/releases)
      - [V2RayW](https://github.com/Cenmrev/V2RayW/releases)
      - [V2RayS](https://github.com/Shinlor/V2RayS/releases)
      - [Qv2ray](https://github.com/Qv2ray/Qv2ray/releases)
    - macOS
    - - ClashX ↑
      - [V2RayX](https://github.com/Cenmrev/V2RayX/releases)
      - [V2rayU](https://github.com/yanue/V2rayU/releases)
      - [V2RayC](https://github.com/gssdromen/V2RayC)
      - [Qv2ray](https://github.com/Qv2ray/Qv2ray/releases)
    - Linux
    - - [Qv2ray](https://github.com/Qv2ray/Qv2ray/releases)
    - Android
    - - Clash for Android ↑
      - [v2rayNG](https://github.com/2dust/v2rayNG/releases)
      - [v2rayNG Google Play](https://play.google.com/store/apps/details?id=com.v2ray.ang)
    - ##### Trojan 客户端
    - iOS: Surge 4, Shadowrocket, Pharos Pro ↑
    - Android: [igniter](https://github.com/trojan-gfw/igniter/releases/tag/v0.1.0-pre-alpha16)
    - Windows: [Trojan-Qt5](https://github.com/TheWanderingCoel/Trojan-Qt5/releases)
    - macOS: Surge Mac, [Trojan-Qt5](https://github.com/TheWanderingCoel/Trojan-Qt5/releases) [TrojanX](https://github.com/JimLee1996/TrojanX/releases)
    - Linux: [Trojan-Qt5](https://github.com/TheWanderingCoel/Trojan-Qt5/releases)
  - FAQ
    collapsed:: true
    - Battery using is huge
      collapsed:: true
      - 这是移动操作系统的一个特殊机制，Surge、Quantumult、Shadowrocket等等所有的 SS 客户端开启后会接管全局的（几乎）所有通信，所以所有的网络方面电量消耗都会被算在 SS 客户端头上，实际使用中不会感到 SS 客户端对电量有明显影响，「设置-电池」中看到它的电池用量，绝大部分都是网络所消耗的电量，并不是 SS 客户端消耗的电量，SS 客户端就是背锅侠。
    - **Telegram 客户端 Proxy 代理设置**
      - https://telegra.ph/Telegram-Proxy-02-15
    - iOS 设备上使用 SS 客户端也会显示VPN 图标:是因为使用了 iOS 系统的 VPN Network Extension 接口（以及 NEPacketTunnelProvider 和 NWUDPSession 组件），iOS 9 才开放的此接口，这些新接口让我们可以制作出私密协议的VPN产品，苹果官方称之为 Enterprise VPN。正是因为 iOS 9 之后开放了这个接口和组件才能有今天iOS 上的各式各样的 SS 客户端。
    - 官方文档:https://developer.apple.com/documentation/networkextension
    - SS/SSR 客户端，在连接SS/SSR 服务器的同时也会在本机开启SOCKS5 和HTTP 连接，用于本机软件和同一局域网内的其他设备连接，所以SS/SSR 信息部分必须和SS/SSR 服务器信息一致。
    - 本地开启的SOCKS5 与SS/SSR 信息无关的，本机的软件和同一局域网内的其他设备只需要连接此台机器就行了，IP和端口也必须和SS/SSR 客户端上开启的信息一致。
    - 本机的软件和同一局域网内的其他设备通过SOCKS5 连接到此台机器的SS/SSR 客户端，SS/SSR 客户端再连接到SS/SSR 服务器。
    - 引用一句 clowwindy 的话:
      - > *往往不需要政府造墙，网民也会自发造墙*
    - ==[欢迎 - 教程WIKI](https://help.happynothings031.xyz/)==
    - [关于在使用 Clash 过程中遇到的问题 - 明心的博客 | 明心 Blog](https://benjamingao.github.io/2019/03/02/%E5%85%B3%E4%BA%8E%E5%9C%A8%E4%BD%BF%E7%94%A8-Clash-%E8%BF%87%E7%A8%8B%E4%B8%AD%E9%81%87%E5%88%B0%E7%9A%84%E9%97%AE%E9%A2%98/)
  - collapsed:: true
    #+BEGIN_IMPORTANT
    Proxies [[sucks]] as well, which would be identified and treated as spam by some service providers.
    #+END_IMPORTANT
    - Reddit [[sucks]]
      - [I got the error message "Looks like you've been doing that a lot. Take a break for 5 minutes before trying again." when posting my first thread in 8 days. : help](https://www.reddit.com/r/help/comments/nh2tsy/i_got_the_error_message_looks_like_youve_been/)