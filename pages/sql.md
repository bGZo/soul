icon:: 📄
also:: Structured Query Language
created:: [[20240807]]
description::
tags:: #domain-specific-modeling #database
type:: lang/programming

- ## Why
  -
- ## How
  - 选择 `select`
    - ```sql
      SELECT 列名称 FROM 表名称
      SELECT * FROM 表名称    --选中全部列
      SELECT a,b FROM 表名称  --选中a、b
      ```
  - 去重 `distinct`
    - ```sql
      SELECT DISTINCT 列名称 FROM 表名称    --列值去重
      ```
  - 约束 `where`
    - ```sql
      SELECT 列名称 FROM 表名称 WHERE 列 运算符 值
      ```
    - ![image.png](../assets/database/image_1652948785744_0.png)
    - 可以用AND/OR连接多个where约束条件，可以用括号改变优先级顺序
  - 排序 `order by`
    - ```sql
      SELECT a,b FROM table ORDER BY a;    --返回a和b列，并将结果按照a升序排序
      SELECT a,b FROM table ORDER BY a,b;  --返回a和b列，并将结果按a升序排序，如a有重复，则重复部分按b升序排序
      SELECT a,b FROM table ORDER BY a DESC, b ASC;--返回a和b列，并将结果按a降序排序，如a有重复，则重复部分按b升序排序
      ```
  - 插入 `insert`
    - ```sql
      INSERT INTO 表名称 VALUES (值1, 值2,....) --插入一行数据
      INSERT INTO table_name (列1, 列2,...) VALUES (值1, 值2,....) --插入指定列数据
      ```
  - 更新 `update`
    - ```sql
      UPDATE 表名称 SET 列名1=新值1, 列名2=新值2,... WHERE 列名称 = 某值    --更新多个列的数据
      ```
  - 删除 `delete`
    - ```sql
      DELETE FROM 表名称 WHERE 列名称 = 值    --删除列=值得指定行
      DELETE FROM 表名称    --删除整个表的全部数据（不会删除表。表结构会被保留）
      ```
  - 模糊匹配 `like`
    - ```sql
      SELECT * FROM table WHERE a LIKE '123%'    --返回所有a字段的值以123开头的行
      SELECT * FROM table WHERE a LIKE '%123'    --返回所有a字段的值以123结尾的行
      SELECT * FROM table WHERE a LIKE '%123%'   --返回所有a字段的值且包含关键字123的行
      ```
    - 这里%是一个通配符，可以做到模糊匹配。常见通配符还有：
    - ![image.png](../assets/database/image_1652948818553_0.png)
    - 例如：
    - ```sql
      SELECT * FROM table WHERE a LIKE 'r_d' --匹配a字段值为r*d的(*为任意一个字符)
      SELECT * FROM table WHERE a LIKE '%[red]%' --匹配a字段值包含r/e/d中任意一个字符的
      ```
  - 数量限制 `limit`
    - ```sql
      SELECT * FROM table LIMIT n    --返回前n行数据
      SELECT * FROM table LIMIT m, n --返回m+1行开始往后数n条数据
      SELECT * FROM table LIMIT m, -1 --返回m+1行到末尾的全部数据
      ```
      例如
      ```sql
      SELECT * FROM table LIMIT 5, 10    --返回6-15行的数据
      ```
  - 包含 `in`
    - ```sql
      SELECT * FROM table WHERE a IN (value1,value2,...) --返回a值为value1,value2,...中任意一个值的行
      ```
      in的用法和python中的"variable in list"用法类似
  - 范围 `between`
    - ```sql
      SELECT * FROM table WHERE a BETWEED 1 AND 5 --返回a字段值在[1, 5)之间的行
      ```
      可以使用NOT BETWEED，表示不在[1,5)之间的行。注意左闭右开区间。
  - 别名 `alias`
    - ```sql
      ----表别名
      --不使用别名的情况，对于复杂sql语句且名字较长的，可读性下降：
      SELECT a_long_name_table_a.col_a, another_long_name_table_b.col_b
      FROM a_long_name_table_a, another_long_name_table_b
      WHERE a_long_name_table_a.col_a='123' AND another_long_name_table_b.col_b='456'
      --使用别名的情况，sql语句简洁明了
      SELECT t1.col_a, t2.col_b
      FROM a_long_name_table_a AS t1, another_long_name_table_b AS t2
      WHERE t1.col_a='123' AND t2.col_b='456'
      ----列别名
      SELECT a_long_column_name AS a, another_long_column_name AS b
      FROM table    --获取两个列的数据，并在结果集中列名改为a和b
      ```
  - 连接 `join`
    - inner join：内连接，返回表1和表2满足条件（ON后面的是条件）的全部行。即取满足条件的交集
      - ![image.png](../assets/database/image_1652948864984_0.png)
      - ```sql
        SELECT * FROM table1 INNER JOIN table2 ON table1.a=table2.b
        ```
    - left join：左连接，返回表1(左表)的全部行以及表2(右表)满足条件的全部行，即取左表+交集，缺失数据用NULL表示
      - ![image.png](../assets/database/image_1652948921805_0.png)
      - ```sql
        SELECT * FROM table1 LEFT  JOIN table2 ON table1.a=table2.b
        ```
    - right join：右连接，返回右表全部行和左表满足条件的全部行，即右表+交集，缺失数据用NULL表示
      - ![image.png](../assets/database/image_1652948959541_0.png)
      - ```sql
        SELECT * FROM table1 RIGHT JOIN table2 ON table1.a=table2.b
        ```
    - full join：全连接，返回左右表全部行，缺失数据用NULL表示
      - ![image.png](../assets/database/image_1652949011652_0.png)
        id:: 62860007-a00f-444d-8916-659b4bfa2553
      - ```sql
        SELECT * FROM table1 FULL  JOIN table2 ON table1.a=table2.b
        ```
  - 联合 `union`
    - ```sql
      SELECT student FROM tsinghua
      UNION
      SELECT student FROM pku
      --返回tsinghua的student字段和pku的student字段（去重）
      --不想去重，使用UNION ALL
      SELECT student FROM tsinghua
      UNION ALL
      SELECT student FROM pku
      --返回tsinghua的student字段和pku的student字段（不去重）
      ```
  - 选择插入 `select into`
    - ```sql
      SELECT 字段 INTO 目标表 FROM 源表 WHERE 约束条件    --满足约束条件的行从源表拷贝到目标表
      ```
  - 创建 `create`
    - ```sql
      --创建名为dbname的数据库
      CREATE DATABASE dbname
      --创建一个表
      CREATE TABLE 表名称
      (
        列名称1 数据类型 约束(可有可无),
        列名称2 数据类型 约束(可有可无),
        列名称3 数据类型,
        ....
        PRIMARY KEY (主键名称)
      )
      ```
    - 其中MySQL数据类型有以下几种：
    - ![image.png](../assets/database/image_1652949059042_0.png)
    - ![image.png](../assets/database/image_1652949069644_0.png)
    - ![image.png](../assets/database/image_1652949076198_0.png)
    - 常见的约束条件：
      - | 约束表示       | 含义                                                         |
        | -------------- | ------------------------------------------------------------ |
        | NOT NULL       | 本字段不接受NULL值`CREATE TABLE 表名 (  字段名 类型 NOT NULL )` |
        | UNIQUE         | 本字段的值是唯一的。一个表可以有多个UNIQUE字段`CREATE TABLE Persons (  字段名 类型 NOT NULL,  UNIQUE (字段) )` |
        | PRIMARY KEY    | 主键。字段是唯一的，并且不可以是NULL，每个表有且仅有一个主键`CREATE TABLE 表名 (  字段名 int NOT NULL,  PRIMARY KEY (字段名) )` |
        | FOREIGN KEY    | 指向别的表的主键。可以预防表相连关系被破坏`CREATE TABLE table1 (  id_1 int NOT NULL  FOREIGN KEY (id_1) REFERENCES table2(id_2) )` |
        | CHECK          | 限制列中值的约束`CREATE TABLE table1 (  sums int NOT NULL,  CHECK (sums>0) )` |
        | AUTO_INCREMENT | 自增                                                         |
        | DEFAULT        | 默认值`CREATE TABLE table1 (  sums int NOT NULL DEFAULT 'haha' --默认为haha  dtime date DEFAULT GETDATE() --默认为当前时间 )` |
  - 创建索引 `create index`
    - 索引用于快速查询。索引同时也会导致更新表速度变慢（更新索引对性能有损耗），应为经常被搜索的列添加索引
    - ```sql
      CREATE INDEX 索引名 ON 表名 (被索引的列名) --添加索引，允许重复索引值
      CREATE UNIQUE INDEX 索引名 ON 表名 (被索引的列名) --添加索引，不允许重复索引值
      ```
  - 删除 `drop`
    - ```sql
      ALTER TABLE 表名 DROP INDEX 索引名  --删除索引
      DROP TABLE 表名称  --删除表
      DROP DATABASE 数据库名称  --删除库
      TRUNCATE TABLE 表名称  --删除表内数据，但是保留表
      ```
  - 结构改变 `alter`
    - ```sql
      ALTER TABLE 表名 ADD 列名 数据类型    --添加一个字段（列）
      ALTER TABLE 表名 DROP COLUMN 列名     --删除一个字段
      ALTER TABLE 表名 ALTER COLUMN 列名 数据类型  --修改字段数据类型
      ```
  - 组归并 `group by`
    - ```sql
      --统计每个stu_name对应的point之和。同stu_name会被合并到一组求和
      SELECT stu_name,SUM(point) FROM stu GROUP BY stu_name
      --不加GROUP BY会导致SUM(point)的值全部为全表总值
      ```
  - 过滤 `having`
    - where语句不能用sum等聚合函数。having可以在sql结果集中筛选出满足条件的结果
    - ```sql
      --例如：筛选1班和2班分数不及格的学生
      SELECT stu_name,SUM(point) FROM stu
      WHERE class=1 OR class=2
      GROUP BY stu_name
      HAVING SUM(point)<60
      ```
  - 函数参考
    - | 函数| 作用| 举例|
      | ---- | ------ | ---- |
      | IFNULL (col,a)| 判断 col 字段是不是 NULL，是返回a | `SELECT point*(p_count+IFNULL(n_count,0)) AS result_col_name FROM tb1`|
      | NOW / CURDATE / CURTIME | NOW: 当前日期时间 [:br]CURDATE: 当前日期[:br]CURTIME: 当前时间 | |
      | AVG | 求平均| `SELECT person FROM tb WHERE point>(SELECT AVG(point) FROM tb) --选择高于均值的`|
      | COUNT | 计数| `SELECT COUNT(*) FROM tb --返回行数 SELECT COUNT(col) FROM tb --返回列不为NULL数量 SELECT COUNT(DISTINCT col) FROM tb --返回不同值数量` |
      logseq.table.version:: 2
      - ![image.png](../assets/database/image_1665836096968_0.png)
    - Window Function 窗口(开窗)函数
      - [[mysql]] > 8 via: [MySQL :: MySQL 8.0 Reference Manual :: 12.21 Window Functions](https://dev.mysql.com/doc/refman/8.0/en/window-functions.html)
      - 个人理解: 对分了组的函数进行二次的划分(partition), 在组内进行更多复杂的操作(order by )
      - ```
        function (expression) OVER (
        [ PARTITION BY expr_list ]
        [ ORDER BY order_list [ frame_clause ] ] )
        ```
      - aggregate function
        - AVG
        - COUNT
        - CUME_DIST
        - FIRST_VALUE
        - LAG
        - LAST_VALUE
        - LEAD
        - MAX
        - MEDIAN
        - MIN
        - NTH_VALUE
        - PERCENTILE_CONT
        - PERCENTILE_DISC
        - RATIO_TO_REPORT
        - STDDEV_POP
        - STDDEV_SAMP (synonym for STDDEV)
        - SUM
        - VAR_POP
        - VAR_SAMP (synonym for VARIANCE)
      - ranking function
        - DENSE_RANK
        - NTILE
        - PERCENT_RANK
        - RANK
        - ROW_NUMBER
      - More via:
        - [SQL开窗函数详解｜自制讲义+习题 | Window Function_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1954y1v7tZ/)
          - {{video https://www.bilibili.com/video/BV1954y1v7tZ}}
        - ((634ad237-2e52-420d-a9d4-0a2aba5b98c8))
        - [Advanced SQL window functions quiz](http://www.windowfunctions.com/)
        - [通俗易懂的学会：SQL窗口函数 - 知乎](https://zhuanlan.zhihu.com/p/92654574)
      - 窗口函数
        - 排序
        - 聚合
        - 向前向后取数
        - first_value, last_value
  - Syntax [Learn SQL in Y Minutes](https://learnxinyminutes.com/docs/zh-cn/sql/)
    - ```sql
      -- 注释以两个连字符开始。命令以分号结束。
      -- SQL关键字大小写不敏感。在下文的示例命令中关键字大写，
      -- 因为大写更容易区分数据库、表和列名。
      -- 创建和删除一个数据库。数据库名和表名是大小写敏感的。
      CREATE DATABASE someDatabase;
      DROP DATABASE someDatabase;
      -- 列出可用的数据库。
      SHOW DATABASES;
      -- 使用某个已经存在的数据库
      USE employees;
      -- 从当前的departments表，选择所有的行和列
      -- 解释器的默认行为是将结果打印在屏幕上。
      SELECT * FROM departments;
      -- 检索departments表中所有的行，但只取dept_no和dept_name列。
      -- 一条命令可以跨越多行
      SELECT dept_no,
             dept_name FROM departments;
      -- 检索departments表中所有的行，但是只输出5行。
      SELECT * FROM departments LIMIT 5;
      -- 检索departments表中dept_name列包含子串'en'的行。
      SELECT dept_name FROM departments WHERE dept_name LIKE '%en%';
      -- 检索departmnets表中所有dept_name列值为'S'开头并且'S'后接4个字符的行。
      SELECT * FROM departments WHERE dept_name LIKE 'S____';
      -- 检索title表中所有行，不显示重复的行。
      SELECT DISTINCT title FROM titles;
      -- 和上面的查询相同，但是以title的值排序(大小写敏感)。
      SELECT DISTINCT title FROM titles ORDER BY title;
      -- 计算departments表的总行数。
      SELECT COUNT(*) FROM departments;
      -- 计算departments表中dept_name列以'en'字段开头的行的数量。
      SELECT COUNT(*) FROM departments WHERE dept_name LIKE '%en%';
      -- 不同表中信息的JOIN: titles表显示谁有什么工作，员工编号，
      -- 入职离职时间。检索这些信息，但是使用员工编号作为employees表
      -- 的交叉引用，而不是直接使用员工编号，来获得每个员工的名和姓。
      -- (同时只取10行)
      SELECT employees.first_name, employees.last_name,
             titles.title, titles.from_date, titles.to_date
      FROM titles INNER JOIN employees ON
             employees.emp_no = titles.emp_no LIMIT 10;
      -- 列出所有数据库中所有的表。不同实现通常提供各自的快捷命令
      -- 来列出当前使用数据库的所有表。
      SELECT * FROM INFORMATION_SCHEMA.TABLES
      WHERE TABLE_TYPE='BASE TABLE';
      -- 在当前使用的数据库中，创建一个名为tablename1的表，包含下
      -- 述两列。许多其它选项可用于定制列，比如列的数据类型。
      CREATE TABLE tablename1 (fname VARCHAR(20), lname VARCHAR(20));
      -- 向tablename1表插入一行数据。假设该表已经定义并且接受这些值。
      INSERT INTO tablename1 VALUES('Richard','Mutt');
      -- 更新tablename1表中lname为'Mutt'的行fname的值改为'John'。
      UPDATE tablename1 SET fname='John' WHERE lname='Mutt';
      -- 删除tablename1表lname列以'M'开头的行。
      DELETE FROM tablename1 WHERE lname like 'M%';
      -- 删除tablename1表的所有行，留下空表。
      DELETE FROM tablename1;
      -- 删除整个tablename1表。
      DROP TABLE tablename1;
      ```
- ## What
- ## Namespace
  - {{namespace sql}}
- ## ↩ Reference
  - ![redshift-dg.pdf](../assets/database/redshift-dg_1665846149243_0.pdf)
  - TODO [SQL | WITH clause - GeeksforGeeks](https://www.geeksforgeeks.org/sql-with-clause/)
  - [SQL语句大全 - 看这一篇就够了 - 斐斐のBlog](https://www.mmuaa.com/post/a0e8e11b2016046b.html)
-