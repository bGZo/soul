title:: algorithms4E/fundamentals

- ### 1.1 编程模型  Programming Model
  collapsed:: true
  - 基础编程模型: **描述和实现算法所用到的语言特性、软件库和操作系统特性**
    id:: 6263bdc1-96b9-4626-90f4-d55164d5ac45
  - Java程序的基本结构
    collapsed:: true
    id:: 6263bdc1-031e-4494-85a4-8469f4d28843
    - 七种语法 -> 创建 静态方法库 / 定义数据类型
      collapsed:: true
      - 原始数据类型
        - 被组合为类似于数学公式定义的表达式。
      - 语句(6)
        - 声明
        - 赋值
        - 条件
        - 循环
        - 调用
        - 返回
      - 数组
        - 声明数组的名字和类型
        - 创建数组
        - 初始化数组元素
      - 静态方法(函数(性质相似))
        - 封装并重用代码
          - 模块开发
        - 静态方法
          - 一组在被调用时会被顺序执行的语句
          - 由签名 (关键字public static以及函数的返回值，方法名以及一串各种类型的参数) + 函数体 (即包含在花括号中的代码) 组成的
          - ![image.png](../assets/image_1649011612654_0.png)
        - 调用
          - 仅由一个方法调用和一个分号组成的语句一般用于产生副作用, 如 `Array.sort();`
        - 性质
          - 方法的参数按值传递
            - 方法处理的是参数的值，而非参数本身。这种方式产生的结果是在静态方法中改变一个参数变量的值对调用者没有影响
          - 方法名可以被重载
          - 方法只能返回一个值，但可以包含多个返回语句
          - 方法可以产生副作用
        - 递归
          - 总有一个最简单的情况——方法的第一条语句总是一个包含return的条件语句
          - 调用总是去尝试解决一个规模更小的子问题，这样递归才能收敛到最简单的情况
          - 调用的父问题和尝试解决的子问题之间不应该有交集。
        - 基础编程模型
          - Java开发的基本模式是编写一个静态方法库（包含一个main()方法）来完成一个任务
        - 模块化编程
          - 构造许多个静态方法库（模块），一个库中的静态方法也能够调用另一个库中定义的静态方法
            - 程序整体的代码量很大时，每次处理的模块大小仍然适中；
            - 可以共享和重用代码而无需重新实现；
            - 很容易用改进的实现替换老的实现；
            - 可以为解决编程问题建立合适的抽象模型；
            - 缩小调试范围
        - 单元测试
          - Java编程的最佳实践之一就是每个静态方法库中都包含一个main()函数来测试库中的所有方法（有些编程语言不支持多个main()方法，因此不支持这种方式）
          - 每个模块的main()方法至少应该调用模块中的其他代码并在某种程度上保证它的正确性
        - 外部库
          - 系统标准库 `java.lang.＊`
          - 导入的系统库，例如 `java.util.Arrays`
            - 每个标准的Java版本中都含有上千个这种类型的库，不过本书中我们用到的并不多。要在程序的开头使用import语句导入才能使用这些库（我们也是这样做的）
          - 本书中的其他库：例如，其他程序也可以使用BinarySearch的rank()方法。要使用这些库，请在本书的网站上下载它们的源代码并放入你的工作目录中。
          - 材An Introduction to Programming inJava: An Interdisciplinary Approach）开发的标准库Std＊
      - 字符串
        - 一连串的操作
        - 自动转换
          - 如果加号（+）的一个参数是字符串，那么Java会自动将其他参数都转换为字符串（如果它们不是的话）
      - 标准输入/输出
        - 程序与外界联系的桥梁
        - 在我们的模型中，Java程序可以从命令行参数或者一个名为标准输入流的抽象字符流中获得输入，并将输出写入另一个名为标准输出流的字符流中。
        - 默认情况下，命令行参数、标准输入和标准输出是和应用程序绑定的，而应用程序是由能够接受命令输入的操作系统或是开发环境所支持
        - 20世纪70年代早期的Unix系统已经证明我们可以用这个模型方便直接地和程序以及数据进行交互。我们在经典的模型中加入了一个标准绘图模块用来可视化表示对数据的分析
        - ![image.png](../assets/image_1649015726789_0.png)
        -
      - **数据抽象**
        - 封装和重用代码
          - 定义**非原始数据类型**
            - 支持**面向对象编程**
    - API, 应用程序编程接口
      collapsed:: true
      id:: 6263bdc1-75e8-407e-b43c-c076ab56fd5e
      - 记录库方法的用法并供其他人参考的文档
        - 统一使用 API 列出本书中使用的每个库方法名称、签名和简短的描述
        - 用 用例 来指代调用另一个库中的方法的程序，用实现描述实现了某个API方法的Java代码
      - Java库
        - 成千上万个库的在线文档是Java发布版本的一部分
          id:: 6249f31f-c0cf-408b-84cd-1c2c904930d1
      - 编写的库
        - 编写用例，在实现中将计算过程分解成可控的部分
        - 明确静态方法库和与之对应的API（或者多个库的多个API）
        - 实现API和一个能够对方法进行独立测试的main()函数
      - 目的
        - 将调用和实现分离
          - 除了API中给出的信息，调用者不需要知道实现的其他细节，而实现也不应考虑特殊的应用场
  - 原始数据类型与表达式
    collapsed:: true
    - 只要能够指定值域和在此值域上的操作，就能定义一个数据类型
    - 运算符和偶尔需要考虑到的各种异常情况
    - 表达式
      collapsed:: true
      - 中缀表达式
      - 一般来说，相同优先级的运算符的运算顺序是从左至右。与在正常的算数表达式中一样，使用括号能够改变这些规则
    - 类型转换
      collapsed:: true
      - 高级的数据类型
    - 比较
    - 其他原始类型
      collapsed:: true
      - int型能够表示232个不同的值，用一个字长32位的机器字即可表示（虽然现在的许多计算机有字长64位的机器字，但int型仍然是32位）
      - 8位整数，及其算术运算符 (byte)
    -
  - 简便记法
    collapsed:: true
    - 声明并初始化
    - 隐式赋值
    - 单语句代码段
    - for语句 -> while
  - 数组
    collapsed:: true
    - 创建并初始化数组
      - 我们需要在运行时明确地创建数组的原因是Java编译器在编译时无法知道应该为数组预留多少空间（对于原始类型则可以）
      - 在代码中使用数组时，一定要依次声明、创建并初始化数组。忽略了其中的任何一步都是很常见的编程错误
    - 简化写法
      - 因为在一个Java数组中double类型的变量的默认初始值都是0.0，但如果你想使用不同的初始值，那么就需要使用for循环了。数值类型的默认初始值是0，布尔型的默认初始值是false。例子中的第三种方式用花括号将一列由逗号分隔的值在编译时将数组初始化
    - 使用数组
    - 起别名
      - 数组名表示的是整个数组——如果我们将一个数组变量赋予另一个变量，那么两个变量将会指向同一个数组
    - 二维数组
    - 静态方法
      id:: 625d9efa-34e7-44d2-bece-5b2f182d4d1f
      - 在许多语言中，静态方法被称为函数，因为它们和数学函数的性质类似
      - 每个静态方法都是由签名（关键字public static以及函数的返回值，方法名以及一串各种类型的参数）和函数体（即包含在花括号中的代码）组成的
      - 调用静态方法
        collapsed:: true
        - 仅由一个方法调用和一个分号组成的语句一般用于产生副作用
      - 方法的性质
        collapsed:: true
        - 方法的参数按值传递
          - 在方法中参数变量的使用方法和局部变量相同，唯一不同的是参数变量的初始值是由调用方提供的。方法处理的是参数的值，而非参数本身。这种方式产生的结果是在静态方法中改变一个参数变量的值对调用者没有影响。本书中我们一般不会修改参数变量。值传递也意味着数组参数将会是原数组的别名（见1.1.5.4节）——方法中使用的参数变量能够引用调用者的数组并改变其内容（只是不能改变原数组变量本身）。例如，Arrays.sort()将能够改变通过参数传递的数组的内容，将其排序。
        - 方法名可以被重载
          - 例如，Java的Math包使用这种方法为所有的原始数值类型实现了Math.abs()、Math.min()和Math.max()函数。重载的另一种常见用法是为函数定义两个版本，其中一个需要一个参数而另一个则为该参数提供一个默认值
        - 方法只能返回一个值，但可以包含多个返回语句：一个Java方法只能返回一个值，它的类型是方法签名中声明的类型。静态方法第一次执行到一条返回语句时控制权将会回到调用代码中。尽管可能存在多条返回语句，任何静态方法每次都只会返回一个值，即被执行的第一条返回语句的参数
        - 方法可以产生副作用：方法的返回值可以是void，这表示该方法没有返回值。返回值为void的静态函数不需要明确的返回语句，方法的最后一条语句执行完毕后控制权将会返回给调用方。我们称void类型的静态方法会产生副作用（接受输入、产生输出、修改数组或者改变系统状态）。例如，我们的程序中的静态方法main()的返回值就是void，因为它的作用是向外输出。技术上来说，数学方法的返回值都不会是void（Math.random()虽然不接受参数但也有返回值
      - 递归
      - 基础编程模型
        - Java开发的基本模式是编写一个静态方法库（包含一个main()方法）来完成一个任务。
      - 模块化编程 [[modular]]
        - 构造许多个静态方法库（模块），一个库中的静态方法也能够调用另一个库中定义的静态方法
        - 程序整体的代码量很大时，每次处理的模块大小仍然适中；
        - 可以共享和重用代码而无需重新实现
        - 很容易用改进的实现替换老的实现
        - 可以为解决编程问题建立合适的抽象模型
        - 缩小调试范围（ ((625d9fb5-755e-4607-8fd8-d3fa74e17f74)) 的讨论）
      - 单元测试
        id:: 625d9fb5-755e-4607-8fd8-d3fa74e17f74
        - Java编程的最佳实践之一就是每个静态方法库中都包含一个main()函数来测试库中的所有方法（有些编程语言不支持多个main()方法，因此不支持这种方式）
        - 每个模块的main()方法至少应该调用模块中的其他代码并在某种程度上保证它的正确性
      - 外部库
      - API
        - 记录库方法的用法并供其他人参考的文档
        - 统一使用应用程序编程接口（API）的方式列出本书中使用的每个库方法名称、签名和简短的描述。我们用用例来指代调用另一个库中的方法的程序，用实现描述实现了某个API方法的Java代码。
        - 举例
          - 为了科学计算以及算法的开发、学习和应用，我们也开发了若干库来提供一些实用的功能。这些库大多用于处理输入输出。我们也会使用以下两个库来测试和分析我们的实现。第一个库扩展了Math.random()方法（见表1.1.8），以根据不同的概率密度函数得到随机值；第二个库则支持各种统计计算
            - 这些方法所实现的抽象层有助于我们将精力集中在实现和测试本书中的算法，而非生成随机数或是统计计算。每次都自己写完成相同计算的代码，不如直接在用例中调用它们要更简洁易懂
            - 方法库会经过大量测试，覆盖极端和罕见的情况，是我们可以信任的。这样的实现需要大量的代码。例如，我们经常需要使用的各种数据类型的实现，又比如Java的Arrays库针对不同数据类型对sort()进行了多次重载。
        - 你自己编写的库
          - 编写用例，在实现中将计算过程分解成可控的部分
          - 明确静态方法库和与之对应的API（或者多个库的多个API）
          - 实现API和一个能够对方法进行独立测试的main()函数
        - API的目的是将调用和实现分离：除了API中给出的信息，调用者不需要知道实现的其他细节，而实现也不应考虑特殊的应用场
      - 字符串
        - 字符串拼接
        - 类型转换
        - 自动转换
        - 命令行参数
    - 输入输出
      - 在我们的模型中，Java程序可以从命令行参数或者一个名为标准输入流的抽象字符流中获得输入，并将输出写入另一个名为标准输出流的字符流中。
      - 默认情况下，命令行参数、标准输入和标准输出是和应用程序绑定的，而应用程序是由能够接受命令输入的操作系统或是开发环境所支持
      - 20世纪70年代早期的Unix系统已经证明我们可以用这个模型方便直接地和程序以及数据进行交互。我们在经典的模型中加入了一个标准绘图模块用来可视化表示对数据的分析
      - 命令和参数
      - 标准输出
        collapsed:: true
        - print()方法会将它的参数放到标准输出中；println()方法会附加一个换行符；printf()方法能够格式化输出（见1.1.9.3节）。Java在其System.out库中提供了类似的方法，但我们会用StdOut库来统一处理标准输入和输出（并进行了一些技术上的改进）
      - 格式化输出
        collapsed:: true
        - printf()方法接受两个参数。第一个参数是一个格式字符串，描述了第二个参数应该如何在输出中被转换为一个字符串
        - 在%和转换代码之间可以插入一个整数来表示转换之后的值的宽度，即输出字符串的长度
        - 使用printf()方法时需要记住的最重要的一点就是，格式字符串中的转换代码和对应参数的数据类型必须匹配
      - 标准输入
        collapsed:: true
        - 可能是一系列由空白字符分隔的值（空格、制表符、换行符等）
        - 默认状态下系统会将标准输出定向到终端窗口——你输入的内容就是输入流（由＜ctrl-d＞或＜ctrl-z＞结束，取决于你使用的终端应用程序）
        - 这些值可能是String或是Java的某种原始类型的数据。标准输入流最重要的特点是这些值会在你的程序读取它们之后消失。只要程序读取了一个值，它就不能回退并再次读取它
        - 这个特点产生了一些限制，但它反映了一些输入设备的物理特性并简化了对这些设备的抽象。有了输入流模型，这个库中的静态方法大都是自文档化的（它们的签名即说明了它们的用途）。右侧列出了StdIn的一个用例
      - 重定向与管道
        collapsed:: true
        - 这条命令将RandomSeq的标准输出和Average的标准输入指定为同一个流
        - 这种差别影响非常深远，因为它突破了我们能够处理的输入输出流的长度限制
        - In和Out库提供了一些静态方法，来实现向文件中写入或从文件中读取一个原始数据类型（或String类型）的数组的抽象
      - 标准绘图库（基本方法）
        collapsed:: true
        - 标准绘图库很简单：我们可以将它想象为一个抽象的能够在二维画布上画出点和直线的绘图设备
        - StdDraw.line()能够根据参数的坐标画出一条连接点（x0,y0）和点（x1, y1）的线段，StdDraw.point()能够根据参数坐标画出一个以（x, y）为中心的点，等等，如图1.1.6所示。几何图形可以被填充（默认为黑色）。默认的比例尺为单位正方形（所有的坐标均在0和1之间）。标准的实现会将画布显示为屏幕上的一个窗口，点和线为黑色，背景为白色。
      -
  - ---
  - [[java/quick-refs]]
    - 什么是Java的字节码？
      collapsed:: true
      - 它是程序的一种低级表示，可以运行于Java的虚拟机。将程序抽象为字节码可以保证Java程序员的代码能够运行在各种设备之上。
    - Java允许整型溢出并返回错误值的做法是错误的。难道Java不应该自动检查溢出吗？
      collapsed:: true
      - 它们之所以被称为原始数据类型就是因为缺乏此类检查。避免此类问题并不需要很高深的知识。我们会使用int类型表示较小的数（小于10个十进制位）而使用long表示10亿以上的数
    - Math.abs(-2147483648) 的返回值是什么？
      collapsed:: true
      - -2147483648。这个奇怪的结果（但的确是真的）就是整数溢出的典型例子
    - 如何才能将一个double变量初始化为无穷大？
      collapsed:: true
      - 可以使用Java的内置常数：Double.POSITIVE_INFINITY和Double.NEGATIVE_INFINITY
    - 如果使用一个变量前没有将它初始化，会发生什么？
      collapsed:: true
      - 编译异常
    - Java表达式1/0和1.0/0.0的值是什么？
      collapsed:: true
      - 第一个表达式会产生一个运行时除以零异常（它会终止程序，因为这个值是未定义的）；第二个表达式的值是Infinity（无穷大）
    - 能够使用＜和＞比较String变量吗？
      collapsed:: true
      - 不行，只有原始数据类型定义了这些运算符
    - 负数的除法和余数的结果是什么？
      collapsed:: true
      - 表达式a/b的商会向0取整；a % b的余数的定义是(a/b)＊b + a % b恒等于a。例如-14/3和14/-3的商都是-4，但-14 % 3是-2，而==14 % -3是2==
    - 为什么使用(a && b)而非(a & b)？
      collapsed:: true
      - 10|6的值为14
    - 有些Java程序员用int a[]而不是int[] a来声明一个数组。这两者有什么不同？
      collapsed:: true
      - 在Java中，两者等价且都是合法的。前一种是C语言中数组的声明方式。后者是Java提倡的方式，因为变量的类型int[]能更清楚地说明这是一个整型的数组
    - 为什么数组的起始索引是0而不是1？
      collapsed:: true
      - 这个习惯来源于机器语言，那时要计算一个数组元素的地址需要将数组的起始地址加上该元素的索引。将起始索引设为1要么会浪费数组的第一个元素的空间，要么会花费额外的时间来将索引减1
    - 我的程序能够重新读取标准输入中的值吗
      collapsed:: true
      - 不行，你只有一次机会，就好像你不能撤销println()的结果一样。
    - 如果我的程序在标准输入为空之后仍然尝试读取，会发生什么
      collapsed:: true
      - StdIn.isEmpty()能够帮助你检查是否还有可用的输入以避免这种错误。
