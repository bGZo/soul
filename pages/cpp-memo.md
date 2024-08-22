tags:: cpp

- > 消除不确定
- It's really hard that I need to remember every function prototype even they don't have manual.😱 via: https://stackoverflow.com/questions/9463640/tools-that-list-the-prototypes-in-so-library
- I have to check the `.h` to find prototype or search info in cppreference. Fucked.q
- `char array` vs `char*` vs `string`
  collapsed:: true
  - convert
    - 全都可以用笨办法, 但是谁希望嘞...
    - ![image.png](../assets/image_1650381995421_0.png)
    - char[] to stinrg
      id:: 625eb6ef-e71e-48a2-b605-4875c729b2ea
      collapsed:: true
      - ```cpp
        // 1 -  String Constructor
        char a[];
        std::string str1(a);
        // 2 -  operator=
        //    string& operator= (const char* s);
        std::string str2 = a;
        // via: https://www.techiedelight.com/convert-char-array-string-cpp/
        ```
    - char* to string
      collapsed:: true
      - more discuss: [Differences using char* and std::string - C++ Forum](http://www.cplusplus.com/forum/beginner/39622/)
      - ```cpp
        // 1 -  String Constructor
        char *p="test";
        std::string str(p);
        std::cout<<str;
        // 2 -  operator=
        //    here must be const, or warning warning: ISO C++ forbids
        //    converting a string constant to 'char*' [-Wwrite-strings]
        const char *p="test";
        std::string str= p;
        ```
    - string to char[]
      collapsed:: true
      - ```cpp
        // 1 - strcpy
        #include <cstring>
        // ...
        std::string s="hello";
        char p[s.size()+1];
        strcpy(p, s.c_str());
        // 2 - std::string::copy
        std::string s = "Hello World!";
        char cstr[s.size() + 1];
        s.copy(cstr, s.size() + 1);
        cstr[s.size()] = '\0';
        // 3 - std::copy
        std::string s = "Hello World!";
        char cstr[s.size() + 1];
        std::copy(s.begin(), s.end(), cstr);
        cstr[s.size()] = '\0';
        //via: https://www.techiedelight.com/convert-string-char-array-cpp/
        ```
    - string to char*
      collapsed:: true
      - ```cpp
        // 1 - c11
        std::string s="hello";
        char* p = &s[0]; // char* c = &*s.begin();
        std::cout<<p;
        // 2 - c14
        std::string s="hello";
        const char* p = s.c_str();
        // 3 - const_cast: removes the const attribute from a class.
        //        That means any change to the char* will be
        //        reflected in the string object and vice versa.
        #include<string>
        std::string str = "std::string to char*";
        char* c = const_cast<char*>(str.c_str());
        // 4 - strcpy
        std::string str = "std::string to char*";
        char* c = strcpy(new char[str.length() + 1], str.c_str());
        // 5 - copy
        std::string str = "std::string to char*";
        int len = str.size();
        char *c = new char[len + 1];
        std::copy(str.begin(), str.end(), c);
        c[len] = '\0';
        // via: https://www.techiedelight.com/convert-std-string-char-cpp/
        ```
    - char[] to char*
      collapsed:: true
      - ```cpp
        //    +---+---+---+---+---+---+
        // a: | h | e | l | l | o |\0 |
        //    +---+---+---+---+---+---+
        char *p = "world"; // pointer
        //    +-----+     +---+---+---+---+---+---+
        // p: |  *======> | w | o | r | l | d |\0 |
        //    +-----+     +---+---+---+---+---+---+
        // via: https://stackoverflow.com/questions/9627962/is-it-possible-to-convert-char-to-char-in-c
        // 1 - address
        char* p = &a[0]
        // 2 - strcpy
        char a[] = "test";
        char *p = strcpy(new char[strlen(a) + 1], a);
        ```
    - char* to char[]
      collapsed:: true
      - ```cpp
        #include <cstring>
        // ...
        char *name="Test";
        char test[255]
        // test=name; is error, cannot put a string(array) in a char
        strcpy(test, name);
        ```
- `r/w` file
  collapsed:: true
  - `fopen` vs `open`
    collapsed:: true
    - `fopen` is a **library function** while `open` is a **system call**.
    - `fopen` provides **buffered IO** which is faster compare to `open` which is **non buffered**.
    - `fopen` is **portable** while `open` not **portable** (**open is environment specific**).
    - `fopen` returns a pointer to a **FILE structure(FILE \*)**; `open` returns an integer that identifies the file.
    - A `FILE *` gives you the ability to use **fscanf** and other stdio functions.
    - ---
      `fopen()` is not [async-signal-safe](https://man7.org/linux/man-pages/man7/signal-safety.7.html) (none of the buffered io is), therefore it should not be used in any signal handler - or a function that may be called by it and be taken with care if used in functions that use asynchronous threads.
      ---
    - via: https://stackoverflow.com/questions/1658476/c-fopen-vs-open
  - `getline` [[cpp/getline]]
  - `istringstream`
  - via: [在 C++ 中读取 CSV 文件 | D栈 - Delft Stack](https://www.delftstack.com/zh/howto/cpp/read-csv-file-in-cpp/)
- csv string format
  collapsed:: true
  - `strtok()`
    collapsed:: true
    - ```c
      char *strtok(char s[], const char *delim);
      ```
    - 首次调用时，s为要分解的字符串
    - 非首次调用时，需要将s参数设为NULL
    - 首次调用时，strtok会忽略起始位置开始的分隔符，即若第一个字符是分割符，会被忽略掉
    - 原理
      - strtok()在参数s的字符串中发现参数delim中包含的分割字符时，则会将该字符改为\0字符。在第一次调用时，strtok()必需给予参数s字符串，往后的调用则将参数s设置成NULL。每次调用成功则返回指向被分割出片段的指针
      - 返回值
        - 当s中的字符查找到末尾时，返回NULL。
        - 如果查找不到delim中的字符时，返回当前strtok的字符串的指针。
      - strtok()函数修改了字符串s的，所以s字符串不能为常量字符串
    - ```cpp
      char str[]="ab,cd,ef";
      char *ptr;
      ptr = strtok(str, ",");
      while(ptr != NULL){
        printf("ptr=%s\n",ptr);
        ptr = strtok(NULL, ",");
      }
      return 0;
      ```
    - via [C/C++根据特定字符分割字符串、读取文件去掉逗号等特定字符、strtok()函数详解](https://blog.csdn.net/Sophia_11/article/details/89517483), [strtok()函数详解](https://blog.csdn.net/weibo1230123/article/details/80177898)
    -
- Global-Array
  collapsed:: true
  - > 全局数组到底可以开多大？为什么局部数组就不可以开大？
  - C语言的内存分配问题，C语言占用的内存可以分为5个区
    - **代码区(Text Segment)**
      - 用于放置编译过后的代码的二进制机器码。
    - **堆区(Heap)**
      - **特点**：first in first out，fifo。
      - **地址空间** ：“向上增加” ，即保存的数据越多，堆的地址就越高。
      - **功能：**用于动态内存分配。由程序员分配和释放，若不释放，当结束程序时可能由OS回收。而长时间不释放易导致“内存泄漏”。（其实就是malloc()函数能够掌控的内存区域）
      - **注：**和栈不一样，从堆上分配和重新分配块没有固定模式；你可以在任何时候分配和释放它。这样使得跟踪哪部分堆已经被分配和被释放变的异常复杂；有许多定制的堆分配策略用来为不同的使用模式下调整堆的性能。 32位以上的操作系统支持“虚存”.
    - **栈区(Stack)**
      - **特点**：向低地址扩展的数据结构，是一块连续的内存的区域。即**栈顶的地址**（在可读写的ram区的最后。是为执行线程留出的内存空间）和**栈的最大容量**是**系统预先规定**好的。last in first out，lifo。在调用函数或过程后，系统通常会清除栈上保存的局部变量、函数调用信息及其它的信息。栈另外一个重要的特征是，它的
      - **地址空间：**“向下减少”，即当栈上保存的数据越多，栈的地址就越低。
      - **功能：**一般用来存放局部变量、函数参数，由编译器自动分配和释放。
      - **性质：**附属于**线程**，当线程结束时栈被回收。
      - **场景：**   函数被调用的时候，栈顶为局部变量和一些 bookkeeping 数据预留块。当函数执行完毕，块就没有用了，可能在下次的函数调用的时候再被使用。栈通常用后进先出（LIFO）的方式预留空间；因此最近的保留块（reserved block）通常最先被释放。这么做可以使跟踪堆栈变的简单；从栈中释放块（free block）只不过是指针的偏移而已。
      - **注：**   16位模式下有段的概念,一个段只有64K。所以任何连续数据都不能超过这个尺寸。
    - **全局初始化数据区/静态数据区(Data Segment)**
      - **功能：**存放**全局变量和静态变量**。初始化的全局变量和静态变量在一块区域， 未初始化的全局变量和未初始化的静态变量在相邻的另一块区域。
      - **特点：**这个区域被整个进程共享。
    - **未初始化数据区(BSS,block started by symbol)**
      - **特点：**初始化值得时候全局变量和静态变量待的地方，运行时改变值的同时根据自身属性进入上面的区域
      - **注：**数组在局部初始化的时候会赋予随机数（乱码），但是变量不会，如果没有没定义多大就会显示类似`Not limited`的错误。**常量字符串就是放在这里的。 程序结束后由系统释放**
  - 总之。研究这个意义不大，不同编译器，可能行为不同。
    - Windows下，Data Segment（静态数据区）的所允许的空间大小取决于剩余内存的大小，也就是说，如果电脑剩余8G内存的话，int类型的二维数组甚至可以开到
      - $$ 46340 * 46340$$
      - 而 Stack（栈区）的空间只有2M. 这里我在用VS编译的时候好像是VS自定义了一个比2M小得多的栈区，经过蛋疼测试，极限是`int p[258298]`, 大概是1M. (可以用连接器参数 `/STACK:reserve[,commit]` 调整栈大小)
      - $$258298 * 4 / 1024 / 1024 = 0.98532M$$
      - $$2M = 2*1024*1024=2097152字节$$
      - 局部变量空间顶多放得下下 524288 个int类型（数组大概是`724.077*724.077`）！
      - 我想在局部中开一个大数组怎么办？很简单，将它归到 __Data Segment__ 中：
      - ```cpp
        #include<iostream>
        using namespace std;
        int main(){
          static int dis[8000][8000];//注意局部变量的初始化
        }
        ```
    - 而在局部定义数组的时候，数组会自动初始化为随机数，所以数组在刚被定义的时候就塞进 Stack 区了，才会出现 `int dis[520073]` 直接报堆栈溢出的问题
    - TODO 如果需要大量的内存. 建议使用new在堆上创建对象().或者直接使用windowsAPI VirtualAlloc,GlobalAlloc等自己从系统堆上分配.
    - ```cpp
      int a = 0; //全局初始化区
      char *p1; //全局未初始化区
      int main() {
        int b; //栈
        char s[] = "abc"; //栈
        char *p2; //栈
        char *p3 = "123456"; //123456在常量区，p3在栈上。
        static int c =0； //全局（静态）初始化区
        p1 = (char *)malloc(10);
        p2 = (char *)malloc(20); //分配得来得10和20字节的区域就在堆区。
        strcpy(p1, "123456"); //123456放在常量区，编译器可能会将它与p3所指向的"123456"优化成一个地方。
      }
      ```
  - [[heap]] vs [[stack]]
    - 申请机制
      - **栈**：只要栈的剩余空间大于所申请空间，系统将为程序提供内存，否则将报异常提示栈溢出。
      - **堆**：首先应该知道操作系统有一个记录空闲内存地址的链表，当系统收到程序的申请时，会遍历该链表，寻找第一个空间大于所申请空间的堆结点，然后将该结点从空闲结点链表中删除，并将该结点的空间分配给程序，另外，对于大多数系统，会在这块内存空间中的首地址处记录本次分配的大小，这样，代码中的delete语句才能正确的释放本内存空间。另外，由于找到的堆结点的大小不一定正好等于申请的大小，系统会自动的将多余的那部分重新放入空闲链表中。
    - 大小限制
      - **栈**：在Windows下,栈是向低地址扩展的数据结构，是一块连续的内存的区域。这句话的意思是栈顶的地址和栈的最大容量是系统预先规定好的，在  WINDOWS下，栈的大小是2M（也有的说是1M，总之是一个编译时就确定的常数），如果申请的空间超过栈的剩余空间时，将提示overflow。因此，能从栈获得的空间较小。
      - **堆**：堆是向高地址扩展的数据结构，是不连续的内存区域。这是由于系统是用链表来存储的空闲内存地址的，自然是不连续的，而链表的遍历方向是由低地址向高地址。堆的大小受限于计算机系统中有效的虚拟内存。由此可见，堆获得的空间比较灵活，也比较大。
    - 效率比较
      - **栈**由系统自动分配，速度较快。但程序员是无法控制的。
      - **堆**是由new分配的内存，一般速度比较慢，而且容易产生内存碎片,不过用起来最方便.
      - 另外，在WINDOWS下，最好的方式是用VirtualAlloc分配内存，他不是在堆，也不是在栈是直接在进程的地址空间中保留一快内存，虽然用起来最不方便。但是速度， 也最灵活
    - 存储内容
      - **栈**： 在函数调用时，第一个进栈的是主函数中后的下一条指令（函数调用语句的下一条可执行语句）的地址，然后是函数的各个参数，在大多数的C编译器中，参数是由右往左入栈的，然后是函数中的局部变量。注意静态变量是不入栈的。
      - 当本次函数调用结束后，局部变量先出栈，然后是参数，最后栈顶指针指向最开始存的地址，也就是主函数中的下一条指令，程序由该点继续运行。
      - **堆**：一般是在堆的头部用一个字节存放堆的大小。堆中的具体内容有程序员安排。
    - 每一个线程都有一个栈，但是每一个应用程序通常都只有一个堆（尽管为不同类型分配内存使用多个堆的情况也是有的）。
      - 效率比较实例：
        - ```cpp
          char s1[] = "aaaaaaaaaaaaaaa"; //aaaaaaaaaaa是在运行时刻赋值的；
          char *s2 = "bbbbbbbbbbbbbbbbb"; //bbbbbbbbbbb是在编译时就确定的；
          ```
      - 在以后的存取中，在栈上的数组比指针所指向的字符串(例如堆)快。 这个可以用编译后的汇编代码查看操作来敲定到底做了什么。（Flag）
  - **理性分析：**
  - 回归这道题目，具体开多大根据题目给的内存进行处理?
  - $$8000 * 8000 * 4 / 1024 / 1024 ≈ 244 MB$$
  - $$8192 * 8192 * 4 / 1024 / 1024 ≈ 256 MB$$
  - 普通题目最大可以开到8129的大小。考虑要用到的局部变量的话，一个局部变量是
  - $$1 * 4 / 1024 / 1024 = 0.0000038MB$$
  - 相对而言比较大的局部变量是他的二倍，不过`0.0000076MB`.明显占不到什么内存。
  -
- Global-Array refs
  collapsed:: true
  - [关于C语言开大数组溢出的问题](https://blog.csdn.net/qq_21882325/article/details/65445810).Leaviathan
  - [局部变量，静态局部变量，全局变量，静态全局变量在内存中的存放区别(转)](https://www.cnblogs.com/bakari/archive/2012/08/05/2623637.html).Linux云计算网络
  - [C++的数组可以int n;cin>>n;int a`n;`这样初始化吗](https://segmentfault.com/q/1010000006672117).
- getline
  collapsed:: true
  - 数组是申请一段连续的内存，`a[10]`申请到的内存是`a[0]`到`a[9]`，是没有`a[10]`的，这里下标就是一个误区，因为以前总是喜欢数组开1000，所以根本没有时注意这点. 也就是说，如何你要读取11位的数字（手机号码），你要开的内存大小最少是12`p[12]`，读取也是12`cin.getline(p,12)`，不存在说p[12]和p[11]都是空的疑问
  - __读取字符串__
    collapsed:: true
    - ```c
      int main() {
        char p[5];
        cin.getline(p, 5);//准确来说读取的位数是4位+'\0'一共五位，四位有效数字
        cout << p << endl;
      }
      ```
    - 如注释所言，这样控制的数量只可以是读取有效的四位而已，如果要读取五位数字，就要定义6大小的数组。
  - __字符数组整体命名__
    collapsed:: true
    - ```c
      int main() {
        char w[5] = { 'Dang' };
        cout << w<<"\n";
        char p[] = { "Dang" };
        cout << p;
      }
      ```
    - 注意的一点就是要用双引号（单引号会变成那个串的最后一个字母!!!枯了）
  - __不确定数组的大小__
    collapsed:: true
    - 字符数组那自不必我多说是用`strlen(p)`来确定，但是同样的，可以用`sizeof(p)/sizeof(char)`来确定
- 断言(assert)的用法 - thisway_diy - 博客园 (11_15_2022 1_17_26 PM).html
  archive:: [💾 Archived](../assets/archived_web/断言(assert)的用法 - thisway_diy - 博客园 (11_15_2022 1_17_26 PM).html)
  collapsed:: true
  - 事实上，它居然是个宏，并且作用并非"报错"
  - assert() 的用法像是一种"契约式编程"，在我的理解中，其表达的意思就是，程序在我的假设条件下，能够正常良好的运作
  - assert 的作用是现计算表达式 expression ，如果其值为假（即为0），那么它先向 stderr 打印一条出错信息,然后通过调用 abort 来终止程序运行
  - 缺点是，频繁的调用会极大的影响程序的性能，增加额外的开销
  - 通过在包含 `#include`  的语句之前插入 `#mark::  NDEBUG` 来禁用 assert 调用
  - <h3>用法</h3>
    - **在函数开始处检验传入参数的合法性**
    - **每个assert只检验一个条件,因为同时检验多个条件时,如果断言失败,无法直观的判断是哪个条件失败**
    - **不能使用改变环境的语句,因为assert只在DEBUG个生效,如果这么做,会使用程序在真正运行时遇到问题**
    - **assert和后面的语句应空一行,以形成逻辑和视觉上的一致感**
    - **有的地方,assert不能代替条件过滤 **
    - 程序一般分为Debug 版本和Release 版本，Debug 版本用于内部调试，Release 版本发行给用户使用。断言assert 是仅在Debug 版本起作用的宏，它用于检查"不应该"发生的情况
    - **原则**
      - 使用断言捕捉不应该发生的非法情况。不要混淆非法情况与错误情况之间的区别，后者是必然存在的并且是一定要作出处理的
      - 使用断言对函数的参数进行确认
      - 在编写函数时，要进行反复的考查，并且自问："我打算做哪些假定？"一旦确定了的假定，就要使用断言对假定进行检查
      - 一般教科书都鼓励程序员们进行防错性的程序设计，但要记住这种编程风格会隐瞒错误。当进行防错性编程时，如果"不可能发生"的事情的确发生了，则要使用断言进行报警
    -
- <ctype.h> Functions
  collapsed:: true
  - via: https://www.programiz.com/c-programming/library-function/ctype.h/isalpha
  - `isalnum()`
  - `isalpha()`
    - Result when uppercase alphabet is passed: 1
    - Result when lowercase alphabet is passed: 2
    - Result when non-alphabetic character is passed: 0
  - `iscntrl()` -> control characters. (backspace, Escape, newline etc.)
  - `isdigit()`
  - `isgraph()` -> graphic characters. (图形字符)
  - `islower()`
  - `isprint()`
  - `ispunct()` ->  punctuation mark. (标点符号)
  - `isspace()` ->  white-space character.
  - `isxdigit()` -> hexadecimal digit character
  - `tolower()`
  - `toupper()`
- 万能头文件
  collapsed:: true
  - ```cpp
    #ifndef _GLIBCXX_NO_ASSERT
    #include <cassert>
    #endif
    #include <cctype>
    #include <cerrno>
    #include <cfloat>
    #include <ciso646>
    #include <climits>
    #include <clocale>
    #include <cmath>
    #include <csetjmp>
    #include <csignal>
    #include <cstdarg>
    #include <cstddef>
    #include <cstdio>
    #include <cstdlib>
    #include <cstring>
    #include <ctime>
    #if __cplusplus >= 201103L
    #include <ccomplex>
    #include <cfenv>
    #include <cinttypes>
    #include <cstdalign>
    #include <cstdbool>
    #include <cstdint>
    #include <ctgmath>
    #include <cwchar>
    #include <cwctype>
    #endif
    // C++
    #include <algorithm>
    #include <bitset>
    #include <complex>
    #include <deque>
    #include <exception>
    #include <fstream>
    #include <functional>
    #include <iomanip>
    #include <ios>
    #include <iosfwd>
    #include <iostream>
    #include <istream>
    #include <iterator>
    #include <limits>
    #include <list>
    #include <locale>
    #include <map>
    #include <memory>
    #include <new>
    #include <numeric>
    #include <ostream>
    #include <queue>
    #include <set>
    #include <sstream>
    #include <stack>
    #include <stdexcept>
    #include <streambuf>
    #include <string>
    #include <typeinfo>
    #include <utility>
    #include <valarray>
    #include <vector>
    #if __cplusplus >= 201103L
    #include <array>
    #include <atomic>
    #include <chrono>
    #include <condition_variable>
    #include <forward_list>
    #include <future>
    #include <initializer_list>
    #include <mutex>
    #include <random>
    #include <ratio>
    #include <regex>
    #include <scoped_allocator>
    #include <system_error>
    #include <thread>
    #include <tuple>
    #include <typeindex>
    #include <type_traits>
    #include <unordered_map>
    #include <unordered_set>
    #endif
    ```
- Sort
  collapsed:: true
  - Custom Compare Function
    collapsed:: true
    - > **comp** - comparison function which ==returns  *true* if the first argument is less than the second==. The signature of the comparison function should be equivalent to the following:  `bool cmp(const Type1 &a, const Type2 &b);`
      More via: [http://en.cppreference.com/w/cpp/algorithm/sort](http://en.cppreference.com/w/cpp/algorithm/sort).
      - ```
        template< class RandomIt, class Compare >
        void sort( RandomIt first, RandomIt last, Compare comp );
        ```
    - 意思就是说, 如果 第一次参数 < 第二个参数, 那么就符合规则(`true`), 所以最终得到的结果是从大到小, 因为 不符合规则的(false) 都丢到后面去了
      - 这样我们就可以更加 #[[abstract]] 一点, 如果我们想要让某个值排得考前一点, 那么我们就可以把他写成小于的那一方
    - Custom C++14 polymorphic lambda:
      - ```
        std::sort(std::begin(container), std::end(container),
                [] (const auto& lhs, const auto& rhs) {
          return lhs.first < rhs.first;
        });
        ```
  - Refs
    - [c++ custom compare function for std::sort() - Stack Overflow](https://stackoverflow.com/questions/16894700/c-custom-compare-function-for-stdsort)
- template
  collapsed:: true
  - [[generic]]
  - 本质和函数模板相同.
  - ```cpp
    template <class myType>
    myType GetMax (myType a, myType b) {
     return (a>b?a:b);
    }
    ```
  - ## USAGE
    collapsed:: true
    - > Here we have created a template function with myType as its template parameter. This template parameter represents a type that has not yet been specified, but that can be used in the template function as if it were a regular type.
      我们以myType作为模板参数创建了一个模板函数。此模板参数表示尚未指定的类型，但是可以在模板函数中使用它，就像它是常规类型一样
  - ## FUNCTION
    collapsed:: true
    - > When the compiler encounters this call to a template function, it uses the template to automatically generate a function replacing each appearance of myType by the type passed as the actual template parameter (int in this case) and then calls it. This process is automatically performed by the compiler and is invisible to the programmer.
    - 当编译器遇到对模板函数的调用时，它将使用模板自动生成一个函数，该函数将myType的每个外观替换为作为实际模板参数（在本例中为int）传递的类型，然后对其进行调用。该过程由编译器自动执行，并且对于程序员是不可见的。
    - > In this specific case where the generic type T is used as a parameter for GetMax the compiler can find out automatically which data type has to instantiate without having to explicitly specify it within angle brackets (like we have done before specifying <int> and <long>).
    - 如果处理的多个参数是同一类型, 那么`<>`里面的类型可以隐形调用, 而不用显示说明.
    - We can also mark::  function templates that accept more than one type parameter, simply by specifying more template parameters between the angle brackets. For example:
    - ```cpp
      template <class T, class U>
      T GetMin (T a, U b) {
      return (a<b?a:b);
      }
      ```
    - 当出现多个参数类型的时候需要使用多个模板参数得以实现.
  - ## ClASS USAGE
    collapsed:: true
    - ```cpp
      template <class T>
      T mypair<T>::getmax ()
      ```
    - >  The first one is the template parameter.
      >
      > The second T refers to the type returned by the function.
      >
      > And the third T (the one between angle brackets) is also a requirement: It specifies that this function's template parameter is also the class template parameter.
  - ## Non-type parameters for templates
    collapsed:: true
    - ```cpp
      template<typename T, int N>
      void func(){
      T a[N];
      }
      ```
  - ## SPECIALIZATION
    collapsed:: true
    - This is the syntax used in the class template specialization:
    - ```cpp
      template <> class mycontainer <char> { ... };
      ```
    - First of all, notice that we precede the class template name with an empty template<> parameter list. This is to explicitly declare it as a template specialization.
    - But more important than this prefix, is the <char> specialization parameter after the class template name. This specialization parameter itself identifies the type for which we are going to declare a template class specialization (char). Notice the differences between the generic class template and the specialization:
    - ```cpp
      template <class T> class mycontainer { ... };
      template <> class mycontainer <char> { ... };
      ```
    - The first line is the generic template, and the second one is the specialization.
    - When we declare specializations for a template class, we must also mark::  all its members, even those exactly equal to the generic template class, because there is no "inheritance" of members from the generic template to the specialization.
    - 当我们为模板类声明特殊化时，我们还必须定义其所有成员，甚至那些与通用模板类完全相同的成员，因为从通用模板到特殊化之间没有成员的“继承性”。
    - 但是，比此前缀更重要的是类模板名称后面的`<char>`专门化参数。这个特殊化参数本身标识了要为其声明模板类特殊化（`char`）的类型。请注意，通用类模板和专业化之间的区别：
    - 即专门模板与通用模板的一些区别
  - ## MUTI-FILES
    collapsed:: true
    - > From the point of view of the compiler, templates are not normal functions or classes. They are compiled on demand, meaning that the code of a template function is not compiled until an instantiation with specific template arguments is required. At that moment, when an instantiation is required, the compiler generates a function specifically for those arguments from the template.
      >
      > When projects grow it is usual to split the code of a program in different source code files. In these cases, the interface and implementation are generally separated. Taking a library of functions as example, the interface generally consists of declarations of the prototypes of all the functions that can be called. These are generally declared in a "header file" with a .h extension, and the implementation (the definition of these functions) is in an independent file with c++ code.
      >
      > Because templates are compiled when required, this forces a restriction for multi-file projects: the implementation (definition) of a template class or function must be in the same file as its declaration. That means that we cannot separate the interface in a separate header file, and that we must include both interface and implementation in any file that uses the templates.
      >
      > Since no code is generated until a template is instantiated when required, compilers are prepared to allow the inclusion more than once of the same template file with both declarations and definitions in a project without generating linkage errors.
      从编译器的角度来看，模板不是正常的函数或类。它们是按需编译的，这意味着直到需要使用特定模板参数的实例化之后，才编译模板函数的代码。那时，需要实例化时，编译器会为模板中的这些参数专门生成一个函数。
      当项目增长时，通常会将程序的代码拆分为不同的源代码文件。在这些情况下，接口和实现通常是分开的。以函数库为例，该接口通常由可调用的所有函数的原型的声明组成。这些通常在带有.h扩展名的“头文件”中声明，并且实现（这些函数的定义）在具有c ++代码的独立文件中。
      由于模板是在需要时编译的，因此对多文件项目施加了限制：模板类或函数的实现（定义）必须与声明的文件位于同一文件中。这意味着我们不能在单独的头文件中分离接口，并且必须在使用模板的任何文件中同时包含接口和实现。
      由于在需要时实例化模板之前不会生成任何代码，因此编译器准备允许在项目中使用声明和定义在同一模板文件中多次包含该模板文件，而不会产生链接错误。
  - ## refs
    - https://blog.csdn.net/EmSoftEn/article/details/50421124
    - http://www.cplusplus.com/doc/oldtutorial/templates/
- `<stdlib.h>/<itoa>`: 任意进制的转换
  collapsed:: true
  - `windows` 特有
  - ```cpp
    //via: https://www.cnblogs.com/gongpixin/p/4477361.html
    #include<iostream>
    #include<stdio.h>
    using namespace std;
    char*my_itoa(int num,char*str,int radix){//原数字，存放地址，要转换的转换进制
        const char table[]="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" ;
        char*ptr=str ;
        bool negative=false ;
        if(num==0){
            //num=0
            *ptr++='0' ;
            *ptr='/0' ;
            // don`t forget the end of the string is '/0'!!!!!!!!!
            return str ;
        }
        if(num<0){
            //if num is negative ,the add '-'and change num to positive
            *ptr++='-' ;
            num*=-1 ;
            negative=true ;
        }
        while(num){
            *ptr++=table[num%radix];
            num/=radix ;
        }
        *ptr='\0' ;
        //if num is negative ,the add '-'and change num to positive
        // in the below, we have to converse the string
        char*start=(negative?str+1:str);
        //now start points the head of the string
        ptr--;
        //now prt points the end of the string
        while(start<ptr){
            char temp=*start ;
            *start=*ptr ;
            *ptr=temp ;
            start++;
            ptr--;
        }
        return str ;
    }
    int main(){
      int a=15;
      char str[100];
      my_itoa(a,str,8);
      printf("%s\n",str);
      return 0;
    }
    ```
- Construct Function
  collapsed:: true
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
- operator-precedence
  collapsed:: true
  - ```cpp
    int main() {
      int a, b, c;
      a = 1, b = 0, c = 1;
      if (a == b == c==0) cout << "Y";
        cout<<endl;
        a = 1, b = 1, c = 1;
      if (a == b == c==0) cout << "Y";
    }
    /*
    Y
    */
    ```
  - 于是上网找了找资料……涉及到了运算符的结合顺序，
  - > 先执行a`==`b结果是（true或false）再和c比。那么c的`==`是和a`==`b的结果进行比较而已。
  - 所以自己从左面一步一步算到右面居然就是正确的……以下附上C++运算符优先级以及结合表，以前都没有这么注意过这个……
  - | 优先级 | 运算符 | 名称或含义 | 使用形式 | 结合方向 | 说明 |
    | 1 | [] | 数组下标 | 数组名[常量表达式] | 左到右 |  |
    |  | () | 圆括号 | (表达式)  函数名(形参表) |  | 函数调用 参数传递 |
    |  | . | 成员选择（对象） | 对象.成员名 |  |  |
    |  | -> | 成员指针选择（指针） | 对象指针->成员名 |  |  |
    |  | .* | 成员指针选择 |  |  |  |
    |  | ->* | 成员指针选择 |  |  |  |
    | 2 | - | 负号运算符 | -表达式 | 右到左 | 单目运算符 |
    |  | (类型) | 强制类型转换 | (数据类型)表达式 |  |  |
    |  | ++ | 自增运算符 | 变量名  变量名 |  | 单目运算符 |
    |  | -- | 自减运算符 | --变量名  变量名-- |  | 单目运算符 |
    |  | * | 取值运算符 | *指针变量 |  | 单目运算符 |
    |  | & | 取地址运算符 | &变量名 |  | 单目运算符 |
    |  | ! | 逻辑非运算符 | !表达式 |  | 单目运算符 |
    |  | ~ | 按位取反运算符 | ~表达式 |  | 单目运算符 |
    |  | sizeof | 长度运算符 | sizeof(表达式) |  |  |
    |  | new delect | 动态内存分配 释放内存 |  |  |  |
    | 3 | / | 除 | 表达式 / 表达式 | 左到右 | 双目运算符 |
    |  | * | 乘 | 表达式*表达式 |  | 双目运算符 |
    |  | % | 余数（取模） | 整型表达式%整型表达式 |  | 双目运算符 |
    | 4 | + | 加 | 表达式+表达式 | 左到右 | 双目运算符 |
    |  | - | 减 | 表达式-表达式 |  | 双目运算符 |
    | 5 | << | 左移 | 变量<<表达式 | 左到右 | 双目运算符 |
    |  | >> | 右移 | 变量>>表达式 |  | 双目运算符 |
    | 6 | > | 大于 | 表达式>表达式 | 左到右 | 双目运算符 |
    |  | >= | 大于等于 | 表达式>=表达式 |  | 双目运算符 |
    |  | < | 小于 | 表达式<表达式 |  | 双目运算符 |
    |  | <= | 小于等于 | 表达式<=表达式 |  | 双目运算符 |
    | 7 | == | 等于 | 表达式==表达式 | 左到右 | 双目运算符 |
    |  | != | 不等于 | 表达式!= 表达式 |  | 双目运算符 |
    | 8 | & | 按位与 | 表达式&表达式 | 左到右 | 双目运算符 |
    | 9 | ^ | 按位异或 | 表达式^表达式 | 左到右 | 双目运算符 |
    | 10 | &\#124; | 按位或 | 表达式&\#124;表达式 | 左到右 | 双目运算符 |
    | 11 | && | 逻辑与 | 表达式&&表达式 | 左到右 | 双目运算符 |
    | 12 | &\#124;&\#124; | 逻辑或 | 表达式&\#124;&\#124;表达式 | 左到右 | 双目运算符 |
    | 13 | ?: | 条件运算符 | 表达式1? 表达式2: 表达式3 | 右到左 | 三目运算符 |
    | 14 | = | 赋值运算符 | 变量=表达式 | 右到左 |  |
    |  | /= | 除后赋值 | 变量/=表达式 |  |  |
    |  | *= | 乘后赋值 | 变量*=表达式 |  |  |
    |  | %= | 取模后赋值 | 变量%=表达式 |  |  |
    |  | += | 加后赋值 | 变量+=表达式 |  |  |
    |  | -= | 减后赋值 | 变量-=表达式 |  |  |
    |  | <<= | 左移后赋值 | 变量<<=表达式 |  |  |
    |  | >>= | 右移后赋值 | 变量>>=表达式 |  |  |
    |  | &= | 按位与后赋值 | 变量&=表达式 |  |  |
    |  | ^= | 按位异或后赋值 | 变量^=表达式 |  |  |
    |  | &\#124;= | 按位或后赋值 | 变量&\#124;=表达式 |  |  |
    | 15 | , | 逗号运算符 | 表达式,表达式,… | 左到右 |  |
  -
  - 下表就整理了优先级同为1 的几种运算符如果同时出现的情况：
  - | 优先级问题 | 表达式 | 经常误认为的结果 | 实际结果 |
    | :---: | :---: | :---: | :---: |
    | . 的优先级高于 *（-> 操作符用于消除这个问题） | `*p.f` | p 所指对象的字段 f，等价于：  (*p).f | 对 p 取 f 偏移，作为指针，然后进行解除引用操作，等价于：  *(p.f) |
    | [] 高于 * | `int *ap[]` | ap 是个指向 int 数组的指针，等价于：  int (*ap)[] | ap 是个元素为 int 指针的数组，等价于：  int *(ap []) |
    | 函数 () 高于 * | `int *fp()` | fp 是个函数指针，所指函数返回 int，等价于：  int (*fp)() | fp 是个函数，返回 int_，等价于：  int_ ( fp() ) |
    | == 和 != 高于位操作 | `(val & mask != 0)` | (val &mask) != 0 | val & (mask != 0) |
    | == 和 != 高于赋值符 | `c = getchar() != EOF` | (c = getchar()) != EOF | c = (getchar() != EOF) |
    | 算术运算符高于位移 运算符 | `msb << 4 + lsb` | (msb << 4) + lsb | msb << (4 + lsb) |
    | 逗号运算符在所有运 算符中优先级最低 | `i = 1, 2` | i = (1,2) | (i = 1), 2 |
  - ## refs
    - [c++中函数参数的求值顺序](https://www.cnblogs.com/Leon-Yan/p/7567766.html). Leon_Yan
    - [[C/C板块推荐阅读] 关于C,C表达式求值顺序.](https://bbs.csdn.net/topics/370153775) . 裘宗燕
- convert
  collapsed:: true
  - ## `int` <-> `string`
    collapsed:: true
    - `string` -> `int`
      - `<string>/stoi()`
      - `<cstdlib>/atoi()`
    - `int` -> `string`
      - `<string>/to_string()`
      - `<sstream><string>/stringstream`
  - ## refs
    collapsed:: true
    - https://www.programiz.com/cpp-programming/string-int-conversion
- c11
  collapsed:: true
  - 新的循环
    collapsed:: true
    - ```c
      int main() {
        int array[] = { 1,2,3,4,5,'\0' };
        for (int i : array)i *= 2;
        for (int i = 0; array[i] != '\0'; i++)cout << array[i] << " ";
        cout << endl;
        for (int &i : array)i *= 2;
        for (int i = 0; array[i] != '\0'; i++)cout << array[i] << " ";
      }
      ```
    - 运行结果是
      `1 2 3 4 5`
      `2 4 6 8 10`
    - 这个循环大有来历，当初问老师老师也不承认这是C++的标准写法，但是整洁度还是让我比较向往这样的写法。
    - 自己仿照这个循环自己写了一个小小的循环，这个循环叫foreach循环，是从Java引用过来的？！**是C++11的新特点**。其实还是有点懵逼
      - ```c
        void printLOVE() {
          char arr[] = { 'I','O','E','V','L',' ','U','Y','O'};
          int index[] = { 0,5,4,1,3,2,5,7,8,6 };
          for (int i : index) {
        cout << arr[i];
          }
        }
        ```
      - 把数组 a中所有的数，一一 赋给 b,并且 每赋值一个数 执行{}中的 代码一次
-