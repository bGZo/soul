icon:: 💾
author:: 时国怀
created:: [[20240727]]
exclude-from-graph-view:: true
source:: https://www.zhihu.com/question/20186057/answer/15893951
type:: archives-web

- https://www.zhihu.com/question/20186057/answer/15893951)
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