title:: question/cpp
alias:: cpp/question

-
- Notes
  collapsed:: true
  - char数组 一定要记住最后的 `\0`
    collapsed:: true
    - 之后的序列是 随机数/全0, 是编译器处理的结果, 各异
  - dec的用处就是1在其他编译器里去转换。
  - 逻辑结构的背后是逻辑电路，正如逻辑语言背后是逻辑内存
  - 遇到有限制条件的题在进行循环的时候将限制条件放在第一位（如题1128）——逻辑短路
  - 读取EOF的意思：while(scanf("%d %d     %d",&m,&n,&t)!=EOF&&(n&&m&&t))
  - `Define`
    collapsed:: true
    - ```cpp
      #mark::  swap(x, y)\
      x = x + y;\
      y = x - y;\
      x = x - y;
      ```
    - ​ int size = sizeof(a) / sizeof(int);是否有必要??????
    - ```cpp
      - char p[10];
      int main(){
        int n;
        cin>>n;
        for(int i=0;i<n;i++)cin>>p[i];
        cout<<strlen(p)<<endl;
        int size=sizeof(p)/sizeof(char);
        cout<<size<<endl;
      }
      ```
  - 两个冒号 `::` 特点
    collapsed:: true
    - 全局作用域符号
      - 当全局变量在局部函数中与其中某个变量重名时，可以用::来区分，否则局部变量会屏蔽全局变量。
        
        ```c
        int a = 10;
        int main() {
          int a = 100;
          cout << a << endl;
          cout << ::a;
        }
        ```
    - 作用域符号
      - 前面一般是该类名称，后面是该类的成员名称。C++为避免不同的类有相同的成员而采用作用域的方式进行区分，eg：A，B表示两个类，在A，B中都有成员member，那么：A::member表示A中的成员member，B::member表示B中的成员member。
    - 作用域分解运算符
      - 比如声明了一个类A，类A里声明了一个成员函数void f()，但没有在类的声明里给出f函数的定义，那么在类外定义f时，就要写成void A::f()，表示这个f函数是类A的成员函数。
  - `exit` #vs `return`
    - exit用于在程序运行的过程中随时结束程序，exit的参数是返回给OS的。main函数结束时也会隐式地调用exit函数。exit函数运行时首先会执行由atexit()函数登记的函数，然后会做一些自身的清理工作，同时刷新所有输出流、关闭所有打开的流并且关闭通过标准I/O函数tmpfile()创建的临时文件。exit是结束一个进程，它将删除进程使用的内存空间，同时把错误信息返回父进程,而return是返回函数值并退出函数
    - return是**语言级别**的，它表示了**调用堆栈**的返回
      collapsed:: true
      而exit是**系统调用**级别的，它**表示了一个进程的结束**。
      - 按照ANSI C，在**最初调用**的main()中使用return和exit()的效果相同
        - **如果main()在一个递归程序中，exit()仍然会终止程序；但return将控制权移交给递归的前一级，直到最初的那一级，此时return才会终止程序**。return和exit()的另一个区别在于，**即使在除main()之外的函数中调用exit()，它也将终止程序。**
    - exit函数是退出应用程序，并将应用程序的一个状态返回给OS，这个状态标识了应用程序的一些运行信息
    - 和机器和操作系统有关一般是  0 为正常退出 非0 为非正常退出
  - OVERFLOW
    collapsed:: true
    - 查到的一点是：stack overflow和CSS里面的overflow属性，还是比较懵逼，自己`cout<<OVERFLOW;`结果是3，也不清楚是什么，留存在这里。
    - OVERFLOW为math.h中的一个[宏定义](https://www.baidu.com/s?wd=%E5%AE%8F%E5%AE%9A%E4%B9%89&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao)，其值为3。含义为运算过程中出现了上溢，即运算结果超出了运算变量所能存储的范围。
  - Nest Error
    collapsed:: true
    - ```cpp
      typedef struct Stu {
        char id;
        string name;
      }S;
      int main() {
        int N, k, i = 0;
        cin >> N, k = N;
        S* p = new S[N];
        while (k--) cin >> p[i].id >> p[i++].name;
        for (i = 0; i < N; i++) {
          cout << p[i].id << " " << p[i].name << endl;
        }
      //  ......
      }
      /*
      程序写了一半
      
      3
      1 zhangsan
      2 lisi
      3 wangwu
      
      result:
      ?zhangsan
      1 lisi
      2 wangwu
      */
      ```
    - 有点懵逼，请教完师傅后明白了，是c++中如果函数的参数列表包含多个实参，那么对参数的求值顺序是不确定的。即编译器对函数的嵌套表达式求值方向是不一样的，即使是同一个编译器在不同情况下也会不一样，而且在每一次变换的情况下最终结构也大相径庭，所以在实际使用中，要尽量避免一个语句中包含多个表达式的情况，或者保证多个表达式之间不存在互相影响结果的情况。
    - > cin其实是个写法特殊的函数，`pi.id`和`pi.name`其实是它的两个参数，c参数求值顺序不确定，例如 f(a,a);假设a的值为10，如果先左后右 就是10、10 ，然后a变11，如果先右后左 就是11、10。这一点c++标准里没规定，所以不同厂商的编译器在处理库函数和自定义函数时处理方法各异，解决办法为：涉及到函数调用实参间时，避免使用。
    - 博主测试代码（转）：
    - ```cpp
      void test(int x, int y) {
        cout << 'x' << x << " y" << y << endl;
      }
      int main() {
        int i = 3;
        test(i, i++);
        i = 3, test(i, ++i);
        i = 3, test(i++, i);
        i = 3, test(++i, i);
      }
      /* result
      x4 y3
      x4 y4
      x3 y4
      x4 y4
      */
      ```
-
- Selction
  collapsed:: true
  - 如果函数值的类型和return语句中表达式的值不一致, 则 {{cloze C}}
    collapsed:: true
    A、语法出错; B、连接出错; C、以函数类型为准; D、以表达式值的类型为准;
    - 比如如果函数是int类型，你return一个字符，会自动转化ascii码
-
- Refs
  collapsed:: true
  - [【题海】郑大C语言期末模拟7 - 哔哩哔哩](https://www.bilibili.com/read/cv13406344)
-
-