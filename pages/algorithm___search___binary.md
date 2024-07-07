title:: algorithm/search/binary
description:: "binary(二分), half-interval(折半),logarithmic(对数), 在一个升序数组中查找一个数, 难点在于到底要给 mid ± 1, while 里到底用  <= / <"
tags:: #[[sort]]

- >Although the basic idea of binary search is comparatively straightforward, the details can be surprisingly tricky | 思路很简单，细节是魔鬼
  — [Donald Knuth](https://en.wikipedia.org/wiki/Donald_Knuth)(1998). *Sorting and searching*. [The Art of Computer Programming](https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming). Vol. 3 (2nd ed.). Reading, MA: Addison-Wesley Professional. [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier)) [978-0-201-89685-5](https://en.wikipedia.org/wiki/Special:BookSources/978-0-201-89685-5).
-
- > 管他左侧还右侧，搜索区间定乾坤
  搜索一个元素时，搜索区间两端闭。
  while 条件带等号，否则需要打补丁。
  if 相等就返回，其他的事甭操心。
  mid 必须加减一，因为区间两端闭。
  while结束就凉了，凄凄惨惨返 -1。
  搜索左右边界时，搜索区间要阐明。
  >
  >左闭右开最常见，其余逻辑便自明：
  while要用小于号，这样才能不漏掉。
  if 相等别返回，利用mid锁边界。
  mid 加一或减一？要看区间开或闭。
  while结束不算完，因为你还没返回。
  索引可能出边界，if检查保平安。
  via: [我写了首诗，让你闭着眼睛也能写对二分搜索 :: labuladong的算法小抄](https://labuladong.github.io/algo/2/20/29/)
- ```java
  int binarySearch(int[] nums, int target) {
      int left = 0, right = ...;
      while(...) {
          int mid = left + (right - left) / 2;
          // NOTE: left + (right - left) / 2  better than  (left + right) / 2
          if (nums[mid] == target) {
              ...
          } else if (nums[mid] < target) {
              left = ...
          } else if (nums[mid] > target) {
              right = ...
          }
      }
      return ...;
  }
  ```
  - Basic
    - 因为我们初始化 right = nums.length - 1
      所以决定了我们的「搜索区间」是 [left, right]
      所以决定了 **while** (left <= right)
      同时也决定了 left = mid+1 和 right = mid-1
      因为我们只需找到一个 target 的索引即可
      所以当 nums[mid] == target 时可以立即返回
    - // 左开右开的写法
      int binary_search(int[] nums, int target) {
          int left = 0,
            right = nums.length - 1; // 注意
          while(left <= right) {
              int mid = left + (right - left) / 2;
              if (nums[mid] < target) {
                  left = mid + 1;   // 注意
              } else if (nums[mid] > target) {
                  right = mid - 1;  // 注意
              } else if(nums[mid] == target) {
                  return mid;
              }
          }
          return -1;
      }
  - Left Bound
    collapsed:: true
    - ```cpp
      // 左开右开的写法
      int left_bound(int[] nums, int target) {
          int left = 0, right = nums.length - 1;
          while (left <= right) {
              int mid = left + (right - left) / 2;
              if (nums[mid] < target) {
                  left = mid + 1;
              } else if (nums[mid] > target) {
                  right = mid - 1;
              } else if (nums[mid] == target) {
                  // 别返回，锁定左侧边界
                  right = mid - 1;
              }
          }
          // 判断 target 是否存在于 nums 中
          // 此时 target 比所有数都大，返回 -1
          if (left == nums.length) return -1;
          // 判断一下 nums[left] 是不是 target
          return nums[left] == target ? left : -1;
      }
      // 左开右闭的写法
      int left_bound(int[] nums, int target) {
          int left = 0,
            right = nums.length; // 注意
          while (left < right) { // 注意
              int mid = left + (right - left) / 2;
              if (nums[mid] == target) {
                  right = mid;
              } else if (nums[mid] < target) {
                  left = mid + 1;
              } else if (nums[mid] > target) {
                  right = mid; // 注意
              }
          }
          return left;
      }
      ```
    - 左开右闭的写法:
      因为我们初始化 right = nums.length
      所以决定了我们的「搜索区间」是 [left, right)
      所以决定了 **while** (left < right)
      同时也决定了 left = mid + 1 和 right = mid
      因为我们需找到 target 的最左侧索引
      所以当 nums[mid] == target 时不要立即返回
      而要收紧右侧边界以锁定左侧边界
  - Right Bound
    collapsed:: true
    - ```java
      // 左开右开的写法
      int right_bound(int[] nums, int target) {
          int left = 0, right = nums.length - 1;
          while (left <= right) {
              int mid = left + (right - left) / 2;
              if (nums[mid] < target) {
                  left = mid + 1;
              } else if (nums[mid] > target) {
                  right = mid - 1;
              } else if (nums[mid] == target) {
                  // 别返回，锁定右侧边界
                  left = mid + 1;
              }
          }
          // 此时 left - 1 索引越界
          if (left - 1 < 0) return -1;
          // 判断一下 nums[left] 是不是 target
          return nums[left - 1] == target ? (left - 1) : -1;
      }
      // 左开右闭的写法
      int right_bound(int[] nums, int target) {
          int left = 0, right = nums.length;
          while (left < right) {
              int mid = left + (right - left) / 2;
              if (nums[mid] == target) {
                  left = mid + 1; // 注意
              } else if (nums[mid] < target) {
                  left = mid + 1;
              } else if (nums[mid] > target) {
                  right = mid;
              }
          }
          return left - 1; // 注意
      }
      ```
    - 左开右闭的写法:
      因为我们初始化 right = nums.length
      所以决定了我们的「搜索区间」是 [left, right)
      所以决定了 **while** (left < right)
      同时也决定了 left = mid + 1 和 right = mid
      因为我们需找到 target 的最右侧索引
      所以当 nums[mid] == target 时不要立即返回
      而要收紧左侧边界以锁定右侧边界
      又因为收紧左侧边界时必须 left = mid + 1
      所以最后无论返回 left 还是 right，必须减一
    -
  -
-
- 时空
  - 最优时间复杂度为 $O(1)$
  - 平均时间复杂度和最坏时间复杂度均为 $O(log n)$
  - 空间复杂度为 $O(1)$
  - 递归（无尾调用消除）版本的二分查找的空间复杂度为 $O(log n)$
    description:: "尾调用是指一个函数里的最后一个动作是返回一个函数的调用结果的情形, 经过适当处理，尾递归形式的函数的运行效率可以被极大地优化。尾调用原则上都可以通过简化函数调用栈的结构而获得性能优化（称为“尾调用消除”），但是优化尾调用是否方便可行取决于运行环境对此类优化的支持程度如何"
    source:: https://zh.wikipedia.org/zh-cn/%E5%B0%BE%E8%B0%83%E7%94%A8
-
- Implement with [[stl]]
-
-
- Refs
  - [二分 - OI Wiki](https://oi-wiki.org/basic/binary/)