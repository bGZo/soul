title:: bash-cookbook
alias:: book/bash-shell脚本编程经典实例
author:: Carl Albing / JP Vossen / Cameron Newham
publisher:: 人民邮电出版社
published-date:: 20210100
source:: https://book.douban.com/subject/35301381 ; https://weread.qq.com/web/reader/0fe3236072462ddc0fee7efkc81322c012c81e728d9d180
- ## Bash
  - #why
    - 历史原因, bash 现在无处不在
      - GNU 项目旨在创建一款彻头彻尾的 [[posix]], bash 最初正是该项目的一部分
    - 一门强大的编程语言, 复杂编程特性
    - 一种优秀的用户界面, 保持键盘输入的便捷性
  - Shell 编程 / Shell 脚本编程
    - 重复性+复杂任务 自动化
      - 易用性
      - 可靠性
      - 可重现性
  - 提示符揭秘
    - TODO 如果系统中运行了某种强制性访问控制（mandatory access control，MAC）系统，如 NSA 的SELinux，root 甚至有可能不再是全能的了
  - 显示当前位置
    - pwd 是 print working directory（打印工作目录）的缩写，该命令接受两个选项。-L 显示当前的逻辑路径，这也是默认选项。-P 显示当前的物理路径，如果跟随符号链接，结果可能和逻辑路径不同。与此类似，cd 命令也提供了 -P 和 -L 选项：
  - 查找并运行命令
    - 可以试试 type、which、apropos、locate、slocate、find 和 ls 命令。
