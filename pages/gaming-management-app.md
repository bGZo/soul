also:: gma
description:: 游戏后花园
icon:: 📂
created:: [[20240721]]
deadline:: 20240821
tags:: #game #android 
type:: product

- ## Project Meta
  - \DOING #project [[page]]
  - query-table:: false
    collapsed:: true
    #+BEGIN_QUERY
    {:title [:h3 "Tasks related to project/gma"]
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
    :query (and (todo todo) (page [[project/gma]]))
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
  -
  - ### \# Program Description
    - 类似 Steam 社区那样，直接可以获得游戏相关新闻、攻略，wiki 跳转的应用，Android Pad & Windows care
    - #### Input
      -
    - #### Output
      -
  - ### \# Alternatives
    -
  - ### \# Notes
    -
- ## Reference
  collapsed:: true
  -
-