- ### 1.2 数据抽象 (学习定义和使用数据类型)
  collapsed:: true
  - **数据类型 (DT)**
    collapsed:: true
    - 一组值和一组对这些值的操作的集合
    - 它的核心概念是对象，即保存了某个数据类型的值的实体
    - 如果只有Java的原始数据类型，我们的程序会在很大程度上被限制在算术计算上
    - [[Java]] 引用 -> 能编写操作字符串、图像、声音以及Java的标准库中或者本书的网站上的数百种抽象类型的程序
  - **抽象数据类型 (ADT)**
    collapsed:: true
    - 一种能够对使用者隐藏数据表示的数据类型
    - Java类来实现抽象数据类型 == 用一组静态方法实现一个函数库
      - 抽象数据类型定义 vs 静态方法库
        id:: 625d9259-f12c-413f-9a8b-637e8a19b707
        - 同
          - 两者的实现均为Java类
          - 实例方法可能接受0个或多个指定类型的参数, 由括号表示并由逗号分隔
          - 它们可能会返回一个指定类型的值，也可能不会 (void)
        - 异
          - API中可能会出现若干个名称和类名相同且没有返回值的构造函数
          - 实例方法不需要static关键字。它们不是静态方法——它们的目的就是操作该数据类型中的值
          - 某些实例方法的存在是为了尊重Java的习惯——我们将此类方法称为继承的方法并在API中将它们显示为灰色。
    - 特点
      - 将数据和函数的实现关联，并将数据的表示方式隐藏起来
        - 使用抽象数据类型时，我们的注意力集中在API描述的操作上而不会去关心数据的表示
        - 在实现抽象数据类型时，我们的注意力集中在数据本身并将实现对该数据的各种操作
      - 抽象数据类型之所以重要是因为在程序设计上它们支持**封装**
  - 使用抽象数据类型
    collapsed:: true
    - 抽象数据类型的API
      collapsed:: true
      - API: 应用程序编程接口
        - 说明抽象数据类型的行为
        - 它将列出所有构造函数和实例方法（即操作）并简要描述它们的功用
      - ((625d9259-f12c-413f-9a8b-637e8a19b707))
    - 继承的方法
      collapsed:: true
      - 任意数据类型都能通过在API中包含特定的方法从Java的内在机制中获益
        - Java中的所有数据类型都会继承toString()方法来返回用String表示的该类型的值
        - Java会在用+运算符将任意数据类型的值和String值连接时调用该方法
          - 该方法的默认实现并不实用（它会返回用字符串表示的该数据类型值的内存地址），因此我们常常会提供实现来重载默认实现，并在此时在API中加上toString()方法
        - 此类方法的例子还包括equals()、compareTo()和hashCode()
    - 对象
      collapsed:: true
      - 特性
        - 状态
          - 对象的状态即数据类型中的值
        - 标识
          - 对象的标识能够将一个对象区别于另一个对象
          - 可以认为对象的标识就是它在内存中的位置
        - 行为
          - 对象的行为就是数据类型的操作
      - 数据类型的实现的唯一职责就是维护一个对象的身份，这样用例代码在使用数据类型时只需遵守描述对象行为的API即可，而无需关注对象状态的表示方法。
      - 对象的状态可以为用例代码提供信息，或是产生某种副作用，或是被数据类型的操作所改变。
      - 数据类型的值的表示细节和用例代码是无关的。
      - 引用是访问对象的一种方式。
        - Java使用术语引用类型以示和原始数据类型（变量和值相关联）的区别。不同的Java实现中引用的实现细节也各不相同，但可以认为引用就是内存地址
    - 创建对象
      collapsed:: true
      - 每当用例调用了new()，系统都会
        - 为新的对象分配内存空间
        - 调用构造函数初始化对象中的值
        - **返回该对象的一个引用** (没有返回值的原因)
    - 调用实例方法
      collapsed:: true
      - 实例方法拥有我们在静态方法的所有性质
        - 参数按值传递
        - 方法名可以被重载
        - 方法可以有返回值
        - 它们也许还会产生一些副作用
      - 方法的每次触发都是和一个对象相关的
    - 使用对象
      collapsed:: true
      - 声明该类型的变量，以用来引用对象
      - 使用**关键字new触发能够创建该类型的对象的一个构造函数**
      - 使用变量名在语句或表达式中调用实例方法
    - 赋值语句
      collapsed:: true
      - 在Java中，**别名**是bug的常见原因
    - 将对象作为参数
      collapsed:: true
      - Java将参数值的一个副本从调用端传递给了方法，这种方式称为**按值传递**
        - 方法无法改变调用端变量的值
      - 每当使用引用类型作为参数时我们创建的都是别名，所以就必须小心
        - 这种约定将会**传递引用的值 (复制引用)**，也就是传递对象的引用
    - 将对象作为返回值
      collapsed:: true
      - Java中的方法只能有一个返回值
        - 有了对象我们的代码实际上就能**返回多个值**
      -
    - 数组也是对象
      collapsed:: true
      - 数组传递的是引用
      - shuffle() 方法
    - 对象的数组
  - 抽象数据类型举例
    collapsed:: true
    - 实际上，我们编写的每一个Java程序实现的都是某种数据类型（或是一个静态方法库）
      collapsed:: true
      - `java.lang.＊`中的标准系统抽象数据类型，可以被任意Java程序调用
      - Java标准库中的抽象数据类型
        collapsed:: true
        - 如`java.swt`、`java.net`和`java.io`
        - 它们也可以被任意Java程序调用，但需要import语句
      - I/O处理类抽象数据类型，和StdIn和StdOut类似
        collapsed:: true
        - 允许我们处理多个输入输出流
      - 面向数据类抽象数据类型
        collapsed:: true
        - 通过封装数据的表示简化数据的组织和处理
      - 集合类抽象数据类型
        collapsed:: true
        - 简化对同一类型的一组数据的操作
          - Bag、Stack和Queue类
          - 优先队列（PQ）及其相关的类
          - 符号表（ST）和集合（SET）以及相关的类
      - 面向操作的抽象数据类型
        collapsed:: true
        - 分析各种算法
      - 图算法相关的抽象数据类型
        collapsed:: true
        - 包括一些用来封装各种图的表示的面向数据的抽象数据类型，和一些提供图的处理算法的面向操作的抽象数据类型
    - ![image.png](../assets/image_1650300587940_0.png)
    - ![image.png](../assets/image_1650300601433_0.png)
    - ![image.png](../assets/image_1650300609797_0.png)
    - ![image.png](../assets/image_1650300618655_0.png)
    -
  - 更多抽象数据类型的实现
    - 封装日期的抽象数据类型
      id:: 6257eab8-071b-459e-bd2a-64544c6911e9
      - ![image.png](../assets/image_1650275092540_0.png)
        - `value=512y+32m+d` 是假设所有的输入年份都为有效的。
          via: https://segmentfault.com/q/1010000012793695
          - 一个int类型的存储长度为32位。
            - `1-5` 位存储 `d` 的值，因为 `0<1<=d<=31`。即 $$2^{5}$$
            - `6-9` 位存储 `m` 的值，因为 `0<1<=m<=12<15`。即 $$2^{4}$$
            - `10-31` 位存储 `y` 的值 ( int 为有符号整数，32位为符号位）
        - diff
          - 我们对日期的**隐式假设** ???
          - 右侧的实现中保存数据类型的值所需的空间较少
            - 代价: 在向用例按照约定的格式提供这些值时花费的时间更多 (一两次算术运算)
        - `euqals` logical
          - 如果该对象的引用和参数对象的引用相同，返回true。这项测试在成立时能够免去其他所有测试工作
          - 如果参数为空（null），根据约定返回false（还可以避免在下面的代码中使用空引用）
          - 如果两个对象的类不同，返回false。要得到一个对象的类，可以使用getClass()方法。请注意我们会使用==来判断Class类型的对象是否相等，因为同一种类型的所有对象的getClass()方法一定能够返回相同的引用。❏将参数对象的类型从Object转换到Date（因为前一项测试已经通过，这种转换必然成功）。❏如果任意实例变量的值不相同，返回false。对于其他类，等价性测试方法的定义可能不同。例如，我们只有在两个Counter对象的count变量相等时才会认为它们相等。
          - ![image.png](../assets/image_1650281314930_0.png)
          -
      - 这个例子的主要意思是说明我们在API中极少完整地指定对实现的要求（一般来说我们都会尽力而为，这里还可以做得更好）
      - 在实现中使用数据抽象的一个关键优势是我们可以将一种实现替换为另一种而无需改变用例的任何代码
      - 我们可能需要维护两种实现，一种适用于某些用例，另一种适用于另一些用例
      - 同一份API的两种不同实现在同一个用例中的性能表现
      - Java有许多高级语言特性来保证在无需修改用例代码的情况下维护多个实现，但我们很少会使用它们，因为即使Java专家使用起它们来也十分困难（有时甚至是有争议的），尤其是同我们极为需要的其他高级语言特性（泛型和迭代器）一起使用时
    - 二分查找重写为一段面向对象的程序
      - ![image.png](../assets/image_1650277044464_0.png)
        -
      -
    - 累加器
      - 避免一种存储所有数据值的实现可能会使调用它的应用程序用光所有内存
    - 可视化的累加器
      - 它的构造函数的签名不同且产生了一种不同的副作用
      - 仔细而完整地设计API，并且一旦定型就不愿再对它做任何改动
  - 数据类型的设计
    collapsed:: true
    - 抽象数据类型是一种向用例隐藏内部表示的数据类型
    - 封装
      collapsed:: true
      - 实现了模块化编程，它允许我们
        - 独立开发用例和实现的代码
        - 切换至改进的实现而不会影响用例的代码
        - 支持尚未编写的程序（对于后续用例，API能够起到指南的作用）
        - 封装同时也隔离了数据类型的操作，这使我们可以
          - 限制潜在的错误
          - 在实现中添加一致性检查等调试工具
          - 确保用例代码更明晰
      - 一个封装的数据类型可以被任意用例使用，因此它扩展了Java语言
      - 模块化编程成功的关键在于保持模块之间的独立性
    - 设计API
      collapsed:: true
      - 一份API应该能够清楚地说明所有可能的输入和副作用
      - 我们应该先写出检查实现是否与API相符的程序
        collapsed:: true
        - 不幸的是，计算机科学理论中一个叫做说明书问题（specification problem）的基础结论说明这个目标是不可能实现的
      - 这样一份说明书应该用一种类似于编程语言的形式语言编写
        collapsed:: true
        - 从数学上可以证明，判定这样两个程序进行的计算是否相同是不可能的
        - 因此，我们的API将是与抽象数据类型相关联的值以及一系列构造函数和实例方法的目的和副作用的自然语言描述
      - 这些宏观概述之中也隐藏着每一份API设计都可能落入的无数陷阱
        collapsed:: true
        - API可能会难以实现：实现的开发非常困难，甚至不可能
        - API可能会难以使用：用例代码甚至比没有API时更复杂
        - API的范围可能太窄：缺少用例所需的方法
        - API的范围可能太宽：包含许多不会被任何用例调用的方法
          - 这种缺陷可能是最常见的，并且也是最难以避免的
          - API的大小一般会随着时间而增长，因为向已有的API中添加新方法很简单，但在不破坏已有用例程序的前提下从中删除方法却很困难
        - API可能会太粗略：无法提供有效的抽象
        - API可能会太详细：抽象过于细致或是发散而无法使用
        - API可能会过于依赖某种特定的数据表示：用例代码可能会因此无法从数据表示的细节中解脱出来
          - 要避免这种缺陷也是很困难的，因为数据表示显然是抽象数据类型实现的核心。
      - > 只为用例提供它们所需要的
    - 算法与抽象数据类型
      collapsed:: true
      - 白名单应用是众多二分查找算法的用例之一
        ![image.png](../assets/image_1650277044464_0.png)
      -
    - 接口继承
      collapsed:: true
      - 在某些情况下Java的习惯用法鼓励我们使用接口：我们用它们进行比较和迭代
        ![image.png](../assets/image_1650301193874_0.png)
    - 实现继承
      collapsed:: true
      - 子类继承被系统程序员广泛用于编写所谓可扩展的库——任何一个程序员（包括你）都能为另一个程序员（或者也许是一个系统程序员团队）创建的库添加方法
      - 它和接口继承之间的优劣还没有定论
      - 我们会避免使用它，因为它会破坏封装。
      - 每个类都是Java的Object类的子类。这种结构意味着每个类都含有getClass()、toString()、equals()、hashCode()
    - 字符串表示的习惯
      collapsed:: true
      - toString()方法的实现通常很简单，只需隐式调用（通过+）每个实例变量的toString()方法即可
    - 封装类型
    - 等价性
      collapsed:: true
      - 两个对象相等意味着什么？
        - 我们检测的是它们的标识是否相同，即引用是否相同
        - 当我们在定义自己的数据类型时，比如Date或Transaction，需要重载equals()方法
      - Java约定equals()必须是一种等价性关系。它必须具有
        - 自反性，x.equals(x)为true
        - 对称性，当且仅当y.equals(x)为true时，x.equals(y)返回true
        - 传递性，如果x.equals(y)和y.equals(z)均为true, x.equals(z)也将为true
      - 它必须接受一个Object为参数并满足以下性质
        - 一致性，当两个对象均未被修改时，反复调用x.equals(y)总是会返回相同的值
        - 非空性，x.equals(null)总是返回false
      -
    - 内存管理
      collapsed:: true
      - 孤儿
      - 自动内存管理。它通过记录孤儿对象并将它们的内存释放到内存池中将程序员从管理内存的责任中解放出来。这种回收内存的方式叫做垃圾回收
      - Java的一个特点就是它不允许修改引用的策略。这种策略使Java能够高效自动地回收垃圾
    - 不可变性
      collapsed:: true
      - 该类型的对象中的值在创建之后就无法再被改变
      - 试图改变final变量的值的代码将会产生一个编译时错误
      - 数据类型是否可变是一个重要的设计决策，它取决于当前的应用场景
    - 契约式设计 [[contract]]
      id:: 625d99cb-d487-49d6-8c28-e9b4cd15ad01
      collapsed:: true
      - 异常（Exception），一般用于处理不受我们控制的不可预见的错误
      - 断言（Assertion），验证我们在代码中做出的一些假设。
    - 异常与错误
      collapsed:: true
      - 快速出错
        - 一旦出错就立刻抛出异常，使定位出错位置更容易
    - 断言
      collapsed:: true
      - 在命令行下使用-enableassertions标志（简写为-ea）启用断言
      - 调试：程序在正常操作中不应该依赖断言，因为它们可能会被禁用
      - 系统编程课程会学习使用断言来保证代码永远不会被系统错误终止或是进入死循环
      - 一种叫做 ((625d99cb-d487-49d6-8c28-e9b4cd15ad01)) 的编程模型采用的就是这种思想
        - 数据类型的设计者需要说明前提条件（用例在调用某个方法前必须满足的条件）、后置条件（实现在方法返回时必须达到的要求）和副作用（方法可能对对象状态产生的任何其他变更）。在开发过程中，这些条件可以用断言进行测试
      -
    - 如果你总是抱怨编程语言的特性，那么你只能自己设计编程语言了
    - 通常你都能够通过构造易于移植到其他编程语言的抽象层来简化用例代码并进行自我保护。设计数据类型是你的主要目标，从而使大多数工作都能在抽象层次完成，且和手头的问题匹配
  - [[java/quick-refs]]
    collapsed:: true
    - 我在哪里能够找到Java如何实现引用和进行垃圾收集的细节？
      collapsed:: true
      - Java系统的实现各有不同
        - 实现引用
          - 使用指针（机器地址）
            - 访问数据的速度更快
          - 句柄（指针的指针）
            - 更好地实现垃圾回收
    - 实现继承有什么问题？(2)
      collapsed:: true
      - 父类的任何改动都会影响它的所有子类。子类的开发不可能和父类无关
        - 事实上，子类是完全依赖于父类的。这种问题被称为脆弱的基类问题
      - 子类代码可以访问所有实例变量，因此它们可能会扭曲父类代码的意图
    - 弃用（deprecated）的方法？
      collapsed:: true
      - 不再被支持但为了保持兼容性而留在API中的方法叫做弃用的方法
      - 随着时间的推移，这种方式显然会使API更复杂。有时候甚至整个类都会被弃用
        - Java为了更好地支持国际化就将它的java. util.Date标记为弃用
- ### 1.3 背包、队列和栈
  collapsed:: true
  - API
    collapsed:: true
    - [[generic]] 泛型
      collapsed:: true
      - 类名后的＜Item＞记号将Item定义为一个类型参数，它是一个象征性的占位符，表示的是用例将会使用的某种具体数据类型。可以将Stack＜Item＞理解为某种元素的栈
      - 有了泛型，我们只需要一份API（和一次实现）就能够处理所有类型的数据，甚至是在未来定义的数据类型
    - 自动装箱
      collapsed:: true
      - Java会自动在引用类型和对应的原始数据类型之间进行转换
    - 可迭代的集合类型
      collapsed:: true
      - 支持迭代需要在实现中添加额外的代码，但这些工作是值得的
    - 背包
      collapsed:: true
      - 一种不支持从中删除元素的集合数据类型
        ![image.png](../assets/image_1650354530595_0.png)
        - 目的: 帮助用例收集元素并迭代遍历所有收集到的元素
      - 元素的处理顺序不重要
      - ```java
        public class Stats
        {
            public static void main(String[] args)
            {
              Bag＜Double＞ numbers = new Bag＜Double＞();
              while (! StdIn.isEmpty())
                  numbers.add(StdIn.readDouble());
              int N = numbers.size();
              double sum = 0.0;
              for (double x : numbers)
                  sum += x;
              double mean = sum/N;
              sum = 0.0;
              for (double x : numbers)
                  sum += (x - mean)＊(x - mean);
              double std = Math.sqrt(sum/(N-1));
              StdOut.printf("Mean: %.2f\n", mean);
              StdOut.printf("Std dev: %.2f\n", std);
            }
        }
        ```
    - (先进先出) 队列
      collapsed:: true
      - 基于先进先出（FIFO）策略的集合类型
        ![image.png](../assets/image_1650354511678_0.png)
      - 队列是许多日常现象的自然模型，它也是无数应用程序的核心
        - 在用集合保存元素的同时保存它们的**相对顺序**：使它们入列顺序和出列顺序相同
        - #[[question]] 我们的In类的静态方法readInts()的一种实现。
          
          这个方法为用例解决的问题是用例无需预先知道文件的大小即可将文件中的所有整数读入一个数组中
          
          我们首先将所有的整数读入队列中，然后使用Queue的size()方法得到所需数组的大小，创建数组并将队列中的所有整数移动到数组中。队列之所以合适是因为它能够将整数按照文件中的顺序放入数组中（如果该顺序并不重要，也可以使用Bag对象）
          
          这段代码使用了自动装箱和拆箱来转换用例中的int原始数据类型和队列的Integer封装类型
          ![image.png](../assets/image_1650354439862_0.png)
    - (下压) 栈
      collapsed:: true
      - 基于后进先出（LIFO）策略的集合类型
        ![image.png](../assets/image_1650354494416_0.png)
    - 算术表达式求值
      collapsed:: true
      - **算术表达式可能是一个数，或者是由一个左括号、一个算术表达式、一个运算符、另一个算术表达式和一个右括号组成的表达式**
        id:: 625e6874-041c-4562-846f-24f871eb1f2d
      - E.W.Dijkstra在20世纪60年代发明了一个非常简单的算法，用两个栈（一个用于保存运算符，一个用于保存操作数）完成了这个任务
        - ![image.png](../assets/image_1650355076365_0.png)
          id:: 625e6b7b-b6db-4513-982b-9a88667c4035
          collapsed:: true
          - 将操作数压入操作数栈
          - 将运算符压入运算符栈
          - 忽略左括号
          - 在遇到右括号时，弹出一个运算符，弹出所需数量的操作数，并将运算符和操作数的运算结果压入操作数栈
        - 证明
          collapsed:: true
          - 每当算法遇到一个被括号包围并由一个运算符和两个操作数组成的子表达式时，它都将运算符和操作数的计算结果压入操作数栈
          - 这样的结果就好像在输入中用这个值代替了该子表达式，因此用这个值代替子表达式得到的结果和原表达式相同
          - 我们可以反复应用这个规律并得到一个最终值
          -
        - ```java
          public class Evaluate{
              public static void main(String[] args){
                Stack＜String＞ ops  = new Stack＜String＞();
                Stack＜Double＞ vals = new Stack＜Double＞();
                while (! StdIn.isEmpty()){  // 读取字符，如果是运算符则压入栈
                    String s = StdIn.readString();
                    if       (s.equals("("))                 ;
                    else if (s.equals("+"))    ops.push(s);
                    else if (s.equals("-"))    ops.push(s);
                    else if (s.equals("＊"))    ops.push(s);
                    else if (s.equals("/"))    ops.push(s);
                    else if (s.equals("sqrt")) ops.push(s);
                    else if (s.equals(")")){  // 如果字符为")"，弹出运算符和操作数，计算结果并压入栈
                      String op = ops.pop();
                      double v = vals.pop();
                      if       (op.equals("+"))    v = vals.pop() + v;
                      else if (op.equals("-"))    v = vals.pop() - v;
                      else if (op.equals("＊"))    v = vals.pop() ＊ v;
                      else if (op.equals("/"))    v = vals.pop() / v;
                      else if (op.equals("sqrt")) v = Math.sqrt(v);
                      vals.push(v);
                    }  // 如果字符既非运算符也不是括号，将它作为double值压入栈
                    else vals.push(Double.parseDouble(s));
                }
                StdOut.println(vals.pop());
              }
          }
          ```
        - 一种重要的**计算模型**：**将一个字符串解释为一段程序并执行该程序得到结果**
        -
  - 集合类数据类型的实现
    collapsed:: true
    - 定容栈
    - ![image.png](../assets/image_1650357604854_0.png)
      id:: 625e74d7-3d50-43aa-89a6-05de545d98d8
      collapsed:: true
      - 恒等式的方式思考这些条件是检验实现正常工作的最简单的方式
        id:: 625e75e4-6b17-4a74-8d0d-626ca336adcb
      -
    - collapsed:: true
      ```java
      public class FixedCapacityStack＜Item＞
      ```
      - Item是一个类型参数，用于表示用例将会使用的某种具体类型的象征性的占位符
      - 实际的类型必须是引用类型，但用例可以依靠自动装箱将原始数据类型转换为相应的封装类型
      - 由于某些历史和技术原因，创建泛型数组在Java中是不允许的
        id:: 625f7650-d68d-4e2e-aa91-831f1bd27cd2
        - 使用 类型转换 曲线救国：
          ```java
          a = (Item[]) new Object[cap];
          ```
      - 为什么不用普通数组来代替泛型数组?
        collapsed:: true
        - Java 的容器多式多样, 不是一个简单的 `test a[] = new test[20];` 就能代替的, 如:
        - ```java
          List<Integer>[] genericArray = (List<Integer>[])new ArrayList[10];
          genericArray[0] = new ArrayList<String>(Arrays.asList(new String[]{"Hello"}));
          //via: https://www.zhihu.com/question/300950759
          Map<String, String>[] wp = new HashMap<String, String>[5];
          //via: https://www.zhihu.com/question/20928981
          ```
      -
      -
    - 调整数组大小
      collapsed:: true
      - ```
        private void resize(int max)
        {  // 将大小为N ＜ = max的栈移动到一个新的大小为max的数组中
            Item[] temp = (Item[]) new Object[max];
            for (int i = 0; i ＜ N; i++)
              temp[i] = a[i];
            a = temp;
        }
        ```
      - collapsed:: true
        ```java
        Item[] temp = (Item[]) new Object[max];
        Item[] temp = new Item[max];
        ```
        - 总之没什么区别, 第一个的实际过程创建一个中间变量然后把引用还给`temp`.
          
          第一句反而来的更加直接, 没什么区别.
          
          via: https://stackoverflow.com/questions/23362900/what-happens-when-we-do-type-casting-on-objects
      -
    - 对象游离
      collapsed:: true
      - Java的垃圾收集策略是回收所有无法被访问的对象的内存
        - 存在引用但是永远不会被访问到的元素会变成孤儿 -> 游离 (保存一个不需要的对象的引用)
        - 解决方案 -> 将用不到的引用设为 `null`
    - 迭代
      collapsed:: true
      - 优点
        collapsed:: true
        - 代码清晰简洁
        - 不依赖于集合数据类型的具体实现
      - 任意可迭代的集合数据类型中我们都需要实现的东西
        collapsed:: true
        - 集合数据类型必须实现一个 `iterator()` 方法并返回一个Iterator对象
        - Iterator类必须包含两个方法：
          - `hasNext()` (返回一个布尔值)
          - `next()`(返回集合中的一个泛型元素)
      - 要使一个类可迭代
        collapsed:: true
        - 声明中加入 `implements Iterable＜Item＞`
          - 对应的接口（即 `java.lang.Iterable`）为
            ```java
            public interface Iterable<Item>{
                Iterator＜Item＞ iterator();
            }
            ```
        - 类中添加一个方法`iterator()`并返回一个迭代器`Iterator<Item>`
          - ```java
            public Iterator＜Item＞ iterator()
            {  return new ReverseArrayIterator();  }
            ```
        - 迭代器
          - 一个实现了hasNext()和next()方法的类的对象
          - ```java
            // java.util.Iterator
            public interface Iterator<Item>{
                boolean hasNext();
                Item next();
                void remove();
            }
            ```
      - 嵌套类可以访问包含它的类的实例变量 (从里到外访问)
      - 因为(某些历史原因) `Iterator` 不在 `java.lang` 中 (尽管 `Iterable` 是 `java.lang` 的一部分)
    - 集合类数据类型的实现的最佳性能
      collapsed:: true
      - 每项操作的用时都**与集合大小无关**
      - **空间需求**总是**不超过**集合大小乘以**一个常数**
      -
    - ```java
      import java.util.Iterator;
      public class ResizingArrayStack＜Item＞ implements Iterable＜Item＞
      {
          private Item[] a = (Item[]) new Object[1];  // 栈元素
          private int N = 0;                             // 元素数量
          public boolean isEmpty()  {  return N == 0; }
          public int size()          {  return N;       }
          private void resize(int max)
          {  // 将栈移动到一个大小为max的新数组
            Item[] temp = (Item[]) new Object[max];
            for (int i = 0; i ＜ N; i++)
                temp[i] = a[i];
            a = temp;
          }
          public void push(Item item)
          {  // 将元素添加到栈顶
            if (N == a.length) resize(2＊a.length);
            a[N++] = item;
          }
          public Item pop()
          {  // 从栈顶删除元素
            Item item = a[--N];
            a[N] = null;  // 避免对象游离（请见1.3.2.4节）
            if (N ＞ 0 && N == a.length/4) resize(a.length/2);
            return item;
        }
        public Iterator＜Item＞ iterator()
          {  return new ReverseArrayIterator();  }
        private class ReverseArrayIterator implements Iterator＜Item＞
        {  // 支持后进先出的迭代
            private int i = N;
            public boolean hasNext() {  return i ＞ 0;   }
            public    Item next()    {  return a[--i];  }
            public    void remove()  {                    }
        }
      }
      ```
  - 链表
    collapsed:: true
    - 构造非 Java 直接支持的数据结构
    - 递归的数据结构
      collapsed:: true
      - 它或者为空 (null), 或者是指向一个结点 (node) 的引用
      - 该结点含有一个泛型的元素和一个指向另一条链表的引用
    - 结点记录
      collapsed:: true
      - 记录
        - 它们实现的不是抽象数据类型
          - 我们会直接使用其实例变量
        - 在我们的实现中
          - Node和它的用例代码都会被封装在相同的类中且无法被该类的用例访问
          - 我们仍然能够享受数据抽象的好处
      -
    - 构造链表
    - 在表头插入结点
      collapsed:: true
      - ![image.png](../assets/image_1650444085198_0.png)
    - 从表头删除结点
      collapsed:: true
      - ![image.png](../assets/image_1650444077059_0.png)
    - 在表尾插入结点
      collapsed:: true
      - ![image.png](../assets/image_1650444064907_0.png)
    - 其他位置的插入和删除操作
      collapsed:: true
      - 实现任意插入和删除操作的标准解决方案是使用双向链表
    - 遍历
      collapsed:: true
      - ```java
        for (Node x = first; x ! = null; x = x.next)
        {
            // 处理x.item
        }
        ```
    - 栈的实现
      collapsed:: true
      - ![image.png](../assets/image_1650445673205_0.png)
      - ![image.png](../assets/image_1650445698749_0.png)
      - ```java
        public class Stack＜Item＞ implements Iterable＜Item＞
        {
            private Node first; // 栈顶（最近添加的元素）
            private int N;       // 元素数量
            private class Node
            {  // 定义了结点的嵌套类
              Item item;
              Node next;
            }
            public boolean isEmpty() {  return first == null; }  // 或：N == 0
            public int size()         {  return N; }
            public void push(Item item)
            {  // 向栈顶添加元素
              Node oldfirst = first;
              first = new Node();
              first.item = item;
              first.next = oldfirst;
              N++;
            }
            public Item pop()
            {  //从栈顶删除元素
              Item item = first.item;
              first = first.next;
              N--;
              return item;
            }
            // iterator()的实现请见算法1.4
            // 测试用例main()的实现请见本节前面部分
        }
        ```
    - 队列的实现
      collapsed:: true
      - ```java
        public class Queue＜Item＞ implements Iterable＜Item＞
        {
            private Node first; // 指向最早添加的结点的链接
            private Node last;  // 指向最近添加的结点的链接
            private int N;       // 队列中的元素数量
            private class Node
            {  // 定义了结点的嵌套类
              Item item;
              Node next;
          }
          public boolean isEmpty() {  return first == null;  }  // 或： N == 0.
          public int size()         {  return N;  }
          public void enqueue(Item item)
          {  // 向表尾添加元素
              Node oldlast = last;
              last = new Node();
              last.item = item;
              last.next = null;
              if (isEmpty()) first = last;
              else            oldlast.next = last;
              N++;
          }
          public Item dequeue()
          {  // 从表头删除元素
              Item item = first.item;
              first = first.next;
              if (isEmpty()) last = null;
              N--;
              return item;
          }
          // iterator()的实现请见算法1.4
          // 测试用例main()的实现请见前面
        }
        ```
      - 要支持迭代，请添加算法1.4中为Bag数据类型给出的加粗部分的代码
      - ![image.png](../assets/image_1650450230494_0.png)
      - 在结构化存储数据集时，链表是数组的一种重要的替代方式
      - McCathy 在 20世纪50年代 发明的 [[lisp]] 语言
        collapsed:: true
        - 链表则是这种语言组织程序和数据的主要结构
        - 在现代编程语言中，安全指针、自动垃圾回收（请见1.2节答疑部分）和抽象数据类型的使用使我们能够将链表处理的代码封装在若干个类中
          id:: 625fe269-8940-4f84-8c3a-fb1ec072e643
      -
      -
    - 背包的实现
      collapsed:: true
      - ```java
        import java.util.Iterator;
        public class Bag＜Item＞ implements Iterable<Item>
        {
            private Node first;  //链表的首结点
            private class Node
            {
                Item item;
                Node next;
            }
            public void add(Item item)
            {  // 和Stack的push()方法完全相同
              Node oldfirst = first;
              first = new Node();
              first.item = item;
              first.next = oldfirst;
            }
            public Iterator<Item> iterator()
            {  return new ListIterator();  }
            private class ListIterator implements Iterator<Item>
            {
                private Node current = first;
                public boolean hasNext()
                {  return current ! = null;  }
                public void remove() { }
                public Item next()
                {
                    Item item = current.item;
                    current = current.next;
                    return item;
                }
            }
        }
        ```
    - [[java/quick-refs]]
      - 并不是所有编程语言都支持泛型，甚至Java的早期版本也不支持。有其他替代方案吗？
        collapsed:: true
        - 一种替代方法是为每种类型的数据都实现一个不同的集合数据类型。另一种方法是构造一个Object对象的栈，并在用例中使用pop()时将得到的对象转换为所需的数据类型。这种方式的问题在于类型不匹配错误只能在运行时发现
        - 能够在编译时发现错误足以说服我们使用泛型。
      - 为什么Java不允许泛型数组？
        collapsed:: true
        - 共变数组（covariantarray）和类型擦除（type erasure）
      - 创建一个字符串栈的数组？
        collapsed:: true
        - 类型转换
        - 在使用泛型时，Java会在编译时检查类型的安全性，但会在运行时抛弃所有这些信息。因此在运行时语句右侧就变成了Stack＜Object＞[]或者只剩下了Stack[]，因此我们必须将它们转化为Stack＜String＞[]
        - 非静态的嵌套类也被称为内部类，因此从技术上来说我们的Node类也是内部类，尽管非泛型的类也可以是静态的
      - 当我输入javac Stack.java编译算法1.2和其他程序时，我发现了Stack.class和Stack$Node.class两个文件。第二个文件是做什么用的？
        - 第二个文件是为内部类Node创建的。Java的命名规则会使用$分隔外部类和内部类
      - Java标准库中有栈和队列吗？
        - 有，也没有。Java有一个内置的库，叫做java.util.Stack，但你需要栈的时候请不要使用它。它新增了几个一般不属于栈的方法，例如获取第i个元素。它还允许从栈底添加元素（而非栈顶），所以它可以被当做队列使用！尽管拥有这些额外的操作看起来可能很有用，但它们其实是累赘。我们使用某种数据类型不仅仅是为了获得我们能够想象的各种操作，也是为了准确地指定我们所需要的操作。这么做的主要好处在于系统能够防止我们执行一些意外的操作
        - java.util.Stack的API是宽接口的一个典型例子，我们通常会极力避免出现这种情况
      - 我们能够用foreach循环访问数组吗？
        - 可以（尽管数组没有实现Iterable接口）
      - 再次强调一遍，这又是一个宽接口的例
- ### 1.4 算法分析
  collapsed:: true
  - 算法分析
    - 科学方法
      id:: 62621bf8-7075-46ad-80f4-caf849a72af9
      - 细致地观察真实世界的特点，通常还要有精确的测量
        id:: 62621bf8-e550-4f8a-8963-5d8695b96478
      - 根据观察结果提出假设模型
        id:: 62621bf8-3b2c-4447-873f-80628f8ce9fb
      - 根据模型预测未来的事件
        id:: 62621bf8-db10-4230-a332-7cb4d51d8225
      - 继续观察并核实预测的准确性
        id:: 62621bf8-430c-4867-a813-ab0690fa9614
      - 如此反复直到确认预测和观察一致
        id:: 62621bf8-9bea-422c-ae24-84d1075867af
      - 关键原则 -> 实验可重现
        id:: 62621bf8-5232-416c-80bd-53f53e9dd25b
        - id:: 62621bf8-49a0-4216-af2b-f816a5f0878c
          > “再多的实验也不一定能够证明我是对的，但只需要一个实验就能证明我是错的。” 
          ---- 爱因斯坦
      -
    - 观察
    -
- ### 1.5 案例研究：union-find算法
-