tags:: #outdated
douban:: [编写高质量代码：改善Python程序的91个建议 (豆瓣)](https://book.douban.com/subject/25910544/)
weread:: [编写高质量代码：改善Python程序的91个建议-张颖 赖勇浩-微信读书](https://weread.qq.com/web/bookDetail/b4832100597d8eb481b4cd6)
cover:: ![](https://img9.doubanio.com/view/subject/l/public/s27308066.jpg)
created:: [[20230227]]
closed:: [[20230227]]

- ## Contents
  - 版权信息
  - 前言
  - 第1章 引论
    - 建议1：理解Pythonic概念
    - 建议2：编写Pythonic代码
    - 建议3：理解Python与C语言的不同之处
    - 建议4：在代码中适当添加注释
    - 建议5：通过适当添加空行使代码布局更为优雅、合理
    - 建议6：编写函数的4个原则
    - 建议7：将常量集中到一个文件
  - 第2章 编程惯用法
    - 建议8：利用assert语句来发现问题
    - 建议9：数据交换值的时候不推荐使用中间变量
    - 建议10：充分利用Lazy evaluation的特性
    - 建议11：理解枚举替代实现的缺陷
    - 建议12：不推荐使用type来进行类型检查
    - 建议13：尽量转换为浮点类型后再做除法
    - 建议14：警惕eval()的安全漏洞
    - 建议15：使用enumerate()获取序列迭代的索引和值
    - ==建议16：分清\=\=与is的适用场景==
      collapsed:: true
      - is 表示 **对象标示符 (object identity)**；\=\=表示**相等 (equal)**
        - 这一点和 Java 相似，Java 中的 \=\= 作用和 Python 中的 is 作用相同；
      - ```python
        >>> a = "Hi"
        >>> b = "Hi"
        >>> a is b	   # True
        >>> a == b     # True
        >>> a1 = "I am using long string for testing"
        >>> b1 = "I am using long string for testing"
        >>> a1 is b1   # False
        >>> a1 == b1   # True
        ```
        - 至于为什么两个列子的最终结果前后不一致
          - **string interning（字符串驻留）机制**
            description:: 对于较小的字符串，为了提高系统性能会保留其值的一个副本，当创建新的字符串的时候直接指向该副本即可
    - 建议17：考虑兼容性，尽可能使用Unicode
      - 要解决示例一的乱码问题可以使用Unicode作为中间介质来完成转换。首先需要对读入的字符用UTF-8进行解码，然后再用GBK进行编码
        - ==我觉得，不如全都用 UTF-8 编解码（关键是Windows命令行也使用 UTF-8），放弃GBK 😅；编码这方面，Windows 家庭中文版总是埋下一个大坑，Linux 就没有这个问题==
          #Windows #linux
    - 建议18：构建合理的包层次来管理module
  - 第3章 基础语法
    - 建议19：有节制地使用from...import语句
      - 一般情况下尽量优先使用 `import a` 式，如访问B时需要使用a.B的形式
      - 有节制地使用 `from a import B` 形式，可以直接访问B
      - 尽量避免使用 `from a import *`，因为这会污染命名空间，并且无法清晰地表示导入了哪些对象
    - 建议20：优先使用absolute import来导入模块
    - 建议21：i+=1不等于++i
    - 建议22：使用with自动关闭资源
    - 建议23：使用else子句简化循环（异常处理）
    - 建议24：遵循异常处理的几点基本原则
    - 建议25：避免finally中可能发生的陷阱
    - 建议26：深入理解None，正确判断对象是否为空
    - 建议27：连接字符串应优先使用join而不是+
    - 建议28：格式化字符串时尽量使用.format方式而不是%
    - 建议29：区别对待可变对象和不可变对象
    - 建议30：[]、()和{}：一致的容器初始化形式
    - 建议31：记住函数传参既不是传值也不是传引用
    - 建议32：警惕默认参数潜在的问题
    - 建议33：慎用变长参数
    - 建议34：深入理解str()和repr()的区别
    - 建议35：分清staticmethod和classmethod的适用场景
  - 第4章 库
    - 建议36：掌握字符串的基本用法
    - 建议37：按需选择sort()或者sorted()
    - 建议38：使用copy模块深拷贝对象
    - 建议39：使用Counter进行计数统计
    - 建议40：深入掌握ConfigParser
    - 建议41：使用argparse处理命令行参数
    - 建议42：使用pandas处理大型CSV文件
    - 建议43：一般情况使用ElementTree解析XML
    - 建议44：理解模块pickle优劣
    - 建议45：序列化的另一个不错的选择——JSON
    - 建议46：使用traceback获取栈信息
    - 建议47：使用logging记录日志信息
    - 建议48：使用threading模块编写多线程程序
    - 建议49：使用Queue使多线程编程更安全
  - 第5章 设计模式
    - 建议50：利用模块实现单例模式
    - 建议51：用mixin模式让程序更加灵活
    - 建议52：用发布订阅模式实现松耦合
    - ==建议53：用状态模式美化代码==
  - 第6章 内部机制
    - 建议54：理解built-1n objects
    - 建议55：__init__()不是构造方法
    - 建议56：理解名字查找机制
    - ==建议57：为什么需要self参数==
    - 建议58：理解MRO与多继承
    - 建议59：理解描述符机制
    - 建议60：区别__getattr__()和__getattribute__()方法
    - 建议61：使用更为安全的property
    - 建议62：掌握metaclass
    - 建议63：熟悉Python对象协议
    - 建议64：利用操作符重载实现中缀语法
    - 建议65：熟悉 Python 的迭代器协议
    - 建议66：熟悉 Python 的生成器
    - 建议67：基于生成器的协程及greenlet
    - 建议68：理解GIL的局限性
    - 建议69：对象的管理与垃圾回收
  - 第7章 使用工具辅助项目开发
    - ==建议70：从PyPI安装包==
    - 建议71：使用pip和yolk安装、管理包
    - 建议72：做paster创建包
    - ==建议73：理解单元测试概念== #testing
      - 有效的单元测试应该从以下几个方面考虑 \#.ol
        - 测试先行，编写单元测试应该尽量安排在项目的早期，并且测试代码应该先于被测试的代码，这样更有利于明确需求。典型的单元测试的步骤如下：\#.ol
          - 创建测试计划（Test Plan）
          - 编写测试用例，准备测试数据
          - 编写测试脚本
          - 编写被测代码，在代码完成之后执行测试脚本
          - 修正代码缺陷，重新测试直到代码可接受为止。
        - 遵循单元测试基本原则 \#.ol
          - 一致性
            collapsed:: true
            - 意味着1000次执行和一次执行的结果应该是一样的
            - 类似于currenttime=time.localtime()，产生这种不确定执行结果的语句应该尽量避免
          - 原子性
            collapsed:: true
            - 意味着单元测试的执行结果返回只有两种，True或者False，不存在部分成功、部分失败的例子
            - 如果发生这样的情况，往往是测试设计得不够合理
          - 单一职责
            collapsed:: true
            - 测试应该基于情景（scenario）和行为，而不是方法。
            - 如果一个方法对应着多种行为，应该有多个测试用例；而一个行为即使对应多个方法也只能有一个测试用例。例如下边的代码。
            - ```python
              def testMethod():
                assertTrue(behaviour1)
                assertTrue(behaviour2)
              def testMethodCheckBehaviour1()：
                assertTrue(behaviour1)
              def testMethodCheckBehaviour2():
                assertTrue(behaviour2)
              ```
          - 隔离性
            collapsed:: true
            - 不能依赖于具体的环境设置，如数据库的访问、环境变量的设置、系统的时间等；也不能依赖于其他的测试用例以及测试执行的顺序，并且无条件逻辑依赖
            - 单元测试所有的输入应该是确定的，方法的行为和结果应是可以预测的
        - 使用单元测试框架
          - PyUnit
    - 建议74：为包编写单元测试
    - ==建议75：利用测试驱动开发提高代码的可测性==
    - 建议76：使用Pylint检查代码风格
    - 建议77：进行高效的代码审查
    - 建议78：将包发布到PyPI
  - 第8章 性能剖析与优化
    - 建议79：了解代码优化的基本原则
    - 建议80：借助性能优化工具
    - 建议81：利用cProfile定位性能瓶颈
    - 建议82：使用memory_profiler 和 objgraph 剖析内存使用
    - 建议83：努力降低算法复杂度
    - 建议84：掌握循环优化的基本技巧
    - 建议85：使用生成器提高效率
    - 建议86：使用不同的数据结构优化性能
    - 建议87：充分利用set的优势
    - 建议88：使用multiprocessing克服GIL的缺陷
    - 建议89：使用线程池提高效率
    - 建议90：使用C/C++模块扩展提高性能
    - 建议91：使用 Cython 编写扩展模块
- [[Comment]]
  - 看到 建议19 的时候就感觉不对，有悖于 Effective Python 开头讲的 PEP8 规范，心想你俩要不打一架？😅 这本书还是不要再看了，建议后来的人去看后者吧（出版时间：2014，2021）