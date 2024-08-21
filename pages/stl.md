also:: cpp/stl
tags:: #[[data-structure]], #[[algorithm]]

- [[cpp]] STL 内置用法:
  collapsed:: true
  - `find`：顺序查找。`find(v.begin(), v.end(), value)`，其中 `value` 为需要查找的值。
  - `find_end`：逆序查找。`find_end(v.begin(), v.end(), value)`。
  - `reverse`：翻转数组、字符串。`reverse(v.begin(), v.end())` 或 `reverse(a + begin, a + end)`。
  - `unique`：去除容器中相邻的重复元素。`unique(ForwardIterator first, ForwardIterator last)`，返回值为指向 **去重后** 容器结尾的迭代器，原容器大小不变。与 `sort` 结合使用可以实现完整容器去重。
  - ~~`random_shuffle`：随机地打乱数组。`random_shuffle(v.begin(), v.end())` 或 `random_shuffle(v + begin, v + end)`。~~
  - `sort`：排序。`sort(v.begin(), v.end(), cmp)` 或 `sort(a + begin, a + end, cmp)`，其中 `end` 是排序的数组最后一个元素的后一位，`cmp` 为自定义的比较函数。
  - `stable_sort`：稳定排序，用法同 `sort()`。
  - `nth_element`：按指定范围进行分类，即找出序列中第 $n$ 大的元素，使其左边均为小于它的数，右边均为大于它的数。`nth_element(v.begin(), v.begin() + mid, v.end(), cmp)` 或 `nth_eleme nt(a + begin, a + begin + mid, a + end, cmp)`。
  - `binary_search`：二分查找。`binary_search(v.begin(), v.end(), value)`，其中 `value` 为需要查找的值。
  - `merge`：将两个（已排序的）序列 **有序合并** 到第三个序列的 **插入迭代器** 上。`merge(v1.begin(), v1.end(), v2.begin(), v2.end() ,back_inserter(v3))`。
  - `inplace_merge`：将两个（已按小于运算符排序的）：`[first,middle), [middle,last)` 范围 **原地合并为一个有序序列**。`inplace_merge(v.begin(), v.begin() + middle, v.end())`。
  - `lower_bound`：在一个有序序列中进行二分查找，返回指向第一个 **大于等于**  $x$ 的元素的位置的迭代器。如果不存在这样的元素，则返回尾迭代器。`lower_bound(v.begin(),v.end(),x)`。
  - `upper_bound`：在一个有序序列中进行二分查找，返回指向第一个 **大于**  $x$ 的元素的位置的迭代器。如果不存在这样的元素，则返回尾迭代器。`upper_bound(v.begin(),v.end(),x)`。
    - `lower_bound` 和 `upper_bound` 的时间复杂度"
      在一般的数组里，这两个函数的时间复杂度均为 $O(\log n)$ ，但在 `set` 等关联式容器中，直接调用 `lower_bound(s.begin(),s.end(),val)` 的时间复杂度是 $O(n)$ 的。
  - `next_permutation`：将当前排列更改为 **全排列中的下一个排列**。如果当前排列已经是 **全排列中的最后一个排列**（元素完全从大到小排列），函数返回 `false` 并将排列更改为 **全排列中的第一个排列**（元素完全从小到大排列）；否则，函数返回 `true`。`next_permutation(v.begin(), v.end())` 或 `next_permutation(v + begin, v + end)`。
  - `partial_sum`：求前缀和。设源容器为 $x$ ，目标容器为 $y$ ，则令 $y[i]=x[0]+x[1]+...+x[i]$ 。`partial_sum(src.begin(), src.end(), back_inserter(dst))`。
-
- Outline
  collapsed:: true
  - Input/output
  - Strings
  - algorithm
  - functional
  - Containers
    collapsed:: true
    - Sequence containers
    - Associative containers
    - Unordered associative containers
  - C standard library
    collapsed:: true
    - **General topics**
      collapsed:: true
      - Data types
      - Character classification
      - Strings
      - Mathematics
      - File input/output
      - Date/time
      - Localization
      - Memory allocation
      - Process control
      - Signals
      - Alternative tokens
    - **Miscellaneous headers**
      collapsed:: true
      - <assert.h>
      - <errno.h>
      - <setjmp.h>
      - <stdarg.h>
-
- Refs
  - https://en.wikipedia.org/wiki/Standard_Template_Library
-