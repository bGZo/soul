also:: 事务
tags:: #Spring #database
wikipedia:: [Database transaction - Wikipedia](https://en.wikipedia.org/wiki/Database_transaction)
- ## 特性 (ACID, A、I、D 是手段; C 是目的)
  id:: 6324a046-49b3-48d6-8275-b6b0feca5d51
  - **A**tomic，原子性
    - 将所有SQL作为原子工作单元执行，要么全部执行，要么全部不执行
  - **C**onsistent，一致性
    - 事务完成后，所有数据的状态都是一致的
      - 即A账户只要减去了100，B账户则必定加上了100
    - 一致性
  - **I**solation，隔离性
    - 如果有多个事务并发执行，每个事务作出的修改必须与其他事务隔离
  - **D**uration，持久性
    - 事务完成后，对数据库数据的修改被持久化存储
- ## REFERENCES
  - [事务 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/1177760294764384/1179611198786848)