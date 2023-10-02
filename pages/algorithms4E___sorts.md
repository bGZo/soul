title:: algorithms4E/sorts
tags:: [[sort]]

- 初级排序
  - 游戏规则
    collapsed:: true
    - 元素通常都是对象，对主键的抽象描述则是通过一种内置的机制来完成的
      collapsed:: true
      - ((62621cd7-2331-432a-bb71-a73418700c77))
    - 将排序代码放在类的sort()方法中，该类还将包含辅助函数less()和exch()（可能还有其他辅助函数）以及一个示例用例main()
      collapsed:: true
      - 早期调试使用的代码
        - 测试用例main()将标准输入得到的字符串排序，并用私有方法show()打印字符数组的内容
    - 大多数情况下，排序代码只通过两个方法操作数据
      collapsed:: true
      - less()方法对元素进行比较
      - exch()方法将元素交换位置
    - 模板
      collapsed:: true
      - ```java
        public class Example
        {
            public static void sort(Comparable[] a)
            {  /＊ 请见算法2.1、算法2.2、算法2.3、算法2.4、算法2.5或算法2.7＊/ }
            private static boolean less(Comparable v, Comparable w)
            {  return v.compareTo(w) ＜ 0;  }
            private static void exch(Comparable[] a, int i, int j)
            {  Comparable t = a[i]; a[i] = a[j]; a[j] = t;  }
            private static void show(Comparable[] a)
            {  // 在单行中打印数组
              for (int i = 0; i ＜ a.length; i++)
                  StdOut.print(a[i] + " ");
              StdOut.println();
            }
            public static boolean isSorted(Comparable[] a)
            {  // 测试数组元素是否有序
              for (int i = 1; i ＜ a.length; i++)
                  if (less(a[i], a[i-1]))  return false;
              return true;
          }
          public static void main(String[] args)
          {  // 从标准输入读取字符串，将它们排序并输出
              String[] a = In.readStrings();
              sort(a);
              assert isSorted(a);
              show(a);
          }
        }
        ```
    - 验证
      collapsed:: true
      - 在测试代码中添加一条语句 assertisSorted(a)；来确认排序后数组元素都是有序的
        collapsed:: true
        - 注:
          - 如果我们只使用exch()来交换数组的元素，这个测试就足够了
          - 当我们直接将值存入数组中时，这条语句无法提供足够的保证
            - 如，把初始输入数组的元素全部置为相同的值也能通过这个测试
    - 运行时间
      collapsed:: true
      - 排序成本模型
        collapsed:: true
        - 计算比较和交换的数量
        - 对于不交换元素的算法，我们会计算访问数组的次数。
    - 额外的内存使用
      collapsed:: true
      - 原地排序算法
      - 其他排序算法
    - 数据类型
      collapsed:: true
      - 遵守Java惯例的好处 -> **很多可以排序的数据都实现了Comparable接口** -> 直接用这些类型的数组作为参数调用我们的排序方法
        id:: 62621cd7-2331-432a-bb71-a73418700c77
        collapsed:: true
        - Java中封装数字的类型 Integer 和 Double，以及 String 和 其他许多高级数据类型 (File / URL) 都实现了Comparable接口
      - `compareTo()` 必须实现一个全序关系 (`v.compareTo(w)`)
        - 全序关系 / 线性顺序 (total order / linear order)
          - 性质
            collapsed:: true
            - 自反性，对于所有的v, v=v
            - 反对称性，对于所有的v＜w都有v＞w，且v=w时w=v
            - 传递性，对于所有的v、w和x，如果v＜=w且w＜=x，则v＜=x
          - 满足全序关系的集合叫做全序集合、线性序集合、简单序集合或链
            - 链还常用来描述偏序集合的全序子集
          - 全序关系的完全性 -> 集合中的任何一对元素都是可相互比较的。
          - 全序关系 ==（满足“完全性”条件的）偏序关系。
            - 完全性条件蕴涵了自反性：$${\displaystyle a\leq a}$$
      - ![image.png](../assets/image_1650601039121_0.png)
        collapsed:: true
        - `compareTo()`: 给出了实现了 `Comparable`接口的任意数据类型的对象的大小顺序的定义
      -
  - 选择排序
    collapsed:: true
    - 特点
      collapsed:: true
      - 运行时间和输入无关
      - 数据移动是最少的
    - ![image.png](../assets/image_1650607873608_0.png)
      - ==对于长度为 N 的数组，选择排序需要大约== $$\frac{N^{2}}{2}$$ ==次比较和 N 次交换==
        - 可以通过算法的排序轨迹来证明这一点。我们用一张N×N的表格来表示排序的轨迹（见算法2.1下部的表格），其中每个非灰色字符都表示一次比较。表格中大约一半的元素不是灰色的——即对角线和其上部分的元素。对角线上的每个元素都对应着一次交换。通过查看代码我们可以更精确地得到，0到N-1的任意i都会进行一次交换和N-1-i次比较，因此总共有N次交换以及（N-1）+（N-2）+...+2+1=N（N-1）/2～N2/2次比较。
    - ```java
      public class Selection
      {
          public static void sort(Comparable[] a)
          {  // 将a[]按升序排列
            int N = a.length;                 // 数组长度
            for (int i = 0; i ＜ N; i++)
            {  // 将a[i]和a[i+1..N]中最小的元素交换
                int min = i;                   // 最小元素的索引
                for (int j = i+1; j ＜ N; j++)
                  if (less(a[j], a[min])) min = j;
                exch(a, i, min);
            }
          }
          // less()、exch()、isSorted()和main()方法见“排序算法类模板”
      }
      ```
  - 插入排序
    collapsed:: true
    - ![image.png](../assets/image_1650608253781_0.png)
      - 插入排序所需的时间取决于输入中元素的初始顺序
        - 如，对一个很大且其中的元素已经有序（或接近有序）的数组进行排序将会比对随机顺序的数组或是逆序数组进行排序要快得多
      - ==对于随机排列的长度为N且主键不重复的数组==
        id:: 62624921-6e74-4559-92f8-af710946b2db
        - 平均情况下插入排序需要 $$\frac{N^{2}}{4}$$ 次比较以及 $$\frac{N^{2}}{4}$$ 次交换
        - 最坏情况下需要 $$\frac{N^{2}}{2}$$ 次比较和 $$\frac{N^{2}}{2}$$ 次交换
        - 最好情况下需要 $$N-1$$ 次比较和 $$0$$ 次交换
        - 证明
          collapsed:: true
          - 和命题A一样，通过一个N×N的轨迹表可以很容易就得到交换和比较的次数。最坏情况下对角线之下所有的元素都需要移动位置，最好情况下都不需要。对于随机排列的数组，在平均情况下每个元素都可能向后移动半个数组的长度，因此交换总数是对角线之下的元素总数的二分之一。比较的总次数是交换的次数加上一个额外的项，该项为N减去被插入的元素正好是已知的最小元素的次数。在最坏情况下（逆序数组），这一项相对于总数可以忽略不计；在最好情况下（数组已经有序），这一项等于N-1。
    - ```java
      public class Insertion
      {
          public static void sort(Comparable[] a)
          {  // 将a[]按升序排列
            int N = a.length;
            for (int i = 1; i ＜ N; i++)
            {  // 将a[i] 插入到a[i-1]、a[i-2]、a[i-3]..．之中
                for (int j = i; j ＞ 0 && less(a[j], a[j-1]); j--)
                  exch(a, j, j-1);
            }
        }
        // less()、exch()、isSorted()和main()方法见“排序算法类模板”
      }
      ```
    - 适用几种典型的部分有序的数组 (选择排序则不然)
      collapsed:: true
      - 数组中每个元素距离它的最终位置都不远
      - 一个有序的大数组接一个小数组
      - 数组中只有几个元素的位置不正确
    - ==当倒置的数量很少时，插入排序很可能比本章中的其他任何算法都要快==
      collapsed:: true
      - 插入排序需要的交换操作和数组中倒置的数量相同，需要的比较次数大于等于倒置的数量，小于等于倒置的数量加上数组的大小再减一
        - 证明
          - 每次交换都改变了两个顺序颠倒的元素的位置，相当于减少了一对倒置，当倒置数量为0时，排序就完成了。每次交换都对应着一次比较，且1到N-1之间的每个i都可能需要一次额外的比较（在a[i]没有达到数组的左端时）。
  - 可视化
    collapsed:: true
    - 棒状图
    - 最复杂的部分是设置y轴的比例以使轨迹的线条符合预期的顺序
  - 比较两种排序算法
    collapsed:: true
    - ((62621bf8-7075-46ad-80f4-caf849a72af9))
    - ((62621bf8-e550-4f8a-8963-5d8695b96478))
    - ((62621bf8-3b2c-4447-873f-80628f8ce9fb))
    - ((62621bf8-db10-4230-a332-7cb4d51d8225))
    - ((62621bf8-430c-4867-a813-ab0690fa9614))
    - ((62621bf8-9bea-422c-ae24-84d1075867af))
    - ((62621bf8-5232-416c-80bd-53f53e9dd25b))
      - ((62621bf8-49a0-4216-af2b-f816a5f0878c))
    - 每个程序员都知道只有经过长期的调试和改进才能得到这样的代码，每个数学家都知道正确分析的难度，每个科学家也都知道从提出猜想到设计并执行实验来验证它们是多么费心。只有研究那些最重要的算法的专家才会经历完整的研究过程，但每个使用算法的程序员都应该了解算法的性能特性背后的科学过程
    - ==对于随机排序的无重复主键的数组，插入排序和选择排序的运行时间是平方级别的，两者之比应该是一个较小的常数==
      collapsed:: true
      - 例证。这个结论在过去的半个世纪中已经在许多不同类型的计算机上经过了验证。在1980年本书第1版完成之时插入排序就比选择排序快一倍，现在仍然是这样，尽管那时这些算法将10万条数据排序需要几个小时而现在只需要几秒钟。在你的计算机上插入排序也比选择排序快一些吗？可以通过SortCompare类来检测。它会使用由命令行参数指定的排序算法名称所对应的sort()方法进行指定次数的实验（将指定大小的数组排序），并打印出所观察到的各种算法的运行时间的比例。
    - ```java
      public class SortCompare
      {
          public static double time(String alg, Double[] a)
          {  
            Stopwatch timer=new Stopwatch();
            if(alg.equals("Insertion"))   Insertion.sort(a);
            if(alg.equals("Selection"))   Selection.sort(a);
            if(alg.equals("Shell"))     Shell.sort(a);
            if(alg.equals("Merge"))     Merge.sort(a);
            if(alg.equals("Quick"))     Quick.sort(a);
            if(alg.equals("Heap"))    Heap.sort(a);
            return timer.elapsedTime();
          }
          public static double timeRandomInput(String alg, int N, int T)
          {  // 使用算法alg将T个长度为N的数组排序
            double total = 0.0;
            Double[] a = new Double[N];
            for (int t = 0; t ＜ T; t++)
            {  // 进行一次测试（生成一个数组并排序)
                for (int i = 0; i ＜ N; i++)
                  a[i] = StdRandom.uniform();
                total += time(alg, a);
            }
            return total;
          }
          public static void main(String[] args)
          {
            String alg1 = args[0];
            String alg2 = args[1];
            int N = Integer.parseInt(args[2]);
            int T = Integer.parseInt(args[3]);
            double t1 = timeRandomInput(alg1, N, T); // 算法1的总时间
            double t2 = timeRandomInput(alg2, N, T); // 算法2的总时间
            StdOut.printf(“For %d random Doubles\n    %s is”, N, alg1);
            StdOut.printf(“ %.1f times faster than %s\n”, t2/t1, alg2);
          }
      }
      ```
    -
  - 希尔排序
    collapsed:: true
    - 基于插入排序的快速的排序算法
    - 思想
      collapsed:: true
      - 使数组中任意间隔为 h 的元素都是有序的。这样的数组被称为 **h有序数组**
        - 一个 h有序数组 就是 h 个互相独立的有序数组编织在一起组成的一个数组
          id:: 626256ed-726c-4bd8-a124-b9a51f2dc91e
        - ![image.png](../assets/image_1650611987892_0.png)
        - 在进行排序时，如果h很大，我们就能将元素移动到很远的地方，为实现更小的h有序创造方便。用这种方式，对于任意以1结尾的h序列，我们都能够将数组排序。这就是希尔排序。
        - 实现希尔排序的一种方法是对于每个h，用插入排序将h个子数组独立地排序。
          - 一个更简单的方法是在h-子数组中将每个元素交换到比它大的元素之前去（将比它大的元素向右移动一格）
            - 因为子数组是相互独立的
            - 只需要在插入排序的代码中将移动元素的距离由1改为h即可
              - 希尔排序的实现就转化为了一个类似于插入排序但使用不同增量的过程
        - 高效原因
          - 权衡了子数组的规模和有序性。
            - 排序之初，各个子数组都很短，排序之后子数组都是部分有序的，这两种情况都很适合插入排序。子数组部分有序的程度取决于递增序列的选择。透彻理解希尔排序的性能至今仍然是一项挑战。实际上，算法2.3是我们唯一无法准确描述其对于乱序的数组的性能特征的排序方法。
              id:: 626258ef-396f-4128-acdf-fd403d8b8f54
    - collapsed:: true
      ```java
      public class Shell
      {
          public static void sort(Comparable[] a)
          {  // 将a[]按升序排列
            int N = a.length;
            int h = 1;
            while (h ＜ N/3) h = 3＊h + 1; // 1, 4, 13, 40, 121, 364, 1093, ...
            while (h ＞= 1)
            {  // 将数组变为h有序
                for (int i = h; i ＜ N; i++)
                {  // 将a[i]插入到a[i-h], a[i-2＊h], a[i-3＊h]..．之中
                  for (int j = i; j ＞= h && less(a[j], a[j-h]); j -= h)
                      exch(a, j, j-h);
                }
                h = h/3;
            }
          }
          // less()、exch()、isSorted()和main()方法见“排序算法类模板”
      }
      ```
      - ![image.png](../assets/image_1650612916706_0.png)
      - ![image.png](../assets/image_1650612971455_0.png)
      -
      - 性能
        id:: 62625e00-4730-4060-9427-d38f8855e017
        - 目前最重要的结论是它的运行时间达不到平方级别
          - 已知在最坏的情况下比较次数和 $$\frac{N^{3}}{2}$$ 成正比
    - 优点
      - 对于中等大小的数组它的运行时间是可以接受的
      - 它的代码量很小
      - 不需要使用额外的内存空间
    - 通过提升速度来解决其他方式无法解决的问题是研究算法的设计和性能的主要原因之一
    - 研究希尔排序性能需要的数学论证超出了本书范围
      collapsed:: true
      - 如果你不相信，可以从证明下面这一点开始：
        - 当一个“h有序”的数组按照增幅k排序之后，它仍然是“h有序”的。
    - ==使用递增序列1, 4, 13, 40, 121, 364…的希尔排序所需的比较次数不会超出N的若干倍乘以递增序列的长度==
      collapsed:: true
      - 证
        - 记录算法2.3中比较的数量并将其除以使用的序列长度是一道简单的练习（请见练习2.1.12）。大量的实验证明平均每个增幅所带来的比较次数约为N1/5，但只有在N很大的时候这个增长幅度才会变得明显。这个性质似乎也和输入模型无关
    - 如果你需要解决一个排序问题而又没有系统排序函数可用（例如直接接触硬件或是运行于嵌入式系统中的代码），可以先用希尔排序，然后再考虑是否值得将它替换为更加复杂的排序算法
  - [[java/quick-refs]]
    collapsed:: true
    - 排序看起来是个很简单的问题，我们用计算机不是可以做很多更有意思的事情吗？
      - 排序算法今天仍然值得我们学习是因为它易于理解，你能从中领会到许多精妙之处。
    - 为什么有这么多排序算法？
      - 原因之一是许多排序算法的性能都和输入模型有很大的关系，因此不同的算法适用于不同应用场景中的不同输入。例如，对于部分有序和小规模的数组应该选择插入排序。其他限制条件，例如空间和重复的主键，也都是需要考虑的因素
    - 为什么要使用less()和exch()这些不起眼的辅助函数？
      - 它们抽象了所有排序算法都会用到的共同操作，这种抽象使得代码更便于理解。而且它们增强了代码的可移植性。
    - 为什么每次的结果都不一样（而且和书上的也不相同）
      - 大量的重复实验可以淡化这种干扰，我们的经验是现如今算法性能的微小差异很难观察。这就是我们要关注较大差异的原因。
  - TODO exercise
