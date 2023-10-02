alias:: Linux/system-call/find

- WAIT System Call & Commands 区别? 要怎么分类???
-
- `name` / `-regex`
- `time`
  - `-atime`: access time
  - `-ctime`: change time
  - `-mtime`: modify time
- `-user root`
- `-uid 0`
- `-exec`
  - 直到遇到 `;` 组成的参数为止的其余命令行参数将作为提供给命令的参数
  - 参数中
    - 所有的字符串 `{}` 将以正在处理的文件名替换
    - 这些参数可能需要用  \\   来 escape   或者用括号括住，防止它们被shell展开
  - 从起始目录执行
- ```shell
  find *txt -exec rm -v {} \;
  grep pass /root/anaconda-ks.cfg | cut -d " " -f 1
  cut -d ":" -f7 /etc/passwd | uniq -c
  cut -d ":" -f7 /etc/passwd | sort | uniq -c | sort -r
  ```