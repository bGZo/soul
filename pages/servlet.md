title:: servlet
tags:: #[[java]]

-
- 概括
  collapsed:: true
  - Server Applet, 服务器端小程序
  - Java Sun -> Servlet(API)
    - 它对开发动态网站需要使用的原生 Java API 进行了封装，形成了一套新的 API
    - 只需处理**业务逻辑**，不需要再为那些基础性的、通用性的功能编写代码
  - **规范**
    - 只是一种规范, 不是具体的东西
    - 除了 Sun 公司，其它公司也可以实现 Servlet 规范 => **Servlet 容器**
      id:: 63159c22-44d2-4292-87ea-392c76727867
      - 管理程序员编写的 Servlet 类
        - Tomcat
        - Weblogic
        - Jetty
        - Jboss
        - WebSphere
  - 接口 `Servlet`
  - 版本
    - ![image.png](../assets/imu/java/image_1662360951450_0.png)
-
- Container
  collapsed:: true
  - ((63159c22-44d2-4292-87ea-392c76727867))
  - #vs Server
    - 服务器
      - 功能单一, 只能提供 http(s) 服务(静态服务), 不能执行任何编程语言
      - 动态网站
        - **必要条件**
          - **编程语言运行环境（运行时， [[runtime]] ）+ 数据库管理系统**
        - TODO 网站开发可以用**非脚本语言**吗???
      - ![image.png](../assets/imu/java/image_1662362580896_0.png)
    - 容器
      - 传统 JRE 无法运行 Servlet
        - Servlet 容器就是 Servlet 代码的运行环境（运行时）
      - 用来装类，装对象
        - 生活中, 用来装水、装粮食
      - **我们自己编写的 Servlet 类为什么需要 Servlet 容器来管理呢？**
        - 我们编写的 Servlet 类没有 main() 函数，不能独立运行，只能作为一个模块被载入到 Servlet 容器，然后由 Servlet 容器来实例化，并调用其中的方法。
      - ![image.png](../assets/imu/java/image_1662363471054_0.png)
        - 一个动态页面对应一个 Servlet 类，开发一个动态页面就是编写一个 Servlet 类，当用户请求到达时，Servlet 容器会根据配置文件（web.xml）来决定调用哪个类。
        - 用户的 HTTP 请求首先到达 Web 服务器，Web 服务器判断该请求是静态资源还是动态资源：如果是静态资源就直接返回，此时相当于用户下载了一个服务器上的文件；如果是动态资源将无法处理，必须将该请求转发给 Servlet 容器
        - Servlet 容器接收到请求以后，会根据配置文件（web.xml）找到对应的 Servlet 类，将它加载并实例化，然后调用其中的方法来处理用户请求；处理结束后，Servlet 容器将处理结果再转交给 Web 服务器，由 Web 服务器将处理结果进行封装，以 HTTP 响应的形式发送给最终的用户
      - Web Container 往往也会自带 Web Server
        - 所以您可以不用再安装 Apache、IIS、Nginx 等传统意义上的服务器，只需要安装一款 Web 容器，就能部署 Servlet 网站了
        - 有的教材将 Tomcat 称为 Web 容器，有的教材又将 Tomcat 称为 Web 服务器，两者的概念已经非常模糊了。
        - ![image.png](../assets/imu/java/image_1662363618717_0.png)
      -
  - Tomcat
    - 目录结构
