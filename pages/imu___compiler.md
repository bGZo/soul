- 基本概念
  collapsed:: true
  - BNF / EBNF
    collapsed:: true
    - **BNF**: like `<number> ::= <digit> | <number> <digit>, <digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9`.
      collapsed:: true
      - ```shell
        <expression> ::= <expression> + <term>
              | <expression> - <term>
              | <term>
        <term> ::= <term> * <factor>
            | <term> / <factor> 
            | <factor>
        <factor> ::= <primary> ^ <factor>
            | <primary>
        <primary> ::= <primary>
            | <element>
        <element> ::= ( <expression> )
            | <variable>
            | <number>
        ```
    - **EBNF**:After BNF appeared with Algol 60, lots of people added their own extensions. Niklaus Wirth wanted to see one form, so he published “What Can We Do About the Unnecessary Diversity of Notation for Syntactic Definitions” in Communications of the ACM in 1977.
      collapsed:: true
      He suggested the use of “[ .. ]” for optional symbols (0 or 1 occurrences), “{ .. }” for 0 or more occurrences. Did not mention “EBNF” or Kleene cross(\*).
      - `*`(The Kleene Star): means 0 or more occurrences
      - `+` (The Kleene Cross): means 1 or more occurrences
      - `?`: means 0 or 1 occurrences (sometimes “[ ... ]” used instead)
      - Use of parentheses for grouping
- 自动机
- 文法分析
  collapsed:: true
  - LL(1)
  - LR(0) / SLR(1) / LALR(1) / LR(1)
- 语法分析
  collapsed:: true
  - 自顶向下
    - 递归下降分析
      collapsed:: true
      - 每个非终结符都有一个对应的函数
      - 语法分析成功 => 从开始符号的对应函数开始执行，成功扫描了整个输入字符串
      - 在调用非终结符对应的函数时就会遇见两种情况：
        - 终结符(本质token), 所以直接把这个终结符和句子中对应位置的token进行比较，判断是否符合；符合就继续，不符合就返回
        - 非终结符, 调用这个非终结符对应的函数.(可能会递归调用)
    - `LL(k)`分析 => `LL(1)`
      collapsed:: true
      - 从左（L）向右读入一个符号，最左（L）推导，采用一个1前看符号
      - LL(1)算法使用了一种称为**分析表**的工具来**避免回溯**操作
      - 工作流程
        - 将开始符号压入栈中
        - 根据输入符号和分析表来选择产生式
        - 把产生式都压入栈中
        - 如果当前栈顶是终结符，就进行匹配
        - 匹配失败退出，成功则读入，再回到第二个步骤
    - 预测分析
  - 自底向上
    - 简单优先
    - 算符优先
    - 优先函数
    - `LR` 分析 (无二义性语法)
      collapsed:: true
      - 拓广文法
        - 如果文法开头不是一个非终结符到另一个非终结符的产生式则需要加入.
      - LR(0)
      - SLR(1)
      - LALR(1)
      - LR(1)
        - 同心集：具有相同核心 (第 1 部分相同) 的项目集
      - 辨别参考
        - https://www.cnblogs.com/alexkk/p/6033159.html
        - https://zhuanlan.zhihu.com/p/331794391
        - https://bbs.csdn.net/topics/340142238
- 提取左部公因子
  collapsed:: true
  - https://www.cnblogs.com/lxykl/p/10106753.html
  - ![image](https://user-images.githubusercontent.com/57313137/147828348-fda4dff2-a845-4ef1-a6e0-2791b7d3946d.png){:height 254, :width 747}
- Refs
  collapsed:: true
  - NF
    collapsed:: true
    - [BNF-wiki](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form)
    - [EBNF-wiki](https://zh.wikipedia.org/wiki/%E6%89%A9%E5%B1%95%E5%B7%B4%E7%A7%91%E6%96%AF%E8%8C%83%E5%BC%8F)
    - [BNF-edu](https://github.com/bGZoCg/algoStack/files/7711788/BNF.pdf) (condor.depaul.edu/ichu/csc447)
  - Lex / Yacc
    collapsed:: true
    - [Part 01: Tutorial on lex/yacc](https://www.youtube.com/watch?v=54bo1qaHAfk)
    - [Part 02: Tutorial on lex/yacc](https://www.youtube.com/watch?v=__-wUHG2rfM)
  - [2021-10-31 《编译原理》学习笔记：第8周_蔗理苦的博客-CSDN博客_同心集编译原理](https://blog.csdn.net/zheliku/article/details/121059717)
  - [编译原理复习总结 - 王陸 - 博客园](https://www.cnblogs.com/wkfvawl/p/13189703.html)
  - [《编译原理之美》笔记——前端部分 | 李乾坤的博客](http://qiankunli.github.io/2020/02/08/fundamentals_of_compiling_frontend.html)
  - https://www.cnblogs.com/secoding/p/11193711.html
  - 在线 DFA 转化: https://cyberzhg.github.io/toolbox
    - (c|da)* 最长匹配  
      c*|(da)* 优先匹配
    - 两个表达式确实不一样