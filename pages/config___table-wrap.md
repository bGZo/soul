icon:: 📄
created:: [[20240728]]
exclude-from-graph-view:: true
description:: config for custom table line wrap.

- ## How this works
  - ```css
    a.tag[data-ref*="config/table-wrap"] {
        display: none;
    }
    [data-refs-self*="config/table-wrap"] .whitespace-nowrap {
      white-space: wrap;
    }
    ```
  - Then tag on blocks what you want to custom
-