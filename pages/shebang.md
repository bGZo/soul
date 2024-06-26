title:: shebang
alias:: hashbang, sha-bang, sharp-exclamation, pound-bang, hash-pling, #!
tags:: #Linux
description:: In Linux, this behavior is the result of both kernel and user-space code
description:: [Shebang (Unix) - Wikipedia](https://en.wikipedia.org/wiki/Shebang_(Unix)); [Shebang - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/Shebang)
closed:: [[20230111]]

  - Etymology
    - May have come from an inexact contraction of *SHArp bang* or *haSH bang*, referring to the two typical Unix names for them
    - Another theory on the sh in shebang is that it is from the default shell sh, usually invoked with shebang
- ```bash
  #!/bin/sh – Bourne shell, or a compatible shell, assumed to be in the /bin directory
  #!/bin/bash – Bash shell
  #!/usr/bin/pwsh – PowerShell
  #!/usr/bin/env python3 –Python interpreter, using the env program search path to find it
  #!/bin/false – Do nothing, but return a non-zero exit status, indicating failure.
  ```
  - `#!/bin/false`
    - Prevent stand-alone execution of a script file intended for execution in a specific context, such as by the . command from sh/bash, source from csh/tcsh, or as a .profile, .cshrc, or .login file
    - In this case, the script will not execute any commands at all. Instead, it will simply exit immediately with a non-zero status, indicating that an error has occurred. This might be useful in a few scenarios, like to prevent accidental execution of a script by user, or to have a fallback shellscript where you can redirect to another script
    - It could also be used as a placeholder for scripts that are not meant to be executed, but rather to be used as library scripts that are sourced by other scripts. This way, when someone accidentally runs the script, it won't do anything instead of causing any harm.
- Portability
  - Program location
    - For example, might be in */usr/bin/python3*, */usr/local/bin/python3*, or even something like */home/username/bin/python3* if installed by an ordinary user.
  - Character interpretation
  - Magic number
    - A human-readable instance of a magic number in the executable file, the magic byte string being 0x23 0x21, the two-character encoding in ASCII of #!.
- In [[url]] via: [URI fragment - Wikipedia](https://en.wikipedia.org/wiki/URI_fragment#hash-bang)
  - 分段标识符, 用于浏览器的状态保存
  - 以叹号开头的分段标识符（即`...url#!state...`）会为Google的网页爬虫所索引
  - > In a single-page application (SPA), the entire UI of the application is loaded in a single HTML page and updates to the UI are made dynamically using JavaScript, without the need to reload the entire page. In order to support navigation and the ability to bookmark specific states of the application, the JavaScript frameworks use the browser's fragment identifier (the part of the URL after the "#" character) to keep track of the current state of the application.
    >
    When a user requests a web page that is built using a SPA, the server will respond with the same HTML file regardless of the URL requested. The JavaScript running on the page then uses the fragment identifier to determine which part of the application to display.
    >
    However, this creates a problem for search engine crawlers, which are not able to index the dynamically generated content of a SPA. **The Hashbang technique solves this problem by having the server respond to URLs that start with "#!" by returning a version of the page that is fully rendered with the requested content, rather than just the basic HTML.**(通過返回完全呈現請求內容的頁面版本，而不僅僅是基本的 HTML)
    >
    In summary, "#!" in URLs is used to enable web crawlers to index single-page web applications that use JavaScript frameworks.
    #chatGPT