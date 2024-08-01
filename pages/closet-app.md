description:: 衣橱管理APP
icon:: 📂
created:: [[20240721]]
title:: closet-app
type:: product

- ## Project Meta
  - \DOING #project [[page]]
  - query-table:: false
    collapsed:: true
    #+BEGIN_QUERY
    {:title [:h3 "Tasks related to project/closet app"]
    :query [:find (pull ?b [*])
       :in $ ?current-page
       :where
       [?p :block/name ?current-page]
       [?b :block/marker ?marker]
    [?p :block/alias ?al]
    (or [?b :block/refs ?p] [?b :block/refs ?al])
    (or
       [(= "NOW" ?marker)]
       [(= "DOING" ?marker)]
       [(= "WAITING" ?marker)]
       [(= "LATER" ?marker)]
    )
    (not [?b :block/page ?p])
    ]
    :inputs [:current-page]
    :result-transform (fn [result]
                        (sort-by (fn [b]
                                   (get b :block/priority "Z")) result))
    :breadcrumb-show? false
    :table-view? false
    }
    #+END_QUERY
  - query-table:: false
    collapsed:: true
    #+BEGIN_QUERY
    {:title [:h3 "Checklist"]
    :query (and (todo todo) (page [[project/closet app]]))
    :result-transform (fn [result]
                        (sort-by (fn [b]
                                   (get b :block/priority "Z")) result))
    :breadcrumb-show? false
    :table-view? false
    }
    #+END_QUERY
- ## Why
  collapsed:: true
  -
- ## How
  -
- ## What
  - ### \# Program Description
    - #### Input
      -
    - #### Output
      -
  - ### \# Alternatives
    - Logseq => 可以做成 Block，然后通过查询形成表格
  - ### \# Notes
    -
- ## Reference
  collapsed:: true
  -
-