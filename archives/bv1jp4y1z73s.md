tags:: #ssm
description:: [【动力节点】SSM框架之MyBatis上线即经典，跟老杜从零学mybatis 入门到架构思维](https://www.bilibili.com/video/BV1JP4y1Z73S/)
created:: [[20230305]]

  - https://www.yuque.com/dujubin/ltckqu/pozck9 & `rs4n`
- ## -nested-2 Contents
  - DONE MyBatis概述
    collapsed:: true
    - 框架
      description:: 对通用代码的封装，提前写好了一堆接口和类，我们可以在做项目的时候直接引入这些接口和类（引入框架），基于这些现有的接口和类进行开发，可以大大提高开发效率
    - 三层架构 #[[Spring MVC]]
      - ![](../assets/BV1JP4y1Z73S/三层架构.png)
      - 三层架构 #vs [[Spring MVC]]
        - **三层架构**
          ![chrome_328.png](../assets/chrome_328_1678015587506_0.png)
        - **SpringMVC**
          ![chrome_329.png](../assets/chrome_329_1678015649608_0.png){:height 232, :width 533}
        - ![chrome_327.png](../assets/chrome_327_1678015505191_0.png)
          (View 就是 JSP 视图)
        - Refer to: https://www.bilibili.com/video/BV1Z3411C7NZ/?p=71
      - Java持久层框架：
        - Hibernate（实现了JPA规范）
        - Spring Data（实现了JPA规范）
        - MyBatis
        - jOOQ
        - Guzz
        - ActiveJDBC
        - ......
    - JDBC不足
      - SQL语句写死在Java程序中，不灵活。改SQL的话就要改Java代码。违背开闭原则OCP；
      - 给`?`传值是繁琐的，一句一句式的赋值非常繁琐；
      - 将结果集封装成Java对象是繁琐的；
    - 了解MyBatis
      - History
        - iBatis (`internet` 和 `abatis`)
        - iBATIS提供的持久层框架包括 SQL Maps 和 Data Access Objects (DAOs)
      - ORM #orm
        - ![chrome_330.png](../assets/chrome_330_1678067720804_0.png)
      - 原理
        - 将接口和 Java 的 POJOs(Plain Ordinary Java Object，简单普通的Java对象)映射成数据库中的记录，避免了几乎所有的 JDBC 代码中手动设置参数以及获取结果集
      - 特点：
        - 轻量级，体积小；
          - 两个jar包
          - 两个XML配置文件
        - **定制化** SQL
          - XML开发居多（灵活优化 SQL），也支持注解式开发；
            - SQL 独立出来使整体架构解耦合；
          - 有 XML 标签，支持 **动态SQL** 的编写
        - 存储过程
        - 基本映射标签
        - 高级映射标签
  - DONE MyBatis入门程序
    collapsed:: true
    - 版本
      - ![Mybatis Reference Verison 3.5.10](../assets/doc_mybatis_3.5.10.pdf)
    - MyBatis下载
    - MyBatis入门程序开发步骤
    - 关于MyBatis核心配置文件的名字和路径详解
      - mybatis 核心配置文件的名字是随意的，存放路径也是随意的
        - `mybatis-config.xml`；
        - 通常该文件会存放到**类路径**当中，这样让项目的移植更加健壮；
      -
    - MyBatis第一个比较完整的代码写法
    - 引入JUnit
    - 引入日志框架logback
    - MyBatis工具类SqlSessionUtil的封装
  - 使用MyBatis完成CRUD
    collapsed:: true
    - insert（Create）
    - delete（Delete）
    - update（Update）
    - select（Retrieve）
      - 查询一条数据
      - 查询多条数据
    - 关于SQL Mapper的namespace
  - DONE MyBatis核心配置文件详解
    collapsed:: true
    - ```xml
      <?xml version="1.0" encoding="UTF-8" ?>
      <!DOCTYPE configuration
              PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
              "http://mybatis.org/dtd/mybatis-3-config.dtd">
      <configuration>
        <environments default="development">
          <environment id="development"> <!-- 包括：事务管理器的配置 + 数据源的配置 -->
            <transactionManager type="JDB	C"/>  <!-- 事务管理器 -->
            <dataSource type="POOLED"> <!-- 数据源 -->
              <property name="driver" value="com.mysql.cj.jdbc.Driver"/>
              <property name="url" value="jdbc:mysql://localhost:3306/powernode"/>
              <property name="username" value="root"/>
              <property name="password" value="root"/>
            </dataSource>
          </environment>
        </environments>
        <mappers>
          <mapper resource="CarMapper.xml"/>
          <mapper resource="CarMapper2.xml"/>
        </mappers>
      </configuration>
      ```
      - transactionManager 事务管理器 ((640556bb-f303-49ad-8b7b-a713cbb4877a))
        - **JDBC** (原生)
          - **底层原理**
            - 事务开启 conn.setAutoCommit(false); ...
            - 处理业务 ...
            - 事务提交 conn.commit();
            - ((64055744-3e93-489b-9e97-fa3bc36cda5e))
        - **MANAGED**
          - WebLogic、JBOSS
            - 如果没有管理事务的容器，则没有事务
          - **没有事务的含义**
            - 只要执行一条DML语句，则提交一次
        - #+BEGIN_NOTE
          ((640557c0-956b-4ead-b339-b232f87b1459))
          #+END_NOTE
          #spring-framework
      - dataSource 数据源 ((6405588e-b1d8-452c-af29-98df978567d7)) type
        - **UNPOOLED**
          - 采用传统的获取连接的方式，虽然也实现Javax.sql.DataSource接口，但是并没有使用池的思想。
          - 需要配置 `driver`. `url`. `username`, `password`, `defaultTransactionIsolationLevel`(事务隔离等级). `defaultNetworkTimeout`(超时时间). [`encoding`]
        - **POOLED**
          - 避免了初始化和创建链接的授权时间，适合于并发应用
            - ((64055a65-59ad-49ea-a1b6-fcd45b587846))
            - 采用传统的javax.sql.DataSource规范中的连接池，mybatis中有针对规范的实现
          - 除了 `UNPOOLED` 的部分，还需要需要配置 `poolMaximumActiveConnections`(10 default) 和 `poolMaximumIdleConnections `(空闲连接数)；
        - **JNDI**
          - 和 EJB 或者 应用服务器一起使用；
            - ((64055b2d-43cb-40de-951e-bdb8646b2aa3))
            - 采用服务器提供的JNDI技术实现，来获取DataSource对象，不同的服务器所能拿到DataSource是不一样。如果不是web或者maven的war工程，JNDI是不能使用的
          -
          - 只需要配置两个参数：`initial_context ` 和 `data_source `
            - 这个属性用来在 InitialContext 中寻找上下文（即，initialContext.lookup(initial_context)）这是个可选属性，如果忽略，那么将会直接从 InitialContext 中寻找 data_source 属性。
            - 这是引用数据源实例位置的上下文路径。提供了 initial_context 配置时会在其返回的上下文中进行查找，没有提供时则直接在 InitialContext 中查找。
          -
    - environment
    - ==transactionManager==
    - dataSource
      - `POOLED`
        - poolMaximumActiveConnections：最大的活动的连接数量。默认值10
        - poolMaximumIdleConnections：最大的空闲连接数量。默认值5
        - poolMaximumCheckoutTime：强行回归池的时间。默认值20秒。
        - poolTimeToWait：当无法获取到空闲连接时，每隔20秒打印一次日志，避免因代码配置有误，导致傻等。（时长是可以配置的）
        - ---
        - poolMaximumLocalBadConnectionTolerance
        - poolPingQuery
        - poolPingEnabled
        - poolPingConnectionsNotUsedFor
    - properties
      - 两个属性
        - `resource`
          - 从类的根路径下开始加载
        - `file`
          - `file:///d:/jdbc.properties` (Linux 下稍有不同)
    - mapper
      - 两种加载方式
        - 类路劲加载
          ```xml
          <mappers>
            <mapper resource="CarMapper.xml"/>
          </mappers>
          ```
        - URL 路劲加载
          ```xml
          <mappers>
            <mapper resource="test/CarMapper.xml"/>
          </mappers>
          ```
  - TODO 手写MyBatis框架（掌握原理）
    collapsed:: true
    - dom4j解析XML文件
    - GodBatis
      - 第一步：IDEA中创建模块
      - 第二步：资源工具类，方便获取指向配置文件的输入流
      - 第三步：定义SqlSessionFactoryBuilder类
      - 第四步：分析SqlSessionFactory类中有哪些属性
      - 第五步：定义GodJDBCTransaction
      - 第六步：事务管理器中需要数据源，定义GodUNPOOLEDDataSource
      - 第七步：定义GodMappedStatement
      - 第八步：完善SqlSessionFactory类
      - 第九步：完善SqlSessionFactoryBuilder中的build方法
      - 第十步：在SqlSessionFactory中添加openSession方法
      - 第十一步：编写SqlSession类中commit rollback close方法
      - 第十二步：编写SqlSession类中的insert方法
      - 第十三步：编写SqlSession类中的selectOne方法
    - GodBatis使用Maven打包
    - 使用GodBatis
    - 总结MyBatis框架的重要实现原理
  - 在WEB中应用MyBatis（使用MVC架构模式）
    - 需求描述
    - 数据库表的设计和准备数据
    - 实现步骤
      - 第一步：环境搭建
      - 第二步：前端页面index.html
      - utils包
      - 第四步：定义pojo类：Account
      - 第五步：编写AccountDao接口，以及AccountDaoImpl实现类
      - 第六步：AccountDaoImpl中编写了mybatis代码，需要编写SQL映射文件了
      - 第七步：编写AccountService接口以及AccountServiceImpl
      - 第八步：编写AccountController
    - **==MyBatis对象作用域以及事务问题==** ((64059dc6-47bb-4c9c-ab1e-129b91007bba))
      - SqlSessionFactoryBuilder
        - ((64059e46-df6e-442c-98fb-17c976a0f826))
      - SqlSessionFactory
        - ((64059e91-9c3b-4f06-b77d-33ebea0055eb))
        - ((64059e83-5bcd-4abd-92c4-71440793e10d))
      - SqlSession
        - ((64059eaa-a595-475a-b48c-a69038cce026))
    - 事务问题（保证它们的同时成功或同时失败）
      - 场景
        - 转账业务中，在 transfer 开始执行时开启事务，直到两个更新都成功之后，再提交事务；
      - 解决方法
        - ThreadLocal 保证一个线程中只有一个 SqlSession
        - ```java
          package com.powernode.bank.utils;
          import org.apache.ibatis.io.Resources;
          import org.apache.ibatis.session.SqlSession;
          import org.apache.ibatis.session.SqlSessionFactory;
          import org.apache.ibatis.session.SqlSessionFactoryBuilder;
          /**
           * MyBatis工具类
           */
          public class SqlSessionUtil {
            private static SqlSessionFactory sqlSessionFactory;
            /**
             * 类加载时初始化sqlSessionFactory对象
             */
            static {
              try {
                SqlSessionFactoryBuilder sqlSessionFactoryBuilder = new SqlSessionFactoryBuilder();
                sqlSessionFactory = sqlSessionFactoryBuilder.build(Resources.getResourceAsStream("mybatis-config.xml"));
              } catch (Exception e) {
                e.printStackTrace();
              }
            }
            private static ThreadLocal<SqlSession> local = new ThreadLocal<>();
            /**
             * 每调用一次openSession()可获取一个新的会话，该会话支持自动提交。
             * @return 新的会话对象
             */
            public static SqlSession openSession() {
              SqlSession sqlSession = local.get();
              if (sqlSession == null) {
                sqlSession = sqlSessionFactory.openSession();
                local.set(sqlSession);
              }
              return sqlSession;
            }
            /**
             * 关闭SqlSession对象
             * @param sqlSession
             */
            public static void close(SqlSession sqlSession){
              if (sqlSession != null) {
                sqlSession.close();
              }
              local.remove();
            }
          }
          ```
  - 使用javassist生成类
    - Javassist的使用
      - SDK 高版本编译异常
        - `--add-opens java.base/java.lang=ALL-UNNAMED`
        - `--add-opens java.base/sun.net.util=ALL-UNNAMED`
    - 使用Javassist生成DaoImpl类 \#动态代理
      - 利用 Java 反射和声明好的接口，生成对应的方法；
      - ```java
        package com.powernode.bank.utils;
        import org.apache.ibatis.javassist.CannotCompileException;
        import org.apache.ibatis.javassist.ClassPool;
        import org.apache.ibatis.javassist.CtClass;
        import org.apache.ibatis.javassist.CtMethod;
        import org.apache.ibatis.session.SqlSession;
        import java.lang.reflect.Constructor;
        import java.lang.reflect.Method;
        import java.lang.reflect.Modifier;
        import java.util.Arrays;
        /**
         * 使用javassist库动态生成dao接口的实现类
         *
         * @author 老杜
         * @version 1.0
         * @since 1.0
         */
        public class GenerateDaoByJavassist {
            /**
             * 根据dao接口生成dao接口的代理对象
             *
             * @param sqlSession   sql会话
             * @param daoInterface dao接口
             * @return dao接口代理对象
             */
            public static Object getMapper(SqlSession sqlSession, Class daoInterface) {
                ClassPool pool = ClassPool.getDefault();
                // 生成代理类
                CtClass ctClass = pool.makeClass(daoInterface.getPackageName() + ".impl." + daoInterface.getSimpleName() + "Impl");
                // 接口
                CtClass ctInterface = pool.makeClass(daoInterface.getName());
                // 代理类实现接口
                ctClass.addInterface(ctInterface);
                // 获取所有的方法
                Method[] methods = daoInterface.getDeclaredMethods();
                Arrays.stream(methods).forEach(method -> {
                    // 拼接方法的签名
                    StringBuilder methodStr = new StringBuilder();
                    String returnTypeName = method.getReturnType().getName();
                    methodStr.append(returnTypeName);
                    methodStr.append(" ");
                    String methodName = method.getName();
                    methodStr.append(methodName);
                    methodStr.append("(");
                    Class<?>[] parameterTypes = method.getParameterTypes();
                    for (int i = 0; i < parameterTypes.length; i++) {
                        methodStr.append(parameterTypes[i].getName());
                        methodStr.append(" arg");
                        methodStr.append(i);
                        if (i != parameterTypes.length - 1) {
                            methodStr.append(",");
                        }
                    }
                    methodStr.append("){");
                    // 方法体当中的代码怎么写？
                    // 获取sqlId（这里非常重要：因为这行代码导致以后namespace必须是接口的全限定接口名，sqlId必须是接口中方法的方法名。）
                    String sqlId = daoInterface.getName() + "." + methodName;
                    // 获取SqlCommondType
                    String sqlCommondTypeName = sqlSession.getConfiguration().getMappedStatement(sqlId).getSqlCommandType().name();
                    if ("SELECT".equals(sqlCommondTypeName)) {
                        methodStr.append("org.apache.ibatis.session.SqlSession sqlSession = com.powernode.bank.utils.SqlSessionUtil.openSession();");
                        methodStr.append("Object obj = sqlSession.selectOne(\"" + sqlId + "\", arg0);");
                        methodStr.append("return (" + returnTypeName + ")obj;");
                    } else if ("UPDATE".equals(sqlCommondTypeName)) {
                        methodStr.append("org.apache.ibatis.session.SqlSession sqlSession = com.powernode.bank.utils.SqlSessionUtil.openSession();");
                        methodStr.append("int count = sqlSession.update(\"" + sqlId + "\", arg0);");
                        methodStr.append("return count;");
                    }
                    methodStr.append("}");
                    System.out.println(methodStr);
                    try {
                        // 创建CtMethod对象
                        CtMethod ctMethod = CtMethod.make(methodStr.toString(), ctClass);
                        ctMethod.setModifiers(Modifier.PUBLIC);
                        // 将方法添加到类
                        ctClass.addMethod(ctMethod);
                    } catch (CannotCompileException e) {
                        throw new RuntimeException(e);
                    }
                });
                try {
                    // 创建代理对象
                    Class<?> aClass = ctClass.toClass();
                    Constructor<?> defaultCon = aClass.getDeclaredConstructor();
                    Object o = defaultCon.newInstance();
                    return o;
                } catch (Exception e) {
                    throw new RuntimeException(e);
                }
            }
        }
        ```
  - MyBatis中接口代理机制及使用
  - MyBatis小技巧
    collapsed:: true
    - \#{}和${}
      - 使用\#{}
      - 使用${}
      - 什么情况下必须使用${}
      - 拼接表名
      - 批量删除
      - 模糊查询
      - 使用${}
      - 使用\#{}
    - typeAliases
      - 第一种方式：typeAlias
      - 第二种方式：package
      - 在SQL映射文件中用一下
    - mappers
      - resource
      - url
      - class
      - package
    - idea配置文件模板
    - 插入数据时获取自动生成的主键
  - MyBatis参数处理
    collapsed:: true
    - 单个简单类型参数
    - Map参数
    - 实体类参数
    - 多参数
    - @Param注解（命名参数）
    - @Param源码分析
  - MyBatis查询语句专题
    collapsed:: true
    - 返回Car
    - 返回List<Car>
    - 返回Map
    - 返回List<Map>
    - 返回Map<String,Map>
    - resultMap结果映射
    - 使用resultMap进行结果映射
    - 是否开启驼峰命名自动映射
      - 返回总记录条数
  - 动态SQL
    - if标签
    - where标签
    - trim标签
    - set标签
    - choose when otherwise
    - foreach标签
    - 批量删除
    - 批量添加
      - sql标签与include标签
  - MyBatis的高级映射及延迟加载
    collapsed:: true
    - 多对一
      - 第一种方式：级联属性映射
      - 第二种方式：association
      - 第三种方式：分步查询
    - 多对一延迟加载
    - 一对多
      - 第一种方式：collection
      - 第二种方式：分步查询
    - 一对多延迟加载
  - MyBatis的缓存
    collapsed:: true
    - 一级缓存
    - 二级缓存
    - MyBatis集成EhCache
  - MyBatis的逆向工程
    collapsed:: true
    - 逆向工程配置与生成
      - 第一步：基础环境准备
      - 第二步：在pom中添加逆向工程插件
      - 第三步：配置generatorConfig.xml
      - 第四步：运行插件
    - 测试逆向工程生成的是否好用
      - 第一步：环境准备
      - 第二步：编写测试程序
  - MyBatis使用PageHelper
    collapsed:: true
    - limit分页
    - PageHelper插件
      - 第一步：引入依赖
      - 第二步：在mybatis-config.xml文件中配置插件
      - 第三步：编写Java代码
  - MyBatis的注解式开发
    collapsed:: true
    - @Insert
    - @Delete
    - @Update
    - @Select
-
- Other
  - `SqlSessionFactoryBuilder` --(Parse解析)--> `Configuration` --(builld)--> `SqlSessionFactory` --(openSession)--> `SqlSession` --(Query)--> `Executor` --(newStatementHandler)--> `StatementHandler` --(handleResultSets)--> `ResultSetHandler`
    via: https://www.bilibili.com/video/BV16u411X7NB?p=4
-