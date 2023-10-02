- 系统编码 (Utf-8 / GBK) 的问题, [[commandline/windows]] 编码是 GBK, 就算时区切回 Utf-8(Bata版本) 命令行会出现乱码/不输出的问题, 官网的 JDK 根据电脑输出编码格式, 无法改变 JDK 的输出语言(GBK), 基本是无解...
- ```shell
  $ chcp (code)
  ```
  - | Name | Code|
    |MS-DOS 美英| 437|
    |Utf-8| 65001|
    |GBK-简中| 936|
    |GBK-繁中| 950|
- 或者直接改注册表
- ```shell
  $OutputEncoding = [console]::InputEncoding = [console]::OutputEncoding = New-Object System.Text.UTF8Encoding
  # 只可以短暂的修改编码方式
  ```
- #+BEGIN_CAUTION
  当时我也只是个 只会用 code runner 的菜鸟, 现在还是自己敲编译命令来的舒服一点...
  #+END_CAUTION
- JDK 13.0.1 降会了 JDK11(LTS)
  - 这句话写的很清晰，你的helloword是 56.0版本编译的，但是你的jre是52版本。 版本不兼容
- ## Refs
  - https://stackoverflow.com/questions/57131654/using-utf-8-encoding-chcp-65001-in-command-prompt-windows-powershell-window
  - https://www.zhihu.com/question/54724102
  - https://blog.csdn.net/yangzhong0808/article/details/79012628
-