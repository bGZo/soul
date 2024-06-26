alias:: 差分
description:: 一种和前缀和相对的策略，可以当做是求和的逆运算（前缀和逆运算）
description:: [Finite difference - Wikipedia](https://en.wikipedia.org/wiki/Finite_difference)

  - #+BEGIN_NOTE
    将原本需要通过遍历对**区间求加和**的时间 $O(n)$ 降低为 $O(1)$
    #+END_NOTE
  - 这种策略的定义是令 $b_i=\begin{cases}a_i-a_{i-1}\,&i \in[2,n] \\ a_1\,&i=1\end{cases}$
- ## 性质
  - $a_i$ 的值是 $b_i$ 的前缀和，即 $a_n=\sum\limits_{i=1}^nb_i$
  - 计算 $a_i$ 的前缀和 $sum=\sum\limits_{i=1}^na_i=\sum\limits_{i=1}^n\sum\limits_{j=1}^{i}b_j=\sum\limits_{i}^n(n-i+1)b_i$
  - 它可以维护多次对序列的一个区间加上一个数，并在最后询问某一位的数或是多次询问某一位的数。注意修改操作一定要在查询操作之前。
  - #+BEGIN_EXAMPLE
    给定一个数组：[0, 0, 0, 0, 0, 0]
    #+END_EXAMPLE
    - 在 $[2, 4]$ 位置上执行 +2：
      collapsed:: true
      - 得到差分数组：
        $$[0,0,2,0,0,-2]$$
      - 通过求前缀和可以直接得到原数组：
        $$[0,0,2,2,2,0]$$
    - 在 $[2, 4]$ 位置上执行 +2；在 $[1, 3]$ 位置上执行 +1；在 $[3, 4]$ 位置上执行 -3；
      collapsed:: true
      - 得到差分数组：
        $$[0,0,2,0,0,-2]$$
        $$[0,1,2,0,-1,-2]$$
        $$[0,1,2,-3,-1,1]$$
      - 通过求前缀和可以直接得到原数组：
        $$[0,1,3,0,-1,0]$$
  - #+BEGIN_EXAMPLE
    给定一个数组：[1, 2, 3, 4, 5, 6]
    #+END_EXAMPLE
    - 在 $[1, 3]$ 位置上执行 +3；在 $[2, 4]$ 位置上执行 -2；
      - 求得原数组的差分数组：
        $$[1,1,1,1,1,1]$$
      - 执行操作：
        $$[1, 4, 1, 1, -2, 1]$$
        $$[1, 4, -1, 1, -2, 3]$$
  - #+BEGIN_IMPORTANT
    为什么需要在下一个位置上执行反操作？
    #+END_IMPORTANT
    - 我们抽象出需要执行增长的项：$$a$$
    - 然后我们知道在求解前缀和的过程中，区间内的每一项都执行 $$+a$$ 操作；
    - 但是区间之外就无需再进行增长，如何抵消呢？
    - 在区间之外（右边界的下一个位置）取一个 $$-a$$ 操作；🎉
  - 抽象一点的公式是这样的：
    collapsed:: true
    - 譬如使 $[l,r]$ 中的每个数加上一个 $k$，即
      - $$b_l \leftarrow b_l + k,b_{r + 1} \leftarrow b_{r + 1} - k$$
    - 其中 $b_l+k=a_l+k-a_{l-1}$，$b_{r+1}-k=a_{r+1}-(a_r+k)$
    - 最后做一遍前缀和就好了
  - [[cpp/library]] 实现了差分函数 [`std::adjacent_difference`](https://zh.cppreference.com/w/cpp/algorithm/adjacent_difference)，定义于头文件 `<numeric>` 中
- ## ↩ Reference
  - [OI-wiki/prefix-sum.md at 0f9abbd7e7d9623f931fa25c9e20e4c66cc83dfc · OI-wiki/OI-wiki · GitHub](https://github.com/OI-wiki/OI-wiki/blob/0f9abbd7e7d9623f931fa25c9e20e4c66cc83dfc/docs/basic/prefix-sum.md?plain=1)