description:: Message Digest Algorithm 5 /  MD5消息摘要算法
author:: [Ronald Rivest](https://en.wikipedia.org/wiki/Ron_Rivest)
published-date:: 19920400
tags:: #[[algorithm]], #[[hash]]

- MD5
  - 128 bits / 16 Bytes / 32 位 16 进制数 (a "word")
- 思路
  - 把一串数据经过处理，得到另一个固定长度的数据
- 特点
  - 不可逆性
  - 唯一性 ( **不完全**可靠
- TODO **Description**
  - Step 1. Append Padding Bits
  - Step 2. Append Length
  - Step 3. Initialize MD Buffer
  - Step 4. Process Message in 16-Word Blocks
  - Step 5. Output
  - $F(X,Y,Z) = (X\wedge{Y}) \vee (\neg{X} \wedge{Z})$
  - $G(X,Y,Z) = (X\wedge{Z}) \vee (Y \wedge \neg{Z})$
  - $H(X,Y,Z) = X \oplus Y \oplus Z$
  - $I(X,Y,Z) = Y \oplus (X \vee \neg{Z})$
  - $\oplus, \wedge, \vee, \neg$ 是 *XOR*, *AND*, *OR* , *NOT* 的符号
- More via: [RFC 1321: The MD5 Message-Digest Algorithm](https://www.rfc-editor.org/rfc/rfc1321) &
  [RFC 6151: Updated Security Considerations for the MD5 Message-Digest and the HMAC-MD5 Algorithms](https://www.rfc-editor.org/rfc/rfc6151)
  > Notice that the collision attack on MD5 can also be applied to password-based challenge-and-response authentication protocols such as the APOP (Authenticated Post Office Protocol) option in POP
  >
- [[Quickref]]
  - [[js]] Library: `https://unpkg.com/spark-md5@3.0.1/spark-md5.min.js`
- Refs
  - [MD5 - Wikipedia](https://en.wikipedia.org/wiki/MD5); [MD5 - 维基百科，自由的百科全书](https://zh.wikipedia.org/zh-cn/MD5)
  - [怎么给文件生成MD5 - 掘金](https://juejin.cn/post/6877072128135561223)
    collapsed:: true
    - [三分钟学习 MD5 - 知乎](https://zhuanlan.zhihu.com/p/26592209)
    - [字节跳动面试官：请你实现一个大文件上传和断点续传](https://juejin.cn/post/6844904046436843527)
    - [js 实现 input file 转换成 blob 和 byte 字节流](https://link.juejin.cn/?target=http%3A%2F%2Fblog.bfw.wiki%2Fuser10%2F15628273380201230054.html)
  - [MD5碰撞——从理论到现实【25c3】【自译】_哔哩哔哩_bilibili](https://www.bilibili.com/video/av7570411/?vd_source=da9d3ea36ca9c1ba9b47b17d8f363922)
  - [MD5 Collision Attack Lab Walkthrough | Cryptography SEEDLab | Coding w/ Kaity - YouTube](https://www.youtube.com/watch?v=mGCVKLLjIns)
-