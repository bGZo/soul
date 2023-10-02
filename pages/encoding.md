define:: **代码页**是字符编码的别名. 也称**内码表**

-
-
- Outline
  - [[askii]]
  - EASCII
  - ISO 8859
    - ISO 8859-n(n=1,2,3,...,11,13,...,16)
    - Latin-1 == ISO8859-1
  - GB2312
    id:: 6d652964-9186-407d-bbae-464bee0b36a1
  - GBK(Chinese Internal Code Specification)
    - \> ((6d652964-9186-407d-bbae-464bee0b36a1))
  - BIG5 (small conflict with GB2312)
  - GB18030
    - \> ((6d652964-9186-407d-bbae-464bee0b36a1))
  - Unicode (NOT Compatible with GBXXX)
    - UCS2
    - UTF-16 (Extend UCS2)
    - UCS4
    - UTF-32 (Currently a subset of UCS4, But ability to encode more unicode characters)
    - UTF-8
      - BOM
      - No BOM
  - via
    - [编码](https://gist.github.com/fanfeilong/844ad0c2e2654cfd4c7e)
    -
- More
  - [为何微软不把 Windows 的默认字符集设置成 Unicode ？](https://www.zhihu.com/question/24103924/answer/26688840)
    collapsed:: true
    - > **Windows内核中默认使用的是UTF-16**，如果你写内核驱动就知道了，在内核里几乎都是以UTF-16的方式处理字符串的。
      >
      > 对于运行在应用层（用户态）的代码，Windows允许用户通过配置确定非Unicode字符的显示方式，可以是中文，也可以是BIG5，也可以是其它字符集。
      >
      > 为什么这么设计？因为是考虑到兼容性的问题，现在Windows7里，仍然能运行大量Windows 98时代的程序，WindowsXP里甚至能运行不少Windows3.x甚至更古老的程序，原因就是为了兼容性。
      >
      > 题主喜欢UTF-8，应该从Linux开发转过来的吧？Linux默认我记得是UTF-8（好像JSP也是？），UTF-8和UTF-16哪个更好我就不细说了，这方面的争论至今都没有结果。但是Windows可以把应用设置成UTF-16，之后的开发几乎没有太多的改变，我也没遇到过“**这不仅导致开发程序复杂**”的情况，至少C语言开发是这样的。所以，我看不出来UTF-16带来多少开发程序的不便。
      >
      > 为什么用UTF-16？好像UTF-16出现的比UTF-8要早一些，微软内核选择了UTF-16，再大改内核是非常困难的，大概是这样的。
      >
      > 如果题主是想讨论UTF-8和UTF-16哪个更好，建议再开个题目。
      >
      > 补充，反对 [@赵冬毓](http://www.zhihu.com/people/a38ac6b1ee685ea2d586c355e0e11902) 的回答，国家标准中只强调支持，而没有强调必须默认使用，“must conform”是“要求符合”，而没有强调默认使用（default）这个字符集，工信部的那个规范里也没有强调默认使用这一点。
      >
      > 遵循国家标准，也可以是把国家标准作为操作系统的子集，因为Linux、MacOS均支持GB18030，并且这个默认支持的行为不需要每次开机都提示，只需要在安装时告之即可。而且微软也做过类似的事情：在欧洲销售的WindowsXP在安装的时候都有浏览器的选择，并提供了Firefox等其它浏览器的下载链接，这也是微软为了提供告之义务以规避当地的反垄断法规。而且微软即使保持对GB18030默认支持，对于兼容性来说也没有问题，既遵守法律，又保持兼容性，未尝不可。
      >
      > 另外，附上标准全文：[信息处理产品中文要求认证实施规则](https://link.zhihu.com/?target=http%3A//www.doc88.com/p-29324427457.html)
      > 以及维基百科上的说明：[GB 18030](https://link.zhihu.com/?target=http%3A//zh.wikipedia.org/wiki/GB18030)
      >
      > 以及检测标准：
      >
      > 
      >
      > > 检测一般要求如下：
      > >
      > > 　　●字汇完整性：产品的字汇范围应是国家标准GB 18030中所有给出字形的字符；
      > >
      > > 　　●体系正确性：产品必须能够正确识别和处理按照国家标准GB 18030进行编码的文本文件。
  - [在 Windows 下键入 Enter 键，是在键盘缓冲区中存入 '\n' 还是 '\r''\n' 两个？](https://www.zhihu.com/question/24639606/answer/28476223)
    collapsed:: true
    - > Windows不是一次设计完的，历经30多年的变迁积累了很多东西，其中一个特点就是vk（虚拟按键？），这是一个DWORD（32bit）类型的数据，用来描述各种键盘状态，因为一个面向事件的系统就必须要能处理各种按键的弹起、落下、组合键，而如果考虑到各种地区的键盘布局（比如欧洲地区的键盘布局），这种键位组合数量庞大，所以才用DWORD表示。而后来软件又希望提供directIO以及各种hook请求，就慢慢演变成如今这种这么复杂的东西。
      >
      > 
      >
      > 以一个USB键盘为例，从USB的请求开始到最终窗口收到消息，中间有好几层缓冲区，每层都不太一样。
      >
      > 1. USB驱动一层有缓冲区，**扫描码，不区分换行符**。如果是使用directX的directIO进行按键输入管理，那么这一层就可以直接把按键信息拿走，有些游戏（比如LOL）就是这么做的。所有键盘消息最终都发送到Windows键盘的一个统一驱动里叫kbdclass.sys，这个驱动负责统一翻译、处理、管理所有键盘以及消息。这一层，应该还是扫描码。
      >
      > 2. 之后，这个**消息就通过内核到用户态了**。在用户态里，进程csrss.exe有一个线程win32k!RawInputThread负责处理按键，广播按键消息。**此时扫描码变成按键（包括区域符号转化）**是"\n"
      >
      > 3. csrss.exe调用DispatchMessage等函数分发消息给各个窗口、线程等。各个窗口收到按键消息，此时仍然是"\n".
      >
      > 4. 部分窗口会根据按键消息做文本转换，转换完以后，看到的才是"\r\n".
      >
      > 5. 对于命令行的C语言，由Windows的POSIX子系统或者其它模块负责接收按键消息，在LibC一层通过stdio/stdlib这些库转化成"\r\n".
      >
      > 6. 所以，如果你操作的内容位于文本框（以及其它Windows文本环境）、命令行的LibC环境（包括但不限于stdio、iostream库），那么收到的应该是"\r\n"，其它情况，比如Windows按键消息等，多数收到的都是"\n"
      >
      > 7. 当然，如果在MS开发环境下，真正到具体使用中的时候，还是分很多情况的：比如字符串"\n"在以非binary方式写入文件的时候，是"\r\n"，在以binary写入文件的时候，是"\n"，getchar返回的是"\n"，但不是绝对的，要根据你输入的数据流决定，有时候，如果输入的数据流是文件，而非键盘控制台，那么文件里的"\r\n"到了你的函数里，就变成了"\n"。所以，一个字符流可能保存在内存里的时候是"\r\n"，但你getchar得到的是"\n"，写到文件里却是"\r\n"。
      >
      > 8. 所以，只能说，用实践去尝试，尤其做开发，甚至会出现不同的开发环境里返回值不同的情况。如果非要做严格检查，建议同时检查"\r\n", "\n\r", "\n", "\r"另附上Windows按键消息的处理流程：一个按键的消息产生流程如下：
      >
      >     1. 硬件中断/硬件端口数据 `//WinIO能模拟，或者修改IDT是在这一层`
      >
      >     2. 键盘Port驱动（USB or PS/2）
      >
      >         ```
      >         //Filter驱动在此
      >         //DirectIO在此
      >         //KeyboardClassServiceCallback也在这一层被调用
      >         ```
      >
      >     3. kbdclass驱动
      >         //处理键盘布局和键盘语言，部分高端的病毒也工作在这里
      >
      >     4. Windows内核边界（zwCreate/zwReadFile）
      >         ----------------------（系统调用）----------------------
      >
      >     5. Windows内核边界（zwCreate/zwReadFile）
      >
      >     6. csrss.exe的win32k!RawInputThread读取，完成scancode和vk的转换
      >         
      >         ```
      >     //SetWindowHook工作在这里（全局）
      >         //kbd_event工作在这里
      >         ```
      >         
      >     7. csrss.exe调用DispatchMessage等函数分发消息
      >
      >         ```
      >         //SetWindowHook工作在这里（进程）
      >         //PostMessage和SendMessage在这里
      >         ```
      >
      >     8. 各个进程处理消息
      >
      >     9. 子系统、LibC、文本框、输入法转换按键到最终字符（符号）
      >
-
- Refs
  -
  - [ISO/IEC 8859 - Wikipedia](https://en.wikipedia.org/wiki/ISO/IEC_8859); [ISO/IEC 8859 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/ISO/IEC_8859)
-