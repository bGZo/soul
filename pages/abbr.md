- [[template]]
  - template:: word(default: en)
    template-including-parent:: false
    - definition:: {{cloze }}
      tags:: #card, #English/word
      refs:: 
      description::
  - template:: word/zh
    template-including-parent:: false
    - definition:: {{cloze }}
      tags:: #card, #Chinese/word
      refs:: 
      description::
  - template:: word/it
    template-including-parent:: false
    - definition:: {{cloze }}
      tags:: #card, #programming
      refs:: 
      description::
  - 在 `page_name`中,  不会再加入 `[[]]`的符号;
    collapsed:: true
    - ```markdown
      # archived
      - template:: wordMeta
        name:: 
        full:: {{cloze }}
        type:: 
      - template:: wordMeta-itRef
        name:: 
        full:: {{cloze }}
        type:: itRef
      - template:: wordMeta-abbr
        name:: 
        full:: {{cloze }}
        type:: abbr
      ```