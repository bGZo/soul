also:: commands/chown
-
- 所有权转移
  - 所有**者**
    - ```shell
      chown <owner> <file>
      ```
  - 所有**组** (`chgrp`)
    - ```shell
      chown <owner>:<group> <file>
      ```
-
- Cases
  - 改变目录的所有权，同时遍历修改其中包含的文件、子目录以及子目录中的文件的所有权
    - ```shell
      chown -R <owner> <file>
      # chown flavio:users test.txt
      ```
-
-