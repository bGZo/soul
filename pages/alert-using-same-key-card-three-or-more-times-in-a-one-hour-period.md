icon:: 👨‍💻
tags:: #leetcode/medium 
mark:: [1604. 警告一小时内使用相同员工卡大于等于三次的人](https://leetcode.cn/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/)
start:: 20230207

- icon:: 👨‍💻
  tags:: #leetcode/medium 
  start:: 20230514
  public:: true
- ## Content
  - <iframe src="https://leetcode.cn/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period" style="height: 400px"></iframe>
    [LeetCode](https://leetcode.cn/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/)
- ## Solution
  -
## Conclusion
  - 多声明局部变量是一个好习惯，有时候为了紧凑的写法，而不考虑写更清晰的局部变量非常不明智 #code/style
    - ```java
      for(int i = 0; i<keyName.length; i++){
        hm.putIfAbsent(keyName[i], new ArrayList<>());
      
        Integer hour = (keyTime[i].charAt(0) -'0')* 10 + (keyTime[i].charAt(1) - '0');
        Integer minute = (keyTime[i].charAt(3) - '0')* 10 + (keyTime[i].charAt(4) - '0');
        timeMap.get(keyName[i]).add(hour*60+minute);
      }
      // Integer hour = (keyTime[i].charAt(0) -'0')* 10 + (keyTime[i].charAt(1) - '0');
      //                                                    ↑
      // 这里非常容易写错，是冗余的写法；
      for (int i = 0; i < n; i++) {
        String name = keyName[i];
        String time = keyTime[i];
        timeMap.putIfAbsent(name, new ArrayList<Integer>());
        int hour = (time.charAt(0) - '0') * 10 + (time.charAt(1) - '0');
        int minute = (time.charAt(3) - '0') * 10 + (time.charAt(4) - '0');
        timeMap.get(name).add(hour * 60 + minute);
      }
      ```
  - ```
    *// error        ArrayList<String> key_time = (ArrayList<String>) Arrays.asList(keyTime);
    **// right        ArrayList<String> key_time = new ArrayList<>(Arrays.asList(keyTime));
    *
    ```