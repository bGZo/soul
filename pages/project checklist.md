alias:: 项目清单
icon:: 📂
tags:: #gtd, #project

- #+BEGIN_QUERY
  {:title [:h3 "Tasks related to project"]
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
   :inputs ["project"]
  :result-transform (fn [result]
                      (sort-by (fn [b]
                                 (get b :block/priority "Z")) result))
  :breadcrumb-show? false
  :table-view? false
  }
  #+END_QUERY
-