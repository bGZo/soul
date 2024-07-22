alias:: project/gaming management app, gma
description:: 类似 Steam 社区那样，直接可以获得游戏相关新闻、攻略，wiki 跳转的应用，Android Pad & Windows care
icon:: 📂
tags:: #project
created:: 20240721
deadline:: 20240821
title:: gaming management app

- ## Project Meta
  collapsed:: true
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
  collapsed:: true
  -
- ## How
  collapsed:: true
  -
- ## What
  collapsed:: true
  - ### \# Program Description
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