- 归并排序
  - 优点: **保证将任意长度为N的数组排序所需时间和** $$NlogN$$ **成正比**
  - 缺点: 它所需的额外空间和N成正比
  - ![image.png](../assets/image_1650615662823_0.png)
  - 原地归并
    collapsed:: true
    - ```java
      public static void merge(Comparable[] a, int lo, int mid, int hi)
      {  // 将a[lo..mid] 和a[mid+1..hi] 归并
          int i = lo, j = mid+1;
          for (int k = lo; k ＜= hi; k++)  // 将a[lo..hi]复制到aux[lo..hi]
            aux[k] = a[k];
          for (int k = lo; k ＜= hi; k++)  // 归并回到a[lo..hi]
            if      (i ＞ mid)         a[k] = aux[j++];
            else if (j ＞ hi )                 a[k] = aux[i++];
            else if (less(aux[j], aux[i]))  a[k] = aux[j++];
            else                              a[k] = aux[i++];
      }
      ```
      - ![image.png](../assets/image_1650615850233_0.png)
  - 自顶向下
    collapsed:: true
    - 分治思想
      collapsed:: true
      - 归纳证明算法能够正确地将数组排序的基础：
        - 如果它能将两个子数组排序，它就能够通过归并两个子数组来将整个数组排序
    - collapsed:: true
      ```java
      public class Merge
      {
          private static Comparable[] aux;       // 归并所需的辅助数组
          public static void sort(Comparable[] a)
          {
            aux = new Comparable[a.length];    // 一次性分配空间
            sort(a, 0, a.length -1);
          }
          private static void sort(Comparable[] a, int lo, int hi)
          {  // 将数组a[lo..hi]排序
            if (hi ＜= lo) return;
            int mid = lo + (hi - lo)/2;
            sort(a, lo, mid);        // 将左半边排序
            sort(a, mid+1, hi);      // 将右半边排序
            merge(a, lo, mid, hi);  // 归并结果（代码见“原地归并的抽象方法”）
          }
      }
      ```
      - ![image.png](../assets/image_1650620972378_0.png)
        id:: 62627a1d-dc5e-4179-b23a-3f7bbbe0fbf7
      - ![image.png](../assets/image_1650621008680_0.png)
      - ![image.png](../assets/image_1650621572432_0.png)
        - #learning/programming $$logN => Tree/Recursion$$
        - ==对于长度为 N 的任意数组，自顶向下的归并排序需要== $$\frac{N}{2}lgN \sim  NlgN$$ ==次比较==
          collapsed:: true
          - 用 $$C(N)$$ 表示一个长度为N的数组排序时所需要的比较次数, 有 $$C(0) =C(1) = 0$$
          - 对于 $$N>0$$, 我们有 $$C([\frac{N}{2}]) + C([\frac{N}{2}]) + [\frac{N}{2}] ≤ C(N) ≤ C([\frac{N}{2}]) + C([\frac{N}{2}]) + N$$
          - 当 $$N=2^{n}$$ 且上限不等式的等号成立时我们能够得到一个解
            - $$ C(2^{n}) = 2C(2^{n-1}) + 2^{n} $$
            - $$ \frac{C(2^{n})}{2^{n}} = \frac{C(2^{n-1})}{2^{n-1}} + 1 $$
            - 递归定义, 不断替换最后得到
            - $$ \frac{C(2^{n})}{2^{n}} = \frac{C(2^{0})}{2^{0}} + n $$
            - $$C(N) = C(2^{n}) = n2^{n} = NlgN$$
          - 对于一般的N，得到的准确值要更复杂一些。但对比较次数的上下界不等式使用相同的方法不难证明前面所述的对于任意N的结论。这个结论对于任意输入值和顺序都成立。
        - ==对于长度为 N 的任意数组，自顶向下的归并排序最多需要访问数组== $$6NlgN$$ ==次==
          collapsed:: true
          - 每次归并最多需要访问数组6N次（2N次用来复制，2N次用来将排好序的元素移动回去，另外最多比较2N次），根据命题F即可得到这个命题的结果
        - id:: 62628c9e-f31d-4baa-b610-82ad76784514
    - 对小规模子数组使用插入排序
      - 递归会使小规模问题中方法的调用过于频繁，所以改进对它们的处理方法就能改进整个算法
      -
  - TODO exercise
