alias:: 模板
collapsed:: true
public:: true
start-date:: 20230531
title:: Template

  - template:: page
    template-including-parent:: false
    collapsed:: true
    - alias:: 
      define:: 
      icon:: 
      start-date:: ``{ date.now.format('YYYYMMDD') }``
      tags:: 
      title:: ``{ c.page.name }``
    - ## Why
      -
    - ## How
      -
    - ## What
      -
  - template:: page/public
    template-including-parent:: false
    collapsed:: true
    - alias:: 
      define:: 
      icon:: 
      public:: true
      start-date:: ``{ date.now.format('YYYYMMDD') }``
      tags:: 
      title:: ``{ c.page.name }``
    - ## Why
      -
    - ## How
      -
    - ## What
      -
- ## Why
  - As I said, ((646ad604-3548-4c57-a41a-4c551df8a8cc)), **every page should have a template page**, then we could type more productive.
- ## How
  - How to write the template in a standard way? #.ol
    - Using page template as soon as possible, giving up the block template.
    - Sort the properties by the initial.
    - Don't add the `[[]]` in `page_name`.
      id:: 6375b6b8-8628-4bf0-9027-668073dceec6
    - #+BEGIN_WARNING
      After being imported [[stdword/logseq13-full-house-plugin]], the whole default variables should be changed again.
      #+END_WARNING
    - ```markdown
      - template:: placeholder
        template-including-parent:: false
        - alias:: 
        	collapsed:: true
          define:: 
        	icon::
      	public:: true
      	start-date:: ``{ date.now.format('YYYYMMDD') }``
      	tags:: 
      	title:: ``{ c.page.name }``
      ```
      - Other properties options references
        collapsed:: true
        - ```yml
          url:: 
          :: 
          title:: 
          #========#
          author:: 
          publisher:: 
          artisit:: 
          developer:: 
          #========#
          end-date:: 
          #========#
          :: 
          released-date:: 
          published-date:: 
          ```
    - Here are [[Deprecated]] properties:
      - `url`
      - `mark`
      - `desc`
      - `release-date`
      - `name`
      - `end`
        collapsed:: true
        - 一天之内就能完成的东西，比如唱片、专辑，没有必要缀一个这样的属性。
        - （PS: 这其实是一个偷懒的做法）
- ## What
  - Old templates archived
    collapsed:: true
    - template:page/tool
      template-including-parent: false
      - icon:: 
        title:: 
        alias:: 
        desc:: 
        tags:: #tools
        document:: 
        changelog:: 
        community:: 
        mark:: 
        start-date:: <% today %>
      - #+BEGIN_PINNED
        <!-- Rules -->
        #+END_PINNED
      - ## [[cheat/sheet]]
        - ### [[shortcut]]
        -
      - ## [[bookmark]]
        -
      - ## [[Issue]]
        - #closed
          -
        -
      - ## 📃 Reference
        -
    - delete ``
    - 因为 [sawhney17/logseq-smartblocks](https://github.com/sawhney17/logseq-smartblocks), 改变模板的写法;
    - `#<% today %>` & `<% today %>` 唯一的区别就是前者渲染为标签, 后者渲染为页面; 但都不会真正创建页面
  - `{{query (property template)}}`