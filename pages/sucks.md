filters:: {}
icon:: 🤮
also:: black list, block, shame, 黑名单, 拉黑

  - template:: sucks
    template-including-parent:: false
    collapsed:: true
    - icon:: 🤮
      also:: ``c.page.name``作的恶
      created:: ``ref(date.now.format('YYYYMMDD'))``
      status:: ``'writing/draft'``
      type:: ``'sucks'``
    -
    - ## ↩ Reference
      -
- ## Those suck
  query-table:: true
  query-properties:: [:page :created :also :tags]
  collapsed:: true
  {{query (property :type "sucks")}}