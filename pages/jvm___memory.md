title:: jvm/memory
tags:: #garbage_collection

- ## [Java (JVM) Memory Model - Memory Management in Java | DigitalOcean](https://www.digitalocean.com/community/tutorials/java-jvm-memory-model-memory-management-in-java)
  ![](../assets/Java-Memory-Model.png)
  - ### Young Generation
    mark:: the place where all the new objects are created
    - GC => **Minor GC**
    - #### Java Memory Model
      - Eden Memory
      - Survivor Memory(S0, S1)
  - ### Old Generation, Tenured
    - GC => **Major GC**
    - #### Stop the World Event
      mark:: **all GC is this event**, which means all application threads are stopped until the operation completes.
    - #### Java Memory Model
      - 永久代 Permanent Generation, Perm Gen
        mark:: contains the application metadata required by the JVM to describe the classes and methods used in the application
        - collapsed:: true
          #+BEGIN_WARNING
          Perm Gen is not part of Java Heap memory, and changed name to **Metaspace** since [[java 8]]. The most significant difference is **how it handles memory allocation**. Specifically, this native memory region grows automatically by default.
          永久代不是堆内存，最显着的区别是它如何处理内存分配。具体而言，默认情况下，此本机内存区域会自动增长
          #+END_WARNING
          via: [Permgen vs Metaspace in Java | Baeldung](https://www.baeldung.com/java-permgen-metaspace)
          - We also have new flags to tune the memory:
            - *MetaspaceSize* and *MaxMetaspaceSize –* we can set the Metaspace upper bounds.
            - *MinMetaspaceFreeRatio – *is the minimum percentage of class metadata capacity free after [garbage collection](https://www.baeldung.com/jvm-garbage-collectors)
            - *MaxMetaspaceFreeRatio *– is the maximum percentage of class metadata capacity free after a garbage collection to avoid a reduction in the amount of space
        - 方法区 Method Area
          mark:: Store class structure (runtime constants and static variables) and code for methods and constructors.
          - 常量池 Runtime Constant Pool
            mark:: per-class runtime representation of constant pool in a class. (类中常量池的每个类运行时表示形式). It contains class runtime constants and static methods.
        - 内存池 Memory Pool
          mark:: Create a pool of immutable objects if the implementation supports it. like String Pool.
          - #+BEGIN_WARNING
            Memory Pool can belong to Heap or Perm Gen, depending on the JVM memory manager implementation.
            属于堆还是永久代取决于 JVM 内存管理的实现
            #+END_WARNING
          -
      - 栈内存 Java Stack Memory
        mark:: used for execution of a thread. They contain method specific values that are short-lived and references to other objects in the heap that is getting referred from the method.
        - #+BEGIN_WARNING
          Stack memory belongs to the non-heap memory of JVM. It is allocated for each thread that runs in the JVM. Stack memory is used to store local variables and method calls for each thread.
          #+END_WARNING
        - [Difference between Stack and Heap Memory](https://www.digitalocean.com/community/tutorials/java-heap-space-vs-stack-memory)
      -
    - #### Memory Management in Java
      - Java Heap Memory Switches
        - Java provides a lot of memory switches that we can use to set the memory sizes and their ratios. Some of the commonly used memory switches are:
        - | VM Switch | VM Switch Description |
          | ---- | ---- | ---- |
          | -Xms | initial heap size [:br]堆初始值 |
          | -Xmx | maximum heap size [:br]堆最大值 |
          | -Xmn | size of the Young Generation, [:br]rest of the space goes for Old Generation. [:br]设置年轻一代的大小，其余的空间用于老一代  |
          | -XX:PermGen | initial size of the Perm Gen [:br]永久代初始值 |
          | -XX:MaxPermGen | maximum size of Perm Gen [:br]永久代最大值|
          | -XX:SurvivorRatio | ratio of Eden space and Survivor Space (8(:1:1) default) [:br]伊甸园和幸存区比率 |
          | -XX:NewRatio | ratio of old/new generation sizes (2 default) |
          - `-XX:SurvivorRatio` example
            - if Young Generation size is 10m and VM switch is -XX:SurvivorRatio=2 then 5m will be reserved for Eden Space and 2.5m each for both the Survivor spaces. The default value is 8.
        - Most of the times, above options are sufficient, but if you want to check out other options too then please check [JVM Options Official Page](https://www.oracle.com/technetwork/java/javase/tech/vmoptions-jsp-140102.html).
      - Java Garbage Collection
        - **Marking**
          - Identifies which objects are in use and which ones are not in use.
        - **Normal Deletion**
          - removes the unused objects and reclaim the free space to be allocated to other objects.
        - **Deletion with Compacting**
          - For better performance, after deleting unused objects, all the survived objects can be moved to be together. This will increase the performance of allocation of memory to newer objects.
        - 2 problems with a simple mark and delete approach.
          - Not efficient
            collapsed:: true
            - most of the newly created objects will become unused
          - 在多个垃圾回收周期中使用的对象也最有可能在未来的周期中使用
            Secondly objects that are in-use for multiple garbage collection cycle are most likely to be in-use for future cycles too.
      - Java Garbage Collection Types
        - **Serial GC (-XX:+UseSerialGC)**
          collapsed:: true
          - Serial GC uses the simple **mark-sweep-compact** approach for young and old generations garbage collection i.e Minor and Major GC.Serial GC is useful in client machines such as our simple stand-alone applications and machines with smaller CPU. It is good for small applications with low memory footprint.
        - **Parallel GC (-XX:+UseParallelGC)**
          collapsed:: true
          - Parallel GC is same as Serial GC except that is spawns N threads for young generation garbage collection where N is the number of CPU cores in the system. We can control the number of threads using `-XX:ParallelGCThreads=n` JVM option.Parallel Garbage Collector is also called throughput collector because it uses multiple CPUs to speed up the GC performance. Parallel GC uses a single thread for Old Generation garbage collection.
        - **Parallel Old GC (-XX:+UseParallelOldGC)**
          collapsed:: true
          - This is same as Parallel GC except that it uses multiple threads for both Young Generation and Old Generation garbage collection.
        - **Concurrent Mark Sweep (CMS) Collector (-XX:+UseConcMarkSweepGC)**
          collapsed:: true
          - CMS Collector is also referred as concurrent low pause collector. It does the garbage collection for the Old generation. CMS collector tries to minimize the pauses due to garbage collection by doing most of the garbage collection work concurrently with the application threads.CMS collector on the young generation uses the same algorithm as that of the parallel collector. This garbage collector is suitable for responsive applications where we can’t afford longer pause times. We can limit the number of threads in CMS collector using `-XX:ParallelCMSThreads=n` JVM option.
        - **G1 Garbage Collector (-XX:+UseG1GC)**
          collapsed:: true
          - The Garbage First or G1 garbage collector is available from Java 7 and its long term goal is to replace the CMS collector. The G1 collector is a parallel, concurrent, and incrementally compacting low-pause garbage collector.Garbage First Collector doesn’t work like other collectors and there is no concept of Young and Old generation space. It divides the heap space into multiple equal-sized heap regions. When a garbage collection is invoked, it first collects the region with lesser live data, hence “Garbage First”. You can find more details about it at [Garbage-First Collector Oracle Documentation](https://docs.oracle.com/javase/7/docs/technotes/guides/vm/G1.html).
      - Java Garbage Collection Monitoring
      - Java Garbage Collection Tuning (调优)
-
- [[question/java]]
  - 介绍下 Java 内存区域（运行时数据区）
  - Java 对象的创建过程（五步，建议能默写出来并且要知道每一步虚拟机做了什么）
  - 对象的访问定位的两种方式（句柄和直接指针两种方式）
- Refs
  - 深入理解 Java 虚拟机：JVM 高级特性与最佳实践 第二版
  - [Java 内存区域详解 | JavaGuide](https://javaguide.cn/java/jvm/memory-area.html)
    collapsed:: true
    - 《自己动手写 Java 虚拟机》
    - Chapter 2. The Structure of the Java Virtual Machine：https://docs.oracle.com/javase/specs/jvms/se8/html/jvms-2.html
    - JVM 栈帧内部结构-动态链接：https://chenxitag.com/archives/368
    - Java 中 new String("字面量") 中 "字面量" 是何时进入字符串常量池的? - 木女孩的回答 - 知乎： https://www.zhihu.com/question/55994121/answer/147296098
    - JVM 常量池中存储的是对象还是引用呢？ - RednaxelaFX 的回答 - 知乎： https://www.zhihu.com/question/57109429/answer/151717241
    - [http://www.pointsoftware.ch/en/under-the-hood-runtime-data-areas-javas-memory-model/open in new window](http://www.pointsoftware.ch/en/under-the-hood-runtime-data-areas-javas-memory-model/)
    - [https://dzone.com/articles/jvm-permgen-–-where-art-thouopen in new window](https://dzone.com/articles/jvm-permgen-%E2%80%93-where-art-thou)
    - [https://stackoverflow.com/questions/9095748/method-area-and-permgen](https://stackoverflow.com/questions/9095748/method-area-and-permgen)
  - https://blog.newnius.com/java-garbage-collection-what-why-how.html
  -