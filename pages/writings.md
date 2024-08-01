icon:: ✍
created:: [[20240727]]
tags:: writing

- ## Ideas
  query-table:: true
  query-properties:: [:page :icon :created :status :tags]
  {{query (property :status "writing/idea")}}
- ## Outline
  collapsed:: true
  - {{query (property :status "writing/outline")}}
- ## Draft
  query-table:: true
  query-properties:: [:page :icon :created :status :tags]
  {{query (property :status "writing/draft")}}
- ## Edit
  collapsed:: true
  - {{query (property :status "writing/edit")}}
- ## Published
  query-table:: true
  query-properties:: [:page :icon :created :status :tags :also]
  {{query (property :status "writing/published")}}
- ## ↩ Reference
  -