alias:: Not Only SQL, 不仅仅是SQL
define:: 对不同于传统的关系型数据库的数据库管理系统的统称, nosql 用于超大规模数据的存储, 这些类型的数据存储不需要固定的模式，无需多余操作就可以横向扩展
mark:: 用户数据和操作日志成倍的增加，如果要对这些数据进行挖掘，只能使用 NoSQL

  - 优点
    collapsed:: true
    - 高可扩展性
    - 分布式计算
    - 低成本
    - 架构的灵活性，半结构化数据
    - 没有复杂的关系
  - 缺点
    collapsed:: true
    - 没有标准化
    - 有限的查询功能（到目前为止）
    - 最终一致是不直观的程序
-
- ## [[Quickref]]
  - | 类型          | 部分代表                                            |
    |---------------|-----------------------------------------------------|
    | 列存储        | Hbase Cassandra Hypertable                          |
    | 文档存储      | MongoDB CouchDB                                     |
    | key-value存储 | Tokyo Cabinet / Tyrant Berkeley DB MemcacheDB Redis |
    | 图存储        | Neo4J FlockDB                                       |
    | 对象存储      | db4o Versant                                        |
    | xml数据库     | Berkeley DB XML BaseX                               |
    - **列存储** 方便存储结构化和半结构化数据，做数据压缩，对针对某一列或者某几列的查询有非常大的IO优势
    - **文档存储** 用类似json的格式存储，存储的内容是文档型的。这样也就有机会对某些字段建立索引，实现关系数据库的某些功能
    - **key-value存储** 快速查询到其value
    - **图存储** 图形关系的最佳存储
    - **对象存储** 通过类似面向对象语言的语法操作数据库，通过对象的方式存取数据
    - **xml数据库** 支持XML的内部查询语法
  -
  - 关系数据库管理系统 (RDBMS) #vs NoSQL
    - RDBMS
      - 高度组织化结构化数据
      - 结构化查询语言（SQL） (SQL)
      - 数据和关系都存储在单独的表中。
      - 数据操纵语言，数据定义语言
      - 严格的一致性
      - 基础事务
    - NoSQL
      - 代表着不仅仅是SQL
      - 没有声明性查询语言
      - 没有预定义的模式
        -键 - 值对存储，列存储，文档存储，图形数据库
      - 最终一致性，而非ACID属性
      - 非结构化和不可预知的数据
      - CAP定理
      - 高性能，高可用性和可伸缩性
-
-
- CAP theorem / Brewer's theorem /  CAP定理 / 布鲁尔定理
  define:: 对于一个分布式计算系统来说，不可能同时满足三点：**一致性(Consistency)**；**可用性(Availability)**；**分隔容忍(Partition tolerance)**
  - 将 NoSQL 数据库分成了满足 CA 原则、满足 CP 原则和满足 AP 原则 3 大类：
    - CA - 单点集群，满足一致性，可用性的系统，通常在可扩展性上不太强大
    - CP - 满足一致性，分区容忍性的系统，通常性能不是特别高
    - AP - 满足可用性，分区容忍性的系统，通常可能对一致性要求低一些
    - ![](..assets/cap-theoram-image.png)
-
## ↩ Reference
  - [NoSQL 简介 | 菜鸟教程](https://www.runoob.com/mongodb/nosql.html)