icon:: 👨‍💻
tags:: #leetcode/simple #array
created:: [[20230529]]

- ## Content
  - <iframe src="https://leetcode.cn/problems/average-value-of-even-numbers-that-are-divisible-by-three" style="height: 400px"></iframe>
    [LeetCode](https://leetcode.cn/problems/average-value-of-even-numbers-that-are-divisible-by-three/)
- ## Solution
  - ```cpp
    class Solution {
      public:
      int averageValue(vector<int>& nums) {
        int ans = 0, count = 0;
        for( auto num : nums){
          if(num % 6 == 0){
            ans += num;
            count++;
          }
        }
        if(count) return ans/count;
        else return 0;
      }
    };
    ```
- ## Conclusion
  -
-