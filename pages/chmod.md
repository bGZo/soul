alias:: commands/chmod
created:: [[20231217]]
icon:: ⌘
- ## Why
- ## How
  - 每个人都可以读取
    - ```shell
      chmod a+r filename
      ```
  - 每个人都可以读取和写入
    - ```shell
      chmod a+rw filename
      ```
  - 其他人（非文件所有者，也不在文件所属用户组中的用户）无法读取、写入或执行文件
    - ```shell
      chmod o-rwx filename
      ```
  - 其他人，和用户组无法读取文件
    - ```shell
      chmod og-r filename
      ```
  - 参数分类
    - 符号参数
      logseq.order-list-type:: number
      $$chmod + characters + <+/-> + <r/w/x>$$
      - characters
        id:: 6303ca6c-d6fa-4225-ba1e-14a08a320624
        - `a` 表示 *all*，即全体
        - `u` 表示 *user*，即用户
        - `g` 表示 *group*，即用户组
        - `o` 表示 *others*，即其他人
    - 数字参数
      id:: 6303c9af-98c8-4845-bfeb-f5f110b5458d
      logseq.order-list-type:: number
      - 使用数字参数速度更快，但当你不是每天都使用的话，是很难记住它们的
        - 拥有执行权限，记为 `1`
        - 拥有写入权限，记为 `2`
        - 拥有读取权限，记为 `4`
      - 这又给我们带来四种组合：
        - `0` 代表无权限
        - `1` 代表可以执行
        - `2` 代表可以写入
        - `3` 代表可以写入和执行
        - `4` 代表可以读取
        - `5` 代表可以读取和执行
        - `6` 代表可以读取和写入
        - `7` 代表可以读取、执行和写入
- ## What
  - {{iframe https://wangchujiang.com/linux-command/c/chmod.html, 400}}
    #+BEGIN_CENTER
    via: [Linux 命令搜索引擎 by wangchujiang](https://wangchujiang.com/linux-command/c/chmod.html)
    #+END_CENTER
    - `-r`
      - 递归
      - 将权限应用到该文件夹中的每个文件