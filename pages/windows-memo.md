icon:: 📝
created:: [[20240713]]
exclude-from-graph-view:: true
status:: writing/draft
tags:: #windows
type:: memo

- ## Close Ads
  collapsed:: true
  - [[xM4ddy/OFGB]]
- ## Close Function
  collapsed:: true
  - Close 粘滞键
    - 设置 > 粘滞键 > 关闭所有触发方式
    - https://blog.csdn.net/xitongzhijia_abc/article/details/125505930
- ## Uninstall build-in soft
  collapsed:: true
  - Setting => Application => installed
    logseq.order-list-type:: number
    - Office plus [^china-office]
      logseq.order-list-type:: number
    - Office plus pdf
      logseq.order-list-type:: number
  - Widget
    logseq.order-list-type:: number
    - Run under admin
      ```shell
      Get-AppxPackage *WebExperience* | Remove-AppxPackage
      ```
      via:
      - https://superuser.com/questions/1684005
      - https://answers.microsoft.com/en-us/windows/forum/all/how-to-permanently-stop-the-widgets-service-from/de082ed2-81db-4074-a334-0c9ca13f15c4
- ## Add flypy
  collapsed:: true
  - ```reg
    Windows Registry Editor Version 5.00
    
    [HKEY_CURRENT_USER\Software\Microsoft\InputMethod\Settings\CHS]
    "UserDefinedDoublePinyinScheme0"="flypy*2*^*iuvdjhcwfg^xmlnpbksqszxkrltvyovt"
    ```
    - Save as `.reg` and run
  - `win+r` => `regedit`
    - ```
      Computer\HKEY_CURRENT_USER\Software\Microsoft\InputMethod\Settings\CHS
      ```
      - New Create `UserDefinedDoublePinyinScheme0`
        - `flypy*2*^*iuvdjhcwfg^xmlnpbksqszxkrltvyovt`
- ## Search with Everything & Tool bar
  collapsed:: true
  - [[EverythingToolbar]]
- ## Disable Turbo boost on ==Laptop==
  collapsed:: true
  - #+BEGIN_TIP
    Considered [[battery]] duration, disable `Processor performance boost mode` on `powercfg.cpl`
    #+END_TIP
  - If not shown on power setting, go `regedit` to edit: [^turbo-boost]
    - ```
      Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\be337238-0d82-4146-a960-4f3749d470c7
      ```
      - Set `Attributes` from `1` to `2`.
  - The turn back to set them disable.
- ## References
  collapsed:: true
  - [^china-office]: https://v2ex.com/t/1048191
  - collapsed:: true
    [^turbo-boost]: https://www.youtube.com/watch?v=iWBVtXPfTB0
    - Seem like some pc support edit on the bios
      collapsed:: true
      - Settings --> AMD OverClocking --> Precision Boost Overdrive
        via: https://www.reddit.com/r/AMDHelp/comments/es0d4a/how_exactly_do_you_disable_pbo/
      -
-
- ## TODO [[scoop]]
- ## TODO Remote Config
  collapsed:: true
  - Reg editor
- ## TODO 备份 .m2 目录
-
-