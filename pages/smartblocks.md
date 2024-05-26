title:: smartblocks
alias::
desc::
tags:: #logseq/plugin
author::
source::
mark::
created:: 20221213
closed::
- [[Issue]]
  - TODO [#B] The block properties would be missing
    source:: [The block properties would be missing · Issue #46 · sawhney17/logseq-smartblocks](https://github.com/sawhney17/logseq-smartblocks/issues/46)
    collapsed:: true
    - Here is my template:
      - ```
        template:: Placeholder
        template-including-parent:: false
        - title::
          desc::
          tags::
          source::
          mark::
          start-date::
          end::
          collapsed:: true
          - Placeholder
            - Placeholder
              background-color:: grey
              collapsed:: true
          - Placeholder
        ```
    - When I use SmartBlocks, what I get:
      - ```
        - title::
          desc::
          tags::
          source::
          mark::
          start-date::
          end::
          - Placeholder
            - Placeholder
              backgroundcolor:: grey
          - Placeholder
        ```
    - Basically the style of template is missing, like properties of block (`collapsed::` & `background-color::`), it's not same as build-in insert way of template.
    - Is that a bug?