alias:: 开支
created:: [[20230529]]
- {{query (property cost)}}
  query-table:: true
  query-properties:: [:title :cost]
  query-sort-by:: cost
  query-sort-desc:: false
  - Cost in USD [[monthly]]: {{function (sum :cost)}}
-