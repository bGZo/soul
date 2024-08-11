tags:: #[[free-software]], #[[video]]

-
- 子程序(4)
  - ffmpeg
    collapsed:: true
    - 对媒体文件的内容进行操作，如格式转换等，是最主要的部件
  - ffplay
    collapsed:: true
    - 简易播放器，虽然没有什么UI，但是能播放各种格式的视频
  - ffprobe
    collapsed:: true
    - 探查媒体文件的属性，如meta标签等，可以选择输出JSON或XML格式
  - ffserver
    collapsed:: true
    - 流媒体服务器，不可多得的免费流媒体服务器软件，可用于架设视频直播
  - C库 --> libav
    collapsed:: true
    - 可集成到别的软件当中提供多媒体文件解码、编码等功能
    - 多媒体处理
-
- default
  - ```shell
    $ ffmpeg -i input.flv output.mp4
    ```
- video size
  - ```shell
    $ ffmpeg -i input.mp4 -s 640x360 output.mp4
    ```
- 截取
  - ```shell
    $ ffmpeg -i input.mp4 -ss 5 -t 10 output.mp4
    # 从开始解码，丢掉前 5 秒的结果
    $ ffmpeg -ss 5 -i input.mp4 -t 10 -c:v copy -c:a copy output.mp4
    # 先跳转到第 5 秒在开始解码输入视频
    # -c:v copy -c:a copy 视频与音频的编码不发生改变，直接复制
    ```
- 转图片
  - ```shell
    $ ffmpeg [-i input.mp3] -i %04d.jpg output.mp4
    $ ffmpeg -i input.mp4 %04d.jpg
    # %04d.jpg表示从1开始用0补全的4位整数为文件名的jpg文件序列
    ```
- 帧率
  - `-r`
- video crop
- video rotation
- 音频压缩
-
-
- Refs
  - [FFmpeg实用命令 - Rutenioum的记事本](https://aenes.com/post/ffmpeg.html)