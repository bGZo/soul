alias:: algo/sort
-
- ## Sort Function
  - #+BEGIN_NOTE
    $a<b$ 是一个升序序列，$a>b$ 是一个降序序列；
    #+END_NOTE
    #cpp
  - [std::sort - cppreference.com](https://en.cppreference.com/w/cpp/algorithm/sort)
    - ```cpp
      constexpr bool operator()(const T &lhs, const T &rhs) const
      {
          return lhs > rhs; // assumes that the implementation uses a flat address space
      }
      ```
  -
-
-
- Outline
  collapsed:: true
  - ![sort_struct.png](../assets/algo/sort/sort_struct_1663212195275_0.png){:height 474, :width 747}
  - 计较类排序
    - 交换排序
      - id:: 63229b85-bfab-4944-9efe-d8a188e60fb2
        1. 冒泡排序
      - id:: 63229b8b-b393-4d32-899c-be19c41e358d
        2. 快速排序
    - 插入排序
      id:: 6327cf4f-e6cb-408d-a30f-da3690d5337b
      - id:: 63229b91-6f24-4e28-a44d-d9f2f2945793
        3. 简单插入排序
      - id:: 63229b97-21e9-4f05-89a9-76589fe9bec7
        4. 希尔排序
    - 选择排序
      id:: 6327cf4f-8816-4ced-ab43-30719633fd63
      - id:: 63229b9b-d803-4609-9750-e622c0decb3e
        5. 简单选择排序
      - id:: 63229ba0-be1e-4ad5-ad52-3d7cfed78250
        6. 堆排序 (Heap)
    - 归并排序
      id:: 6327cf4f-c18d-4817-90c5-798bb111ffcd
      - id:: 63229ba8-e09f-4636-ae39-c8a45b605c87
        7. 二路归并排序
      - id:: 63477f68-638f-4130-b766-d305f0ecf06f
        8. 多路归并排序
  - 非比较类排序
    - id:: 6327cf4f-8e44-41f6-ab99-b9fdf398e56a
      9. 计数排序
    - id:: 63229b76-3951-43fe-bd40-f2b407fd2944
      10. 桶排序 (Bucket)
    - id:: 6327cf4f-3759-4bad-9563-7662ea7373ef
      11. 基数排序
-
- Implement
  collapsed:: true
  - with [[cpp]]
    - ((63229b85-bfab-4944-9efe-d8a188e60fb2))
      - ```c++
        void bubbles(int p[], int m) {
          int i, j;
          for (i = 0; i < m; i++) {
            for (j = i + 1; j < m - 1; j++) {
              if (p[i] < p[j]) swap(p[i], p[j]);
            }
          }
        }
        ```
    - ((63229b8b-b393-4d32-899c-be19c41e358d))
      - ```c++
        int* p;
        void qsort(int l, int r) {
          int mid = p[(l + r) / 2];
          int i = l, j = r;
          do {
            while (p[i] < mid) i++;
            while (p[j] > mid) j--;
            if (i <= j) {
              swap(p[i], p[j]);
              i++;
              j--;
            }
          } while (i <= j);//注意等号
          if (l < j) qsort(l, j);//递归搜索左半部分
          if (i < r) qsort(i, r);//递归搜索右半部分
        }
        ```
    - ((63229b91-6f24-4e28-a44d-d9f2f2945793))
      - 从第二个元素开始，依次比较大小，小的去前面，大的去后面，采用的方式是最低效的平移数组，针对于基本有序的数列很高效。
      - ```c++
        void InsertSort(int p[], int start, int end) {
          for (int i = start + 1; i < end; i++) {
        int temp = p[i];//相当于一个容器，将无序数列的第一个元素取出
        int j = i - 1;//作为有序数列的最后一个元素
        while (j > 0 && temp < p[j]) {
          p[j + 1] = p[j];
          j--;
        }
        p[j + 1] = temp;
          }
        }
        ```
    - ((63229b97-21e9-4f05-89a9-76589fe9bec7)) -> 缩小增量
      - 作为插入排序的改进版,，先分组进行排序使得数列基本有序，再用插入排序进行排序。
      - ```c++
        void Shellsort(int p[], int len) {
          for (int i = len / 2; i < len; i /= 2) {
                for (int j = i; j < len; j++) {
                    int temp = i;
                    while (temp - j >= 0 && p[temp] < p[temp - j]) {
                        swap(p[temp], p[temp - j]);
                        temp -= i;
                    }
                }
          }
        }
        ```
    - ((63229b9b-d803-4609-9750-e622c0decb3e))
      - ```c++
        void selections(int p[], int m) {
          int k, i, j;
          for (i = 0; i < m; i++) {
            k = i;
            for (j = i + 1; j < m - 1; j++) {
              if (p[k] > p[j]) k = j;
              //是p[k]而不是p[q]的原因：因为一找到比他大的就赋值，会导致最后交换的不是最大的数的后果。这样才会记录最大值。最后用于交换！！
            }
            if (k != i)swap(p[i], p[k]);
          }
        }
        ```
    - ((63229ba0-be1e-4ad5-ad52-3d7cfed78250)) -> 优先队列
      - > 利用堆这种数据结构所设计的一种排序算法. 堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点.
      - ```c++
        #include <iostream>
        #include <queue>
        int main() {
          std::priority_queue<int>q;        //优先队列
          for (int i = 1; i <= 5; i++) q.push(i);
          for (int i = 0; i < 5; i++) {
            std::cout << q.top() << std::endl;
            q.pop();
          }
          return 0;
        }
        ```
    - ((63229ba8-e09f-4636-ae39-c8a45b605c87))
      - 运用**递归化简到两两排序**和二分归并
      - ```cpp
        int a[10] = { 13 , 27 , 19 , 2 , 8 , 12 , 2 , 8 , 30 , 89 };
        int b[10];
        void Merge(int a[],int s,int m,int e,int tmp[]) {
          int pb = 0;
          int p1 = s, p2 = m + 1;
          while (p1 <= m && p2 <= e) {
        if (a[p1] < a[p2]) tmp[pb++] = a[p1++];
        else tmp[pb++] = a[p2++];
          }
          while (p1 <= m) tmp[pb++] = a[p1++];
          while (p2 <= e) tmp[pb++] = a[p2++];
          for (int i = 0; i < e - s + 1; i++) a[s+i] = tmp[i];
        }
        void MergeSort(int a[], int s, int e, int tmp[]) {
          if (s < e) {
        int m = (s + e) / 2;//向下取整得到m=s或写作 m=s + (e - s) / 2;
        MergeSort(a, s, m, tmp);
        MergeSort(a, m + 1, e, tmp);
        Merge(a, s, m, e, tmp);
          }
        }
        int main() {
          int size = sizeof(a) / sizeof(int);
          MergeSort(a, 0, size - 1, b);
          for (int i = 0; i < size; ++i)cout << a[i] << " ";
          return 0;
        }
        ```
    - ((63229b76-3951-43fe-bd40-f2b407fd2944))
      mark:: 适用于待排序数据值域较大但分布比较均匀的情况
      - [[stl]] Set 天然自带排序功能
        - ```cpp
          #include <iostream>
          #include <set>
          using namespace std;
          set<int> s;
          int a[105];
          int main(){
            cin>>a[0];
              //a[0] means the array size, to decrease paras of function calling
            for(int i=1;i<=a[0];i++){
              cin>>a[i];
              s.insert(a[i]);
            }
            cout<<s.size()<<endl;
            while(s.size()!=0){
                cout<<*s.begin()<<" ";
                s.erase(s.begin());
            }
            cout<<endl;
            return 0;
          }
          ```
        - | 方法 | 效果 |
          | :----: | :----: |
          |   begin()    |  返回set容器的第一个元素的 地址    |
          |   end()    |   返回set容器的最后一个元素 地址   |
          |   clear()   |   删除set容器中的所有的元素   |
          |   empty()   |   判断set容器是否为空   |
          |   max_size()   |   返回set容器可能包含的元素最大个数   |
          |   size()    |   返回当前set容器中的元素个数   |
          |  erase(it)    |  删除迭代器指针it处元素    |
          |   insert(a)    |    插入某个元素  |
-
- 稳定性 (Stability)
  collapsed:: true
  - 稳定
    - ((63229b85-bfab-4944-9efe-d8a188e60fb2))
    - ((63229b91-6f24-4e28-a44d-d9f2f2945793))
    - ((63229ba8-e09f-4636-ae39-c8a45b605c87))
    - ((63477f68-638f-4130-b766-d305f0ecf06f))
    - ((6327cf4f-8e44-41f6-ab99-b9fdf398e56a))
    - ((6327cf4f-3759-4bad-9563-7662ea7373ef))
  - 不稳定 **希快选堆**
    - ((63229b8b-b393-4d32-899c-be19c41e358d))
    - ((63229b97-21e9-4f05-89a9-76589fe9bec7))
    - ((63229b9b-d803-4609-9750-e622c0decb3e))
    - ((63229ba0-be1e-4ad5-ad52-3d7cfed78250))
-
- 复杂度 [[complexity]]
  collapsed:: true
  - ((63229b8b-b393-4d32-899c-be19c41e358d))
    - Worst-case running time
      - ![image.png](../assets/algo/sort/image_1665720923174_0.png)
      - $cn+c(n−1)+c(n−2)+⋯+2c$
        $=c(n+(n−1)+(n−2)+⋯+2)$
        $=c((n+1)(n/2)−1)$
        $=c(\frac{n(n+1)}{2} −1) \approx c(n^2)$
      - $c$ 表示完成一次交换需要的时间
    - Best-case running time
      - ![image.png](../assets/algo/sort/image_1665721963029_0.png)
      - $\Theta(nlog_{2}n)$
        (Theta, left parenthesis, n, log, start base, 2, end base, n, right parenthesis)
    - More via:
      - [如何证明快速排序法的平均复杂度为 Θ(nlogn)？ - 知乎](https://www.zhihu.com/question/22393997/answer/66668420)
    -
  - ((63477f68-638f-4130-b766-d305f0ecf06f))
    - $n$ 路归并排序，$m$ 个归并段
      - 复杂度 $$log_{n}m$$
-
- Place
  collapsed:: true
  - Out-Place
    - ((63229ba8-e09f-4636-ae39-c8a45b605c87))
      - ((63477f68-638f-4130-b766-d305f0ecf06f))
    - ((6327cf4f-8e44-41f6-ab99-b9fdf398e56a))
    - ((63229b76-3951-43fe-bd40-f2b407fd2944))
    - ((6327cf4f-3759-4bad-9563-7662ea7373ef))
-
- Compare
  collapsed:: true
  - ![](../assets/algo/sort/sort-intro-1.apng)
  - ![sort_comp.png](../assets/algo/sort/sort_comp_1663212086420_0.png){:height 507, :width 747}
-
- 排序优化
  collapsed:: true
  - 一个从 (via: [csdn](https://www.cnblogs.com/laizhenghong2012/p/8442270.html))引用来的一C语言的个例子（C语言内置的qsort函数）
    collapsed:: true
    - ```c
      #include <stdio.h>      /* printf */
      #include <stdlib.h>     /* qsort */
      int values[] = { 40, 10, 100, 90, 20, 25 };
      int compare(const void* a, const void* b){
        return (*(int*)a - *(int*)b);
      }
      int main(){
        int n;
        qsort(values, 6, sizeof(int), compare);
        for (n = 0; n < 6; n++) printf("%d ", values[n]);
        return 0;
      }
      ```
    - **函数原型**
      - ```cpp
        void qsort(
            void *base,//指向数组的起始地址，通常该位置传入的是一个数组名
            size_t nmemb,//表示该数组的元素个数
            size_t size,//表示该数组中每个元素的大小（字节数）
            int (*compar)(const void *, const void *)//此为指向比较函数的函数指针，决定了排序的顺序。（作为回调函数使用 ）
        );
        ```
      - 如果两个元素的值是相同的，那么它们的前后顺序是不确定的。也就是说qsort()是一个不稳定的排序算法。
    - 上述中的决定排序顺序的比较函数: **compar**参数指向一个比较两个元素的函数。 在compar函数内部会将const void *型转换成实际类型
      - `int compar(const void *p1, const void *p2);`
      - 如果compar返回值小于0（< 0），那么p1所指向元素会被排在前面
      - 如果compar返回值等于0（= 0），那么p1指向元素与p2指向元素的顺序**不确定**
      - 如果compar返回值大于0（> 0），那么p2所指向元素会被排在前面
      - **也就是说默认是升序序列**，换序直接作用于比较函数即可。
    - 回调函数：（函数的多层叠加） 通过函数指针调用的函数。 如果把函数的指针（地址）作为参数传递给另一个函数，当这个指针被用来调用其所指向的函数时，就说这是回调函数。
    - 竞赛中的排序有三种：分别是C库的qsort，C++库的sort（第一种是传入一个 functor 对象，另外一种是直接传入一个排序函数），经过下面代码的运行
      - ```cpp
        using namespace std;
        #mark::  _for(i,a,b) for(int i=(a);i<(b);++i)
        const int N = 10000000;
        struct TS {
          int a, b, c;
        };
        inline bool cmp(const TS& t1, const TS&t2) {
          if (t1.a != t2.a)return t1.a < t2.a;
          if (t1.b != t2.b)return t1.b < t2.b;
          return t1.c < t2.c;
        }
        int cmp4qsort(const void* a, const void* b) {
          TS* t1 = (TS*)a, * t2 = (TS*)b;
          if (t1->a != t2->a)return t1->a - t2->a;
          if (t1->b != t2->b)return t1->b - t2->b;
          return t1->c - t2->c;
        }
        struct cmpFunctor {
          inline bool operator()(const TS& t1, const TS& t2) {
            if (t1.a != t2.a)return t1.a < t2.a;
            if (t1.b != t2.b)return t1.b < t2.b;
            return t1.c < t2.c;
          }
        };
        TS tss[N];
        void genData() {
          _for(i, 0, N) {
            tss[i].a = rand();
            tss[i].b = rand();
            tss[i].c = rand();
          }
        }
        int main() {
          srand(time(NULL));
          genData();
          clock_t start = clock();
          sort(tss, tss + N, cmp);
          printf("sort by functor pointer: %ld\n", clock() - start);
          genData();
          start = clock();
          sort(tss, tss + N, cmpFunctor());
          printf("sort by functor: %ld\n", clock() - start);
          genData();
          start = clock();
          qsort(tss, N, sizeof(TS), cmp4qsort);
          printf("qsort by functor pointer: %ld\n", clock() - start);
          return 0;
        }
        ```
        - 运行结果
        - `sort by functor pointer: 27337（36732）（C 5515）(D 3200) sort by functor: 25326（6324）（C 3408）(D 3106) qsort by functor pointer: 9481（15996）（C 3071）(D 2884)`
        - 不知道为什么和作者的测试效果不一样，我的这个编译器（VS2019）测出来qsort是最快的，这点值得商榷。传入排序函数是最慢的这一点是相同的。已经有点混乱了，程序应该是没有问题的呀？和作者测试的不一样，这里先存疑吧？？？
-
- Sort with
  collapsed:: true
  - [[cpp]]
    - ```c++
      #include<algorithm>
      #mark::  sorts(p,m) sort(p,p+m);
      sorts(p,m);//此处只做参考，具体使用的时候再做打算
      //sort ( start , end , cmp(compare) )
      //start表示要排序数组的起始地址；
      //end表示数组结束地址的下一位；
      //cmp用于规定排序的方法，可不填，默认升序。
      ```
-
-
- Refs
  collapsed:: true
  - [排序简介 - OI Wiki](https://oi-wiki.org/basic/sort-intro/)
  - [排序算法 - 维基百科，自由的百科全书](https://zh.wikipedia.org/zh-cn/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95)
  - [qsort()函数详解](https://www.cnblogs.com/laizhenghong2012/p/8442270.html)
  - [十大经典排序算法（动图演示） - 一像素 - 博客园](https://www.cnblogs.com/onepixel/p/7674659.html)
  - 《算法竞赛入门经典第三册——习题与解答》
-