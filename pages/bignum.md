also:: maths/bignum
-
- 高精度计算 (Arbitrary-Precision Arithmetic), 大整数 (bignum) 计算
-
- 四则运算
  collapsed:: true
  - 加
    id:: 6322cb71-9ccf-405f-b0ff-5f75c0e340b4
  - 减
  - 乘
  - 除
    id:: 6322cb89-e7e9-4b45-b4ef-33b22d5c14cb
-
- Implement
  collapsed:: true
  - with [[cpp]]
    - ((6322cb71-9ccf-405f-b0ff-5f75c0e340b4))
      collapsed:: true
      - ```cpp
        // 斐波那契数列
        int main() {
          int N, j;
          cin >> N;
          if (N < 3) {
            if (N < 0) return 0;
            if (N == 0)cout << "0";
            if (N == 1)cout << "1";
            if (N == 2)cout << "1";
          }
          else {
            N -= 2;
            int a[5000] = { 0 }, b[5000] = { 0 }, c[5000] = { 0 };
            a[0] = 1;
            b[0] = 1;
            for (int i = 0; i < N; i++) {
              for (j = 0; j < N; j++) {
                c[j] += a[j] + b[j];
                if (c[j] > 9) {
                  c[j] -= 10;
                  c[j + 1] = 1;
                }
              }
              swap(a, b);
              swap(b, c);
              for (int i = 0; i < 5000; i++) c[i] = 0;
            }
            for (j; b[j] == 0; j--);
            for (j; j >= 0; j--)cout << b[j];
          }
        }
        ```
    - ((6322cb89-e7e9-4b45-b4ef-33b22d5c14cb))
      collapsed:: true
      - ```c++
        // 被17整除
        int main(){
          char p[1000];
          while (cin.getline(p, 1000)) {
            if (p[0] != '0') {
              int sum = 0;
              for (int i = 0; p[i] != '\0'; i++) {
                sum *= 10;
                sum += p[i] - '0';
                if (sum > 17)sum %= 17;
              }
              if (sum == 0)cout << "1\n";
              else cout << "0\n";
            }
          }
        }
        ```
-
- Refs
  collapsed:: true
  - [高精度计算 - OI Wiki](https://oi-wiki.org/math/bignum)
-
-