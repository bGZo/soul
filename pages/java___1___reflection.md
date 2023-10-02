title:: java/1/reflection
alias:: java 反射
define:: Reflection enables Java code to discover information about the fields, methods and constructors of loaded classes, and to use reflected fields, methods, and constructors to operate on their *underlying counterparts(底层对应物)*, *within security restrictions*(安全限制内). The API *accommodates(满足)* applications that need access to either the public members of a target object (based on its runtime class) or the members declared by a given class(该API访问目标对象的公共成员（基于其运行时的类）或特定类所声明的成员的应用程序). It also allows programs to suppress default reflective access control(它还允许程序抑制默认的反射性访问控制).
mark:: [Core Java Reflection](https://docs.oracle.com/javase/8/docs/technotes/guides/reflection/index.html)；from java 1.1

  - Enhanced in #java/1 #java/5 #java/6 #java/8
  -
-
- [反射 - 廖雪峰](https://www.liaoxuefeng.com/wiki/1252599548343744/1255945147512512)
  - ```java
    method.invoke(object, new Object[][]{new Object[]{obj1, obj2}});
    object.method(obj1, obj2);
    ```
  - Java的反射是指程序在运行期可以拿到一个对象的所有信息
  - 反射是为了解决在运行期，对某个实例一无所知的情况下，如何调用其方法
  - Java的其他类型全部都是`class`（包括`interface`）
  - `class`（包括`interface`）的本质是数据类型（`Type`）。无继承关系的数据类型无法赋值。而`class`是由JVM在执行过程中动态加载的。JVM在第一次读取到一种`class`类型时，将其加载进内存。
    collapsed:: true
    - 每加载一种`class`，JVM就为其创建一个`Class`类型的实例，并关联起来。注意：这里的`Class`类型是一个名叫`Class`的`class`。它长这样：
      
      ```java
      public final class Class {
          private Class() {}
      }
      ```
    - 以`String`类为例，当JVM加载`String`类时，它首先读取`String.class`文件到内存，然后，为`String`类创建一个`Class`实例并关联起来：
      
      ```java
      Class cls = new Class(String);
      ```
    - 只有JVM能创建`Class`实例，我们自己的Java程序是无法创建`Class`实例的，JVM持有的每个`Class`实例都指向一个数据类型（`class`或`interface`）
      
      ```
      ┌───────────────────────────┐
      │      Class Instance       │──────> String
      ├───────────────────────────┤
      │name = "java.lang.String"  │
      ├───────────────────────────┤
      │package = "java.lang"      │
      ├───────────────────────────┤
      │super = "java.lang.Object" │
      ├───────────────────────────┤
      │interface = CharSequence...│
      ├───────────────────────────┤
      │field = value[],hash,...   │
      ├───────────────────────────┤
      │method = indexOf()...      │
      └───────────────────────────┘
      ┌───────────────────────────┐
      │      Class Instance       │──────> Random
      ├───────────────────────────┤
      │name = "java.util.Random"  │
      ├───────────────────────────┤
      │......                      │
      └───────────────────────────┘
      ┌───────────────────────────┐
      │      Class Instance       │──────> Runnable
      ├───────────────────────────┤
      │name = "java.lang.Runnable"│
      ├───────────────────────────┤
      │......                      │
      └───────────────────────────┘
      ```
      - 如果获取了某个`Class`实例，我们就可以通过这个`Class`实例获取到该实例对应的`class`的所有信息。
      - 这种通过`Class`实例获取`class`信息的方法称为反射（Reflection）
  - ```java
      //1
    Class cls = String.class;
    //2
    String s = "Hello";
    Class cls = s.getClass();
    //3
    Class cls = Class.forName("java.lang.String");
    ```
-
- `Class` #vs `instanceof`
  collapsed:: true
  - ```java
    Integer n = new Integer(123);
    
    boolean b1 = n instanceof Integer; // true，因为n是Integer类型
    boolean b2 = n instanceof Number; // true，因为n是Number类型的子类
    // 用`instanceof`不但匹配指定类型，还匹配指定类型的子类
    
    boolean b3 = n.getClass() == Integer.class; // true，因为n.getClass()返回Integer.class
    boolean b4 = n.getClass() == Number.class; // false，因为Integer.class!=Number.class
    用`==`判断`class`实例可以精确地判断数据类型，但不能作子类型比较
    ```
  - 用`instanceof`判断数据类型
    - 因为面向抽象编程的时候，我们不关心具体的子类型
  - 用`==`判断`class`精确判断一个类型是不是某个`class`实例
  - 可以通过该`Class`实例来创建对应类型的实例
    
    ```java
    // 获取String的Class实例:
    Class cls = String.class;
    // 创建一个String实例:
    String s = (String) cls.newInstance();
    
    // Same as
    String s = new String();
    ```
    - 局限
      - 带参数 / 非`public`的构造方法 都无法通过`Class.newInstance()`被调用
      - Java 的反射 API 提供了 Constructor 对象
        - Constructor 对象 vs Method
          - Constructor 对象 是一个构造方法
          - Constructor 对象 调用结果总返回实例
        - `getConstructor(Class...)`
          - 获取某个`public`的`Constructor`
        - `getDeclaredConstructor(Class...)`
          - 获取某个`Constructor`
        - `getConstructors()`
          - 获取所有`public`的`Constructor`
        - `getDeclaredConstructors()`
          - 获取所有`Constructor`
-
- 动态加载
  collapsed:: true
  - JVM 执行程序并不是一次性把所有用到的 class 全部加载到内存, 即只有运行到对应方法时，才会实体化对应类
  - 特性
    - 在运行期根据条件加载不同的实现类
      - Commons Logging 总是优先使用Log4j
        - 只有当Log4j不存在时，才使用JDK的logging
          
          ```
          // 我们只需要把Log4j的jar包放到classpath中
          // Commons Logging就会自动使用Log4j
          
          LogFactory factory = null;
          if (isClassPresent("org.apache.logging.log4j.Logger")) {
              factory = createLog4j();
          } else {
              factory = createJdkLog();
          }
          
          boolean isClassPresent(String name) {
              try {
                  Class.forName(name);
                  return true;
              } catch (Exception e) {
                  return false;
              }
          }
          ```
-
- 访问字段
  - `Class`类提供了以下几个方法来获取字段：
    - `Field getField(name)`
      - 根据字段名获取某个public的field（包括父类）
    - `Field getDeclaredField(name)`
      - 根据字段名获取当前类的某个field（不包括父类）
    - `Field[] getFields()`
      - 获取所有public的field（包括父类）
    - `Field[] getDeclaredFields()`
      - 获取当前类的所有field（不包括父类）
  - 一个`Field`对象包含了一个字段的所有信息：
    - `getName()`
      - 返回字段名称，例如，`"name"`；
    - `getType()`
      - 返回字段类型，也是一个`Class`实例，例如，`String.class`；
    - `getModifiers()`
      - 返回字段的修饰符，它是一个`int`，不同的bit表示不同的含义。
  - 获取字段值
    - > 如果使用反射可以获取`private`字段的值，那么类的封装还有什么意义？
      - 正常情况下，我们总是通过`p.name`来访问`Person`的`name`字段，编译器会根据`public`、`protected`和`private`决定是否允许访问字段，这样就达到了数据封装的目的。
      - 而反射是一种非常规的用法，**使用反射，首先代码非常繁琐**，其次，**它更多地是给工具或者底层框架来使用，目的是在不知道目标实例任何信息的情况下，获取特定字段的值**
      - 此外，`setAccessible(true)`可能会失败。如果JVM运行期存在`SecurityManager`，那么它会根据规则进行检查，有可能阻止`setAccessible(true)`。例如，某个`SecurityManager`可能不允许对`java`和`javax`开头的`package`的类调用`setAccessible(true)`，这样可以保证JVM核心库的安全。
  - 设置字段值
  - 调用方法
    - `Class`类提供了以下几个方法来获取`Method`：
      - `Method getMethod(name, Class...)`
        - 获取某个`public`的`Method`（包括父类）
      - `Method getDeclaredMethod(name, Class...)`
        - 获取当前类的某个`Method`（不包括父类）
      - `Method[] getMethods()`
        - 获取所有`public`的`Method`（包括父类）
      - `Method[] getDeclaredMethods()`
        - 获取当前类的所有`Method`（不包括父类）
    - 一个`Method`对象包含一个方法的所有信息：
      - `getName()`
        - 返回方法名称，例如：`"getScore"`；
      - `getReturnType()`
        - 返回方法返回值类型，也是一个Class实例，例如：`String.class`；
      - `getParameterTypes()`
        - 返回方法的参数类型，是一个Class数组，例如：`{String.class, int.class}`；
      - `getModifiers()`
        - 返回方法的修饰符，它是一个`int`，不同的bit表示不同的含义。
    - 调用
      - 普通方法
      - 静态方法
      - 非public方法
      - 符合多态特性
-
- 获取继承关系
  - 获取父类的Class
  - 获取interface
  - 继承关系
-
- 动态代理
  - `interface`类型的变量总是通过某个实例向上转型并赋值给接口类型变量
  - Java标准库提供了一种动态代理 (Dynamic Proxy) 的机制
    - 可以在运行期动态创建某个`interface`的实例
    - 通过JDK提供的一个`Proxy.newProxyInstance()`创建了一个`Hello`接口对象
      - 这种没有实现类但是在运行期动态创建了一个接口对象的方式，我们称为动态代码。
      - JDK提供的动态创建接口对象的方式，就叫动态代理
  - 在运行期动态创建一个`interface`实例的方法如下：
    1. 定义一个`InvocationHandler`实例，它负责实现接口的方法调用；
    2. 通过`Proxy.newProxyInstance()`创建`interface`实例，它需要3个参数：
       1. 使用的`ClassLoader`，通常就是接口类的`ClassLoader`；
       2. 需要实现的接口数组，至少需要传入一个接口进去；
       3. 用来处理接口方法调用的`InvocationHandler`实例。
    3. 将返回的`Object`强制转型为接口。
-
-
- Refs
  - [访问字段 - 廖雪峰](https://www.liaoxuefeng.com/wiki/1252599548343744/1264803033837024)
  - [获取继承关系 - 廖雪峰](https://www.liaoxuefeng.com/wiki/1252599548343744/1264804244564000)
  - [动态代理 - 廖雪峰](https://www.liaoxuefeng.com/wiki/1252599548343744/1264804593397984)
  -