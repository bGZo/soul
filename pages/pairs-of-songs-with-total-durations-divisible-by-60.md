icon:: 👨‍💻
tags:: #leetcode/medium #hashtable 
start:: 20230507
public:: true

- ## Content
  - <iframe src="https://leetcode.cn/problems/pairs-of-songs-with-total-durations-divisible-by-60" style="height: 600px"></iframe>
    [LeetCode](https://leetcode.cn/problems/pairs-of-songs-with-total-durations-divisible-by-60/)
- ## Solution
  - ```cpp
    class Solution {
    public:
        int numPairsDivisibleBy60(vector<int>& time) {
            std::unordered_map<int, int> hm;
            int ans =0;
            for(auto t: time) {
                t %= 60;
                if( t == 0 ){
                    ans+= hm[t];
                }else{
                    ans+= hm[60-t];
                }
                hm[t] ++;
            }
            return ans;
        }
    }
    ```
- ## Conclusion
  - 今后遇到一次一次过不去的情况下就换方法吧，不要太钻牛角尖了。
  - 总是喜欢用模拟的思路去解题，源自于自己乱七八糟的解题方法，但是这种方法需要考虑的情况实在是太多了，就像是一个地狱，永远没有尽头。
    - 就像是这道题，最后一次我已经避免掉了溢出的可能，但是还是不知道少考虑了哪种情况，不知道要从哪里去下手：
      - ```cpp
        class Solution {
          public:
          int numPairsDivisibleBy60(vector<int>& time) {
            std::unordered_map<int, int> hm;
        
            int len = time.size();
            int ans = 0;
        
            for(int i=0; i<len; i++ ){
              time[i]%=60;
              hm[time[i]] ++;
              cout<<time[i]<<", ";
            }
            cout<<endl;
        
            bool flag[61] = {false};
            for (auto iter = hm.begin(); iter != hm.end(); ++iter) {
              if(flag [60 - iter->first] == false){
                unsigned long long int sum;
                if(iter->first * 2 == 60 || iter->first == 0) {
                  // 阶乘/2
                  sum=1;
                  for(int i=1; i <= hm[iter->first]; i++){
                    sum *= i;
                  }
                  if(iter->first != 0 || sum != 1){
                    sum /= 2 ;
                  }
                }else{
                  sum = hm[60 - iter->first] * hm[iter->first];
                }
        
                ans += sum;
                flag [60 - iter->first] = true;
                flag [iter->first] = true;
              }
            }
            return ans;
          }
        };
        ```
    - 迭代器的做法更是如此了，在内存循环把迭代器的某个未来元素删除之后，父级的迭代器就坏了，所以会报内存错误。
      - [C++ STL unordered_map删除元素：erase()和clear() (biancheng.net)](http://c.biancheng.net/view/7247.html)
  - collapsed:: true
    ```cpp
    bool mark[100] = { true }
    ```
    - 我不知道把这个语句放在全局和主函数里执行结果一不一样，我觉得应该不一样，但默认是 False 的，习惯上我也一直这么定义，所以总是漏掉了这种情况。
  - HashMap（ `unordered_map` in cpp） 是乱序的，直接以迭代器遍历是鲁莽的做法；
  - [std::unordered_map<Key,T,Hash,KeyEqual,Allocator>::contains - cppreference.com](https://en.cppreference.com/w/cpp/container/unordered_map/contains)
    - `contains` >= C++20
-