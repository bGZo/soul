also:: 时间复杂度, 空间复杂度
tags:: #algorithm
description:: [复杂度 - OI Wiki](https://oi-wiki.org/basic/complexity/)

- 时间复杂度
  description:: 衡量一个算法的效率时. 最重要的不是看它在某个数据规模下的用时. 而是看**它的用时随数据规模而增长的趋势**. 即 **时间复杂度**
  - 数据规模
    description:: "输入数字个数、图点数与边数等等; 一般来说，数据规模越大，算法的用时就越长"
    - 为什么要考虑数据规模?
      - 现代计算机的运算速度会把微乎其微的差别无限放大;
  - 考虑到**输入内容** $$∝$$ 运行用时, 分为
    - 最坏时间复杂度
    - 平均时间复杂度 / 期望
  - floor(x)=[x] (<=x的最大整数)  ceil(x)=[x] (>=x 的最小整数)
  - 复杂度
    - [数学分析](https://www.zhihu.com/question/21387264/answer/417321105)
    - Master Theorem
- 渐进符号
  description:: "函数的阶的规范描述, 简单来说，渐进符号忽略了一个函数中增长较慢的部分以及各项的系数(在时间复杂度相关分析中，系数一般被称作 "常数"), 而保留了可以用来表明该函数增长趋势的重要部分"
  collapsed:: true
  - 大 $O$ 符号
    description:: 研究时间复杂度时通常会使用 $O$ 符号; 因为我们关注的通常是程序用时的上界; 而不关心其用时的下界; 这里的「上界」和「下界」是对于函数的变化趋势而言的; 而不是对算法而言的
    - 使用广泛主要原因
      - 我们有时只能证明时间复杂度的上界而无法证明其下界
        collapsed:: true
        - 这种情况一般出现在较为复杂的算法以及复杂度分析
      - $O$ 在电脑上输入更方便一些
    - 量度 Big O notation
      - $O(1)$ / Constant Complexity / 常数复杂度
        - 表示与输入数据规模无关
      - $O(logn)$ / Logarithmic Complexity / 对数复杂度
        - 一般底数默认2
        - 不是2也没关系, 用换底公式 ${\log_a}b = \frac{{{\log_c}b}} {{{\log_c}a}}$ 之后就是常数了
      - O（Vn）
      - $O(n)$ / Linear Complexity / 线性复杂度
      - $O(n^2)$ / N square Complexity / 平⽅复杂度
      - $O(n^3)$ / N square Complexity / ⽴⽅复杂度
      - $...$
      - $O(C^n)$ / Exponential Growth / 指数级, $C$ 是一个常数
      - $O(n!)$ / Factorial / 阶乘级
      - 注意：只看最⾼复杂度的运算
- 空间复杂度
  description:: 类似地. 算法所使用的空间随输入规模变化的趋势可以用 **空间复杂度** 来衡量
  -
  - `int` #计算机组成原理
    - 32bit / 4Byte
    - $2^{31}-1=2147483647$
    - 符号位+数值位
  - long long
    - double : 符号位1+指数位11+小数位52
      0.3*2取二进制?? -- 精度丢失
    - |a-b|<=10^-9 / 10\^-6
  - 512M/32位=128\*1024\*1024
  - 1s -> 3-5s