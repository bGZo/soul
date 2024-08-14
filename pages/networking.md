icon:: 🌐
also:: 网络
created:: [[20240814]]
description::

- ## Why
  -
- ## How
  -
- ## What
  -
- ## Namespace
  - {{namespace networking}}
- ## ↩ Reference
  - [Why is Ethernet So Power Hungry? - Electrical Engineering Stack Exchange](https://electronics.stackexchange.com/questions/52349/why-is-ethernet-so-power-hungry)
    collapsed:: true
    - This is mostly due to ethernet not being a mobile standard. It was never intended for low power usage
    - The biggest current draw in a operating mode is the integrated PHY. It keeps the ethernet connection active. As long as a cable is plugged in (on both ends and both devices are on), the link is active, 10baseT keeps ±2v on each pair. This is how the standard (IEEE 802.3) was designed, a always active data connection.
    - On the other hand, all of these have a comparably low standby/powerdown current. If you need "low power" ethernet, then you want to power manage. If you don't need to use the ethernet, you power off the entire thing. This works great for transmit only projects. Arbitrary receive mode projects, not so much (web host for example).
    - http://www.silabs.com/Support%20Documents/TechnicalDocs/CP2200.pdf
    - http://www.micrel.com/_PDF/Ethernet/datasheets/ksz8851snl_ds.pdf
    - http://www.marvell.com/transceivers/assets/Marvell-88E3016-Fast-Ethernet.pdf
  - #ping #python  实现 （抄来的）
    collapsed:: true
    - ```python
      #ICMPPing.py
      import socket
      import os
      import struct
      import time
      import select
      ICMP_ECHO_REQUEST = 8
      #生成校验和
      def checksum(str):
          csum = 0
          countTo = (len(str) / 2) * 2
          count = 0
          while count < countTo:
              thisVal = str[count + 1] * 256 + str[count]
              csum = csum + thisVal
              csum = csum & 0xffffffff
              count = count + 2
          if countTo < len(str):
              csum = csum + str[len(str) - 1].decode()
              csum = csum & 0xffffffff
          csum = (csum >> 16) + (csum & 0xffff)
          csum = csum + (csum >> 16)
          answer = ~csum
          answer = answer & 0xffff
          answer = answer >> 8 | (answer << 8 & 0xff00)
          return answer
      #接收一次Ping的返回消息
      def receiveOnePing(mySocket, ID, sequence, destAddr, timeout):
          timeLeft = timeout
          while 1:
              startedSelect = time.time()
              whatReady = select.select([mySocket], [], [], timeLeft)
              howLongInSelect = (time.time() - startedSelect)
              if whatReady[0] == []:  # Timeout
                  return None
              timeReceived = time.time()
              ########## Begin ##########
              recPacket, addr = mySocket.recvfrom(1024)
              header = recPacket[20:28]
              type, code, checksum, packetID, sequence = struct.unpack("!bbHHh", header)
              if type == 0 and packetID == ID:  # type should be 0
                  byte_in_double = struct.calcsize("!d")
                  timeSent = struct.unpack("!d", recPacket[28 : 28 + byte_in_double])[0]
                  delay = timeReceived - startedSelect
                  ttl = ord(struct.unpack("!c", recPacket[8:9])[0].decode())
                  return (delay, ttl, byte_in_double)
              ########## End ##########
              timeLeft = timeLeft - howLongInSelect
              if timeLeft <= 0:
                  return None
      #发送一次Ping数据包
      def sendOnePing(mySocket, ID, sequence, destAddr):
          # 头部构成： type (8), code (8), checksum (16), id (16), sequence (16)
          myChecksum = 0
          # Make a dummy header with a 0 checksum.
          # struct -- Interpret strings as packed binary data
          header = struct.pack("!bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, sequence)
          data = struct.pack("!d", time.time())
          # 计算头部和数据的校验和
          myChecksum = checksum(header + data)
          header = struct.pack("!bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, sequence)
          packet = header + data
          mySocket.sendto(packet, (destAddr, 1))  # AF_INET address must be tuple, not str
          # Both LISTS and TUPLES consist of a number of objects
          # which can be referenced by their position number within the object
      #向指定地址发送Ping消息
      def doOnePing(destAddr, ID, sequence, timeout):
          icmp = socket.getprotobyname("icmp")
          # 创建原始套接字
          mySocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
          sendOnePing(mySocket, ID, sequence, destAddr)
          delay = receiveOnePing(mySocket, ID, sequence, destAddr, timeout)
          mySocket.close()
          return delay
      #主函数Ping
      def ping(host, timeout=1):
          # timeout=1指: 如果1秒内没从服务器返回，客户端认为Ping或Pong丢失。
          dest = socket.gethostbyname(host)
          print("Pinging " + dest + " using Python:")
          print("")
          #每秒向服务器发送一次Ping请求
          myID = os.getpid() & 0xFFFF  # 返回进程ID
          loss = 0
          for i in range(4):
              result = doOnePing(dest, myID, i, timeout)
              if not result:
                  print("Request timed out.")
                  loss += 1
              else:
                  delay = int(result[0]*1000)
                  ttl = result[1]
                  bytes = result[2]
                  print("Received from " + dest + ": byte(s)=" + str(bytes) + " delay=" + str(delay) + "ms TTL=" + str(ttl))
              time.sleep(1)  # one second
          print("Packet: sent = " + str(4) + " received = " + str(4-loss) + " lost = " + str(loss))
          return
      ping("127.0.0.1")
      ```
    - Checksum 二进制反码求和
      - 方法:
        - 遇到进位舍去, 再加1, 直到不产生进位
        - ```cpp
           unsigned short checksum(unsigned short *buf, int length) {
               unsigned long sum;
               for(sum = 0; length > 0; length--) {
                   sum += *buf++;
                   sum = (sum>>16) + (sum&0xffff);
                   sum += (sum>>16);
               }
               return ~sum;
           }  // from https://article.itxueyuan.com/pBrplP
           ```
      - 证明 (refer to: https://note.sbwcwso.com/pages/1dd33b)
      - $[X]_{反} + [Y]_{反} = [X+Y]_{反}$
        - $X \ge 0 \& Y\ge 0$, 显然成立
        - $X * Y < 0$ 时, 原式变为 $[X]_{反} + [Y]_{反} = X + Y + 2^{n} - 1$
          - 当 $X+Y \le 0$, 此时 应该为 $[X]_{反} + [Y]_{反} = X + Y + 2^{n} - 1$, 与原式相同, 保持不变
          - 当 $X+Y \ge 0$, 此时 应该为 $[X]_{反} + [Y]_{反} = X + Y$, 此时原式溢出, 去掉最高位, 再加 $1$ 恢复.
        - 当 $X < 0 \& Y < 0$, 原式变为 $[X]_{反} + [Y]_{反} = X + 2^{n} - 1 + Y + 2^{n} - 1$, 原式溢出, 需要去掉最高位, 再加 $1$ 恢复.
      - Links
        - https://www.cnblogs.com/jcchan/p/10400504.html
          ```math
            - $[X]_{反} + [Y]_{反} = [X+Y]_{反}$
              - $X \ge 0 \& Y\ge 0$, 显然成立
              - $X * Y < 0$ 时, 原式变为 $[X]_{反} + [Y]_{反} = X + Y + 2^{n} - 1$
          - 当 $X+Y \le 0$, 此时 应该为 $[X]_{反} + [Y]_{反} = X + Y + 2^{n} - 1$, 与原式相同, 保持不变
          - 当 $X+Y \ge 0$, 此时 应该为 $[X]_{反} + [Y]_{反} = X + Y$, 此时原式溢出, 去掉最高位, 再加 $1$ 恢复.
              - 当 $X < 0 \& Y < 0$, 原式变为 $[X]_{反} + [Y]_{反} = X + 2^{n} - 1 + Y + 2^{n} - 1$, 原式溢出, 需要去掉最高位, 再加 $1$ 恢复.
          ```
  - [2020-01-15] 在查了三个小时的英文 Wikipedia 无果，科学上网 倒腾了4个小时无果，Github CLone 奇慢,  我只想说在国内查资料的门槛太高了...... In , 这个时代的主流技术, 下个时代的预备技术.
  - 网站为什么要做301跳转（永久重定向）
    source:: https://wz.a5.net/article/981.html
    collapsed:: true
    - 相比javascirp跳转、mete refresh跳转，php等动态语言reditect，301跳转对搜索引擎最友好，避免作弊嫌疑。
    - 301跳转能转移流量、权重。不会浪费在原url上的工作成果。
    - 解决网址规范化问题。如86722.com，[www.86722.com](http://www.86722.com/)实际返回都是主页内容，但他们却是不同的URL，对百度等搜索引擎来说不但是重复内容，更分散了权重,因此可用301转向到同一URL。
    - 原理
    - 根据HTTP协议，客户端向服务器发出请求，服务器返回数据应答头中状态码为301，表示永久转移到loction字段中的URL。
    - 301跳转（永久重定向）的实现
    - DNS服务器
    - 一般DNS服务器都提供URL转发功能，而且大部分用的就是301转发，如果虚拟主机服务器不支持301跳转、或者无法用程序实现时。可以使用域名服务器实现转发，DNS实现的301转发功能简单，只能实现域名、子目录等跳转,另外特别注意有的DNS服务器转发不一定是301，所以要检测一下。
    - WEB服务器
    - apache需要加载rewrite模块，然后在主机配置中或者在网站的.htaccess文件中写rewrite规则进行URL跳转设置。IIS同样可以加载rewrite模块，然后在httpd.ini文件中写rewrite规则。如果能够控制IIS服务器，可以选中要跳转的域名或目录，图形方式设置资源重定向。
    - 网站改版后导致URL方式改变了，老页面已不能访问了，新页面又没被收录，如果两个页面都保留的话，或许新页面就永远不会被收录了，因为内容重复了。这个时候就可以通过301跳转把老页面跳转到新的页面。
    - 两个域名绑定了同一个空间，两个域名都被搜索引擎收录了，而只想用其中一个域名。不然会内容复制的。可以用301跳转。
    - 在购买域名时，域名本身是不带有www的，由于在以前网站方都会增加一个"www"的子域名来帮助客户以更多的路径访问网站，客户会养成在网站前添加www来访问网站的习惯，所以如果没有做www域名解析的话客户输入www域名便不能访问，基于此，一些域名提供商会自动帮购买者做了这个"www"的解析，这样带"www"的和不带两个域名同时可以访问一个同样的内容。但是这样的话，会分散某个域名的流量与PR值，最好的解决方案是将所有访问用301跳转定向到某个域名下。
    - URL转发注意点：
    - url转发有两种方式，隐藏转发和（url转发后浏览器地址栏输入的网址不变）不隐藏转发（也叫显性转发：url转发后地址栏显示的地址为转发后的网址）。不管是隐藏转发还是不隐藏转发，根据不同的域名注册服务商，可能会返回不同的http header。有的会使服务器返回302状态码给搜索引擎，而不是301 http  状态码。有的是通过给浏览器窗口套用一个框架iframe的方式来实现隐藏转发，有的则是使用Javascript或Meta  Refresh来实现不隐藏方式的url转发，不一定是真正用到301重定向，所以，应该尽可能少用url转发功能
  - 伪造ip地址到底能否实现
    source:: https://segmentfault.com/q/1010000000162518
    collapsed:: true
    - 就我所知,真正的ip地址不能伪造,可是一些http header头是可以伪造的.以http_开头都可以伪造.有些程序会"多此一举"的判断客户端是否通过代理访问网站.以致于会有你说的 "伪造ip地址来刷票".伪造这个词应该是修改数据包，而不是使用代理。
    - TCP无法伪造IP，因为需要三次握手，比较安全；UDP可以伪造，但是由于伪造攻击很多，部分机房再路由上做了过滤，原地址不是机房的IP的数据包自动丢弃；不过很多监管不严的机房里还是可以伪造的；
    - IP地址伪造是可以发送但是不能回得来，因为在来的数据包的IP地址是伪造的请求的IP地址，自然数据包是收不到的，也就是说只能发送不能接收，上层的是TCP协议是面向连接的不能够伪造，UDP可以伪造。但是都是同样的只能发送不能收取，除非使用IP源路由协议，不过很多网络设备因为安全性考虑都禁用了。
    - 仅从协议上看应用是对真实的(被用作路由的) IP 无感知, 因为数据包在协议栈中上升到 TCP 层就已经把 IP 地址给剥除了,  更不用说最上层的 HTTP 协议了. 所以自以为取到数据包的 SourceIP 的其实都是从 HTTP 头中取出来的.  这个数据是可以被轻易篡改的.
    - 曾经做过刷票的功能，本来想找代理服务器来刷的，但是一时找不到大量的代理，所以就把电脑直连ADSL，通过java调用cmd执行网络连接、断开命令。每断开重连一次就获得一个新IP，当然有失败也有重复，但是10秒做一次成功率就比较高了。缺点是可能小区分配的IP段有限，同时速度比较慢
  - 企业带宽100M带宽要7万，可以用家庭宽带代替吗？
    source:: https://www.zhihu.com/question/331505875/answer/730117410
    collapsed:: true
    - 网工是做traffic engineering的。明明平均只有2，3Mb的宽带是怎么几乎随时随地都跑到100M甚至更多的。
    - 在这之前，还是建议把之前写的文章读一下，了解一下什么叫以太网。
    - 对于个人用户而言，你是不会一直用网的。你点开网页到点下一个网页之前，网络是空着的。虽然也有视频什么的吧，但你也不能一天到晚连着看不停息不是？所以如果把个人用户的带宽使用量画成图的话，大概是这样的
    - ![img](https://pic1.zhimg.com/50/v2-ceccf39e390d8fad9fd4d5452c0a0013_hd.jpg)
    - 高高低低，相差非常明显。但你和你的邻居不可能在完完全全同一时间都用网，所以在大量用户使用量叠加之后，再从1分钟到5分钟这个时间尺度上来看，带宽的使用量其实是一条相对平滑的曲线。（5分钟是国际惯例，不要嫌长）
    - ![img](https://pic2.zhimg.com/50/v2-7bfee99fd7274a0fc4be9529ed56d466_hd.jpg)
    - 而且正常来讲，每天的形状都差不多。峰值会在晚上8点到11点左右出现。所以只要保证实际使用的峰值和设备所能提供的最大带宽尚有一定的富余，就可以近似的认为下面用户几乎是随时随地可以满速度运行。反面教材是这样的
    - <img src="https://pic4.zhimg.com/80/v2-50fe5caed8c270c44b90972015b192bc_720w.jpg" alt="img"  />
    - 流量筑顶了，也就是这个节点的带宽爆了，一旦出现这样的情况就说明下面有人要遭殃了，具体表现就是丢包。丢谁的包，不知道。撞大运呗，谁运气不好就丢谁的。发生这样的情况之后TCP的拥塞控制开始起作用，TCP会自动降低速度，减少每次发包的数量，以避免发生丢包。一般来说家用宽带没有那么讲究，楼层/楼/小区的交换机爆个几秒几分的都是日常。所以测速的时候有一些抖动，无法稳定的达到线速，都有这方面的影响。这就叫BEST EFFORT。尽量不给你丢，丢了别怨我。为什么独享带宽的网络那么贵呢，因为有QoS，即使像这样有节点爆掉，也会优先保证独享带宽的包的传输，扔也先扔共享带宽的。你可以近似的认为独享带宽的宽带可以随时随地稳定的达到线速。但有的运营商鸡贼嘛。并不是所有的独享带宽都会给你上QoS的，有的时候只是保证你的带宽在接入层的交换机不爆，再往上爆不爆看你造化。所以会有真独享和假独享的说法。同样都叫独享带宽，价格也会差很多。
    - 那到底应该留多少富余呢？
    - 这就看运营商良心了。呃，不对，划掉划掉，这就是一门学问了。富余越多，节点爆掉的几率越低，下面体验越好，相对的成本也就越高。但富余高到一定程度之后，再增加对于下面体验的增加几乎没有帮助了。所以这个线具体划到哪各家不一样。所以都叫100M的宽带，各个运营商的价格不一样体验也不一样，毕竟成本也不一样嘛。
    - 另外呢，虽然流量波形每天都差不多，但把时间尺度拉到月/年这个水平上的时候，是可以看出来流量是在增长的。
    - ![img](https://pic2.zhimg.com/50/v2-0f9e18e1a0c1519c69ea792ff373714d_hd.jpg)
    - 所以需要周期性的扩容。一般来说负责任的运营商会划一条黄线，比如30%。超过这个黄线就开始计划对这个节点扩容，保证每个节点一直都有一定量的富余。如果运营商做的好呢，是可以做到下面用宽带的人想用的时候都能差不多满速跑。但你要真是一直跑，运营商是会生气的。
    - 最后说说昂贵的带宽实际大概每户能用多少，平均能给分多少。并不是每个人都要成天挂BT的，平均算下一个人确实用不了多少。这是辽宁省2018年8月的互联网报告。
    - http://lnca.miit.gov.cn/zxzx2/qtxx/201811/t20181109_3368843.html
    - 电信联通的网络间流量也就是115Gbps/45Gbps这个水平
    - ![img](https://pic3.zhimg.com/80/v2-a04727318ffe35eb4ca34ac9308c065a_720w.jpg)
    - 当然喽，总流量还要加上出国的流量和网内的流量。但数量级应该是差不多的量级。平均一个人贡献了多少自己估计一下呗？
    - 再举个大一点的例子？可以啊。
    - [HKIX](https://baike.baidu.com/item/%E9%A6%99%E6%B8%AF%E4%BA%92%E8%81%94%E7%BD%91%E4%BA%A4%E6%8D%A2%E4%B8%AD%E5%BF%83/22302699?fromtitle=HKIX&fromid=23551811&fr=aladdin)，亚太地区最大的互联网交换中心之一。
    - 2018年的峰值流量也就是1100Gbps多，世界杯决赛大概带来了300Gbps的波动。怎么样，数字也不是很大是不是？
    - ![img](https://pic4.zhimg.com/80/v2-897ac0568056270bfd75159793ec8882_720w.jpg)
    - 所以说真不是你3000个100M家用宽带就顶人家300G了，到了上游平均给你分一两个M那就照顾你了。毕竟按照现在的市价，运营商每个M零售的话不收你个几十元/月那是要赔死的。
    - 家用的是共享带宽。或者叫best effort。
    - 共享带宽和独享带宽有什么区别？都是100M宽带, 总共1000M给10个人分，叫独享带宽。总共1000M给11个人分，叫共享带宽。给100个人分呢？也叫共享带宽。给500个人分呢？还是共享带宽。具体多少人分呢？不好意思，企业机密。多少人分全凭运营商良心。要不怎么同样都叫100M宽带有的好用有的渣呢。一分钱一分货就是用在这里的。到底多少人分我没法告诉你，但我可以明确的告诉你：如果阿里100M一年7万的话，那要分差不多100户以上才能一年700的价格卖给你。实际上也差不多，100M的共享宽带平均一户分1M以上你差不多就可以烧高香了。你说那不对啊，我测速明明可以跑满速。那是因为在这一瞬间其他人用的不够多而已。
  - 3model
    collapsed:: true
    - a three-layer model for network design first proposed by [Cisco](https://en.wikipedia.org/wiki/Cisco).
    - ![https://community.fs.com/blog/how-to-choose-the-right-distribution-switch.html](https://media.fs.com/images/community/upload/kindEditor/202105/25/distribution-layer-diagram-1621937301-ES7wiU19cL.jpg){:height 408, :width 778}
      - ### Core 核心层
        - 为进出数据中心的包提供高速的转发
      - ### Distribution / Aggregation 汇聚层
        - 连接接入交换机，同时提供其他的服务；
        - 例如：防火墙，SSL Offload，入侵检测，网络分析等
      - ### Access layer 接入层
        - ToR（Top of Rack）交换机；
        -
      - Khalid Raza, Mark Turner (2002), *Cisco Network Topology and Design*, Cisco Press
      - [网络三层架构 - yipianchuyun - 博客园](https://www.cnblogs.com/yipianchuyun/p/13842297.html)
    -
      -
-
-