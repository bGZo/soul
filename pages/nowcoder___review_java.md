tags:: #java/interview
mark:: [Java校招面试题目合集_Java工程师/Java开发_牛客网](https://www.nowcoder.com/ta/review-java)

- ## Contents
  - DONE [什么是Java虚拟机？为什么Java被称作是“平台无关的编程语言”？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21069&query=&asc=true&order=&page=1)
  - DONE [JDK和JRE的区别是什么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21070&query=&asc=true&order=&page=2)
  - [”static”关键字是什么意思？Java中是否可以覆盖(override)一个private或者是static的方法？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21071&query=&asc=true&order=&page=3)
    collapsed:: true
    - ((63e72783-9c4d-4975-8316-8eefaa9e9f64))
    - 两个都不可以
      collapsed:: true
      - Private 只可以被本类成员和方法访问，所以无法被 Override
      - Override 是基于运行时动态绑定的，而 Static 早在编译期就已经静态绑定，与任何类的实例再不相关，因此无法 Override
  - [是否可以在static环境中访问非static变量？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21072&query=&asc=true&order=&page=4)
    collapsed:: true
    - 没有实例就不能访问 非static 变量，除非是在 static 环境中初始化一个实例；
  - DONE [Java支持的数据类型有哪些？什么是自动拆装箱？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21073&query=&asc=true&order=&page=5)
  - DONE [Java中的方法覆盖(Overriding)和方法重载(Overload)是什么意思？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21074&query=&asc=true&order=&page=6)
  - [Java中，什么是构造方法？什么是构造方法重载？什么是复制构造方法？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21075&query=&asc=true&order=&page=7)
    collapsed:: true
    - Java不支持像C++中那样的复制构造方法，这个不同点是因为如果你不自己写构造方法的情况下，Java不会创建默认的复制构造方法。（对任何对象都使用引用机制）
  - DONE [Java支持多继承么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21076&query=&asc=true&order=&page=8)
  - [接口和抽象类的区别是什么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21077&query=&asc=true&order=&page=9)
    collapsed:: true
    - ((63e7791a-04a5-425e-a98b-9c35bd1f7400))
  - [什么是值传递和引用传递？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21078&query=&asc=true&order=&page=10)
    collapsed:: true
    - Java 只有值传递参数；
      collapsed:: true
      - 当一个对象实例作为一个参数被传递到方法中时，参数的值就是该对象的引用一个副本
    - Related: [Java中只有按值传递，没有按引用传递！ - - ITeye博客](https://www.iteye.com/blog/guhanjie-1683637) & [Java 到底是值传递还是引用传递？ - 知乎](https://www.zhihu.com/question/31203609)
  - [进程和线程的区别是什么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21079&query=&asc=true&order=&page=11) #process
    collapsed:: true
    - 进程是执行着的应用程序，而线程是进程内部的一个执行序列
    - 线程又叫做轻量级进程
    - 一个进程可以有多个线程
    - **线程与进程的区别归纳：**
      collapsed:: true
      - **a.地址空间和其它资源**
        collapsed:: true
        - 进程间相互独立，同一进程的各线程间共享。某进程内的线程在其它进程不可见。
      - **b.通信**
        collapsed:: true
        - 进程间通信IPC，线程间可以直接读写进程数据段（如全局变量）来进行通信——需要进程同步和互斥手段的辅助，以保证数据的一致性。
      - **c.调度和切换**
        collapsed:: true
        - 线程上下文切换比进程上下文切换要快得多
      - d.在多线程OS中，进程不是一个可执行的实体
    - ((63e72768-1f77-4542-9d9b-aa3e724b7bce))
  - [创建线程有几种不同的方式？你喜欢哪一种？为什么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21080&query=&asc=true&order=&page=12)
    collapsed:: true
    - 继承Thread类
    - 实现Runnable接口
      collapsed:: true
      - 实现Runnable接口这种方式更受欢迎，因为这不需要继承Thread类
    - 应用程序可以使用Executor框架来创建线程池
      collapsed:: true
      - 线程池也是非常高效的，很容易实现和使用
    - 还有一种方式是实现Callable接口
  - [概括的解释下线程的几种可用状态。](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21081&query=&asc=true&order=&page=13)
    collapsed:: true
    - 1.新建 (new)
      collapsed:: true
      - 新创建了一个线程对象。
    - 2.可运行 (runnable)
      collapsed:: true
      - 线程对象创建后，其他线程(比如main线程）调用了该对象的start()方法。该状态的线程位于可运行线程池中，等待被线程调度选中，获取cpu的使用权。
    - 3.运行(running)
      collapsed:: true
      - 可运行状态(runnable)的线程获得了cpu时间片(timeslice)，执行程序代码
    - 4.阻塞(blocked)
      collapsed:: true
      - 阻塞状态是指线程因为某种原因放弃了cpu使用权，也即让出了cputimeslice，暂时停止运行
        直到线程进入可运行(runnable)状态，才有机会再次获得cputimeslice转到运行(running)状态
        阻塞的情况分三种：
      - (一).等待阻塞
        collapsed:: true
        - 运行(running)的线程执行o.wait()方法，JVM会把该线程放入等待队列(waittingqueue)中。
      - (二).同步阻塞
        collapsed:: true
        - 运行(running)的线程在获取对象的同步锁时，若该同步锁被别的线程占用，则JVM会把该线程放入锁池(lockpool)中。
      - (三).其他阻塞
        collapsed:: true
        - 运行(running)的线程执行Thread.sleep(longms)或t.join()方法，或者发出了I/O请求时，JVM会把该线程置为阻塞状态
        - 当sleep()状态超时、join()等待线程终止或者超时、或者I/O处理完毕时，线程重新转入可运行(runnable)状态。
        - 即让出了cputimeslice，
    - 5.死亡 (dead)
      collapsed:: true
      - 线程run()、main()方法执行结束，或者因异常退出了run()方法，则该线程结束生命周期。死亡的线程不可再次复生
    - ![](http://uploadfiles.nowcoder.com/images/20151217/149974_1450349079825_4697A22AC611680A692472687DEC1CFD)
    - ？**time_waiting** / **terminated** / **waiting**
  - [同步方法和同步代码块的区别是什么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21082&query=&asc=true&order=&page=14)
    collapsed:: true
    - 同步方法默认用this或者当前类class对象作为锁；
    - 同步代码块可以选择以什么来加锁，比同步方法要更细颗粒度，我们可以选择只同步会发生同步问题的部分代码而不是整个方法；
  - [在监视器(Monitor)内部，是如何做线程同步的？程序应该做哪种级别的同步？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21083&query=&asc=true&order=&page=15)
    collapsed:: true
    - 监视器和锁在Java虚拟机中是一块使用的。监视器监视一块同步代码块，确保一次只有一个线程执行同步代码块。每一个监视器都和一个对象引用相关联。线程在获取锁之前不允许执行同步代码。
  - DONE [什么是死锁(deadlock)？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21084&query=&asc=true&order=&page=16)
    collapsed:: true
    - 多个进程因竞争资源而造成的一种僵局（互相等待），若无外力作用，这些进程都将无法向前推进
    - 4个必要条件：
      collapsed:: true
      - 互斥条件
        collapsed:: true
        - 进程要求对所分配的资源（如打印机）进行排他性控制，即在一段时间内某 资源仅为一个进程所占有。此时若有其他进程请求该资源，则请求进程只能等待。
      - 不剥夺条件
        collapsed:: true
        - 进程所获得的资源在未使用完毕之前，不能被其他进程强行夺走，即只能 由获得该资源的进程自己来释放（只能是主动释放)。
      - 请求和保持条件
        collapsed:: true
        - 进程已经保持了至少一个资源，但又提出了新的资源请求，而该资源 已被其他进程占有，此时请求进程被阻塞，但对自己已获得的资源保持不放。
      - 循环等待条件
        collapsed:: true
        - 存在一种进程资源的循环等待链，链中每一个进程已获得的资源同时被 链中下一个进程所请求
  - [如何确保N个线程可以访问N个资源同时又不导致死锁？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21085&query=&asc=true&order=&page=17)
    collapsed:: true
    - 指定获得锁的顺序 （破环循环等待条件）
      collapsed:: true
      - 保证在获得第一个锁之前，不会请求第二个锁，保证每一个线程都以同样的顺序加锁和释放锁。
  - DONE [Java集合类框架的基本接口有哪些？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21086&query=&asc=true&order=&page=18)
    collapsed:: true
    - [[java 2/collections]]
    - 两大接口，容器和图，集合的父类是可迭代接口，下分列表，队列，集合；图下分哈希表实现，哈希图实现，有序图接口；
  - [为什么集合类没有实现Cloneable和Serializable接口？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21087&query=&asc=true&order=&page=19)
    collapsed:: true
    - 克隆和序列化的语义是根据具体实现走的，应该由具体实现决定是否由这些属性；
  - [什么是迭代器(Iterator)？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21088&query=&asc=true&order=&page=20)
    collapsed:: true
    - 迭代器接口提供对集合元素的迭代方法；
    - 每一个集合都有一个返回了迭代器的迭代方法；
    - 迭代过程甚至可以用非直接方法删除元素（迭代器提供的remove方法）；
  - [Iterator和ListIterator的区别是什么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21089&query=&asc=true&order=&page=21)
  - [快速失败(fail-fast)和安全失败(fail-safe)的区别是什么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21090&query=&asc=true&order=&page=22)
    id:: 63fc3a6b-687c-4703-8381-62d56b41eae0
    - 快速失败（fail—fast）
      mark:: 在用迭代器遍历一个集合对象时，如果遍历过程中对集合对象的结构进行了修改（增加、删除），则会抛出Concurrent Modification Exception。
      collapsed:: true
      - 原理：迭代器在遍历时直接访问集合中的内容，并且在遍历过程中使用一个 modCount 变量。集合在被遍历期间如果结构发生变化，就会改变modCount的值。每当迭代器使用hashNext()/next()遍历下一个元素之前，都会检测modCount变量是否为expectedmodCount值，是的话就返回遍历；否则抛出异常，终止遍历。
      - 注意：这里异常的抛出条件是检测到 modCount！=expectedmodCount 这个条件。如果集合发生变化时修改modCount值刚好又设置为了expectedmodCount值，则异常不会抛出。因此，不能依赖于这个异常是否抛出而进行并发操作的编程，这个异常只建议用于检测并发修改的bug。
      - 场景：java.util包下的集合类都是快速失败的，不能在多线程下发生并发修改（迭代过程中被修改）
    - 安全失败（fail—safe）
      mark:: 采用安全失败机制的集合容器，在遍历时不是直接在集合内容上访问的，而是先复制原有集合内容，在拷贝的集合上进行遍历。
      - 原理：由于迭代时是对原集合的拷贝进行遍历，所以在遍历过程中对原集合所作的修改并不能被迭代器检测到，所以不会触发Concurrent Modification Exception。
      - 缺点：基于拷贝内容的优点是避免了Concurrent Modification Exception，但同样地，迭代器并不能访问到修改后的内容，即：迭代器遍历的是开始遍历那一刻拿到的集合拷贝，在遍历期间原集合发生的修改迭代器是不知道的。
      - 场景：java.util.concurrent包下的容器都是安全失败，可以在多线程下并发使用，并发修改。
  - [Java中的HashMap的工作原理是什么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21091&query=&asc=true&order=&page=23) #[[java 2/collections]]
    collapsed:: true
    - hashmap是一个key-value键值对的数据结构，从结构上来讲在jdk1.8之前是用数组加链表的方式实现，jdk1.8 加了红黑树，hashmap数组的默认初始长度是16，hashmap数组只允许一个key为null，允许多个value为null
    - hashmap的内部实现，hashmap是使用数组+链表+红黑树的形式实现的，其中数组是一个一个Node[]数组，我们叫他hash桶数组，它上面存放的是key-value键值对的节点。HashMap是用hash表来存储的，在hashmap里为解决hash冲突，使用链地址法，简单来说就是数组加链表的形式来解决，当数据被hash后，得到数组下标，把数据放在对应下表的链表中。
    - 然后再说一下hashmap的方法实现
      - put方法
        - 计算出要put元素在hash桶数组中的索引位置（3）
          - 取put元素key的hashcode值
          - 高位运算
            collapsed:: true
            - 高位运算就是用第一步得到的值h，用h的高16位和低16位进行异或操作；
            - ```java
              /**
              * Computes key.hashCode() and spreads (XORs) higher bits of hash
              * to lower.  Because the table uses power-of-two masking, sets of
              * hashes that vary only in bits above the current mask will
              * always collide. (Among known examples are sets of Float keys
              * holding consecutive whole numbers in small tables.)  So we
              * apply a transform that spreads the impact of higher bits
              * downward. There is a tradeoff between speed, utility, and
              * quality of bit-spreading. Because many common sets of hashes
              * are already reasonably distributed (so don't benefit from
              * spreading), and because we use trees to handle large sets of
              * collisions in bins, we just XOR some shifted bits in the
              * cheapest possible way to reduce systematic lossage, as well as
              * to incorporate impact of the highest bits that would otherwise
              * never be used in index calculations because of table bounds.
              */
              static final int hash(Object key) {
                int h;
                return (key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16);
              }
              ```
            - 用 h 的高 16 位和低 16 位进行异或操作，就是将 h 的二进制表示分成两部分，每部分有 16 位，然后对应的位进行异或运算。例如，假设 h = 10000000000000001000000000000000（32位），那么 h 的高低位异或操作就是：
            - ![chrome_296.png](../assets/chrome_296_1676626462508_0.png)
            - 可以看到，这样的操作可以让 h 的哈希值更加分散，减少冲突的可能性。
          - 取模运算
            - 为了使hash桶数组元素分布更均匀，采用取模运算，取模运算就是用第二步得到的值和hash桶数组长度-1的值取与；
            - ```java
              public V computeIfAbsent(K key,
              	Function<? super K, ? extends V> mappingFunction) {
                  // ...
              	if ((first = tab[i = (n - 1) & hash]) != null) {
              ```
            - 这样得到的结果和传统取模运算结果一致，而且效率比取模运算高
        - jdk1.8中put方法的具体步骤
          - 先判断hashmap是否为空，为空的话扩容，不为空计算出key的hash值i
          - 看table[i]是否为空，为空就直接插入，不为空判断当前位置的key和table[i]是否相同，相同就覆盖，不相同就查看table[i]是否是红黑树节点
          - 如果是的话就用红黑树直接插入键值对，如果不是开始遍历链表插入，如果遇到重复值就覆盖，否则直接插入
          - 如果链表长度大于8，转为红黑树结构；
          - 执行完成后看size是否大于阈值threshold，大于就扩容，否则直接结束
      - get方法：计算出要获取元素的hash值，去对应位置取即可。
    - 扩容机制（2）
      - 把数组长度变为原来的两倍；
      - 把旧数组的元素重新计算hash插入到新数组中，在jdk1.8时，不用重新计算hash，只用看看原来的hash值新增的一位是零还是1，如果是1这个元素在新数组中的位置，是原数组的位置加原数组长度，如果是零就插入到原数组中
        - 扩容过程第二部一个非常重要的方法是transfer方法，采用头插法，把旧数组的元素插入到新数组中。
    - hashmap大小为什么是2的幂次方？
      - 在计算插入元素在hash桶数组的索引时第三步，为了使元素分布的更加均匀，用取模操作，但是传统取模操作效率低，然后优化成 h&(length-1)，设置成2幂次方，是因为2的幂次方-1后的值每一位上都是1，然后与第二步计算出的h值与的时候，最终的结果只和key的hashcode值本身有关，这样不会造成空间浪费并且分布均匀，如果不是2的幂次方
      - 如果length不为2的幂，比如15。那么length-1的2进制就会变成1110。在h为随机数的情况下，和1110做&操作。尾数永远为0。那么0001、1001、1101等尾数为1的位置就永远不可能被entry占用。这样会造成浪费，不随机等问题。
    - Java中的HashMap是以键值对(key-value)的形式存储元素的。HashMap需要一个hash函数，它使用hashCode()和equals()方法来向集合/从集合添加和检索元素。当调用put()方法的时候，HashMap会计算key的hash值，然后把键值对存储在集合中合适的索引上。如果key已经存在了，value会被更新成新值。HashMap的一些重要的特性是它的容量(capacity)，负载因子(load factor)和扩容极限(threshold resizing)。
    -
    - https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21090&query=&asc=true&order=&page=22
  - [hashCode()和equals()方法的重要性体现在什么地方？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21092&query=&asc=true&order=&page=24)
    collapsed:: true
    - hashcode和equals组合在一起确定元素的唯一性。
    - 查找元素时，如果单单使用equals来确定一个元素，需要对集合内的元素逐个调用equals方法，效率太低。因此加入了hashcode方法，将元素映射到随机的内存地址上，通过hashcode快速定位到元素（大致）所在的内存地址，再通过使用equals方法确定元素的精确位置。
    - ```java
      public final int hashCode() {
        return Objects.hashCode(key) ^ Objects.hashCode(value);
      }
      ```
    - 比较两个元素时，先比较hashcode，如果hashcode不同，则元素一定不相等
    - 如果相同，再用equals判断。
    - HashMap采用这两个方法实现散列存储，提高键的索引性能。
    - HashSet是基于HashMap实现的。
      - ```java
        public class HashSet<E> extends AbstractSet<E>
            implements Set<E>, Cloneable, java.io.Serializable {
            private transient HashMap<E,Object> map;
            // Dummy value to associate with an Object in the backing Map
            private static final Object PRESENT = new Object();
            public HashSet() {
                map = new HashMap<>();
            }
            ...
        }
        ```
        而HashMap通过Entry实现，Entry是一个内部类，它存储table中每一个位置上的元素值和KEY。
        ```java
                static class Entry<K,V> implements Map.Entry<K,V> {
                    final K key;
                    V value;
                    Entry<K,V> next;
                    int hash;
                    ....
                }
        ```
        HashSet 通过HashMap的key去重（不允许添加重复的entry），HashMap的value使用了Object中的一个对象实例（PRESENT(final)），做了一个空的占位。可以理解HashSet的结构就是：key - value（占位符），这个value不需要具体的意义，只是为了定义这个entry而存在就可以了。
  - [HashMap和Hashtable有什么区别？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21093&query=&asc=true&order=&page=25)
    -
  - [数组(Array)和列表(ArrayList)有什么区别？...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21094&query=&asc=true&order=&page=26)
  - [ArrayList和LinkedList有什么区别？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21095&query=&asc=true&order=&page=27)
  - [Comparable和Comparator接口是干什么的？...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21096&query=&asc=true&order=&page=28)
  - [什么是Java优先级队列(Priority Queue)？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21097&query=&asc=true&order=&page=29)
  - [你了解大O符号(big-O notation)么？你能给出...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21098&query=&asc=true&order=&page=30)
  - [如何权衡是使用无序的数组还是有序的数组？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21099&query=&asc=true&order=&page=31)
  - [Java集合类框架的最佳实践有哪些？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21100&query=&asc=true&order=&page=32)
  - [Enumeration接口和Iterator接口的区别有哪些？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21101&query=&asc=true&order=&page=33)
  - [HashSet和TreeSet有什么区别？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21102&query=&asc=true&order=&page=34)
  - [Java中垃圾回收有什么目的？什么时候进行垃圾回收？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21103&query=&asc=true&order=&page=35)
  - [System.gc()和Runtime.gc()会做什么事情？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21104&query=&asc=true&order=&page=36)
  - [finalize()方法什么时候被调用？析构函数(fina...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21105&query=&asc=true&order=&page=37)
  - [如果对象的引用被置为null，垃圾收集器是否会立即释放对象...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21106&query=&asc=true&order=&page=38)
  - [Java堆的结构是什么样子的？什么是堆中的永久代(Perm...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21107&query=&asc=true&order=&page=39)
  - [串行(serial)收集器和吞吐量(throughput)...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21108&query=&asc=true&order=&page=40)
  - ---
  - [说出三种支持重绘(painting)的组件。](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21129&query=&asc=true&order=&page=61)
  - [什么是裁剪(clipping)？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21130&query=&asc=true&order=&page=62)
  - [MenuItem和CheckboxMenuItem的区别是什么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21131&query=&asc=true&order=&page=63)
  - [边缘布局(BorderLayout)里面的元素是如何布局的？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21132&query=&asc=true&order=&page=64)
  - [网格包布局(GridBagLayout)里面的元素是如何布局的？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21133&query=&asc=true&order=&page=65)
  - [Window和Frame有什么区别？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21134&query=&asc=true&order=&page=66)
  - [裁剪(clipping)和重绘(repainting)有什...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21135&query=&asc=true&order=&page=67)
  - [事件监听器接口(event-listener interf...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21136&query=&asc=true&order=&page=68)
  - [GUI组件如何来处理它自己的事件？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21137&query=&asc=true&order=&page=69)
  - [Java的布局管理器比传统的窗口系统有哪些优势？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21138&query=&asc=true&order=&page=70)
  - [Java的Swing组件使用了哪种设计模式？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21139&query=&asc=true&order=&page=71)
  - ### [[jdbc]]
    - [什么是JDBC？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21140&query=&asc=true&order=&page=72)
      collapsed:: true
      - JDBC是允许用户在不同数据库之间做选择的一个抽象层。JDBC允许开发者用JAVA写数据库应用程序，而不需要关心底层特定数据库的细节。
    - [解释下驱动(Driver)在JDBC中的角色。](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21141&query=&asc=true&order=&page=73)
      collapsed:: true
      - 提供了特定厂商对JDBC API接口类的实现，驱动必须要提供java.sql包下面这些类的实现
        collapsed:: true
        - Connection
        - Statement
        - PreparedStatement
        - CallableStatement
        - ResultSet
        - Driver
    - [Class.forName()方法有什么作用？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21142&query=&asc=true&order=&page=74)
      collapsed:: true
      - 初始化参数指定的类，并且返回此类对应的Class 对象
    - [PreparedStatement比Statement有什么优势？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21143&query=&asc=true&order=&page=75)
      collapsed:: true
      - PreparedStatements是预编译的，因此，性能会更好。同时，不同的查询参数值，PreparedStatement可以重用。
    - [什么时候使用CallableStatement？用来准备CallableStatement的方法是什么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21144&query=&asc=true&order=&page=76)
      collapsed:: true
      - CallableStatement用来执行存储过程。
      - 存储过程是由数据库存储和提供的。
      - 存储过程可以接受输入参数，也可以有返回结果。
      - 鼓励使用存储过程，因为它提供了安全性和模块化。
      - 准备一个CallableStatement的方法是：
        CallableStatement Connection.prepareCall();
    - [数据库连接池是什么意思？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21145&query=&asc=true&order=&page=77)
      collapsed:: true
      - 像打开关闭数据库连接这种和数据库的交互可能是很费时的，尤其是当客户端数量增加的时候，会消耗大量的资源，成本是非常高的
      - 可以在应用服务器启动的时候建立很多个数据库连接并维护在一个池中。连接请求由池中的连接提供。在连接使用完毕以后，把连接归还到池中，以用于满足将来更多的请求
  - [什么是RMI？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21146&query=&asc=true&order=&page=78)
    collapsed:: true
    - Java RMI，Remote Method Invocation，Java的远程方法调用
      mark:: Java所特有的分布式计算技术，它允许运行在一个Java虚拟机上的对象调用运行在另一个Java虚拟机上的对象的方法，从而使Java编程人员可以方便地在网络环境中作分布式计算
    - 面向对象设计要求每个任务由最适合该任务的对象执行，RMI将这个概念更深入了一步，使任务可以在最适合该任务的机器上完成。
    - RMI定义了一组远程接口，可以用于生成远程对象。客户机可以象调用本地对象的方法一样用相同的语法调用远程对象。RMI API提供的类和方法可以处理所有访问远程方法的基础通信和参数引用要求的串行化
    - 使用RMI开发步骤：
      collapsed:: true
      - 1、定义一个远程接口（远程接口必须继承接口，每个方法必须抛出远程异常，方法参数和方法返回值都必须是可序列化的）
      - 2、实现远程接口
      - 3、定义使用远程对象的客户程序
      - 4、产生远程访问对象的桩和框   5、注册远程对象   6、运行服务器和客户程序
  - [RMI体系结构的基本原则是什么？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21147&query=&asc=true&order=&page=79)
    collapsed:: true
    - 基本原则就是把对象的使用和对象的创建相分离，我们在服务器端定义类，定义开放哪些方法，并创建对象；在客户端调用对象的方法
  - [RMI体系结构分哪几层？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21148&query=&asc=true&order=&page=80)
    collapsed:: true
    - ![](https://uploadfiles.nowcoder.com/files/20190325/466357877_1553488666460_thumb525-Archilecture-of-RMI-c69de7547869dfcf6fee3a2bad5e25ae.jpg)
    - 存根和骨架层(Stub and Skeleton layer)
      collapsed:: true
      - 这一层对程序员是透明的，它主要负责拦截客户端发出的方法调用请求，然后把请求重定向给远程的RMI服务。
    - 远程引用层(Remote Reference Layer)
      collapsed:: true
      - RMI体系结构的第二层用来解析客户端对服务端远程对象的引用。这一层解析并管理客户端对服务端远程对象的引用。连接是点到点的。
    - 传输层(Transport layer)
      collapsed:: true
      - 这一层负责连接参与服务的两个JVM。这一层是建立在网络上机器间的TCP/IP连接之上的。它提供了基本的连接服务，还有一些防火墙穿透策略。
  - [RMI中的远程接口(Remote Interface)扮演了什么样的角色？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21149&query=&asc=true&order=&page=81)
    collapsed:: true
    - A remote object is an instance of a class that implements a remote interface. A remote interface extends the interface java.rmi.Remote and declares a set of remote methods. Each remote method must declarejava.rmi.RemoteException (or a superclass of RemoteException)
       来自：https://docs.oracle.com/javase/8/docs/technotes/guides/rmi/hello/hello-world.html
  - [java.rmi.Naming类扮演了什么样的角色？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21150&query=&asc=true&order=&page=82)
  - [RMI的绑定(Binding)是什么意思？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21151&query=&asc=true&order=&page=83)
  - [Naming类的bind()和rebind()方法有什么区别？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21152&query=&asc=true&order=&page=84)
  - [让RMI程序能正确运行有哪些步骤？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21153&query=&asc=true&order=&page=85)
  - [RMI的stub扮演了什么样的角色？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21154&query=&asc=true&order=&page=86)
  - [什么是分布式垃圾回收(DGC)？它是如何工作的？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21155&query=&asc=true&order=&page=87)
  - [RMI中使用RMI安全管理器(RMISecurityMan...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21156&query=&asc=true&order=&page=88)
  - [解释下Marshalling和demarshalling。](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21157&query=&asc=true&order=&page=89)
  - [解释下Serialization和Deserializat...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21158&query=&asc=true&order=&page=90)
  - [什么是Servlet？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21159&query=&asc=true&order=&page=91)
  - [说一下Servlet的体系结构。](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21160&query=&asc=true&order=&page=92)
  - [Applet和Servlet有什么区别？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21161&query=&asc=true&order=&page=93)
  - [GenericServlet和HttpServlet有什么区别？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21162&query=&asc=true&order=&page=94)
  - [解释下Servlet的生命周期。](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21163&query=&asc=true&order=&page=95)
  - [doGet()方法和doPost()方法有什么区别？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21164&query=&asc=true&order=&page=96)
  - [什么是Web应用程序？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21165&query=&asc=true&order=&page=97)
  - [什么是服务端包含(Server Side Include)？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21166&query=&asc=true&order=&page=98)
    collapsed:: true
    - 服务端包含(SSI)是一种简单的解释型服务端脚本语言，大多数时候仅用在Web上，用servlet标签嵌入进来。SSI最常用的场景把一个或多个文件包含到Web服务器的一个Web页面中。当浏览器访问Web页面的时候，Web服务器会用对应的servlet产生的文本来替换Web页面中的servlet标签。
    - 如果增加的动态内容少，就用SSI，如果整个页面大多数都需要动态加载，则可以使用cgi提供整个页面，或者使用其他的动态技术。
  - [什么是Servlet链(Servlet Chaining)？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21167&query=&asc=true&order=&page=99)
  - [如何知道是哪一个客户端的机器正在请求你的Servlet？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21168&query=&asc=true&order=&page=100)
  - [HTTP响应的结构是怎么样的？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21169&query=&asc=true&order=&page=101)
  - [什么是cookie？session和cookie有什么区别？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21170&query=&asc=true&order=&page=102)
  - [浏览器和Servlet通信使用的是什么协议？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21171&query=&asc=true&order=&page=103)
  - [什么是HTTP隧道？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21172&query=&asc=true&order=&page=104)
  - [sendRedirect()和forward()方法有什么区别？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21173&query=&asc=true&order=&page=105)
  - [什么是URL编码和URL解码？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21174&query=&asc=true&order=&page=106)
    collapsed:: true
    - URL编码是负责把URL里面的空格和其他的特殊字符替换成对应的十六进制表示，反之就是解码。
  - [什么是JSP页面？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21175&query=&asc=true&order=&page=107)
  - [JSP请求是如何被处理的？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21176&query=&asc=true&order=&page=108)
  - [JSP有什么优点？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21177&query=&asc=true&order=&page=109)
  - [什么是JSP指令(Directive)？JSP中有哪些不同...](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21178&query=&asc=true&order=&page=110)
  - [什么是JSP动作(JSP action)？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21179&query=&asc=true&order=&page=111)
  - [什么是Scriptlets？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21180&query=&asc=true&order=&page=112)
  - [声明(Decalaration)在哪里？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21181&query=&asc=true&order=&page=113)
  - [什么是表达式(Expression)？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21182&query=&asc=true&order=&page=114)
  - [隐含对象是什么意思？有哪些隐含对象？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21183&query=&asc=true&order=&page=115)
  - [面向对象软件开发的优点有哪些？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21184&query=&asc=true&order=&page=116)
  - [封装的定义和好处有哪些？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21185&query=&asc=true&order=&page=117)
  - [多态的定义？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21186&query=&asc=true&order=&page=118)
  - [继承的定义？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21187&query=&asc=true&order=&page=119)
  - [抽象的定义？抽象和封装的不同点？](https://www.nowcoder.com/ta/review-java/review?tpId=31&tqId=21188&query=&asc=true&order=&page=120)
  -