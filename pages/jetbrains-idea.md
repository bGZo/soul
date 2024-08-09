icon:: 🛠
also:: IntelliJ-IDEA, IntelliJ IDEA
created:: [[20240808]]
document:: 
exclude-from-graph-view:: true
status:: tool/star
tags:: 
type:: tool

- ## Why
  -
- ## How
  -
- ## What
  - ShortCuts
    collapsed:: true
    - 寻找官方文档
    - 查看设置说明
    - more
      - {{youtube https://www.youtube.com/watch?v=QYO5_riePOQ}}
        via: https://www.jetbrains.com/help/idea/mastering-keyboard-shortcuts.html
  - Plugin
    collapsed:: true
    - ### [[leetcode]]
      - #+BEGIN_NOTE
        Check setting ***custom template*** & ***code type*** when switch language used
        #+END_NOTE
      - #### [[java]]
        collapsed:: true
        - TempFilePath
          ```
          \\wsl$\Ubuntu\home\bgzocg\demo\tasks\leetcode\java\src\cc\bgzo
          ```
        - Code Filename
          ```
          $!velocityTool.camelCaseName(${question.frontendQuestionId})$!velocityTool.camelCaseName(${question.title})
          ```
        - Code Template
          ```java
          package cc.bgzo.leetcode.editor.cn;
          public class $!velocityTool.camelCaseName(${question.frontendQuestionId})$!velocityTool.camelCaseName(${question.title}){
              public static void main(String[] args) {
                  Solution solution = new $!velocityTool.camelCaseName(${question.frontendQuestionId})$!velocityTool.camelCaseName(${question.title})().new Solution();
              }
              ${question.code}
          }
          // ${question.title}
          ${question.content}
          ```
      - #### [[sql]]
        collapsed:: true
        - TempFilePath
          ```
          \\wsl$\Ubuntu\home\bgzocg\demo\tasks\leetcode\mysql\src\cc\bgzo
          ```
        - Code filename
          ```
          [$!{question.frontendQuestionId}]${question.title}
          ```
        - Code Template
          ```
          ${question.content}
          ${question.code}
          ```
- ## Namespace
  - {{namespace jetbrains-idea}}
- ## ↩ Reference
  - [IntelliJ IDEA – the Leading Java and Kotlin IDE (jetbrains.com)](https://www.jetbrains.com/idea/)
-