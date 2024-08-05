also:: java 容器, java 集合
description:: a framework that provides an architecture to store and manipulate(操纵) the group of objects
description:: from java 1.2
tags:: #[[java02]]

- #+BEGIN_NOTE
  灵活性(存储, 类型, 数量, 映射关系) > 数组
  #+END_NOTE
-
- Map/Hierarchy of Collection Framework
  - Iterable
    - Collection
      - List
        id:: 632dca84-78bc-41b6-b6fa-8a5af022a7e2
        - Vector
          id:: 632dcab0-65f1-4abb-b354-3d3245d1ae5a
          - Stack
        - ArrayList
          id:: 632dcaab-2ecb-412b-80d5-03a1c8464039
        - LinkedList
          id:: 632dca98-ffb9-4184-9941-ee414e0cb3f7
      - Queue
        id:: 632dca85-724d-47f1-8c94-374e45c73cf5
        - Deque
          id:: 632dcabb-11e0-44e3-9dc5-4650a37729b6
          - ((632dca98-ffb9-4184-9941-ee414e0cb3f7))
            id:: 632dcac1-b50a-4f71-ae40-564de514dda9
          - ArrayDeque
            id:: 632dcaf4-a182-43d6-8b59-2a4a519c22bf
        - PriorityQueue
          id:: 632dcaca-395d-4641-9c76-764882a6bbc1
      - Set
        id:: 632dca8a-b676-42b3-a86b-731ee1b2ae20
        - SortedSet
          - TreeSet
            id:: 632dcf22-9be9-4d21-95f0-25ce123e6ffa
        - HashSet
          id:: 632dcb0c-b678-48bd-a06a-a1918892a55b
          - LinkedHashSet
            id:: 632dcb10-70cb-477e-aea4-479701e77e8b
  - Map
    id:: 632dca8e-3286-4ea0-b0eb-f631076beece
    - HashTable
      id:: 632dcb31-df51-443f-978d-4741a4061228
    - HashMap
      id:: 632dcb36-cd98-4c18-ae97-566e0241b807
    - SortedMap
      - TreeMap
        id:: 632dcb3a-4de2-4e94-98e4-0fa89e3e9ca1
  - ![image.png](../../soul/assets/image_1652522212837_0.png){:height 479, :width 747}
    (省略了AbstractList, NavigableSet等抽象类以及其他的一些辅助)
  - [[java-interview]]
    - Map 没有继承 iterable, 却可以使用迭代器?
      - Map及其子类虽然没有实现Interable、Iterator，但是，Map内部生成Collection，从而间接实现Iterable接口和生成Iterator，所以，Map也可以使用迭代器。
      - via: [map没有继承iterable，为什么可以使用迭代器_百度知道](https://zhidao.baidu.com/question/1771462425941801540.html)
-
- Implements
  - Collection
    - ((632dca84-78bc-41b6-b6fa-8a5af022a7e2))
      - **List** 均按添加时的顺序存放，不自动排序
      - ((632dcab0-65f1-4abb-b354-3d3245d1ae5a)) vs ((632dcaab-2ecb-412b-80d5-03a1c8464039))
        - | **Items** | **Vector**| **Arraylist** |
          | **底层**  | `Object[]`|
          | **地位** | 古老实现 | 主要实现 |
          | **线程安全** | ✖ | ✔ |
      - ((632dcaab-2ecb-412b-80d5-03a1c8464039)) vs ((632dca98-ffb9-4184-9941-ee414e0cb3f7))
        - | **Items** | **Arraylist** | **LinkedList** |
          | **线程安全** | ✖| ✖|
          | **底层** | Object [] | ~~循环链表~~ 双向链表(>=JDK1.7) |
          | **插/删 受元素位置影响** | ✔ O(n/2) | ✖ O(1) |
          | **快速随机访问**  | ✔| ✖|
          | **内存占用** | 结尾需要预留出空间 | 原子元素更多(前驱后继)|
      - ((632dcab0-65f1-4abb-b354-3d3245d1ae5a)) vs ((632dcaab-2ecb-412b-80d5-03a1c8464039)) vs ((632dca98-ffb9-4184-9941-ee414e0cb3f7))
        - 三者都是有序集合, 功能也比较近似, 但在行为、性能、线程安全等方面，有很大不同 (具体设计)
        - Vector 是 Java 早期提供的 **线程安全的动态数组** ，如果不需要线程安全，并不建议选择，毕竟同步是有额外开销的。Vector 内部是使用对象数组来保存数据，可以根据需要自动的增加容量，当数组已满时，会创建新的数组，并拷贝原有数组数据。
        - ArrayList 是应用更加广泛的 **动态数组** 实现，它本身不是线程安全的，所以性能要好很多。与 Vector 近似，ArrayList 也是可以根据需要调整容量，不过两者的调整逻辑有所区别，Vector 在扩容时会提高 1 倍，而 ArrayList 则是增加 50%。
        - LinkedList 顾名思义是 Java 提供的 **双向链表** ，所以它不需要像上面两种那样调整容量，它也不是线程安全的。
      - ArrayList 的扩容机制
      - RandomAccess 接口
    - ((632dca85-724d-47f1-8c94-374e45c73cf5))
      - ((632dca85-724d-47f1-8c94-374e45c73cf5)) vs ((632dcabb-11e0-44e3-9dc5-4650a37729b6))
        - | **Queue 接口** | **抛出异常**  | **返回特殊值** |
            | ------------ | --------- | ---------- |
            | **插入队尾**     | add(E e)  | offer(E e) |
            | **删除队首**     | remove()  | poll()     |
            | **查询队首元素** | element() | peek()     |
        - | **Deque 接口** | **抛出异常**      | **返回特殊值**      |
            | ------------ | ------------- | --------------- |
            | **插入队首**     | addFirst(E e) | offerFirst(E e) |
            | **插入队尾**     | addLast(E e)  | offerLast(E e)  |
            | **删除队首**     | removeFirst() | pollFirst()     |
            | **删除队尾**     | removeLast()  | pollLast()      |
            | **查询队首元素** | getFirst()    | peekFirst()     |
            | **查询队尾元素** | getLast()     | peekLast()      |
          - Deque 还提供有 push() 和 pop() 等其他方法，可用于模拟栈
      - ((632dcaf4-a182-43d6-8b59-2a4a519c22bf)) vs ((632dca98-ffb9-4184-9941-ee414e0cb3f7))
        - | **Items** | **ArrayDeque** | **LinkedList** |
          | **Deque 接口** | ✔|✔|
          | **队列性质**| ✔|✔|
          | **底层** | 可变长数组和双指针 | 链表 |
          | **存储 NULL 数据** | ✖|✔|
          | **JDK** | >=1.6 | >=1.2|
          | **性能**|除扩容外, O(1)| 申请堆空间, 更慢|
        - ArrayDeque 也可以用于实现栈
      - ((632dcaca-395d-4641-9c76-764882a6bbc1))
        id:: 6280df76-268a-436e-9011-5dc3ed99e294
        - \>=  JDK1.5
        - 二叉堆
          - 底层使用可变长的数组来存储数据
        - 堆元素的上浮和下沉
          - O(logn) 的时间复杂度内插入元素和删除堆顶元素
        - 非线程安全的
          - 不支持存储 NULL 和 non-comparable 的对象
        - 默认是小顶堆，但可以接收一个 Comparator 作为构造参数，从而来自定义元素优先级的先后
      - TODO 手撕算法, 堆排序、求第K大的数、带权图的遍历
    - ((632dca8a-b676-42b3-a86b-731ee1b2ae20))
      - **Set** 默认按自然顺序排序，可通过构造器传入自定义的比较器自定义排序策略，**但是，**LinkedHashSet无序
      - ((632dcb0c-b678-48bd-a06a-a1918892a55b)) vs ((632dcb10-70cb-477e-aea4-479701e77e8b)) vs ((632dcf22-9be9-4d21-95f0-25ce123e6ffa))
        - | **Items** | **HashSet** | **LinkedHashSet** | **TreeSet**|
          | **Set 接口实现**| ✔|✔ |✔ |
          | **元素唯一**| ✔| ✔| ✔|
          | **线程安全**|✖|✖|✖|
          | **底层** | 哈希表`HashMap` | 链表(FIFO) + 哈希表 | 红黑树(有序) |
          | **应用场景** | 不保证元素顺序| 保证顺序满足 FIFO | 自定义排序 |
      - `comparable` vs `Comparator`
        - `comparable` 接口
          - from: java.lang包
          - `compareTo(Object obj)` 排序
        - `comparator` 接口
          - from: `java.util` 包
          - `compare(Object obj1, Object obj2)` 排序
      - 无序性 / 不可重复性 含义
        - 无序性
          - 存储的数据在底层数组中并非按照数组索引的顺序添加 ，而是根据数据的哈希值决定的
        - 不可重复性
          - 添加的元素按照 equals()判断时 ，返回 false，需要同时重写 equals()方法和 HashCode()方法
  - ((632dca8e-3286-4ea0-b0eb-f631076beece))
    - **HashMap, TreeMap, ConcurrentHashMap 是有序的**
    - ~~**Hashtable, LinkedHashMap 不是有序的**~~
    - ((632dcb36-cd98-4c18-ae97-566e0241b807)) vs ((632dcb31-df51-443f-978d-4741a4061228))
      - | **Items** | **HashMap** | **Hashtable** |
        | **线程安全** | ✖ | ✔ (`synchronized` 修饰)|
        | **效率**(基于第一点) | 较高 | 遗留类, 很多冗余, 不如用[:br] `ConcurrentHashMap`|
        | **Null key / Null value** | ✔|✖|
        | **初始 / 扩容 容量**| 16-> 16*2; N->$$2^{N}$$(`tableSizeFor()`) | 11->2n+1|
        | **底层** | >=1.8, 链表长>8, 数组>64, 转换红黑树 | ✖|
    - ((632dcb36-cd98-4c18-ae97-566e0241b807)) vs ((632dcb0c-b678-48bd-a06a-a1918892a55b))
      - |               **HashMap**                |                          **HashSet**                           |
        | :------------------------------------: | :----------------------------------------------------------: |
        |           实现了 `Map` 接口            |                       实现 `Set` 接口                        |
        |               存储键值对               |                          仅存储对象                          |
        |     调用 `put()`向 map 中添加元素      |             调用 `add()`方法向 `Set` 中添加元素              |
        | `HashMap` 使用键（Key）计算 `hashcode` | `HashSet` 使用成员对象来计算 `hashcode` 值，对于两个对象来说 `hashcode` 可能相同，所以`equals()`方法用来判断对象的相等性 |
    - ((632dcb36-cd98-4c18-ae97-566e0241b807)) vs ((632dcb3a-4de2-4e94-98e4-0fa89e3e9ca1))
      id:: 6281aacf-fca1-4b5e-a89c-8134870db5ff
      - ![image.png](../../soul/assets/image_1652685166712_0.png)
  - 底层 -> ((632dca84-78bc-41b6-b6fa-8a5af022a7e2)) vs ((632dca8a-b676-42b3-a86b-731ee1b2ae20)) vs ((632dca85-724d-47f1-8c94-374e45c73cf5)) vs ((632dca8e-3286-4ea0-b0eb-f631076beece))
    - ((632dca84-78bc-41b6-b6fa-8a5af022a7e2))
      - `Arraylist`
        - `Object[]` 数组
      - `Vector`
        - `Object[]` 数组
      - `LinkedList`
        - 双向链表(JDK1.6 之前为循环链表，JDK1.7 取消了循环)
    - ((632dca8a-b676-42b3-a86b-731ee1b2ae20))
      - `HashSet`(无序，唯一)
        - 基于 `HashMap` 实现的，底层采用 `HashMap` 来保存元素
      - `LinkedHashSet`
        - `HashSet` 的子类
        - 内部是通过 `LinkedHashMap` 实现的。有点类似于我们之前说的 `LinkedHashMap` 其内部是基于 `HashMap` 实现一样，不过还是有一点点区别的
      - `TreeSet`(有序，唯一)
        - 红黑树(自平衡的排序二叉树)
    - Queue
      - `PriorityQueue`
        - `Object[]` 数组来实现二叉堆
      - `ArrayQueue`
        - `Object[]` 数组 + 双指针
    - Map
      - `HashMap`
        - JDK1.8 之前 `HashMap` 由数组+链表组成的，数组是 `HashMap` 的主体，链表则是主要为了解决哈希冲突而存在的（“拉链法”解决冲突）。JDK1.8 以后在解决哈希冲突时有了较大的变化，当链表长度大于阈值（默认为 8）（将链表转换成红黑树前会判断，如果当前数组的长度小于 64，那么会选择先进行数组扩容，而不是转换为红黑树）时，将链表转化为红黑树，以减少搜索时间
      - `LinkedHashMap`
        - `LinkedHashMap` 继承自 `HashMap`，所以它的底层仍然是基于拉链式散列结构即由数组和链表或红黑树组成。另外，`LinkedHashMap` 在上面结构的基础上，增加了一条双向链表，使得上面的结构可以保持键值对的插入顺序。同时通过对链表进行相应的操作，实现了访问顺序相关逻辑。详细可以查看：[《LinkedHashMap 源码详细分析（JDK1.8）》open in new window](https://www.imooc.com/article/22931)
      - `Hashtable`
        - 数组+链表组成的，数组是 `Hashtable` 的主体，链表则是主要为了解决哈希冲突而存在的
      - `TreeMap`
        - 红黑树（自平衡的排序二叉树）
  - [ConcurrentMap 是一个接口，它是 Map 接口的扩展](https://www.baeldung.com/java-concurrent-map)[1](https://www.baeldung.com/java-concurrent-map)[。它的目的是提供一个结构和指导，来解决吞吐量和线程安全之间的问题](https://www.baeldung.com/java-concurrent-map)[1](https://www.baeldung.com/java-concurrent-map)[。通过覆盖一些接口默认方法，ConcurrentMap 给出了有效实现的指导，以提供线程安全和内存一致性的原子操作](https://www.baeldung.com/java-concurrent-map)[1](https://www.baeldung.com/java-concurrent-map)[2](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentMap.html)[1](https://www.baeldung.com/java-concurrent-map)。
  - [ConcurrentHashMap 是一个 Java 类，它实现了 ConcurrentMap 和 Serializable 接口](https://stackoverflow.com/questions/2836267/concurrenthashmap-in-java)[1](https://stackoverflow.com/questions/2836267/concurrenthashmap-in-java)[。它是 HashMap 的一个改进，可以在多线程环境下提高性能](https://stackoverflow.com/questions/2836267/concurrenthashmap-in-java)[1](https://stackoverflow.com/questions/2836267/concurrenthashmap-in-java)[2](https://dzone.com/articles/how-concurrenthashmap-works-internally-in-java)[。ConcurrentHashMap 允许多个线程并发地访问 map，而不需要对整个 map 加锁，只需要对 map 的一部分（称为 Segment）加锁](https://dzone.com/articles/how-concurrenthashmap-works-internally-in-java)[2](https://dzone.com/articles/how-concurrenthashmap-works-internally-in-java)[3](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentHashMap.html)[。ConcurrentHashMap 还可以用作可扩展的频率 map（一种直方图或多重集合），通过使用 LongAdder 值和 computeIfAbsent 方法](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentHashMap.html)[3](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentHashMap.html)。
- Refs
  - [Collections in Java - javatpoint](https://www.javatpoint.com/collections-in-java)
  - [极客时间 | Java核心技术36讲](http://www.gcjlovecl.ltd/02-Java%E6%A0%B8%E5%BF%83%E6%8A%80%E6%9C%AF36%E8%AE%B2/02-%E6%A8%A1%E5%9D%97%E4%B8%80%20Java%E5%9F%BA%E7%A1%80%20%2814%E8%AE%B2%29/%E7%AC%AC08%E8%AE%B2%E4%B8%A8%E5%AF%B9%E6%AF%94Vector%E3%80%81ArrayList%E3%80%81LinkedList%E6%9C%89%E4%BD%95%E5%8C%BA%E5%88%AB%EF%BC%9F.html)
  - [你必须知道的几种java容器（集合类）_晚秋星辰的博客-CSDN博客](https://blog.csdn.net/dengpeng0419/article/details/47983033)
  - [Java 集合存入数据时会自动排序吗？ - 知乎](https://zhuanlan.zhihu.com/p/55840526)
-
-