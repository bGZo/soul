- [[template]]
  - template:: word(default: en)
    template-including-parent:: false
    - title::
      definition:: {{cloze }}
      tags:: #card, #English/word
      refs::
      mark::
  - template:: word/zh
    template-including-parent:: false
    - title::
      definition:: {{cloze }}
      tags:: #card, #Chinese/word
      refs::
      mark::
  - template:: word/it
    template-including-parent:: false
    - title::
      definition:: {{cloze }}
      tags:: #card, #programming/word
      refs::
      mark::
  - 在 `page_name`中,  不会再加入 `[[]]`的符号;
    collapsed:: true
    - ```markdown
      # archived
      - template:: wordMeta
        name::
        full:: {{cloze }}
        tag::
        mark::
        type::
      - template:: wordMeta-itRef
        name::
        full:: {{cloze }}
        tag::
        mark::
        type:: itRef
      - template:: wordMeta-abbr
        name::
        full:: {{cloze }}
        tag::
        mark::
        type:: abbr
      ```