-
- Create(3)
  collapsed:: true
  - Servlet & GenericServlet & HttpServlet
    - ![image.png](../assets/imu/java/image_1662364811475_0.png)
    -
    - Servlet
      - ```java
        void init(ServletConfig config);            // 初始化
        void service(ServletRequest req,ServletResponse res); // 处理请求
        void destroy();
        ServletConfig getServletConfig();
        String getServletInfo();
        ```
    - GenericServlet
      - 实现了 Servlet 接口的抽象类
      - id:: 6315b145-0fdc-4dad-96b8-db6641fac0c5
        ```java
        String getInitParameter(String name);       // web.xml 中进行配置
        Enumeration<String> getInitParameterNames();  // 初始化参数的名字的枚举集合
        ServletContext getServletContext();       // 上下文对象的引用
        String getServletName();            // 实例名称
        ```
    - HttpServlet
      - GenericServlet 的子类在
      - HTTP/1.1 协议中共定义了 7 种请求方式，即 GET、POST、HEAD、PUT、DELETE、TRACE 和 OPTIONS
        - doGet()、doPost()、doHead()、doPut()、doDelete()、doTrace() 和 doOptions()
        - HttpServlet 重写了 service() 方法
          - 先获取客户端的请求方式，然后根据请求方式调用对应 doXxx 方法
    - Servlet 程序 (MyServlet 类)
      - 一个实现了 Servlet 接口的 Java 类。
-
- Deploy & Visit
  collapsed:: true
  - webapps Content
    - | 目录 | 描述| 是否必要|
      | ---------------------------- | ---------------------------------------------------------- | --- |
      | \\servletDemo                 | Web 应用的根目录，属于该 Web 应用的所有资源都存放在这个目录下。                       | 是   |
      | \\servletDemo\\WEB-INF         | 存放 web.xml、lib 目录以及 classes 目录等。                           | 是   |
      | \\servletDemo\\WEB-INF\\classes | 存放各种 .class 文件或者包含 .class 文件的目录，Servlet 类的 .class 文件也存放在此。 | 否   |
      | \\servletDemo\\WEB-INF\\lib     | 存放应用所需的各种 jar 包，例如 JDBC 驱动程序的 jar 包。                       | 否   |
      | \\servletDemo\\WEB-INF\\web.xml | web.xml 中包含应用程序的配置和部署信息。                                   | 是   |
    - ![image.png](../assets/imu/java/image_1662366951672_0.png)
-
- Annotation 注解
  collapsed:: true
  - 属性
    - ![image.png](../assets/imu/java/image_1662367293682_0.png)
  - `web.xml`
    - 将所有的 Servlet 的配置集中进行管理
    - 冗长解决方案 => 注解（Annotation）就是一种更好的选择
      - From Servlet 3.0
    - Annotation #vs XML
      - `@WebServlet`
        - 优点：@WebServlet 直接在 Servlet 类中使用，代码量少，配置简单。每个类只关注自身业务逻辑，与其他 Servlet 类互不干扰，适合多人同时开发。
        - 缺点：Servlet 较多时，每个 Servlet 的配置分布在各自的类中，不便于查找和修改。
      - `@web.xml`
        - 优点：集中管理 Servlet 的配置，便于查找和修改。
        - 缺点：代码较繁琐，可读性不强，不易于理解。
-
- 生命周期
  collapsed:: true
  - 初始化 => 运行时 => 销毁
    - 初始化
      - 加载和实例化 Servlet；
        - **==Servlet 实例可以通过 ServletConfig 对象获取在 web.xml 或者 @WebServlet 中配置的初始化参数==**
      - 调用 init() 方法进行初始化
        - 只能被调用一次
    - 运行时
      - Servlet 容器接收到来自客户端请求时，容器会针对该请求分别创建一个 ServletRequst 对象和 ServletResponse 对象，将它们以参数的形式传入 service() 方法内，并调用该方法对请求进行处理
        - init() 方法必须已成功执行
      - Servlet 的每一次请求，Servlet 容器都会调用一次 service() 方法，并创建新的 ServletRequest 和 ServletResponse 对象。即 service() 方法在 Servlet 的整个生命周期中会被调用多次。
    - 销毁
      - 只能被调用一次
    -
  - ![image.png](../assets/imu/java/image_1662360074985_0.png)
