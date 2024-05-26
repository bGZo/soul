title:: command/env
- 传递环境变量，而不需要在外部环境（例如当前 Shell 中）设置它们
-
-
- Cases
  - 假设你想运行一个 Node.js 应用，同时要为它设置名为 `USER` 的变量
    - ```shell
      env USER=flavio node app.js
      ```
      - Node.js 应用可以通过 Node 的 `process.env` 接口访问 `USER` 这个环境变量。
  - 清除所有已经设置的环境变量
    - ```shell
      env -i /usr/local/bin/node app.js
      ```
  - 让某个变量在你运行的应用中无法访问
    - ```shell
      env -u HOME node app.js
      # 移除了当前环境中的 HOME 变量
      ```
-
-