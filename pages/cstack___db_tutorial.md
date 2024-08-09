icon:: 📦
created::  [[20220808]]
description:: 
tags:: #database #tutorial
type:: github/repo
source:: {{gh cstack/db_tutorial}}

- ## P01
  collapsed:: true
  - **REPL** (read-execute-print loop)
    - 读取﹣求值﹣输出循环 / **交互式顶层构件**
    - 一个编程环境. 因它能立刻对初学者做出回应. 对学习一门语言具有很大的帮助.
    - via: [Read–eval–print loop - Wikipedia](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)
  - ✖ B Tree
    collapsed:: true
    - via: [Youtube-29:45](https://www.youtube.com/watch?v=aZjYr87r1b8).
  - `size_t` & `ssize_t`
    collapsed:: true
    - `size_t `
      collapsed:: true
      - 32 Bit: `typedef unsigned int size_t;`.
      - 64 Bit: `typedef unsigned long size_t;`.
      - 注意写函数的时候, 无符号数不要和符号数比较.
        ```c
        #include <stdio.h>
        #include <string.h>
        int main(){
            int i = -1;
            if(i > strlen("Demon")) printf("Hello World");
            else printf("Hello Demon");
            return 0;
        } //Hello World via http://demon.tw/programming/c-size_t-pitfall.html
        ```
    - `ssize_t `
      collapsed:: true
      - 32 Bit: `int`.
      - 64 Bit: `long int`.
      - via: https://blog.csdn.net/bzhxuexi/article/details/19899803 & https://stackoverflow.com/questions/2550774/what-is-size-t-in-c
  - getline in C.
    collapsed:: true
    - collapsed:: true
      ```c
      // from https://c-for-dummies.com/blog/?p=1112
      #include <stdio.h>
      int input(char *s,int length);
      int main(){
          char *buffer;
          size_t bufsize = 32;
          size_t characters;
          buffer = (char *)malloc(bufsize * sizeof(char));
          if( buffer == NULL){
              perror("Unable to allocate buffer");
              exit(1);
          }
          printf("Type something: ");
          characters = getline(&buffer,&bufsize,stdin);
          printf("%zu characters were read.\n",characters);
          printf("You typed: '%s'\n",buffer);
          return(0);
      }
      // case two
      #include <stdio.h>
      int input(char *s,int length);
      int main()
      {
          char *b;
          size_t bufsize = 0;
          size_t characters;
          printf("Type something: ");
          characters = getline(&b, &bufsize, stdin);
          printf("%ld\n", bufsize);
          printf("%zu characters were read.\n", characters);
          printf("You typed: '%s'\n", b);
          return(0);
      }
      ```
      - 会发现在 `char` 指针做缓冲区的时候, `bufsize` 默认为 `120`, 就算读入缓冲超过 `120` , 也会加倍为`240`. 但是, char 指针可以
        ```
        > ./test
        Type something: dsdsa
        120
        6 characters were read.
        You typed: '����'
        > ./test
        Type something: testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttestt
        240
        130 characters were read.
        You typed: 'testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttestt
        '
        ```
      - more via: https://stackoverflow.com/questions/20036074/length-of-line-in-getline-function-c.
- ## P02
  collapsed:: true
  - `.exit`: "meta-commands"
  - `strncmp`: the “insert” keyword will be followed by data.
- ## P03
  collapsed:: true
  - name:: HTH
    full:: {{cloze Hope That Helps}}
    description:: used in electronic messages when you have told someone something or done something for them via: https://www.macmillandictionary.com/dictionary/british/hth
    type:: abbr
  - `uint8_t` / `uint16_t` / `uint32_t` / `uint64_t` in [[system-c]]
    id:: 629d9e2c-2c0c-48db-ae2d-56eba8649d36
    collapsed:: true
    - 这些类型的来源：这些数据类型中都带有_t, _t 表示这些数据类型是通过typedef定义的，而不是新的数据类型。也就是说，它们其实是我们已知的类型的别名。
    - 使用这些类型的原因：方便代码的维护。比如，在C中没有bool型，于是在一个软件中，一个程序员使用int，一个程序员使用short，会比较混乱。最好用一个typedef来定义一个统一的bool：
    - 在涉及到跨平台时，不同的平台会有不同的字长，所以利用预编译和typedef可以方便的维护代码。 via: [浅析C语言之uint8_t / uint16_t / uint32_t /uint64_t](https://zhuanlan.zhihu.com/p/37422763)
    - 在C99标准中定义了这些数据类型，具体定义在：`/usr/include/stdint.h` ISO C99: 7.18 Integer types
      collapsed:: true
      - ```c
        #ifndef __int8_t_mark:: d
        # mark::  __int8_t_mark:: d
        typedef signed char             int8_t;
        typedef short int               int16_t;
        typedef int                     int32_t;
            # if __WORDSIZE == 64
                typedef long int                int64_t;
            # else
            __extension__
            typedef long long int           int64_t;
            # endif
        #endif
        typedef unsigned char           uint8_t;
        typedef unsigned short int      uint16_t;
        #ifndef __uint32_t_mark:: d
            typedef unsigned int            uint32_t;
            # mark::  __uint32_t_mark:: d
        #endif
        #if __WORDSIZE == 64
            typedef unsigned long int       uint64_t;
        #else
            __extension__
            typedef unsigned long long int  uint64_t;
        #endif
        ```
      - collapsed:: true
        > [When should one use the datatypes from stdint.h?](https://stackoverflow.com/questions/20077313)
        - When the programming tasks specify the integer width especially to accommodate some file or communication protocol format.
        - When high degree of *portability* between platforms is required over *performance*.
      - `uint32_t` means `unsigned int 32 type`. via: https://stackoverflow.com/questions/48833976 & https://stackoverflow.com/questions/231760
  - Strcut, Typedef
    collapsed:: true
    - ```c
      // via: https://stackoverflow.com/questions/17720223
      truct {
         ...
      } myNameStruct;  // mark:: s myNameStruct as a variable with this struct
                       // definition, but the struct definition cannot be re-used.
      struct Name {
         ...
      } myNameStruct;  // mark::  a struct, and declare/mark::  a struct variable
               // at the same time:
      typedef struct {
         ...
      } Name_t;    // use an untagged struct type inside a typedef:
      typedef struct Name {
         ...
      } Name_t;    // begin with typedef, NewTypeName will be Name_t,
               // not a varible
      ```
  - 序列化(serialize): 把对象转化为可传输的字节序列过程称为序列化
  - 反序列化(deserialize): 把字节序列还原为对象的过程称为反序列化
- ## P04
  id:: 629dbc40-678d-4e9e-bb94-3d03c9040a26