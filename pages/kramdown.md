title:: kramdown
define:: parsing and converting a **superset** of Markdown
tags:: #markdown #ruby/library #mit 
url:: [Home | kramdown](https://kramdown.gettalong.org/index.html)
start:: 20230108

  - based on the Markdown syntax and has been enhanced with features that are found in other Markdown implementations like Maruku , PHP Markdown Extra and Pandoc .
  - ![](https://kramdown.gettalong.org/overview.png)
- ## Syntax
  - [Syntax | kramdown](https://kramdown.gettalong.org/syntax.html) `Difference to Standard Markdown`
    - A list of all the characters (character sequences) that can be *escaped(转义)*:
      - ```
        \         backslash
        .         period
        *         asterisk
        _         underscore
        +         plus
        -         minus
        =         equal sign
        `         back tick
        ()[]{}<>  left and right parens/brackets/braces/angle brackets
        #         hash
        !         bang
        <<        left guillemet
        >>        right guillemet
        :         colon
        |         pipe
        "         double quote
        '         single quote
        $         dollar sign
        ```
    - Difference to Standard Markdown
      - Setext Style
        - ```
          This is a normal
          paragraph.
          
          And A Header
          ------------
          And a paragraph
          
          > This is a blockquote.
          
          And A Header
          ------------
          ```
      - atx Style
        - ```
          # First level header
          
          ### Third level header    ###
          
          ## Second level header ######
          ```
      - Specifying a Header ID
        - ```
          Hello        {#id}
          -----
          
          # Hello      {#id}
          
          # Hello #    {#id}
          ```
      - Code Blocks
        - ```
              Here comes some code
          
              This text belongs to the same code block.
          ```
      - Fenced Code Blocks
        - ```
          \~~~
          def what?
            42
          end
          \~~~
          {: .language-ruby}
          ```
        - ~~~ ruby
          def what?
            42
          end
          ~~~
      - Definition Lists
        - ```
          kramdown
          : A Markdown-superset converter
          
          Maruku
          :     Another Markdown-superset converter
          ```
        - ```
          {:#term} Term with id="term"
          : {:.cls} Definition with class "cls"
          
          {:#term1} First term
          {:#term2} Second term
          : {:.cls} Definition
          ```
      - Inline Links
        - Additional link attributes can be added by using a span IAL after the inline link, for example:
        - ```
          This is a [link](http://example.com){:hreflang="de"}
          ```
      - Abbreviations
        - kramdown provides a syntax to assign the full phrase to an abbreviation. When writing the text, you don’t need to do anything special. However, ==once you add abbreviation definitions, the abbreviations in the text get marked up automatically. Abbreviations can consist of any character except a closing bracket.==
        - ```
          This is some text not written in HTML but in another language!
          
          *[another language]: It's called Markdown
          
          *[HTML]: HyperTextMarkupLanguage
          {:.mega-big}
          ```
      - Typographic Symbols
        - `---` will become an em-dash (like this —)
        - `--` will become an en-dash (like this –)
        - `...` will become an ellipsis (like this …)
        - `<<` will become a left guillemet (like this «) – an optional following space will become a non-breakable space
        - `>>` will become a right guillemet (like this ») – an optional leading space will become a non-breakable space
      - End-Of-Block Marker
      - Attribute List Definitions
      - Block Inline Attribute Lists
      - Span Inline Attribute Lists
      - ...