-
- 启动优先级 in `web.xml` -> `load-on-startup`
-
- 接口
  collapsed:: true
  - ServletConfig | **容器初始化参数**
    - ((6315b145-0fdc-4dad-96b8-db6641fac0c5))
    - 方式
      - `web.xml`
      - `@WebServlet`
  - ServletContext | **Servlet 上下文**
    - Web 应用中的所有 Servlet 共享同一个 ServletContext 对象，不同 Servlet 之间可以通过 ServletContext 对象实现数据通讯，因此 ServletContext 对象也被称为 Context 域对象。
    - > 域对象是服务器在内存上创建的存储空间，该空间用于不同动态资源（例如 Servlet、JSP）之间传递与共享数据。
    - 获得对象 (4)
      - ```java
        ServletContext servletContext;
        servletContext = this.getServletContext();            // GenericServlet
        servletContext = this.getServletConfig().getServletContext(); // ServletConfig
        servletContext = req.getSession().getServletContext();      // HttpSession
        servletContext = req.getServletContext();           // HttpServletRequest
        ```
      - 应用
        - 获取上下文初始化参数
          - `web.xml` set tags
            - ```xml
              <context-param>
              <!-- 元素用来声明上下文初始化参数，必须在根元素 <web-app> 内使用 -->
                <param-name>name</param-name>
                <!-- 唯一 -->
                <param-value>AppName</param-value>
              </context-param>
              <context-param>
                <param-name>url</param-name>
                  <param-value>AppUrl</param-value>
              </context-param>
              ```
          - ```java
            String getInitParameter(String name);
            Enumeration<String> getInitParameterNames();
            ```
        - 实现数据通讯
          - id:: 6315ba24-8210-41b0-adb3-06547995067f
            ```java
            void setAttribute(String name, Object object);
            void removeAttribute(String name);
            Object getAttribute(String name);
            Enumeration getAttributeNames();
            ```
        - 读取 Web 应用下的资源文件
          - ```java
            Set getResourcePaths(String path);        // 子目录和文件的名称
            String getRealPath(String path);        // 资源文件的真实路径（文件的绝对路径）
            URL getResource(String path);         // 映射到资源文件的 URL 对象
            InputStream getResourceAsStream(String path); // 映射到资源文件的 InputStream 输入流对象
            ```
  - HttpServletRequest | **Servlet 请求**
    - Servlet 处理 HTTP 请求的流程
      - Servlet 容器接收到来自客户端的 HTTP 请求后，容器会针对该请求分别创建一个 HttpServletRequest 对象和 HttpServletReponse 对象。
      - 容器将 HttpServletRequest 对象和 HttpServletReponse 对象以参数的形式传入 service() 方法内，并调用该方法。
      - 在 service() 方法中 Servlet 通过 HttpServletRequest 对象获取客户端信息以及请求的相关信息。
      - 对 HTTP 请求进行处理。
      - 请求处理完成后，将响应信息封装到 HttpServletReponse 对象中。
        Servlet 容器将响应信息返回给客户端。
      - 当 Servlet 容器将响应信息返回给客户端后，HttpServletRequest 对象和 HttpServletReponse 对象被销毁。
      - ![image.png](../assets/imu/java/image_1662368872209_0.png)
    - 获取请求行信息
      - ```java
        String getMethod();
        String getRequestURI();
        String getQueryString();
        String getContextPath();
        String getServletPath();
        String getRemoteAddr();
        String getRemoteHost();
        ```
    - 获取请求头信息
      - ```java
        String getHeader(String name);
        Enumeration getHeaders(String name);
        Enumeration getHeaderNames();
        String getContentType();
        int getContentLength()
        String getCharacterEncoding();
        ```
    - 获取 form 表单的数据
      - ```java
        String getParameter(String name);
        String[] getParameterValues (String name);
        Enumeration getParameterNames();
        Map getParameterMap();
        ```
  - RequestDispatcher | (协作) **请求转发** / 请求包含?
    id:: 6315b6aa-c5a1-46f4-b1bc-5ab3b5c2929b
    - 获得 RequestDispatcher 对象(2)
      - **ServletContext** 的 getRequestDispatcher(String path) 方法
        - 必须为绝对路径
      - **ServletRequest** 的 getRequestDispatcher(String path) 方法
        - 可以为绝对路径，也可以为相对路径
    - ```java
      void forward(ServletRequest request,ServletResponse response);
      void include(ServletRequest request,ServletResponse response);
      ```
    - 原理
      - ![image.png](../assets/imu/java/image_1662369494829_0.png)
    - 特点
      - 不支持跨域, 只能跳到当前应用中的资源
      - URL 不会发生变化, 浏览器不知道在服务器内部发生了转发行为
      - 转发的 Web 资源之间共享 request 对象和 response 对象
      - 只有转发到最后一个 Web 资源时，生成的响应才会被发送到客户端
    - request 域对象
      - ((6315ba24-8210-41b0-adb3-06547995067f))
      - #vs Context 域对象
        - 生命周期不同
          - Context 域对象的生命周期从容器启动开始，到容器关闭或者 Web 应用被移除时结束；
          - request 域对象的生命周期从客户端向容器发送请求开始，到对这次请求做出响应后结束。
        - 作用域不同
          - Context 域对象对整个 Web 应用内的所有Servlet都有效；
          - request 域对象只对本次请求涉及的 Servlet 有效。
        - Web 应用中数量不同
          - 整个 Web 应用中只有一个 Context 域对象；
          - 由于 Servlet 能处理多个请求，因此 Web 应用中的每个 Servlet 实例都可以有多个 request 域对象。
        - 实现数据共享的方式不同
          - Context 域对象可以独立完成动态资源之间的数据共享；
          - Request 域对象需要与请求转发配合使用才能实现动态资源之间的数据共享。
  - HttpServletResponse | **Servlet 响应**
    - 响应行
      - ```java
        void setStatus(int status);
        void sendError(int sc);
        ```
    - 响应头
      - ```java
        void addHeader(String name,String value)
        void setHeader (String name,String value);
        void addIntHeader(String name,int value);
        void setIntHeader(String name, int value);
        void setContentType(String type);
        void setCharacterEncoding(String charset);
        ```
    - 响应体
      - ```java
        ServletOutputStream getOutputStream();
        PrintWriter getWriter();
        // 不可同时使用，否则会发生 IllegalStateException 异常。
        ```
    - 重定向
      - 流程
        - 用户在浏览器中输入 URL，请求访问服务器端的 Web 资源。
        - 服务器端的 Web 资源返回一个状态码为 302 的响应信息，该响应的含义为：通知浏览器再次发送请求，访问另一个 Web 资源（在响应信息中提供了另一个资源的 URL）。
        - 当浏览器接收到响应后，立即自动访问另一个指定的 Web 资源。
        - 另一 Web 资源将请求处理完成后，由容器把响应信息返回给浏览器进行展示。
        - ![image.png](../assets/imu/java/image_1662370062860_0.png)
      - #vs ((6315b6aa-c5a1-46f4-b1bc-5ab3b5c2929b))
        - | 区别                           | 转发        | 重定向       |
          | ---------------------------- | --------- | --------- |
          | 浏览器地址栏 URL 是否发生改变            | 否         | 是         |
          | 是否支持跨域跳转                     | 否         | 是         |
          | 请求与响应的次数                     | 一次请求和一次响应 | 两次请求和两次响应 |
          | 是否共享 request 对象和 response 对象 | 是         | 否         |
          | 是否能通过 request 域对象传递数据        | 是         | 否         |
          | 速度                           | 相对要快      | 相对要慢      |
          | 行为类型                         | 服务器行为     | 客户端行为     |
      - ```java
        void sendRedirect(String location);
        ```
  - FilterConfig
    id:: 6315b6b4-a235-4973-bfab-b360af1774b1
    - ```java
      String getInitParameter(String name);
      Enumeration getInitParameterNames();
      ServletContext getServletContext();
      String getFilterName();
      ```
