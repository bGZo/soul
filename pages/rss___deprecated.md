title:: 
tags:: #rss/deprecated
mark:: 
template:: rss/deprecated
template-including-parent:: true

- ## Why
  - 无要点，或欣赏不来，或充斥着大量内容，好似内容农场。为了澄清信息流，后者更适合喂给AI去做浓缩和提取。
- ## How
  - ### 欣赏不来
    query-table:: true
    query-properties:: [:title :mark]
    {{query (and (property :tags rss/deprecated) (property :tags "#cannot/enjoy"))}}
  - ### 内容过多
    query-table:: true
    query-properties:: [:title :mark]
    {{query (and (property :tags rss/deprecated) (property :tags much/contents))}}
- ## What