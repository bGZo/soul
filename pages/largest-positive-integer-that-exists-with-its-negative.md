icon:: 👨‍💻
tags:: #leetcode/simple #hashtable #two-pointers  
start:: 20230513
public:: true

- ## Content
  - <iframe src="https://leetcode.cn/problems/largest-positive-integer-that-exists-with-its-negative" style="height: 400px"></iframe>
    [LeetCode](https://leetcode.cn/problems/largest-positive-integer-that-exists-with-its-negative/)
- ## Solution
  - ```cpp
    class Solution {
    public:
        int findMaxK(vector<int>& nums) {
            unordered_set<int> hs;
            int len = nums.size(), maxK = -1;
            for(int i =0; i<len; i++){
                hs.insert(nums[i]);
                if(hs.find(-nums[i]) != hs.end()){
                    maxK = max(abs(nums[i]), maxK);
                }
            }
            return maxK ;
        }
    };
    ```
  - ```java
    class Solution {
      public int findMaxK(int[] nums) {
        HashSet<Integer> hs = new HashSet<>();
    
        int len = nums.length, maxK = -1;
        for(int i =0 ; i< len; i++){
          hs.add(nums[i]);
    
          if(hs.contains(-nums[i])){
            maxK = Math.max(Math.abs(nums[i]), maxK);
          }
        }
        return maxK;
      }
    }
    ```
- ## Conclusion
  - CPP 的集合好像没有 Contains 方法，判断是否存在 Key 只发现用 `find` 这一种方法。
  - Java 集合用 `add`，字符串、List用 `insert`；CPP 字符串和集合基本都用 `insert`；
    - #+BEGIN_QUOTE
      命名不同，主要是为了反映它们在底层数据结构上的不同特点和性能表现。这样的命名约定有助于开发者更清晰地理解和使用不同的集合类，并根据具体的需求选择适当的实现类。
      ...
      `add()`方法可以联想到在集合末尾添加元素，`insert()`方法可以联想到在集合中间或指定位置插入元素。
      by ``chatGPT
      #+END_QUOTE
    - 尽管 chatGPT 否认了这一事实，列举出一点例外的数据结构，如：
      - `std::vector`: 使用 `push_back()` 方法在末尾插入元素，也可以使用 `insert()` 方法在指定位置插入元素。
      - `std::deque`: 使用 `push_back()` 方法在末尾插入元素，也可以使用 `push_front()` 方法在头部插入元素，或者使用 `insert()` 方法在指定位置插入元素。
      - 但其他如`std::set`、`std::map`、`std::unordered_set`、`std::unordered_map`均只有 `insert` 方法。
-