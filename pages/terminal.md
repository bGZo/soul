-
- Under Different OS
  - Linux
    collapsed:: true
    - Categories
      - 物理终端
        collapsed:: true
        - `/dev/console`
      - 伪终端
        collapsed:: true
        - 远程网络终端, 图形下的终端
        - `/dev/pts/#(num)`
      - 虚拟终端
        collapsed:: true
        - `/dev/tty#`
      - 串行终端：
        collapsed:: true
        - `/dev/ttys#`
        - ```bash
          cat /etc/shells # see your shell in Linux
          ```
  - WAITING Windows
-
- VSZ/RSS/TTY/STAT/START/PTS & TTY
  - ```bash
    # Physical Line
    | teletype |<--------------------->| teletype |
    # Physical Line
    | Terminal |<->| Modem |<--------------------->| Modem |<->| UART |<->| Computer |
    -------------------------------------------------
    |          Kernel           |
    | UART |  |  Line  |  | TTY  |<---------->| User process A |
    <------>|    |<->|      |<->|    |  | driver |  | discipline |  | driver |<---------->| User process B |
    |  ----------  --------------  |    |  |    ------------------
    |                 ----------  |
    |                        |
    -------------------------------------------------
    ```
-