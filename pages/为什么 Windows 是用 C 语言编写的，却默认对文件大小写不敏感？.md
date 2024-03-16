---
created: 20240224
tags: Microsoft Windows,C（编程语言）
source: https://www.zhihu.com/question/443835000/answer/1726902348
author: 初生之鸟 关注
---

- 其实在WSL出现之后，Windows逐步开放了大小写区分的支持
- 在RS5以上的系统里，可以用以下命令对某个目录打开/关闭Win32大小写区分支持，保存的是一个扩展属性
- ```shell
  fsutil.exe file setCaseSensitiveInfo <path> enable
  fsutil.exe file setCaseSensitiveInfo <path> disable
  ```
- 打开了之后，这个目录下就是大小写区分的了，所有Win32程序都会区分路径大小写
- 在以前的系统里，可以改注册表打开对Win32的全局的大小写区分支持