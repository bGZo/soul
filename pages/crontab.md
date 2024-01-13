alias:: commands/crontab
mark:: Job scheduler on Unix-like operating systems | 定期运行的作业
icon:: ⌘
tags:: #Linux 

date:: 20230625
title:: crontab
wikipedia:: [cron - Wikipedia](https://en.wikipedia.org/wiki/Cron)

- ## Why
- ## How
- ## What
  - [crontab (opengroup.org)](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/crontab.html#tag_20_25_07)
  - [Cron - ArchWiki](https://wiki.archlinux.org/title/cron)
    - base system uses [systemd/Timers](https://wiki.archlinux.org/title/Systemd/Timers) instead by default.
    - ```
      # ┌───────────── minute (0 - 59)
      # │ ┌───────────── hour (0 - 23)
      # │ │ ┌───────────── day of the month (1 - 31)
      # │ │ │ ┌───────────── month (1 - 12)
      # │ │ │ │ ┌───────────── day of the week (0 - 6) (Sunday to Saturday;
      # │ │ │ │ │             7 is also Sunday on some systems)
      # │ │ │ │ │
      # │ │ │ │ │
      # * * * * * <command to execute>
      ```
    - ```shell
      crontab -l
      # 显示你的作业
      
      crontab -e
      # 编辑已有的 Cron 作业
      # 设定编辑器 EDITOR=nano crontab -e
      
      ```
    - Cases
      - 每 12 小时运行来自 `/Users/flavio/test.sh` 的脚本
        - ```shell
          * */12 * * * /Users/flavio/test.sh >/dev/null 2>&1
          ```
  - Tools
    - [Crontab Generator - Generate crontab syntax](https://crontab-generator.org/)
    - [Crontab.guru - The cron schedule expression editor](https://crontab.guru/)