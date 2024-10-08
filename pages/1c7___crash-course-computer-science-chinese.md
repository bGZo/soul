icon:: 📦
created::  [[20230324]]
exclude-from-graph-view:: true
type:: github/repo
tags:: #computer-science #tutorial 
source:: {{gh 1c7/crash-course-computer-science-chinese}}

- [CSAPP+SICP - 知乎](https://www.zhihu.com/column/c_1212802114247979008)
- Coursera镜像网站：[https://www.mooc.cn](https://www.mooc.cn)
- ## Content
  - 计算机早期历史
    id:: 6331a08f-14fb-483b-ab89-e92add5bc9ea
    - M(Mega)B
    - G(Giga)B
    - ASKII：7位
    - Mojibake
    - 不同编码方式1个英文字母占的字节是不同的：
      - ASCII
        - 一个英文字母（不分大小写）占一个字节的空间，一个中文汉字占两个字节的空间。
      - UTF-8
        - 一个英文字符等于一个字节，一个中文（含繁体）等于三个字节。中文标点占三个字节，英文标点占一个字节。
      - Unicode
        - 一个英文等于两个字节，一个中文（含繁体）等于两个字节。中文标点占两个字节，英文标点占两个字节。
        - Unicode：16
    - 计算机算术逻辑单元 ALU（Arithmetic And Logic Unit）
    - Random Access Memory
    - Static Random Access Memory
    - DRAM
    - NVRAM
    - 闪存
    - 时常困扰我的一个问题是1M到底有多大？1M到底有多小？这里作为我初入计算机这个坑的导线。
      - $$1M(B)=1024K(B)$$
      - $$1K(B)=1024B(字节)$$
      - $$1B(字节)=8位(Bit)$$
      - 往上则分别有`GB`、`TB`、`PB`、`EB`、`ZB`、`YB`、`BB`、`NB`、`DB`
  - 电子计算机
    description:: "涉及的设备：继电器、真空管、晶体管"
    - **继电器（relay）**: 用电控制的机械开关
      - 1937年最大的机电计算机之一是哈佛的马克(Mark)一号，是IBM在1944年给二战同盟国建造的。该机器的大脑是由继电器（relay）构成的，存在大约3500个继电器。
      - **原理:** 通过产生磁场来闭合开关形成通路
      - **性能:** 1940年一个好的继电器一秒最多50开关次. 哈佛马克一号1秒能做3次加减法运算，一次乘法需要6秒，除法需要15秒，三角函数需要一分钟以上。
      - **缺点:** 无法快速开关。哈佛马克一号平均每天需要更换一个故障继电器。
    - **真空管/电子管（Thermionic valve）**
      - 1904年，英国物理学家John Ambrose Fleming -> 新的电子组件——热电子管（Thermionic valve）
      - **原理:** 气密的真空玻璃灯泡中一个电极A可以加热，从而发射电子，称为**热电子发射（Thermionic emission）**；另一个电极**B会吸引电子，来形成电流**。但**只有当电极B带正电时才能吸引电子，否则当电极B带负电荷或者中性电荷时，电子就无法跨越真空区域**。
      - 1906年，美国发明家Lee de Forest在此基础上加入了第三个控制电极。通过向控制电极施加正电荷，就能吸引电子，从而闭合电路；而通过施加负电荷，就能闭合电路。
      - **性能：**每秒可开闭数千次。
      - **优势：**和继电器相同的是，可以通过一个控制线路来控制断开或闭合电路，并且真空管内没有会动的组件，因此存在更少的磨损。
      - **缺点：**比较脆弱，并且会像灯泡一样烧坏，并且体积比较大。
      - **真空管的出现，标志着计算机从机电转向电子**
      - **第一个大规模使用真空管的计算机是巨人1号**，由工程师Tommy Flowers设计并于1943年12月完工。巨人1号包含1600个真空管，并被认为是第一个可编程的电子计算机，编程方法是把几百根电线插入插板，由此让计算机执行正确操作。
      - **电子数值积分计算机 ENIAC**，**在1946年于宾夕法尼亚大学设计制造**，这是世上第一个真正的通用可编程电子计算机，每秒可执行5000次十位加减法。但是由于存在大量的真空管，因此ENIAC运行半天左右就会出现一次故障。
    - **晶体管（Transistor）:**
      - **晶体管：**类似于继电器和真空管，晶体管也是一个用于控制电路闭合断开的开关。晶体管有**两个电极**，这**两个电极之间通过半导体材料隔开**。这里通过控制连接到半导体的电极电荷数，可以控制半导体的导电性，由此来控制电流是否流动。当控制线路通电时，两个电极接通，否则两个电极断开。
      - **性能：**每秒可开关10000次。
      - **优势：**相比玻璃制成的真空管，晶体管是固体的，并且体积远小于继电器和真空管。
      - **IBM 608**，它有3000个晶体管，每秒执行4500次加减法，或80次左右的乘除法。
      - 如今，计算机里的晶体管小于50nm，并且每秒可切换上百万次，工作几十年。很多晶体管和半导体开发在圣克拉拉谷，位于旧金山和圣河西之间，**由于制造半导体最常见的材料是硅，由此这个地方被称为“硅谷”**。并且William Shockley搬过去创建了**肖克利半导体**，里面的员工后来成立了**仙童半导体**，而这里面的员工后来创立了**英特尔**。
  - 布尔逻辑和逻辑门
    - 使用二进制的原因
      - 计算机最早的是机电设备，一般使用十进制计数，比如用齿轮数来代表十进制。一些早期电子计算机，通过对不同电流大小进行划分，可以使用三进制、五进制等等。但问题是，**状态越多就越难区分信号，如果存在电噪音，可能就会使状态十分混乱**。所以为了让信号更加清晰，可以只使用“开”和“关”两种状态。
      - **布尔代数（Boolean Algebra）**: 一整个数学分支专门处理“真”和“假”，已解决了所有法则和运算. 在布尔代数中，变量的值是true和false，能够对其进行逻辑操作。布尔代数中有三个基本操作：NOT、AND和OR。
    - **NOT操作**: 使用晶体管实现门控时，可以将控制线作为输入，将底部的电极当做输出，而上端电极始终保持高电平状态。这样当输入开启时，就会使得两个电极接通，使得输出也会开启；如果输入关闭时，两个电极是断开状态，就会使得输出还是保持关闭状态。
    - **AND操作**：这里需要使用两个晶体管来实现AND GATE. 下方两个电极分别为两个输入，左侧电极接通电源，右侧电极为输出。当两个输入都开启时，电源和输出就会接通，使得输出开启；当任意输入关闭时，电源就不会和输出接通，使得输出保持关闭。
    - **OR操作**: 左侧电极为电源，下方两个电极分别表示两个输入，右侧电极为输出。只要任意一个输入开启，就能使得电源和输出电极接通，使得输出开启；当两个输入都关闭时，就使得电源和输出电极保持断开状态，使得输出保持关闭。由此通过上方的三个组件（NOT门、AND门和OR门）可以构建出更加复杂的组件。另一个常见的布尔操作叫做异或操作。
    - **异或操作（XOR）**: XOR操作和OR操作唯一的不同就只有当两个输入都为true时，XOR输出false，而OR输出true。通过对AND操作真值表取反，再和OR操作真值表进行对比，可以发现，第二三行都为true，而第一四行结果不同，因此只要在这两个结果后面加个AND就能得到XOR的真值表。
  - 二进制
    - 二进制的基为2，每一位是前一位的两倍。
    - **位（bit）**: 一个1或0
    - **字节（byte）**: 8位二进制数, 定义原因是八位太过常见，最小为0，最大为255。
    - **字(word)**: 32位和64位操作系统，指的是操作系统处理数据的块，大小是32位或者64位
    - 正数、负数、整数、**浮点数（Floating Point Numbers）**的表示
    - 1963年发明了ASCII（美国信息交换标准代码），当时为7位二进制数，能够存放128个不同的值，可以用来表示大小写字母、数字、标点符号等等，并且其中存储了特殊字符，比如换行符、制表符等等。
      - 在128-255的字符: 美国额外的数字主要用于编码附加符号；在俄罗斯，他们用这些额外的字符表示西里尔字符等等。
      - **局限:**
        - 如果在土耳其电脑上打开拉脱维亚语写的电子邮件，就会出现乱码；
        - 像中文和日语这种包含数千字符的语言，根本无法使用8位二进制数来表示所有字符。为了解决这个问题，每个国家发明了多字节编码方案，可以使用多个字节来编码字符，但各个国建之间的编码方案不互相兼容。
    - UNICODE 1992年诞生，是字符编码标准，解决 ASCII 不够表达所有语言的问题
      - 最常见的Unicode是16位的，有超过一百万个位置来编码字符，编码所有语言的所有字符都足够了，并且还有位置放数学符号、Emoji等等。
  - 算数逻辑单元（Arithmetic and Logic Unit，ALU）
    - ALU
      - 英特尔 74181
      - 算数单元（Arithmetic Unit）
        - 半加器（Half adder）
        - 全加器（Full Adder）
          - 我们也可以对全加器进行抽象，得到一个包含三个输入和两个输出的独立部件。
        - 8位加法器（8-bit adder）
        - 超前进位加法器（Carry-Look-Ahead Adder）
        - ALU通常支持以下操作：加法、带进位的加法、减法、带借位的减法、取反、增1、减1、数字无改变通过。这些操作也是由逻辑门构成的。注意：简单的ALU并不支持乘法，而是把乘法用多次加法来实现，而更好的处理器有专门做乘法的算数单元。
      - 逻辑单元（Logic Unit）
        - 能做简单的数值测试，比如数字是不是负数(一堆OR门最后加上NOT门)。
        - 两个8位输入，并且有一个4位操作码（Operation Code）来告诉ALU对输入执行什么操作, 有一个8位输出。同时ALU会输出一系列1位标志（FLAG），来表示特定状态，比如我们可以计算A-B，然后通过ZERO来判断结果是否为零来判断A与B是否相等，通过NEGATIVE来判断A是否小于B；然后OVERFLOW连接到加法器的进位，来判断是否出现溢出。
  - 寄存器和内存
    - **随机存取存储器（Random Access Memory, RAM）**: 只能在有电的情况下存储东西
    - **持久存储（Persistent Memory）**: 电源关闭时数据也不会丢失，它用来存其他东西。
    - **构建存储一位的锁存器**
      - **AND-OR锁存器（AND-OR Latch）**: 上方的是SET输入，下方的是RESET输入，当SET=1、RESET=0，就能将输出设置为1，当RESET=1，就能将输出设置为0，当SET=0、RESET=0，则输出最后放入的内容。由此能够存储1位的信息（该信息存储在OR门上方的输入电极中）对其进行SET和RESET进行合并，并添加其他门控单元，可以得到一个**门锁（GATE LATCH）**
    - 如果我们并排8个锁存器，就能存储8位信息。一组这样的锁存器称为**寄存器（Register）**，寄存器能够存一个数字，这个数字的位数称为寄存器的**位宽（Width）**。
      - 当WRITE ENABLE=0时，会忽略数据输入，保持OUTPUT不变。当WRITE ENABLE=1时，数据输入会直接传到输出，而且数据输入会保存在OR门的上方电极，进行数据存储。
    - 写入寄存器之前，要先启动里面所有的锁存器，可以将所有锁存器的允许写入线都连接在一起，把它设为1，然后用8条数据线发送数据，然后将允许写入线设回0，就能将8位数据存储在寄存器中。
    - 但是通过这种形式排列锁存器需要太多的线路，64位寄存器需要129条线，256位寄存器需要513条线，可以通过矩阵形式排列来进行化简。我们可以构建**16x16门锁矩阵（Latch Matrix）**，其中一共有256个，通过打开相应的行线和列线来启用某个锁存器。
      - 对于256位存储，只需要一条数据线，一条允许写入线，一条允许读取线和16行16列的线用来选择锁存器，一共35条线。
      - 由于16x16门锁矩阵最多16行16列，所以可以分别用4位表示行和列的地址，就能用一共8位来定位一个锁存器，比如“12行8列”可以表示为11001000。
    - **多路复用器（Multiplexer）**: 为了将地址转换成“行和列”
      - 可以对256位寄存器进行封装，它的输入是一个8位地址，4位表示行，4位表示列，同时需要允许写入线和允许读取线，然后需要一条数据线用于读写数据。（注意：每次只能选择一个锁存器，所以数据线只能读写1bit数据）
      - 对其再进步一扩展，可以将8个256位内存拼在一起，这样就能一次读写8bit数据，也就是一个字节数据。由于每个256位内存都使用相同的8位数据线，因此8位数据会存在每个256位内存的相同地址中，并且第一个256位内存存放第一位，第二个256位内存存放第二位，以此类推。这个模块可以在256个地址中存储256个字节。（由于这种设计，所以计算机中**以一个字节为寻址的最小单位**）
      - 使用8个16x16门锁矩阵可以得到256字节的内存，然后可以用4位表示行4位表示列来进行寻址，由此可以将门锁矩阵扩展到更大范围，但是需要更多位来表示地址。所以对于nxn门锁矩阵，存储空间为 n ^2^ 字节，需要的寻址空间为 n ^2^ 。比如要给千兆字节的内存寻址，就需要32位的地址。
    - **内存的一个重要特性是：能够随时访问任何位置。所以称为随机存取寄存器（Random Access Memory, RAM）。RAM只记录当前在做什么。**
    - RAM中存储的数据是保存在OR门其中一个电极上，所以断电后就无法保存。
    - 这一节用锁存器做了一块静态随机存取存储器（Static Random-Access Memory，SRAM），还有很多其他类型的RAM，比如DRAM、闪存和NVRAM，它们的功能和SRAM相似，但是使用不同的电路存放单个位。但是根本上，这些技术都是矩阵层层嵌套来存储大量信息。
  - 中央处理器（Central Processing Unit，CPU）
    - ALU + RAM
    - 给CPU支持的所有指令分配一个ID，可以得到指令表（Instruction Table）
      - 追踪程序运行到了哪里，称为指令地址寄存器（Instruction Address Register），用来存放当前指令的内存地址。
      - 存放当前指令，称为指令寄存器（Instruction Register）。
    - 指令
      - LOAD A 指令
        - CPU的第一个阶段叫取**指令阶段（Fetch Phase）**，负责拿到指令。首先，将指令地址寄存器连接到RAM，由于当我们启动计算机时，所有寄存器从0开始，所以指令地址寄存器中的值为0，将指令地址寄存器与RAM的地址线相连，然后开启RAM的允许读取线，就能使得RAM返回地址0中保存的值，并且将RAM的数据线和指令寄存器相连，就能将存放到指令寄存器中。
        - 取到指令后，CPU就会进入**解码阶段（Decode Phase）**来分析取到的指令内容。在这个例子中，指令寄存器中保存的是00101110，前四位0010为操作码，通过指令表可知这个指令是LOAD A指令，就是将RAM中的值保存在寄存器A中，而后四位1110保存的是RAM地址，转成十进制就是14，所以指令00101110的意思就是将RAM中14位的数据保存到寄存器A中。
          - 解码过程，是由控制单元（Control Unit）进行解码，控制单元也是由逻辑门组成的。比如控制单元要检查操作码是否为LOAD A，就需要以下电路，如果返回1，说明操作码就是LOAD A（所以对于指令表中的操作码，都需要对应的电路进行判断）。
        - 知道了指令寄存器中保存的指令后，就进入了执行阶段（Execute Phase）。通过LOAD A指令的电路，我们可以用来控制RAM的允许读取线，比如LOAD A指令的电路返回1，则说明要读取RAM，所以用这个1设置RAM的允许读取线来读取RAM的内容；如果LOAD A指令的电路返回0，说明不需要读取RAM，就用这个0设置RAM的允许读取线来关闭RAM的读取。然后还需要将指令中保存的地址传到RAM的地址线。
      - ADD 指令
        - 在解码阶段，通过逻辑电路可以判断操作码0100并返回1，而通过地址01来设置寄存器B的允许读取线，通过地址00来设置寄存器A的允许读取线和允许写入线。在执行阶段，控制单元会将寄存器A和寄存器B中的数据作为ALU的两个输入，并且输出对应加法的操作码给ALU。然后结果应该保存在寄存器A中，但是不能直接写入寄存器A中，不然ALU会不断读取这个结果然后和自己相加，因此控制单元会用一个自己的寄存器来暂时保存结果，然后关闭ALU后，再将值写入正确的寄存器中。最终还要讲指令地址寄存器+1。
      - STORE A指令
        - 对于指令01001101，操作码0100表示STORE A指令，即将寄存器A的值存放到内存中，而内存的地址就是后面的1101。这里，控制单元会先通过逻辑电路判断是否为STORE A指令，如果时，则开启RAM的允许写入线，并且同时开启寄存器A的允许读取线，然后通过1101指定RAM的对应锁存器，来保存寄存器A中的地址。
        - 在计算机中，其实有一个时钟来负责管理CPU的节奏，来执行取指-解码-执行过程。时钟以精确的间隔来触发电信号，控制单元会用这个信号来推进CPU的内部操作，确保一些按步骤进行。CPU完成一次取指-解码-执行称为一个时钟周期（Clock Cycle），而完成时钟周期的速度叫时钟速度（Clock Speed），单位是赫兹，用来表示频率的单位，表示1秒完成了几次“取指-解码-执行”的过程。（存疑？）而超频，值指的是修改时钟速度来加快CPU执行指令的速度，但是超频太多会让CPU过热或产生乱码，因为信号传输也需要一定时间，使得信号跟不上时钟。
        - 第一个单芯片CPU是1971年发布的4位CPU——Intel 4004，它的微架构如下图所示，有16个8位寄存器，4个指令地址寄存器，时钟速度达到了740kHz，即每秒74万次。
        - 在对控制单元加入时钟后才变成一个完整的独立组件，可以得到一个CPU芯片。而RAM是CPU外面的独立组件，CPU和RAM之间通过地址线、数据线、允许读取线和允许写入线来进行通信。
  - 指令和程序
    - CPU，它之所以强大，是因为它是可编程的，如果写入不同指令，就会执行不同任务，所以CPU是一块可以被软件控制的硬件。
    - JUMP指令就是将后面4位的内存地址覆盖当前的指令地址寄存器，使得指令地址寄存器指向新的内存地址。JUMP_NEG指令是当ALU结果为负数时进行跳转，我们知道ALU中有若干个FALG，其中有个NEG标志位，**当ALU结果为负数时NEG=1，所以JUMP_NEG就通过和这个标志位取AND来进行判断**。**HALT来指示计算机停止工作，应该将HALT放在程序的结尾，说明程序结束**。
      - 指令和数据都存储在同一个内存中，它们在根本上没有区别，都是二进制数，所以HALT指令很重要，能够用来区分指令和数据。
    - **无限循环（Infinite Loop）**
      - JUMP_NEG就是条件跳转的一个例子，其实还有其他类型的条件跳转，比如JUMP_IF_EQUAL或者JUMP_IF_GREATER。可以对上述例子进行修改，得到一个不会无限循环的例子。
    - 这里假设的CPU十分简单，一个指令长度只有8位，操作码4位说明最多只支持16中指令，而地址位只有4位，说明最多只能索引到RAM中的16位，这具有很大的局限性。目前真正的现代CPU采用两种策略：
      - 最直接的方法就是用更多位来代表指令，比如32位或64位，这个称为**指令长度（Instruction Length）**，说明一个指令要跨越多个字节。
      - 另一种策略可以使用**可变长度指令（Variable Length Instruction）**。比如某个CPU用8位操作码，因为内存中每个地址保存一个字节，而指令地址寄存器保存的是该指令最小地址，并且操作码刚好是一个字节，所以指令地址寄存器保存的是操作码的地址，所以CPU最先看到的信息就是操作码，所以CPU可以根据操作码的类型，来决定是否要读取后续字节来确定指令内容。比如CPU看到HALT指令，因为HALT指令不需要其他额外的数据，所以CPU就会马上执行HALT指令；如果看到了JUMP，因为该操作码需要知道需要跳转到的地址，而这个值就在JUMP后面，这个称为**立即值（Immediate Value）**，CPU就会读取这立即值来知道跳转的地址。通过这样设计，指令可以是任意长度的，但是会让读取阶段复杂一些
        > 一般来说，指令=操作码+操作值地址，比如LOAD_A 10表示的是将RAM 10中保存的数据加载到寄存器A中。当指令=操作码+操作值时，该操作值就称为**立即值**，不需要在RAM中索引出对应的操作值，比如JUMP 2，这里直接跳转到RAM 2处，所以这个2称为立即值。总之，不需要从RAM中索引出操作值就能使用的称为立即值。
    - 在Intel 4004中，它支持46个指令，使用8位立即值来执行JUMP，所以可以表示更多的内存地址。处理器从1971年至今，现代CPU比如Intel Core i7含有上千个指令和指令变体，长度从1到15字节。
  - 高级CPU设计
    - 早期计算机的提速方式是**减少晶体管的切换时间**
    - 处理器厂商发明各种新技术来提升性能
      - **给CPU增加专门电路**
        - 用软件方式实现了除法, 很多时钟周期，效率很低，所以现代CPU直接在硬件层面设计了除法，可以直接给ALU除法指令。
        - 处理器有专门的电路来实现图片操作，解码压缩视频，加密文档。
        - > 基于标准操作用软件方式构建的方法，通常需要若干个时钟周期，而通过关键专门的电路可以进行提速。
        - 为了兼容旧指令集，指令数量变得越来越多。**第一个集成CPU Intel 4004有46条指令，但现代处理器有上千条指令，有各种巧妙复杂的电路**。
    - **给CPU增加缓存**
      - 缓存脏位（DIRTY BIT）
      - 同步——缓存满了但是CPU又要缓存—>回查是否是脏位—>写会RAM
    - **流水线设计/并行处理（Instruction Pipelining）**
      - 通过并行处理（Paralleize）（PARAII FLIZE）来进一步提高效率
      - “取值-解码-执行”: 每个时钟周期都能执行1个指令，吞吐量变成了3倍。
    - **乱序处理**
      - （？动态排序——最小化流水线停工时间）
      - 流水线处理器要先弄清数据依赖性，在必要时停止流水线，避免出问题。高级的处理器会动态排序有依赖关系的指令，最小化流水线的停工时间，称为乱序执行（Out-of-order Execution）
      - **推测执行/分支预测**
        - **条件跳转（Conditional Jump Instructions）**
        - 简单的流水线处理器，看到JUMP指令会停一会儿，等条件值确定下来后，处理器才会继续流水线。高端的处理器会猜哪条路的可能性更大（即继续顺序执行还是跳转到指定位置），然后提前把指令放进流水线，称为**推测执行（Speculative Execution）**。当JUMP结果出来后，如果CPU猜对了，则流水线已经塞满了正确指令可以马上运行，但是如果CPU猜错了，就要**清空流水线（Pipeline Flush）**。为了减少清空流水线的次数，CPU厂商开发了复杂的方法来猜测哪条分支更有可能，称为**分支预测（Branch Prediction）**。
      - **多个ALU**
        - **超标量处理器（Superscalar Processor）**: 一个时钟周期可以完成多个指令。
        - 一次性处理多条指令（取值+解码）会更好，如果多条指令要ALU的不同部分，就多条同时执行。我们也可以更进一步，多加几个相同的电路来执行出现频率很高的指令，比如很多CPU有四个、八个甚至更多完全相同的ALU，可以同时执行多个数学运算。
      - **多核**: 同时运行多个指令流
        - 需要使用**多核处理器（Multi-core Processors）**
        - 四核处理器意味着一个CPU芯片内，有多个独立处理单元，并且它们之间可以共享一些资源，比如缓存，使得多核之间可以合作运算。
      - **多CPU**
        - **超级计算机（Supercomputer）**，模拟宇宙的形成, 中国无锡的国家超算中心，神威·太湖之光有40960个CPU，每个CPU有256个核，每个核心的频率为1.45GHz，每秒可进行9.3亿亿次浮点数运算，也称为浮点运算次数（Floating Point Math Operations Per Second，FLOPS）。
    - MMX，3DNOW，SEE——多余的电路去实现更经一部的操作
    - 46——1000+ ——超级高的时针转速——快速传数据给CPU
  - 早期的编程方式
    - 最早的可编程的物品——纺织机（亚卡尔织布机）
      - 每一行的图案由可穿孔卡纸决定UARD——线高线低
      - 连续指令时的图案更加丰富
    - 控制面板——执行不同的计算(PLUGBOARDS"插线板")
      - 插线板的编程对象的变换 ——机电计算机（ENIAC）——渴求更快更灵活
      - 1940-1950内存变得可行——存储程序计算机（STORED-PROGRAM COMPUTERS）
      - 存储的的地方——冯诺依曼体系——（1948）“绰号宝宝”——数据输入——穿孔卡片
    - 新的编程方式——（PANEL PROGRAMMING）
      - 商用计算机——altair 8800
      - 门槛——底层硬件
      - 优化——PROGRAMMING LANGUAGE
  - 编程语言与发展
    - 机器可以处理 ML(机器语言) && MC(机器码)
    - 在计算机早期，必须用机器码写程序，一般会先对程序进行高层次的功能描述，称为伪代码（Pseudo-code）
      - 助于程序员理解，无法让计算机运行，然后根据**指令表**将伪代码转换成**二进制机器码**，然后将机器码送入计算机中并运行
    - **助记符（Mnemonics）**(1940-1950), 后跟数据，形成完整的指令。
      - 与其写0和1的机器码，程序员可以直接写“LOAD_A 14”，这个语言称为汇编语言（Assembly Language）
      - **汇编器（Assembler）**
        - **自动分析JUMP地址:** JUMP后面跟的是内存中的真实地址，如果我们在上方对程序进行修改，则后面的所有地址都会改变。所以汇编器不用固定跳转地址，而是让你插入可跳转的标签，当程序传入汇编器，汇编器就会自己推算出跳转地址，这样就程序员就无序过分关注细节。
        - **一条汇编指令对应一条机器指令**，所以汇编码和底层硬件连接很密切
        - 在需要的地方插入代码用goto，而不是得重新更新程序
    - **霍普**设计了一个高级编程语言，叫做**Arithmetic Language Version 0(A0)**
      - 一行高级编程语言，可能转换成几十条二进制指令。
      - 霍普在1952年创造了第一个编译器（Compiler），编译器专门把高级语言转换成低级语言（比如汇编或机器码）
      - **高级编程语言就不用管寄存器或内存位置，编译器会解决这些细节。**
    - **语言普通面向商业语言（Common Business-Oriented Language，COBOL）**
      - 在1950年，大多数编程语言和编译器只能运行在一种计算机中，如果更换计算机，就要重写所有代码，因此1959年开发一种通用编程语言，可以在不同机器上通用。
      - 为了兼容不同底层硬件，每个计算机架构需要一个COBOL编译器，由此无论运行的计算机是什么，这些编译器可以接收相同的COBOL代码。如今大多数编程语言都是如此，不必接触CPU特有的汇编码和机器码。
      - 60年代：ALGOL，LISP，BASIC
      - 70年代：Pascal，C和Smalltalk
      - 80年代：C++，Objective-C，Perl
      - 90年代：Python，Ruby和Java
      - 新千年：Swift，C\#，Go
      - 正是语言才是大众化的桥梁
      - 变量的抽象就是地址的抽象（COBOL）
  - 编译原理 语句和函数
    - 0x0d 语句
    - ——语法
    - 控制流语句
    - ??????
  - 算法入门——运行步骤和输入大小之间的关系
  - 数据结构
    - 数组Array
    - 字符串String
    - 矩阵Matrix
    - 结构体Struct
    - 链表Linked List
  - 软件工程
  - 集成电路&&摩尔定律
    - 集成开发环境
      电子管到晶体管
      仙童半导体让集成电路成为可嫩
      PCB 蚀刻金属线——PCB和IC结合
      光刻技术 把复杂图案印在材料上
    - 晶圆开始
      半导体通过控制导电时机
      晶体管更小密度更高， 切换状态更快，耗电少
    - 1970年超大规模集成（VLSI）软件自动生产芯片设计
      光的波长导致精度达到极致——波长更短、投射更小
      量子隧穿效应——电极之间的极速靠近导致电子跳跃
    - 如何判断是否是小数？？
  - 操作系统（OS）
    - 目的：让计算机自动运行
    - 一种拥有操作硬件的特殊权利来运行软件和管理其他程序
      为了避免繁琐的软硬件交互，操作系统是作为硬件和软件之间的媒介
      开始于1950年，可以实现进程的连续运行，以避免时间的浪费，被叫做批处理。同十年年末CPU的告诉发展带动机械设备的发展
      操作系统提供API来抽象硬件，叫做“设备驱动程序”（device drives）
      通过标准化机制和输入输出硬件（I/O）交互
    - 多线程
      - Atlas通过调度解决可以在一个CPU上运行多个程序，在单个CPU上共享时间，这种操作叫做多任务处理
        操作系统将不连续的内存虚拟化，叫做“虚拟内存”，程序可以假定内存总是从0开始，这样就不必时时刻刻追踪内存了
        操作系统会自动处理虚拟内存和实际内存之间的映射，这种机制使得内存可以灵活增删，叫做“动态内存分配”，这样子也不会影响其他内存，叫做“内存保护”
        以上两种机制是进行多任务处理的必不可少的条件
      - #### Multics
        1969年后期发展出一个主计算机和多个终端——分时操作系统（Multics）（多任务信息与计算系统）最大的特点：考虑安全（防止恶意用户访问非法内存）
      - #### Unix
        受限于内存保护的复杂度上升，开发出了替代品——Unix
        将内存分为两部分：一是核心部分“内核”，二是一对有用的工具（程序和运行库）
        将以前的系统恢复直接压缩为“内核恐慌”（调用一个恐慌的函数，无线循环打印恐慌），需要重启电脑，得到用户的一致好评
        1971年顺势成为最流行的语言
    - 个人电脑的出现
      - 微软的磁盘操作系统（MS-DOS）（160k）
  - 内存&&存储介质
  - 文件与文件系统
    - 文件格式：可以随便存文件数据，但按格式会更方便
      - TXT文本文件：ASKII
      - WAV音频文件：每秒上千次的采集数字
      - BMP图片文件：像素的红绿蓝 RGB 值
    - 文件系统：很早期时空间小，整个储存器就像是一整个文件，后期多文件很重要
    - 目录系统：同来解决多文件问题，存其他文件的信息，比如开头、结尾、创建时间等
    - 平面目录系统：—Flat Film System：文件都在同一个层次，早期空间小，只有十几个文件，平面系统够用
    - 如果文件紧密的一个个前后排序造成问题，所以文件系统会：
      - 空间划分块
      - 文件拆分存在多个块中
    - 文件的增删查改会不可避免的造成文件散落在各个块中
       如果是磁带这样的存储介质就会造成问题，所以做碎片整理
    - 分层文件系统 —Hierarchical File System：有不同文件夹，文件夹可以层层嵌套
  - 文件压缩
    - 压缩的好处是能存更多的文件，传输也更快
      - 游码编程
      - 无损压缩
      - 霍夫曼树
      - “消除冗余”和“用更紧凑的表示方法”，混合使用
      - 字典编码
      - 感知编码
      - 有损压缩
      - 时间冗余
      - MPEG-4视频编码
  - 命令行界面
    - 人机交互
    - 早期输入数据是打印到纸上，而输入是用纸纸卡一次性把程序和数据都给进去
    - QWERTY 打字机的发展，克里斯托弗·莱瑟姆·肖尔斯 发明于1868年
    - 电传打字机
    - 命令行界面
    - ls命令
    - 早期文字游戏  Zork （1977年）
    - cd命令
  - 屏幕与2D图形显示
    - PDP-1计算机、键盘与显示器分开，屏幕显示临时值
      - PDP-1（Programmed Data Processor-1），程序数据处理机１号 , 是形成骇客文化的重要推手。史上第一个电脑游戏是在这个平台上开发的（一段简单的FORTRAN程序。在这个程序里，Crowther设计了一张地图，地图上不规则的分布着陷阱，游戏者必须寻找路径避开陷阱）
         其磁芯内存的周期时间是**5.35微秒**(换算成**时脉频率**约**187千赫兹**)。大部分算数指令需要10.7微秒来完成(亦即约**每秒完成93458个运算**)，这是因为这些指令运算需要使用两个内存周期：第一个周期用来**取得指令**，而第二个周期用来**存取数据**。
         PDP-1的晶体管数量为2700个，并且拥有3000个二极管
      - 文本任务 和 图像任务是分开的。因为早期的屏幕分辨率连纸都不如。**早期的屏幕的值更多是追踪程序的值（比如寄存器的值）**
    - 阴极射线管（CRT）（原理是：把电子发射到有碳光体涂层的屏幕上，当电子撞击涂层时会发光几分之一秒，由于电子是带电拉子。略径可以用磁场控制，屏幕内用板子或线圈把电子引导到想要的位置）
       既然可以这样控制。 有2种方法绘制图形1，
      - 矢量扫描：引导电子末描绘出形状。因为发光只持续一小会儿，如果重复得足够决可以得到清晰的图像
      - 光栅扫描：按固定路径。一行行来从上向下。从左到右。不断重复。只在特定的点打开电子束。以此绘制图形。用这种方法。可以用很多小线联绘制形状甚至文字。最后。因为显示技术的发展。我们终于可以在屏幕上显示清晰的点。叫像嘉"
    - 液晶显示器
    - 字符生成器
    - 屏幕缓冲区
    - 矢量命令画图
    - Sketchpad，光笔
    - 函数划线，矩形
  - The Cold War and Consumerism
  - The Personal Computer Revolution
  - Graphical User Interface
  - 计算机网络-Computer Networks
    - 第一个计算机网络出现在1950~1960年代
    - **"球鞋网络"**(sneakernet): 非正式的术语，用于通过在计算机之间物理移动介质（例如磁带，软盘，光盘，USB闪存驱动器或外部硬盘驱动器）来传输电子信息，而不是通过计算机网络进行传输.
    - **LAN**
      - 最著名和成功的是"以太网",
      - 开发于1970年代
      - "帕洛阿尔托研究中心"诞生
    - **MAC(Media Access Control address)**
      - 这个唯一的地址放在头部，作为数据的前缀发送到网络中
      - **监听以太网电缆**, 只有看到自己的 MAC 地址，才处理数据
    - **载波侦听多路访问(Carrier Sense Multiple Access, or CSMA)**: 很多计算机同时侦听载体
    - 载体传输数据的速度 叫"带宽"
    - **指数退避(Exponential Backoff)**: 遇到错误: 会等一秒+随机时间-> 网络拥塞
    - **冲突域(the Collision Domain)**
    - **路由(routing)**
      - 数据传输时, 全球的路由器协同工作，找出最高效的线路
    - **报文交换(Message Switching)**: 传输数据的另一个方法
    - **数据包(packets)**: 将大报文分成很多小块
      - 数据包都有目标地址
      - 跳几次数据包才会到达指定IPA(IP Adress).
      - traceroute
      - 具体格式由"互联网协议"定义(IP)
      - 优点:
        - **去中心化** being decentralized
        - **没有中心权威机构  没有单点失败问题** with no central authority or single point of failure.
    - IP:
      - IP: 数据包的头部（或者说前面）只有目标地址
      - 头部存 "关于数据的数据", 也叫 元数据(metadata)
      - UDP(用户数据报协议): UDP 也有头部，位于数据前面, 头部信息之一是端口号,
        - 每个想访问网络的程序, 都要向操作系统申请一个端口号.
        - 简单又快.
      - TCP(Transmission Control Protocol, 传输控制协议):所有数据必须到达
        - TCP 数据包有序号, 可以将数据包排序
        - 确认码的成功率和来回时间, 可以推测网络的拥堵程度, 并且可根据拥挤情况自动调整传输率
        - **缺点**: 那些"确认码"数据包把数量翻了一倍但并没有传输更多信息
      - **总结**:
        - IP 负责把数据包送到正确的计算机, UDP 负责把数据包送到正确的程序
        - TCP/IP(Internet Protocol), 可以解决乱序问题, 将数据拆分成多个小数据包，然后通过灵活的路由传递
      - **修复**:
        - UDP接收方知道数据损坏后，一般只是扔掉, 不提供重发的机制
        - TCP 要求接收方的电脑收到数据包并且"校验和"检查无误后（数据没有损坏） 给发送方发一个确认码，代表收到了"**确认码**" 简称 **ACK**, 得知上一个数据包成功抵达后，发送方会发下一个数据包如果过了一定时间还没收到确认码, 发送方会再发一次
    - "因特网控制消息协议"(ICMP, Internet Control Message Protocol)
    - "边界网关协议"(BGP) the Border Gateway Protocol
    - 现代互联网的祖先是 ARPANET, 来源于美国高级研究计划局Advanced Research Projects Agency.
    - "物联网""internet of things".
    - 广域网也叫 WAN
    - 互联网服务提供商(ISP): Internet Service Provider
    - 互联网主干由一群超大型、带宽超高路由器组成
    - DNS 不是存成一个超长超长的列表，而是存成树状结构
      - 顶级域名（简称 TLD）在最顶部，比如 .com 和 .gov
      - 下一层是二级域名，比如 .com 下面有 \N google.com 和 dftba.com
      - 再下一层叫子域名，\N 比如 images.google.com, store.dftba.com
    - 网络分层: 每一层处理各自的问题如果不分层, 直接从上到下捏在一起实现网络通信，是完全不可能的, 抽象使得科学家和工程师能分工同时改进多个层, 不被整体复杂度难倒.
      - "数据链路层"负责操控"物理层" 数据链路层有：媒体访问控制地址（MAC），碰撞检测，
      - 指数退避，以及其他一些底层协议
      - 网络层: 负责各种报文交换和路由
      - 传输层: 比如 UDP 和 TCP 这些协议,负责在计算机之间进行点到点的传输而且还会检测和修复错误
      - 会话层session: 使用 TCP 和 UDP 来创建连接，传递信息，然后关掉连接
  - The World Wide Web
  - Cybersecurity
  - Hackers&Cyber Attacks
  - Cryptography
  - ML&AI
  - Computer Vision
  - Natural Language Processing
  - Robots
  - Psychology Of Computing
  - Educational Technology
  - The Singularity,Skynet And The Future Of Computing