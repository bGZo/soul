icon:: 💾
author:: 时国怀
created:: [[20240727]]
exclude-from-graph-view:: true
source:: https://www.zhihu.com/question/24639606/answer/28476223
type:: archives-web

- https://www.zhihu.com/question/24639606/answer/28476223
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