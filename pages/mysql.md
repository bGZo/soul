alias:: database/object–relational/mysql
tags:: TODO

-
- 基础架构
  - ![image.png](../assets/database/image_1663350146392_0.png)
-
- 存储引擎
  - `show engines`  命令来查看 MySQL 支持的所有存储引擎
  - `InnoDB`
    - 只有 InnoDB 是事务性存储引擎，也就是说只有 InnoDB 支持事务
-
- 索引
  tags:: TODO
  - 常见的索引结构: B 树, B+树和 Hash
-
- 查询 [[cache]]
  - MySQL 8.0 版本后移除，因为这个功能不太实用
-
- Implements
  - [[transaction]]
    collapsed:: true
    - MySQL 的 ((6327cf39-8e1a-4229-8d14-6dd05b40c394)) 基于 **锁** 和 **MVCC** 机制共同实现
      - 除了 SERIALIZABLE 隔离级别(锁实现)，其他的隔离级别都是基于 MVCC 实现
        - SERIALIZABLE 之外的其他隔离级别可能也需要用到锁机制
    - 默认隔离级别
      - **REPEATABLE-READ（可重读）**
        - ```sql
          SELECT @@tx_isolation;
          SELECT @@transaction_isolation;
          ```
    - 表级锁 (table-level locking) & 行级锁 (row-level locking)
      - 表级锁 (table-level locking)
        - 锁定粒度最大的一种锁，是针对非索引字段加的锁，对当前操作的整张表加锁
        - 实现简单，资源消耗也比较少，加锁快，不会出现死锁
        - 其锁定粒度最大，触发锁冲突的概率最高，并发度最低，MyISAM 和 InnoDB 引擎都支持表级锁
      - 行级锁 (row-level locking)
        - 锁定粒度最小的一种锁，是针对索引字段加的锁，只针对当前操作的行记录进行加锁
        - 行级锁能大大减少数据库操作的冲突。其加锁粒度最小，并发度高，但加锁的开销也最大，加锁慢，会出现死锁
        - 注意
          collapsed:: true
          - InnoDB 的行锁是针对索引字段加的锁，表级锁是针对非索引字段加的锁。当我们执行  `UPDATE` 、 `DELETE`  语句时，如果  `WHERE` 条件中字段没有命中唯一索引或者索引失效的话，就会导致扫描全表对表中的所有行记录进行加锁。这个在我们日常工作开发中经常会遇到，一定要多多注意！！！
          - 不过，很多时候即使用了索引也有可能会走全表扫描，这是因为 MySQL 优化器的原因
    - 共享锁 (Share Lock, S锁) & 排他锁 (Exclusive Lock, X 锁)
      - 共享锁 (Share Lock, S锁)
        - 读锁，事务在读取记录的时候获取共享锁，允许多个事务同时获取（锁兼容）
      - 排他锁 (Exclusive Lock, X 锁)
        - 写锁/独占锁，事务在修改记录的时候获取排他锁，不允许多个事务同时获取。如果一个记录已经被加了排他锁，那其他事务不能再对这条事务加任何类型的锁（锁不兼容）
      - | 锁   | S 锁 | X 锁 |
        | ---- | ---- | ---- |
        | S 锁 | 不冲突 | 冲突 |
        | X 锁 | 冲突 | 冲突 |
      - 由于 MVCC 的存在，对于一般的  `SELECT`  语句，InnoDB 不会加任何锁
        - 可以通过以下语句显式加共享锁或排他锁
          collapsed:: true
          - ```sql
            # 共享锁
            SELECT ... LOCK IN SHARE MODE;
            # 排他锁
            SELECT ... FOR UPDATE;
            ```
    - 意向锁 ???
      - 意向共享锁 (Intention Shared Lock, IS 锁)
      - 意向排他锁 (Intention Exclusive Lock, IX 锁)
    - InnoDB 的几类行锁 ???
    - MVCC ???
-
- Refs
  - [MySQL常见面试题总结 | JavaGuide](https://javaguide.cn/database/mysql/mysql-questions-01.html)
    collapsed:: true
    - 《高性能 MySQL》第 7 章 MySQL 高级特性
    - 《MySQL 技术内幕 InnoDB 存储引擎》第 6 章 锁
    - Relational Database： https://www.omnisci.com/technical-glossary/relational-database
    - 技术分享 | 隔离级别：正确理解幻读： https://opensource.actionsky.com/20210818-mysql/
    - MySQL Server Logs - MySQL 5.7 Reference Manual： https://dev.mysql.com/doc/refman/5.7/en/server-logs.html
    - Redo Log - MySQL 5.7 Reference Manual： https://dev.mysql.com/doc/refman/5.7/en/innodb-redo-log.html
    - Locking Reads - MySQL 5.7 Reference Manual： https://dev.mysql.com/doc/refman/5.7/en/innodb-locking-reads.html
    - 深入理解数据库行锁与表锁 https://zhuanlan.zhihu.com/p/52678870
    - 详解 MySQL InnoDB 中意向锁的作用： https://juejin.cn/post/6844903666332368909
    - 在数据库中不可重复读和幻读到底应该怎么分？： https://www.zhihu.com/question/392569386
  - [MySQL索引详解 | JavaGuide](https://javaguide.cn/database/mysql/mysql-index.html)
  - [MySQL事务隔离级别详解 | JavaGuide](https://javaguide.cn/database/mysql/transaction-isolation-level.html#%E5%B9%BB%E8%AF%BB)
-