- ## Output
  - 例如，再也不用让操作员将磁带挂载到磁带驱动器上（至少我们见过的桌面系统和笔记本计算机不用了）
  - 软件开发人员是否要针对各种输出设备编写代码，甚至包括尚未发明的设备？这显然是件麻烦事。用户是不是也得知道如何将想要运行的程序连接到不同种类的设备？这也不是什么好主意
  - 操作系统负责实现这套魔法。无论你要写入的目标是磁盘文件、终端、磁带设备、记忆棒，还是其他东西，程序只需要知道如何写入文件就够了，剩下的事情由操作系统搞定
  - 程序怎么知道是该写入代表终端窗口的文件、磁盘文件还是其他种类的文件？不难，这种事情留给 shell 就行了
  - 考虑下面这条简单的命令：[插图]
  - 输出到终端/终端窗口
    - shell 负责解析 echo 的命令行参数（shell 对其他命令也是如此）。这意味着，在将参数交给 echo 前，shell 会完成所有的替换、通配符匹配等操作。其次，在解析参数时，参数之间的空白字符会被忽略
  - 消除输出中的换行符
    - 该特性在 shell 脚本中用处更大，你可能希望在形成一整行前由多条语句逐部分输出，或者在读取输入前显示用户提示
    - 转移序列与 C 语言字符串中的类似。要想使用它们，调用 echo 命令时必须加上 -e 选项
  - 保存命令输出
    - cat 命令得名自一个较长的单词 concatenation（拼接）
  - 将输出保存到其他文件
    - 如果文件名以斜线（/）起始，那就是绝对路径名
    - 放置在文件系统层次结构（目录树）中以根目录起始的指定位置（假设所有的中间目录都存在且你有权限进入）
    - /tmp，这是一个几乎所有 Unix 系统都存在且普遍可用的临时目录
    - 每次引用 .. 就会在文件系统目录树中向上（往根的方向，并非惯常意义中的沿着树“向上”）移动一级
  - 保存ls命令的输出
    - 我们加上 -C 选项
    - shell 的重定向功能意在对所有程序保持透明，因此程序无须编写特定代码来让自身的输出能够被重定向
    - 我们可以在程序中加入代码，判断输出何时被发往终端（参见 manisatty）。然后，程序就能够针对不同情况进行处理，这也正是 ls 所做的
    - 那么用户可能希望按列输出（-C 选项）
    - man isatty
  - 将输出和错误消息发送到不同文件
    - 1> 和 2> 中，数字表示文件 描述符
    - 1 代表标准输出（STDOUT）
    - 2 代表标准错误（STDERR）
    - 如果不指定数字，则假定为 STDOUT
  - 将输出和错误消息发送到同一文件
    - 又或者老式且略烦琐（但可移植性更好）的写法：[插图]
    - both 是准备向 STDERR 和 STDOUT 生成输出的（假想）程序
    - &> 和 >& 只是将 STDOUT 和 STDERR 发送到相同地方（这正是我们想做的）的便捷写法
    - 1 用作重定向的目标，但是 >& 将 1 解释为文件描述符。实际上，2>&1 是一个实体（其中不允许出现空格），表示标准错误（2）会被重定向（>）到随后的文件描述符（&）1
    - 2>& 必须作为整体出现，不能夹杂空格；否则，2 就成了另一个参数，而 & 代表与其表面完全不同的含义（与在后台运行命令有关）
    - 所有的重定向操作符都带有一个前导数字（如 2>），而 >（标准输出的文件描述符）的默认数字为 1
    - 有时候，错误消息在文件中出现的时间可能早于在屏幕上出现的时间。这与标准错误的无缓冲性质有关，当写入文件而不是屏幕时，这种现象会更加明显
  - 仅使用文件的起始或结尾部分
    - 使用 head 或 tail 命令。默认情况下，head 输出指定文件的前 10 行，tail 输出最后 10 行
    - tail 还有 -f 和 -F 选项，这两个选项能够跟踪文件末尾的写入
    - head、tail、
    - cut 和 uniq
  - 跳过文件标题
    - tail 命令的选项 -n number（或者 -number）可以指定相对于文件末尾的行偏移。因此，tail -n 10 file 会显示 file 的最后 10 行，这也是不指定任何选项时的默认处理方式
  - 丢弃输出
    - Unix 和 Linux系统都存在一个特殊设备，该设备并非真实的硬件，而仅仅是一个位桶（bit bucket），我们可以将不需要的数据都扔进去。它就是 /dev/null，非常适用于此类场景
  - 保存或分组多个命令的输出
    - 花括号（{}）将这些命令组合在一起，然后将重定向应用于分组中所有命令的输出
    - 花括号实际上是保留字，因此两侧必须有空白字符。另外，闭合花括号之前的拖尾分号也是不能少的
    - 你也可以用括号（()）告诉 bash 在子 shell 中运行这些命令，然后重定向整个子shell 的输出
    - 第一处是语法上的，第二处是语义上的。从语法上来看，花括号两侧需要有空白字符，命令列表中的最后一个命令必须以分号结尾。如果使用括号，那就不要求这些了
    - 花括号只是一种组合多个命令的方式而已，更像是重定向的便捷写法，这样我们就不用单独重定向各个命令了。而出现在括号中的命令是在 shell 的另一个实例中运行，也就是当前 shell 的子 shell
    - 子 shell 几乎复刻了当前 shell 的环境，包括 $PATH 在内的变量都是一模一样的，但对陷阱的处理有所不同
    - 陷阱的更多信息
    - 因为 cd 命令是在子 shell 中执行的，所以退出子 shell 后，父 shell 的当前目录仍保持原样，shell 变量也不会发生变化
    - 花括号有一种值得注意的用法，即能够形成更简洁的分支语句块
    - 第一种形式，这种写法更清晰，适合更大范围的受众
  - 将输出作为输入，连接两个程序
    - 利用管道符号（|）将输出直接发送到下一个程序
    - 使用管道符号意味着不用再创建临时文件，事后再将其删除
    - 像 sort 这种程序，既能从标准输入中获取输入（通过 < 符号进行重定向），也能从作为参数的文件中获取输入。因此，可以按以下方式操作
    - 不用再将输入重定向到 sort
    - 这种程序称为过滤器，如果照此方式编写程序和 shell 脚本，则更有助于你个人以及你的同事
    - 初级的并行处理机制
    - 后面向前面写???你可以让两个命令（程序）并行运行并共享数据：一个的输出作为另一个的输入。二者不必按顺序运行（一个结束，另一个接着开始），只要第一个命令产生可用数据，第二个命令立刻就可以开始处理
    - 你可以让两个命令（程序）并行运行并共享数据：一个的输出作为另一个的输入。二者不必按顺序运行（一个结束，另一个接着开始），只要第一个命令产生可用数据，第二个命令立刻就可以开始处理
    - 但要注意，按照这种方式运行的多个命令（通过管道相连）分别在多个独立的进程中运行。尽管这一细微之处经常被忽视，有时所带来的影响却不容小视
    - 19.8 节会对此展开讨论
    - 通过管道将大量数据传给 less 等命令时，总会出现这种事：一旦发现了要找的东西，就会想要退出，哪怕是管道中还有更多数据
  - 将输出作为输入，同时保留其副本
    - 2.16.2　解决方案
    - tee 命令
    - 同时发送到 /tmp/x.x 和 awk
    - 后者通过管道与 tee 的输出连接在一起
    - 演示 tee 命令在命令序列中的用法
    - tee 命令可以用来代替重定向标准输出的做法
    - tee 的输出并未重定向到别处，因此会显示在屏幕上。但是输出的副本也会发送给指定的文件（如 cat /tmp/all.my.sources），以备后用
    - 这意味着错误（如来自 find 命令）会显示在屏幕上，但不会出现在 tee 指定的文件中。我们可以在 find 命令中加入 2>&1
  - 以输出为参数连接两个程序
    - 将待删除的文件指定为命令参数
    - rm 并不会从标准输入中读取参数
    - 能以命令行参数的形式获取文件名，那该如何将先前运行过的命令（如 echo 或 ls）的输出放入命令行呢？
    - bash 的命令替换特性
    - 也可以使用 xargs 命令
    - 参见 15.13 中的讨论
    - 子 shell 中运行的
    - #markdown 早期的 shell 语法没有使用 $()，而是将命令放进反引号（``）
    - 可以用 rm -i 降低风险，选项 -i 会提醒你确认每次删除。对于小批量文件来说，这么做没毛病，但如果文件数量众多，那整个过程可就冗长不堪了
    - 用 !! 来确保更加万无一失
  - 在一行中多次重定向
    - 也就是说，shell 脚本 divert 可以将其输出定向到不同的描述符，调用程序（invoking program）可以将描述符指向不同的目标
    - 如果 divert 是一个 C 程序的可执行文件，则无须任何 open() 调用就可以向文件描述符3、4、5、6 写入
    - 标准输入是 0，标准输出是 1，标准错误是 2
    - 如果不指定数字，则假定为 1。这意味着可以用略显啰唆的写法 1>（而不是简单的 >）跟上文件名来重定向标准输出，不过其实没这个必要，便捷写法 > 就挺好
    - 可以在 shell 中打开任意数量的文件描述符，令其指向各种文件，这样一来，随后在命令行上调用的程序就不用再费事了，直接就可以使用这些已打开的文件描述符
  - 重定向不起作用时保存输出
    - Unix 和 Linux 中的每个进程通常一开始都有 3 个已打开的文件描述符：一个用于输入（标准输入 STDIN），一个用于输出（标准输出 STDOUT），一个用于错误消息（标准错误STDERR）
    - 至于是否遵循这种约定，将错误消息写入标准错误，将正常输出写入标准输出，那真的就得看程序员了
    - 每个文件描述符都由一个数字（从 0 开始）表示。标准输入是 0，标准输出是 1，标准错误是 2。这意味着可以用略显啰唆的写法来重定向标准输出：1>（而不是简单的 >）跟上文件名，但其实没这个必要，便捷写法 > 就够了。要想重定向标准错误，可以使用 2>
    - 前者是缓冲式的（buffered），后者是非缓冲式的（unbuffered）
    - 非缓冲意味着每个字符都是单独写入，不会被收集在一起，然后再批量写入。也就是说，你可以立刻看到错误消息，发生故障时丢失此类消息的可能性较小，但由此带来的就是效率问题
    - 如果想要同时保存并查看输出，该怎么办？2.16 节中讨论过的 tee 命令此时就能派上用场了
    - 此时标准输出指向的是屏幕
    - 因此，只有标准输出消息会出现在文件中，而错误消息仍旧会出现在屏幕上
    - bash 对此做了特殊处理，它可以识别出标准输出连接到了管道 3。因此，当你写出 2>&1 时，bash会假定你希望将标准错误也连入管道，尽管 2>&1 的正常处理方式并非如此
    - 3命令行中的管道会先于重定向进行处理。详见 Bash Reference Manual 的 3.2.2 节
    - 这种做法（包括一般的管道语法）带来的另一个结果是，我们无法只将标准错误（而非标准输出）传入其他命令，除非事先交换文件描述符
  - 交换STDERR和STDOUT
    - STDERR和STDOUT
    - 第三个文件描述符交换 STDERR 和 STDOUT：
    - 每次重定向文件描述符时，就会将打开的描述符复制到另一个描述符
    - 将语法 3>&1 读作“使文件描述符 3 指向与标准输出文件描述符 1 相同的值”。
  - 避免意外覆盖文件
    - 发现将输出重定向到了原本打算保存的文件，这种事情太常见了
    - noclobber 选项告诉 bash 在重定向输出时不要覆盖任何现有文件
  - 有意覆盖文件
    - 使用 >| 重定向输出。即便是设置了 noclobber，bash 也会忽略该选项，并覆盖文件
    - noclobber 的使用并不会代替文件权限。不管有没有使用 >|，如果没有目录的写权限，那么就无法创建文件
    - 不管有没有使用 >|，你必须拥有文件的写权限才能覆盖现有文件
    - 据 Chet 所说，“POSIX 指定了语法 >|，这还是从 ksh88 中选出来的。我也说不清楚 Korn5 为什么会选用这种写法。csh 用的是 >!”。为了帮助记忆，你可以将其视为一种强调。它的用法在英语中带有祈使语气，符合要求 bash 在必要时“无论如何”都要覆盖文件的意味。vi 和 ex 编辑器在其 write 命令中也用 ! 表达了相同含义（:w!filename）。如果没有 !，覆盖已有文件时，编辑器会发出抱怨。要是加上 !，就相当于告诉编辑器“做就行了！”
