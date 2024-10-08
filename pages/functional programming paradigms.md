also:: Functional Programming, 函数式编程范式, 函数式编程
tags:: #programming-paradigms
created:: [[20230826]]
wikipedia:: https://en.wikipedia.org/wiki/Functional_programming

- ## Why
  -
- ## How
  -
- ## What
  - [[first-class-function]] 头等函数
  - Purely-functional Paradigms 纯函数式
    - 所有计算都当作数学函数的求值 (evaluation), 纯函数式编程主要在于确保函数遵守函数式范型，只依赖于它们的实际参数，而不用管任何全局或局部的状态
    - Vs [[Functional Programming Paradigms]]
      - 有争议
      - 当一个程序使用了某些函数式编程概念的时候， 比如头等函数和高阶函数，它通常就被称为是函数式
        - 头等函数不必然是纯函数式的，由于它可以使用来自指令式范型的技术，比如数组或输入/输出方法，故而它们不是纯函数程序。事实上，最早被引证为函数式的编程语言，IPL和LISP[3][4]，按照当前定义都是非纯函数式语言。
      - 纯函数式数据结构必然是持久性数据结构; 函数式编程可以使用非纯函数式的持久性数据结构
        - 函数式编程需要持久性；没有它，相同的计算可能会返回不同的结果
        - 函数式编程可能会使用持久的非纯函数式数据结构，而这些数据结构可能不会在纯函数式程序中使用
      - 纯粹采用函数式编程的基础部件（如map、reduce、filter等），进行响应式编程（异步数据流程编程）的编程范型，被称为函数式响应式编程。
    - [Purely functional programming - Wikipedia](https://en.wikipedia.org/wiki/Purely_functional_programming)
      id:: 6257dd94-ce48-48d0-9afd-501c95120cea
  - Function-level Paradigms 函数级
    - [[tacit]] 隐式
    - [[concatenative]] 串接
    - vs [[Functional Programming Paradigms]] ???+++
      - A key distinction from functional languages is that Backus' language has the following hierarchy of types:
        - atoms
        - functions, which take atoms to atoms
        - Higher-order functions (which he calls "functional forms"), which take one or two functions to functions
    - ## Lang Support
      - CMS Pipelines
      - Factor (programming language)
      - FL (programming language)
      - FP (programming language)
      - J (programming language)
      - K (programming language)
      - Q (programming language from Kx Systems)
    - ## Refs
      - [Function-level programming - Wikipedia](https://en.wikipedia.org/wiki/Function-level_programming)
  - [[pattern-matching]] 模式匹配
  - [[list-comprehension]] 推导式
-