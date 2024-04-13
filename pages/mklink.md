alias:: commands/cmd/mklink
tags:: TODO

  - same as [[commands/ln]] in [[-nix]]
-
- WAITING Onedrive don't support symbolic link to snyc data, wait for it Or chose other plugin/substitute
  collapsed:: true
  - via [OneDrive not syncing files inside symbolic links : onedrive](https://www.reddit.com/r/onedrive/comments/amq38m/onedrive_not_syncing_files_inside_symbolic_links/) & [Why do all my symbolic links always have the blue "Sync pending" icon? : onedrive](https://www.reddit.com/r/onedrive/comments/k82lav/why_do_all_my_symbolic_links_always_have_the_blue/)
- WAITING 为什么 linux 与 windows 软链接底层兼容？ / 通用?
  collapsed:: true
  - [如何实现linux与windows软链接底层兼容？ - SegmentFault 思否](https://segmentfault.com/q/1010000007544629)
  -
-
- ![image.png](../assets/command/image_1648108822570_0.png){:height 113, :width 779} #a-picture-is-worth-a-thousand-words
  - ```shell
    # cmd administrator via: - https://answers.microsoft.com/en-us/windows/forum/windows_10-files/mklink-not-recognized/b388d6f5-13ac-4ef1-8860-ca35783c8dfc
    MKLINK [[/D] | [/H] | [/J]] Link Target
            /D      Creates a directory symbolic link.  Default is a file
                    symbolic link.
            /H      Creates a hard link instead of a symbolic link.
            /J      Creates a Directory Junction.
            Link    Specifies the new symbolic link name.
            Target  Specifies the path (relative or absolute) that the new link
                    refers to.
    ```
    - `hard link` #vs `symbolic link` #vs `soft link / junction`
      id:: 623c25ff-70ad-4030-8de6-eee1e2d4f22a
      - More via [[os/file-system]]
      - `hard link`
        id:: 623c28d0-3a10-40de-a9a9-c25de29fa936
        - 局限
          - **只用于文件**, 无法链接到目录
          - **只建立在同一分区内的文件指向**, 链接到外部文件系统（磁盘驱动器）
            - WAITING linux 主要分区就一个好吗? 基本就完全不起作用呗...
          - **不跨系统**
            - 每个文件系统都有各自的 inode 数据结构和列表
            - via: [[os/file-system]]
          - **不允许对空文件建立链接**
      - ↓ More Powerful
      - `Junction` vs `symbolic link`
        - 远端连接
          - junction point: `\\Alice\c$\myjp` -> `\\Alice\c$\targetfolder`
          - symbolic link: `\\Alice\c$\mysymlink` -> `\\Bob\c$\targetfolder`
        - `soft link / junction` 建立时会自动引用原文件（或目录）的绝对路径，而 `symbolic link` 允许相对路径的引用
      - 删除文件时
        - `hard link`: 源文件和链接文件一起删除
          - 多个目录项都是指向一个 inode，那么只有删除文件的所有硬链接以及源文件时，系统才会彻底删除该文件
        - `symbolic link` vs `soft link / junction`: 删除链接文件, 源文件不变; 源文件删除, 链接文件变为无用链接.
          id:: 623c2b0b-28cd-47aa-9e0d-2357d066b40d
      - ![image.png](../assets/command/image_1668418659313_0.png)
    - More Via
      - [symlink - Creating hard and soft links using PowerShell - Stack Overflow](https://stackoverflow.com/questions/894430/creating-hard-and-soft-links-using-powershell)
      - [windows - "directory junction" vs "directory symbolic link"? - Super User](https://superuser.com/questions/343074/directory-junction-vs-directory-symbolic-link)
      - [unix - What is the difference between a symbolic link and a hard link? - Stack Overflow](https://stackoverflow.com/questions/185899/what-is-the-difference-between-a-symbolic-link-and-a-hard-link)
      - [Hard vs Soft Links in Linux (Linux Links) - YouTube](https://www.youtube.com/watch?v=4-vye3QFTFo)
    - The `mklink` is s built-in to the Command Prompt (cmd.exe). It can't run directly from PowerShell. So should run cmd under admin. see help:
      - https://answers.microsoft.com/en-us/windows/forum/windows_10-files/mklink-not-recognized/b388d6f5-13ac-4ef1-8860-ca35783c8dfc?auth=1
      - https://blog.csdn.net/qq_37861937/article/details/79064841