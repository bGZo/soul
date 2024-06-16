## [[issue]]
collapsed:: true
  - DONE Fork somebody repo cannot change to private?
    - [What security issue is caused by changing the visibility of a fork on Github? - Stack Overflow](https://stackoverflow.com/questions/71446341/what-security-issue-is-caused-by-changing-the-visibility-of-a-fork-on-github)
  -
- ## [[template]]
  collapsed:: true
  - template:: github
    template-including-parent:: false
    - title:: ![](https://img.shields.io/github/stars/)
      tags:: #Github #opensource
      created:: <% today %>
      mark::
  - template:: page/github
    template-including-parent:: false
    - title::
      tags:: #Github #opensource
      created:: <% today %>
      mark:: ![](https://img.shields.io/github/stars/)
- collapsed:: true
  ---
  - 在 `page_name`中,  不会再加入 `[[]]`的符号;
    - ```
      source::  ![](https://img.shields.io/github/stars/)
      desc::
      tags::
      author::
      mark::
      start-date:: <% today %>
      end-date::
      template:: github
      ```