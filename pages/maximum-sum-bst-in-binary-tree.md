icon:: 👨‍💻
tags:: #leetcode/medium 
start:: 20230520
public:: true

- ## Content
  - <iframe src="https://leetcode.cn/problems/maximum-sum-bst-in-binary-tree" style="height: 400px"></iframe>
    [LeetCode](https://leetcode.cn/problems/maximum-sum-bst-in-binary-tree/)
- ## Solution
  -
- ## Conclusion
  - [DFS深度优先搜索，python近百 | 1373. 二叉搜索子树的最大键值和 - 二叉搜索子树的最大键值和 - 力扣（LeetCode）](https://leetcode.cn/problems/maximum-sum-bst-in-binary-tree/solution/dfsshen-du-you-xian-sou-suo-pythonjin-ba-4x4x/)
  - [LeetCode 1373. Maximum Sum BST in Binary Tree - AcWing](https://www.acwing.com/file_system/file/content/whole/index/content/384057/)
    - 判断左右子树和当前结点是否构成二叉搜索树，即当前结点的值是否大于左子树最大值，以及小于右子树最小值。
    - 如果可以，则更新答案，然后返回新的三元组。否则，返回一个表示非法的二叉搜索树的三元组（见代码）。
    - ```cpp
      class Solution {
      public:
          struct T {
              int sum, lo, hi;
              T(int sum_, int lo_, int hi_):sum(sum_), lo(lo_), hi(hi_){}
          };
      
          int ans;
      
          T solve(TreeNode *rt) {
              T tl(0, rt->val, INT_MIN);
              T tr(0, INT_MAX, rt->val);
      		// 后序遍历
             
              if (rt->left) tl = solve(rt->left);
              if (rt->right) tr = solve(rt->right);
      
              if (tl.hi < rt->val && rt->val < tr.lo) {
                  ans = max(ans, tl.sum + rt->val + tr.sum);
                  return T(tl.sum + rt->val + tr.sum, tl.lo, tr.hi);
              }
      
              return T(INT_MIN, INT_MIN, INT_MAX);
          }
      
          int maxSumBST(TreeNode* root) {
              ans = 0;
              solve(root);
              return ans;
          }
      };
      ```