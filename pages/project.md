icon:: 📂
alias:: para/project,项目
created:: 20230623
description:: any undertaking, carried out individually or collaboratively and possibly involving research or design, that is carefully planned to achieve a particular goal.
template:: project
template-including-parent:: false

  - alias:: 
    description::
    icon:: 📂
    tags:: #project
    created:: ``{ date.now.format('YYYYMMDD') }``
    title:: ``{ c.page.name }``
  - ## Project Meta
    collapsed:: true
    - \DOING #project [[page]]
    - query-table:: false
      collapsed:: true
      #+BEGIN_QUERY
      {:title [:h3 "Tasks related to ``{ c.page.name }``"]
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
       :query (and (todo todo) (page [[``{ c.page.name }``]]))
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
- ## Why
  -
- ## How
  -
- ## What
  -
  -
 - ## Namespace
  - {{namespace project}}
- ## ↩ Reference
  -