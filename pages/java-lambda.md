icon:: ☕
also:: [[]], 
created:: [[20240805]]
description::

- ## Why
  -
- ## How
  -
- ## What
  - 局限
    - Lambda 不算 Java 中的语法糖，在敏感场景，如初始化开销时会体现差距，因为在首次调用时，JVM 需要为其构建[CallSite](https://docs.oracle.com/javase/8/docs/api/java/lang/invoke/CallSite.html)实例；
    - Lambda 打断点复杂，程序栈很复杂；
- ## Namespace
  - {{namespace java-lambda}}
- ## ↩ Reference
  -
-
-