alias:: 压缩
icon:: 📦
created:: 20240626

- ## Why
  - save money
    - memory
      - performance
    - bandwidth
  - encryption
  - trans easy rather then multi files
- ## How
- ## What
  - What's the **format** of compression
    collapsed:: true
    - logseq.table.version:: 2
      logseq.table.compact:: true
      logseq.table.stripes:: true
      logseq.table.max-width:: 10
      collapsed:: true
      | Name | 概括特点 | 创始人 | 备注 |
      | :--- | :--- | :--- | :--- |
      | zip | 压缩数据段 + 中央目录区 + 中央目录区尾部 | 菲尔·卡茨 | unzip |
      | gzip| GNU 计划的实现，gzip 代表 GNU zip | Jean-loup Gailly / Mark Adler |  |
      | rar | > ZIP压缩比，但压缩/解压缩速度较慢&&分卷压缩&&固实压缩&&恢复记录&&AES-128-cbc | 尤金·罗谢尔 | unrar e |
      | 7z | Max压缩比 && 开源 && AES-256加密 && 支持16EB && 多线程压缩 | - |  |
      | tar | Unix和类Unix系统上的压缩，可将多个文件合并为一个文件，打包后的文件后缀亦为“tar”。tar已经成为POSIX标准，当前是POSIX.1-2001。名字的含义是将文件备份到磁带上（tape archive） | 自由软件基金会 | tar –xvf |
      | gz | GZ是UNIX系统中的压缩文件，ZIP的Gnu版本 | gzip fileName | gzip -d或者gunzip |
      | *.bz2 | tar 打包，gzip 程序压缩的文件。数据压缩算法及程序。在1996年7月第一次公开发布了bzip2 0.15版，2000年1.0版 | Julian Seward | bzip2 -d或者用bunzip2 |
      | tar.gz | tar打包，gzip程序压缩的文件 | tar zcvf FileName.tar.gz dirName | tar –xzf（tgz） |
      | tar.xz | tar打包，xz程序压缩的文件 | tar cvJf fileName.tar.xz dirName |  |
      | tar.bz2 | tar打包，bzip2程序压缩的文件 | tar jcvf FileName.tar.bz2 dirName | tar –xjf |
      | Z | compress命令解压缩rar文件 | compress fileName | uncompress |
      | tar.Z |  |  | tar –xZf |
      - `zip` - `unzip`
        collapsed:: true
        - [菲尔·卡茨 - 维基百科，自由的百科全书](https://zh.m.wikipedia.org/zh-hans/%E8%8F%B2%E5%B0%94%C2%B7%E5%8D%A1%E8%8C%A8);
        - 文件由zip 压缩数据段、中央目录区、中央目录区尾部
      - `gzip`
        collapsed:: true
        - Jean-loup Gailly / Mark Adler
        - 通常指GNU计划的实现，gzip代表GNU zip
      - `rar` - `unrar e`
        collapsed:: true
        - 尤金·罗谢尔
        - 压缩比 \> ZIP
        - 但压缩/解压缩速度较慢
        - 分卷压缩
        - 固实压缩
        - 恢复记录
        - AES-128-cbc
      - `7z`
        collapsed:: true
        - Max压缩比
        - 开源
        - AES-256加密
        - 支持16EB
        - 多线程压缩
      - `tar` - `tar –xvf`
        collapsed:: true
        - 自由软件基金会
        - tar已经成为POSIX标准，当前是POSIX.1-2001
        - 名字的含义是将文件备份到磁带上（tape archive）
        - Unix和类Unix系统上的压缩，可将多个文件合并为一个文件，打包后的文件后缀亦为“tar”
      - `gz` - `gzip fileName` - `gzip -d / gunzip`
        collapsed:: true
        - GZ 是 UNIX系统中的压缩文件, ZIP 的 Gnu 版本
      - `bz2` - `bzip2 -d / bunzip2`
        collapsed:: true
        - Julian Seward
        - tar 打包，gzip 程序压缩的文件
        - 数据压缩算法及程序
        - 在1996年7月第一次公开发布了bzip2 0.15版，2000年1.0版
      - `tar.gz` - `tar zcvf FileName.tar.gz dirName` - `tar –xzf（tgz）`
        collapsed:: true
        - tar打包，gzip程序压缩的文件
      - `tar.xz` - `tar cvJf fileName.tar.xz dirName`
        collapsed:: true
        - tar打包，xz程序压缩的文件
      - `tar.bz2` - `tar jcvf FileName.tar.bz2 dirName` - `tar –xjf`
        collapsed:: true
        - tar打包，bzip2程序压缩的文件
      - `Z` - `compress fileName` - `uncompress`
        collapsed:: true
        - compress 命令解压缩 rar 文件
      - `tar.Z` - `tar –xZf`
    -
    -
    -
    -
    -
-