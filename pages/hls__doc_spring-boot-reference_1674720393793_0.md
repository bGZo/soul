file:: [doc_spring-boot-reference_1674720393793_0.pdf](../assets/doc_spring-boot-reference_1674720393793_0.pdf)
file-path:: ../assets/doc_spring-boot-reference_1674720393793_0.pdf
- @SpringBootTest annotation, which can be used as an alternative to the standard spring-test @ContextConfiguration annotation when you need Spring Boot features.
  ls-type:: annotation
  hl-page:: 156
  hl-color:: yellow
  id:: 63d244b1-8572-4263-8d21-197decff603c
- If you want to focus only on the web layer and not start a complete ApplicationContext, consider using @WebMvcTest instead.
  ls-type:: annotation
  hl-page:: 165
  hl-color:: yellow
  id:: 63d268d6-2155-4425-93aa-21bf9186c87d
- @WebMvcTest auto-configures the Spring MVC infrastructure and limits scanned beans to @Controller,@ControllerAdvice, @JsonComponent, Converter, GenericConverter, Filter, HandlerInterceptor, WebMvcConfigurer, WebMvcRegistrations, and HandlerMethodArgumentResolver. Regular @Component and@ConfigurationProperties beans are not scanned when the @WebMvcTest annotation is used.@EnableConfigurationProperties can be used to include @ConfigurationProperties beans.
  ls-type:: annotation
  hl-page:: 178
  hl-color:: red
  id:: 63d2699d-04d0-41da-bc94-c357a4f43608
- @WebMvcTest
  ls-type:: annotation
  hl-page:: 828
  hl-color:: yellow
  id:: 63d27402-b74e-462a-92f7-8cb894ba8cae
- Mocking and Spying Beans
  ls-type:: annotation
  hl-page:: 171
  hl-color:: yellow
  id:: 63d38953-fce4-471c-990e-98f98b614547
- Supported Connection Pools
  ls-type:: annotation
  hl-page:: 321
  hl-color:: yellow
  id:: 63e13a7c-6d40-4f76-b974-3c91d4868bb2
- @SpringBootApplication also provides aliases to customize the attributes of@EnableAutoConfiguration and @ComponentScan.
  ls-type:: annotation
  hl-page:: 56
  hl-color:: yellow
  id:: 6454d3c0-bdea-4061-879d-813ab8b61927
- • @EnableAutoConfiguration: enable Spring Boot’s auto-configuration mechanism
  ls-type:: annotation
  hl-page:: 55
  hl-color:: yellow
  id:: 6454d495-c37d-467b-9d1c-d17e8d14ddf3
- • @ComponentScan: enable @Component scan on the package where the application is located (see the best practices)
  ls-type:: annotation
  hl-page:: 55
  hl-color:: yellow
  id:: 6454d49b-6373-495c-95ec-ad764fca3ea5
- • @SpringBootConfiguration: enable registration of extra beans in the context or the import of additional configuration classes. An alternative to Spring’s standard @Configuration that aids configuration detection in your integration tests.
  ls-type:: annotation
  hl-page:: 55
  hl-color:: yellow
  id:: 6454d4a5-e090-42a3-b441-e7d0523dcd5d
- Spring Boot chooses to disable suffix pattern matching by default
  ls-type:: annotation
  hl-page:: 261
  hl-color:: yellow
  id:: 6454d5ed-e408-4807-9042-28dd4fa6db8f