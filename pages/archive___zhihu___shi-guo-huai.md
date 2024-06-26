title:: archive/zhihu/shi-guo-huai
description:: 时国怀
source:: [时国怀 - 知乎](https://www.zhihu.com/people/shi-guo-huai)
collapsed:: true

  - [有些人现在起就一辈子不会见了 想到这会不会就有莫名得悲伤？](https://www.zhihu.com/question/22375641/answer/21160254)
    collapsed:: true
    - 世界上任何两个人，最后无非两个结果：生离，或者死别。
    - 就算两个人一直在一起，死亡这一关也是过不去的。
    - 人生有太多的无奈，离别是其中的一个。
  - [破解一个加密 zip 文件要多久？](https://www.zhihu.com/question/23728226/answer/25530432)
    collapsed:: true
    - 做过AES加密，隐约记得AES-256的处理速度好像是10MB/s，假设破解ZIP文件需要读一个扇区的数据，那么一秒能处理20480个扇区，24小时一共能处理:
    - 20480*3600*24=1769472000 = 1.769472e+9
    - 按照你说的组合：假设只包括大小写和数字，一共是62个字符，9位的总组合数是：
    - 62^9 = 13537086546263552 = 1.3537086546263552e+16
    - 数量级差了7个，就算处理速度提高1000倍，还需要1万天左右才能破解，所以，放弃吧。
    - 另外，我不清楚如果用硬件加速计算以后会怎么样，我的时间是按照CPU时间算的。
    - 补充，我自己测试的结果：基于openssl 1.0.1g的AES-256-ECB，外层封装XTS算法，
    - **每512字节换一次key**
    - ，16字节为一组，一秒钟处理数据约40MB/s，C语言代码，gcc编译，运行环境debian，CPU是I7-3770，主频3.4G，单线程，无硬件优化。
    - 我这个配置算是很高的配置，如果用显卡加速，加上各种优化，多线程一起跑，速度应该能提高1-2个数量级，但我觉得每秒处理速度要超过1GB还是有困难的，那么一秒钟能跑200万个密码，如果跑字典的话，这个速度足够了，但就看题主自己的密码有多复杂了，万一字典里没有，那就没办法了。
    - 另外，有人说的用CRC校验，是个不错的思路。
  - [为什么路由器没有实体重启按键？](https://www.zhihu.com/question/24010785/answer/26380915)
    collapsed:: true
    - 路由器为什么需要重启键？不需要，所以没有。
    - 过去的电脑上还有强制重启的按钮，现在都没有了，为什么？因为不需要。
    - 一个设备需要重启，是因为：
    - 1、它死机了，没有响应了。
    - 2、它的软件不支持重启，必须由硬件提供重启按钮。
    - 对于路由器来说，如果遇到第一种情况，直接拔电源即可；遇到第二种情况，路由器支持软重启。
    - 为什么个人电脑需要有重启键（当然，实际情况是重启键越来越少）？ 因为：早期DOS时代是没有重启的命令的，必须由硬件提供（也就是前面的第二条）。
    - 现代PC因为运行时有数据读写，直接拔电源可能会对存储设备造成损坏，所以大多数情况下PC是不推荐拔电源来重启的。而路由器运行过程中几乎没有向存储设备写数据的动作，所以直接拔电源对于路由器来说几乎没有伤害，所以路由器没有必要再设计一个“额外”的功能了，硬件设计上，能省一点是一点。路由器、交换机、网络服务器等设备，在设计的时候通常认为它是长期运行的设备，所以，这些设备一般都没有重启键，比如Windows Server版重启操作很麻烦，因为这类设备设计之初，就认为是要长期运行的。
  - [为什么 IP 有归属地概念，像 8.8.8.8 这样的 IP 是买的吗？](https://www.zhihu.com/question/24286996/answer/27297641)
    collapsed:: true
    - 先来介绍几个概念：
    - IANA： Internet Assigned Numbers Authority (IANA)，互联网数字分配机构，负责管理，分配IP地址（[Internet Assigned Numbers Authority](http://www.iana.org/)）。同时还负责AS号（自治域编号）等分配。IANA的管理机构是ICANN(ICANN, The Internet Corporation for Assigned Names and Numbers,互联网名称与数字地址分配机构，官网：
    - [ICANN](https://www.icann.org/))
    - APNIC：亚太互联网络信息中心 （Asia-Pacific Network Information Centre，APNIC），官网：[APNIC - Home](http://www.apnic.net/)，负责亚洲地区的地址分配。
    - 然后再说具体的流程：
    - IP地址都是向以上机构申请的，但不好意思，IPv4地址已经申请完了，申请的流程那些网站上都有。
    - **IP地址只有所有权，不存在真正的归属地，归属地都是运营商（指**
    - **网络运营商**
    - **，下同）决定的，理论上说一个地址可以用在全球任何地方。**
    - 比如，某IP地址属于美国某公司，但这个公司在中国开了一个分公司，那么这个分公司也可以用这个地址。
    - 那么IP地址的归属地查询是怎么来的呢？
    - 因为拥有IP地址只是第一步，有了IP地址以后还要运营商认可这个地址并将地址信息广播给互联网，告诉互联网（内外网都算）如何到达这个IP地址——也就是路由。而
    - **这个IP地址使用者的接入运营商决定了这个地址在哪**，所以才有了归属地的概念。
    - 比如北京的某个用户，要访问服务器位于上海的一个网站，通过DNS域名解析获得IP地址，当这个用户要发送网页请求的时候，先要知道如何才能到达目标IP地址，这个时候，运营商的路由器知道怎么到达目标地址，所以用户请求经过网络转发才能到达目的。当然，前提是**运营商认可这个地址是存在的**
    - 所以，当拥有IP地址以后第二步就是，让运营商知道这个地址在这里，方法有：
    - **1、自己成为一个运营商，并且与其它运营商连接起来，被其它运营商认可。**
    - **2、向运营商付钱，在运营商的网络里设置上这条路径（承认这个地址在这里存在）。**
    - 运营商之间（当然，前提是互相认可的运营商），**通常都会无条件的学习对方的全部公开的路由**（过程参考BGP协议，展开说较复杂），所以，只要向一个公共的运营商付钱并设置上路由，那么理论上全球大部分地方都最终会学习到这条路由的，也就是说全球的大部分用户都会知道怎么到达这个IP地址。通常，如果这么干，**一般都是向接入的运营商付钱**
    - 。
    - 所以，要想获得IP地址靓号，先要知道这个地址是属于谁的，到IANA网站上可查到。然后联系对方，购买这个地址（或者地址段）的所有权。最后，向运营商付钱，或者自己成为一个运营商，把这个地址通告出去。
    - 理论上说，只要有钱，肯定能办成，但实际上不好说。因为在国内，要让运营商干这种事情，恐怕还不仅仅是钱的问题。
    - 此外，买卖地址是要花钱的，这个钱跟买卖域名一样，完全是想要多少就可能是多少的。同时，拿到所有权以后，
    - **还要定期向IANA支付管理费才行**，不然这个地址还是会被收回去的。
    - 对了，附上怎么查IP地址属于谁：
    - 在这个页面里：
    - [IANA — Number Resources](http://www.iana.org/numbers)
    - 可以看到有好多IP地址管理机构的连接，随便点进去一个，一般都会有一个叫做whois的查询的地方，APNIC的是这个：
    - [APNIC - Query the APNIC Whois Database](http://wq.apnic.net/apnic-bin/whois.pl)
    - 输入一个要查询的地址，比如22.22.22.22，点查询会给出一些信息，有时候信息不全，要求你到别 的地址管理机构的网站去查，那就说明这个地址不在这里管辖，按照说明去别的地方找就是了。
    - 再说这个22.22.22.22，查询的内容如下：
    - `NetRange: 22.0.0.0 - 22.255.255.255 CIDR: 22.0.0.0/8 OriginAS: NetName: DNIC-SNET-022 NetHandle: NET-22-0-0-0-1 Parent: NetType: Direct Allocation Ref: http://whois.arin.net/rest/net/NET-22-0-0-0-1 `
    - `OrgName: DoD Network Information Center OrgId: DNIC Address: 3990 E. Broad Street City: Columbus StateProv: OH PostalCode: 43218 Country: US RegDate: Updated: 2011-08-17 Ref: http://whois.arin.net/rest/org/DNIC `
    - 主要的信息包括：地址范围，申请类型，归哪管（这个地址归ARIN，北美的地址），OrgName就是所有者信息了，包括地址什么的，到ARIN去查有时候会有更多信息，后面还有电话，我就不列了。
    - 如果题主向申请地址靓号，按照上面步骤去做就可以了，至于如何打通运营商，只能说，祝你好运了……
    - 前面说了个AS号，后面忘记补充了，所有的运营商都是有AS号的，这个号码范围是0-65535，有一些号码被保留，AS是自治域的意思，因为全世界的网络实在太大了，如果每个路由器都记录所有网络的路由信息，那么
    - 路由表
    - 会非常恐怖，即使是核心路由器也负担不起，解决的方法就是把全球网络划分为若干个自治域，每个自治域之间只关注如何到达对方的边界，而不关心对方内部的网络情况，这样一来路由器的负担会小一些，这是BGP协议所确定的，因为自治域要有一个名字，所以就用了一个编号，就是AS号，比如
    - 中国电信
    - 的编号是4134，这是全球唯一的。有些虚拟主机的网站所说的BGP机房就是说这个网络本身是一个独立的自治域，有自己的AS号，可以在路由选路上有一定优势（实际情况未必）。
    - AS号跟IP地址什么关系呢？如果能申请到一个独立的AS号，就可以自己做运营商，再花点钱把自己的网络跟别的运营商连起来，就可以广播自己的IP地址范围和路由了。当然，成本非常的高。
  - [把系统盘里的所有东西都复制到 U 盘里，是否可以变成系统盘？](https://www.zhihu.com/question/22641275/answer/27214049)
    collapsed:: true
    - 刚好家里有台闲置的台式机正在装系统，所以实际做了个实验：
    - 硬件配置：
    - CPU：Intel I5 760
    - 主板：
    - 华硕P7P55D
    - 显卡：技嘉GV-N610-1GI
    - 主硬盘：金士顿(Kingston)V300 120G
    - 内存：金士顿4G*2
    - 其它配置略
    - 已经装好了WIN7的系统，手头有一个320G的移动硬盘，用ghost方式把整个C盘克隆到移动硬盘上，设置好MBR，确认WIN7使用MBR方式启动，然后，重启。
    - 开机的时候，一开始确实看到了Windows的开机画面，但很快，就看到了这个：
    - 其实我之前分析的时候就想到了这个结果，做实验只是为了验证结果，符合预期。
    - 然后开始讲讲为什么会这样，以下是技术分析，对技术不感兴趣的可以跳过：
    - Windows启动的时候实际上分几个阶段进行的，boot阶段的时候并不是完全运行在保护模式下，从Windows泄露的代码上看boot阶段会在实模式和保护模式下来回切换几次，因为此时没有磁盘驱动，Windows需要使用int13h中断来读磁盘，当把主要的驱动都载入完以后，bootloader会把控制权交给Windows内核(NTOSKRNL.EXE)，内核把通过bootloader载入的驱动都加载起来，开始进行后续的操作，而这个蓝屏就是死在这个位置上。
    - bootloader需要加载开机必要的驱动，这个“**必要**”二字是很重要的，如果bootloader加载全部驱动，那么负担太重，如果什么都不加载，那么内核很难运行（Windows不是宏内核结构，算是混合内核，内核文件不包括主要的驱动），所以Windows才有“最后一次正确配置”的说法，这个配置就是保存在注册表里的，bootloader通过访问注册表决定载入哪些驱动。一个安装在硬盘的Windows，最后一次正确的配置是，
    - **通过IDE或者SATA控制器驱动来加载后续的文件**
    - ，但一个基于USB运行的Windows需要的是
    - **通过USB控制器和U盘驱动来加载后续的文件**
    - ，但bootloader并不知道这一点，所以当把Windows移动到U盘上的时候，bootloader需要的配置并没有改变，所以
    - **当bootloader交出控制权的时候，Windows的内核没办法访问磁盘，于是就挂了**
    - 。
    - =====================操作系统的分割线=====================
    - 关于Linux是否能这么做，我并不看好，可以确定的是
    - 内核镜像
    - 能正确加载，但剩下的模块是否能加载就不好说了，Linux里硬盘是hda/sda这些设备名，但USB好像不是这样的，各个路径能否正确挂载我觉得是一个疑问，有时间我会补充我Linux的实验，但折腾整个太麻烦了。
    - MacOS我没有条件，估计需要用黑苹果了，手头没有条件。但是我认为同样困难很多。
    - =====================总结的分割线=====================
    - 我认为大部分个人操作系统要这么做都很困难，原因是配置文件，大部分
    - 操作系统
    - 都需要保存上次的硬件配置，以备下次启动使用，而把操作系统从硬盘移动到U盘上，不仅仅是设备的变化，还包括加载这些设备的行为都发生的变化，SATA/IDE驱动和USB驱动可完全不是一回事，除非更改配置文件。
    - =====================补充的分割线=====================
    - Windows8有
    - WIN8 to go
    - ，允许装到U盘上，但本质上说这是一个工具，而不是直接把Windows8复制到U盘上，所以这是有区别的，WIN8 to go实际上是通过写入正确的配置（比如在启动阶段加载USB驱动）的方法来加载系统，跟直接复制C盘数据有本质区别。
    - 补充一些其它的内容：
    - MBR和UEFI方式有很大区别，有些BIOS里可以设置，UEFI需要面对的困难更多。
    - WIN7开始有时候会单独创建新分区放bootloader和boot menu，如果是这样的话需要把这个分区也复制过去，否则是起不来的。
    - 所谓的“复制”，应该是用ghost等软件克隆，直接复制是不可能的，并且由于权限的问题不是所有文件都会被正确复制。
    - Linux需要grub等内容一起复制过去。
    - U盘要足够大，最好用移动硬盘（Windows里移动硬盘和U盘使用不同的上层驱动）。
    - 能想到的就这么多。
    - 最后，反对一下大部分回答，
    - **题主问的是直接复制**
    - ，Windows直接复制肯定是不行的。
    - =====================Linux实现结果的分割线=====================
    - 实验过程如下：
    - 先在SSD上安装上Linux，版本是ubuntu 11.04，确认安装启动正常。
    - 重启，用克隆软件disk to disk方式克隆磁盘到移动硬盘上，重启，禁用SSD主硬盘。
    - 开机。
    - 嗯？黑屏？啥情况？？？
    - 多试了几次，还是黑屏。
    - 好吧，使用工具修复以下MBR，重启，还是黑屏？？
    - 好吧，动用神器，扇区对拷，把SSD上前0x100000字节复制到移动硬盘上。
    - 重启，哎，有东西了，不过，不是你们想要的：
    - 并且，键盘不能用（USB键盘），别的没试反正卡在这里也是不动了。
    - 实验到此为止。
    - 结论：直接复制（硬盘对拷）不管是Windows还是Linux都是不行的，建议有条件的试试MacOS再做结论。我只相信实验数据。
    - **另外，不要再强调USB boot这类东西了，题主问的不是这种情况，U盘启动系统的方法很多，不用各位提醒我也是知道的**
  - [计算机专业毕业只能从事 IT 行业么？](https://www.zhihu.com/question/24329504/answer/27437649)
    collapsed:: true
    - 1、IT行业不等于敲代码。
    - 2、计算机毕业的人有很多不从事IT行业。
    - IT行业还包括IT企业的销售、售后、运维、测试等职位，这些职位大部分都不怎么敲代码。再广义一点的IT行业还包括非IT企业（比如银行、医院等等）的IT支撑部门。
    - 我是计算机专业毕业的，本科，985+211学校，学校还算可以，但我们班级毕业27人毕业的时候完全从事编码的不到1/3，2007年毕业到现在，还在做一线开发的，应该不超过5个人的样子。所以计算机专业毕业的人真正敲代码的其实很少。27人里还在广义IT行业的（包括银行这种），大概有一半多一点，剩下的人则完全跟IT行业无关。
    - 这些人包括：医药销售代表、高校行政人员、公务员、事业单位从业人员、继承家族企业、军队等岗位。
    - 而且，这个时代要完全跟IT行业保持距离的话其实很困难的，所以在广义的IT行业里做点事情的话，加上自己的计算机专业背景也许更容易发展。
    - 至于是否上培训机构，这个看你自己的选择，一个稍微差不多的码农的收入还是高于很多行业的，所以是选择自己喜欢的，还是选择挣钱多一点的（但要考虑好你自己能否成为合格的码农），选择权在你自己手里。
    - 有句话送给题主：不要让自己后悔自己的选择。
  - [为什么用通用串行总线（USB）设备复制文件的速度远低于理论值？](https://www.zhihu.com/question/20186057/answer/15893951)
    collapsed:: true
    - 我就是做USB驱动的，U盘驱动也做过，控制器驱动也做过，我来解释一下速度的问题：
    - 首先实际速度肯定低于理论速度，比如百兆以太网，能到10MB/s的速度就不错了，但是为什么USB差距这么大，主要是USB传输的无用包实在是太多了。
    - 对于USB2.0，480Mbps是指总线的频率，也就说，总线信号每秒最多能传输这么多bit，这些信号包括控制信号和数据信号，现在来看看那数据信号都有什么：
    - 每125us就有一个micro frame（微帧），每1ms还有一个frame，在USB规范里叫SOF，类似于一种同步信号。
    - **标准USB传输过程：**
    - in/out token，data0/1，ack，真正有效的数据就在data0/1里，如果一个data包放不下，那么会放到多个data里。
    - 传输之前，对于2.0设备还要发起一个ping请求，确认设备是活着的。
    - USB不是一个全双工设备，通常的行为是这样：总线空闲，主机端请求数据，总线空闲，设备回应，总线空闲，主机准备接受数据，总线开始传输，传输完成总线空闲，主机检查数据无误，给设备回应说数据传输正常结束（不需要重传）。
    - **对于U盘本身：**
    - 由于U盘规范的原因，大多数操作系统要求定期检查U盘状态（是否是alive的），这个请求叫做test unit ready（各个OS都有，大家就不要吵了，U盘规范上的）。
    - 同时传输512字节（一个扇区的数据）要包括命令标识，命令号，LBN（逻辑块地址）以及乱七八糟一堆堆的东西，一个扇区
    - 大概需要将近600字节的数据。同时主机端还要给予相应的回应。
    - 至于前面有人说bulk传输不会占满带宽，这也不是完全对的，确实USB传输分为interrupt传输，bulk传输，ISO传输，但是只有interrupt预留了很少，ISO会保留30%左右，但当没有ISO传输存在的时候，bulk是可以占掉这一部分的。
    - USB2.0规范里给了一个公式，算传输时间的（算法解释就太复杂了，见USB2.0 5.11.3 Calculating Bus Transaction Times）：
    - **High-speed (Input)：**
    - **Non-Isochronous Transfer (Handshake Included)**
    - **= (55 * 8 * 2.083) + (2.083 * Floor(3.167 + BitStuffTime(Data_bc))) + Host_Delay**
    - BitStuffTime(Data_bc) 这部分就是数据传输需要的时间，算起来麻烦，但是看到前面有一个2.083就能看出来，传输一个bit基本上需要2.083倍的时间，所以，简单的把480Mbps除以2.083，再转换成字节大概是：28.8MB/s，也就是说，最多就这么快，再刨除bulk-only模式里的那一堆堆的多余指令：一个包需要16个字节左右，Windows一次请求是4KB（可能是为了页对齐），再浪费掉1%左右的时间，以及host delay，也就是主机的校验延迟，那么实际速度就20多MB/s，不管是读还是写。
    - 但是我知道肯定有人说，测得的实际速度比这个快，当然了，我也见过比这个快的，为什么？恰好我做过Windows里文件系统开发，也研究过Linux里的fat驱动，先说Linux，它很变态，你的写操作不一定真正写到磁盘上（证据我有，因为我有USB分析仪，能抓总线传输），Linux会在后台慢慢的写，前台看上去已经写进去。
    - Windows比Linux强一些，但是基于强大的预读和缓存，Windows也不是实时读写，所以会看到数字有跳动的情况（Windows内核里cc开头的函数就是干这个的）。
    - 我们开发产品的过程中，看到过的最高总线利用率也就是80%左右（分析仪获得的总线数据），也就是说28MB的速度可能还要打个八折，崩溃去吧。
    - 另外，U盘（flash介质）会更慢一些，因为U盘本身写的就慢，SSD和硬盘会好些，虽然SSD也是flash，但是SSD缓存大，并且有保障机制。
    - 所以，作为一个USB驱动的开发人员（维护过EHCI驱动，改过U盘驱动，写过鼠标、FTDI串口驱动，改过USBD），我觉得U盘的速度是很坑爹的。
    - 解释完了。
  - [在 Windows 下键入 Enter 键，是在键盘缓冲区中存入 '\n' 还是 '\r''\n' 两个？](https://www.zhihu.com/question/24639606/answer/28476223)
    collapsed:: true
    - 首先，题主要说明这个键盘缓冲区是指什么呢？
    - 以一个USB键盘为例，从USB的请求开始到最终窗口收到消息，中间有好几层缓冲区，每层都不太一样。
    - USB驱动一层有缓冲区，这里保存的都是扫描码，不区分换行符。
    - 如果是使用directX的directIO进行按键输入管理，那么这一层就可以直接把按键信息拿走，有些游戏（比如LOL）就是这么做的。
    - 所有键盘消息最终都发送到Windows键盘的一个统一驱动里叫 kbdclass.sys ，这个驱动负责统一翻译、处理、管理所有键盘以及消息。这一层，应该还是扫描码。
    - 之后，这个消息就通过内核到用户态了。
    - 在用户态里，进程csrss.exe有一个线程win32k!RawInputThread负责处理按键，广播按键消息。此时扫描码变成按键（包括区域符号转化）是"\n"
    - csrss.exe调用DispatchMessage等函数分发消息给各个窗口、线程等。
    - 各个窗口收到按键消息，此时仍然是"\n".
    - 部分窗口会根据按键消息做文本转换，转换完以后，看到的才是"\r\n".
    - 对于命令行的C语言，由Windows的POSIX子系统或者其它模块负责接收按键消息，在LibC一层通过stdio/stdlib这些库转化成"\r\n".
    - 所以，如果你操作的内容位于文本框（以及其它Windows文本环境）、命令行的LibC环境（包括但不限于stdio、iostream库），那么收到的应该是"\r\n"，其它情况，比如Windows按键消息等，多数收到的都是"\n"
    - 当然，如果在MS开发环境下，真正到具体使用中的时候，还是分很多情况的：比如字符串"\n"在以非binary方式写入文件的时候，是"\r\n"，在以binary写入文件的时候，是"\n"，getchar返回的是"\n"，但不是绝对的，要根据你输入的数据流决定，有时候，如果输入的数据流是文件，而非键盘控制台，那么文件里的"\r\n"到了你的函数里，就变成了"\n"。所以，一个字符流可能保存在内存里的时候是"\r\n"，但你getchar得到的是"\n"，写到文件里却是"\r\n"。
    - 所以，只能说，用实践去尝试，尤其做开发，甚至会出现不同的开发环境里返回值不同的情况。如果非要做严格检查，建议同时检查"\r\n", "\n\r", "\n", "\r"
    - 另附上Windows按键消息的处理流程：
    - 一个按键的消息产生流程如下：
    - 1)硬件中断/硬件端口数据
    - //WinIO能模拟，或者修改IDT是在这一层
    - 2)
    - 键盘Por
    - t驱动（USB or PS/2）
    - //Filter驱动在此
    - //DirectIO在此
    - //KeyboardClassServiceCallback也在这一层被调用
    - 3)kbdclass驱动
    - //处理键盘布局和键盘语言，部分高端的病毒也工作在这里
    - 4)Windows
    - 内核边界
    - （zwCreate/zwReadFile）
    - ----------------------（系统调用）----------------------
    - 5)Windows内核边界（zwCreate/zwReadFile）
    - 6)csrss.exe的win32k!RawInputThread读取，完成scancode和vk的转换
    - //SetWindowHook工作在这里（全局）
    - //kbd_event工作在这里
    - 7)csrss.exe调用DispatchMessage等函数分发消息
    - //SetWindowHook工作在这里（进程）
    - //PostMessage和SendMessage在这里
    - 8)各个进程处理消息
    - 9)子系统、LibC、文本框、输入法转换按键到最终字符（符号）
    - 另外，评论里有人问为什么Windows设计的这么复杂，这是一个历史问题，Windows不是一次设计完的，历经30多年的变迁积累了很多东西，其中一个特点就是vk（虚拟按键？），这是一个DWORD（32bit）类型的数据，用来描述各种键盘状态，因为一个面向事件的系统就必须要能处理各种按键的弹起、落下、组合键，而如果考虑到各种地区的键盘布局（比如欧洲地区的键盘布局），这种键位组合数量庞大，所以才用DWORD表示。而后来软件又希望提供directIO以及各种hook请求，就慢慢演变成如今这种这么复杂的东西。
  - [Windows账户名字中文与英文的区别？](https://www.zhihu.com/question/24573983/answer/28257817)
    collapsed:: true
    - 展开说太复杂了，题主应该是非计算机专业的，理解起来也有困难，简单的说就是这个软件的设计者在设计的时候没有考虑支持中文环境。
    - 题主应该知道，计算机里的路径都是一串字符，那么这个字符串，如果是纯英文的，那么几乎在任何版本任何语言的Windows环境中，都是相同的。
    - 比如一个路径：
    - "C:\User\Admin\Doc\1.doc"
    - 不管在任何语言的Windows环境里，都是一样的。
    - 但如果包含中文、日文、韩文等一些非英语字符，那么不同版本里可能就完全不同，当然这个要根据软件设计者的开发环境确定，一种情况是：
    - 你的路径：
    - "C:\User\用户\Doc\1.doc"
    - 在软件看来是：
    - "C:\User\??\Doc\1.doc"
    - 显然，这是无法正常访问的。
    - 有些软件需要使用临时文件，临时文件夹一般默认是（WIN7环境）：
    - C:\Users\
    - 用户名
    - \AppData\Local\Temp
    - 如果你的用户名是中文，那么有些软件得到的临时文件夹名字就是：
    - C:\\Users\\xxx\\AppData\\Local\\Temp
    - 显然这个路径是错误的。
    - 这是因为软件无法正确支持中文的缘故，至于为什么不能正确支持，这涉及的东西比较多，因为历史上各个国家的编码有各自的规范，后来才统一的，但即使统一以后，还有很多软件不支持统一以后的规范，这就造成了有些软件无法跨语言使用。
  - [为什么文件由GBK转成UTF-8后文件大小变大了很多？](https://www.zhihu.com/question/24813398/answer/29068630)
    collapsed:: true
    - 谢邀。
    - GBK编码中，**通常情况下（特别强调是通常情况）**，1个英文字母占1个字节，1个汉字占2字节，
    - UTF-8编码中，通常情况下，1个英文字母占1个字节，1个汉字占3个字节。
    - 所以变大了，因为汉字需要更多的存储空间。
  - [为何感觉电脑或者安卓手机内存越大，占内存更多呢？](https://www.zhihu.com/question/24935892/answer/29551098)
    collapsed:: true
    - 谢邀。
    - 确实是内存越大，占用的内存越多，这里指总数而不是指比例。以下讨论仅限于Windows环境。
    - 比如同样的系统，你装1GB内存，开机以后不开任何东西看到的内存使用总量，再装2GB内存，开机以后不开任何东西，看到的内存使用总量肯定是2GB的比1GB的要多。
    - 原因有：
    - 1、管理内存本身需要占用内存，更术语一点是因为页表也要占内存。内存中通常以4KB字节为单位划分内存页，内存页是操作系统最小的内存管理单元。操作系统需要管理内存页，那么就需要给所有内存页建立索引来描述其状态，所以当内存总数增多的时候，内存页的索引项必然也增多，因为索引也是在内存里的，所以使用的内存必然要多一些，这是其一，但这不是大头。
    - 2、操作系统的很多驱动会根据内存规模动态的决定要使用多大内存，以FAT文件系统驱动为例，它会根据当前操作系统的内存总数决定延迟关闭的文件总数，内存小的时候，延迟关闭的文件总数是16个，内存多的时候是256个。微软提供了一个API是MmQuerySystemSize专门用于查询系统内存规模。多数驱动程序都会根据这个API返回值来动态增长缓存规模，所以内存越大，被占用的内存越多，这是正常的。
    - 需要说明的是，这是一种好事，因为缓存多，速度通常更快。
  - [OTG与micro USB是否是一回事？](https://www.zhihu.com/question/24981100/answer/29715197)
    collapsed:: true
    - OTG（全名USB-OTG）是功能的名称，我们可以说XXX接口支持OTG功能（参见[USB On-The-Go](http://zh.wikipedia.org/wiki/OTG)），具体是否是支持是硬件行为。
    - Micro USB是接口名称，是特指这种形状的接口（参见[micro USB_百度百科](http://baike.baidu.com/view/1851541.htm?fr=aladdin)）
    - Micro USB接口实际上分为Micro-B和Micro-AB两种，Micro USB接口最早确实是为OTG功能设计的，但使用了这种设计的接口也可以不支持OTG，对此USB-IF没有严格规定，看厂商的意愿。
    - 如果有人用Mini USB口实现了OTG功能，也是可以的。当然，如果愿意，也可以设计出一个USB接口但实际上是一条网线，形状，跟功能不是一回事。
  - [设计一个物理接口要考虑哪些方面？](https://www.zhihu.com/question/24871270/answer/29566471)
    collapsed:: true
    - 我来随便说说吧：
    - 接口是用来连接设备并传输信息的，所以接口设计的最重要原则是如何可靠、高效的传输信息，所以在很长的一段时间里，接口用着是否方便并不是一个最重要的。
    - 以外部接口为例，从早年的串口(COM口，PS/2接口)，到后来的并口(PRN口)、VGA口，再后来的电话线、网线口，再后来的USB、1394，到今天的像eSATA这些，接口改变的最主要目的是提升速度，然后才有易用性的考虑。尤其是USB接口，最早就不是给可移动设备使用的，只不过后来人们发现这东西可以接插即用以后，才有了今天这么多的USB设备。
    - 对于可移动设备，接口曾经一度没有规范可言，不知道多少人记得诺基亚手机的数据线，这就完全是一种厂商自己设计的接口，不属于任何标准接口。
    - 直到后来，移动设备多起来了，人们才考虑要统一接口，并且考虑接口的易用性。
    - 对于任何一个制定技术规范的组织来说，接口先要考虑的是传输速度和可靠性（比如最大传输距离、误码率等等），我相信任何用户在购买设备的时候，优先考虑的一个指标也是设备速度。当速度已经差不多满足用户需求的时候，易用性才会列入技术规范的考虑范围。当然，也有例外，比如像苹果公司这种，把用户体验放在第一位，但这种公司实在是太少了，并且必须要有足够的技术储备才能做到这一点，当然这也是后来才有的，苹果的老接口也设计的很糟糕。
    - 为什么双面可插的USB才出来，因为用户体验不重要，就这么简单。只有当速度提升出现瓶颈的时候，用户体验才需要被考虑。