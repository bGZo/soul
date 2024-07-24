also:: [[logseq/template]]
icon:: 📄
created:: [[20230531]]
exclude-from-graph-view:: true

- ## Why
- ## How
- ## What
  - The version has changed several times after those thing imported.
    - Dynamic variable build-in, like `<% today %>`, `<% current page %>`
      logseq.order-list-type:: number
    - [[sawhney17/logseq-smartblocks]]
      logseq.order-list-type:: number
      - ```
        {{renderer :smartblock, book, +Book, true}}
        ```
    - 🌟 [[stdword/logseq13-full-house-plugin]]
      logseq.order-list-type:: number
      - add more variable to format notes.
- ## Templates
  query-table:: false
  {{query (and (property template) (sort-by created asc))}}
  - query-table:: false