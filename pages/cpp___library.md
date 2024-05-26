- It's really hard that I need to remember every function prototype even they don't have manual.😱 via: https://stackoverflow.com/questions/9463640/tools-that-list-the-prototypes-in-so-library
- I have to check the `.h` to find prototype or search info in cppreference. Fucked.q
- ---
- [[cpp/array]]
- [[cpp/getline]]
- [[stl/vector]]
- [[stl/set]]
- [[stl/map]]
- [[cpp/convert]]
- [[cpp/scale]]
- [[cpp/template]]
-
- name:: 断言(assert)的用法 - thisway_diy - 博客园 (11_15_2022 1_17_26 PM).html
  tags::
  mark::
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
-
-