-
- Cookie | **客户端会话**
  collapsed:: true
  - 分类(2)
    - 会话级别 Cookie (default)
      - 内存
    - 持久的 Cookie
      - 外存
  - 流程
    - 客户端浏览器访问服务器时，服务器通过在 HTTP 响应中增加 Set-Cookie 字段，将数据信息发送给浏览器。
    - 浏览器将 Cookie 保存在内存中或硬盘上。
    - 再次请求该服务器时，浏览器通过在 HTTP 请求消息中增加 Cookie 请求头字段，将 Cookie 回传给 Web 服务器。服务器根据 Cookie 信息跟踪客户端的状态。
    - ![image.png](../assets/imu/java/image_1662370373637_0.png)
  - API
    - HttpServletResponse 接口和 HttpServletRequest 接口
      - ```java
        void addCookie(Cookie cookie);
        Cookie[] getCookies();
        ```
    - javax.servlet.http.Cookie
      - ```java
        int getMaxAge() ;
        String getName() ;
        String getPath();
        boolean getSecure() ;
        String getValue() ;
        int getVersion() ;
        void setMaxAge(int expiry);
        void setPath(String uri);
        void setSecure(boolean flag);
        void setValue(String newValue);
        ```
  - 使用细节
    - 一个 Cookie 只能标识一种信息，至少包含一个名称（NAME）和一个值（VALUE）
    - 如果创建了一个 Cookie，并发送到浏览器，默认情况下它是一个会话级别的 Cookie
      - 用户退出浏览器就被删除。如果希望将 Cookie 存到磁盘上，则需要调用 setMaxAge(int maxAge) 方法设置最大有效时间，以秒为单位。
    - 使用 setMaxAge(0) 手动删除 Cookie时，需要使用 setPath 方法指定 Cookie 的路径，且该路径必须与创建 Cookie 时的路径保持一致
  - 缺点
    - 在 HTTP 请求中，Cookie 是**明文传递**的，容易泄露用户信息，安全性不高。
    - **浏览器可以禁用** Cookie，一旦被禁用，Cookie 将无法正常工作。
    - Cookie 对象中**只能设置文本（字符串）信息**。
    - 客户端浏览器**保存 Cookie 的数量和长度是有限制**的。
