icon:: 📄
also:: pgsql
created:: [[20240817]]
description:: C实现；BDS协议；之前叫Ingres，后面为了解决一些ingres中的一些问题，更名 postgre；社区活跃，3个月一版；允许跨版本升级；
tags:: #database-object–relational
source:: {{nav-ri https://www.postgresql.org/}}, {{nav-ri http://www.postgres.cn/v2/home}}
title:: postgresql

- ## Why
  -
- ## How
  - Install
    collapsed:: true
    - ```shell
      # 下载PGSQL的rpm包
      sudo yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
      # 安装PGSQL12的软件程序，需要下载，需要等一会，一般不会失败，即便失败，他也会重新帮你找镜像
      sudo yum install -y postgresql12-server
      # 数据库初始化
      sudo /usr/pgsql-12/bin/postgresql-12-setup initdb
      # 设置开启启动项，并设置为开启自行启动
      sudo systemctl enable postgresql-12
      # 启动PGSQL
      sudo systemctl start postgresql-12
      # 切换到postgres用户
      su postgres
      # 进入命令行
      psql
      # 查看有哪些库，如果是新安装的，有三个库，一个是postgres，template0，template1
      \l
      
      ```
  - Config
    - remote connect
      collapsed:: true
      - #+BEGIN_TIP
        mysql 是基于改表来控制连接的用户，而PG是通过修改文件的方式进行配置
        #+END_TIP
      - ```shell
        vim pg_hba.conf
        ```
      - PostgreSQL默认情况下不支持远程连接的，这个跟MySQL几乎一样
        - ```shell
          # 第一块
          local：代表本地连接，host代表可以指定连接的ADDRESS
          # 第二块
          database编写数据库名，如果写all，代表所有库都可以连接
          # 第三块
          user编写连接的用户，可以写all，代表所有用户
          # 第四块
          address代表那些IP地址可以连接
          # 第五块
          method加密方式，这块不用过多关注，直接md5
          # 直接来个痛快的配置吗，允许任意地址的全部用户连接所有数据库
          host    all             all             0.0.0.0/0               md5
          ```
      - `listen_address='*'`
      - 重启
        - ```shell
          # postgres密码不管，直接root用户
          sudo systemctl restart postgresql-12
          ```
    - log
      collapsed:: true
      - ```shell
        $ vim postgresql.conf
        # 代表日志是开启的。
        logging_collector = on
        # 日志存放的路径，默认放到当前目录下的log里
        log_directory = 'log'
        # 日志的文件名，默认是postgresql为前缀，星期作为后缀
        log_filename = 'postgresql-%a.log'
        # 默认一周过后，日志文件会被覆盖
        log_truncate_on_rotation = on
        # 一天一个日志文件
        log_rotation_age = 1d
        # 一个日志文件，没有大小限制
        log_rotation_size = 0
        ```
- ## What
  - Data type
    collapsed:: true
    - logseq.table.version:: 2
      | 名称 | 说明| 对比MySQL|
      | ---------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
      | 布尔 | boolean，标准的布尔类型，只能存储true，false| MySQL中虽然没有对应的boolean，但是有替换的类型，数值的tinyint类型，和PGSQL的boolean都是占1个字节。 |
      | 整型 | smallint（2字节），integer（4字节），bigint（8字节）| 跟MySQL没啥区别。|
      | 浮点型 | decimal，numeric（和decimal一样一样的，精准浮点型），real（float），double precision（double），money（货币类型） | 和MySQL基本也没区别，MySQL支持float，double，decimal。MySQL没有这个货币类型。|
      | 字符串 | varchar(n)（character varying），char(n)（character），text | 这里和MySQL基本没区别。PGSQL存储的varchar类型，可以存储一个G。MySQL好像存储64kb（应该是）。 |
      | 日期 | date（年月日），time（时分秒），timestamp（年月日时分秒）（time和timestamp可以设置时区）| 没啥说的，和MySQL基本没区别。MySQL有个datetime。|
      | 二进制 | bytea-存储二进制类型| MySQL也支持，MySQL中是blob |
      | 位图 | bit(n)（定长位图），bit varying(n)（可变长度位图）| 就是存储0，1。MySQL也有，只是这个类型用的不多。|
      | 枚举 | enum，跟Java的enum一样| MySQL也支持。|
      | 几何 | 点，直线，线段，圆…………| MySQL没有，但是一般开发也用不到|
      | 数组 | 在类型后，追加[]，代表存储数组| MySQL没有~~~ |
      | JSON | json（存储JSON数据的文本），jsonb（存储JSON二进制） | 可以存储JSON，MySQL8.x也支持 |
      | ip | cidr（存储ip地址）| MySQL也不支持~ |
      |... | http://www.postgres.cn/docs/12/datatype.html||
    - 单双引号
      collapsed:: true
      - 单引号用来标识实际的值
      - 双引号用来标识一个关键字，比如表名，字段名。
      - ```sql
        -- 单引号写具体的值，双引号类似MySQL的``标记，用来填充关键字
        -- 下面的葡萄牙会报错，因为葡萄牙不是关键字
        select 1.414,'卡塔尔',"葡萄牙";
        ```
    - 数据类型转换（3）
      collapsed:: true
      - ```sql
        -- 1、将字符串转成位图类型
        select bit '010101010101001';
        -- 2、数据类型
        select '2011-11-11'::date;
        select '101010101001'::bit(20);
        select '13'::int;
        -- 3、类型转换的完整写法
        select CAST(varchar '100' as int);
        ```
    - 布尔运算
      collapsed:: true
      - ```sql
        -- 布尔类型的约束没有那么强，true，false大小写随意，他会给你转，同时yes，no这种他也认识，但是需要转换
        select true,false,'yes'::boolean,boolean 'no',True,FaLse,NULL::boolean;
        ```
      - | 字段A | 字段B | a and b | a or b |
        | ----- | ----- | ------- | ------ |
        | true  | true  | true    | true   |
        | true  | false | false   | true   |
        | true  | NULL  | NULL    | true   |
        | false | false | false   | false  |
        | false | NULL  | false   | NULL   |
        | NULL  | NULL  | NULL    | NULL   |
    - 数值类型
      collapsed:: true
      - 整型
        collapsed:: true
        - smallint、int2：2字节
        - integer、int、int4：4字节
        - bigint、int8：8字节
      - 浮点型
        collapsed:: true
        - decimal(n,m)：本质就是numeric，PGSQL会帮你转换
        - numeric(n,m)：PGSQL本质的浮点类型
      - 序列
        collapsed:: true
        - #+BEGIN_TIP
          MySQL中的主键自增，是基于auto_increment去实现。MySQL里没有序列的对象。
          #+END_TIP
        - 序列的正常构建方式：
        - ```sql
          create sequence laozheng.table_id_seq;
          -- 查询下一个值
          select nextval('laozheng.table_id_seq');
          -- 查询当前值
          select currval('laozheng.table_id_seq');
          ```
        - 高速缓存
          collapsed:: true
          - 插入的数据比较多，可以指定告诉缓存，一次性计算出20个后续的值，nextval时，就不可以不去计算，直接去高速缓存拿值，效率会有一内内的提升。
        - ```sql
          -- 表自增
          create table laozheng.xxx(
              id int8 default nextval('laozheng.table_id_seq'),
              name varchar(16)
          );
          insert into laozheng.xxx (name) values ('xxx');
          select * from laozheng.xxx;
          
          -- 表自增，使用提供的序列类型
          create table laozheng.yyy(
              id bigserial,   
              name varchar(16)
          );
          insert into laozheng.yyy (name) values ('yyy');
          
          ```
        - 序列类型
          collapsed:: true
          - smallserial
          - serial
          - bigserial
        - #+BEGIN_NOTE
          如果是单独构建序列，再构建表，使用传统方式实现，序列和表就是相对独立的。
          
          #+END_NOTE
      - 数值运算
        collapsed:: true
        - | 操作符 | 描述   | 示例    | 结果 |
          | ------ | ------ | ------- | ---- |
          | ^      | 幂     | 2 ^ 3   | 8    |
          | @@html: &vert;@@/    | 平方根 | @@html: &vert;@@/ 36  | 6    |
          | @      | 绝对值 | @ -5    | 5    |
          | &      | 与     | 31 & 16 | 16   |
          | @@html: &vert;@@      | 或     | 31 @@html: &vert;@@ 32  | 63   |
          | <<     | 左移   | 1<<1    | 2    |
          | >>     | 右移   | 16>>1   | 8    |
        - 数值操作也提供了一些函数，比如pi()，round(数值，位数)，floor()，ceil()
    - 字符串
      collapsed:: true
      - character（就是MySQL的char类型），定长字符串。（最大可以存储1G）
      - character varying（varchar），可变长度的字符串。（最大可以存储1G）
      - text（跟MySQL异常）长度特别长的字符串。
    - 日期
      collapsed:: true
      - 类型
        collapsed:: true
        - timestamp（时间戳，覆盖 年月日时分秒）
        - date（年月日）
        - time（时分秒）
      - 时间
        collapsed:: true
        - 可以使用now作为当前系统时间（没有时区的概念）
        - ```sql
          select timestamp 'now';
          -- 直接查询now，没有时区的概念
          select time with time zone 'now' at time zone '08:00:00'
          ```
        - 也可以使用current_timestamp的方式获取（推荐，默认东八区）
      - 运算
        collapsed:: true
        - 正常对date类型做+，-操作，默认单位就是天~
        - date + time = timestamp~~~
          collapsed:: true
          - ```sql
            select date '2011-11-11' + time '12:12:12' ;
            ```
        - 可以针对timestamp使用interval的方式进行 +，-操作，在查询以时间范围为条件的内容时，可以使用
          collapsed:: true
          - ```sql
            select timestamp '2011-11-11 12:12:12' + interval '1day' + interval '1minute' + interval '1month';
            ```
    - 枚举
      collapsed:: true
      - ```sql
        -- 声明一个星期的枚举，值自然只有周一~周日。
        create type week as enum ('Mon','Tues','Sun');
        -- 声明一张表，表中的某个字段的类型是上面声明的枚举。
        drop table test;
        create table test(
            id bigserial ,
            weekday week
        );
        insert into test (weekday) values ('Mon');
        ```
    - IP
      collapsed:: true
      - 支持IPv4、IPv6、Mac
      - IP校验
        - ```sql
          select '192.168.11.256'::cidr
          -- 256 超了
          ```
      - 范围查找
        - ```sql
          drop table test;
          create table test{
          	id bigserial,
              ip cidr
          }
          insert into test(ip) value ('192.168.11.11')
          insert into test(ip) value ('192.168.11.12')
          insert into test(ip) value ('192.168.11.13')
          
          select * from test 
          where ip between '192.168.11.11' and '192.168.11.12'
          ```
    - JSON & JSONB
      collapsed:: true
      - JSON和JSONB的区别：
        collapsed:: true
        - JSON类型无法构建索引，JSONB类型可以创建索引。
        - JSON类型的数据中多余的空格会被存储下来。JSONB会自动取消多余的空格。
        - JSON类型甚至可以存储重复的key，以最后一个为准。JSONB不会保留多余的重复key（保留最后一个）。
        - JSON会保留存储时key的顺序，JSONB不会保留原有顺序。
      - JSON中key对应的value的数据类型
        collapsed:: true
        - | JSON    | PGSQL   |
          | ------- | ------- |
          | String  | text    |
          | number  | numeric |
          | boolean | boolean |
          | null    | (none)  |
        - 上述的四种JSON存储的类型：
          collapsed:: true
          - ```sql
            select '9'::JSON,'null'::JSON,'"laozheng"'::JSON,'true'::json;
            select '9'::JSONB,'null'::JSONB,'"laozheng"'::JSONB,'true'::JSONB;
            ```
      - JSON数组
        collapsed:: true
        - ```sql
          select '[9,true,null,"我是字符串"]'::JSON;
          ```
      - JSON对象
        collapsed:: true
        - ```sql
          select '{"name": "张三","age": 23,"birthday": "2011-11-11","gender": null}'::json;
          select '{"name": "张三","age": 23,"birthday": "2011-11-11","gender": null}'::jsonb;
          ```
      - 构建表存储JSON
        collapsed:: true
        - ```sql
          create table test(
              id bigserial,
              info json,
              infob jsonb
          );
          insert into test (info,infob) values 
          ('{"name": "张三","age": 23,"birthday": "2011-11-11","gender": null}',
          '{"name": "张三","age": 23,"birthday": "2011-11-11","gender": null}')
          select * from test;
          ```
      - 构建索引的效果
        collapsed:: true
        - ```sql
          create index json_index on test(info);
          create index jsonb_index on test(infob);
          ```
      - JSON还支持很多函数。可以直接查看   http://www.postgres.cn/docs/12/functions-json.html   函数太多了，不分析了。
      -
    - 复合类型
      collapsed:: true
      - Java 中的对象；
        collapsed:: true
        - ```java
          public class User{
             private Integer id;
             private Info info;
          }
          
          class Info{
             private String name;
             private Integer age;
          }
          ```
      - 建表
        collapsed:: true
        - ```sql
          -- 构建复合类型，映射上Info
          create type info_type as (name varchar(32),age int);
          -- 构建表，映射User
          create table tb_user(
              id serial,
              info info_type
          );
          -- 添加数据
          insert into tb_user (info) values (('张三',23));
          insert into tb_user (info) values (('露丝',233));
          insert into tb_user (info) values (('jack',33));
          insert into tb_user (info) values (('李四',24));
          select * from tb_user;
          ```
    - 数组
      collapsed:: true
      - ```sql
        drop table test;
        create table test(
            id serial,
            col1 int[],
            col2 int[2],
            col3 int[][]
        );
        -- 构建表指定数组长度后，并不是说数组内容只有2的长度，可以插入更多数据
        -- 甚至在你插入数据，如果将二维数组结构的数组扔到一维数组上，也可以存储。
        -- 数组编写方式
        select '{{how,are},{are,you}}'::varchar[];
        select array[[1,2],[3,4]];
        insert into test (col1,col2,col3) values ('{1,2,3}','{4,5,6}','{7,8,9}');
        insert into test (col1,col2,col3) values ('{1,2,3}','{4,5,6}',array[[1,2],[3,4]]);
        insert into test (col1,col2,col3) values ('{1,2,3}','{4,5,6}','{{1,2},{3,4}}');
        select * from test;
        ```
      - 如果现在要存储字符串数组，如果存储的数组中有双引号怎么办，有大括号怎么办。
        - ```sql
          -- 如果存储的数组中的值，有单引号怎么办？
          -- 使用两个单引号，作为一个单引号使用
          select '{''how''}'::varchar[];
          -- 如果存储的数组中的值，有逗号怎么办？(PGSQL中的数组索引从1开始算，写0也是从1开始算。)
          -- 用双引号将数组的数据包起来~
          select ('{"how,are"}'::varchar[])[2];
          -- 如果存储的数组中的值，有双引号怎么办？
          -- 如果要添加双引号，记得转义。
          select ('{"\"how\",are"}'::varchar[])[1];
          ```
      - 比较运算
        - ```sql
          -- 包含
          select array[1,2] @> array[1];
          -- 被包含
          select array[1,2] <@ array[1,2,4];
          -- 是否有相同元素
          select array[2,4,4,45,1] && array[1];
          ```
  - Table
    - 约束
    - 触发器
    - 表空间
    - 视图
    - 索引
    - 物化视图
  - [[transaction]]
  -
    -
-
-
-
- ## Namespace
  - {{namespace postgresql}}
- ## ↩ Reference
  - 华为GaussDB还有腾讯的Tbase都是基于PGSQL做的二次封装；
-