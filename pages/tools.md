created:: [[20240128]]
icon:: 📄
exclude-from-graph-view:: true
tags:: #tool

- ## Using
  query-table:: true
  query-properties:: [:page :icon :created :document :status :tags :type :wikipedia]
  {{query (and (property :type "tool") (property :status "tool/star"))}}
- ## Deprecated
  query-table:: true
  query-properties:: [:page :icon :created :document :exclude-from-graph-view :status :tags :type :also]
  collapsed:: true
  {{query (and (property :type "tool") (property :status "tool/deprecated"))}}
- ## Others
  - 隔音耳塞
    logseq.order-list-type:: number
  - LED 灯
    logseq.order-list-type:: number
  - 海露滴眼液（干眼）
    logseq.order-list-type:: number
  - 扶他林双氯芬酸二乙胺乳胶剂
    logseq.order-list-type:: number
-