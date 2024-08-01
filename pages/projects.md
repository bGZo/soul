icon:: 📂
created:: [[20240801]]
tags:: project

- ## Project
  query-sort-by:: type
  query-sort-desc:: true
  {{query (or (page-property :type project) (page-property :type "product"))}}
- ## Project
  {{query (or (page-property :type project/done) (page-property :type "product/done"))}}
-