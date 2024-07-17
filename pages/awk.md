alias:: Linux/system-call/awk
:LOGBOOK:
CLOCK: [2022-09-28 Wed 09:39:46]
:END:

- #vs [[sed]]
  collapsed:: true
  - `swk` 统计较为规范的文本
  - `sed` 格式不规范
-
- Syntax
  collapsed:: true
  - 脚本编程 --> 流程控制
    collapsed:: true
    - before: BEGIN{}
    - main: {}
    - after: END{}
  - 字段
    collapsed:: true
    - 引用/分离
      - 行->记录
      - 空格/制表符分割的单词是字段 可以自己指定
      - ```shell
        awk -F "'" '/regular/{ print x++, $1 $2 $3 }' filename
        ```
  - 表达式
    collapsed:: true
    - 赋值
    - 系统变量
      - `FS`/`OFS`
        - ```shell
          head -5 /etc/passwd | awk 'BEGIN{FS=":";OFS="-"}{print $1, $2}'
          ```
      - `RS`
        - ```shell
          head -5 /etc/passwd | awk 'BEGIN{RS=":"}{print $0}'
          ```
      - `NR`/`FNR`
        - ```shell
          awk '{print FNR, $0}' /etc/hosts /etc/hosts
          head -5 /etc/passwd | awk 'BEGIN{FS=":"}{print NF}'
          head -5 /etc/passwd | awk 'BEGIN{FS=":"}{print $NF}'
          ```
    - 布尔
      - `~` 匹配
    - `if`
      - ```shell
        awk 'if($2>=80){print $1; print $2}' api.txt
        ```
    - `for` / `while` / ``do...while`
      - ```shell
        awk 'sum=0; for(c=2;c<=NF;c++){print sum += $c; print sum/(NF-1)}' kpi.txt
        ```
    - `break `/ `continue`
    - array , 关联性数组
      - ```shell
        vim array.awk
        awk '{sum=0; for(column=2;column<=NF;column++) sum+=$column; average[$1]=sum/(NF-1)} END{ for(user in average) print user, average[user]}' kpi.txt
        awk -f array.awk api.txt
        ```
    - Function
      - 算数函数
        - `sin()`
        - `cos()`
        - `int()`
        - `srand()`
          - `rand()` 范围 0~1
      - 字符串函数
        - `gsub(r, s, t)`
        - `index(s, t)`
        - `length(s)`
        - `match(s, r)`
        - `split(s, a, sep)`
        - `sub(r, s, t)`
        - `substr(s, p, n)`
      - 自定义函数
-