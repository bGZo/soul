tags:: #[[data-structure]], #[[maths]]
description:: algorithm

-
- [[roadmap]] via: [List of algorithms - Wikipedia](https://en.wikipedia.org/wiki/List_of_algorithms)
  collapsed:: true
  - 01. Automated planning, 自动化规划
  - collapsed:: true
    02. Combinatorial algorithms, 组合算法
    - General combinatorial algorithms, 通用组合算法
    - Graph algorithms, 图算法
      collapsed:: true
      - Graph drawing, 图形绘制
      - Network theory, 网络理论
      - Routing for graphs, 图的路由
      - Graph search, 图形搜索
      - Subgraphs, 子图
    - Sequence algorithms, 序列算法
      - Approximate_sequence_matching, 近似序列匹配
      - Selection_algorithms, 选择算法
      - Sequence_search, 序列搜索
      - Sequence_merging, 序列合并
      - Sequence permutations, [[sort]], 序列排列
      - Sequence_combinations, 序列组合
      - Sequence_alignment, 序列比对
      - Sequence_sorting, 序列排序
      - Subsequences, 子序列
      - Substrings, 子串
  - collapsed:: true
    03. Computational mathematics, 计算数学
    - Abstract algebra, 抽象代数
    - Computer algebra, 计算机代数
    - Geometry, 几何
    - Number theoretic algorithms, 数论算法
    - Numerical algorithms, 数值算法
      collapsed:: true
      - Linear algebra, 线性代数
    - Optimization algorithms, 优化算法
  - collapsed:: true
    04. Computational science, 计算科学
    - 天文学
    - 生物信息学
    - 地球科学
    - 语言学
    - 医学
    - 物理学
    - 统计
  - collapsed:: true
    05. Computer science, 计算机科学
    - Computer architecture, 计算机体系结构
    - Computer graphics, 计算机图形学
    - Cryptography, 密码学
    - Digital logic, 数字逻辑
    - Machine learning and statistical classification, 机器学习与统计分类
    - Programming language theory, 程序设计语言理论
    - Parsing, 解析
    - Quantum algorithms, 量子算法
  - collapsed:: true
    06. Information theory and signal processing, 信息论与信号处理
    - Coding theory, 编码理论
    - Digital signal processing, 数字信号处理
  - 07. Software engineering, 软件工程
  - 08. Database algorithms, 数据库算法
  - collapsed:: true
    09. Distributed systems algorithms, 分布式系统算法
    -
  - 10. Networking, 网络
  - collapsed:: true
    11. Operating systems algorithms, 操作系统算法
    - Process synchronization, 进程同步
    - Scheduling, 调度
    - I/O_scheduling, I/O调度
-
- outline
  collapsed:: true
  - 树
    collapsed:: true
    - 二叉树
      collapsed:: true
      - 遍历
        collapsed:: true
        - DFS
        - BFS
      - 二叉搜索树
      - 平衡二叉树
        collapsed:: true
        - AVL 树
        - 红黑树
      - 剪枝
    - 字典树
      collapsed:: true
      - 空间换时间
  - 图
    collapsed:: true
    - 遍历时需要记录已经访问过的结点
  - 递归、分治
    collapsed:: true
    - 盗梦空间
    - 终止状态
    - 本层处理
    - Drill Down
    - 本层状态清理
  - 二分查找
    collapsed:: true
    - 有序
    - 有界
    - 能够通过索引随机访问
  - 贪心算法
    collapsed:: true
    - 判断能不能贪心
    - 弱化版的动态规划
  - 动态规划
    collapsed:: true
    - 简单版本是递归加缓存
    - 高级版本是递推公式
    - 状态的定义
      collapsed:: true
      - 有些场景需要套用模板
    - 最优子结构
    - 状态转移方程
  - 位运算
    collapsed:: true
    - 需要记忆一些常见的位运算公式
  - 布隆过滤器
    collapsed:: true
    - 判断不存在 100% 准确
    - 判断存在有误差
    - 利用 Hash 函数将待判断 Key 对应到多个位上
  - LRU
    collapsed:: true
    - HashTable + 双向链表
    - get 和 set 都是 O(1) 的复杂度
  - 工具
    collapsed:: true
    - Google 搜索引擎
    - iTerm2 + zsh 最强终端体验
    - heyfocus.com
    - IDEA + LeetCode Plugin
    - LeetCode
  - 复杂度
    collapsed:: true
    - 时间复杂度
      collapsed:: true
      - O(1) 常数复杂度，最佳，比如 Hash 表、缓存等
      - O(log n) 仅次于常数复杂度，如二分查找、二叉搜索树等
      - O(n) 线性复杂度，如大多数遍历操作
      - O(n^2) 双重 for 循环
      - O(2^n) 递归的时间复杂度
    - 空间复杂度
      collapsed:: true
      - O(1) 原地操作
      - O(n) 开辟线性辅助空间
  - 数组
    collapsed:: true
    - 连续空间
    - 查找快、插入/删除结点慢
  - 链表
    collapsed:: true
    - 离散空间
    - 查找慢，插入/删除结点快
  - 栈
    collapsed:: true
    - 先进后出
  - 队列
    collapsed:: true
    - 先进先出
  - 映射
    collapsed:: true
    - K/V 键值对，Key 不重复
  - 集合
    collapsed:: true
    - Key 不重复
  - 并查集
    collapsed:: true
    - 站队问题
    - 初始化
    - 查询、合并
    - 路径压缩
  - ![data-struct.png](../assets/algo/data-struct_1663207949320_0.png)
    - | 数据结构 |                            优点                            |                         缺点                         |
      | :------: | :--------------------------------------------------------: | :--------------------------------------------------: |
      |   数组   |                           插入快                           |      查找慢，删除慢，大小固定，只能存储单一元素      |
      | 有序数组 |                      比无须数组查询快                      |      插入慢，删除慢，大小固定，只能存储单一元素      |
      |    栈    |                   提供后进先出的存取方式                   |                    存取其他项很慢                    |
      |   队列   |            提供先进先出的存取方式插入快，删除快            |                    存取其他项很慢                    |
      |   链表   |           如果树是平衡的，则查找、插入、删除都快           |                        查找慢                        |
      |  二叉树  |         查找、删除、插入都快。树总是平衡的算法复杂         |                     删除算法复杂                     |
      |  红黑树  | 查找、删除、插入都快。树总是平衡的。类似的树对磁盘存储有效 |                   算法复杂算法复杂                   |
      | 2-3-4树  |                   如果关键字已知则存取极                   | 删除慢，如果不知道关键字存取慢，对存储空间使用不充分 |
      |  哈希表  |             快插入、删除快，对最大数据项存取快             |                  对其他数据项存取慢                  |
      |    堆    |                       对现实世界建模                       |                    有些算法慢且身                    |
  - 预处理
    collapsed:: true
    - 前缀最大和
  - 特征
    collapsed:: true
    - 有穷性
      - 一个算法必须总是在执行有限步之后结束
    - 确定性
      - 算法的每一个步骤必须是确切地定义的。
    - 输入
      - 一个算法有0个或多个输入
    - 输出
      - 一个算法有1个或多个输出
    - 可行性
      - 算法中要执行的每一个计算步骤都是可以在有限时间内完成的
  - 尺度
    collapsed:: true
    - 正确性
    - 可读性
    - 健壮性( 容错性 ) -- 对不规范数据的处理能力( 竞赛中不考虑 )
    - Tools
      - Google
      - Terminal
        - Mac: iTerm2 + zsh (oh my zsh)
        - Windows: Microsoft new terminal: (https://github.com/microsoft/terminal)
      - VSCode; Java: IntelliJ; Python: Pycharm
        - https://vscodethemes.com/
        - 骚操作：
          - https://juejin.im/entry/587e0f2f570c352201113e14
          - https://juejin.im/post/5ce1365151882525ff28ed47
      - LeetCode plugin (VSCode & IntelliJ)
      - Code Style
        collapsed:: true
        - Google code style
        - Facebook
        - Airbnb
      - LeetCode
        - leetcode-cn.com 和 题解
        - leetcode.com 和 Discuss board
      - ⾃顶向下的编程⽅式
        - https://markhneedham.com/blog/2008/09/15/clean-codebook-review/
        - https://leetcode-cn.com/problems/valid-palindrome
  - 数组、链表、跳表
    collapsed:: true
    - **Array**
        ```cpp
        int a[100];    //Java/C++
        list = []      //Python
        let x=[1,2,3]  //JavaScript
        ```
      - 泛化语言，任何一个单元类型都可以放进去
      - 内存管理器(Memory Controller)——删除/插入
      - o(1)+o(n)=o(n+1/2);
      - java 自动内存回收机制。
            ```cpp
            prepend   o(1)
            append    o(1)
            lookup    o(1)
            insert    o(n)
            delete    o(n)
            ```
    - **Linked List**
        Head Tail
        java的next指针是引用
        双向链表
        循环链表
        ```java
        Entry<T>
        ```
        java的链表是双向链表
        slide
        ```cpp
        prepend   o(1)//增加
        append    o(1)
        lookup    o(n)
        insert    o(1)
        delete    o(1)
        ```
    - **Skip LIst**
        Redis
        升维思想——空间换时间
        添加第一级索引
        添加二级索引
        增加log2n个级索引
        64（2^6）个元素(log2n-1)
        ```
        n/2、n/4、n/8、第k级索引结点的个数就是n/（2k）
        假设索引有h级，最高级的索引有2个结点。n/（2h）=2，从而求得h=log2（n）-1
        ```
        维护成本高
        n*(1-1/2^n)<n
        LRU Cache - Linked list
        https://www.jianshu.com/p/b1ab4a170c3c
        https://leetcode-cn.com/problems/Iru-cache
        Redis - Skip - List
        https://redisbook.readthedocs.io/en/latest/internal-datastruct/skiplist.html
        https://www.zhihu.com/question/20202931
      > 给的建议也是让我们快速的练习，而不是从零到有，我觉得不好，但是又想不出下文。
  - 栈、队列、优先队列、双端队列
    collapsed:: true
    - 练习
      1. https://leetcode-cn.com/problems/container-with-most-water/
      2. https://leetcode-cn.com/problems/move-zeroes/
      3. https://leetcode-cn.com/problems/climbing-stairs/
      4. https://leetcode-cn.com/problems/3sum/（高频老题）
    - Stack：先入后出；添加、删除皆为o（1）
    - Queue：先入先出；添加、删除皆为o（1）
      - 查询加哈希表加速
    - **Deque(Double-End Queue)(双端队列)**
      - vector 线程安全
    - [Java 的 PriorityQueue 文档](http://docs.oracle.com/javase/10/docs/api/java/util/PriorityQueue.html)
    - [Java 的 Stack 源码](http://developer.classpath.org/doc/java/util/Stack-source.html)
    - [Java 的 Queue 源码](http://fuseyism.com/classpath/doc/java/util/Queue-source.html)
    - [Python 的 heapq](https://docs.python.org/2/library/heapq.html)
    - [高性能的 container 库](https://docs.python.org/2/library/collections.html)
  - 哈希表、映射、集合树、二叉树、二叉搜索树
    collapsed:: true
    - Hash table
      - 散列表，是根据关键码值（Key value）而直接进行访问的数据结构。它通过把关键码值映射到表中一个位置来访问记录，以加快查找的速度。这个映射函数叫作散列函数（Hash Function），存放记录的数组叫作哈希表（或散列表）
      - 电话号码簿
      - 用户信息表
      - 缓存（LRU Cache）
      - 键值对存储（Redis）
    - Hash FunctionDF
    - Hash Collisions
      - 增加维度->拉链式解决冲突法
    - 好的情况下O(1),坏的情况下O(n)
    - Map：key-value对，key不重复
      - new HashMap() / new TreeMap()
      - map.set(key, value)
      - map.get(key)
      - map.has(key)
      - map.size()
      - map.clear()
    - Set：不重复元素的集合
      - new HashSet() / new TreeSet()
      - set.add(value)
      - set.delete(value)
      - set.hash(value)
        ```python
        ist_x = [1, 2, 3, 4]
        map_x = {
        ‘jack’: 100,
        ‘张三’: 80,
        ‘selina’: 90,
        # …
        }
        set_x = {‘jack’, ‘selina’, ‘Andy’}
        set_y = set([‘jack’, ‘selina’, ‘jack’])
        ```
        Map, Set : interfaces
    - Java set classes:
      - [TreeSet, HashSet,ConcurrentSkipListSet, CopyOnWriteArraySet, EnumSet, JobState Reasons, LinkedHashSet](https://docs.oracle.com/en/java/javase/12/docs/api/java.base/java/util/Set.html)
    - Java map classes:
      - [HashMap, Hashtable, ConcurrentHashMap](https://docs.oracle.com/en/java/javase/12/docs/api/java.base/java/util/Map.html)
        实战题目
        1. https://leetcode-cn.com/problems/valid-anagram/description/
        2. https://leetcode-cn.com/problems/group-anagrams/
        3. https://leetcode-cn.com/problems/two-sum/description/
        小技巧
    - 养成收藏精选代码的习惯
      collapsed:: true
      - Anagram, group-anagrams, two sum
            ```python
            # 思路：手动模拟hashtable，将字符串”a-z“的ASCII码作key，计数求差异
            def  isAnagram(self, s: str, t: str) -> bool:
              arr1, arr2 = [0]*26, [0]*26
              for i in s:
                  arr1[ord(i) - ord('a')] += 1
              for i in t:
                  arr2[ord(i) - ord('a')] += 1
              return arr1 == arr2
            ```
            ```python
            # 思路：map计数，对比计数差异
          def isAnagram(self, s: str, t: str) -> bool:
              dict1, dict2 = {}, {}
              for item in s:
                  dict1[item] = dict1.get(item,0) + 1
              for item in t:
                  dict2[item] = dict2.get(item,0) + 1
              return dict1 == dict2
            ```
            ```python
            # 思路：数组排序后比较差异
          def isAnagram(self, s: str, t: str) -> bool:
              return sorted(s) == sorted(t)
             ```+
             ```java
            public class Solution {
          public boolean isAnagram(String s, String t) {
              if(s.length() != t.length()) return false;
              int [] a = new int [26];
              for(Character c : s.toCharArray()) a[c - 'a']++;
              for(Character c : t.toCharArray()) {
                  if(a[c -'a'] == 0) return false;
                  a[c - 'a']--;
              }
              return true;
          }
            }
            ```
            ```java
            public boolean isAnagram(String s1, String s2) {
              int[] freq = new int[256];
              for(int i = 0; i < s1.length(); i++) freq[s1.charAt(i)]++;
              for(int i = 0; i < s2.length(); i++) if(--freq[s2.charAt(i)] < 0) return false;
              return s1.length() == s2.length();
          }
            ```
            ```java
            public boolean isAnagram(String s, String t)
            {
          char[] sChar = s.toCharArray();
          char[] tChar = t.toCharArray();
          Arrays.sort(sChar);
          Arrays.sort(tChar);
          return Arrays.equals(sChar, tChar);
            }
            ```
        Group Anagrams:
            ```python
            def groupAnagrams(self, strs):
          d = {}
          for w in sorted(strs):
              key = tuple(sorted(w))
              d[key] = d.get(key, []) + [w]
          return d.values()
            ```
            ```python
            def groupAnagrams(self, strs):
          dic = {}
          for item in sorted(strs):
              sortedItem = ''.join(sorted(item))
              dic[sortedItem] = dic.get(sortedItem, []) + [item]
          return dic.values()
            ```
            ```java
            public List<List<String>> groupAnagrams(String[] strs) {
          List<List<String>> res = new ArrayList<>();
          HashMap<String, List<String>> map = new HashMap<>();
          Arrays.sort(strs);
          for (int i = 0; i < strs.length; i++) {
              String temp = strs[i];
              char[] ch = temp.toCharArray();
              Arrays.sort(ch);
              if (map.containsKey(String.valueOf(ch))) {
                  map.get(String.valueOf(ch)).add(strs[i]);
              } else {
                  List<String> each = new ArrayList<>();
                  each.add(strs[i]);
                  map.put(String.valueOf(ch), each);
              }
          }
          for (List<String> item: map.values()) {
              res.add(item);
          }
          return res;
            }
            ```
          Two sum
            ```python
            def twoSum(self, nums, target):
              d = dict()
              for index,num in enumerate(nums):
                  if d.get(num) == None:
                      d[target - num] = index
                  else:
                      return [d.get(num), index]
            ```
            ```java
            public int[] twoSum(int[] nums, int target) {
              HashMap<Integer, Integer> tracker =
                  new HashMap<Integer, Integer>();
              int len = nums.length;
              for (int i = 0; i < len; i++){
                  if (tracker.containsKey(nums[i])){
                      int left = tracker.get(nums[i]);
                      return new int[]{left+1, i+1};
                  } else {
                      tracker.put(target - nums[i], i);
                  }
              }
              return new int[2];
          }
            ```
    - [有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/description/)
    - https://leetcode-cn.com/problems/group-anagrams/
    - https://leetcode-cn.com/problems/two-sum/description/
  - 泛型递归、树的递归
    collapsed:: true
    - 递归 -> 盗梦空间
      collapsed:: true
      - 向下进入到不同的梦境, 再带着不一样的状态回到原来的这层
      - 声音(参数)同步回到上一层
      - 每一层都是一份拷贝
    - 要点:
      collapsed:: true
      - 不要人肉进行递归（最大误区）
      - 找到最近最简方法，将其拆解成可重复解决的问题（重复子问题）
      - 数学归纳法思维, n = 1 时成立, 且 n 成立, n+1 也成立
        collapsed:: true
        - 类似于放鞭炮, 保证第一个会炸, 后一个会接着前一个炸, 那么结论成立
    - template:
      collapsed:: true
      - ```python
        # Python
        def recursion(level, param1, param2, ...):
          # recursion terminator
          if level > MAX_LEVEL:
           process_result
           return
          # process logic in current level
          process(level, data...)
          # drill down
          self.recursion(level + 1, p1, ...)
          # reverse the current level status if needed
        ```
        ```java
        // Java
        public void recur(int level, int param) {
        // terminator
        if (level > MAX_LEVEL) {
          // process result
          return;
        }
        // process current logic
        process(level, param);
        // drill down
        recur( level: level + 1, newParam);
        // restore current status
        ```
        ```cpp
        // C/C++
        void recursion(int level, int param) {
        // recursion terminator
        if (level > MAX_LEVEL) {
          // process result
          return ;
        }
        // process current logic
        process(level, param);
        // drill down
        recursion(level + 1, param);
        // reverse the current level status if needed
        }
        ```
        ```javascript
        // JavaScript
        const recursion = (level, params) =>{
         // recursion terminator
         if(level > MAX_LEVEL){
           process_result
           return
         }
         // process current level
         process(level, params)
         //drill down
         recursion(level+1, params)
         //clean current level status if needed
        }
        ```
    - 习题
      collapsed:: true
      - [爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)
        collapsed:: true
        - mutual exclusive: 互斥状况
        - complete exhaustive: 完全详尽
      - [括号生成](https://leetcode-cn.com/problems/generate-parentheses/)
      - ```cpp
        //List usage
        list<string>s1;
        list<string>::iterator it;
        it=s1.begin();
        s1.insert(it,"sdasdas");
        for(it=s1.begin();it!=s1.end();++it){
            cout<<' '<<*it;
        }
        ```
      - ```cpp
        void _generate(int, int, const std::string);
        std::list<std::string> generateParenthesis(int n) {
          _generate(0, 2 * n, "");
          return {};
        }
        void _generate(int level, int max, const std::string s) { //自顶向下编程.
            //terminator
            if(level>=max) {
                std::cout<<s<<"\n";
                return;
            }
          //process currnet logic : lefe, right
          //down is here.
          //drill down
          _generate(level+1, max, s+"(");
          _generate(level+1, max, s+")");
          //reverse state
        }
        int main(){
            generateParenthesis(3);
        }
        ```
      - ```cpp
        void _generate(int, int, int, const std::string);
        std::list<std::string>result;
        std::list<std::string>::iterator it;
        std::list<std::string> generateParenthesis(int n) {
            _generate(-1, 0, n, "");
            return result;
        }
        void _generate(int right, int left ,int n, const std::string s) { //自顶向下编程.
            //terminator
            if(right == n && left == n ) {
        //        std::cout<<s<<"\n";
                it=result.begin();
                result.insert(it,s);
                return;
            }
            //process currnet logic : lefe, right
            //drill down
            if(left < n)
                _generate(right,left+0, n, s+"(");
            if(right < left)
                _generate(right+0,left, n, s+")");
                //reverse state
            }
            int main(){
                generateParenthesis(2);
                for(it=result.begin();it!=result.end();++it)
                    std::cout<<*it<<"\n";
            }
        ```
    - https://leetcode-cn.com/problems/invert-binary-tree/description/
    - https://leetcode-cn.com/problems/validate-binary-search-tree
    - https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
    - https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
    - https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
    - **每日一课**: [如何优雅地计算斐波那契数列](https://time.geekbang.org/dailylesson/detail/100028406)
    - **作业**
      collapsed:: true
      - https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
      - https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
      - https://leetcode-cn.com/problems/combinations/
      - https://leetcode-cn.com/problems/permutations/
      - https://leetcode-cn.com/problems/permutations-ii/
  - 分治&回溯 Divide & COnquer
    collapsed:: true
    - 递归的另外一种表现形式.
    - 最近重复性
    - 最优重复性: 动态规划
    - recursion
    - Template:
      collapsed:: true
      - ```python
           # Python
           def divide_conquer(problem, param1, param2, ...):
             # recursion terminator
             if problem is None:
             print_result
             return
             # prepare data
             data = prepare_data(problem)
             subproblems = split_problem(problem, data)
             # conquer subproblems
             subresult1 = self.divide_conquer(subproblems[0], p1, ...)
             subresult2 = self.divide_conquer(subproblems[1], p1, ...)
             subresult3 = self.divide_conquer(subproblems[2], p1, ...)
             …
             # process and generate the final result
             result = process_result(subresult1, subresult2, subresult3, …)
             # revert the current level states
           ```
            ```cpp
            //C/C++
            int divide_conquer(Problem *problem, int params) {
              // recursion terminator
              if (problem == nullptr) {
                process_result
                return return_result;
              }
              // process current problem
              subproblems = split_problem(problem, data)
              subresult1 = divide_conquer(subproblem[0], p1)
              subresult2 = divide_conquer(subproblem[1], p1)
              subresult3 = divide_conquer(subproblem[2], p1)
              ...
              // merge
              result = process_result(subresult1, subresult2, subresult3)
              // revert the current level status
              return 0;
            }
            ```
            ```java
            //Java
            private static int divide_conquer(Problem problem, ) {
            if (problem == NULL) {
                int res = process_last_result();
                return res;
            }
            subProblems = split_problem(problem)
            res0 = divide_conquer(subProblems[0])
            res1 = divide_conquer(subProblems[1])
            result = process_result(res0, res1);
            return result;
            }
            ```
            ```javascript
            //Javascript
            const divide_conquer = (problem, params) => {
            // recursion terminator
            if (problem == null) {
                process_result
                return
            }
            // process current problem
            subproblems = split_problem(problem, data)
            subresult1 = divide_conquer(subproblem[0], p1)
            subresult2 = divide_conquer(subproblem[1], p1)
            subresult3 = divide_conquer(subproblem[2], p1)
            ...
            // merge
            result = process_result(subresult1, subresult2, subresult3)
            // revert the current level status
            }
            ```
  - **回溯 Backtracking**
    collapsed:: true
    - 八皇后
    - 数独
    - 归去来兮.
    - 回溯法采用试错的思想，它尝试分步的去解决一个问题。在分步解决问题的过程中，当它通过尝试发现现有的分步答案不能得到有效的正确的解答的时候，它将取消上一步甚至是上几步的计算，再通过其它的可能的分步解答再次尝试寻找问题的答案。
    - 回溯法通常用最简单的递归方法来实现，在反复重复上述的步骤后可能出现两种情况：
    - 找到一个可能存在的正确的答案；
    - 在尝试了所有可能的分步方法后宣告该问题没有答案。
    - 在最坏的情况下，回溯法会导致一次复杂度为指数时间的计算。
    - https://leetcode-cn.com/problems/powx-n/
    - [牛顿迭代法原理](http://www.matrix67.com/blog/archives/361)
    - [牛顿迭代法代码](http://www.voidcn.com/article/p-eudisdmk-zm.html)
    - [子集](https://leetcode-cn.com/problems/subsets/)
    - ```cpp
      // template: 1. terminator 2.process (split your big problem) 3. drill down (subproblmes) , merge(subsult) 4. reverse states
      - x\^n ——\>2\^10： 2\^5—\>（2\^2）\*2
      - pow(x, n):
        subproblem: subresult = pow(x, n/2)
      merge:
      - if n%2 == 1 {//obb
            result = subresult * subresult *x;
        }else{//even
            result = subresult * subresult;
        }
      - //3. 牛顿迭代法
      ```
    - ```java
      public class Solution {
      - public List<Integer>subsets(int []nums){
        List<List<Integer>> ans = new ArrayList<>();
        dfs(ans, nums, new ArrayList<Integer>(), 0);
        return ans;
      }
      - private void dfs(list<list<Integer>> ans, int []nums, list<Integer> list, int index) {
        //terminator
        if(index == nums.length ) {
            ans.add(new Arraylist<Integer>(list));
            return ;
        }
        dfs(ans, nums, list, index+1);// not pick the number at this index
      - list.add(nums[index]);
        dfs(ans, nums, list, index+1);// pick the number at this index
      - // reverse the current state
        list.remove(list.size()-1);
      }
      ```
      迭代
      ```python
      class Solution(object):
        def subsets(self, nums):
            subsets = [[]]
            for num in nums:
                for subset in subsets:
                    new_subset = sulset + [num]
                    newsets.append(new_subset)
                subsets. extend(newsets).
        return subsets
      ```
  - 深度优先搜索和广度优先搜索
  - 贪心算法
  - 二分查找
  - 动态规划
  - 字典树和并查集
  - 第14课丨高级搜索
  - 第15课丨红黑树和AVL树
  - 第16课丨位运算
  - 第17课丨布隆过滤器和LRU缓存
  - 第18课丨排序算法
  - 第19课丨高级动态规划
  - 第20课丨字符串算法
  - 第21课丨期末串讲
-
- Tips
  collapsed:: true
  - Chunk it up 切碎知识点
    collapsed:: true
    - 庖丁解牛
    - 脉络连接
  - Deliberate Practicing 刻意练习
    collapsed:: true
    - 职业化运动
    - 基本功是区别业余和职业选手的根本
    - 基础动作的分解训练和反复练习 —> 最大的误区
    - 刻意练习 — 过遍数（五毒神掌）
      - 5分钟：读题 + 思考 + 直接看解法：注意！多解法，比较解法优劣 + 背诵、默写好的解法
      - 马上自己写 —> LeetCode 提交 + 多种解法比较、体会 —> 优化
      - 过了一天后，再重复做题 + 不同解法的熟练程度 —> 专项练习
      - 过了一周：反复回来练习相同题目
      - 面试前一周恢复性训练
    - 练习缺陷、弱点地方
    - 不舒服、不爽、枯燥
  - Feedback 反馈
    collapsed:: true
    - 即时反馈
    - 主动型反馈（自己去找）
    - 高手代码 (GitHub, LeetCode, etc.)
    - 第一视角直播
    - 被动式反馈（高手给你指点）
    - code review
    - 教练看你打，给你反馈
  - 切题四件套
    collapsed:: true
    - Clarification
    - Possible solutions
      - compare (time/space)
      - optimal（加强）
    - Coding（多写）
    - Test cases
  - Tips
    collapsed:: true
    - 断点继传法
    - 对照阅读法
    - 教学视频法
    - 书看不懂时，不硬看，扫清障碍，咱再来……
    - 多找几本书，对照着看……
    - 先看教学视频入门，再看书
-
- [[standard]]
  collapsed:: true
  - ACM SoftwareProcesse
    collapsed:: true
    - SE/Software Processes
      - Topics
        collapsed:: true
        - **[Core-Tier1]（必须掌握的核心知识：第 1 级）**
          • Systems level considerations, i.e., the interaction of software with its intended environment (crossreference IAS/Secure Software Engineering)
          • Introduction to software process models (e.g., waterfall, incremental, agile)
          o Activities within software lifecycles
          • Programming in the large vs. individual programming
        - **[Core-Tier2]（必须掌握的核心知识：第 2 级）**
          • Evaluation of software process models
          [Elective]（选修部分）
          • Software quality concepts
          • Process improvement
          • Software process capability maturity models
          • Software process measurements
      - Learning Outcomes
        collapsed:: true
        - **[Core-Tier1]**
          1. Describe how software can interact with and participate in various systems including information management, embedded, process control, and communications systems.[Familiarity]
          2. Describe the relative advantages and disadvantages among several major process models (e.g., waterfall, iterative, and agile). [Familiarity]
          3. Describe the different practices that are key components of various process models. [Familiarity]
          4. Differentiate among the phases of software development. [Familiarity]
          5. Describe how programming in the large differs from individual efforts with respect to understanding a large code base, code reading, understanding builds, and understanding context of changes. [Familiarity]
        - **[Core-Tier2]**
          6. Explain the concept of a software lifecycle and provide an example, illustrating its phases including the deliverables that are produced. [Familiarity]
          7. Compare several common process models with respect to their value for development of particular classes of software systems taking into account issues such as requirement stability, size, and non-unctional characteristics. [Usage]
        - **[Elective]**
          8. Define software quality and describe the role of quality assurance activities in the software process.[Familiarity]
          9. Describe the intent and fundamental similarities among process improvement approaches. [Familiarity]
          10. Compare several process improvement models such as CMM, CMMI, CQI, Plan-Do-Check-Act, or ISO9000. [Assessment]
          11. Assess a development effort and recommend potential changes by participating in process improvement (using a model such as PSP) or engaging in a project retrospective. [Usage]
          12. Explain the role of process maturity models in process improvement. [Familiarity]
          13. Describe several process metrics for assessing and controlling a project. [Familiarity]
          14. Use project metrics to describe the current state of a project. [Usage]
  - ACM 总结的18个计算机科学关键领域
    collapsed:: true
    - | 缩写 | 关键知识领域（英文名称） | 说明 |
      | :----: | :------------------------: | :----: |
      |AL| Algorithms and Complexity |算法与复杂度|
      |AR| Architecture and Organization| 体系结构与组织|
      |CN| Computational Science| 计算科学|
      |DS| Discrete Structures| 离散结构|
      |GV| Graphics and Visualization| 图形与可视化|
      |HCI| Human-Computer Interaction| 人机交互|
      |IAS |Information Assurance and Security| 信息安全|
      |IM |Information Management| 信息管理|
      |IS| Intelligent Systems| 智能系统|
      |NC |Networking and Communication |网络与通讯|
      |OS |Operating Systems |操作系统|
      |PBD| Platform-based Development| 基于特定平台的开发|
      |PD |Parallel and Distributed Computing| 并行与分布式计算|
      |PL |Programming Languages |编程语言|
      |SDF| Software Development Fundamentals| 软件开发基础|
      |SE| Software Engineering |软件工程|
      |SF | Systems Fundamentals| 系统基础|
      |SP| Social Issues and Professional Practice| 社会性主题与职业实践|
      http://www.acm.org/education/curricula-recommendations
      《Computer Science Curricula-2013》
      不要试图做你认为做不到的事情, 而当你感到自闭的时候. 那恰巧正是你意识到要发生改变的时候.
  - ACM的《Computer Science Curricula-2013》
  - 衡量计算机科学知识的掌握程度
    collapsed:: true
    - > What do you know about this ?
      > What do you know how to do ?
      > Why would you do that ?
    - 当你主要在第N层工作时，需要对第N-1和N+1层下功夫，通常就足以应付日常的工作和学习任务了
-
- Competitions
  collapsed:: true
  - [[noip]]
  - ICPC/ACM (International Collegiate Programming Contest, 国际大学生程序设计竞赛)
    collapsed:: true
    - 最具影响力的大学生计算机竞赛
    - 官方地址: [icpc.baylor.edu](https://icpc.baylor.edu/)
  - CCPC (China Collegiate Programming Contest) 中国大学生程序设计竞赛
    collapsed:: true
    - 官方地址: [ccpc.io](https://ccpc.io/)
-
- Refs
  collapsed:: true
  - [CTF Wiki](https://ctf-wiki.org/)
  - [OI Wiki](https://oi-wiki.org/)
  - [知乎 Live - 如何自学计算机专业课程？ · Shannon's Blog](https://shannonchenchn.github.io/2018/10/07/zhihu-live-how-to-learn-cs-by-yourself/)
    - [如何自学计算机专业课程？ - 知乎 Live](https://www.zhihu.com/lives/837669764146003968)
  - [OI 赛事与赛制 - OI Wiki](https://oi-wiki.org/contest/oi/)
  - [ICPC/CCPC 赛事与赛制 - OI Wiki](https://oi-wiki.org/contest/icpc/)
  -
  - [黄明《从简单的线性数据结构开始：栈与队列》](https://shimo.im/docs/jTKWyPTYkQwDPYkr/)
  - [王记超《Java中HashMap数据结构分析（语言无关）》](https://shimo.im/docs/wXpyygqVqYhHW6px)
  - [张宇腾《Dijkstra算法分享》](https://shimo.im/docs/kkTgptvpQxj633Dk)
  - [阎文元《聊聊散列表》](https://shimo.im/docs/K9vKxdr69RtpKJtJ)
  - [张鹏《深入浅出数组》](https://shimo.im/docs/jpDKpgDTXTjtDkhj/)
-
- [[algorithm/bitwise-operation]]
  - TODO  diff [[data-structure/bit-map]] && [[data-structure/bit-array]] and above ???
- [[algorithm/stack/monotone]] | 单调栈
-
-