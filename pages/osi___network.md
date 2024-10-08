description:: 网络层

-
- Networking/OSI/Network
  - IP (Internet Protocol)
    - IPv4 (Internet Protocol version 4)
      - IP 分组数据包
        - ![image](https://user-images.githubusercontent.com/57313137/147385485-ff697c11-65a1-4614-bf59-a92e101fbca7.png)
        - 分片
        - 转发流程
      - NAT (Network Address Translation)
        - 传输层(拿端口号)
      - 子网划分 与 CIDR (Classless Inter-Domain Routing)
      - ARP / DHCP / ICMP
        - ARP (Address Resolution Protocol)
        - DHCP (Dynamic Host Configuration Protocol)
          - 应用层
          - UDP
        - TODO ICMP (Internet Control Message Protocol)
          - 主机或路由器报告差错和异常
          - ![image](https://user-images.githubusercontent.com/57313137/147382997-bdbf7f30-e308-499e-b648-2550702b7e6b.png)
          - 应用: `ping/traceroute`
          - 类型
            - 差错: 终点不可达/超时/参数/重定向(改变路由)...
            - 询问: 回送/时间戳...
            - more via
              - `Control messages`: https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol
              - https://www.cnblogs.com/liuqiyun/p/10364373.html
    - IPv6 (Internet Protocol version 6)
      - No => 首部检验和/首部协议/ARP, 源点分片
      - 过渡方法
        - Dual Stack (双协议栈)
        - Tunneling (隧道)
  - RP ( (Dynamically/Static) Routing Protocol, 动态/静态路由协议)
    collapsed:: true
    - AS (Autonomous System)
    - IGP (International Graduate Program)
      - RIP (Routing Information Protocol, not R.I.P.)
        - 分布式基于距离向量的路由选择协议
        - UDP
      - OSPF (Open Shortest Path First)
        - 分布式的链路状态协议
        - IP, Flooding (洪范法, 略可靠)
    - EGP (International Graduate Program)
      - BGP-4 (Border Gateway Protocol version 4)
        - 路径向量路由选择协议
        - TCP
        - 分类
          - iBGP
          - eBGP
    - 注: 选择路径的时候: AS数 > 内部跳数
  - IP Multicast (IP多播)
    collapsed:: true
    - IGMP (Internet Group Management Protocol)
  - VPN
  - 设备
    collapsed:: true
    - 路由器(隔离 冲突域&广播域 )
    - 中继器/集线器 & 网桥/交换机 区别
-
-
- Refs
  - [Network layer - Wikipedia](https://en.wikipedia.org/wiki/Network_layer)
-
-