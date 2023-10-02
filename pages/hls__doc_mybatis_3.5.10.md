file:: [doc_mybatis_3.5.10.pdf](../assets/doc_mybatis_3.5.10.pdf)
file-path:: ../assets/doc_mybatis_3.5.10.pdf

- transactionManager
  ls-type:: annotation
  hl-page:: 29
  hl-color:: yellow
  id:: 640556bb-f303-49ad-8b7b-a713cbb4877a
- By default, it enables auto-commit when closing the connection for compatibility with some drivers. However, for some drivers, enabling auto-commit is not only unnecesry, but also is an expensive operation.
  ls-type:: annotation
  hl-page:: 29
  hl-color:: yellow
  id:: 64055744-3e93-489b-9e97-fa3bc36cda5e
- NOTE If you are planning to use MyBatis with Spring there is no need to configure any TransactionManager because the Spring module will set its own one overriding any previously set configuration.
  ls-type:: annotation
  hl-page:: 30
  hl-color:: yellow
  id:: 640557c0-956b-4ead-b339-b232f87b1459
- dataSource
  ls-type:: annotation
  hl-page:: 30
  hl-color:: yellow
  id:: 6405588e-b1d8-452c-af29-98df978567d7
- This implementation of DataSource pools JDBC Connection objects to avoid the initial connection and authentication time required to create a new Connection instance. This is a popular approach for concurrent web applications to achieve the fastest response.
  ls-type:: annotation
  hl-page:: 31
  hl-color:: yellow
  id:: 64055a65-59ad-49ea-a1b6-fcd45b587846
- use with containers such as EJB or Application Servers that may configure the DataSource centrally or externally and place a reference to it in a JNDI context
  ls-type:: annotation
  hl-page:: 31
  hl-color:: yellow
  id:: 64055b2d-43cb-40de-951e-bdb8646b2aa3
- Scope and Lifecycle
  ls-type:: annotation
  hl-page:: 10
  hl-color:: yellow
  id:: 64059dc6-47bb-4c9c-ab1e-129b91007bba
- There is no need to keep it around once you've created your SqlSessionFactory. Therefore the best scope for instances of SqlSessionFactoryBuilder is method scope
  ls-type:: annotation
  hl-page:: 10
  hl-color:: yellow
  id:: 64059e46-df6e-442c-98fb-17c976a0f826
- the best scope of SqlSessionFactory is application scope
  ls-type:: annotation
  hl-page:: 10
  hl-color:: yellow
  id:: 64059e83-5bcd-4abd-92c4-71440793e10d
- SqlSessionFactory should exist for the duration of your application execution
  ls-type:: annotation
  hl-page:: 10
  hl-color:: yellow
  id:: 64059e91-9c3b-4f06-b77d-33ebea0055eb
- Each thread should have its own instance of SqlSession. Instances of SqlSession are not to be shared and are not thread safe. Therefore the best scope is request or method scope
  ls-type:: annotation
  hl-page:: 10
  hl-color:: yellow
  id:: 64059eaa-a595-475a-b48c-a69038cce026