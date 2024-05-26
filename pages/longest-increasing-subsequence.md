icon:: 👨‍💻
alias:: 最长递增子序列
tags:: #leetcode/medium #动态规划
- ## Content
  - <iframe src="https://leetcode.cn/problems/longest-increasing-subsequence" style="height: 400px"></iframe>
    [LeetCode](https://leetcode.cn/problems/longest-increasing-subsequence/)
- ## Solution
  - 状态转移函数：
    - $$dp[i] = max(dp[j]) +  1$$
      $$ 0 \leq j < i$$
  - 则本题的答案方程为：
    - $$LIS_{length} = max(dp[i])$$
  - ```cpp
    class Solution {
      public:
      int lengthOfLIS(vector<int>& nums) {
        int ans = 0, len = nums.size();
        int *dp = new int[len];
        dp[0] = 1;
        for(int i =0 ; i< len; i++){
          int maxInt = dp[0];
    	
          for(int j =0 ; j< i; j++ ){
            if(nums[i] > nums[j])
              maxInt = max(maxInt, dp[j] + 1);
          }
          dp[i] = maxInt;
        }
        return *max_element(dp, dp + len);
      }
    };
        // for (auto i : dp){
        //     cout<< i << ", "
        // }
        // compiler error
    class Solution {
      public:
      int lengthOfLIS(vector<int>& nums) {
        int ans = 0, len = nums.size();
        int *dp = new int[len];
        for(int i =0 ; i< len; i++){
          dp[i] = 1;
          for(int j =0 ; j< i; j++ ){
            if(nums[i] > nums[j])
              dp[i] = max(dp[i], dp[j] + 1);
          }
        }
        return *max_element(dp, dp + len);
      }
    };
    class Solution {
      public:
      int lengthOfLIS(vector<int>& nums) {
        int n = (int)nums.size();
        if (n == 0) {
          return 0;
        }
        vector<int> dp(n, 0);
        for (int i = 0; i < n; ++i) {
          dp[i] = 1;
          for (int j = 0; j < i; ++j) {
            if (nums[j] < nums[i]) {
              dp[i] = max(dp[i], dp[j] + 1);
            }
          }
        }
        return *max_element(dp.begin(), dp.end());
      }
    };
    ```
    - 时空复杂度： $$O(n^{2})$$
- [第36课 教媳妇编程: 最长递增子序列之动态规划算法 - YouTube](https://www.youtube.com/watch?v=gMunuT3IAfU&t=814s)
  - subseqence
    - 不连续
  - sublist
    - 连续
-