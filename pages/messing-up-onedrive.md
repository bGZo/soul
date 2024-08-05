icon:: 📝
created:: [[20221025]]
exclude-from-graph-view:: true
status:: writing/draft
tags:: #onedrive #geek

- ## ↩ Reference
  -
- 因为一开始忽视了软件的使用方式, 导致日常的冗余难以维护, 每次重新 Build 都会产生上十万细小的文件同步, 只是最近这个频率开始变大, 网络情况实在是难以跟上, 一个不小心就浪费了上百兆昂贵的流量, 一个月的额度, 这明明应该是让 Microsoft Offical 头痛的事情, 却神奇地转嫁在我头上, 哈哈哈哈 (悲), 我能给自己提供什么建议吗?
  - 不要忽视小文件, 去尽量优化 meaningless/small size ($<50KB$) 的文件, 像 `.gitignore` 一样, 就比如说我是用的素材管理工具 Billfish 就存在大量的图片缓存(30G -> 1G);
  - 善用 `link/mklink/ln`, 参考软件开发的思路, 减少给部分的耦合, 那么唯一解就只有**通过链接去指向同一个库这个方法了**;
  - $>100M$ 频繁改动的文件不要同步
- 在没有完全吃透一门技术的时候, 我们可以尽情地享受它带个我们的福利, 但是, 这不是免费的, 暗地里都标好了价格.
- Onedrive 在 Linux/MacOS 上的普及程度还有没办法统计, 尤其是 Linux, 真的是未来的痛点.
- 整理 (删除) 文件我给出的建议是
  - 不要在 pause/reset 状态下删除
- reset 之后, 之前做的编辑会失效, 云端和本地两份文件 merge 失败, 当然也非常恶心...
- OneDrive Arrange