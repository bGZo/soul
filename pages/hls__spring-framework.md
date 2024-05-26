file-path:: ../assets/spring-framework.pdf
- 2.3. Design Philosophy
  ls-type:: annotation
  hl-page:: 29
  hl-color:: yellow
  id:: 63ff4c81-939e-4651-b735-744c0b4cd4df
- The term "Spring" means different things in different contexts.
  ls-type:: annotation
  hl-page:: 28
  hl-color:: yellow
  id:: 63ff843b-2b4d-42bc-aca3-7e371d06ca30
- IoC is also known as dependency injection (DI)
  ls-type:: annotation
  hl-page:: 31
  hl-color:: yellow
  id:: 63ff846e-02b8-4234-a392-040d638756bd
- ApplicationContext is a sub-interface of BeanFactory. It adds:• Easier integration with Spring’s AOP features• Message resource handling (for use in internationalization)• Event publication• Application-layer specific contexts such as the WebApplicationContext for use in web applications.
  ls-type:: annotation
  hl-page:: 31
  hl-color:: yellow
  id:: 63ff8679-87eb-460c-8f2c-fb46a5ed1ec1
- Spring Web MVC is the original web framework built on the Servlet API and has been included in the Spring Framework from the very beginning.
  ls-type:: annotation
  hl-page:: 884
  hl-color:: yellow
  id:: 63ff8852-97c7-4c1f-978e-61de46efd270
- Spring MVC, as many other web frameworks, is designed around the front controller pattern where a central Servlet, the DispatcherServlet, provides a shared algorithm for request processing, while actual work is performed by configurable delegate components.
  ls-type:: annotation
  hl-page:: 884
  hl-color:: yellow
  id:: 63ff8afe-e8d9-4dfe-9a1d-02fc80e19647
- Spring Boot relies on the MVC Java configuration to configure Spring MVC and provides many extra convenient options.
  ls-type:: annotation
  hl-page:: 890
  hl-color:: yellow
  id:: 63ff8b7e-8f8e-4ad9-a7ff-a73a4846a1fb
- Finally, if you need to further customize the DispatcherServlet itself, you can override the createDispatcherServlet method.
  ls-type:: annotation
  hl-page:: 894
  hl-color:: yellow
  id:: 63ff8bcf-2730-49b1-9c9d-6a493cf9629c