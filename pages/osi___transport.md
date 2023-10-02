title:: osi/transport
define:: 建立**端到端**的连接

- OSI/Transport
  - UDP
    - ![image-https://user-images.githubusercontent.com/57313137](../assets/network/147385876-d9ac3168-0555-4244-80ad-741fcd8ab889.png)
      via: https://en.wikipedia.org/wiki/User_Datagram_Protocol
  - TCP
    - ![image](../assets/network/147385959-12ad1630-e0e0-4bee-9aff-3c24b3ed6a89.png){:height 281, :width 716}
      via: https://en.wikipedia.org/wiki/Transmission_Control_Protocol
    - 连接
      - 3 次握手
        - $SYN = 1, seq_{client} = x$
          - SYN 报文
        - $SYN = ACK = 1, seq_{server} = y, ack_{server} = x + 1$
          - SYN-ACK 报文
        - $ACK = 1, seq_{client} = x + 1, ack_{client} = y + 1$
          - ACK 报文
        - ![image.png](../assets/network/image_1666337786741_0.png)
          - ![image](../assets/network/147386123-28c9d059-5b4c-4239-b377-f0ba7e6e1829.png)
        - 注意:
          - $SYN(Synchronization)$; $Seq(Sequence); (ACK)Acknowledged$
          - $x$ 序号产生为随机值; $y$ 序号产生为服务器根据 IP 运算得到的.
          - DDos 攻击, 不断发起 TCP 连接(发出第一次 TCP 握手请求), 但是不进行下一步;
    - 释放
      - 4 次挥手
        - $FIN = 1, seq = u$
          collapsed:: true
          - FIN 报文
        - $ACK = 1, seq = v, ack = u + 1$
          collapsed:: true
          - ACK 报文
        - $ACK = 1, seq = w, ack = u + 1, FIN = 1$
          collapsed:: true
          - FIN-ACK 报文
        - $ACK = 1, seq = u + 1, ack = w + 1$
          collapsed:: true
          - ACK 报文
        - ![image.png](../assets/network/image_1666337709433_0.png){:height 185, :width 259}
          collapsed:: true
          - ![image](../assets/network/147386061-0e10894a-b8da-4217-9ca5-054929492414.png)
        - 注意
          collapsed:: true
          - $u$ $v$ 的值不确定, 因为之前经历了无数的 HTTP 传输, 序号自增到什么地步是不确认的
          - 我查阅的这期视频 ([TCP三次握手和四次挥手_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV18h41187Ep/)) 中, 关于最后挥手是否会发送 $ACK$ 讲述错误, 原文 [RFC 793 - Transmission Control Protocol](https://datatracker.ietf.org/doc/html/rfc793#page-37) 中 并没有提及最开始一方发送的 FIN 后有没有带 ACK. 2022 王道考研也
    - 可靠管理
      - 序号
      - 确认
      - 重传
      - 校验
    - 流量控制
      - 滑动窗口
    - 拥塞控制
      - 慢开始
      - 拥塞避免
      - 快重传
      - 快恢复
-
- socket == IP + 端口号
-