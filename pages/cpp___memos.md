title:: cpp/memos
- > 消除不确定
- ## char array vs char* vs string
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
- ## r/w file
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
- ## csv string format
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
- ## basic
  -