- 快速排序
  - TODO exercise
- 优先队列
  - 收集一些元素处理当前键值最大的元素，然后再收集更多的元素处理当前键值最大的元素，如此这般
    collapsed:: true
    - 一个合适的数据结构应该支持:
      - 删除最大元素
      - 插入元素
    - 应用场景
      - 模拟系统
        - 事件的键即为发生的时间
        - 系统需要按照时间顺序处理所有事件
        - 任务调度，其中键值对应的优先级决定了应该首先执行哪些任务
        - 数值计算，键值代表计算错误，而我们需要按照键值指定的顺序来修正它们
      -
  - API
    collapsed:: true
    - MaxPQ
    - MinPQ
    - 示例
      id:: 62639d56-1a6a-4728-ac55-ecc2f5fdd5de
      collapsed:: true
      - 将每个 新的输入 N 和 已知的 M 个最大元素 比较 (M要控制得小, 要不然代价会很高)
        - 高效地实现 `insert()` 和 `delMin()`
          id:: 62639dea-4961-43ff-9ee5-db1c4328a331
        - 现代基础性计算环境中超大的输入 N 非常常见
        - 这些实现使我们能够解决以前缺乏足够资源去解决的问题
        - ![image.png](../assets/image_1650695838076_0.png)
        - ```java
          public class TopM
          {
              public static void main(String[] args)
              {  // 打印输入流中最大的M行
                int M = Integer.parseInt(args[0]);
                MinPQ＜Transaction＞ pq = new MinPQ＜Transaction＞(M+1);
                while (StdIn.hasNextLine())
                {  // 为下一行输入创建一个元素并放入优先队列中
                    pq.insert(new Transaction(StdIn.readLine()));
                    if (pq.size() ＞ M)
                      pq.delMin();     // 如果优先队列中存在M+1个元素则删除其中最小的元素
                }  // 最大的M个元素都在优先队列中
                Stack＜Transaction＞ stack = new Stack＜Transaction＞();
                while (! pq.isEmpty()) stack.push(pq.delMin());
                for (Transaction t : stack) StdOut.println(t);
            }
          }
          ```
  - 初级实现
    collapsed:: true
    - 数组实现 (无序)
      collapsed:: true
      - 数组 + 下压栈
      - TODO insert()方法的代码和栈的push()方法完全一样。要实现删除最大元素，我们可以添加一段类似于选择排序的内循环的代码，将最大元素和边界元素交换然后删除它，和我们对栈的pop()方法的实现一样。和栈类似，我们也可以加入调整数组大小的代码来保证数据结构中至少含有四分之一的元素而又永远不会溢出
      -
    - 数组实现 (有序)
      collapsed:: true
      - TODO 另一种方法就是在insert()方法中添加代码，将所有较大的元素向右边移动一格以使数组保持有序（和插入排序一样）。这样，最大的元素总会在数组的一边，优先队列的删除最大元素操作就和栈的pop()操作一样了
    - 链表表示法
      collapsed:: true
      - ![image.png](../assets/image_1650698284687_0.png)
      - ![image.png](../assets/image_1650698343075_0.png)
      - 堆实现
    - (二叉) 堆 定义
      collapsed:: true
      - 当一棵二叉树的每个结点都大于等于它的两个子结点时，它被称为堆有序
        collapsed:: true
        - 在二叉堆的数组中，每个元素都要保证大于等于另两个特定位置的元素。相应地，这些位置的元素又至少要大于等于数组中的另两个元素，以此类推
        - 在堆有序的二叉树中，每个结点都小于等于它的父结点（如果有的话）。从任意结点向上，我们都能得到一列非递减的元素；从任意结点向下，我们都能得到一列非递增的元素
      - ==根结点是堆有序的二叉树中的最大结点==
        id:: 6263a8b6-2ae8-41f7-83af-8210c3c04996
        collapsed:: true
        - 根据树的性质归纳可得
      - 二叉堆表示法
        collapsed:: true
        - 二叉堆是一组能够用堆有序的完全二叉树排序的元素，并在数组中按照层级储存（不使用数组的第一个位置）
        - 指针
          - 每个元素都需要三个指针来找到它的上下结点（父结点和两个子结点各需要一个）
        - 数组
          - 位置k的结点的父结点的位置为[k/2]，而它的两个子结点的位置则分别为2k和2k+1。这样在不使用指针的情况下（我们在第3章中讨论二叉树时会用到它们）我们也可以通过计算数组的索引在树中上下移动：从a[k]向上一层就令k等于k/2，向下一层则令k等于2k或2k+1
          - 用数组（堆）实现的完全二叉树的结构是很严格的，但它的灵活性已经足以让我们高效地实现优先队列。用它们我们将能实现对数级别的插入元素和删除最大元素的操作。利用在数组中无需指针即可沿树上下移动的便利和以下性质，算法保证了对数复杂度的性能
        - ==一棵大小为N的完全二叉树的高度为[lgN]==
          - 通过归纳很容易可以证明这一点，且当N达到2的幂时树的高度会加1
        - ![image.png](../assets/image_1650699238023_0.png)
        -
  - (二叉) 堆的算法
    collapsed:: true
    - 我们用长度为 N+1 的私有数组 pq[] 来表示一个大小为 N 的堆，我们不会使用 pq[0]，堆元素放在 pq[1] 至 pq[N] 中
    - 堆的有序化 (reheapifying)
      collapsed:: true
      - 首先进行一些简单的改动, 打破堆的状态, 然后再遍历堆并按照要求将堆的状态恢复
      - 私有辅助函数 `less()` 和 `exch()` 来访问元素
        - ```java
          private boolean less(int i, int j){
            return qp[i].compareTo(pq[j])<0;
          }
          private void exch(int i, int j){
            Key t = pq[i]; pq[i]=pq[j]; pq[j]=t;
          }
          ```
      - 当某个结点的优先级上升（或是在堆底加入一个新的元素）时，我们需要由下至上恢复堆的顺序
      - 当某个结点的优先级下降（例如，将根结点替换为一个较小的元素）时，我们需要由上至下恢复堆的顺序
    - 由下至上的堆有序化 (上浮, swim)
      collapsed:: true
      - ![image.png](../assets/image_1650700218810_0.png)
      - ```java
        private void swim(int k){
          while(k>1 && less(k/2, k)){
            exch(k/2, k);
            k = k/2;
          }
        }
        ```
    - 由上至下的堆有序化 (下沉, sink)
      collapsed:: true
      - ![image.png](../assets/image_1650700209923_0.png)
      - ```java
        private void sink(int k){
          while(2*k <= N){
            int j = 2*k;
            if(j<N && less(j, j+1)) j++;
            if(!less(k, j)) break;
            exch(k, j);
            k = j;
          }
        }
        ```
      - swim & sink 意义
        - ![image.png](../assets/image_1650700303258_0.png)
    - collapsed:: true
      ```java
      public class MaxPQ＜Key extends Comparable＜Key＞＞
      {
          private Key[] pq;               // 基于堆的完全二叉树
          private int N = 0;             // 存储于pq[1..N]中，pq[0]没有使用
          public MaxPQ(int maxN)
          {  pq = (Key[]) new Comparable[maxN+1];  }
          public boolean isEmpty()
          {  return N == 0;  }
          public int size()
          {  return N;  }
          public void insert(Key v)
          {
            pq[++N] = v;
            swim(N);
          }
          public Key delMax()
          {
            Key max = pq[1];            // 从根结点得到最大元素
            exch(1, N--);                // 将其和最后一个结点交换
            pq[N+1] = null;             // 防止对象游离
            sink(1);                     // 恢复堆的有序性
            return max;
          }
          // 辅助方法的实现请见本节前面的代码框
          private boolean less(int i, int j)
          private void exch(int i, int j)
          private void swim(int k)
          private void sink(int k)
      }
      ```
      - ==对于一个含有N个元素的基于堆的优先队列，插入元素操作只需不超过（lgN+1）次比较，删除最大元素的操作需要不超过2lgN次比较==
        - 证明。由命题P可知，两种操作都需要在根结点和堆底之间移动元素，而路径的长度不超过lgN。对于路径上的每个结点，删除最大元素需要两次比较（除了堆底元素），一次用来找出较大的子结点，一次用来确定该子结点是否需要上浮
      -
    - 多叉堆
      - TODO 对于数组中1至N的N个元素，位置k的结点大于等于位于3k-1、3k和3k+1的结点，小于等于位于[（k+1）/3]的结点。甚至对于给定的d，将其修改为任意的d叉树也并不困难。我们需要在树高（log dN）和在每个结点的d个子结点找到最大者的代价之间找到折中，这取决于实现的细节以及不同操作的预期相对频繁程度
    - 调整数组大小
      - TODO 我们可以添加一个没有参数的构造函数，在insert()中添加将数组长度加倍的代码，在delMax()中添加将数组长度减半的代码，就像在1.3节中的栈那样。这样，算法的用例就无需关注各种队列大小的限制。当优先队列的数组大小可以调整、队列长度可以是任意值时，命题Q指出的对数时间复杂度上限就只是针对一般性的队列长度N而言了（请见练习2.4.22）
    - 索引优先队列
      - 允许用例引用已经进入优先队列中的元素是有必要的
        collapsed:: true
        - 一种简单方法是给每个元素一个索引。
        - 一种常见的情况是用例已经有了总量为N的多个元素，而且可能还同时使用了多个（平行）数组来存储这些元素的信息。此时，其他无关的用例代码可能已经在使用一个整数索引来引用这些元素了
      - ![image.png](../assets/image_1650705662529_0.png)
      - ==在一个大小为N的索引优先队列中，插入元素（insert）、改变优先级（change）、删除（delete）和删除最小元素（remove the minimum）操作所需的比较次数和logN成正比（如表2.4.6所示）==
        collapsed:: true
        ![image.png](../assets/image_1650706021077_0.png){:height 194, :width 685}
        - 已知堆中所有路径最长即为～lgN，从代码中很容易得到这个结论
      - 用例 -- 多向归并
        collapsed:: true
        - 它将多个有序的输入流归并成一个有序的输出流。许多应用中都会遇到这个问题。输入可能来自于多种科学仪器的输出（按时间排序），或是来自多个音乐或电影网站的信息列表（按名称或艺术家名字排序），或是商业交易（按账号或时间排序），或者其他。如果有足够的空间，你可以把它们简单地读入一个数组并排序，但如果用了优先队列，无论输入有多长你都可以把它们全部读入并排序
        - ```java
          public class Multiway
          {
              public static void merge(In[] streams)
              {
                int N = streams.length;
                IndexMinPQ＜String＞ pq = new IndexMinPQ＜String＞(N);
                for (int i = 0; i ＜ N; i++)
                    if (! streams[i].isEmpty())
                        pq.insert(i, streams[i].readString());
                while (! pq.isEmpty())
                {
                    StdOut.println(pq.min());
                    int i = pq.delMin();
                    if (! streams[i].isEmpty())
                        pq.insert(i, streams[i].readString());
                }
              }
              public static void main(String[] args)
              {
                int N = args.length;
                In[] streams = new In[N];
                for (int i = 0; i ＜ N; i++)
                    streams[i] = new In(args[i]);
                merge(streams);
              }
          }
          ```
        -
  - 堆排序
    - 堆的构造
      collapsed:: true
      - 从左至右遍历数组，用swim()保证扫描指针左侧的所有元素已经是一棵堆有序的完全树即可，就像连续向优先队列中插入元素一样。
        - 从右至左用sink()函数构造子堆
          - 数组的每个位置都已经是一个子堆的根结点了，sink()对于这些子堆也适用。如果一个结点的两个子结点都已经是堆了，那么在该结点上调用sink()可以将它们变成一个堆。这个过程会递归地建立起堆的秩序。
          - 开始时我们只需要扫描数组中的一半元素，因为我们可以跳过大小为1的子堆。最后我们在位置1上调用sink()方法，扫描结束。在排序的第一阶段，堆的构造方法和我们的想象有所不同，因为我们的目标是构造一个堆有序的数组并使最大元素位于数组的开头（次大的元素在附近）而非构造函数结束的末尾。
      - ==用下沉操作由N个元素构造堆只需少于2N次比较以及少于N次交换==
        - 观察可知，构造过程中处理的堆都较小。例如，要构造一个127个元素的堆，我们会处理32个大小为3的堆，16个大小为7的堆，8个大小为15的堆，4个大小为31的堆，2个大小为63的堆和1个大小为127的堆，因此（最坏情况下）需要32×1 + 16×2 + 8×3 + 4×4 +2×5 + 1×6= 120次交换（以及两倍的比较）。完整证明请见练习2.4.20。
    - ```java
      public static void sort(Comparable[] a)
      {
          int N = a.length;
          for (int k = N/2; k ＞= 1; k--)
            sink(a, k, N);
          while (N ＞ 1)
          {
            exch(a, 1, N--);
            sink(a, 1, N);
          }
      }
      ```
  - 先下沉后上浮
  - [[java/quick-refs]]
    collapsed:: true
    - 我还是不明白优先队列是做什么用的。为什么我们不直接把元素排序然后再一个个地引用有序数组中的元素？
      collapsed:: true
      - 在某些数据处理的例子里，比如TopM和Multiway，总数据量太大，无法排序（甚至无法全部装进内存）。如果你需要从10亿个元素中选出最大的十个，你真的想把一个10亿规模的数组排序吗？但有了优先队列，你就只用一个能存储十个元素的队列即可。在其他的例子中，我们甚至无法同时获取所有的数据，因此只能先从优先队列中取出并处理一部分，然后再根据结果决定是否向优先队列中添加更多的数据。
    - 为什么不像我们在其他排序算法中那样使用Comparable接口，而在MaxPQ中使用泛型的Item呢？
      collapsed:: true
      - 这么做的话delMax()的用例就需要将返回值转换为某种具体的类型，比如String。一般来说，应该尽量避免在用例中进行类型转换
  - TODO exercise
-
- $$学习一个新的算法 == 思路 + 代码 + 算法轨迹$$ 
  tags:: #[[TIL]], #[[programming]]
-
-