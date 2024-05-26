alias:: maths/number-theory/gcd, Greatest Common Divisor, 最大公约数
-
- 辗转相除法 / 欧几里德算法 / Euclidean algorithm
  id:: 6322ca85-80ce-4347-a589-8174d423ff3d
  - &least common multiple10.29[·](https://blog.csdn.net/qq_42504734/article/details/88369780)
  - 基于一个定理：两个正整数a和b（a>b），它们的最大公约数等于
  - a除以b的余数c和b之间的最大公约数。但是当数字比较大的时候a%b的性能会变差也是理所当然。
-
- 更相减损术
  id:: 6322caa1-0ab2-4aff-a69c-cf2f0f3ce1a3
  collapsed:: true
  - 出自《九章算术》，也是一种求最大公约数的算法。
  - 两个正整数a和b（a>b），它们的最大公约数等于a-b的差值c和较小数b的最大公约数。（可以用递归实现）
-
- Implements with [[cpp]]
  collapsed:: true
  - ((6322ca85-80ce-4347-a589-8174d423ff3d))
    collapsed:: true
    - ```c++
      int cdivisor(int m, int n) {
        int a, b, r;
        a = (m > n) ? m : n;
        b = (m > n) ? n : m;
        r = b;
        while (r != 0) {
      r = a % b;
      a = b;
      b = r;
        }
        return a;
      }
      ```
  - ((6322caa1-0ab2-4aff-a69c-cf2f0f3ce1a3))
    collapsed:: true
    - ```c++
      int cdivisor(int a, int b) {
        while (a != b) {
          if (a > b)a -= b;
          else b -= a;
        }
        return a;
      }
      ```
-
- Refs
  - [求最大公约数4种算法比较_@老王哟的博客-CSDN博客](https://blog.csdn.net/qq_42504734/article/details/88369780)
-