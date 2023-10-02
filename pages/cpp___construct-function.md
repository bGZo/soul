title:: cpp/construct-function

- # Construct Function
  - ## 显式/隐式 explicit/implicit
    - ```cpp
      class B{
      public:
        B(int iLength){} //本意是预先分配n个字节给字符串
        B(const char *pString){} // 用C风格的字符串p作为初始化值
      };
      int main(){
          B temp1 = B(5);
          B temp2 = B("a");
          B temp3 = 5; // 等价于B temp1 = B(5);
          B temp4 = "a"; // 等价于 B temp2 = B("a");
          B temp5 = 'a'; // 等价于 B temp2 = 97;
          return 0;
      }
      ```
      - 隐式构造与是否有这个成员变量没有关系. 只有存在这个参数的构造函数, 就可以编译通过; 但是, `B temp5 = 'a';` 会有问题, CPP中字符以 ASKII 存储, 这条语句隐式构造会调用第一个构造函数. 所以要这么写:
    - ```cpp
      class B{
      public:
        explicit B(int iLength){} //本意是预先分配n个字节给字符串
        B(const char *pString){} // 用C风格的字符串p作为初始化值
      };
      ```
      - 此时, `B temp5 = 'a';` 就会编译不通过. 必须写成 `B temp = B(5)/B temp(5)`
  - ## refs
    - [C++ Explicit Constructors(显式构造函数) - 旭东的博客 - 博客园](https://www.cnblogs.com/xudong-bupt/p/3671972.html)
    - [隐式转换 - cppreference.com](https://en.cppreference.com/w/cpp/language/implicit_conversion)
-