- ## Input
  - 从文件获取输入
    - 它们可以从视觉上提示重定向的方向
    - cat
    - ，但这是 shell 脚本编程的一项重要特性（DOS 命令行也借鉴了），对 shell 的功能性和简单性必不可少
  - 将数据与脚本存放在一起
    - <<（here-document）从命令行而非文件重定向输入文本
    - grep 命令查找第一个参数是否在指定文件中出现，如果没有指定文件，那么它会在标准输入中查找。
    - 设置 here-document，告诉 shell 将标准输入重定向（临时）到此处
    - EOF 是一个任意的字符串（你想用什么都行），用作临时输入的终止符。它并不属于输入的一部分，只是作为标记告诉输入在哪里结束
    - grep 命令加入 -i 选项，以示搜索时不区分大小写。这样便可以使用 grep -i $1<<EOF同时搜索“Bill”或“bill”
  - 避免here-document中的怪异行为
    - Here Document
      - here文档 / heredoc / hereis / here-字符串 / here-脚本，是一种在命令行shell（如sh、csh、ksh、bash、PowerShell和zsh）和程序语言（像Perl、PHP、Python和Ruby）里定义一个字符串的方法。它可以保存文字里面的换行或是缩进等空白字元。一些语言允许在字符串里执行变量替换和命令替换。
      - here文档最通用的语法是 `<<`; 紧跟一个标识符，从下一行开始是想要引用的文字，然后再在单独的一行用相同的标识符关闭。在Unix shell里，here文档通常用于给命令提供输入内容。
        via: https://zh.wikipedia.org/zh-cn/Here%E6%96%87%E6%A1%A3here-document
    - 足以告诉 bash 你希望区别处理 here-document 中的内容
    - here-document 的每一行都要执行参数扩展、命令替换以及算术扩展”
    - $100 被视为 shell 变量 $1，随后跟着两个 0。这就是为什么我们在搜索“pete”时，得到的是 pete00
    - 搜索“bill”时，得到的是 bill00
    - bash 就知道不用执行扩展，这样就符合我们的预期行为了
    - 扩展操作
    - 在结尾处的 EOF 标记中出现的拖尾空白字符（哪怕只是一个空格）会导致无法将其识别为结束标记。bash 会吞掉脚本的剩余部分，将其也视为输入并继续查找 EOF。所以，一定要确保 EOF 之后没有额外的空白字符（尤其是空格或制表符）。
  - 缩进here-document
    - 弄乱 shell 脚本的格式
    - 就像结尾处的 EOF 标记中出现的任何拖尾空白字符都会导致其无法被识别为结束标记一样（参见 3.3 节中的警告部分），使用除制表符外的前导字符也会造成同样的后果。如果你的脚本使用空格或混合空格和制表符来进行缩进，可别在here-document 中这么做。要么使用制表符，要么什么都不用。另外，小心有些文本编辑器会自动将制表符替换成空格。
  - 获取用户输入
    - 取用户输入并将其保存在 shell 变量 REPLY中，这是 read 的最简形式
    - 记住，要在提示信息结尾处加上标点符号或空格，因为光标会停在那里等待输入
    - t 选项可以设置超时值。指定秒数达到后，不管用户是否输入，read语句都会返回。我们的示例同时用到了 -t 和 -p 选项，但你也可以单独使用 -t 选项。从 bash 4 开始，你甚至可以将超时值指定为小数，如 .25 或 3.5。如果读取超时，则退出状态码（$?）将大于 128
  - [[zsh]] 运行 `read -p` 时会报错 `-p: no coprocess`
    - > In both shells read is a builtin. It shares the same purpose, but the implementation and options differ.
    - Solutions
      - use `bash xxx.sh`
      - or modify the usage of `read` under zsh, usage like
        - ```shell
          $ read name"?input some: "
          ```
  - ,获取yes或no
    - 尤其是不用区分大小写，如果用户直接按回车键，还能提供默认值
    - 11.7 节中给出了该问题的另一种处理方法
  - 选择选项列表
    - select 语句能够轻松地在 STDERR 上为用户生成编号列表，以便用户从中做出选择。虽然按下 Ctrl-D 可以结束 select，空输入会再次输出菜单，但别忘了提供“退出”或“结束”选项
  - 提示输入密码
    - 从用户那里读取到的输入行保存在变量 $PASSWD 中。
    - 如果禁止了回显功能，当用户按下回车键时，就不会回显换行符，后续输出就会和提示信息出现在同一行
    - 密码在内存中是以明文形式存放的，有可能通过核心转储或 /proc/core（如果你所用的操作系统提供了 /proc/）访问到。在多进程环境中也是如此，其他进程也有可能读取到密码。可能的话，最好使用 SSH 证书。无论任何情况，明智的做法是假定系统中的 root 和其他可能的用户都能接触到密码并对其进行相应的处理
    - 用 stty -echo 来禁止输入密码时的屏幕回显。这么做的问题在于如果脚本意外终止，那么回显仍会处于关闭状态。有经验的用户知道输入 stty sane 将其恢复，但这并非人人都懂
- ## refs
  - [Here文档 - 维基百科，自由的百科全书](https://zh.wikipedia.org/zh-cn/Here%E6%96%87%E6%A1%A3)
  - [arrays - Why does read -a fail in zsh - Stack Overflow](https://stackoverflow.com/questions/36453146/why-does-read-a-fail-in-zsh)
  - [Unix & Linux: "no coprocess" error when using read - YouTube](https://www.youtube.com/watch?v=VDibMOCJk_E)
- built-in command
-