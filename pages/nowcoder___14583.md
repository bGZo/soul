icon:: 👨‍💻
tags:: #prefix_sum
description:: [糖糖别胡说，我真的不是签到题目](https://ac.nowcoder.com/acm/problem/14583)
created:: 20230205

- ## Content
  - 从前，有 nnn 只萌萌的糖糖，他们分成了==两组==一起玩游戏。他们会排成一排，第 iii 只糖糖会随机得到一个能力值 bib_ibi​。从第 iii 秒的时候，第 iii 只糖糖就可以消灭掉所有排在他前面的和他不是同一组的且能力值小于他的糖糖。
  - 为了使游戏更加有趣，糖糖的爸爸，娇姐，会发功 mmm 次，第 iii 次发功的时间为 cic_i ci​，则在第 cic_ici​ 秒结束后，b1,b2,.....,bcib_1,b_2,.....,b_{c_i}b1​,b2​,.....,bci​​都会增加 1.
  - 现在，娇姐想知道在第 nnn 秒后，会有多少只糖糖存活下来。
- ## Solution
  - https://ac.nowcoder.com/discuss/412302
  - 任何问题都有一个从简单到复杂的过程——先考虑没有娇姐发功怎么做：
    - 我们可以考虑每只糖糖最后能不能存活：第i只糖糖能存活的条件是他后面没有比他大的另外一组的糖糖，所以我们只需要从后往前扫描维护当前位置往后每一组糖糖的最大值是多少然后和当前糖糖的能力值比较就行。
  - 现在再来考虑娇姐发功的问题：
    - 娇姐会在第ci秒使得前ci个人的能力值+1，其实不影响第ci个糖糖在第ci秒消灭他前面的糖糖——大家都加一，大小关系不变；但是会影响后面的糖糖打他。
    - 换句话说，第x个糖糖开始能打前面的糖糖的时候看到的前面的糖糖数字是第x秒的数字，而随着之后大家一起增大，大小关系就不变了，所以用每个人最后他的能力值判断能不能存活就行了。
    - 于是我们只需要把先得出每个糖糖最后的能力值，再从后往前判断他是否还存活。维护每个糖糖最后的能力值可以用差分来维护，也可也累加一下当前位置x即x往后贡献了多少个加一就可以了
  - ```cpp
    #include<bits/stdc++.h>
    using namespace std;
    int idx[50010];
    int main(){
        int T;
        cin>>T;
        while(T--){
            int n, m;
            cin>>n>>m;
            int *suger = new int[n+1];
            int *suger_group = new int [n+1];
            memset(idx,0,sizeof(idx));
            for(int i = 1; i<=n; i++){
                cin >> suger_group[i] >> suger[i];
            }
            while(m--){
                int gong;
                cin>>gong;
                idx[1]++;
                idx[gong+1]--;
                //差分
            }
            for(int i=1; i<=n; i++){
                idx[i] += idx[i-1];
                suger[i] += idx[i];
                // 求前缀和还原数组
            }
            int max_group0 = -1,
                max_group1 = -1,
                ans = 0;
            for(int i = n; i>=1; i--){
                if(suger_group[i] == 0){
                    max_group0 = max(max_group0, suger[i]);
                }else{
                    max_group1 = max(max_group1, suger[i]);
                }
                if(suger_group[i]==0 && suger[i]>=max_group1)
                    ans++;
                if(suger_group[i]==1 && suger[i]>=max_group0)
                    ans++;
            }
            cout<< ans << endl;
        }
    }
    ```
- ## Conclusion
  - 一开始没看清楚题是分 2 组；
  - 然后写出来了怎么也过不了，才发现是一开始`suger` `suger_group` 两个变量写反了😅
  - 数组越界就往外多开一个就好了；
  - 然后，还是不想写Java... TM的我怎么知道都在哪个包下...
    - [ACM模式下 Java 导入包_牛客网](https://www.nowcoder.com/discuss/815927)
-