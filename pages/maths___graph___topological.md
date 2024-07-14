description:: 拓扑图

-
- [[sort]] | 拓扑排序
  - Use Case -> 先修课
  - 目标
    - 将所有节点排序，使得排在前面的节点不能依赖于排在后面的节点
  - 定义
    - DAG (有向无环图)
    - 顶点 $u$
    - 边 $(u, v)$
    - 将图中的顶点以线性方式进行排序，使得对于任何的顶点 $u$ 到 $v$ 的有向边 $(u, v)$, 都可以有 $u$ 在 $v$ 的前面
  - 条件
    - 不成环
  - Way
    - (1) 从 DAG 图中选择一个 没有前驱（即入度为0）的顶点并输出。
    - (2) 从图中删除该顶点和所有以它为起点的有向边。
    - (3) 重复 (1) 和 (2) 直到当前的 DAG 图为空或当前图中不存在无前驱的顶点为止。后一种情况说明有向图中必然存在环
    - ```
      L ← Empty list that will contain the sorted elements
      S ← Set of all nodes with no incoming edges
      while S is not empty do
          remove a node n from S
          insert n into L
          for each node m with an edge e from n to m do
              remove edge e from the graph
              if m has no other incoming edges then
                  insert m into S
      if graph has edges then
          return error (graph has at least one cycle)
      else
          return L (a topologically sorted order)
      via: https://oi-wiki.org/graph/topo/
      ```
  - Implement
    - 卡恩 (**Kahn**) 算法 ($G=(V,E)$)
      - 时间复杂度 $O(E+V)$
      - 空间复杂度 $O(V)$
  -
  - via: [拓扑排序 - OI Wiki](https://oi-wiki.org/graph/topo/)
    - [Topological sorting - Wikipedia](https://en.wikipedia.org/wiki/Topological_sorting)
    - [拓扑排序的原理及其实现_dm_vincent的博客-CSDN博客](https://blog.csdn.net/dm_vincent/article/details/7714519)
-
-
-