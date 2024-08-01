icon:: 📂
also:: 
created:: [[20240801]]
description:: 
tags:: 
type:: project

- ## Project Meta
  - DOING #project [[making-game]]
    :LOGBOOK:
    CLOCK: [2024-07-21 Sun 22:36:48]
    :END:
  - query-table:: false
    #+BEGIN_QUERY
    {:title [:h3 "Tasks related to making-game"]
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
    #+BEGIN_QUERY
    {:title [:h3 "Checklist"]
    :query (and (todo todo) (page [[making-game]]))
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