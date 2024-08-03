icon:: 📝
created:: [[20240713]]
status:: writing/draft
tags:: #windows
type:: memo

- ## Close Ads
  - created::  [[20240626]]
    type:: tool/star
    source:: https://github.com/xM4ddy/OFGB
    ![](https://img.shields.io/github/stars/xM4ddy/OFGB)
- ## Uninstall build-in soft
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
      via: https://answers.microsoft.com/en-us/windows/forum/all/how-to-permanently-stop-the-widgets-service-from/de082ed2-81db-4074-a334-0c9ca13f15c4
- ## Add flypy
  - ```reg
    Windows Registry Editor Version 5.00
    
    [HKEY_CURRENT_USER\Software\Microsoft\InputMethod\Settings\CHS]
    "UserDefinedDoublePinyinScheme0"="flypy*2*^*iuvdjhcwfg^xmlnpbksqszxkrltvyovt"
    ```
    - Save as `.reg` and run
  - `win+r`
    - `regedit`
      - `计算机\HKEY_CURRENT_USER\Software\Microsoft\InputMethod\Settings\CHS`
        - New Create `UserDefinedDoublePinyinScheme0`
          - `flypy*2*^*iuvdjhcwfg^xmlnpbksqszxkrltvyovt`
- ## Power Search with Everything & Tool bar
  - EverythingToolbar
    icon:: 🛠
    created:: [[20240731]]
    document:: https://github.com/srwi/EverythingToolbar
    status:: tool/star
    type:: tool
    ![](https://img.shields.io/github/stars/srwi/EverythingToolbar)
- ## References
  - [^china-office]: https://v2ex.com/t/1048191