-
- Session | **服务端会话**
  collapsed:: true
  - 原理
    - 当客户端第一次请求会话对象时，服务器会创建一个 Session 对象，并为该 Session 对象分配一个唯一的 SessionID（用来标识这个 Session 对象）
    - 服务器将 SessionID 以 Cookie（Cookie 名称为：“JSESSIONID”，值为 SessionID 的值）的形式发送给客户端浏览器；
    - 客户端浏览器再次发送 HTTP 请求时，会将携带 SessionID 的 Cookie 随请求一起发送给服务器；
    - 服务器从请求中读取 SessionID，然后根据 SessionID 找到对应的 Session 对象
    - ![image.png](../assets/imu/java/image_1662370705364_0.png)
    - 注意：
      - 流程中的 Cookie 是容器自动生成的，它的 maxAge 属性取值为 -1，表示仅当前浏览器有效。
      - 浏览器关闭时，对应的 Session 并没有失效，但此时与此 Session 对应的 Cookie 已失效，导致浏览器无法再通过 Cookie 获取服务器端的 Session 对象。
      - 同一浏览器的不同窗口共享同一 Session 对象，但不同浏览器窗口之间不能共享 Session 对象。
  - #vs Cookie
    - | 不同点         | Cookie                                              | Session                                                   |
      | ----------- | --------------------------------------------------- | --------------------------------------------------------- |
      | 存储位置     | 客户端 浏览器内存/硬盘                         | 服务器端                                       |
      | 大小数量   | 有限(浏览器)                              | 不受限制                                     |
      | 存放数据类型    | 字符串                                    | 对象                                          |
      | 安全性      | 低(明文传递+客户端存储) | 较高                                     |
      | 服务器压力 | 不占服务器资源                          | 用户独占Session, 并发压力大 |
      | 支持跨域     | ✔                                     | ✖                                      |
  - API
    - ```java
      HttpSession session=request.getSession(); // 获取session对象
      long getCreationTime();
      String getId();
      long getLastAccessedTime();
      int getMaxInactiveInterval() ;
      ServletContext getServletContext() ;
      void invalidate();
      void setMaxInactiveInterval(int interval);
      ```
  - 设置 Session 过期时间 (2)
    - Session 的默认过期时间为 30 分钟
    - 使用 <session-config> 元素
    - 调用 setMaxInactiveInterval() 方法
  - 生命周期
    - 创建
      - Session 对象在容器第一次调用 request.getSession() 方法时创建
      - >静态资源无Session
    - 销毁
      - Session 过期；
      - 调用 session.invalidate() 方法，手动销毁 Session；
      - 服务器关闭或者应用被卸载。
  - Session 域对象
    - Session 、request 以及 ServletContext 合称为 Servlet 的三大域对象，它们都能保存和传递数据，但是三者也存在许多差异
    - #vs request, context
      - | 不同   | request                                                         | Session                                                                                                    | ServletContext                                        |
        | ---- | --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
        | 类型   | javax.servlet.http.HttpServletRequest                           | javax.servlet.http.HttpSession                                                                             | javax.servlet.ServletContext                          |
        | 创建   | 客户端向容器发送请求时创建。                                                  | 容器第一次调用 getSession() 方法时创建。                                                                                | Servlet 容器启动时创建。                                      |
        | 销毁   | 容器对这次请求做出响应后销毁。                                                 | Session 销毁的时机：<br><br><br>- 关闭服务器或应用被卸载。<br>- Session 过期，默认为 30 分钟。<br>- 手动调用 session.invalidate() 方法进行销毁。 | 容器关闭或者 Web 应用被移除时销毁。                                  |
        | 有效范围 | 只对当前请求涉及的 Servlet 有效。                                           | Session 对本次会话期间的所有 Servlet 都有效。                                                                            | 对整个 Web 应用内的所有 Servlet 有效。                            |
        | 数量   | Web 应用中的所有 Servlet 实例都可以有多个 request 对象。                         | Web 应用中可以有多个 Session，多个 Servet 实例可以共享同一 Session 对象。                                                        | 在整个 Web 应用中只有一个 Context 对象。                           |
        | 数据共享 | 每一次请求都是一个新的 request 对象。<br>通过和请求转发的配合使用可以实现一次请求中 Web 组件之间共享的数据。 | 每一次会话都是一个新的 Session 对象。<br>通过 Session 域对象可以实现一次会话中的多个请求之间共享数据。                                             | 在一个应用中有且只有一个 Context 对象，作用于整个 Web 应用，可以实现多次会话之间的数据共享。 |
