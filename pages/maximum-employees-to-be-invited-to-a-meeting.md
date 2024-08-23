icon:: 👨‍💻
tags:: #leetcode/hard
created:: [[20231101]]

- ## Content
  - <iframe src="https://leetcode.cn/problems/maximum-employees-to-be-invited-to-a-meeting" style="height: 400px"></iframe>
    [LeetCode](https://leetcode.cn/problems/maximum-employees-to-be-invited-to-a-meeting/)
- ## Solution
  - ```java
    class Solution {
      public int maximumInvitations(int[] favorite) {
        int n = favorite.length;
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
          graph.add(new ArrayList<>());
        }
        int[] in = new int[n];// 获取所有节点入度
        for (int i = 0; i < n; i++) {
          graph.get(i).add(favorite[i]);
          in[favorite[i]]++;
        }
        LinkedList<Integer> queue = new LinkedList<>();// 把入度为零的节点加入队列
        for (int i = 0; i < n; i++) {
          if (in[i] == 0) {
            queue.addLast(i);
          }
        }
        while (!queue.isEmpty()) {// 队列为空后，如果还有入度不为零的节点，他们将成环
          int cur = queue.removeFirst();
          for (int next : graph.get(cur)) {
            if (--in[next] == 0) {
              queue.addLast(next);
            }
          }
        }
        int ans = 0;
        boolean[] visited = new boolean[n];
        HashMap<Integer, Integer> map = new HashMap<>();// 获取双向奔赴的两个节点
        for (int i = 0; i < n; i++) {
          if (in[i] == 1 && !visited[i]) {
            int cur = i;
            int cnt = 0;
            while (!visited[cur]) {
              cnt++;
              visited[cur] = true;
              cur = favorite[cur];
            }
            if (cnt > 2) {
              ans = Math.max(ans, cnt);// 如果当前环是多人首尾相连，那么答案可能在其中，取最大
            } else {
              map.put(i, favorite[i]);// 双向奔赴
            }
          }
        }
        graph = new ArrayList<>();// 构建反图，为了获取从双向奔赴节点到最远端节点的距离
        for (int i = 0; i < n; i++) {
          graph.add(new ArrayList<>());
        }
        for (int i = 0; i < n; i++) {
          graph.get(favorite[i]).add(i);
        }
        int best = 0;// 所有双向奔赴节点都可以参与会议
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
          int i = entry.getKey();
          int j = entry.getValue();
          // 从双向奔赴节点两侧各自宽度优先遍历，获取最大深度
          queue.add(i);
          int level = 0;
          while (!queue.isEmpty()) {
            int size = queue.size();
            while (size-- > 0) {
              int cur = queue.removeFirst();
              for (int next : graph.get(cur)) {
                if (next != j) {
                  queue.addLast(next);
                }
              }
            }
            level++;
          }
          queue.add(j);
          while (!queue.isEmpty()) {
            int size = queue.size();
            while (size-- > 0) {
              int cur = queue.removeFirst();
              for (int next : graph.get(cur)) {
                if (next != i) {
                  queue.addLast(next);
                }
              }
            }
            level++;
          }
          best += level;
        }
        return Math.max(ans, best);// 返回（多人首尾相连最大值） 与 （双向奔赴节点集群累加和）的最大值
      }
    }
    ```
- ## Conclusion
  -