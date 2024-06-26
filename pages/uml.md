alias:: lang/modeling/unified
tags:: #[[software/pattern]]
description:: Unified Modeling Language; UML打算成為可以對並發和分布式系統的標準建模語言; UML使用一套與Java語言或其他面向對象語言等價物. 同時也是本體論等價物的圖形標記

-
- [[Quickref]]
  collapsed:: true
  - {{embed ((63491e31-6a93-4ce5-9330-372765c2ef57))}}
-
- Outline
  - History
    collapsed:: true
    - 1997年
      collapsed:: true
      - UML被對象管理組織接納為標準，並在此之後受該組織管理
    - 2005年
      collapsed:: true
      - UML被國際標準化組織接納為一種標準自此，該標準被定期修訂以涵蓋UML的最新版本
      - 軟件工程中，大多數從業者不使用UML，而是產生非正式的手繪圖
        collapsed:: true
        - 不過，這些圖例中仍往往包括UML的元素
  - Module 模型 (3)
    collapsed:: true
    - 功能模型
      collapsed:: true
      - 从用户的角度展示系统的功能
        collapsed:: true
        - 用例图
    - 对象模型
      collapsed:: true
      - 采用对象，属性，操作，关联等概念展示系统的结构和基础
        collapsed:: true
        - 类别图
        - 对象图
    - 动态模型
      collapsed:: true
      - 展现系统的内部行为
        collapsed:: true
        - 序列图
        - 活动图
        - 状态图
  - Shape 图形
    - ![image.png](../assets/uml/image_1655795835076_0.png)
    - 结构性图形（Structure diagrams）强调**系统式的建模**
      - 静态图（static diagram）
        - 类图（Class Diagram）
          id:: 63491e31-6a93-4ce5-9330-372765c2ef57
          - ![image.png](../assets/uml/image_1655796205788_0.png)
          - 依赖 (Dependency)
            - ![image.png](../assets/uml/image_1655796723111_0.png)
          - 关联 (Association)
            - ![image.png](../assets/uml/image_1655796730332_0.png)
          - 聚合 (Aggregation)
            - ![image.png](../assets/uml/image_1655796737007_0.png)
          - 组合 (Composition)
            - ![image.png](../assets/uml/image_1655796742972_0.png)
          - 继承 (Generalization)
            - ![image.png](../assets/uml/image_1655796754787_0.png){:height 394, :width 310}
          - 实现 (Implementation)
            - ![image.png](../assets/uml/image_1655796763181_0.png)
        - 对象图（Object diagram）
          - ![image.png](../assets/uml/image_1655796219356_0.png)
        - 包图（Package diagram）
          - ![image.png](../assets/uml/image_1655796229157_0.png)
      - 实现图（implementation diagram）
        - 组件图（Component diagram）
          - ![image.png](../assets/uml/image_1655796253349_0.png)
        - 部署图（Deployment diagram）
          - ![image.png](../assets/uml/image_1655796261640_0.png)
      - 剖面图
      - 复合结构图
    - 行为式图形（Behavior diagrams）强调**系统模型中触发的事件**
      - 活动图
      - 状态图
      - 用例图
    - 交互性图形（Interaction diagrams）强调**系统模型中的资料流程**:
      - 属于行为图形的子集合
      - 通信图
      - 交互概述图（UML 2.0）
      - 时序图（UML 2.0）
      - 时间图（UML 2.0）
  - Use Case 用例
    collapsed:: true
    - ![image.png](../assets/book/大话设计模式/image_1648016765556_0.png)
-
- Refs
  - [Unified Modeling Language - Wikipedia](https://en.wikipedia.org/wiki/Unified_Modeling_Language)
  - [设计模式之 UML 类图 - 知乎](https://zhuanlan.zhihu.com/p/24576502)
  - https://www.youtube.com/watch?v=R9SXpaD_aB4
  - [UML类图的6种连线示意 - 简书](https://www.jianshu.com/p/48de81a8f0ab)
  - [er图 和 类图 区别 - Google Search](https://www.google.com.hk/search?q=er%E5%9B%BE+%E5%92%8C+%E7%B1%BB%E5%9B%BE+%E5%8C%BA%E5%88%AB&newwindow=1)
  -