alias:: Windows package manager cli
tags:: #Windows #tools, #scoop
github:: [microsoft/winget-cli](https://github.com/microsoft/winget-cli)
released-created:: [[20200514]]
created:: [[20230512]]
![](https://img.shields.io/github/stars/microsoft/winget-cli)

- #+BEGIN_WARNING
  winget cannot switch multi versions of app[^version]
  #+END_WARNING
- ## Consists
  - 仓库：[GitHub - microsoft/winget-pkgs: The Microsoft community Windows Package Manager manifest repository](https://github.com/microsoft/winget-pkgs)
  - 客户端：[GitHub - microsoft/winget-cli: Windows Package Manager CLI (aka winget)](https://github.com/microsoft/winget-cli)
    - [Releases · microsoft/winget-cli · GitHub](https://github.com/microsoft/winget-cli/releases)
-
- ## References
  - [^version]: 就算是允许多版本安装 Python，也都是安装在 `$LOCALAPPDATA\Programs\Python\PythonXX` 下，但是本身的环境变量没有办法方便的修改(via： [Can winget install an older version of Python? - Stack Overflow](https://stackoverflow.com/questions/70281103/can-winget-install-an-older-version-of-python))，所以相当鸡肋。只适用于 #.ol
    - 微软已登录用户？
      - Github 安装的版本可以绕过这个限制吗？
    - 一些没有被墙的源（如 winget 源的 Google.PlatformTools，碍于无法使用代理，并且需要从 Google 官方那里拉取软件，所以基本已报错收尾）
      id:: 645f8f88-c973-44da-8e08-41f71bd3e2d2
      - ```
        An unexpected error occurred while executing the command:
        InternetOpenUrl() failed.
        0x80072efd : unknown error
        NativeCommandExitException: Program "winget.exe" ended with non-zero exit code: -2147012867.
        ```
    - 专门为 Windows 做了优化的（比如calibre、telegram等，这些特性可能便携版天然就做不到），也已说是便携版（scoop）用着不爽的。
-