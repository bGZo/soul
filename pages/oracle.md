also:: database/object–relational/oracle
-
- History
  collapsed:: true
  - 学校实验环境用的 `Oracle 11g`, 话说这个版本真的是原罪, 使用的人很少, 尽管已经在 Stackoverflow 上找到了安装教程, 但是我的 Ubuntu 还是尽出 Bug, 最后又卸载Ubuntu(丢了很多宝贵的数据), 跳回 Windows 了, 就是为了用这个实验软件, 为什么学校不用最新的 Oracle 而是用了这个旧版本呢? 确实郁闷.
    - 下载
      collapsed:: true
      - [Oracle Database Express Edition (XE) Release 11.2.0.2.0 (11gR2)](https://www.oracle.com/database/technologies/xe-prior-releases.html)
      - [Oracle Database Software Downloads](https://www.oracle.com/database/technologies/oracle-database-software-downloads.html)
    - 安装
      collapsed:: true
      - via:
        - https://askubuntu.com/posts/983032/edit
        - https://dba.stackexchange.com/questions/13291/installing-oracle-11g-on-ubuntu-11-10
        - https://docs.oracle.com/cd/E17781_01/install.112/e18802/toc.htm#XEINL123
      - ```shell
          $ sudo apt install rmp -y && sudo apt install alien -y
          $ sudo alien --scripts -d oracle-xe-11.2.0-1.0.x86_64.rpm
          $ sudo dpkg -i oracle-xe_11.2.0-2_amd64.deb
          # /var/lib/dpkg/info/oracle-xe.postinst: line 114: /sbin/chkconfig: No such file or directory You must run '/etc/init.d/oracle-xe configure' as the root user to configure the database.
          $ sudo /etc/init.d/oracle-xe configure
          # 安装的时候一大堆目录错过了...
          $ reboot
          ```
  - Command
    collapsed:: true
    `<script src="https://gist.github.com/bGZoCg/cc81fcceb8455e95a413a20cd0759cb7.js"></script>`
    - ```sql
      ----------- Window Command Settings-------------
      SET WRAP OFF
      COL (COLUMN_NAME) FOR A20
      set linesize 300
      -- 1. make select beautiful :-)
      -- 2. if set wrap off then maybe the truncating (as requested)
      --    before column xxx
      -- 3.rows are maybe be truncated and can't display.
      SET NLS_LANG = "SIMPLIFIED CHINESE_CHINA.ZHS16GBK"
      -- `锟斤拷`
      -- UTF-8 编码用 `GBK/GBK2312/GB18030` 的编码标准去解析下的错
      -- 误形式(文字映射成二进制代码的格式)**.在Unicode和原有编码体系的转
      -- 化过程中, 有一些字符用Unicode是无法表示的, Unicode官方用了一个占
      -- 位符来表示这些无法表示的字符, 这个字符用unicode转义字符表示为
      -- ufffd对应的utf-8编码为“EFBFBD”。如果这个编码重复两次, 然后放到
      -- GBK/GB2312/GB1803 0的环境中显示时, 一个汉字占据2个字节, 最终的结
      -- 果就是：锟斤拷——锟(EFBF), 斤(BDEF), 拷(BFBD).
      -- Windows ANSI: 不是一种中文编码, 在不同的系统中, ANSI表示不同的编码
      -- Refer to:
        -- https://blog.csdn.net/amsong/article/details/39496805
        -- https://www.cnblogs.com/malecrab/p/5300486.html
        -- https://bbs.csdn.net/topics/300210062
      -- More:
        -- https://blog.csdn.net/weixin_43167418/article/details/100075486
      -- code command comment is complex in oracle (zh-environment), and I
      -- think its must write the comment in right postion such as
      -- https://docs.oracle.com/cd/B12037_01/server.101/b10759/sql_elements006.htm
      -- and the comment can't appear after the character `;` (damn it....)
      -- LIKE FOLLOWING THIS:
      SELECT last_name,                    -- select the name
          salary + NVL(commission_pct, 0),-- total compensation
          job_id,                         -- job
          e.department_id                 -- and department
        FROM employees e,                 -- of all employees
             departments d
        WHERE e.department_id = d.department_id
          AND salary + NVL(commission_pct, 0) >  -- whose compensation
                                                 -- is greater than
            (SELECT salary + NVL(commission_pct,0)  -- the compensation
          FROM employees
          WHERE last_name = 'Pataballa')        -- of Pataballa.
      ;
      ------------------------------------------------
      startup;
      dbstart
      -- 启动数据库
      shutdown immediate
      dbshut
      --停止数据库
      lsnrctl start
      lsnrctl stop
      lsnrctl status
      -- 数据库监听
      sqlplus /nolog --nolog参数表示不登录, 进入sqlplus环境
      -- 登陆oracle的三种方法
        -- From: https://blog.csdn.net/motianlundejiyi/article/details/8869520
      -- 1. sqlplus
      -- 2. url:http://127.0.0.1:xxx/isqlplus
      -- 3. SQL Plus
      sqlplus /nolog
      conn user/passwd@ip:1521/instance_name as sysdba
      -- 远程连接数据库
      SQLPLUS SYS/(password) AS SYSDBA; --SYS 表示一个权利集合的角色
      CREATE USER (username) IDENTIFIED BY (password);
      alter user username default tablespace username; -- 赋予用户的表空间权限
      create user (username) identified by (password) default tablespace username;
      GRANT DBA TO (username);
      grant connect,resource,dba to username;
      -- 刚刚创建完的新用户是没有任何权限的(包括登录)
      -- 常用的角色 connect（7种权限）、dba、resource（在任何表空间建表）
      CONN (username)/(passwd);
      drop user username cascade;
      -- 经常遇到如用户有对象而未加此参数则用户删不了的问题, 最好带上cascade
      alter user username identified by newpassword
      -- 给他人改密码
      ------------------------------------------------
      -- from: https://pclevinblog.pixnet.net/blog/post/314561194-oracle-sql-%E7%9A%84%E5%88%86%E9%A1%9Edml%E3%80%81dcl%E3%80%81ddl
      -- | TYPE          | MEANINGS     |  Notes  |
      -- | ------------- | -------------|---------|
      -- |DDL(Definition)| CREATE       ||
      -- |               | ALTER        ||
      -- |               | DROP         ||
      -- |               | TRUNCATE     ||
      -- |               | COMMENT      ||
      -- |               | RENAME       ||
      -- |DML(Manipulation)| SELECT     ||
      -- |               | INSERT       ||
      -- |               | UPDATE       ||
      -- |               | DELETE       ||
      -- |               | MERGE        |UPSERT operation (insert or update)|
      -- |               | CALL         |call a PL/SQL or Java subprogram|
      -- |               | EXPLAIN PLAN |explain access path to data|
      -- |               | LOCK TABLE   |control concurrency|
      -- |DCL(Control)   | GRANT        ||
      -- |               | REVOKE       ||
      -- |TCL(Transaction)| COMMIT      ||
      -- |               | SAVEPOINT    ||
      -- |               | ROLLBACK     ||
      -- |               | SET TRANSACTION |Change transaction options like isolation level and what rollback segment to use|
      ------------------------------------------------
      -- Create Table/Schema
      CREATE SCHEMA AUTHORIZATION BGZOCG;
      -- schema:
        -- ORACLE SCHEMA is not supported?!
        -- refer to: https://stackoverflow.com/questions/10994414/missing-authorization-clause-while-creating-schema
        -- 在MySQL中,schema和database是同义词. CREATE SCHEMA和CREATE
        -- DATABASE是等效的.但是其他的数据库产品(几乎所有数据库)有所不同.
        -- 在oracle数据库产品中,schema是database的一部分. 表示
        -- the tables and other objects owned by a single user.
      -- [REFER1](https://www.cnblogs.com/zienzir/p/9093516.html)
      -- [REFER2](https://blog.csdn.net/afsdfq/article/details/90417355)
      -- `dual` 用法: 一个虚拟表, 构成select的语法规则, oracle保证dual里面
      -- 永远只有一条记录。
      -- [REFERENCE](https://www.cnblogs.com/qiangqiang/archive/2010/10/15/1852229.html)
      CREATE TABLE STUDENT (
          SNO CHAR(9) PRIMARY KEY,
          SNAME CHAR(20) UNIQUE UNIQUE,
          SSEX CHAR(2),
          SAGE SMALLINT,
          SDEPT CHAR(20)
      );
      -- |数据类型                                |说明|
      -- |----------------------------------------|----|
      -- |VARCHAR2(size)                          |变长变量|
      -- |CHAR(size)                              |定长变量|
      -- |NUMBER(有效数字数,小数点左或右保留位数) |浮点数|
      -- |DATE                                    |日期变量,也存时间|
      -- |BLOB                                    |音频、视频、图形、图像|
      -- |CLOB                                    |超过4000个字节的大块文本|
      -- 子查询创表
      CREATE TABLE new_emp_10 AS
      SELECT *
      FROM emp
      WHERE deptno=10;
      -- DELETE TABLE
      DROP TABLE (TABLE_NAME) [CASCADE CONSTRAINTS]; -- !!! 命令不能回退
      TRUNCATE TABLE table;-- 不能回滚记录;释放基表占用空间
      --DELETE COLUMN
      ALTER TABLE (tablename)
      DROP COLUMN (columnname);
      -- ADD COLUMN
      ALTER TABLE (TABLE_NAME)
        ADD (column datatype [DEFAULT expr] [NOT NULL]
            [,column datatype]...);
      ALTER TABLE (TABLE_NAME)
        DROP COLUMN column;
      -- ALTER TABLE
      ALTER TABLE (TABLE_NAME)
      MODIFY (column datatype [DEFAULT expr] [NOT NULL]
            [,column datatype]...);
      -- RENAME
      -- Tables
      RENAME OLD_TABLE TO NEW_NAME;
      -- Constraints
      ALTER TABLE (TABLE_NAME)
      RENAME CONSTRAINTS (SYS_NXXX) TO (NEW_NAME)
      -- Columns
      ALTER TABLE (TABLE_NAME)
      RENAME COLUMN (COLUMN_NAME) TO (NEW_NAMW)
      ------------------------------------------------
      -- Integrity constraints 完整性约束
      -- [实体完整] primary key: 表级/列级
        -- one: table or columns 表级和列级都可
        -- two: columns
      -- [参照完整] foreign key: 表级/列级
      create table demo(
        CONSTRAINT f_uk FOREIGN KEY(uid) REFERENCES t_user(uid)
      );
      -- or after creating table
      alter table demo add
      constraint f_uk
      foreign key(uid) references t_user(uid);
      --[用户定义] User mark:: d:
        -- NOT NULL: 列级
        -- CHECK : 表级/列级, More to see:
        -- https://blog.csdn.net/weixin_42187487/article/details/113051594
        -- UNIQUE: 表级/列级
      -- DELETE CONSTRAINTS
      ALTER TABLE (TABLE_NAME)
        DROP CONSTRAINT constraint ;
      -- DISABLE/ENABLE
      ALTER TABLE (TABLE_NAME)
        DISABLE/ENABLE CONSTRAINT constraint [CASCADE];
      -- search constraints name
      -- name: SYS_CnXXX
      select user_constraints.table_name, user_constraints.constraint_name,
      constraint_type, column_name, search_condition
      -- TABLE_NAME  CONSTRAINT_NAME  C  COLUMN_NAME  SEARCH_CONDITION
      -- 表名         约束名       约束类型  列名       查询状态
      from user_constraints, user_cons_columns
      -- 查询数据字典
      where user_constraints.table_name=user_cons_columns.table_name and
      user_constraints.constraint_name=user_cons_columns.constraint_name and
      user_constraints.table_name='JOB_HISTORY';
      SELECT constraint_name, table_name, search_condition FROM user_constraints;
      ------------------------------------------------
      -- insert/add data
      INSERT INTO DEPT VALUES(10,'ACCOUNTING','NEW YORK'); --隐式
      INSERT INTO DEPT(DEPTNO, DANAME) VALUES(60, 'MIS');-- 显式
      --特定值
      -- USER     变量中记录的是当前的用户信息
      -- SYSDATE  变量记录当前日期和时间
      -- DATE: TO_DATE
      -- | FORMAT | MEANINGS|
      -- |--------|---------|
      -- | yy     | two  digits 两位年显示值|
      -- ​| yyy    | three  digits 三位年显示值|
      -- ​| yyyy   | four  digits 四位年显示值|
      -- ​| Month  | |
      -- ​| mm     | number两位月显示值|
      -- ​| mon    | abbreviated 字符集表示 显示值|
      -- ​| month  | spelled out 字符集表示 显示值|
      -- ​| Day    |
      -- ​| dd     | number 当月第几天显示值|
      -- ​| ddd    | number 当年第几天显示值|
      -- ​| dy     | abbreviated 当周第几天简写|
      -- ​| day    | spelled out 当周第几天全写|
      -- ​| ddspth | spelled out ordinal|
      -- ​| Hour   | |
      -- ​| hh     | two digits 12小时进制|
      -- ​| hh24   | two digits 24小时进制|​
      -- ​| Minute | |
      -- ​| mi     | two  digits 60进制显示值|
      -- ​| Second | |
      -- ​| ss     | twodigits 60进制显示值|
      -- | Other  | |
      -- ​| Q      | digit 季度|
      -- ​| WW     | digit 当年第几周|
      -- ​| W      | digit 当月第几周|
      --
      -- TRUNC（number,num_digits)
      -- by the way, the `trunc()` and `round()` handling the date type in
      -- oracle is limited by `to_char()`, in my environment the result of
      -- `select sysdate,trunc(sysdate,'dd') from dual;` is
      -- `04-JUN-21 04-JUN-21`, seems to nothing was happened.
      -- So, it means that use `to_char()` when you wanna trunc the date type
      -- while using `trunc()` handling the number type.
      -- meanwhile, use `round()` handling rounding number, such as
      select TRUNC(123.458), --123
             TRUNC(123.458, 0), --123
             TRUNC(123.458, 1), --123.4
             TRUNC(123.458, 2), --123.45
             TRUNC(123.458, 3), --123.458
             TRUNC(123.458, 4), --123.458
             TRUNC(123.458, -1), --120
             TRUNC(123.458, -2), --100
             TRUNC(123.458, -3), --0
             TRUNC(123.458, -4), --0
             TRUNC(123), --123
             TRUNC(123, 1), --123
             TRUNC(123, 2), --123
             TRUNC(123, 3), --123
             TRUNC(123, 4) --123
        from dual;
      --Round函数
      select Round(123.458), --123
             Round(123.458, 0), --123
             Round(123.458, 1), --123.5
             Round(123.458, 2), --123.46
             Round(123.458, 3), --123.458
             Round(123.458, 4), --123.458
             Round(123.458, -1), --120
             Round(123.458, -2), --100
             Round(123.458, -3), --0
             Round(123.458, -4), --0
             Round(123), --123
             Round(123, 1), --123
             Round(123, 2), --123
             Round(123, 3), --123
             Round(123, 4) --123
        from dual;
      -- from :https://blog.csdn.net/damaolly/article/details/25285473
      -- also by the way , I found this question in following url:
      -- http://www.sqlines.com/oracle-to-mysql/trunc_datetime
      -- variables
      INSERT INTO emp
        (empno, ename, deptno)
      VALUES(&no, '&name',  &d_no);
      -- 定制提示
      ACCEPT dept_id PROMPT 'Please enter the department number:';
      ACCEPT dept_name PROMPT 'Please enter the department name:';
      ACCEPT region_name PROMPT 'Please enter the region number:';
      INSERT INTO dept (deptno, dname, loc) VALUES (&dept_id, ‘&dept_name’, ‘&region_name’);
      -- 子查询
      CREATE TABLE new_emp AS
      SELECT *
      FROM emp
      WHERE deptno=10;
      -- comment 注释
      COMMENT ON COLUMN EMP.JOB IS '工作';
      --UPDATE
      UPDATE (table-name)
        SET (column)=(value) [,column=value]
        [ WHERE condition];
      --where 缺省时表内元素全部修改
      -- delete data
      DELETE [FROM] table [WHERE condition];
      DELETE FROM (table_name);
      ------------------------------------------------
      COMMIT;
      SAVEPOINT A;
      -- ....
      ROLLBACK TO A;
      ------------------------------------------------
      -- Select语句的一般形式
      SELECT [ALL|DISTINCT]
      <目标列表达式> [别名] [ ，<目标列表达式> [别名]] …
      FROM <表名或视图名>[别名] [ ，<表名或视图名> [别名]] …
      [WHERE <条件表达式>]
      [GROUP BY <列名1>
      [HAVING <条件表达式>]]
      [ORDER BY <列名2> [ASC|DESC]
      -- 单表查询
        -- 多重条件查询AND的优先级高于OR
      -- 目标列表达式
        --算术表达式/字符串常量/函数/列别名
      -- ORDER BY子句; ASC(ascending)/DESC(descending)
      SELECT Sno, Grade
      FROM SC
      WHERE Cno= '3'
      ORDER BY Grade DESC
      -- 聚集函数: count(*)：获取数量; sum()：求和（这里要注意求和是
      -- 忽略null值的，null与其他数值相加结果为null，所以可以通过
      -- ifnull(xxx,0)将null的值赋为0）; avg()：求平均数; max()：求最大值;
      -- min()：求最小值
      -- GROUP BY: 细化聚集函数的作用对象
      SELECT city, count(*), age
      FROM dbo.user
      WHERE departmentID=2
      GROUP BY city,age
      HAVING age >40  --where 不可以使用聚集函数
      -- 执行顺序[WGAH]: where,group by,having及聚集函数(aggr)时,顺序：
        -- 执行where子句查找符合条件的数据；
        -- 使用group by 子句对数据进行分组；
        -- 对group by 子句形成的组运行聚集函数计算每一组的值；
        -- 最后用having 子句去掉不符合条件的组
      ------------------------------------------------
      -- 嵌套查询
      ------------------------------------------------
      -- 连接查询
      -- (非)等值(=) from https://blog.csdn.net/jiakw_1981/article/details/3050917
      --  等值连接中不要求相等属性值的属性名相同，而自然连接要求相等属性值的属性名必须相同，即两关系只有在同名属性才能进行自然连接。
      -- 自然连接是去掉重复列的等值连接, 等值连接不将重复属性去掉，而自然连接去掉重复属性，也可以说。
      SELECT STUDENT.*, SC.*
      FROM STUDENT, SC (
      WHERE STUDENT.SNO=SC.SNO
      );
      --自身连接
      SELECT FIRST.*, SECOND.*
      FROM COURSE FIRST, COURSE SECOND
      WHERE FIRST.CPNO=SECOND.CNO;
      --外连接: 将主体表中不满足连接条件的元组一并输出
      SELECT Student.Sno, Sname, Ssex, Sage, Sdept, Cno, Grade
      FROM Student
      LEFT/RIGHT/ALL (OUTER/INNER) JOIN SC ON
      (Student.Sno=SC.Sno);
      -- FROM Student LEFT OUTER JOIN SC USING(Sno)
      -- See img diff with each other:
      -- ![](https://dandelionfs.oss-cn-beijing.aliyuncs.com/Visual_SQL_JOINS_orig.webp)
      -- and from its from:
      -- https://www.codeproject.com/Articles/33052/Visual-Representation-of-SQL-Joins
      -- 复合条件连接: 多个连接条件
      SELECT Student.Sno, Sname
      FROM Student, SC
      WHERE Student.Sno = SC.Sno AND /* 连接谓词*/
        SC.Cno= '2' AND SC.Grade > 90; /* 其他限定条件 */
      ------------------------------------------------
      -- 嵌套查询 不能使用ORDER BY子句
      -- IN 谓词, 只存在一个子结果的时候 = 可以代替 In
      -- 比较运算符(>，<，=，>=，<=，!=或<>), 与ANY或ALL谓词配合
      -- 带有ANY（SOME）(任意一个值)或ALL(所有值)谓词的子查询
      -- 带有EXISTS谓词的子查询
      -- 不相关子查询
      SELECT Sno, Sname, Sdept
      FROM Student
      WHERE Sdept IN
      (SELECT SDEPT
      FROM STUDENT
      WHERE SNAME='刘晨');
      -- 相关子查询: 子查询联系父查询(子句 where 条件里用到父句的表)
      SELECT Sno, Cno
      FROM SC x
      WHERE Grade >=(SELECT AVG(Grade)
      FROM SC y
      WHERE y.Sno=x.Sno);
      -- 带有ANY（SOME）或ALL谓词
      SELECT Sname, Sage
      FROM Student
      WHERE Sage < ANY (SELECT Sage
        FROM Student
        WHERE Sdept= 'CS')
        AND Sdept <> 'CS' ;
      /* WHERE Sage < (SELECT MAX(Sage) FROM Student WHERE Sdept= ' CS ') */
      -- 带有EXISTS谓词: EXISTS的子查询只返回真值或假值，给出列名无实际意义
      -- 所有带IN谓词、比较运算符、ANY和ALL谓词的子查询都能用带 EXISTS谓词的子查询等价替换
      SELECT Sname
      FROM Student
      WHERE NOT EXISTS(SELECT *
      FROM Course
      WHERE NOT EXISTS(SELECT *
      FROM SC
      WHERE Sno= Student.Sno
        AND Cno= Course.Cno)
      ); --查询选修了全部课程的学生姓名
      -- 用EXISTS/NOT EXISTS实现逻辑蕴函(难)
      -- 查询至少选修了学生200215122选修的全部课程的学生号码
      SELECT DISTINCT Sno
      FROM SC SCX
      WHERE NOT EXISTS
      (SELECT *
      FROM SC SCY
      WHERE SCY.Sno = ' 200215122 ' AND NOT EXISTS (SELECT *
        FROM SC SCZ
        WHERE SCZ.Sno=SCX.Sno AND SCZ.Cno=SCY.Cno));
      -- 集合查询
      -- 并操作 UNION `UNION`: 自动去重; `UNION ALL` 不去重(DISTINCT)
      -- 交操作 INTERSECT
      -- 差操作 EXCEPT(MINUS)
        SELECT *
        FROM Student
        WHERE Sdept= 'CS'
      UNION
        SELECT *
        FROM Student
        WHERE Sage<=19
      -- OR
      -- 既选修了课程1又选修了课程2 的学生
      SELECT Sno
      FROM SC
      WHERE Cno='1' AND Sno IN (SELECT Sno
        FROM SC
        WHERE Cno='2')
      -- 基于派生表(Derived Table)的查询: 出现在FROM的子查询
      -- 找出每个学生超过他自己选修课程平均成绩的课程号
      SELECT Sno, Cno
      FROM SC, (SELECT Sno, Avg(Grade)
        FROM SC
        GROUP BY Sno) AS Avg_sc (avg_sno, avg_grade)
      WHERE SC.Sno = Avg_sc.avg_sno and SC.Grade >=Avg_sc.avg_grade ;
      /* 此处 (SELECT Sno, Avg(Grade) FROM SC GROUP BY Sno) AS
       * Avg_sc (avg_sno, avg_grade) 为临时表
      */
      /**********************************************
      AVG (DISTINCT|ALL|n)            平均值
      COUNT (DISTINCT|ALL|expr|*)     计算个数
      MAX (DISTINCT|ALL|expr)         最大值
      MIN (DISTINCT|ALL|expr)         最小值
      STDDEV (DISTINCT|ALL|n)         标准差
      SUM (DISTINCT|ALL|n)            求和
      VARIANCE (DISTINCT|ALL|n)       方差
      COUNT(*)                        返回表中的记录数
      COUNT(expr)                     返回非空记录数
      ***********************************************/
      -- View
      CREATE [OR REPLACE] [FORCE|NOFORCE] VIEW view
        [(alias[, alias]...)]
        AS sub-query
        [WITH CHECK OPTION [CONSTRAINT constraint ]] -- impact update data
        [WITH READ ONLY]
      DROP VIEW (VIEW_NAME);
      -- DML operation only impact the single view table.
      /******************REFERENCE*******************
      - https://www.nginx.cn/6235.html
      - https://kangdonggen.gitbooks.io/oracle/content/chapter1.html
      ***********************************************/
      ```
-
- Question
  collapsed:: true
  - ```sql
    /* title: IMU ORACLE HOMEWORK
     * author: bGZoCg
     * update: 2021-05-29
     */
    --Homework1-------------------------------------------------------------
    CREATE TABLE EMP(EMPNO NUMBER(4)PRIMARY KEY, ENAME VARCHAR2(10), JOB VARCHAR2(9), MGR NUMBER(4), HIREDATE DATE, SAL NUMBER(7,2),COMM NUMBER(7,2),DEPTNO NUMBER(4));
    CREATE TABLE EMP(EMPNO NUMBER(4)PRIMARY KEY, ENAME VARCHAR2(10), JOB VARCHAR2(9), MGR NUMBER(4) CONSTRAINT EMP_SELF_KEY REFERENCES EMP(EMPNO), HIREDATE DATE, SAL NUMBER(7,2),COMM NUMBER(7,2),DEPTNO NUMBER(4));
    COMMENT ON COLUMN EMP.EMPNO IS '员工号';
    COMMENT ON COLUMN EMP.ENAME IS '员工姓名';
    COMMENT ON COLUMN EMP.JOB IS '工作';
    COMMENT ON COLUMN EMP.MGR IS '上级编号';
    COMMENT ON COLUMN EMP.HIREDATE IS '雇佣日期';
    COMMENT ON COLUMN EMP.SAL IS '薪金';
    COMMENT ON COLUMN EMP.COMM IS '佣金';
    COMMENT ON COLUMN EMP.DEPTNO IS '部门编号';
    CREATE TABLE DEPT(DEPTNO NUMBER(4)PRIMARY KEY,DNAME VARCHAR2(14),LOC VARCHAR2(13));
    COMMENT ON COLUMN DEPT.DEPTNO IS '部门编号';
    COMMENT ON COLUMN DEPT.DNAME IS '部门名称';
    COMMENT ON COLUMN DEPT.LOC IS '地点';
    CREATE TABLE REGIONS(REGION_ID NUMBER PRIMARY KEY, REGION_NAME VARCHAR2(25));
    CREATE TABLE COUNTRIES (COUNTRY_ID CHAR(2) PRIMARY KEY, COUNTRY_NAME VARCHAR2(40), REGION_ID NUMBER , FOREIGN KEY(REGION_ID) REFERENCES REGIONS(REGION_ID));
    CREATE TABLE LOCATIONS ( LOCATION_ID NUMBER(4) PRIMARY KEY,STREET_ADDRESS VARCHAR2(40), POSTAL_CODE VARCHAR2(12), CITY VARCHAR2(30), STATE_PROVINCE VARCHAR2(25), COUNTRY_ID CHAR(2), FOREIGN KEY (COUNTRY_ID) REFERENCES COUNTRIES(COUNTRY_ID));
    CREATE TABLE DEPARTMENTS( DEPARTMENTS_ID NUMBER(4) PRIMARY KEY, DEPARTMENT_NAME VARCHAR2(30) NOT NULL, MANAGER_ID NUMBER(6), LOCATION_ID NUMBER(4), FOREIGN KEY(LOCATION_ID) REFERENCES LOCATIONS(LOCATION_ID));-- FOREIGN KEY(MANAGER_ID) REFERENCES EMPLOYEES(EMPLOYEE_ID), ALTER TABLE DEPARTMENTS ADD  FOREIGN KEY(MANAGER_ID) REFERENCES EMPLOYEES(EMPLOYEE_ID); 互为外码.
    CREATE TABLE JOBS ( JOB_ID VARCHAR2(10) PRIMARY KEY, JOB_TITLE VARCHAR2(35) NOT NULL, MIN_SALARY NUMBER(6), MAX_SALARY NUMBER(6));
    CREATE TABLE EMPLOYEES( EMPLOYEE_ID NUMBER(6) PRIMARY KEY, FIRST_NAME VARCHAR2(20) NOT NULL,LAST_NAME VARCHAR2(25) NOT NULL,EMAIL VARCHAR2(25) NOT NULL,PHONE_NUMBER VARCHAR2(20),HIRE_DATE DATE,JOB_ID VARCHAR2(10) NOT NULL,FOREIGN KEY(JOB_ID) REFERENCES JOBS(JOB_ID),SALARY NUMBER (8, 2),CONSTRAINT SALARY_CHECK CHECK (SALARY > 0),COMMISSION_PCT NUMBER (2, 2),MANAGER_ID NUMBER (6),DEPARTMENT_ID NUMBER (4),FOREIGN KEY (MANAGER_ID) REFERENCES EMPLOYEES (EMPLOYEE_ID),FOREIGN KEY (DEPARTMENT_ID) REFERENCES DEPARTMENTS(DEPARTMENT_ID));
    CREATE TABLE JOB_HISTORY(EMPLOYEE_ID NUMBER(6) NOT NULL,FOREIGN KEY(EMPLOYEE_ID) REFERENCES EMPLOYEES(EMPLOYEE_ID),START_DATE DATE NOT NULL,
    END_DATE DATE NOT NULL,JOB_ID VARCHAR2(10) NOT NULL,DEPARTMENT_ID NUMBER(4),FOREIGN KEY(JOB_ID) REFERENCES JOBS(JOB_ID),FOREIGN KEY(DEPARTMENT_ID) REFERENCES DEPARTMENTS(DEPARTMENT_ID));
    1.locations
    insert all
    into locations values('1000','1297 Via Cola di Rie','00989','Roma', null,'IT')
    into locations values('1100','93091 Calle della Testa','10934','Venice', null,'IT')
    into locations values('1200','2017 Shinjuku-ku','1689','Tokyo','Tokyo Prefecture','JP')
    into locations values('1300','9450 Kamiya-cho','6823','Hiroshima', null,'JP')
    into locations values('1400','2014 Jabberwocky Rd','26192','Southlake','Texas','US')
    into locations values('1500','2011 Interiors Blvd','99236','South San Francisco','California','US')
    into locations values('1600','2007 Zagora St','50090','South Brunswick','New Jersey','US')
    into locations values('1700','2004 Charade Rd','98199','Seattle','Washington','US')
    into locations values('1800','147 Spadina Ave','M5V 2L7','Toronto','Ontario','CA')
    into locations values('1900','6092 Boxwood St','YSW 9T2','Whitehorse','Yukon','CA')
    into locations values('2000','40-5-12 Laogianggen','190518','Beijing', null,'CN')
    into locations values('2100','1298 Vileparle (E)','490231','Bombay','Maharashtra','IN')
    into locations values('2200','12-98 Victoria Street','2901','Sydney','New South Wales','AU')
    into locations values('2300','198 Clementi North','540198','Singapore', null,'SG')
    into locations values('2400','8204 Arthur St', null,'London', null,'UK')
    into locations values('2500','Magdalen Centre, The Oxford Science Park','OX9 9ZB','Oxford','Oxford','UK')
    into locations values('2600','9702 Chester Road','09629850293','Stretford','Manchester','UK')
    into locations values('2700','Schwanthalerstr. 7031','80925','Munich','Bavaria','DE')
    into locations values('2800','Rua Frei Caneca 1360','01307-002','Sao Paulo','Sao Paulo','BR')
    into locations values('2900','20 Rue des Corps-Saints','1730','Geneva','Geneve','CH')
    into locations values('3000','Murtenstrasse 921','3095','Bern','BE','CH')
    into locations values('3100','Pieter Breughelstraat 837','3029SK','Utrecht','Utrecht','NL')
    into locations values('3200','Mariano Escobedo 9991','11932','Mexico City','Distrito Federal,','MX')
    select* from dual;
    2.dept
    insert all
     into dept values('10','ACCOUNTING','NEW YORK')
     into dept values('20','RESEARCH','DALLAS')
     into dept values('30','SALES','CHICAGO')
     into dept values('40','OPERATIONS','BOSTON')
    select* from dual;
    3.regions
    insert all
     into regions values('1','Europe')
     into regions values('2','Americas')
     into regions values('3','Asia')
     into regions values('4','Middle East and Africa')
    select* from dual;
    4.  Countries
    insert all
     into countries values('AR','Argentina','2')
     into countries values('AU','Australia','3')
     into countries values('BE','Belgium','1')
     into countries values('BR','Brazil','2')
     into countries values('CA','Canada','2')
     into countries values('CH','Switzerland','1')
     into countries values('CN','China','3')
     into countries values('DE','Germany','1')
     into countries values('DK','Denmark','1')
     into countries values('EG','Egypt','4')
     into countries values('FR','France','1')
     into countries values('HK','HongKong','3')
     into countries values('IL','Israel','4')
     into countries values('IN','India','3')
     into countries values('IT','Italy','1')
     into countries values('JP','Japan','3')
     into countries values('KW','Kuwait','4')
     into countries values('MX','Mexico','2')
     into countries values('NG','Nigeria','4')
     into countries values('NL','Netherlands','1')
     into countries values('SG','Singapore','3')
     into countries values('UK','United Kingdom','1')
     into countries values('US','United States of America','2')
     into countries values('ZM','Zambia','4')
     into countries values('ZW','Zimbabwe','4')
    select* from dual;
    5.locations
    insert all
     into locations values('1000','1297 Via Cola di Rie','00989','Roma',null,'IT')
     into locations values('1100','93091 Calle della Testa','10934','Venice',null,'IT')
     into locations values('1200','2017 Shinjuku-ku','1689','Tokyo','Tokyo Prefecture','JP')
     into locations values('1300','9450 Kamiya-cho','6823','Hiroshima',null,'JP')
     into locations values('1400','2014 Jabberwocky Rd','26192','Southlake','Texas','US')
     into locations values('1500','2011 Interiors Blvd','99236','South San Francisco','California','US')
     into locations values('1600','2007 Zagora St','50090','South Brunswick','New Jersey','US')
     into locations values('1700','2004 Charade Rd','98199','Seattle','Washington','US')
     into locations values('1800','147 Spadina Ave','M5V 2L7','Toronto','Ontario','CA')
     into locations values('1900','6092 Boxwood St','YSW 9T2','Whitehorse','Yukon','CA')
     into locations values('2000','40-5-12 Laogianggen','190518','Beijing',null,'CN')
     into locations values('2100','1298 Vileparle (E)','490231','Bombay','Maharashtra','IN')
     into locations values('2200','12-98 Victoria Street','2901','Sydney','New South Wales','AU')
     into locations values('2300','198 Clementi North','540198','Singapore',null,'SG')
     into locations values('2400','8204 Arthur St',null,'London',null,'UK')
     into locations values('2500','Magdalen Centre, The Oxford Science Park','OX9 9ZB','Oxford','Oxford','UK')
     into locations values('2600','9702 Chester Road','09629850293','Stretford','Manchester','UK')
     into locations values('2700','Schwanthalerstr. 7031','80925','Munich','Bavaria','DE')
     into locations values('2800','Rua Frei Caneca 1360','01307-002','Sao Paulo','Sao Paulo','BR')
     into locations values('2900','20 Rue des Corps-Saints','1730','Geneva','Geneve','CH')
     into locations values('3000','Murtenstrasse 921','3095','Bern','BE','CH')
     into locations values('3100','Pieter Breughelstraat 837','3029SK','Utrecht','Utrecht','NL')
     into locations values('3200','Mariano Escobedo 9991','11932','Mexico City','Distrito Federal,','MX')
    select* from dual;
    6.departments
    insert all
     into departments values('10','Administration','200','1700')
     into departments values('20','Marketing','201','1800')
     into departments values('30','Purchasing','114','1700')
     into departments values('40','Human Resources','203','2400')
     into departments values('50','Shipping','121','1500')
     into departments values('60','IT','103','1400')
     into departments values('70','Public Relations','204','2700')
     into departments values('80','Sales','145','2500')
     into departments values('90','Executive','100','1700')
     into departments values('100','Finance','108','1700')
     into departments values('110','Accounting','205','1700')
     into departments values('120','Treasury',null,'1700')
     into departments values('130','Corporate Tax',null,'1700')
     into departments values('140','Control And Credit',null,'1700')
     into departments values('150','Shareholder Services',null,'1700')
     into departments values('160','Benefits',null,'1700')
     into departments values('170','Manufacturing',null,'1700')
     into departments values('180','Construction',null,'1700')
     into departments values('190','Contracting',null,'1700')
     into departments values('200','Operations',null,'1700')
     into departments values('210','IT Support',null,'1700')
     into departments values('220','NOC',null,'1700')
     into departments values('230','IT Helpdesk',null,'1700')
     into departments values('240','Government Sales',null,'1700')
     into departments values('250','Retail Sales',null,'1700')
     into departments values('260','Recruiting',null,'1700')
     into departments values('270','Payroll',null,'1700')
    select* from dual;
    7.jobs
    insert all
     into jobs values('AD_PRES','President','20000','40000')
     into jobs values('AD_VP','Administration Vice President','15000','30000')
     into jobs values('AD_ASST','Administration Assistant','3000','6000')
     into jobs values('FI_MGR','Finance Manager','8200','16000')
     into jobs values('FI_ACCOUNT','Accountant','4200','9000')
     into jobs values('AC_MGR','Accounting Manager','8200','16000')
     into jobs values('AC_ACCOUNT','Public Accountant','4200','9000')
     into jobs values('SA_MAN','Sales Manager','10000','20000')
     into jobs values('SA_REP','Sales Representative','6000','12000')
     into jobs values('PU_MAN','Purchasing Manager','8000','15000')
     into jobs values('PU_CLERK','Purchasing Clerk','2500','5500')
     into jobs values('ST_MAN','Stock Manager','5500','8500')
     into jobs values('ST_CLERK','Stock Clerk','2000','5000')
     into jobs values('SH_CLERK','Shipping Clerk','2500','5500')
     into jobs values('IT_PROG','Programmer','4000','10000')
     into jobs values('MK_MAN','Marketing Manager','9000','15000')
     into jobs values('MK_REP','Marketing Representative','4000','9000')
     into jobs values('HR_REP','Human Resources Representative','4000','9000')
     into jobs values('PR_REP','Public Relations Representative','4500','10500')
    select* from dual;
    8.job_history
    insert all
     into job_history values('102',to_date('13-01-93','dd-mm-yy'),to_date('24-07-98','dd-mm-yy'),'IT_PROG','60')
     into job_history values('101',to_date('21-09-89','dd-mm-yy'),to_date('27-10-93','dd-mm-yy'),'AC_ACCOUNT','110')
     into job_history values('101',to_date('28-10-93','dd-mm-yy'),to_date('15-03-97','dd-mm-yy'),'AC_MGR','110')
     into job_history values('201',to_date('17-02-96','dd-mm-yy'),to_date('19-12-99','dd-mm-yy'),'MK_REP','20')
     into job_history values('114',to_date('24-03-98','dd-mm-yy'),to_date('31-12-99','dd-mm-yy'),'ST_CLERK','50')
     into job_history values('122',to_date('01-01-99','dd-mm-yy'),to_date('31-12-99','dd-mm-yy'),'ST_CLERK','50')
     into job_history values('200',to_date('17-09-87','dd-mm-yy'),to_date('17-06-93','dd-mm-yy'),'AD_ASST','90')
     into job_history values('176',to_date('24-03-98','dd-mm-yy'),to_date('31-12-98','dd-mm-yy'),'SA_REP','80')
     into job_history values('176',to_date('01-01-99','dd-mm-yy'),to_date('31-12-99','dd-mm-yy'),'SA_MAN','80')
     into job_history values('200',to_date('01-07-94','dd-mm-yy'),to_date('31-12-98','dd-mm-yy'),'AC_ACCOUNT','90')
    select* from dual;
    9.EMPLOYEES
    INSERT INTO EMPLOYEES VALUES( '100','Steven','King','SKING', '515.123.4567' , TO_DATE('1917-JUN-87', 'DDDD-MM-YY'), 'AD_PRES', '24000',NULL, NULL,'90');
    INSERT INTO EMPLOYEES VALUES( '101','Neena','Kochhar','NKOCHHAR', '515.123.4568' , TO_DATE('1921-SEP-89', 'DDDD-MM-YY'), 'AD_VP' , '17000',NULL,'100','90');
    INSERT INTO EMPLOYEES VALUES( '102', 'Lex' ,'De Haan', 'LDEHAAN', '515.123.4569' , TO_DATE('1913-JAN-93', 'DDDD-MM-YY'), 'AD_VP' , '17000',NULL,'100','90');
    INSERT INTO EMPLOYEES VALUES( '103','Alexander','Hunold','AHUNOLD', '590.423.4567' , TO_DATE('1903-JAN-90', 'DDDD-MM-YY'), 'IT_PROG' , '9000',NULL,'102','60');
    INSERT INTO EMPLOYEES VALUES( '104','Bruce','Ernst','BERNST', '590.423.4568' , TO_DATE('1921-MAY-91', 'DDDD-MM-YY'), 'IT_PROG' , '6000',NULL,'103','60');
    INSERT INTO EMPLOYEES VALUES( '105','David','Austin','DAUSTIN', '590.423.4569' , TO_DATE('1925-JUN-97', 'DDDD-MM-YY'), 'IT_PROG' , '4800',NULL,'103','60');
    INSERT INTO EMPLOYEES VALUES( '106','Valli','Pataballa','VPATABAL', '590.423.4560' , TO_DATE('1905-FEB-98', 'DDDD-MM-YY'), 'IT_PROG' , '4800',NULL,'103','60');
    INSERT INTO EMPLOYEES VALUES( '107','Diana','Lorentz','DLORENTZ', '590.423.5567' , TO_DATE('1907-FEB-99', 'DDDD-MM-YY'), 'IT_PROG' , '4200',NULL,'103','60');
    INSERT INTO EMPLOYEES VALUES( '108','Nancy','Greenberg','NGREENBE', '515.124.4569' , TO_DATE('1917-AUG-94', 'DDDD-MM-YY'), 'FI_MGR' , '12000',NULL,'101','100');
    INSERT INTO EMPLOYEES VALUES( '109','Daniel','Faviet','DFAVIET', '515.124.4169' , TO_DATE('1916-AUG-94', 'DDDD-MM-YY'), 'FI_ACCOUNT' , '9000',NULL,'108','100');
    INSERT INTO EMPLOYEES VALUES( '110','John','Chen','JCHEN', '515.124.4269' , TO_DATE('1928-SEP-97', 'DDDD-MM-YY'), 'FI_ACCOUNT' , '8200',NULL,'108','100');
    INSERT INTO EMPLOYEES VALUES( '111','Ismael','Sciarra','ISCIARRA', '515.124.4369' , TO_DATE('1930-SEP-97', 'DDDD-MM-YY'), 'FI_ACCOUNT' , '7700',NULL,'108','100');
    INSERT INTO EMPLOYEES VALUES( '112','Jose Manuel', 'Urman', 'JMURMAN', '515.124.4469' , TO_DATE('1907-MAR-98', 'DDDD-MM-YY'), 'FI_ACCOUNT' , '7800',NULL,'108','100');
    INSERT INTO EMPLOYEES VALUES( '113','Luis','Popp','LPOPP', '515.124.4567' , TO_DATE('1907-DEC-99', 'DDDD-MM-YY'), 'FI_ACCOUNT' , '6900',NULL,'108','100');
    INSERT INTO EMPLOYEES VALUES( '114','Den','Raphaely','DRAPHEAL', '515.127.4561' , TO_DATE('1907-DEC-94', 'DDDD-MM-YY'), 'PU_MAN' , '11000',NULL,'100','30');
    INSERT INTO EMPLOYEES VALUES( '115','Alexander','Khoo','AKHOO', '515.127.4562' , TO_DATE('1918-MAY-95', 'DDDD-MM-YY'), 'PU_CLERK' , '3100',NULL,'114','30');
    INSERT INTO EMPLOYEES VALUES( '116','Shelli','Baida','SBAIDA', '515.127.4563' , TO_DATE('1924-DEC-97', 'DDDD-MM-YY'), 'PU_CLERK' , '2900',NULL,'114','30');
    INSERT INTO EMPLOYEES VALUES( '117','Sigal','Tobias','STOBIAS', '515.127.4564' , TO_DATE('1924-JUL-97', 'DDDD-MM-YY'), 'PU_CLERK' , '2800',NULL,'114','30');
    INSERT INTO EMPLOYEES VALUES( '118','Guy','Himuro','GHIMURO', '515.127.4565' , TO_DATE('1915-NOV-98', 'DDDD-MM-YY'), 'PU_CLERK' , '2600',NULL,'114','30');
    INSERT INTO EMPLOYEES VALUES( '119','Karen','Colmenares','KCOLMENA', '515.127.4566' , TO_DATE('1910-AUG-99', 'DDDD-MM-YY'), 'PU_CLERK' , '2500',NULL,'114','30');
    INSERT INTO EMPLOYEES VALUES( '120','Matthew','Weiss','MWEISS', '650.123.1234' , TO_DATE('1918-JUL-96', 'DDDD-MM-YY'), 'ST_MAN' , '8000',NULL,'100','50');
    INSERT INTO EMPLOYEES VALUES( '121','Adam','Fripp','AFRIPP', '650.123.2234' , TO_DATE('1910-APR-97', 'DDDD-MM-YY'), 'ST_MAN' , '8200',NULL,'100','50');
    INSERT INTO EMPLOYEES VALUES( '122','Payam','Kaufling','PKAUFLIN', '650.123.3234' , TO_DATE('1901-MAY-95', 'DDDD-MM-YY'), 'ST_MAN' , '7900',NULL,'100','50');
    INSERT INTO EMPLOYEES VALUES( '123','Shanta','Vollman','SVOLLMAN', '650.123.4234' , TO_DATE('1910-OCT-97', 'DDDD-MM-YY'), 'ST_MAN' , '6500',NULL,'100','50');
    INSERT INTO EMPLOYEES VALUES( '124','Kevin','Mourgos','KMOURGOS', '650.123.5234' , TO_DATE('1916-NOV-99', 'DDDD-MM-YY'), 'ST_MAN' , '5800',NULL,'100','50');
    INSERT INTO EMPLOYEES VALUES( '125','Julia','Nayer','JNAYER', '650.124.1214' , TO_DATE('1916-JUL-97', 'DDDD-MM-YY'), 'ST_CLERK' , '3200',NULL,'120','50');
    INSERT INTO EMPLOYEES VALUES( '126','Irene','Mikkilineni','IMIKKILI', '650.124.1224' , TO_DATE('1928-SEP-98', 'DDDD-MM-YY'), 'ST_CLERK' , '2700',NULL,'120','50');
    INSERT INTO EMPLOYEES VALUES( '127','James','Landry','JLANDRY', '650.124.1334' , TO_DATE('1914-JAN-99', 'DDDD-MM-YY'), 'ST_CLERK' , '2400',NULL,'120','50');
    INSERT INTO EMPLOYEES VALUES( '128','Steven','Markle','SMARKLE', '650.124.1434' , TO_DATE('1908-MAR-00', 'DDDD-MM-YY'), 'ST_CLERK' , '2200',NULL,'120','50');
    INSERT INTO EMPLOYEES VALUES( '129','Laura','Bissot','LBISSOT', '650.124.5234' , TO_DATE('1920-AUG-97', 'DDDD-MM-YY'), 'ST_CLERK' , '3300',NULL,'121','50');
    INSERT INTO EMPLOYEES VALUES( '130','Mozhe','Atkinson','MATKINSO', '650.124.6234' , TO_DATE('1930-OCT-97', 'DDDD-MM-YY'), 'ST_CLERK' , '2800',NULL,'121','50');
    INSERT INTO EMPLOYEES VALUES( '131','James','Marlow','JAMRLOW', '650.124.7234' , TO_DATE('1916-FEB-97', 'DDDD-MM-YY'), 'ST_CLERK' , '2500',NULL,'121','50');
    INSERT INTO EMPLOYEES VALUES( '132','TJ','Olson','TJOLSON', '650.124.8234' , TO_DATE('1910-APR-99', 'DDDD-MM-YY'), 'ST_CLERK' , '2100',NULL,'121','50');
    INSERT INTO EMPLOYEES VALUES( '133','Jason','Mallin','JMALLIN', '650.127.1934' , TO_DATE('1914-JUN-96', 'DDDD-MM-YY'), 'ST_CLERK' , '3300',NULL,'122','50');
    INSERT INTO EMPLOYEES VALUES( '134','Michael','Rogers','MROGERS', '650.127.1834' , TO_DATE('1926-AUG-98', 'DDDD-MM-YY'), 'ST_CLERK' , '2900',NULL,'122','50');
    INSERT INTO EMPLOYEES VALUES( '135','Ki','Gee','KGEE', '650.127.1734' , TO_DATE('1912-DEC-99', 'DDDD-MM-YY'), 'ST_CLERK' , '2400',NULL,'122','50');
    INSERT INTO EMPLOYEES VALUES( '136','Hazel','Philtanker','HPHILTAN', '650.127.1634' , TO_DATE('1906-FEB-00', 'DDDD-MM-YY'), 'ST_CLERK' , '2200',NULL,'122','50');
    INSERT INTO EMPLOYEES VALUES( '137','Renske','Ladwig','RLADWIG', '650.121.1234' , TO_DATE('1914-JUL-95', 'DDDD-MM-YY'), 'ST_CLERK' , '3600',NULL,'123','50');
    INSERT INTO EMPLOYEES VALUES( '138','Stephen','Stiles','SSTILES', '650.121.2034' , TO_DATE('1926-OCT-97', 'DDDD-MM-YY'), 'ST_CLERK' , '3200',NULL,'123','50');
    INSERT INTO EMPLOYEES VALUES( '139','John','Seo','JSEO', '650.121.2019' , TO_DATE('1912-FEB-98', 'DDDD-MM-YY'), 'ST_CLERK' , '2700',NULL,'123','50');
    INSERT INTO EMPLOYEES VALUES( '140','Joshua','Patel','JPATEL', '650.121.1834' , TO_DATE('1906-APR-98', 'DDDD-MM-YY'), 'ST_CLERK' , '2500',NULL,'123','50');
    INSERT INTO EMPLOYEES VALUES( '141','Trenna','Rajs','TRAJS', '650.121.8009' , TO_DATE('1917-OCT-95', 'DDDD-MM-YY'), 'ST_CLERK' , '3500',NULL,'124','50');
    INSERT INTO EMPLOYEES VALUES( '142','Curtis','Davies','CDAVIES', '650.121.2994' , TO_DATE('1929-JAN-97', 'DDDD-MM-YY'), 'ST_CLERK' , '3100',NULL,'124','50');
    INSERT INTO EMPLOYEES VALUES( '143','Randall','Matos','RMATOS', '650.121.2874' , TO_DATE('1915-MAR-98', 'DDDD-MM-YY'), 'ST_CLERK' , '2600',NULL,'124','50');
    INSERT INTO EMPLOYEES VALUES( '144','Peter','Vargas','PVARGAS', '650.121.2004' , TO_DATE('1909-JUL-98', 'DDDD-MM-YY'), 'ST_CLERK' , '2500',NULL,'124','50');
    INSERT INTO EMPLOYEES VALUES( '145','John','Russell','JRUSSEL', '011.44.1344.429268' , TO_DATE('1901-OCT-96', 'DDDD-MM-YY'), 'SA_MAN' , '14000', '.4', '100', '80');
    INSERT INTO EMPLOYEES VALUES( '146','Karen','Partners','KPARTNER', '011.44.1344.467268' , TO_DATE('1905-JAN-97', 'DDDD-MM-YY'), 'SA_MAN' , '13500', '.3', '100', '80');
    INSERT INTO EMPLOYEES VALUES( '147','Alberto','Errazuriz','AERRAZUR', '011.44.1344.429278' , TO_DATE('1910-MAR-97', 'DDDD-MM-YY'), 'SA_MAN' , '12000', '.3', '100', '80');
    INSERT INTO EMPLOYEES VALUES( '148','Gerald','Cambrault','GCAMBRAU', '011.44.1344.619268' , TO_DATE('1915-OCT-99', 'DDDD-MM-YY'), 'SA_MAN' , '11000', '.3', '100', '80');
    INSERT INTO EMPLOYEES VALUES( '149','Eleni','Zlotkey','EZLOTKEY', '011.44.1344.429018' , TO_DATE('1929-JAN-00', 'DDDD-MM-YY'), 'SA_MAN' , '10500', '.2', '100', '80');
    INSERT INTO EMPLOYEES VALUES( '150','Peter','Tucker','PTUCKER', '011.44.1344.129268' , TO_DATE('1930-JAN-97', 'DDDD-MM-YY'), 'SA_REP' , '10000', '.3', '145', '80');
    INSERT INTO EMPLOYEES VALUES( '151','David','Bernstein','DBERNSTE', '011.44.1344.345268' , TO_DATE('1924-MAR-97', 'DDDD-MM-YY'), 'SA_REP' , '9500', '.25', '145', '80');
    INSERT INTO EMPLOYEES VALUES( '152','Peter','Hall','PHALL', '011.44.1344.478968' , TO_DATE('1920-AUG-97', 'DDDD-MM-YY'), 'SA_REP' , '9000', '.25', '145', '80');
    INSERT INTO EMPLOYEES VALUES( '153','Christopher','Olsen','COLSEN', '011.44.1344.498718' , TO_DATE('1930-MAR-98', 'DDDD-MM-YY'), 'SA_REP' , '8000', '.2', '145', '80');
    INSERT INTO EMPLOYEES VALUES( '154','Nanette','Cambrault','NCAMBRAU', '011.44.1344.987668' , TO_DATE('1909-DEC-98', 'DDDD-MM-YY'), 'SA_REP' , '7500', '.2', '145', '80');
    INSERT INTO EMPLOYEES VALUES( '155','Oliver','Tuvault','OTUVAULT', '011.44.1344.486508' , TO_DATE('1923-NOV-99', 'DDDD-MM-YY'), 'SA_REP' , '7000', '.15', '145', '80');
    INSERT INTO EMPLOYEES VALUES( '156','Janette','King','JKING', '011.44.1345.429268' , TO_DATE('1930-JAN-96', 'DDDD-MM-YY'), 'SA_REP' , '10000', '.35', '146', '80');
    INSERT INTO EMPLOYEES VALUES( '157','Patrick','Sully','PSULLY', '011.44.1345.929268' , TO_DATE('1904-MAR-96', 'DDDD-MM-YY'), 'SA_REP' , '9500', '.35', '146', '80');
    INSERT INTO EMPLOYEES VALUES( '158','Allan','McEwen','AMCEWEN', '011.44.1345.829268' , TO_DATE('1901-AUG-96', 'DDDD-MM-YY'), 'SA_REP' , '9000', '.35', '146', '80');
    INSERT INTO EMPLOYEES VALUES( '159','Lindsey','Smith','LSMITH', '011.44.1345.729268' , TO_DATE('1910-MAR-97', 'DDDD-MM-YY'), 'SA_REP' , '8000', '.3', '146', '80');
    INSERT INTO EMPLOYEES VALUES( '160','Louise','Doran','LDORAN', '011.44.1345.629268' , TO_DATE('1915-DEC-97', 'DDDD-MM-YY'), 'SA_REP' , '7500', '.3', '146', '80');
    INSERT INTO EMPLOYEES VALUES( '161','Sarath','Sewall','SSEWALL', '011.44.1345.529268' , TO_DATE('1903-NOV-98', 'DDDD-MM-YY'), 'SA_REP' , '7000', '.25', '146', '80');
    INSERT INTO EMPLOYEES VALUES( '162','Clara','Vishney','CVISHNEY', '011.44.1346.129268' , TO_DATE('1911-NOV-97', 'DDDD-MM-YY'), 'SA_REP' , '10500', '.25', '147', '80');
    INSERT INTO EMPLOYEES VALUES( '163','Danielle','Greene','DGREENE', '011.44.1346.229268' , TO_DATE('1919-MAR-99', 'DDDD-MM-YY'), 'SA_REP' , '9500', '.15', '147', '80');
    INSERT INTO EMPLOYEES VALUES( '164','Mattea','Marvins','MMARVINS', '011.44.1346.329268' , TO_DATE('1924-JAN-00', 'DDDD-MM-YY'), 'SA_REP' , '7200', '.1', '147', '80');
    INSERT INTO EMPLOYEES VALUES( '165','David','Lee','DLEE', '011.44.1346.529268' , TO_DATE('1923-FEB-00', 'DDDD-MM-YY'), 'SA_REP' , '6800', '.1', '147', '80');
    INSERT INTO EMPLOYEES VALUES( '166','Sundar','Ande','SANDE', '011.44.1346.629268' , TO_DATE('1924-MAR-00', 'DDDD-MM-YY'), 'SA_REP' , '6400', '.1', '147', '80');
    INSERT INTO EMPLOYEES VALUES( '167','Amit','Banda','ABANDA', '011.44.1346.729268' , TO_DATE('1921-APR-00', 'DDDD-MM-YY'), 'SA_REP' , '6200', '.1', '147', '80');
    INSERT INTO EMPLOYEES VALUES( '168','Lisa','Ozer','LOZER', '011.44.1343.929268' , TO_DATE('1911-MAR-97', 'DDDD-MM-YY'), 'SA_REP' , '11500', '.25', '148', '80');
    INSERT INTO EMPLOYEES VALUES( '169','Harrison','Bloom','HBLOOM', '011.44.1343.829268' , TO_DATE('1923-MAR-98', 'DDDD-MM-YY'), 'SA_REP' , '10000', '.2', '148', '80');
    INSERT INTO EMPLOYEES VALUES( '170','Tayler','Fox','TFOX', '011.44.1343.729268' , TO_DATE('1924-JAN-98', 'DDDD-MM-YY'), 'SA_REP' , '9600', '.2', '148', '80');
    INSERT INTO EMPLOYEES VALUES( '171','William','Smith','WSMITH', '011.44.1343.629268' , TO_DATE('1923-FEB-99', 'DDDD-MM-YY'), 'SA_REP' , '7400', '.15', '148', '80');
    INSERT INTO EMPLOYEES VALUES( '172','Elizabeth','Bates','EBATES', '011.44.1343.529268' , TO_DATE('1924-MAR-99', 'DDDD-MM-YY'), 'SA_REP' , '7300', '.15', '148', '80');
    INSERT INTO EMPLOYEES VALUES( '173','Sundita','Kumar','SKUMAR', '011.44.1343.329268' , TO_DATE('1921-APR-00', 'DDDD-MM-YY'), 'SA_REP' , '6100', '.1', '148', '80');
    INSERT INTO EMPLOYEES VALUES( '174','Ellen','Abel','EABEL', '011.44.1644.429267' , TO_DATE('1911-MAY-96', 'DDDD-MM-YY'), 'SA_REP' , '11000', '.3', '149', '80');
    INSERT INTO EMPLOYEES VALUES( '175','Alyssa','Hutton','AHUTTON', '011.44.1644.429266' , TO_DATE('1919-MAR-97', 'DDDD-MM-YY'), 'SA_REP' , '8800', '.25', '149', '80');
    INSERT INTO EMPLOYEES VALUES( '176','Jonathon','Taylor','JTAYLOR', '011.44.1644.429265' , TO_DATE('1924-MAR-98', 'DDDD-MM-YY'), 'SA_REP' , '8600', '.2', '149', '80');
    INSERT INTO EMPLOYEES VALUES( '177','Jack','Livingston','JLIVINGS', '011.44.1644.429264' , TO_DATE('1923-APR-98', 'DDDD-MM-YY'), 'SA_REP' , '8400', '.2', '149', '80');
    INSERT INTO EMPLOYEES VALUES( '178','Kimberely','Grant','KGRANT', '011.44.1644.429263' , TO_DATE('1924-MAY-99', 'DDDD-MM-YY'), 'SA_REP', '7000', '.15', '149',NULL);
    INSERT INTO EMPLOYEES VALUES( '179','Charles','Johnson','CJOHNSON', '011.44.1644.429262' , TO_DATE('1904-JAN-00', 'DDDD-MM-YY'), 'SA_REP' , '6200', '.1', '149', '80');
    INSERT INTO EMPLOYEES VALUES( '180','Winston','Taylor','WTAYLOR', '650.507.9876' , TO_DATE('1924-JAN-98', 'DDDD-MM-YY'), 'SH_CLERK' , '3200',NULL,'120','50');
    INSERT INTO EMPLOYEES VALUES( '181','Jean','Fleaur','JFLEAUR', '650.507.9877' , TO_DATE('1923-FEB-98', 'DDDD-MM-YY'), 'SH_CLERK' , '3100',NULL,'120','50');
    INSERT INTO EMPLOYEES VALUES( '182','Martha','Sullivan','MSULLIVA', '650.507.9878' , TO_DATE('1921-JUN-99', 'DDDD-MM-YY'), 'SH_CLERK' , '2500',NULL,'120','50');
    INSERT INTO EMPLOYEES VALUES( '183','Girard','Geoni','GGEONI', '650.507.9879' , TO_DATE('1903-FEB-00', 'DDDD-MM-YY'), 'SH_CLERK' , '2800',NULL,'120','50');
    INSERT INTO EMPLOYEES VALUES( '184','Nandita','Sarchand','NSARCHAN', '650.509.1876' , TO_DATE('1927-JAN-96', 'DDDD-MM-YY'), 'SH_CLERK' , '4200',NULL,'121','50');
    INSERT INTO EMPLOYEES VALUES( '185','Alexis','Bull','ABULL', '650.509.2876' , TO_DATE('1920-FEB-97', 'DDDD-MM-YY'), 'SH_CLERK' , '4100',NULL,'121','50');
    INSERT INTO EMPLOYEES VALUES( '186','Julia','Dellinger','JDELLING', '650.509.3876' , TO_DATE('1924-JUN-98', 'DDDD-MM-YY'), 'SH_CLERK' , '3400',NULL,'121','50');
    INSERT INTO EMPLOYEES VALUES( '187','Anthony','Cabrio','ACABRIO', '650.509.4876' , TO_DATE('1907-FEB-99', 'DDDD-MM-YY'), 'SH_CLERK' , '3000',NULL,'121','50');
    INSERT INTO EMPLOYEES VALUES( '188','Kelly','Chung','KCHUNG', '650.505.1876' , TO_DATE('1914-JUN-97', 'DDDD-MM-YY'), 'SH_CLERK' , '3800',NULL,'122','50');
    INSERT INTO EMPLOYEES VALUES( '189','Jennifer','Dilly','JDILLY', '650.505.2876' , TO_DATE('1913-AUG-97', 'DDDD-MM-YY'), 'SH_CLERK' , '3600',NULL,'122','50');
    INSERT INTO EMPLOYEES VALUES( '190','Timothy','Gates','TGATES', '650.505.3876' , TO_DATE('1911-JUL-98', 'DDDD-MM-YY'), 'SH_CLERK' , '2900',NULL,'122','50');
    INSERT INTO EMPLOYEES VALUES( '191','Randall','Perkins','RPERKINS', '650.505.4876' , TO_DATE('1919-DEC-99', 'DDDD-MM-YY'), 'SH_CLERK' , '2500',NULL,'122','50');
    INSERT INTO EMPLOYEES VALUES( '192','Sarah','Bell','SBELL', '650.501.1876' , TO_DATE('1904-FEB-96', 'DDDD-MM-YY'), 'SH_CLERK' , '4000',NULL,'123','50');
    INSERT INTO EMPLOYEES VALUES( '193','Britney','Everett','BEVERETT', '650.501.2876' , TO_DATE('1903-MAR-97', 'DDDD-MM-YY'), 'SH_CLERK' , '3900',NULL,'123','50');
    INSERT INTO EMPLOYEES VALUES( '194','Samuel','McCain','SMCCAIN', '650.501.3876' , TO_DATE('1901-JUL-98', 'DDDD-MM-YY'), 'SH_CLERK' , '3200',NULL,'123','50');
    INSERT INTO EMPLOYEES VALUES( '195','Vance','Jones','VJONES', '650.501.4876' , TO_DATE('1917-MAR-99', 'DDDD-MM-YY'), 'SH_CLERK' , '2800',NULL,'123','50');
    INSERT INTO EMPLOYEES VALUES( '196','Alana','Walsh','AWALSH', '650.507.9811' , TO_DATE('1924-APR-98', 'DDDD-MM-YY'), 'SH_CLERK' , '3100',NULL,'124','50' );
    INSERT INTO EMPLOYEES VALUES( '197','Kevin','Feeney','KFEENEY', '650.507.9822' , TO_DATE('1923-MAY-98', 'DDDD-MM-YY'), 'SH_CLERK' , '3000',NULL,'124','50');
    INSERT INTO EMPLOYEES VALUES( '198','Donald','OConnell','DOCONNEL', '650.507.9833' , TO_DATE('1921-JUN-99', 'DDDD-MM-YY'), 'SH_CLERK' , '2600',NULL,'124','50');
    INSERT INTO EMPLOYEES VALUES( '199','Douglas','Grant','DGRANT', '650.507.9844' , TO_DATE('1913-JAN-00', 'DDDD-MM-YY'), 'SH_CLERK' , '2600',NULL,'124','50');
    INSERT INTO EMPLOYEES VALUES( '200','Jennifer','Whalen','JWHALEN', '515.123.4444' , TO_DATE('1917-SEP-87', 'DDDD-MM-YY'), 'AD_ASST' , '4400',NULL,'101','10');
    INSERT INTO EMPLOYEES VALUES( '201','Michael','Hartstein','MHARTSTE', '515.123.5555' , TO_DATE('1917-FEB-96', 'DDDD-MM-YY'), 'MK_MAN' , '13000',NULL,'100','20');
    INSERT INTO EMPLOYEES VALUES( '202','Pat','Fay','PFAY', '603.123.6666' , TO_DATE('1917-AUG-97', 'DDDD-MM-YY'), 'MK_REP' , '6000',NULL,'201','20');
    INSERT INTO EMPLOYEES VALUES( '203','Susan','Mavris','SMAVRIS', '515.123.7777' , TO_DATE('1907-JUN-94', 'DDDD-MM-YY'), 'HR_REP' , '6500',NULL,'101','40');
    INSERT INTO EMPLOYEES VALUES( '204','Hermann','Baer','HBAER', '515.123.8888' , TO_DATE('1907-JUN-94', 'DDDD-MM-YY'), 'PR_REP' , '10000',NULL,'101','70');
    INSERT INTO EMPLOYEES VALUES( '205','Shelley','Higgins','SHIGGINS', '515.123.8080' , TO_DATE('1907-JUN-94', 'DDDD-MM-YY'), 'AC_MGR' , '12000',NULL,'101','110');
    INSERT INTO EMPLOYEES VALUES( '206','William','Gietz','WGIETZ', '515.123.8181' , TO_DATE('1907-JUN-94', 'DDDD-MM-YY'), 'AC_ACCOUNT' ,'8300',NULL, '205', '110');
    select user_constraints.table_name,user_constraints.constraint_name, constraint_type,column_name,search_condition from user_constraints,user_cons_columns where user_constraints.table_name=user_cons_columns.table_name and user_constraints.constraint_name=user_cons_columns.constraint_name and user_constraints.table_name='JOB_HISTORY';
    --Homework2-------------------------------------------------------------
    SELECT EMPNO, ENAME, JOB FROM EMP;
    SELECT EMPNO AS "NUMBER", ENAME AS "NAME", JOB AS JOB FROM EMP;
    SELECT DISTINCT JOB FROM EMP;
    SELECT 'No:'||EMPNO||',Name:'||ENAME||',Job:'||JOB FROM EMP; -- ''单引号字符串查询输出可以; "" 重命名可以
    SELECT ENAME, SAL*12 FROM EMP;
    SELECT * FROM EMP WHERE SAL>1500 AND NVL(COMM,0)!=0;
    SELECT * FROM EMP WHERE SAL<=1500 AND NVL(COMM,0)=0;
    SELECT * FROM EMP WHERE HIREDATE BETWEEN '1-JAN-1981' AND '31-DEC-1981'; -- 日期的顺序(DD-MM-YYYY)
    SELECT * FROM EMP WHERE EMPNO<>7368 AND EMPNO<>7499;
    SELECT * FROM EMP WHERE EMPNO<>7369;
    SELECT * FROM EMP ORDER BY SAL;
    SELECT * FROM EMP ORDER BY (SAL+NVL(COMM,0)) DESC, HIREDATE ASC;
    SELECT * FROM EMP WHERE DEPTNO=10 ORDER BY (SAL+NVL(COMM,0)) DESC, HIREDATE ASC;
    SELECT EMPNO, INITCAP(ENAME), JOB, MGR, HIREDATE, SAL, COMM,DEPTNO FROM EMP;
    SELECT ENAME, SUBSTR(ENAME, -3,3) FROM EMP;
    SELECT EMPNO, ENAME,TRUNC(MONTHS_BETWEEN(SYSDATE, HIREDATE)) FROM EMP;
    SELECT * FROM EMP WHERE NVL(COMM,0)>SAL*0.6 ;
    SELECT * FROM EMP WHERE (DEPTNO='10' AND JOB='MANAGER') OR (DEPTNO='20' AND JOB='CLERK');
    SELECT * FROM EMP WHERE JOB <> 'CLERK' AND JOB <> 'MANAGER' AND SAL>=2000;
    SELECT DISTINCT JOB FROM EMP WHERE COMM IS NULL OR COMM=0;
    SELECT * FROM EMP WHERE HIREDATE >= LAST_DAY(HIREDATE)-2;
    SELECT * FROM EMP WHERE MONTHS_BETWEEN(SYSDATE,HIREDATE)/12>=12;
    SELECT * FROM EMP WHERE LENGTH(ENAME)=5;
    SELECT * FROM EMP WHERE ename not like '%R%';-- 单引号
    SELECT ENAME, HIREDATE FROM EMP ORDER BY HIREDATE;
    SELECT ENAME, TO_CHAR(HIREDATE,'YYYY'), TO_CHAR(HIREDATE,'MM')  FROM EMP ORDER BY 3, 2; -- SELECT ENAME, (TO_CHAR(HIREDATE,'YYYY'))S1, (TO_CHAR(HIREDATE,'MM'))S2  FROM EMP ORDER BY S2, S1;
    SELECT ENAME, HIREDATE FROM EMP ORDER BY HIREDATE;
    SELECT trunc(MONTHS_BETWEEN(SYSDATE,hiredate)/12) year, trunc(MOD(MONTHS_BETWEEN(SYSDATE,hiredate),12)) months, trunc(SYSDATE - ADD_MONTHS(hiredate,months_between(sysdate,hiredate))) day FROM emp ;
    SELECT * FROM EMP WHERE ENAME LIKE '__A%';
    SELECT ENAME FROM EMP WHERE ENAME LIKE '%A%' OR ENAME LIKE '%N%';
    SELECT ENAME,SAL FROM EMP WHERE SAL>=1000 AND SAL<=1500 ORDER BY SAL DESC;
    SELECT ENAME,JOB,SAL*12 YSAL FROM EMP WHERE SAL*12>=15000 AND SAL*12<=20000 AND (JOB='MANAGER' OR JOB='SALESMAN');
    --区别: null的字段上做逻辑关系永假, <>,>,=,<
    /*  1. 在雇员表中查询雇员的编号、姓名、工作。（其视图名为 T2_1,后面的题目以 此类推）
        2. 为题目 1 中查询列取别名（number, NAME,JOB ）。
        3. 查询所有的工作。
        4. 按照以下的格式进行结果输出，如 NO:7469,Name:SMITH,Job:CLERK。
        5. 列出每个雇员的姓名及年薪。
        6. 查看每月可以得到奖金的雇员信息。
        7. 基本工资大于 1500，同时可以领取奖金的雇员信息。
        8. 查询基本工资不大于 1500，同时不可以领取奖金的雇员信息。
        9. 查询在 1981 年雇佣的全部雇员信息，BETWEEN .. AND 包含等于的情况。
        10. 查询出雇员编号不是 7369、7499 的雇员信息。
        11. 查看雇员编号不是 7369 的雇员信息，使用<>或!=。
        12. 对雇员的工资由低到高进行排序，升序为默认(ASC)，降序(DESC)。
        13. 查看出部门号为 10 的雇员信息，查询的信息按照工资从高到低，若工资相 等则按雇用日期从早到晚排列。
        14. 将雇员姓名变为开头字母大写，INITCAP。
        15. 显示所有雇员的姓名及姓名的后 3 个字符。
        16. 查询从雇用日期到今天所有雇员的雇员编号、姓名和月数。
        17. 找出佣金高于薪金的 60%的员工。
        18. 找出部门 10 中所有经理(MANAGER)和部门 20 中所有办事员(CLERK)的详 细资料。
        -43-19. 找出既不是经理又不是办事员但其薪金大于或等于2000的所有员工的资料。
        20. 找出有奖金的员工的不同工作。
        21. 找出各月倒数第 3 天受雇的所有员工。
        22. 找出早于 12 年前受雇的员工。
        23. 显示刚好为 5 个字符的员工的姓名。
        24. 显示不带有"R"的员工的姓名。
        25. 显示员工的姓名和受雇日期，将最老的员工排在最前。
        26. 显示所有员工的姓名，加入公司的年份和月份，按受雇日期所在月排序，若 月份相同则按年份排序。
        27. 找出在 2 月受聘的员工信息。
        28. 以年月日方式显示所有员工服务年限。
        29. 找出EMP 表中的姓名（ENAME）第三个字母是A 的员工姓名。
        30. 找出EMP 表员工名字中含有A 和N的员工姓名。
        31. 显示工资不在 1000 到 1500 之间的员工信息：名字、工资，按工资从大到小 排序。
        32. 显示职位为MANAGER 和 SALESMAN，年薪在 15000 和 20000 之间的员 工的信息：名字、职位、年薪。
        33. 说明以下两条 SQL语句的输出结果：
            1) SELECT EMPNO,COMM FROM EMP WHERE COMM IS NULL;
            2) SELECT EMPNO,COMM FROM EMP WHERE COMM = NULL;*/
    --Homework3-------------------------------------------------------------
    SELECT EMP.EMPNO, EMP.ENAME, EMP.DEPTNO, DEPT.LOC FROM EMP, DEPT WHERE EMP.DEPTNO=DEPT.DEPTNO;
    SELECT E1.ENAME,E1.JOB,E2.ENAME FROM EMP E1,EMP E2 WHERE E1.MGR=E2.EMPNO;
    SELECT E1.ENAME, E1.JOB, E2.ENAME, DNAME FROM EMP E1, EMP E2, DEPT WHERE E1.MGR=E2.EMPNO AND E.DEPTNO=DEPT.DEPTNO;
    SELECT E1.ENAME, E1.SAL+NVL(COMM,0), DNAME, E2.ENAME FROM EMP E1, EMP E2, DEPT WHERE E1.DEPTNO=DEPT.DEPTNO AND E1.MGR=E2.EMPNO;
    SELECT TO_CHAR(SALARY,'L99,999.99'), TO_CHAR(SALARY,'$99,999.99') FROM HR.EMPLOYEES WHERE ROWNUM < 5; -- 英文环境??
    SELECT ENAME, SAL+NVL(COMM,0), ROUND((E.SAL+NVL(COMM,0))*1.08) AS LATER_SAL FROM EMP WHERE ROWNUM<=5;
    SELECT UPPER(FIRST_NAME)||' '||UPPER(LAST_NAME) FROM EMPLOYEES WHERE MANAGER_ID IS NULL;
    SELECT E2.FIRST_NAME FROM EMPLOYEES E1, EMPLOYEES E2 WHERE E1.MANAGER_ID=E2.EMPLOYEE_ID AND E1.FIRST_NAME='David' AND E1.LAST_NAME='Austin';-- select first_name ||' '|| last_name from employees where employee_id=(select manager_id from employees where first_name='David' and last_name='Austin');
    SELECT E2.FIRST_NAME||' '|| E2.LAST_NAME FROM EMPLOYEES E1, EMPLOYEES E2 WHERE E1.FIRST_NAME='Alexander' AND E1.LAST_NAME='Hunold' AND E2.MANAGER_ID=E1.EMPLOYEE_ID;
    SELECT E1.FIRST_NAME, E1.SALARY, E2.FIRST_NAME, E2.SALARY FROM EMPLOYEES E1, EMPLOYEES E2 WHERE E1.MANAGER_ID=E2.EMPLOYEE_ID AND E1.SALARY>E2.SALARY;
    SELECT FIRST_NAME, LAST_NAME FROM EMPLOYEES WHERE DEPARTMENT_ID=(SELECT DEPARTMENT_ID FROM EMPLOYEES WHERE LAST_NAME='Chen');-- other: select * from employees e1 where exists( select *  from employees e2  where LAST_NAME='Chen' and e1.DEPARTMENT_ID=e2.DEPARTMENT_ID ) and e1.LAST_NAME<>'Chen' ;
    SELECT FIRST_NAME, LAST_NAME FROM EMPLOYEES WHERE JOB_ID=(SELECT JOB_ID FROM EMPLOYEES WHERE LAST_NAME='De Haan');-- other: select * from employees e1where exists( select *  from employees e2  where LAST_NAME='Chen' and e1.DEPARTMENT_ID=e2.DEPARTMENT_ID ) and e1.LAST_NAME<>'Chen' ;
    SELECT FIRST_NAME, LAST_NAME FROM EMPLOYEES WHERE DEPARTMENT_ID<>(SELECT DEPARTMENT_ID FROM EMPLOYEES WHERE LAST_NAME='Hall');-- other: select * from employees e1 where exists( select *  from employees e2 where LAST_NAME='Hall' AND E1.DEPARTMENT_ID <>E2.DEPARTMENT_ID or E1.DEPARTMENT_ID is null) ; --???? NOT EXISTS HOW TO WRITE????
    SELECT FIRST_NAME, LAST_NAME FROM EMPLOYEES WHERE JOB_ID<>(SELECT JOB_ID FROM EMPLOYEES WHERE FIRST_NAME='William' AND LAST_NAME='Smith'); -- other: select * from employees e1 where exists( select * from employees e2 where (LAST_NAME='Smith' and FIRST_NAME='William') and e1.JOB_ID<>e2.JOB_ID);
    SELECT E.FIRST_NAME, E.LAST_NAME, E.COMMISSION_PCT, DEPARTMENT_NAME, CITY FROM EMPLOYEES E, DEPARTMENTS D, LOCATIONS L WHERE E.DEPARTMENT_ID=D.DEPARTMENT_ID AND D.LOCATION_ID=L.LOCATION_ID AND COMMISSION_PCT IS NOT NULL; -- AND COMMISSION_PCT !=0;
    SELECT DISTINCT JOB_TITLE FROM EMPLOYEES E, JOBS J, DEPARTMENTS D WHERE E.DEPARTMENT_ID=D.DEPARTMENT_ID AND E.JOB_ID=J.JOB_ID AND D.DEPARTMENT_NAME='Executive';-- SELECT DISTINCT JOB_TITLE FROM EMPLOYEES ,JOBS WHERE JOBS.JOB_ID=EMPLOYEES.JOB_ID AND DEPARTMENT_ID =(SELECT DEPARTMENT_ID FROM DEPARTMENTS WHERE DEPARTMENT_NAME='Executive');
    SELECT MAX(SALARY)-MIN(SALARY) FROM EMPLOYEES;
    SELECT COUNT(*) FROM EMPLOYEES WHERE COMMISSION_PCT IS NOT NULL AND  COMMISSION_PCT>0; --emp和employees歧义 --zwz
    SELECT MAX(NVL(SALARY,0)), MIN(NVL(SALARY,0)), COUNT(NVL(SALARY,0)), ROUND(AVG(NVL(SALARY,0))) FROM EMPLOYEES; --emp和employees歧义 --zwz
    SELECT COUNT(DISTINCT(MANAGER_ID)) FROM EMPLOYEES WHERE MANAGER_ID IS NOT NULL;
    SELECT * FROM EMPLOYEES E1 WHERE SALARY=(SELECT MAX(SALARY) FROM EMPLOYEES WHERE DEPARTMENT_ID=E1.DEPARTMENT_ID) AND HIRE_DATE=(SELECT MAX(HIRE_DATE) FROM EMPLOYEES WHERE DEPARTMENT_ID=E1.DEPARTMENT_ID);-- SELECT FIRST_NAME, SALARY, HIRE_DATE FROM EMP E1 WHERE SAL=(SELECT MAX(SAL) FROM EMP WHERE DEPTNO=E1.DEPTNO) AND HIREDATE=(SELECT MAX(HIREDATE) FROM EMP WHERE DEPTNO=E1.DEPTNO); -- SELECT DISTINCT E1.FIRST_NAME, E1.LAST_NAME, E1.SALARY, E1.HIRE_DATE FROM EMPLOYEES E1, EMPLOYEES E2 WHERE E1.DEPARTMENT_ID=E2.DEPARTMENT_ID AND E1.SALARY>E2.SALARY AND E1.HIRE_DATE > E2.HIRE_DATE;-- SELECT DISTINCT E1.FIRST_NAME, E1.LAST_NAME, E1.SALARY, E1.HIRE_DATE FROM EMPLOYEES E1, EMPLOYEES E2 WHERE E1.DEPARTMENT_ID=E2.DEPARTMENT_ID AND E1.SALARY>E2.SALARY AND E1.HIRE_DATE > E2.HIRE_DATE; 不一样???
    /*1. 要求查询雇员的编号、姓名、部门编号、部门名称及部门位置。（其视图名为 T3_1,后面的题目以此类推）
      2. 要求查询每个雇员的姓名、工作、雇员的直接上级领导的姓名(表自关联)。
      3. 对题目 2 进行扩充，将雇员所在部门名称同时列出。
      4. 查询每个雇员的姓名、工资、部门名称，及其领导的姓名。
      5. 让 SELECT TO_CHAR(SALARY,'L99,999.99') FROM HR.EMPLOYEES WHERE ROWNUM < 5 输出结果的货币单位是￥和$。
      6. 列出前五位每个员工的名字，工资、涨薪后的的工资（涨幅为 8%），以“元” 为单位进行四舍五入。
      7. 找出谁是最高领导，将名字按大写形式显示。
      8. 找出 First_Name 为David，Last_Name 为 Austin 的直接领导名字。
      9. First_Name 为Alexander，Last_Name为Hunold领导谁。（谁向David 报告）。
      10. 哪些员工的工资高于他直接上司的工资，列出员工的名字和工资，上司的名 字和工资。
      11. 哪些员工和Chen(LAST_NAME)同部门。
      12. 哪些员工跟 De Haan(LAST_NAME)做一样职位。
      13. 哪些员工跟 Hall(LAST_NAME)不在同一个部门。
      14. 哪些员工跟William（FIRST_NAME）、Smith(LAST_NAME)做不一样的职位。
      15. 显示有提成的员工的信息：名字、提成、所在部门名称、所在地区的名称。
      16. 显示 Executive 部门有哪些职位。
      17. 整个公司中，最高工资和最低工资相差多少。
      18. 提成大于 0 的人数。
      19. 显示整个公司的最高工资、最低工资、工资总和、平均工资保留到整数位。
      20. 整个公司有多少个领导。
      21. 列出在同一部门入职日期晚但工资高于其他同事的员工：名字、工资、入职 日期。*/
    --Homework4-------------------------------------------------------------
    SELECT DNAME FROM DEPT WHERE DEPTNO IN (SELECT DEPTNO FROM EMP GROUP BY DEPTNO HAVING COUNT(EMPNO)>=1); --other1: select dname from dept where deptno in(select deptno from emp); -- other2: SELECT DISTINCT DNAME FROM EMP E1, DEPT D1 WHERE E1.DEPTNO=D1.DEPTNO AND (SELECT COUNT(*) FROM DEPT D2 WHERE D1.DEPTNO=D2.DEPTNO)>=1;
    SELECT * FROM EMP WHERE SAL> ( SELECT SAL FROM EMP WHERE ENAME='SMITH');-- `=` -> like.....
    SELECT E1.ENAME,E2.ENAME FROM EMP E1,EMP E2 WHERE E1.MGR=E2.EMPNO;
    SELECT E1.* FROM EMP E1,EMP E2 WHERE E1.MGR=E2.EMPNO AND E1.HIREDATE<E2.HIREDATE;
    SELECT A.DNAME,E.* FROM DEPT A LEFT JOIN EMP E ON A.DEPTNO = E.DEPTNO;
    SELECT ENAME, DNAME FROM EMP, DEPT WHERE DEPT.DEPTNO=EMP.DEPTNO AND JOB='CLERK';
    SELECT * FROM JOBS WHERE MIN_SALARY>1500;
    SELECT ENAME FROM EMP WHERE DEPTNO=(SELECT DEPTNO FROM DEPT WHERE DNAME='SALES');
    SELECT * FROM EMP WHERE SAL>(SELECT AVG(SAL) FROM EMP);
    SELECT * FROM EMP WHERE JOB=(SELECT JOB FROM EMP WHERE ENAME='SCOTT');
    SELECT FIRST_NAME FROM EMPLOYEES E1 WHERE SALARY IN(SELECT SALARY FROM EMPLOYEES E2 WHERE E2.DEPARTMENT_ID=30) AND E1.DEPARTMENT_ID <>30;--SELECT ENAME ,SAL FROM EMP WHERE SAL IN(SELECT SAL FROM EMP WHERE DEPTNO=30);
    SELECT * FROM EMP WHERE SAL > (SELECT MAX(SAL) FROM EMP WHERE DEPTNO=30);
    SELECT DEPTNO, COUNT(1), AVG(SAL), AVG(SYSDATE-HIREDATE) FROM EMP GROUP BY DEPTNO;-- select (select b.dname from dept b where a.deptno=b.deptno) as deptname ,count(deptno) as deptcount,avg(sal) as deptavgsal from emp a group by deptno;
    SELECT ENAME, DNAME, SAL+NVL(COMM,0) FROM EMP,DEPT WHERE DEPT.DEPTNO=EMP.DEPTNO; -- emps employees歧义
    SELECT DEPT.*, count(emp.empno) FROM DEPT, EMP WHERE DEPT.DEPTNO=EMP.DEPTNO(+) GROUP BY DEPT.DEPTNO, DEPT.DNAME, DEPT.LOC; -- SELECT DEPT.DNAME, COUNT(EMP.EMPNO) FROM EMP, DEPT WHERE EMP.DEPTNO=DEPT.DEPTNO GROUP BY EMP.DEPTNO, DEPT.DNAME;---JOIN SELECT DEPT.*, COUNT(EMP.EMPNO) FROM DEPT LEFT JOIN EMP ON DEPT.DEPTNO=EMP.EMPNO; ??? -- (+) 和 join left right 转化
    SELECT JOB_TITLE, MIN_SALARY FROM JOBS;
    SELECT DEPTNO, MIN(SALARY) FROM EMPLOYEES WHERE JOB='MANAGER' GROUP BY DEPTNO;-- EMPLOYEES & EMP 歧义
    select EMPLOYEE_ID,SALARY*12 FROM EMPLOYEES ORDER BY 2;
    SELECT AVG(SAL), MAX(SAL), MIN(SAL), COUNT(*) FROM EMP GROUP BY DEPTNO ORDER BY DEPTNO;-- EMPLOYEES & EMP 歧义 SELECT DEPARTMENT_ID, AVG(SALARY), MAX(SALARY), MIN(SALARY), COUNT(*) FROM EMPLOYEES GROUP BY DEPARTMENT_ID ORDER BY DEPARTMENT_ID;
    SELECT DEPARTMENT_ID,COUNT(EMPLOYEE_ID) FROM EMPLOYEES WHERE SALARY>5000 GROUP BY DEPARTMENT_ID; --?? EMP 没有大于5000的人 所以是employees, 为什么没有部门还有工资???
    SELECT DEPT.DEPTNO, AVG(SAL), COUNT(EMPNO) FROM EMP, DEPT WHERE EMP.DEPTNO(+)=DEPT.DEPTNO GROUP BY DEPT.DEPTNO; -- EMPLOYEES & EMP 歧义 为什么这个group不用全写出来????
    -- SELECT DEPARTMENT_ID,SALARY,COUNT(EMPLOYEE_ID) FROM EMPLOYEES GROUP BY DEPARTMENT_ID,SALARY；
    SELECT DNAME, LOC, COUNT(EMPNO) FROM EMP, DEPT WHERE SAL>1000 AND DEPT.DEPTNO=EMP.DEPTNO(+) GROUP BY DEPT.DEPTNO, DEPT.DNAME, DEPT.LOC HAVING COUNT(EMP.EMPNO)>2; --??? SELECT DNAME, LOC, COUNT(EMPNO) FROM EMP, DEPT WHERE SAL>1000 AND DEPT.DEPTNO=EMP.DEPTNO(+) GROUP BY DEPT.DEPTNO, DEPT.DNAME, DEPT.LOC;
    SELECT ENAME, SAL+NVL(COMM,0) LS FROM EMP WHERE SAL+NVL(COMM,0)>(SELECT AVG(SAL) FROM EMP) ORDER BY SAL+NVL(COMM,0) DESC;
    SELECT * FROM EMPLOYEES WHERE SALARY BETWEEN (SELECT AVG(SALARY) FROM EMPLOYEES WHERE DEPARTMENT_ID=50) AND (SELECT AVG(SALARY) FROM EMPLOYEES WHERE DEPARTMENT_ID=80); -- 哪些员工的工资，介于 50 号 和 80 号部门平均工资之间。DEPT 没有80号部门
    SELECT FIRST_NAME||' '||LAST_NAME FROM EMPLOYEES E1 WHERE E1.SALARY>(SELECT AVG(SALARY) FROM EMPLOYEES E2 WHERE E2.DEPARTMENT_ID=E1.DEPARTMENT_ID);
    SELECT FIRST_NAME||' '||LAST_NAME, DEPARTMENT_ID, SALARY FROM EMPLOYEES E1 WHERE SALARY= (SELECT MAX(SALARY) FROM EMPLOYEES E2 WHERE E2.DEPARTMENT_ID =E1.DEPARTMENT_ID) HIRE_DATE=(SELECT MAX(HIRE_DATE) FROM EMPLOYEES E3 WHERE E3.DEPARTMENT_ID = E1.DEPARTMENT_ID);
    SELECT * FROM (SELECT AVG(SALARY) FROM EMPLOYEES GROUP BY DEPARTMENT_ID ORDER BY DEPARTMENT_ID DESC) WHERE ROWNUM=1;
    /*  1. 列出至少有一个员工的所有部门。（其视图名为 T4_1,后面的题目以此类推）
        2. 列出薪金比“SMITH”多的所有员工。
        3. 列出所有员工的姓名及其直接上级的姓名。
        4. 列出受雇日期早于其直接上级的所有员工。
        5. 列出部门名称和这些部门的员工信息，同时列出那些没有员工的部门。
        6. 列出所有“CLERK”（办事员）的姓名及其部门名称。
        7. 列出最低薪金大于 1500 的各种工作。
        8. 列出在部门“SALES”（销售部）工作的员工的姓名，假定不知道销售部的部 门编号。
        9. 列出薪金高于公司平均薪金的所有员工。
        10. 列出与“SCOTT”从事相同工作的所有员工。
        11. 列出薪金等于部门 30 中员工的薪金的所有员工的姓名和薪金。
        12. 列出薪金高于在部门 30 工作的所有员工的薪金的员工姓名和薪金。
        13. 列出在每个部门工作的员工数量、平均工资和平均服务期限。
        14. 列出所有员工的姓名、部门名称和工资。
        15. 列出所有部门的详细信息和部门人数。
        16. 列出各种工作的最低工资。
        17. 列出各个部门的MANAGER（经理）的最低薪金。
        18. 列出所有员工的年工资,按年薪从低到高排序。
        19. 各个部门平均、最大、最小工资、人数，按照部门号升序排列。
        20. 各个部门中工资大于 5000 的员工人数。
        21. 各个部门平均工资和人数，按照部门名字升序排列。
        22. 列出每个部门中有同样工资的员工的统计信息，列出他们的部门号，工 资，人数。
        23. 列出同部门中工资高于 1000 的员工数量超过 2 人的部门，显示部门名 字、地区名称。
        24. 哪些员工的工资，高于整个公司的平均工资，列出员工的名字和工资（降序）。
        25. 哪些员工的工资，介于 50 号 和 80 号部门平均工资之间。
        26. 所在部门平均工资高于 5000 的员工名字。
        27. 列出各个部门中工资最高的员工的信息：名字、部门号、工资。
        28. 最高的部门平均工资是多少。*/
    --Homework4-------------------------------------------------------------
    SELECT DEPARTMENT_ID,COUNT(*) FROM EMPLOYEES GROUP BY DEPARTMENT_ID HAVING COUNT(*) > (SELECT COUNT(*) FROM EMPLOYEES WHERE DEPARTMENT_ID = 90);-- SELECT DEPARTMENT_NAME FROM DEPARTMENTS WHERE DEPARTMENT_ID IN (SELECT DISTINCT DEPARTMENT_ID FROM EMPLOYEES E2 WHERE (SELECT COUNT(*) FROM EMPLOYEES E3 WHERE E2.DEPARTMENT_ID=E3.DEPARTMENT_ID) > (SELECT COUNT(*) FROM EMPLOYEES E1 WHERE E1.DEPARTMENT_ID=90));
    SELECT FIRST_NAME||' '||LAST_NAME FROM EMPLOYEES WHERE EMPLOYEE_ID=( SELECT  MANAGER_ID FROM EMPLOYEES WHERE FIRST_NAME='Den' AND LAST_NAME='Raphaely');
    SELECT FIRST_NAME||' '||LAST_NAME FROM EMPLOYEES WHERE MANAGER_ID=(SELECT EMPLOYEE_ID FROM EMPLOYEES WHERE FIRST_NAME='Den' AND LAST_NAME='Raphaely');
    SELECT FIRST_NAME||' '||LAST_NAME FROM EMPLOYEES E1 WHERE EXISTS ( SELECT * FROM EMPLOYEES E2 WHERE FIRST_NAME='Den' AND LAST_NAME='Raphaely' AND E2.MANAGER_ID=E1.EMPLOYEE_ID);
    SELECT FIRST_NAME||' '||LAST_NAME FROM EMPLOYEES E1 WHERE EXISTS ( SELECT * FROM EMPLOYEES E2 WHERE FIRST_NAME='Den' AND LAST_NAME='Raphaely' AND E1.MANAGER_ID=E2.EMPLOYEE_ID);
    SELECT FIRST_NAME||' '||LAST_NAME, DEPARTMENT_ID, SALARY FROM EMPLOYEES E1 WHERE SALARY= (SELECT MAX(SALARY) FROM EMPLOYEES E2 WHERE E2.DEPARTMENT_ID =E1.DEPARTMENT_ID) HIRE_DATE=(SELECT MAX(HIRE_DATE) FROM EMPLOYEES E3 WHERE E3.DEPARTMENT_ID = E1.DEPARTMENT_ID);-- 列出在同一部门共事，入职日期晚但工资高于其他同事的员工：名字、 工资、入职日期
    SELECT FIRST_NAME||' '||LAST_NAME FROM EMPLOYEES E1 WHERE DEPARTMENT_ID <> (SELECT DEPARTMENT_ID FROM EMPLOYEES E2 WHERE FIRST_NAME='Den' AND LAST_NAME='Raphaely');
    SELECT FIRST_NAME||' '||LAST_NAME FROM EMPLOYEES E1 WHERE NOT EXISTS (SELECT 1 FROM EMPLOYEES E2 WHERE FIRST_NAME='Den' AND LAST_NAME='Raphaely' AND E1.DEPARTMENT_ID=E2.DEPARTMENT_ID);
    SELECT DISTINCT JOB_ID FROM EMPLOYEES WHERE DEPARTMENT_ID = ( SELECT DEPARTMENT_ID FROM DEPARTMENTS WHERE DEPARTMENT_NAME = 'Finance'); -- SELECT DISTINCT JOB_TITLE FROM JOBS J1 WHERE JOB_ID IN (SELECT JOB_ID FROM EMPLOYEES E1, DEPARTMENTS D1 WHERE D1.DEPARTMENT_ID=E1.DEPARTMENT_ID AND DEPARTMENT_NAME='Finance'); -- SELECT DISTINCT JOB_TITLE FROM JOBS J1, DEPARTMENTS D1, EMPLOYEES E1 WHERE J1.JOB_ID=E1.JOB_ID AND D1.DEPARTMENT_ID=E1.DEPARTMENT_ID AND DEPARTMENT_NAME='Finance';
    SELECT DISTINCT JOB_ID FROM EMPLOYEES E1 WHERE EXISTS (SELECT * FROM DEPARTMENTS D1 WHERE DEPARTMENT_NAME = 'Finance' AND E1.DEPARTMENT_ID=D1.DEPARTMENT_ID);
    -- *, 1 AND DEPARTMENT_ID IS OK BUT WHY??????
    /*1. 哪些部门的人数比 90 号部门的人数多
     *2. Den(FIRST_NAME)、Raphaely(LAST_NAME)的领导是谁（非关联子查询）
     *3. Den(FIRST_NAME)、Raphaely(LAST_NAME) 领导谁（非关联子查询）
     *4. Den(FIRST_NAME)、Raphaely(LAST_NAME) 的领导是谁（关联子查询）
     *5. Den(FIRST_NAME)、Raphaely(LAST_NAME) 领导谁（关联子查询）
     *6. 列出在同一部门共事，入职日期晚但工资高于其他同事的员工：名字、 工资、入职日期（关联子查询）
     *7. 哪些员工跟 Den(FIRST_NAME)、Raphaely(LAST_NAME)不在同一个部 门（非关联子查询）
     *8. 哪些员工跟 Den(FIRST_NAME)、Raphaely(LAST_NAME)不在同一个部 门（关联子查询）
     *9. Finance 部门有哪些职位（非关联子查询）
     *10. Finance 部门有哪些职位（关联子查询）
     */
    ```
-
-