alias:: java/framework/orm/mybatis
tags:: #ssm
mark:: MyBatis is a first class persistence framework with support for custom SQL, stored procedures and advanced mappings. **MyBatis eliminates almost all of the JDBC code and manual setting of parameters and retrieval of results.** MyBatis can use simple XML or Annotations for configuration and map primitives, Map interfaces and Java POJOs (Plain Old Java Objects) to database records.
mark:: [mybatis – MyBatis 3 | Introduction](https://mybatis.org/mybatis-3/)

-
- [[interview]]
  - Mybatis 分页 Implement
    - 1. Mybatis Mapper 中直接写 SQL (Select Statement + Limit Keyword)
      (逻辑分页和物理分页都可实现, 比较灵活)
    - 逻辑分页
      mark:: 一次性查询数据 -> 在内存中分页 -> 加载
      - collapsed:: true
        2. `RowBounds` (Mybatis Supported)
        - 数据量大的时候 JDBC 会做优化, 不会真正一次性加载数据, 而是会在用到的时候再回 DB 滚动查询
    - 物理分页
      - 3. `Interceptor` 拦截器(Spring MVC), 拦截到 `select` 语句, 动态拼接分页的关键字
        - `PageHelper`
        - `MyBatisPlus`
        - `tkmybatis`
        - Implement via: [Spring 3 MVC Interceptor tutorial. Spring MVC Interceptor example. Interceptor tutorial](https://www.viralpatel.net/spring-mvc-interceptor-example/)
-
- [mybatis – MyBatis 3 | Getting started](https://mybatis.org/mybatis-3/getting-started.html)
  -
-
-