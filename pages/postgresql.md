alias:: pgsql
tags:: #database/object–relational
created:: 20230822
- ## Why
  - [[vs]] [[mysql]] Ref [彦祖们， pg 还是 mysql? 到底该怎么选？ - V2EX](https://v2ex.com/t/800592)
    - [MySQL :: MySQL Restrictions and Limitations :: 12 Limits in MySQL](https://dev.mysql.com/doc/mysql-reslimits-excerpt/8.0/en/limits.html)
      collapsed:: true
      - [Identifier Length Limits](https://dev.mysql.com/doc/mysql-reslimits-excerpt/8.0/en/identifier-length.html) 标识符长度
        collapsed:: true
        - | Identifier Type | Maximum Length (characters) |
          | ---- | ---- | ---- |
          | Database | 64 (includes NDB Cluster 8.0.18 and later) |
          | Table | 64 (includes NDB Cluster 8.0.18 and later) |
          | Column | 64 |
          | Index | 64 |
          | Constraint | 64 |
          | Stored Program | 64 |
          | View | 64 |
          | Tablespace | 64 |
          | Server | 64 |
          | Log File Group | 64 |
          | Alias | 256 (see exception following table) |
          | Compound Statement Label | 16 |
          | User-Defined Variable | 64 |
          | Resource Group | 64 |
      - [Grant Table Scope Column Properties](https://dev.mysql.com/doc/mysql-reslimits-excerpt/8.0/en/grant-tables-scope-column-properties.html) 授权列长度
        collapsed:: true
        - **Table 12.1 Grant Table Scope Column Lengths**
          | Column Name | Maximum Permitted Characters |
          | ---- | ---- | ---- |
          | `Host`, `Proxied_host` | 255 (60 prior to MySQL 8.0.17) |
          | `User`, `Proxied_user` | 32 |
          | `Db` | 64 |
          | `Table_name` | 64 |
          | `Column_name` | 64 |
          | `Routine_name` | 64 |
      - ~~[Limits on Number of Databases and Tables](https://dev.mysql.com/doc/mysql-reslimits-excerpt/8.0/en/database-count-limit.html)~~
      - ~~[Limits on Table Size](https://dev.mysql.com/doc/mysql-reslimits-excerpt/8.0/en/table-size-limit.html)~~ determined by operating system constraints on file sizes
      - [Limits on Table Column Count and Row Size](https://dev.mysql.com/doc/mysql-reslimits-excerpt/8.0/en/column-count-limit.html)
        collapsed:: true
        - MySQL has hard limit of ==4096 columns per table==, but the effective maximum may be less for a given table.
        - The internal representation of a MySQL table has a maximum ==row size== limit of 65,535 bytes, even if the storage engine is capable of supporting larger rows.1
      -
      -
      -
      -
    - [PostgreSQL: Documentation: 13: Appendix K. PostgreSQL Limits](https://www.postgresql.org/docs/13/limits.html)
      collapsed:: true
      - [Table K.1](limits.html#LIMITS-TABLE) describes various hard limits of PostgreSQL. However, practical limits, such as performance limitations or available disk space may apply before absolute hard limits are reached.
      - **Table K.1. PostgreSQL Limitations**
        | Item | Upper Limit | Comment |
        |---|---|---|
        | database size | unlimited | |
        | number of databases | 4,294,950,911 | |
        | relations per database | 1,431,650,303 | |
        | relation size | 32 TB | with the default BLCKSZ of 8192 bytes |
        | rows per table | limited by the number of tuples that can fit onto 4,294,967,295 pages | |
        | columns per table | 1600 | further limited by tuple size fitting on a single page; see note below |
        | columns in a result set | 1664 | |
        | field size | 1 GB | |
        | identifier length | 63 bytes | can be increased by recompiling PostgreSQL |
        | indexes per table | unlimited | constrained by maximum relations per database |
        | columns per index | 32 | can be increased by recompiling PostgreSQL |
        | partition keys | 32 | can be increased by recompiling PostgreSQL |
      - The maximum number of columns for a table is further reduced as the tuple being stored must fit in a single 8192-byte heap page. For example, excluding the tuple header, a tuple made up of 1600 `int` columns would consume 6400 bytes and could be stored in a heap page, but a tuple of 1600 `bigint` columns would consume 12800 bytes and would therefore not fit inside a heap page. Variable-length fields of types such as `text`, `varchar`, and `char` can have their values stored out of line in the table's TOAST table when the values are large enough to require it. Only an 18-byte pointer must remain inside the tuple in the table's heap. For shorter length variable-length fields, either a 4-byte or 1-byte field header is used and the value is stored inside the heap tuple.
      - Columns that have been dropped from the table also contribute to the maximum column limit. Moreover, although the dropped column values for newly created tuples are internally marked as null in the tuple's null bitmap, the null bitmap also occupies space.
      -
- ## How
  -
- ## What
  -
  -
-