-
- Filter
  collapsed:: true
  - 工作流程
    - 客户端请求访问容器内的 Web 资源。
    - Servlet 容器接收请求，并针对本次请求分别创建一个 request 对象和 response 对象。
    - 请求到达 Web 资源之前，先调用 Filter 的 doFilter() 方法，检查 request 对象，修改请求头和请求正文，或对请求进行预处理操作。
    - 在 Filter 的 doFilter() 方法内，调用 FilterChain.doFilter() 方法，将请求传递给下一个过滤器或目标资源。
    - 目标资源生成响应信息返回客户端之前，处理控制权会再次回到 Filter 的 doFilter() 方法，执行 FilterChain.doFilter() 后的语句，检查 response 对象，修改响应头和响应正文。
    - 响应信息返回客户端。
    - ![image.png](../assets/imu/java/image_1662372590946_0.png)
  - 生命周期
    - 初始化阶段
      - Servlet 容器负责加载和实例化 Filter。容器启动时，读取 web.xml 或 @WebFilter 的配置信息对所有的过滤器进行加载和实例化。
      - 加载和实例化完成后，Servlet 容器调用 init() 方法初始化 Filter 实例。在 Filter 的生命周期内， init() 方法只执行一次。
    - 拦截和过滤阶段
      - 当客户端请求访问 Web 资源时，Servlet 容器会根据 web.xml 或 @WebFilter 的过滤规则进行检查。当客户端请求的 URL 与过滤器映射匹配时，容器将该请求的 request 对象、response 对象以及 FilterChain 对象以参数的形式传递给 Filter 的 doFilter() 方法，并调用该方法对请求/响应进行拦截和过滤。
    - 销毁阶段
      - Filter 对象创建后会**驻留在内存**中，直到容器关闭或应用被移除时销毁。销毁 Filter 对象之前，容器会先调用 destory() 方法，释放过滤器占用的资源
  - 注册与映射 Filter
    - web.xml
      - ```xml
        <filter>
            <filter-name>myFilter</filter-name>
            <filter-class>net.biancheng.www.MyFilter</filter-class>
            <init-param>
                <param-name>name</param-name>
                <param-value>编程帮</param-value>
            </init-param>
            <init-param>
                <param-name>URL</param-name>
                <param-value>www.biancheng.net</param-value>
            </init-param>
        </filter>
        ```
    - @WebFilter
      - ```java
        String filterName;
        String[] urlPatterns;
        String[] value;
        String[] servletNames;
        DispatcherType dispatcherTypes
        WebInitParam[]  initParams;
        boolean asyncSupported;
        String description;
        String displayName;
        ```
  - 过滤器链
    - 拦截过程
      - ![image.png](../assets/imu/java/image_1662376038929_0.png)
    - javax.servlet 包中提供了一个 FilterChain 接口，该接口由容器实现
    - ```java
      void doFilter(ServletRequest request ,ServletResponse response)
      ```
      - 在 Filter.doFilter() 方法中调用 FilterChain.doFilter() 方法的语句前后增加某些程序代码，就可以在 Servlet 进行响应前后实现某些特殊功能，例如权限控制、过滤敏感词、设置统一编码格式等。
    - 接口 -> ((6315b6b4-a235-4973-bfab-b360af1774b1))
