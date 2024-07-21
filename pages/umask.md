alias:: commands/umask
-
- ```shell
  umask -S
  # u=rwx,g=rx,o=rx
  umask 002
  umask g+r
  ```
  - {{embed ((6303ca6c-d6fa-4225-ba1e-14a08a320624))}}
  - 数字含义和 [[chmod]] 的 ((6303c9af-98c8-4845-bfeb-f5f110b5458d)) 是不一样的
    - `0` 代表读取、写入与执行
    - `1` 代表读取与写入
    - `2` 代表读取与执行
    - `3` 代表只读
    - `4` 代表写入与执行
    - `5` 代表仅写入
    - `6` 代表仅执行
    - `7` 代表没有权限
-