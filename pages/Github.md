## [[Issue]]
collapsed:: true
  - DONE Fork somebody repo cannot change to private?
    - [What security issue is caused by changing the visibility of a fork on Github? - Stack Overflow](https://stackoverflow.com/questions/71446341/what-security-issue-is-caused-by-changing-the-visibility-of-a-fork-on-github)
  -
- ## [[Template]]
  collapsed:: true
  - template:: github
    template-including-parent:: false
    - title:: ![](https://img.shields.io/github/stars/) 
      tags:: #Github #opensource 
      start:: <% today %>
      mark::
  - template:: page/github
    template-including-parent:: false
    - title::  
      tags:: #Github #opensource 
      start:: <% today %>
      mark:: ![](https://img.shields.io/github/stars/)
- collapsed:: true
  ---
  - 在 `page_name`中,  不会再加入 `[[]]`的符号;
    - ```
      url::  ![](https://img.shields.io/github/stars/)
      desc:: 
      tags:: 
      author:: 
      mark:: 
      start:: <% today %>
      end:: 
      template:: github
      ```