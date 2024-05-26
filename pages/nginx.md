-
-
-
- Refs
  collapsed:: true
  - [【nginx入门】nginx反向代理与负载均衡教程 - YouTube](https://www.youtube.com/watch?v=UbslfYXlk9U)
    - {{video https://www.youtube.com/watch?v=UbslfYXlk9U}}
    - ```conf
      worker_processes 1;
      events {
          worker_connections 1024;
      }
      http{
          include             mime.types;
          default_type        application/octet-stream;
          sendfile            on;
          keepalive_timeout   65;
          upstream group1{
              server 192.168.0.12:80 weight=10;
              server 192.168.0.12:81 weight=1;
          }
        server {
              listen          80;
              server_name   localhost;
              default_type  text/html;
              location / {
                  echo "hello";
              }
              location /a/ [
                  proxy_pass http://group1/:
              }
          }
      }
      ```