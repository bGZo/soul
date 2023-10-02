icon:: 💬
alias:: 话题
tags:: #writing

- ## [[random]] Roll a topic [[monthly]] 
  query-table:: true
  collapsed:: true
  #+BEGIN_QUERY
  {
  	:query [
              :find (pull ?p [*])
              :where
              (property ?p :tags "Topic")
              ]
      :collapsed? true
  }
  #+END_QUERY 
  ((63f9ae8a-e1fa-4445-82e0-49c140a21057))
-