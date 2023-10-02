title:: java/5/concurrency/multithreading
alias:: multithreading/java

-
- [[Java]]
  - 内置支持多线程
    - 一个Java程序实际上是一个JVM进程
      - JVM进程用一个主线程来执行 `main()` 方法，在 `main()` 方法内部，我们又可以启动多个线程。
      - JVM还有负责垃圾回收的其他工作线程等
    - 多任务，实际上是说**如何使用多线程实现多任务**
  - 多线程**经常需要读写共享数据，并且需要同步**
    - 多线程编程的**复杂度高，调试更困难**
      - 多线程模型是Java程序最基本的并发模型；
      - 后续读写网络、数据库、Web开发等都依赖Java多线程模型。
- Status
- 创建
  - 继承类 `thread`, 重写 `run()`
  - 实现接口 `Runnable`, 重写 `run()` + `Lambda` ([[jdk]]>=8)
  -
- 启动
  - `start()` -> `start0()`
    collapsed:: true
    - ```diff
      // In particular, a thread may not be restarted once it has completed execution.
      public synchronized void start() {
          /**
              * This method is not invoked for the main method thread or "system"
              * group threads created/set up by the VM. Any new functionality added
              * to this method in the future may have to also be added to the VM.
              *
              * A zero status value corresponds to state "NEW".
              */
          if (threadStatus != 0)
              throw new IllegalThreadStateException();
      
          /* Notify the group that this thread is about to be started
              * so that it can be added to the group's list of threads
              * and the group's unstarted count can be decremented. */
          group.add(this);
      
          boolean started = false;
          try {
      +       start0();
              started = true;
          } finally {
              try {
                  if (!started) {
                      group.threadStartFailed(this);
                  }
              } catch (Throwable ignore) {
                  /* do nothing. If start0 threw a Throwable then
                      it will be passed up the call stack */
              }
          }
      }
      
      +private native void start0();
      // native 修饰符表示这个方法是由 JVM 虚拟机内部的 C 代码实现
      ```
  - 优先级
    - `Thread.setPriority(int n)`
      - 1 ~ 10 (default:5)
- WAIT 状态
  - New | 新创建未执行
  - Runnable | 正在执行
  - Blocked | 阻塞挂起
  - Waiting | 等待
    - Timed Waiting
      - 运行中的线程，因为执行sleep()方法正在计时等待；
  - Terminated | 终止
    - 原因
      - 正常
        - `run()` 方法执行到 `return` 语句返回；
      - 意外
        - `run()` 方法因为未捕获的异常导致线程终止；
      - 强制
        - `stop()`
  - `join()`
    collapsed:: true
    - 插队
    - 可以让一个线程等待另一个线程直到其运行结束
      - ```java
        public class Main {
            public static void main(String[] args) throws InterruptedException {
                Thread t = new Thread(() -> {
                    System.out.println("hello");
                });
                System.out.println("start");
                t.start();
                t.join(); // main线程 等待 t线程 运行结束后再运行
                          // join(long) 设定等待时间
                System.out.println("end");
            }
        }
        ```
- WAIT 中断
- WAIT 守护 | Daemon Thread
  - 守护线程是指为其他线程服务的线程
  - JVM退出时不必关心守护线程
    - 所有非守护线程都执行完毕后，无论有没有守护线程，JVM 都会自动退出
  - `setDaemon(true)`
  - 守护线程不能持有任何需要关闭的资源
    - 例如打开文件等，因为虚拟机退出时，守护线程没有任何机会来关闭文件，这会导致数据丢失
- 同步
  - `ILOAD` -> `IADD` -> `ISTORE` 的指令形式
    - 原子运行的必要性 -> ==加锁 / 解锁==
      - 某一个线程执行时，其他线程必须等待
      - 任何时候临界区 (Critical Section) 最多只有一个线程能执行
  - 代价
    - 效率下降
      - 原子操作时无法并发
      - 需要合理的选择加锁对象, 选择加锁最少但是等效的对象
  - JVM规范定义了几种原子操作
    - 基本类型赋值
      - 如：`int n = m;`
      - `long` 和 `double` 除外
        - 64 位赋值不确定
        - x64平台 是原子操作
    - 引用类型赋值
      - 如：`List<String> list = anotherList`
      - WAIT 但多行赋值语句就需要同步, 大多数情况需要巧妙转换下
  - WAIT 方法
    - `synchronized`
      - ```java
        synchronized(Counter.lock) { // 获取锁
            ...
        } // 释放锁
        ```
  - 死锁
    - 两个线程各自持有不同的锁，然后各自试图获取对方手里的锁，造成了双方无限等待下去
    - 没有任何机制能解除死锁，只能强制结束JVM进程
- `wait()` 和 `notify()`
  - 多线程协调运行原则
    - 当条件不满足时，线程进入等待状态
    - 当条件满足时，线程被唤醒，继续执行任务
  -
- ReentrantLock
- Condition
- ReadWriteLock
- StampedLock
- Concurrent集合
- Atomic
- 线程池
- Future
- CompletableFuture
- ForkJoin
- ThreadLocal
-
- Refs
  - [【狂神说Java】多线程详解_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1V4411p7EF)
  - [多线程基础 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/1252599548343744/1304521607217185)
-