-
- Listener 监听器
  collapsed:: true
  - 概念
    - 监听另一个 Java 对象的方法调用或属性改变，当被监听对象发生上述事件后，监听器某个方法将立即自动执行
    - 事件：方法调用、属性改变、状态改变等。
    - 事件源：被监听的对象（ 例如：request、session、servletContext）。
    - 监听器：用于监听事件源对象 ，事件源对象状态的变化都会触发监听器。
    - 注册监听器：将监听器与事件源进行绑定。
  - 按照监听的事件划分(3)
    - 监听对象创建和销毁的监听器
      - ![image.png](../assets/imu/java/image_1662376596747_0.png)
    - 监听对象中属性变更的监听器
      - ![image.png](../assets/imu/java/image_1662376636338_0.png)
    - 监听 HttpSession 中的对象状态改变的监听器
      - ![image.png](../assets/imu/java/image_1662376674348_0.png)
-
- 统计在线人数 via: [Servlet监听器统计网站在线人数](http://c.biancheng.net/servlet2/user-online.html)
-
- More Link
  - [Jakarta Servlet - Wikipedia](https://en.wikipedia.org/wiki/Jakarta_Servlet)
-
- Refs
  - [C语言中文网：C语言程序设计门户网站(入门教程、编程软件)](http://c.biancheng.net/)