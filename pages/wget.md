icon:: ⌘
created:: [[20230703]]
description:: Linux系统下载文件工具
type:: command/linux

- ## Why
- ## How
- ## What
  - {{iframe https://wangchujiang.com/linux-command/c/wget.html,40vh,iframe-radius}}
    - ==wget非常稳定，它在带宽很窄的情况下和不稳定网络中有很强的适应性，如果是由于网络的原因下载失败，wget会不断的尝试，直到整个文件下载完毕。如果是服务器打断下载过程，它会再次联到服务器上从停止的地方继续下载。这对从那些限定了链接时间的服务器上下载大文件非常有用。==
      - TODO 如何复现这个应用场景？
    - **镜像网站**：`--mirror`
      - ```
        wget --mirror -p --convert-links -P ./LOCAL URL
        ```
        - `--miror`开户镜像下载。
        - `-p`下载所有为了html页面显示正常的文件。
        - `--convert-links`下载后，转换成本地的链接。
        - `-P ./LOCAL`保存所有文件和目录到本地指定目录。
-