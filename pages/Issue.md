alias:: 议题
mark::
icon:: ⏸
created:: 20231227
tags::
title:: Issue
- ## Why
- ## How
- ## What
- collapsed:: true
  #+BEGIN_QUERY
  {:title [:h3 "All Issues in Other Page"]
   :query [:find (pull ?b [*])
           :where
           [?b :block/name "TODO"]
  [?b :block/refs ?p]
  ]
   :collapsed? true
   :table-view? false
  }
  #+END_QUERY
- collapsed:: true
  #+BEGIN_QUERY
    {:title [:h6 "Blocks tagged #issue"]
     :query [:find (pull ?h [*])
             :in $ ?target
             :where
             [?p :block/name ?target]
             [?h :block/refs ?p]]
     :inputs ["issue"]
     :table-view? false}
   #+END_QUERY
-