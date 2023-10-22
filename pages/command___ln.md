title:: command/ln
tags::

- On [[Windows]] its called [[mklink]]
-
- hard link
  - ```shell
    # ln <源文件路径> <链接路径>
    ln recipes.txt newrecipes.txt
    ```
- soft link
  - ```shell
    # ln -s <源文件路径> <链接路径>
    ln -s recipes.txt newrecipes.txt
    ```
-
-