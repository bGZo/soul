alias:: 插帧, 补帧,  motion-compensated frame interpolation, MCFI
mark::  a form of video processing in which intermediate animation frames are generated between existing ones by means of interpolation, in an attempt to make animation more fluid, to compensate for display motion blur, and for fake slow motion effects.
tags:: #Video 

date:: 20230717
title:: motion interpolation
wikipedia:: [Motion interpolation - Wikipedia](https://en.wikipedia.org/wiki/Motion_interpolation)

- ## Why
  - Play the video smoothly.
- ## How
  - How to use motion interpolation application?
    collapsed:: true
    - [PotPlayer Motion Interpolation · GitHub](https://gist.github.com/edjdavid/8ad0445042c4ca4fa66e4055f2cbfc3b)
      - DONE [最简单的播放视频插值补帧方案 Potplayer + Avisynth 实现 24FPS -> 60FPS - V2EX](https://www.v2ex.com/t/861809)
        id:: 64af60c3-88da-49b4-8500-4e3803f1d31f
      - PotPlayer + AviSynth+ (with vcredist) + [pinterf/mvtools: mvtools plugin for avisynth (github.com)](https://github.com/pinterf/mvtools)
        - [Hall of Shame (ffmpeg.org)](https://ffmpeg.org/shame.html)
        - [PotPlayer快捷键大全 快捷键一览表 - PotPlayer中文网 (potplayercn.com)](http://www.potplayercn.com/course/2926.html)
          collapsed:: true
          - | **快捷键** | **功能** |
            | " | 播放->跳略播放->跳略播放 开|关 |
            | ' | 播放->跳略播放->跳略播放设置... |
            | , | 字幕->字幕同步(帧率)->滞后0.5 秒 |
            | Alt + , | 字幕->字幕同步(帧率)->滞后50 秒 |
            | . | 字幕->字幕同步(帧率)->超前0.5 秒 |
            | Alt + . | 字幕->字幕同步(帧率)->超前50 秒 |
            | / | 字幕->字幕同步(帧率)->复位 |
            | < | 字幕->字幕同步(帧率)->滞后0.5 秒 |
            | > | 字幕->字幕同步(帧率)->超前0.5 秒 |
            | [ | 播放->AB 区段循环->设定起点 |
            | Alt + [ | 播放->AB 区段循环->将起点步进 0.1 秒 |
            |   | 播放->AB 区段循环->区段循环 开|关 |
            | Alt + | 播放->AB 区段循环->当前章节/标记/书签 区段循环 |
            | ] | 播放->AB 区段循环->设定止点 |
            | Alt + ] | 播放->AB 区段循环->将止点步进 0.1 秒 |
            | ` | 屏幕->迷你尺寸 |
            | { | 播放->AB 区段循环->解除起点 |
            | } | 播放->AB 区段循环->解除止点 |
            | Backspace | 播放->定位->重新开始 |
            | Shift + Backspace | 播放->定位->结束前30秒 |
            | Ctrl + Backspace | 播放->定位->中段 |
            | Alt + Backspace | DVD->标题菜单 |
            | Tab | 配置/语言/其他->OSD信息 |
            | Shift + Tab | 配置/语言/其他->简要信息 |
            | Enter | 屏幕->全屏 |
            | Ctrl + Enter | 屏幕->全屏+(拉伸) |
            | Ctrl + Shift + Enter | 屏幕->全屏(其他显示器) |
            | Alt + Enter | 屏幕->全屏 |
            | Ctrl + Alt + Enter | 屏幕->全屏+(保持比例) |
            | Space | 播放->播放|暂停 |
            | PgUp | 电视->下一频道 |
            | Shift + PgUp | 上一 书签/章节 |
            | Ctrl + PgUp | 电视->前一收看频道 |
            | Alt + PgUp | 字幕->字幕样式->字体 + |
            | PgDn | 电视->上一频道 |
            | Shift + PgDn | 下一 书签/章节 |
            | Ctrl + PgDn | 电视->后一收看频道 |
            | Alt + PgDn | 字幕->字幕样式->字体 - |
            | End | 播放->定位->下一对白 |
            | Home | 播放->定位->上一对白 |
            | Ctrl + Home | 播放->定位->当前字幕起点 |
            | Alt + Home | 字幕->字幕样式->复位 |
            | ← | 播放->定位->步退5 秒 |
            | Shift + ← | 播放->定位->步退1 分 |
            | Ctrl + ← | 播放->定位->步退30 秒 |
            | Ctrl + Shift + ← | 播放->定位->上一关键帧 |
            | Alt + ← | 字幕->字幕样式->左移 |
            | Ctrl + Alt + ← | 播放->定位->步退5 分 |
            | ↑ | 声音->音量 + |
            | Shift + ↑ | 声音->播放音量控制->主音量 + |
            | Alt + ↑ | 字幕->字幕样式->上移 |
            | Ctrl + Alt + ↑ | 声音->系统音量->波形音量 + |
            | Ctrl + Alt + Shift + ↑ | 声音->系统音量->主音量 + |
            | → | 播放->定位->步进5 秒 |
            | Shift + → | 播放->定位->步进1 分 |
            | Ctrl + → | 播放->定位->步进30 秒 |
            | Ctrl + Shift + → | 播放->定位->下一关键帧 |
            | Alt + → | 字幕->字幕样式->右移 |
            | Ctrl + Alt + → | 播放->定位->步进5 分 |
            | ↓ | 声音->音量 - |
            | Shift + ↓ | 声音->播放音量控制->主音量 - |
            | Alt + ↓ | 字幕->字幕样式->下移 |
            | Ctrl + Alt + ↓ | 声音->系统音量->波形音量 - |
            | Ctrl + Alt + Shift + ↓ | 声音->系统音量->主音量 - |
            | Insert | 电视->最后收看频道 |
            | Ctrl + Insert | 收藏->添加当前文件夹 |
            | Alt + Insert | 收藏->添加当前文件 |
            | Delete | 电视->跳转至指定频道... |
            | Shift + Delete | 播放->播放列表->删除->删除文件 |
            | Ctrl + Shift + Delete | 播放->播放列表->删除->删除文件(+字幕) |
            | 0 | 屏幕->自定义尺寸设置... |
            | 1 | 屏幕->半倍屏 |
            | Alt + 1 | 屏幕->显示器 30% 尺寸 |
            | 2 | 屏幕->1 倍屏 |
            | Alt + 2 | 屏幕->显示器 45% 尺寸 |
            | 3 | 屏幕->1.5 倍屏 |
            | Alt + 3 | 屏幕->显示器 60% 尺寸 |
            | 4 | 屏幕->2.0 倍屏 |
            | Alt + 4 | 屏幕->显示器 75% 尺寸 |
            | 5 | 屏幕->最大化 |
            | 6 | 屏幕->最大化|还原 |
            | 7 | 屏幕->最大化+(过任务栏)|还原 |
            | 8 | 屏幕->无边框尺寸 |
            | 9 | 屏幕->自定义尺寸 |
            | A | 声音->选择声音 |
            | Shift + A | 声音->声音处理->语音增强 |
            | Alt + A | 声音->选择声音->按序切换声音 |
            | Ctrl + Alt + A | 配置/语言/其他->收尾处理->依次切换收尾方式 |
            | Ctrl + B | 视频->图像处理->软模糊 |
            | Alt + B | 字幕->字幕样式->粗体 |
            | Ctrl + Alt + B | 视频->下边距->按序切换边距 |
            | C | 播放->播放速度->加速 + |
            | Shift + C | 声音->声音处理->晶化 |
            | Ctrl + C | 视频->图像截取->复制当前源画面 |
            | Alt + C | 视频->视频录制->录制视频... |
            | Ctrl + Alt + C | 视频->图像截取->复制当前实画面 |
            | D | 播放->定位->上一帧 |
            | Shift + D | 声音->声音处理->降噪 |
            | Ctrl + D | 打开->DVD 设备 |
            | Alt + D | 打开->设备设置... |
            | Ctrl + Alt + D | 打开->蓝光设备 |
            | E | 视频->亮度 +1% |
            | Shift + E | 声音->均衡器 |
            | Ctrl + E | 视频->图像截取->截存当前源画面 |
            | Alt + E | 字幕->字幕浏览器... |
            | Ctrl + Alt + E | 视频->图像截取->截存当前实画面 |
            | F | 播放->定位->下一帧 |
            | Ctrl + F | 滤镜->滤镜/解码器管理... |
            | Alt + F | 字幕->字幕样式->字体设置... |
            | G | 播放->定位->手动定位... |
            | Shift + G | 声音->音轨->声音录制... |
            | Ctrl + G | 视频->图像截取->连续截图... |
            | Alt + G | 电视->频道控制->频道管理... |
            | H | 播放->章节/书签 |
            | Shift + H | 声音->音调->低音 |
            | Ctrl + H | 视频->图像处理->去块(提高画质) |
            | Alt + H | 字幕->显示字幕 |
            | I | 视频->色彩度 -1% |
            | Ctrl + I | 视频->反交错->切换反交错方式 |
            | J | 视频->3D 视频输出 |
            | Shift + J | 声音->音调->高音 |
            | Ctrl + J | 打开->摄像头/其他设备 |
            | K | 视频->图像截取 |
            | Shift + K | 声音->音调->默认音调 |
            | Ctrl + K | 打开->数字 TV(BDA 设备) |
            | Alt + K | 视频->图像旋转->按序选择旋转方式 |
            | L | 字幕->选择字幕 |
            | Shift + L | 配置/语言/其他->语言 |
            | Ctrl + L | 视频->图像处理->电平控制 |
            | Alt + L | 字幕->选择字幕->依次选择字幕 |
            | M | 声音->静音 |
            | Ctrl + M | 视频->图像处理->瞬态降噪 |
            | Ctrl + Alt + M | 声音->系统音量->静音 |
            | Ctrl + Alt + Shift + M | 声音->系统音量->静音 |
            | N | 电视->频道控制 |
            | Shift + N | 声音->声音处理->规格化 |
            | Ctrl + N | 视频->图像处理->3D 降噪 |
            | Alt + N | 视频->图像截取->创建缩略图... |
            | O | 视频->色彩度 +1% |
            | Ctrl + O | 打开->打开文件... |
            | Alt + O | 打开->打开字幕... |
            | P | 添加书签 |
            | Shift + P | 视频->像素着色->调整尺寸前的着色切换 |
            | Ctrl + P | 视频->图像处理->上下翻转 |
            | Alt + P | 字幕->手动输入字幕... |
            | Ctrl + Alt + P | 视频->像素着色->调整尺寸后的着色切换 |
            | Q | 视频->图像属性复位 |
            | Ctrl + Q | 视频->裁剪/拉伸->图像缩放设置... |
            | R | 视频->对比度 -1% |
            | Shift + R | 声音->声音处理->混响 |
            | Ctrl + R | 视频->图像处理->锐化 |
            | S | 视频->像素着色 |
            | Ctrl + S | 打开->采集器 |
            | Ctrl + Shift + S | 字幕->保存字幕->按影片名称保存 |
            | Alt + S | 字幕->保存字幕->回写SMI字幕 |
            | Ctrl + Alt + S | 字幕->保存字幕->另存字幕为... |
            | T | 视频->对比度 +1% |
            | Shift + T | 声音->声音处理->左右声道互换 |
            | Ctrl + T | 配置/语言/其他->置顶方式->切换最前端 |
            | U | 视频->饱和度 +1% |
            | Ctrl + U | 打开->打开链接... |
            | V | 视频->选择图像 |
            | Shift + V | 声音->声音处理->语音消除 |
            | Ctrl + V | 打开->打开剪贴板 |
            | Alt + V | 视频->选择图像->图像顺序选择 |
            | W | 视频->亮度 -1% |
            | Ctrl + W | 打开->模拟TV |
            | X | 播放->播放速度->减速 - |
            | Shift + X | 声音->开启声音处理滤镜 |
            | Ctrl + X | 视频->图像处理滤镜->依次切换图像处理滤镜 |
            | Y | 视频->饱和度 -1% |
            | Ctrl + Y | 打开->重开当前/最后文件 |
            | Ctrl + Alt + Y | 打开->重载字幕 |
            | Z | 播放->播放速度->正常/之前的速度 |
            | Shift + Z | 播放->定位->时间场景浏览... |
            | Ctrl + Z | 视频->图像处理->左右翻转 |
            | Alt + Z | 播放->定位->章节/书签场景浏览... |
            | Numpad 0 | 帧位->预置->选择预置顺序 |
            | Numpad 1 | 帧位->全帧 - |
            | Ctrl + Alt + Numpad 1 | 屏幕->窗口定位->置于 ↙ |
            | Numpad 2 | 帧位->帧高 - |
            | Ctrl + Numpad 2 | 帧位->偏移 ↓ |
            | Alt + Numpad 2 | 字幕->字幕样式->上下边距 - |
            | Ctrl + Alt + Numpad 2 | 屏幕->窗口定位->位移 ↓ |
            | Ctrl + Alt + Numpad 3 | 屏幕->窗口定位->置于 ↘ |
            | Numpad 4 | 帧位->帧宽 - |
            | Ctrl + Numpad 4 | 帧位->偏移 ← |
            | Alt + Numpad 4 | 字幕->字幕样式->左右边距 - |
            | Ctrl + Alt + Numpad 4 | 屏幕->窗口定位->位移 ← |
            | Numpad 5 | 帧位->帧位 之前/复位 |
            | Ctrl + Numpad 5 | 帧位->帧位居中 |
            | Ctrl + Alt + Numpad 5 | 屏幕->窗口定位->外框居中 |
            | Numpad 6 | 帧位->帧宽 + |
            | Ctrl + Numpad 6 | 帧位->偏移 → |
            | Alt + Numpad 6 | 字幕->字幕样式->左右边距 + |
            | Ctrl + Alt + Numpad 6 | 屏幕->窗口定位->位移 → |
            | Ctrl + Alt + Numpad 7 | 屏幕->窗口定位->置于 ↖ |
            | Numpad 8 | 帧位->帧高 + |
            | Ctrl + Numpad 8 | 帧位->偏移 ↑ |
            | Alt + Numpad 8 | 字幕->字幕样式->上下边距 + |
            | Ctrl + Alt + Numpad 8 | 屏幕->窗口定位->位移 ↑ |
            | Numpad 9 | 帧位->全帧 + |
            | Ctrl + Alt + Numpad 9 | 屏幕->窗口定位->置于 ↗ |
            | Add | 帧位->全帧 + |
            | Ctrl + Alt + Add | 屏幕->窗口 + |
            | Subtract | 帧位->全帧 - |
            | Ctrl + Alt + Subtract | 屏幕->窗口 - |
            | F1 | 关于... |
            | Ctrl + F1 | 属性... |
            | Ctrl + Alt + F1 | 直播->采集器I |
            | F2 | 打开->打开文件夹... |
            | Ctrl + Alt + F2 | 直播->采集器II |
            | F3 | 打开文件... |
            | Ctrl + Alt + F3 | 直播->采集器I开始 |
            | F4 | 关闭 |
            | Ctrl + Alt + F4 | 直播->采集器II开始 |
            | F5 | 选项... |
            | Ctrl + F5 | 比例->依次切换比例模式 |
            | Ctrl + Alt + F5 | 直播->采集设置... |
            | F6 | 列表... |
            | Ctrl + F6 | 比例->依次切换比例 |
            | F7 | 控制... |
            | F9 | 直播->聊天/浏览器... |
            | F12 | 打开->简索->简索文件... |
            | Ctrl + F12 | 打开->简索->简索菜单... |
            | Alt + F12 | 打开->打开远程连接... |
            | Scroll Lock | 配置/语言/其他->播放信息 |
            | Shift + , | 声音->声音匹配(同步)->滞后 0.05 秒 |
            | Ctrl + , | 字幕->字幕同步(帧率)->滞后5 秒 |
            | Ctrl + Alt + , | 字幕->字幕同步(帧率)->上一字幕同步 |
            | Shift + . | 声音->声音匹配(同步)->超前 0.05 秒 |
            | Ctrl + . | 字幕->字幕同步(帧率)->超前5 秒 |
            | Ctrl + Alt + . | 字幕->字幕同步(帧率)->下一字幕同步 |
            | Shift + / | 声音->声音匹配(同步)->复位 |
            | B | 播放->AB 区段循环 |
            | [ | 播放->AB 区段循环->设定起点 |
            | Shift + [ | 播放->AB 区段循环->解除起点 |
            | Ctrl + [ | 播放->AB 区段循环->将起点步退 0.1秒 |
            | Alt + [ | 播放->AB 区段循环->将起点步进 0.1 秒 |
            | ] | 播放->AB 区段循环->设定止点 |
            | Shift + ] | 播放->AB 区段循环->解除止点 |
            | Ctrl + ] | 播放->AB 区段循环->将止点步退 0.1秒 |
            | Alt + ] | 播放->AB 区段循环->将止点步进 0.1 秒 |
            | Ctrl + Alt + [ | 播放->AB 区段循环->将循环区步退 0.1秒 |
            | Ctrl + Alt + ] | 播放->AB 区段循环->将循环区步进 0.1秒 |
            | Ctrl + Alt + + | 播放->AB 区段循环->减少区段循环次数 |
            | Ctrl + Alt + = | 播放->AB 区段循环->增加区段循环次数 |
            | Ctrl + - | 播放->AB 区段循环->上一字幕区段循环 |
            | Ctrl + \ 或 Insert | 播放->AB 区段循环->循环当前字幕 |
            | Ctrl + = | 播放->AB 区段循环->下一字幕区段循环 |
            | Alt + - | 播放->AB 区段循环->上一章节/标记/书签 区段循环 |
            | Alt + \ | 播放->AB 区段循环->当前章节/标记/书签 区段循环 |
            | Alt + = | 播放->AB 区段循环->下一章节/标记/书签 区段循环 |
            | Ctrl + \ | 播放->AB 区段循环->快速区段循环(5 秒) |
            | \ | 播放->AB 区段循环->区段循环 |
            | Shift + \ | 播放->AB 区段循环->编辑AB区段循环列表 |
        - [PotPlayer Motion Interpolation (github.com)](https://gist.github.com/edjdavid/8ad0445042c4ca4fa66e4055f2cbfc3b)
          collapsed:: true
          - ```
            Preferences
              -> Filter Control
                -> Video Decoder
                  -> Built-in Video Codec/DXVA Settings
                    -> Use DXVA
                      -> Checked
                    -> DXVA2 Copy-Back
                      -> Select D311 with the GPU
              -> Avisynth
                -> Enable AviSynth processing
                  -> Checked
                -> Add "potplayer_source()"
                  -> Checked
                -> Leave other checkboxes on default
                -> Load Script
                  -> Select or copy the avs script below
            ```
          - ```
            SetMemoryMax(512)
            SetFilterMTMode("DEFAULT_MT_MODE", 2)
            SetFilterMTMode("FFVideoSource", 3)
            potplayer_source()
            LoadPlugin("C:\Program Files (x86)\AviSynth+\plugins64\mvtools2.dll")
            super=MSuper(pel=1, hpad=0, vpad=0)
            backward_1=MAnalyse(super, chroma=false, isb=true, blksize=32, blksizev=32, searchparam=3, plevel=0, search=3, badrange=(-24))
            forward_1=MAnalyse(super, chroma=false, isb=false, blksize=32, blksizev=32, searchparam=3, plevel=0, search=3, badrange=(-24))
            backward_2 = MRecalculate(super, chroma=false, backward_1, blksize=8, blksizev=8, searchparam=0, search=3)
            forward_2 = MRecalculate(super, chroma=false, forward_1, blksize=8, blksizev=8, searchparam=0, search=3)
            MBlockFps(super, backward_2, forward_2, num=60, den=1, mode=2)
            Prefetch(4)
            ```
    - [PotPlayer RePack - 4 типа сборок программы](https://potplayer.club/repack.html)
      collapsed:: true
      - 我直接用 7sh3 封裝版，內建 SVP 補幀
    - [完美解码官方网站 (wmzhe.com)](https://jm.wmzhe.com/)
    - [hooke007/MPV_lazy: 🔄 mpv player 播放器折腾记录 windows conf ； 中文注释配置 快速帮助入门 ； mpv-lazy 懒人包 win10 x64 config (github.com)](https://github.com/hooke007/MPV_lazy)
    - [Get – SVP – SmoothVideo Project (svp-team.com)](https://www.svp-team.com/get/)
    - https://www.bilibili.com/video/BV1V7411A7Th
    - [PotPlayer 篇七：享受丝质顺滑，PotPlayer播放器的几种补帧方法介绍和用法_软件应用_什么值得买 (smzdm.com)](https://post.smzdm.com/p/amxzgzwv/)
- ## What
  - See also
    - [Inbetweening](https://en.wikipedia.org/wiki/Inbetweening)
    - [Motion compensation](https://en.wikipedia.org/wiki/Motion_compensation)
    - [Motion interpolation (computer graphics)](https://en.wikipedia.org/wiki/Motion_interpolation_(computer_graphics))
    - [Flicker-free](https://en.wikipedia.org/wiki/Flicker-free)
    - [Television standards conversion](https://en.wikipedia.org/wiki/Television_standards_conversion)
    - [3:2 pulldown](https://en.wikipedia.org/wiki/3:2_pulldown)
-
-