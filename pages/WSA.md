alias:: Windows Subsystem for Android
tags:: #Windows #android
alternatives:: [[samsung/dex]]
created:: [[20230823]]

- ## Why
- ## How
  #+BEGIN_NOTE
  The most of issues here is about [[adb]] problem.
  #+END_NOTE
  - [Any idea on using a proxy?](https://github.com/WSA-Community/WSAGAScript/issues/131) #proxy
    id:: 64e5f8f2-7901-46a2-a719-dbc03af14363
    - ```shell
      adb connect 127.0.0.1:58526 && adb shell "settings put global http_proxy ``ip route list match 0 table all scope global | cut -F3``:7890"
      ```
    - [Windows Android 子系统 WSA 代理设置方法教程 — 秋风于渭水 (tjsky.net)](https://www.tjsky.net/tutorial/391)
    - [Android device: set Wifi Proxy with ADB command | by Andres Sandoval | Medium](https://andresand.medium.com/android-device-set-wifi-proxy-with-adb-command-7a2f8cf4c434)
    - [Win11 安卓子系统VirtWifi无法访问网络_virtwifi已连接,但无法访问互联网_被闲置的鱼的博客-CSDN博客](https://blog.csdn.net/qq_14902731/article/details/124891739)
  - [How to use adb command to push a file on device without sd card](https://stackoverflow.com/questions/20834241/how-to-use-adb-command-to-push-a-file-on-device-without-sd-card)
    collapsed:: true
    - ```cmd
      adb connect 127.0.0.1:58526
      adb install application.apk
      adb push file_path /storage/emulated/0/Download
      ```
  - [How to install xapk, apks, or multiple-apks via adb?](https://android.stackexchange.com/questions/221204/how-to-install-xapk-apks-or-multiple-apks-via-adb)
    id:: 64955cce-c045-4f84-bccb-253cc0fd23e7
    collapsed:: true
    - ```
       .\adb install-multiple ..\Snipd_2.2.24\base.apk ..\Snipd_2.2.24\split_config.arm64_v8a.apk ..\Snipd_2.2.24\split_config.en.apk ..\Snipd_2.2.24\split_config.ja.apk ..\Snipd_2.2.24\split_config.xxhdpi.apk ..\Snipd_2.2.24\split_config.zh.apk
      ```
  - [APK installation failed: [INSTALL_FAILED_VERIFICATION_FAILURE]](https://stackoverflow.com/questions/15014519/apk-installation-failed-install-failed-verification-failure)
    id:: 64955cce-0168-4c61-87ff-259d0e252437
    collapsed:: true
    - ```
      adb shell settings put global verifier_verify_adb_installs 0
      adb shell settings put global package_verifier_enable 0
      ```
- ## What
  - Alternatives for GPlay/Su care
    collapsed:: true
    - [MustardChef/WSABuilds: Run Windows Subsystem For Android on your Windows 10 and Windows 11 PC using prebuilt binaries with Google Play Store (OpenGApps/ MindTheGapps) and/or Magisk or KernelSU (root solutions) built in. (github.com)](https://github.com/MustardChef/WSABuilds)
  - Applications collection:
    collapsed:: true
    - [微信读书](https://weread.qq.com/web/redirect?from=NavBar)
    - [Download | Tachiyomi](https://tachiyomi.org/download/)
  - [在 Windows 上运行 Andriod 应用：WSA 安装说明 - sysin](https://sysin.org/blog/wsa-install/)