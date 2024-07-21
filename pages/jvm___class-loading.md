tags:: TODO
-
- Class Life Cycle
  id:: 6331a761-a18d-4464-b9fa-69756c4a9f6f
  - (Class Loading Process)
    background-color:: grey
    id:: 6331aa90-8b85-4ce1-94f9-d6438c7a3405
    - 加载
    - 连接
      - 验证
      - 准备
      - 解析
    - 初始化
      id:: 354a1598-83d0-453d-a2b3-27280f6eacbe
  - 使用
  - 卸载
-
- Process
  - ((6331aa90-8b85-4ce1-94f9-d6438c7a3405))
    - 任务
      - 通过全类名获取定义此类的二进制字节流
      - 将字节流所代表的静态存储结构转换为方法区的运行时数据结构
      - 在内存中生成一个代表该类的  `Class`  对象，作为方法区这些数据的访问入口
    -
  - ((354a1598-83d0-453d-a2b3-27280f6eacbe))
    - ???
  - Class Loader
    - 总结
    - 双亲委派模型
    - 自定义类加载器
-
-
-
- Refs
  - [类加载过程详解 | JavaGuide](https://javaguide.cn/java/jvm/class-loading-process.html)
  - [https://docs.oracle.com/javase/specs/jvms/se7/html/jvms-5.html](https://docs.oracle.com/javase/specs/jvms/se7/html/jvms-5.html)
  - TODO ((6331a761-a18d-4464-b9fa-69756c4a9f6f)) 为什么搜不到国外的教材内容???
-