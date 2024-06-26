title:: java exception
description:: from java 1.0

- ![image.png](../assets/exception-hierarchy-in-java.webp)
  via: [Exception Hierarchy in Java - BenchResources.Net](https://www.benchresources.net/exception-hierarchy-in-java/)
- ## `Exception` #vs `Error`
  id:: 6277ae64-a3bf-40c7-9165-ce9b94ac7941
  - 程序本身是否可以处理 via:[Java中的两种异常类型是什么？他们有什么区别？__牛客网](https://www.nowcoder.com/questionTerminal/3ded1983c85c4ae197e005bd31777bc7?toCommentId=80958)
    - Error 程序无法处理；
      collapsed:: true
      - 如果OutOfMemoryError、OutOfMemoryError等等
      - 这些异常发生时, java虚拟机一般会终止线程
    - Exception 程序处理一半；
      id:: 627f6081-e6fb-4bc7-b22f-783a222493ea
      - 受检查异常 / 非运行时异常 / RuntimeException
        id:: 627f60a3-8730-44af-94f1-a05b21a29c9c
      - 不受检查异常 / 运行时异常
-
-