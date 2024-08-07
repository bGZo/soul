icon:: ☕
created:: [[20240612]]
type:: java-version
released-date:: 20240319

- ## Why
  -
- ## How
  -
- ## What
  - ## Download
    - IDE: https://www.jetbrains.com/idea/download/download-thanks.html?platform=windowsZip&code=IIC
    - JDK: https://download.java.net/java/GA/jdk22.0.2/c9ecb94cd31b495da20a27d4581645e8/9/GPL/openjdk-22.0.2_windows-x64_bin.zip
  - ## Features JEP
    - 423: Region Pinning for G1 via: https://openjdk.org/jeps/423
      logseq.order-list-type:: number
      background-color:: green
      id:: cbb1ecbf-cfa9-4277-b057-6b1aef5cd5e6
      - 通过在G1中实现区域钉扎来减少延迟，这样在Java Native Interface（JNI）关键区域期间就不需要禁用垃圾收集。
    - 447: Statements before super(...) (Preview)
      logseq.order-list-type:: number
      collapsed:: true
      - 允许没有应用实例的语句出现在显式构造函数调用之前（explicit constructor invocation）
      - ```java
        import java.math.BigInteger;
        
        public class PositiveBigInteger extends BigInteger {
          public PositiveBigInteger(long value) {
            super(String.valueOf(value)); // Potentially unnecessary work
            if (value <= 0)
              throw new IllegalArgumentException("non-positive value");
          }
        }
        ```
        via: https://openjdk.org/jeps/447
    - 454: Foreign Function & Memory API via: https://openjdk.org/jeps/454
      logseq.order-list-type:: number
      collapsed:: true
      - 引入API，Java程序可以通过该API与Java运行时之外的代码和数据进行互操作。通过有效地调用外部函数（即JVM外部的代码），并通过安全地访问外部内存（即不受JVM管理的内存），API使Java程序能够调用本机库并处理本机数据，而不会出现JNI的脆弱性和危险性。
      - ```java
        package com.byd.jep454;
        
        import java.lang.foreign.*;
        import java.lang.invoke.MethodHandle;
        
        public class ForeignFunction {
        
          public static void main(String[] args) {
            // 1. 获取常用库的查找对象
            SymbolLookup stdlib = Linker.nativeLinker().defaultLookup();
        
            // 2. 获取 C 标准库中“strlen”函数的句柄
            MethodHandle strlen =
              Linker.nativeLinker()
              .downcallHandle(
              stdlib.find("strlen").orElseThrow(),
              FunctionDescriptor.of(ValueLayout.JAVA_LONG, ValueLayout.ADDRESS));
        
            // 3. 获取一个受限内存区域（我们可以显式关闭的内存区域）
            try (Arena offHeap = Arena.ofConfined()) {
        
              // 4. 将Java字符串转换为C字符串并将其存储在堆外内存中
              MemorySegment str = offHeap.allocateFrom("coding if fun!");
        
              // 5. 调用外部函数
              long len = 0;
              try {
                len = (long) strlen.invoke(str);
              } catch (Throwable e) {
                e.printStackTrace();
              }
              System.out.println("len = " + len);
            }
            // 6. 堆外内存在 try-with-resources 结束时被释放
          }
        }
        ```
        via: https://blog.csdn.net/nanxiaotao/article/details/136863342
    - 456: Unnamed Variables & Patterns
      logseq.order-list-type:: number
      collapsed:: true
      - 使用未命名变量和未命名模式增强Java编程语言，当需要变量声明或嵌套模式但从未使用时，可以使用这些变量和模式。两者都用下划线字符_表示。
      - 表明声明的该变量创建者无意使用，并告知后开者也不该使用，之前我们可能写 `ignored variable`. 现在统一写 `_`
      - `_` 在 Java 8 中是警告，在 Java 9 中是错误；
        via: https://stackoverflow.com/questions/23523946
        - `use of '_' as an identifier is not supported in releases since java 9`
      - 适用场景
        - 块内局部变量；
        - 异常处理；
          - `try()` 块内（resource specification）
          - `catch()` 块内
        - `for` 循环；
          - 增强 for 循环；
        - `lambda` 表达式
      - ```java
        
        import java.util.ArrayList;
        import java.util.List;
        import java.util.Map;
        import java.util.stream.Collectors;
        
        public class UnnamedVariable {
        
            public static void main(String[] args) {
                List<Order> _ = new ArrayList<>();
        
                List<Order> orderList = new ArrayList<>();
                orderList.add(new Order());
                orderList.add(new Order());
                orderList.add(new Order());
                for (Order i : orderList) {
                    System.out.println("placeholder");
                }
        
                String s = "...";
                try {
                    Integer i = Integer.parseInt(s);
                } catch (NumberFormatException i) {
                    System.out.println("Bad number: " + s);
                }
        
                List<String> strs = new ArrayList<>();
                strs.add("a");
                strs.add("b");
                Map<Object, Object> result = strs.stream().collect(Collectors.toMap(String::toUpperCase, i -> "NODATE"));
                System.out.println(result);
            }
        }
        
        class Order {
            String orderNo;
        }
        
        ```
    - 457: Class-File API (Preview) via: https://openjdk.org/jeps/457
      logseq.order-list-type:: number
      background-color:: pink
      - 提供一个标准的API，用于解析、生成和转换Java类文件。这是一个预览API。
      - ASM???
      - https://jameshamilton.eu/programming/build-compiler-jep-457-class-file-api
      - https://github.com/mrjameshamilton/jep457-hello-world/blob/master/Main.java
        - ??? 为什么运行不了???
    - 458: Launch Multi-File Source-Code Programs
      logseq.order-list-type:: number
      collapsed:: true
      - #+BEGIN_EXAMPLE
        增强java应用程序启动器，使其能够运行作为java源代码的多个文件提供的程序。这将使从小程序到大程序的过渡更加渐进，使开发人员能够选择是否以及何时配置构建工具。
        #+END_EXAMPLE
      - JDK 11 针对 Java 应用启动器做过优化，可以直接跑 `.java` 的 `source` 文件:
        - ```java
          class Prog {
            public static void main(String[] args) { Helper.run(); }
          }
          
          class Helper {
            static void run() { System.out.println("Hello!"); }
          }
          /**
           *java Prog.java
           **/
          ```
        - 局限是这些类必须放在一个文件中
      - JDK 22 打破了这个限制
    - 459: String Templates (Second Preview)
      logseq.order-list-type:: number
      collapsed:: true
      - #+BEGIN_EXAMPLE
        使用字符串模板增强Java编程语言。字符串模板通过将文本与嵌入的表达式和模板处理器耦合来产生专门的结果，从而补充Java现有的字符串文本和文本块。这是一个预览语言功能和API。
        #+END_EXAMPLE
      - 之前的方案
        collapsed:: true
        - `+`
        - `StringBuilder`
        - `String::format`
        - `MessageFormat`
        - ```java
          String s = x + " plus " + y + " equals " + (x + y);
          // 难以阅读
          String s = new StringBuilder()
                           .append(x)
                           .append(" plus ")
                           .append(y)
                           .append(" equals ")
                           .append(x + y)
                           .toString();
          //冗长
          String s = String.format("%2$d plus %1$d equals %3$d", x, y, x + y);
          String t = "%2$d plus %1$d equals %3$d".formatted(x, y, x + y);
          //可能不匹配
          MessageFormat mf = new MessageFormat("{0} plus {1} equals {2}");
          String s = mf.format(x, y, x + y);
          // 复杂
          ```
      - demo
        - ```java
          
          import static java.lang.StringTemplate.STR;
          
          public class templateStr {
              public static void main(String[] args) {
                  // Embedded expressions can be strings
                  String firstName = "Bill";
                  String lastName  = "Duck";
                  String fullName  = STR."\{firstName} \{lastName}";
                  System.out.println(fullName);
          //| "Bill Duck"
                  String sortName  = STR."\{lastName}, \{firstName}";
                  System.out.println(sortName);
          //| "Duck, Bill"
          
          // Embedded expressions can perform arithmetic
                  int x = 10, y = 20;
                  String s = STR."\{x} + \{y} = \{x + y}";
                  System.out.println(s);
          //| "10 + 20 = 30"
          
          // Embedded expressions can invoke methods and access fields
                  s = STR."You have a \{getOfferType()} waiting for you!";
                  System.out.println(s);
          //| "You have a gift waiting for you!"
          
          //        String t = STR."Access at \{req.date} \{req.time} from \{req.ipAddress}";
          //        System.out.println(t);
          //| "Access at 2022-03-25 15:34 from 8.8.8.8"
          
                  String name = "Smith' OR p.last_name <> 'Smith";
                  String query = STR."SELECT * FROM Person p WHERE p.last_name = '\{name}'";
                  System.out.println(query);
              }
          
              static String getOfferType(){
                  return "gift";
              }
          
          }
          ```
    - 460: Vector API (Seventh Incubator) via: https://openjdk.org/jeps/460
      logseq.order-list-type:: number
      collapsed:: true
      - #+BEGIN_EXAMPLE
        引入API来表示向量计算，这些向量计算在运行时可靠地编译为支持的CPU架构上的最佳向量指令，从而实现优于等效标量计算的性能。
        #+END_EXAMPLE
      - ```java
        import jdk.incubator.vector.IntVector;
        import jdk.incubator.vector.VectorSpecies;
        
        public class vectorDemo {
        
          private static final VectorSpecies<Integer> SPECIES = IntVector.SPECIES_PREFERRED;
        
        public static void vectorAddition(int[] a, int[] b, int[] result) {
          int i = 0;
          int upperBound = SPECIES.loopBound(a.length);
          for (i = 0; i < upperBound; i += SPECIES.length()) {
            // 从数据中加载向量
            IntVector va = IntVector.fromArray(SPECIES, a, i);
            IntVector vb = IntVector.fromArray(SPECIES, b, i);
            // 执行逐元素加法
            IntVector vr = va.add(vb);
            // 将结果存储在结果数组中
            vr.intoArray(result, i);
          }x
          // 处理剩余元素
          for (; i < a.length; i++) {
            result[i] = a[i] + b[i];
          }
        }
        
        
        
        public static void main(String[] args) {
          int[] a = {1, 2, 3, 4, 5};
          int[] b = {6, 7, 8, 9, 10};
          int[] result = new int[a.length];
        
          vectorAddition(a, b, result);
        
          // 输出结果
          for (int r : result) {
            System.out.println(r);
          }
        
        }
        }
        ```
        via: https://blog.csdn.net/nanxiaotao/article/details/136863342
      - ```shell
        D:\apps\jdk-22.0.2\bin\java.exe --add-modules=jdk.incubator.vector .\vectorDemo.java
        ```
      - Java 机器学习
        - https://time.geekbang.org/column/article/464927
    - 461: Stream Gatherers (Preview)
      logseq.order-list-type:: number
      collapsed:: true
      - #+BEGIN_EXAMPLE
        增强Stream API以支持自定义中间操作。这将允许流管道以现有内置中间操作无法轻松实现的方式转换数据。这是一个预览API。
        #+END_EXAMPLE
      - #+BEGIN_EXAMPLE
        [0, 1, 2, 3, 4, 5, 6, ...] 
        分为窗口大小为 3 的组，并只保留前两组
        #+END_EXAMPLE
        - ```java
          import java.util.ArrayList;
          import java.util.Arrays;
          import java.util.List;
          import java.util.stream.Collector;
          import java.util.stream.Collectors;
          import java.util.stream.Gatherers;
          
          public class GatherDemo {
          
            public static ArrayList<ArrayList<Integer>> findGroupsOfThree(List<Integer> source, long fixed_size, int grouping) {
              //                Stream.iterate(0, i -> i + 1)
              return source.stream()
                .limit(fixed_size * grouping)
                .collect(Collector.of(
                  ArrayList::new,
                  (groups, element) -> {
                    if(groups.isEmpty() || groups.getLast().size() == fixed_size) {
                      var current = new ArrayList<Integer>();
                      current.add(element);
                      groups.addLast(current);
                    } else {
                      groups.getLast().add(element);
                    }
                  },(_, _) -> {
                    throw new UnsupportedOperationException("Cannot be parallelized");
                  }
                ));
            }
          
            public static List<List<Integer>> findGroupsOfThreeWithGatherer(List<Integer> source, long fixed_size, int grouping) {
              return source.stream()
                .gather(Gatherers.windowFixed((int)fixed_size))
                .limit(grouping)
                .collect(Collectors.toList());
            }
          
          
            public static void main() {
              List<Integer> target = new ArrayList<>(Arrays.asList(1,2,3,4,5,6,7,8,9,0));
              System.out.println(findGroupsOfThree(target, 4, 2));
              System.out.println(findGroupsOfThreeWithGatherer(target, 4, 2));
            }
          
          }
          ```
      - TODO `Gather` 带来的新的 API
        - ...
    - 462: Structured Concurrency (Second Preview)
      logseq.order-list-type:: number
      background-color:: green
      - 通过引入用于结构化并发的API来简化并发编程。结构化并发将在不同线程中运行的相关任务组视为单个工作单元，从而简化错误处理和消除，提高可靠性，并增强可观察性。这是一个预览API。
    - 463: Implicitly Declared Classes and Instance Main Methods (Second Preview)
      logseq.order-list-type:: number
      collapsed:: true
      - 发展Java编程语言，使学生无需理解为大型程序设计的语言功能即可编写第一个程序。学生们可以为单类程序编写精简的声明，而不是使用单独的语言方言，然后随着技能的发展，无缝地扩展程序，使用更高级的功能。这是一个预览语言功能。
      - ```java
        public class HelloWorld {
            public static void main(String[] args) {
                System.out.println("Hello, World!");
            }
        }
        ```
      - ```java
        void main() {
            System.out.println("Hello, World!");
        }
        ```
    - 464: Scoped Values (Second Preview)
      logseq.order-list-type:: number
      collapsed:: true
      - #+BEGIN_EXAMPLE
        引入作用域值，使不可变数据能够与同一线程中的子帧和子线程进行托管共享。作用域值比线程本地变量更容易推理，并且空间和时间成本更低，尤其是与虚拟线程和结构化并发结合使用时。这是一个预览API。
        #+END_EXAMPLE
      - Java 20 中的孵化功能（ [JEP 429）](https://openjdk.org/jeps/429)引入，作为 Java 21 中的预览功能[（JEP 446）](https://openjdk.org/jeps/446)引入，目前处于 Java 22 中的第二轮预览（ [JEP 464）](https://openjdk.org/jeps/464)。
      - ```java
        public static <T> void runWhere(ScopedValue<T> key, T value, Runnable op) {
          where(key, value).run(op);
        }
        ```
        - Key -> 作用域值的位置
        - Value -> 作用域值的位置
        - Op -> 在此范围内运行的可运行程序
        - #+BEGIN_NOTE
          Value 只能由运行 Op 操作的线程访问，当 Op 完成之后，值将无法访问
          #+END_NOTE
      - ```java
        public class scopedValuesDemo {
            public static void main(String[] args) throws InterruptedException {
                Thread.startVirtualThread(() ->
                        ScopedValue.runWhere(
                                CurrentUser.USERNAME, "David", TaskDefinition::runTaskDefinition
                        ));
                Thread.sleep(100);
            }
        }
        
        class CurrentUser{
            final static ScopedValue<String> USERNAME = ScopedValue.newInstance();
        }
        
        class TaskDefinition {
            static void runTaskDefinition(){
                Step step = new Step();
                step.performStep();
            }
        }
        
        class Step{
        
            public void performStep() {
                System.out.println("name = " + CurrentUser.USERNAME.get());
                /**
                 * 不需要在整个应用程序代码中将用户名作为参数传递，而是可以在需要的地方直接访问它。这对于在范围/上下文中运行的事物非常有用
                 */
            }
        }
        ```
        via: https://davidvlijmincx.com/posts/java-scoped-values-tutorial/
  - ## References
    - https://waylau.com/jdk-22-released/
    - https://openjdk.org/projects/jdk/22/
- ## Namespace
  - {{namespace java22}}
- ## ↩ Reference
  -