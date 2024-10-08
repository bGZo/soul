cover:: ![🖼 ](../assets/t6_YueWen_32435929.jpg){:width 225}
also:: books/dev/Rust权威指南, The Rust Programming Language
author:: Steve Klabnik, Carol Nichols
translator:: 毛靖凯 / 唐刚 / 沙渺
icon:: 📖
isbn:: 9787121387067
publisher:: 电子工业出版社
published-date:: 20200601
tags:: #rust
douban:: https://book.douban.com/subject/35081743/
weread:: https://weread.qq.com/web/bookDetail/d733256071eeeed9d7322fd
created:: [[20240102]]

- ## Contents
  - ## 版权信息
  - ## 内容简介
  - ## 译者序
  - ## 序
  - ## 前言
  - ## 致谢
  -
  -
  - ## 关于技术审校者
  - ## 第2章 编写一个猜数游戏
    collapsed:: true
    - ### 创建一个新的项目
    - ### 处理一次猜测
    - ### 生成一个保密数字
    - ### 比较猜测数字与保密数字
    - ### 使用循环来实现多次猜测
    - ### 总结
  - ## 第3章 通用编程概念
    collapsed:: true
    - ### 变量与可变性
    - ### 数据类型
    - ### 函数
    - ### 注释
    - ### 控制流
    - ### 总结
  - ## 第4章 认识所有权
    collapsed:: true
    - ### 什么是所有权
    - ### 引用与借用
    - ### 切片
    - ### 总结
  - ## 第5章 使用结构体来组织相关联的数据
    collapsed:: true
    - ### 定义并实例化结构体
    - ### 一个使用结构体的示例程序
    - ### 方法
    - ### 总结
  - ## 第6章 枚举与模式匹配
    collapsed:: true
    - ### 定义枚举
    - ### 控制流运算符match
    - ### 简单控制流if let
    - ### 总结
  - ## 第7章 使用包、单元包及模块来管理日渐复杂的项目
    collapsed:: true
    - ### 包与单元包
    - ### 通过定义模块来控制作用域及私有性
    - ### 用于在模块树中指明条目的路径
    - ### 用use关键字将路径导入作用域
    - ### 将模块拆分为不同的文件
    - ### 总结
  - ## 第8章 通用集合类型
    collapsed:: true
    - ### 使用动态数组存储多个值
    - ### 使用字符串存储UTF-8编码的文本
    - ### 在哈希映射中存储键值对
    - ### 总结
  - ## 第9章 错误处理
    collapsed:: true
    - ### 不可恢复错误与panic!
    - ### 可恢复错误与Result
    - ### 要不要使用panic!
    - ### 总结
  - ## 第10章 泛型、trait与生命周期
    collapsed:: true
    - ### 通过将代码提取为函数来减少重复工作
    - ### 泛型数据类型
    - ### trait：定义共享行为
    - ### 使用生命周期保证引用的有效性
    - ### 同时使用泛型参数、trait约束与生命周期
    - ### 总结
  - ## 第11章 编写自动化测试
    collapsed:: true
    - ### 如何编写测试
    - ### 控制测试的运行方式
    - ### 测试的组织结构
    - ### 总结
  - ## 第12章 I/O项目：编写一个命令行程序
    collapsed:: true
    - ### 接收命令行参数
    - ### 读取文件
    - ### 重构代码以增强模块化程度和错误处理能力
    - ### 使用测试驱动开发来编写库功能
    - ### 处理环境变量
    - ### 将错误提示信息打印到标准错误而不是标准输出
    - ### 总结
  - ## 第13章 函数式语言特性：迭代器与闭包
    collapsed:: true
    - ### 闭包：能够捕获环境的匿名函数
    - ### 使用迭代器处理元素序列
    - ### 改进I/O项目
    - ### 比较循环和迭代器的性能
    - ### 总结
  - ## 第14章 进一步认识Cargo及crates.io
    collapsed:: true
    - ### 使用发布配置来定制构建
    - ### 将包发布到crates.io上
    - ### Cargo工作空间
    - ### 使用cargo install从crates.io上安装可执行程序
    - ### 使用自定义命令扩展Cargo的功能
    - ### 总结
  - ## 第15章 智能指针
    collapsed:: true
    - ### 使用Box<T>在堆上分配数据
    - ### 通过Deref trait将智能指针视作常规引用
    - ### 借助Drop trait在清理时运行代码
    - ### 基于引用计数的智能指针Rc<T>
    - ### RefCell<T>和内部可变性模式
    - ### 循环引用会造成内存泄漏
    - ### 总结
  - ## 第16章 无畏并发
    collapsed:: true
    - ### 使用线程同时运行代码
    - ### 使用消息传递在线程间转移数据
    - ### 共享状态的并发
    - ### 使用Sync trait和Send trait对并发进行扩展
    - ### 总结
  - ## 第17章 Rust的面向对象编程特性
    collapsed:: true
    - ### 面向对象语言的特性
    - ### 使用trait对象来存储不同类型的值
    - ### 实现一种面向对象的设计模式
    - ### 总结
  - ## 第18章 模式匹配
    collapsed:: true
    - ### 所有可以使用模式的场合
    - ### 可失败性：模式是否会匹配失败
    - ### 模式语法
    - ### 总结
  - ## 第19章 高级特性
    collapsed:: true
    - ### 不安全Rust
    - ### 高级trait
    - ### 高级类型
    - ### 高级函数与闭包
    - ### 宏
    - ### 总结
  - ## 第20章 最后的项目：构建多线程Web服务器
    collapsed:: true
    - ### 构建单线程Web服务器
    - ### 把单线程服务器修改为多线程服务器
    - ### 优雅地停机与清理
    - ### 总结
  - ## 附录A 关键字
    collapsed:: true
    - ### 当前正在使用的关键字
    - ### 将来可能会使用的保留关键字
    - ### 原始标识符
    - ## 附录B 运算符和符号
    - ### 运算符
    - ### 非运算符符号
  - ## 附录C 可派生trait
    collapsed:: true
    - ### 面向程序员格式化输出的Debug
    - ### 用于相等性比较的PartialEq和Eq
    - ### 使用PartialOrd和Ord进行次序比较
    - ### 使用Clone和Copy复制值
    - ### 用于将值映射到另外一个长度固定的值的Hash
    - ### 用于提供默认值的Default
  - ## 附录D 有用的开发工具
    collapsed:: true
    - ### 使用rustfmt自动格式化代码
    - ### 使用rustfix修复代码
    - ### 使用Clippy完成更多的代码分析
    - ### 使用Rust语言服务器来集成IDE
  - ## 附录E 版本