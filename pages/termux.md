also:: android/app/termux
changelog:: https://github.com/termux/termux-app/releases

-
- Changelog
  - 0.90及以上 版本需要 Android7.0 及以上版本的系统. 此安装包由 F-Droid 编译并签名, 且保证与此源代码 tarball 保持一致.
-
- TODO 模拟 Ubuntu (获取ROOT)
  - tmoe https://gitee.com/mo2/linux
-
- 添加环境变量 via: https://v2ex.com/t/741093#;
  - ```
        export PATH=/data/data/com.termux/files/usr/bin:/data/data/com.termux/files/usr/bin/applets:$PATH
        export LD_LIBRARY_PATH=/data/data/com.termux/files/usr/lib
    ```
-
- Libs
  - `libwebp` ->`cwebp` 压缩图片 via https://blog.dsrkafuu.su/post/2020/libwebp-docs-cwebp
    - tool/commandline, tool/cl, cl
-
- LATER 模拟 Ubuntu (获取ROOT)
  - tmoe https://gitee.com/mo2/linux
- 添加环境变量 via: https://v2ex.com/t/741093#;
  - ```
        export PATH=/data/data/com.termux/files/usr/bin:/data/data/com.termux/files/usr/bin/applets:$PATH
        export LD_LIBRARY_PATH=/data/data/com.termux/files/usr/lib
    ```
- Libs
  - `libwebp` ->`cwebp` 压缩图片 via https://blog.dsrkafuu.su/post/2020/libwebp-docs-cwebp
    - https://github.com/PicGo/flutter-picgo 上传图片
- History
  - ```shell
    sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-packages-24 stable main@' $PREFIX/etc/apt/sources.list sed -i 's@^\(deb.*games stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/game-packages-24 games stable@' $PREFIX/etc/apt/sources.list.d/game.list sed -i 's@^\(deb.*science stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/science-packages-24 science stable@' $PREFIX/etc/apt/sources.list.d/science.list apt update && apt upgrade
    #then install vim
    vim $PREFIX/etc/apt/sources.list.d/game.list
    deb https://mirrors.tuna.tsinghua.edu.cn/termux/game-packages-24 games stable
    vim $PREFIX/etc/apt/sources.list.d/science.list
    deb https://mirrors.tuna.tsinghua.edu.cn/termux/science-packages-24 science stable
    vim $PREFIX/etc/apt/sources.list
    deb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-packages-24 stable main
    # refer to https://mirrors.tuna.tsinghua.edu.cn/help/termux/
    termux-setup-storage
    # acquire the access of storage
    ```
-