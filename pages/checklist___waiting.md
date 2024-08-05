also:: 可能清单
icon:: 🤔
tags:: gtd

- {{query (task waiting)}}
  query-table:: true
  query-properties:: [:page :block]
  query-sort-by:: page
  query-sort-desc:: true
- collapsed:: true
  ---
  - Another way to query
    collapsed:: true
    - ```
      [:h2 {:class text-right} "Waiting List"]
      #+BEGIN_QUERY
      {:query [:find (pull ?b [*])
              :in $ ?start ?today
              :where
              (task ?b #{"LATER" "WAIT" "WAITING"})
              (between ?b ?start ?today)]
      :inputs [:-3650d :today]
      :collapsed? true
      :table-view? true
      :breadcrumb-show? false
      }]}
      #+END_QUERY
      ```