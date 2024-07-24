also:: commands/cut
-
-
- **Cases**
  - 拿到文件的后缀
    - ```shell
      basename $file | rev | cut -d . -f 1- | rev
      ```
    -