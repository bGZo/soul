- ## Global-Array
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
      - **场景：**   函数被调用的时候，栈顶为局部变量和一些 bookkeeping 数据预留块。当函数执行完毕，块就没有用了，可能在下次的函数调用的时候再被使用。栈通常用后进先出（LIFO）的方式预留空间；因此最近的保留块（reserved block）通常最先被释放。这么做可以使跟踪堆栈变的简单；从栈中释放块（free block）只不过是指针的偏移而已。
      - **注：**   16位模式下有段的概念,一个段只有64K。所以任何连续数据都不能超过这个尺寸。
    - **全局初始化数据区/静态数据区(Data Segment)**
      - **功能：**存放**全局变量和静态变量**。初始化的全局变量和静态变量在一块区域， 未初始化的全局变量和未初始化的静态变量在相邻的另一块区域。
      - **特点：**这个区域被整个进程共享。
    - **未初始化数据区(BSS,block started by symbol)**
      - **特点：**初始化值得时候全局变量和静态变量待的地方，运行时改变值的同时根据自身属性进入上面的区域
      - **注：**数组在局部初始化的时候会赋予随机数（乱码），但是变量不会，如果没有没定义多大就会显示类似`Not limited`的错误。**常量字符串就是放在这里的。 程序结束后由系统释放**
  - 总之。研究这个意义不大，不同编译器，可能行为不同。
    - Windows下，Data Segment（静态数据区）的所允许的空间大小取决于剩余内存的大小，也就是说，如果电脑剩余8G内存的话，int类型的二维数组甚至可以开到
      - $$ 46340 * 46340$$
      - 而 Stack（栈区）的空间只有2M. 这里我在用VS编译的时候好像是VS自定义了一个比2M小得多的栈区，经过蛋疼测试，极限是`int p[258298]`, 大概是1M. (可以用连接器参数 `/STACK:reserve[,commit]` 调整栈大小)
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
      - **栈**：在Windows下,栈是向低地址扩展的数据结构，是一块连续的内存的区域。这句话的意思是栈顶的地址和栈的最大容量是系统预先规定好的，在  WINDOWS下，栈的大小是2M（也有的说是1M，总之是一个编译时就确定的常数），如果申请的空间超过栈的剩余空间时，将提示overflow。因此，能从栈获得的空间较小。
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
- ## refs
  - [关于C语言开大数组溢出的问题](https://blog.csdn.net/qq_21882325/article/details/65445810).Leaviathan
  - [局部变量，静态局部变量，全局变量，静态全局变量在内存中的存放区别(转)](https://www.cnblogs.com/bakari/archive/2012/08/05/2623637.html).Linux云计算网络
  - [C++的数组可以int n;cin>>n;int a`n;`这样初始化吗](https://segmentfault.com/q/1010000006672117).