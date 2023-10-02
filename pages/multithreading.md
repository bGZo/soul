alias:: concurrency/multithreading
define:: 进程(中国大陆); ==过程==、行程、程序、处理程序(港台)
tags:: TODO

- [[process]] #vs [[thread]]
  id:: 63e72768-1f77-4542-9d9b-aa3e724b7bce
  - 定义/内存共享/阻塞/依赖/数据共享/系统处理
    collapsed:: true
    创建/上下文切换/通信/资源/终止
    ![image.png](../assets/os/image_1666321023071_0.png)
    via: [Difference between Process and Thread](https://www.tutorialspoint.com/difference-between-process-and-thread)
    - | Comparison Basis                       | **Process**                                                                          | **Thread**                                                                        |
      | -------------------------------------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
      | **Definition**                   | A program under execution(执行)                                                            | A lightweight process that[:br]can be managed independently by a scheduler             |
      | Memory [:br]Sharing        | Totally independent and don't share memory                                                 | May share some memory with its peer threads.                                            |
      | **Blocked**                      | Remaining processes can continue execution.                                                | If a user level thread gets blocked,[:br]all of its peer threads also get blocked.     |
      | **Dependency**                   | Individual processes are independent of each other.                                        | Threads are parts of a process and so are dependent.                                    |
      | Data and [:br]Code sharing  | Independent data and code segments.                                                        | Shares the data segment, code segment, files etc.[:br]with its peer threads.           |
      | **Treatment by OS**              | All the different processes are treated[:br]**separately** by the operating system. | All user level peer threads are treated [:br]as a single task by the operating system. |
      | Time for [:br]creation      | More                                                                                       | Less                                                                                    |
      | Context [:br]switching time | More (heavier)                                                                             | Less (lighter)                                                                          |
      | Communication                | More                                                                                       | Less                                                                                    |
      | Resource [:br]Consumption   | More                                                                                       | Less                                                                                    |
      | [:b "Time for"] [:br] [:b "termination"]   | More                                                                                       | Less                                                                                    |
  - ![image.png](../assets/os/image_1660737501730_0.png)
  - ![image.png](../assets/os/image_1660736864976_0.png){:height 357, :width 449}
  - ![https://www.youtube.com/watch?v=Dhf-DYO1K78](../assets/os/Screenshotter--YouTube-ProcessvsThread-1’18”_1660740100262_0.png)
-
- Refs
  - [Process (computing) - Wikipedia](https://en.wikipedia.org/wiki/Process_(computing))
  - [Multithreading and concurrency fundamentals](https://www.educative.io/blog/multithreading-and-concurrency-fundamentals)
  - Todo List
    - [想练一下 Java 多线程相关的知识点可以做什么项目？ - V2EX](https://www.v2ex.com/t/617678)
-
-