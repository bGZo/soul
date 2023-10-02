title:: os
alias:: system/operating

-
- [[soft-return]]
- [[process]]
- [[os/bios]]
- [[os/file-system]]
-
- Page replacement algorithm
  - **OPT/OPR**, **Optimal Page Replacement**.
  - FIFO,First In First Out. (LIFO,First In Last Out.)
    - **Second Chance**.
  - LRU/NRU,Least/Not Recently Used.
    - **CLOCK**: 因为 LRU 实现起来比较复杂 (**栈和寄存器**的支持), 所以用 Clock 替代.
  - LFU/NFU, Least/Not Frequently Used.
  - MFU, Most Frequently Used.
  - Related Links
    - Page_replacement-[Wikipedia-EN](https://en.wikipedia.org/wiki/Page_replacement_algorithm#Page_replacement_algorithms)
    - Memory Management-[Pdx Edu](http://web.cecs.pdx.edu/~harry/os/slides/Ch3-MemMgmt-2.pdf)
- 进程
  - `fork()`: 返回两个三种类型的参数, 从调用的地方复制一份, 两者同时向下运行.
  - `exec()`
  -
  -
  - [[ipc]]
  - ## 通信
  - ```
    pipe
    ```
    - ```
      #include<unistd.h>
      int pipe(int filedes[2]); // 成功返回0; 否则返回-1
      // 返回两个文件的描述符; fd[0]:读管道, fd[1]:写管道
      ```
  - ```
    write
    ```
    - ```
      #include <unistd>
      ssize_t write(int filedes, void *buf, size_t nbytes); // 成功返回写入的字节数; 出错返回-1
      // filedes: 文件描述符; buf: 待写入数据缓存区; nbytes:要写入的字节数
      ```
  - mkfifo()函数
    
    创建FIFO管道
    - ```
      #include <sys/types.h>
      #include <sys/stat.h>
      int mkfifo(const char *pathname, mode_t mode);
      // 创建成功返回0，出错返回1
      // pathname: 普通的路径名; mode: 与open函数中的mode参数相同
      ```
      
      [3/n] 存储管理
- 磁盘工作原理
  - 一直以来不是很理解计算机组成原理的磁盘工作原理, 这周上操作系统再次提到了这个模块, 偶然寻到一个[视频](https://www.bilibili.com/video/BV11a4y1x7PC/)讲解, 感觉非常清晰, 总之就是三级寻址, `柱面 => 磁道(定位盘面) => 扇区`.
    ![output](https://user-images.githubusercontent.com/57313137/144595594-178548be-1bce-4f4b-9b08-85d77d497e82.gif)
-
-
-
- More
  - [tobegit3hub/understand_linux_process: The open-source ebook of Understand Linux Process](https://github.com/tobegit3hub/understand_linux_process)
  - [doctording/os: 《操作系统真相还原》笔记](https://github.com/doctording/os)
-