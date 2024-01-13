title:: linux/system-call

- ![image.png](../assets/image_1645969460108_0.png)
- 进程管理
  - ![image.png](../assets/image_1645969691367_0.png)
  - 通俗理解: 两种复制 => 从头开始 ❌ / 复制一个一模一样的后魔改 ✔
  - 返回值区分(子进程返回 0; 父进程返回子进程进程号) + `if-else` 语句判断 => 子进程调用 [[linux/system-call/execve]] 执行另一个程序, 此时子进程和父进程就彻底分道扬镳, 即产生了一个分支(fork)了
  - [[linux/system-call/waitpid]] => 父进程调用, 将子进程的进程号作为参数传给它, 这样父进程就知道子进程运行完了没有,成功与否
- 内存管理
  - 对于进程的内存空间来讲,放程序代码的这部分,我们称为**代码段(Code Segment)**
  - 对于进程的内存空间来讲,放进程运行中产生数据的这部分,我们称为**数据段(Data Segment)**
  - 其中局部变量的部分,在当前函数执行的时候起作用,当进入另一个函数时,这个变量就释放了;也有动态分配的,会较长时间保存,指明才销毁的,这部分称为**堆(Heap)**
  - > 一个进程的内存空间是很大的,32 位的是 4G,64 位的就更大了,我们不可能有这么多物理内存。就像一个公司的会议室是有限的,作为老板,你不可能事先都给项目组分配好。哪有这么多会议室啊,一定是需要的时候再分配
  - [[linux/system-call/brk]] => 分配的内存数量比较小的时候,使用 brk,会和原来的堆的数据连在一起,这就像多分配两三个工位
  - [[linux/system-call/mmap]] => 当分配的内存数量比较大的时候,使用 mmap,会重新划分一块区域,也就是说,当办公空间需要太多的时候,索性来个一整块
- 文件管理
  - 对于已经有的文件,可以使用 [[linux/system-call/open]] 打开这个文件, [[linux/system-call/close]] 关闭这个文件;
  - 对于没有的文件,可以使用 [[linux/system-call/creat]] 创建文件;
  - 打开文件以后,可以使用 [[linux/system-call/lseek]] 跳到文件的某个位置;
  - 可以对文件的内容进行读写,读的系统调用是 [[linux/system-call/read]], 写是 [[linux/system-call/write]]
- 异常处理与信号处理
  - 对于一些不严重的信号,可以忽略,该干啥干啥,但是像 [[linux/system-call/SIGKILL]] (用于终止一个进程的信号)和 [[linux/system-call/SIGSTOP]] (用于中止一个进程的信号)是不能忽略的,可以执行对于该 ==信号的默认动作==
  - [[linux/system-call/sigaction]] => 注册一个信号处理函数
- 组间沟通与进程间通信
  - **消息队列**(Message Queue), 内核里
    - [[linux/system-call/msgget]] 创建一个新的队列,
    - [[linux/system-call/msgsnd]] 将消息发送到消息队列,而消息接收方可以使用
    - [[linux/system-call/msgrcv]] 从队列中取消息
  - **共享内存**
    - [[linux/system-call/shmget]] 创建一个共享内存块
    - [[linux/system-call/shmat]] 将共享内存映射到自己的内存空间,然后就可以读写了
- 网络通信
  - [[Socket]]
- 源代码中的系统调用
  - https://www.kernel.org
  - 对于 64 位操作系统,找到 unistd_64.h 文件,里面对于系统调用的定义,就是下面这样
    ```cpp
    #mark::  __NR_restart_syscall    0
    #mark::  __NR_exit     1
    #mark::  __NR_fork     2
    #mark::  __NR_read     3
    #mark::  __NR_write      4
    #mark::  __NR_open     5
    #mark::  __NR_close      6
    #mark::  __NR_waitpid      7
    #mark::  __NR_creat      8
    ......
    ```
- Glibc
  - **Glibc 为程序员提供丰富的 API,除了例如字符串处理、数学运算等用户态服务之外,最重要的是封装了操作系统提供的系统服务,即系统调用的封装**
  - 有时候,Glibc 一个单独的 API 可能调用多个系统调用,比如说,Glibc 提供的 printf 函数就会调用如 sys_open、sys_mmap、sys_write、sys_close 等等系统调用。
  - 也有时候,多个 API 也可能只对应同一个系统调用,如 Glibc 下实现的 malloc、calloc、free 等函数用来分配和释放内存,都利用了内核的 sys_brk 的系统调用。
  - 有个命令 strace,常用来跟踪进程执行时系统调用和所接收的信号。你可以试一下咱们学过的命令行,看看都执行了哪些系统调用
- Refs
  - 趣谈Linux操作系统