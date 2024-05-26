title:: encoding/complement
mark:: 补码
- Ones' Complement
  mark:: "一的补码, 一补数, 一补码, 反码"
  id:: 63233299-4c35-4594-a358-c2b35d9fef9f
  - 任意一对相反数的反码的 "和" 都是一串 $1$，所以我们可以这样定义负数 $N$ 的 $n$ 位二进制反码
  - 负数的反码定义
    $$N_{补} = \underbrace{ 111\cdots1 }_{n个1} - \left| N \right|$$
- Two's Complement
  mark:: "二的补码, 二补数, 二补码"
  id:: 632332a2-db20-41f7-905d-6af2ff488157
  - 表示 (一个) $2$ 的补, 与 ((63233299-4c35-4594-a358-c2b35d9fef9f)) 不同
  - 负数的补码的定义
    $$N_{补} = 2^{n} - \left|N\right|$$
- ((63233299-4c35-4594-a358-c2b35d9fef9f)) -> ((632332a2-db20-41f7-905d-6af2ff488157))
  - 本来用 1反码 表示负数就够了，但是有缺陷
    - 0 必须有 -0 表示
      collapsed:: true
      - 这是因为在 1-反码 的情况下，为了在1-反码的二进制加减法规则下让N+(-N)=N-N，才需要定义-0
    - 二进制加减法会有溢出，需要对溢出的字节做环回处理
    - 表示范围只能是 $[-2^{(n-1)}-1, 2^{(n-1)}]$
  - 使用2-反码（等于1-反码+1）表示负数则
    - 0只需要唯一表示
    - 二进制加减法不需要对溢出的字节做处理
    - 表示范围是 $[-2^{(n-1)}, 2^{(n-1)}]$
  - 比如 IPV4 的 Checksum：
    - > The checksum field is the 16-bit one's complement of the one's complement sum of all 16-bit words in the header.
    - 实际计算算法：
      - 1. 把头部的每16个位直接按32bit数加起来得到一个32位数
        2. 把得到的32位数拆成高16位和低16位，把高16位加到低16位
        3. 取反
    - > The checksum field is the 16-bit one's complement of the one's complement sum of all 16-bit words in the header.
      - 这句话的`sum of all 16-bit words`代表的是计算步骤的1-2步 这句话的`the 16-bit one's complement of the one's complement..`代表的是计算步骤的第3步
-
- Refs
  - [Ones' complement - Wikipedia](https://en.wikipedia.org/wiki/Ones'_complement ); [一的补码 - 维基百科，自由的百科全书](https://zh.wikipedia.org/zh-cn/%E4%B8%80%E8%A3%9C%E6%95%B8)
  - [Two's complement - Wikipedia](https://en.wikipedia.org/wiki/Two's_complement ); [补码 - 维基百科，自由的百科全书](https://zh.wikipedia.org/zh-cn/%E4%BA%8C%E8%A3%9C%E6%95%B8)
  - [反码，补码为什么又叫“一的补”，“二的补”？ - 哔哩哔哩](https://www.bilibili.com/read/cv1669932/)
  - [编码](https://gist.github.com/fanfeilong/844ad0c2e2654cfd4c7e)
-