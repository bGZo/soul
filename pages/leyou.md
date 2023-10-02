tags:: #imu/graduation

- ## 01
  - ### 目标
    - 了解SpringBoot的作用
    - 掌握java配置的方式
    - 了解SpringBoot自动配置原理
    - 掌握SpringBoot的基本使用
    - 了解Thymeleaf的基本使用
  - ### SpringBoot
    - .
  - ### Java配置
    - 比如我们要配置一个数据库连接池，以前会这么玩：
      - ```XML
        <!-- 配置连接池 -->
        <bean id="dataSource" class="com.alibaba.druid.pool.DruidDataSource"
              init-method="init" destroy-method="close">
            <property name="url" value="${jdbc.url}" />
            <property name="username" value="${jdbc.username}" />
            <property name="password" value="${jdbc.password}" />
        </bean>
        ```
-
-
-