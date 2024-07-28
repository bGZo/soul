icon:: 🛠
created:: [[20230127]]
document:: https://www.billfish.cn/category/knowledge, https://www.billfish.cn/download, https://www.billfish.cn/bbs
exclude-from-graph-view:: true
status:: tool/deprecated
tags:: #font #photo
type:: tool

- #+BEGIN_TIP
  软件其实有一个更好的 Geek 思路
  #+END_TIP
  - 就是像我一样创建一个动态链接, 然后直接在父文件夹中进行管理
  - 官方提供的索引是对每个文件取链接, 但是那样对文件的管理就转变成了索引的管理, 并且存在同步(源文件是否可以移动?), 失效(删除的索引怎么办?)的问题;
    - > Billfish索引方式，是将原文件的快捷方式创建在素材库文件夹内。从而实现快速查找。通过索引导入的文件在素材库内是.lnk文件
      via: [如何正确使用索引方式 - Billfish素材管理工具](https://www.billfish.cn/knowledge/why-lose-1/);
- ## 我的初衷
  - Just view picture quickly; I could manage well using directory;
- ## 文件存储
  - Billfish素材库文件夹有两部分内容：
    via: [Billfish如何存储素材文件 - Billfish素材管理工具](https://www.billfish.cn/knowledge/billfish-cunchu/)
    - 1、用户个人素材文件；
      - 存储在素材库文件夹内的个人素材；
    - 2、素材库信息记录文件夹: .bf
      - 记录用户的素材库信息记录文件包含：
        - 素材标识信息颜色，缩略图等一系列信息。
        - 删除或编辑该文件夹内容将导致素材库异常
  - ```
    /mnt/c/Users/15517/Desktop/billfish/.bf > ll
    total 37M
    drwxrwxrwx 1 bgzocg bgzocg  512 Jan 27 15:05 ./
    drwxrwxrwx 1 bgzocg bgzocg  512 Jan 27 10:59 ../
    lrwxrwxrwx 1 bgzocg bgzocg   40 Jan 27 11:15 .backup -> /mnt/e/OneDrive/resource/backup_billfish/
    drwxrwxrwx 1 bgzocg bgzocg  512 Oct 25 18:31 .preview/
    drwxrwxrwx 1 bgzocg bgzocg  512 Jan 27 14:54 .recycle/
    drwxrwxrwx 1 bgzocg bgzocg  512 Jan 27 14:54 .recycle2/
    drwxrwxrwx 1 bgzocg bgzocg  512 Jan 27 15:05 .temp/
    drwxrwxrwx 1 bgzocg bgzocg  512 Oct 25 18:30 .ui_config/
    -rwxrwxrwx 1 bgzocg bgzocg  25M Jan 27 15:05 billfish.db*
    -rwxrwxrwx 1 bgzocg bgzocg 163K Jan 15  2022 folder.ico*
    -rwxrwxrwx 1 bgzocg bgzocg  13M Jan 27 14:54 summary_v2.db*
    ```
  - 有几点有趣的发现
    - 文件不会最终删除, 删除两次的文件在  `.recycle2` 中, 需要三次删除;
    - TODO 软件生成缓存的方式是 `cwebp`, 存放在 `.preview` 中, 文件存放格式和 Git 很相似, 我应该搞清楚这是怎么做的...
      - 32G -> 2G
      - 每个文件不大, 但是数量和素材成正比, 所以该素材文件才不适合用 Onedrive 同步;
    - 数据库文件 `billfish.db` 存储素材和用户数据
      - TODO 但是不知道为什么数据库只增不减, 并不清楚数据库中详细条目的占用情况, 有时间优化下;
    - `.backup` 中备份自己的两个数据库, 所以我只把这部分取动态链接到 Onedrive 同步了, 但要时常主义该备份是否可用, 因为上一次就是因为备份失效了, 才导致我努力了好多天, 花巨大精力维护的数据库直接没了 😭
      - via: 上一次 -> ((63d1f165-74a3-4cf6-b656-3a46700c6dd8))
-