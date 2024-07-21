alias:: 
created:: 20240721
description::
icon:: 📂
tags::

- ## Project Meta
  - DOING #project [[project/leetcode]]
    :LOGBOOK:
    CLOCK: [2024-07-21 Sun 22:36:48]
    :END:
  - query-table:: false
    collapsed:: true
    #+BEGIN_QUERY
    {:title [:h3 "Tasks related to project/leetcode"]
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
    :query (and (todo todo) (page [[project/leetcode]]))
    :result-transform (fn [result]
                        (sort-by (fn [b]
                                   (get b :block/priority "Z")) result))
    :breadcrumb-show? false
    :table-view? false
    }
    #+END_QUERY
- ## Why
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
    -
  - ### \# Notes
    -
- ## ↩ Reference
  -
-