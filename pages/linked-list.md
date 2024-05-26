alias:: data-structure/linked-list
-
-
- 单向链表
  collapsed:: true
  - 缺点
    collapsed:: true
    - 只能通过一个结点的引用访问其后续结点，而无法直接访问其前驱结点，要在单链表中找到某个结点的前驱结点，必须从链表的首结点出发依次向后寻找，但是需要Ο(n)时间
- 双向链表 / 循环链表
  collapsed:: true
  - 扩展单链表结点结构很简单，在单链表结点结构中新增加一个域，该域用于指向结点的直接前驱结点即可
-
- Refs
  - [链表 - OI Wiki](https://oi-wiki.org/ds/linked-list/)