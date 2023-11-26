title:: index/mysql
alias:: mysql/index
tags:: #[[data-structure]], TODO
define:: "一种用于快速查询和检索数据的数据结构"

  - Use Case
    - `not null`(**Best**) & `where` & `having`
    - Tip: 如果长时间都会有排序的需求, 可以用 带有 `groupby` 的`alter` 语句提前
  - 特点
    collapsed:: true
    - 优点
      - [主因] 大大加快 **数据的检索速度** (大大减少检索的数据量)
      - 通过创建唯一性索引，可以保证数据库表中每一行数据的唯一性。
    - 缺点
      - 创建索引和维护索引需要耗费许多时间。当对表中的数据进行增删改的时候，如果数据有索引，那么索引也需要动态的修改，会**降低 SQL 执行效率**
      - 索引需要使用**物理文件存储**, 也会耗费一定空间
  - [[data-structure]]
    collapsed:: true
    - Hash
    - B 树
    - B+ 树
  - Category
    collapsed:: true
    - 主键索引 (Primary Key)
    - 二级索引 (辅助索引)
      define:: "二级索引的叶子节点存储的数据是主键, 也就是说，通过二级索引，可以定位主键的位置"
      - 普通索引, Index
        - 作用(1)
          - 快速查询数据
        - 一张表允许创建多个普通索引，并允许数据重复和 NULL
      - 唯一索引, Unique Key
        - 唯一索引也是一种约束。**唯一索引的属性列不能出现重复的数据，但是允许数据为 NULL，一张表允许创建多个唯一索引。** 建立唯一索引的目的大部分时候都是为了该属性列的数据的唯一性，而不是为了查询效率。
      - 前缀索引, Prefix
        collapsed:: true
        - 前缀索引只适用于字符串类型的数据。前缀索引是对文本的前几个字符创建索引，相比普通索引建立的数据更小， 因为只取前几个字符。
      - 全文索引, Full Text
        collapsed:: true
        - 全文索引主要是为了检索大文本数据中的关键字的信息，是目前搜索引擎数据库使用的一种技术。Mysql5.6 之前只有 MYISAM 引擎支持全文索引，5.6 之后 InnoDB 也支持了全文索引。
  - 聚集索引与非聚集索引
    collapsed:: true
    - 聚集索引, cluster index
      define:: "索引结构和数据一起存放的索引"
      -
    - 非聚集索引, non-cluster index
      define:: "索引结构和数据分开存放的索引"
  - 覆盖索引 ???
  - 联合/组合/复合 索引 ???
-
- [[interview]]
  collapsed:: true
  - 为什么使用索引?
  - 索引是怎么工作的?
  - 为什么 MySql 索引采用 B+ 树?
-
- Refs
  - [MySQL索引详解 | JavaGuide](https://javaguide.cn/database/mysql/mysql-index.html)