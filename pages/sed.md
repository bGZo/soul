also:: Linux/system-call/sed, commands/sed

- vs [[vim]]
  - 全文本编辑器 vs 行编辑器
    - 非 / 交互
    - **文件 / 行** 操作模式
- sed: 替换
  - `s`
  - `-e` 多替换
  - `-i` 写回
  - `-r` 扩展正则
  - `/g` 全局替换; `/{num}` 替换第 num 的元素
  - `/p` 打印模式空间的内容
    - ` -n` 不输出
  - `/w`将模式空间的内容写在文件中
  - 寻址 `/regular/s/old/new/g`; `lineNum + s/old/new/g`
    - 行号 / 正则表达式 可以混用
  - 分组 `/regular/{s/old/new/;s/old/new/}`
  - `-f` 加载 sed 脚本
  - `[寻址]d`
    - `sed '/ab/d' file`
  - `[寻址]a` 追加
  - `[寻址]c` 改写
  - `[寻址]r` 读文件
  - `[寻址]w` 写文件
  - `[寻址]n` 下一行
  - `[寻址]=` 打印行号
  - `[寻址]p` 打印
  - `[寻址]q` 退出
    - 效率更高
  - 多行模式
    - `N` 下一行追加到模式空间(内存)
    - `D` 删除 第一个字符到第一个换行符
    - `P` 打印第一个字符到第一个换行符
    - ```shell
      sed 'N;s/\n//;s/hello bash/hello sed\n/;P;D' b.txt
      ```
  - 保持空间
    - `h/H` 模式 -> 保持
    - `g/G` 保持 -> 模式
    - `x` 交换两个空间
    - ```shell
      cat -n /etc/passwd | head -6 | sed -n '1h;1!G;$!x;$p'
      cat -n /etc/passwd | head -6 | sed -n '1!G;h$p'
      cat -n /etc/passwd | head -6 | sed -n '1!G;h$p!d'
      ```