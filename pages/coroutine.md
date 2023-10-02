alias:: concurrency/coroutine
tags:: TODO 
define:: "协程"

-
- 协程
  - via: [为什么 Java 坚持多线程不选择协程？ - 大宽宽的回答 - 知乎](https://www.zhihu.com/question/332042250/answer/734115120)
    - 优点
      - 节省资源，轻量，具体就是：
        - 节省内存，每个线程需要分配一段栈内存，以及内核里的一些资源
        - 节省分配线程的开销（创建和销毁线程要各做一次syscall）
        - 节省大量线程切换带来的开销
      - 与NIO配合实现非阻塞的编程，提高系统的吞吐
-
- Refs
  - [关于 Java 和 go 高并发的话题 - V2EX](https://www.v2ex.com/t/791169)