icon:: 📂
also:: 
created:: [[20240823]]
description:: 
tags:: 
type:: project

- ## Project Meta
  collapsed:: true
  :LOGBOOK:
  CLOCK: [2024-07-21 Sun 22:36:48]
  :END:
  - DOING #project [[wms稳定专项]]
  - query-table:: false
    #+BEGIN_QUERY
    {:title [:h3 "Tasks related towms稳定专项"]
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
    :query (and (todo todo) (page [[wms稳定专项]]))
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
- ## ↩ Reference
  -
- ## 维护脚本
  - 数据表：增量查询
    collapsed:: true
    - ```sql
      select count(1) from wms_sap_post_result where to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') >= current_date - INTERVAL '1 day' AND to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') < current_date;
      
      select count(1) from wms_out_requirement_head where to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') >= current_date - INTERVAL '1 day' AND to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') < current_date;
      
      select count(1) from wms_in_receipt where to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') >= current_date - INTERVAL '1 day' AND to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') < current_date;   
      
      select count(1) from wms_out_requirement_item where to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') >= current_date - INTERVAL '1 day' AND to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') < current_date;
      
      select count(1) from wms_out_return_item_d where to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') >= current_date - INTERVAL '1 day' AND to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') < current_date;
      
      
      
      select count(1) from wms_out_return_item where to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') >= current_date - INTERVAL '1 day' AND to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') < current_date;
      
      select count(1) from wms_out_return_head where to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') >= current_date - INTERVAL '1 day' AND to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') < current_date;
      
      select count(1) from wms_core_wmsdoc_item where to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') >= current_date - INTERVAL '1 day' AND to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') < current_date;
      
      select count(1) from wms_task_center where to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') >= current_date - INTERVAL '1 day' AND to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') < current_date;
      
      select count(1) from wms_core_wmsdoc_head where to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') >= current_date - INTERVAL '1 day' AND to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') < current_date;
      
      
      
      select count(1) from wms_in_delivery_pack_label where to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') >= current_date - INTERVAL '1 day' AND to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') < current_date;
      
      select count(1) from wms_in_inbound_head where to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') >= current_date - INTERVAL '1 day' AND to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') < current_date;
      
      select count(1) from wms_in_delivery_pack_item where to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') >= current_date - INTERVAL '1 day' AND to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') < current_date;
      
      select count(1) from wms_in_inbound_item where to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') >= current_date - INTERVAL '1 day' AND to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') < current_date;
      
      select count(1) from wms_in_delivery_pack where to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') >= current_date - INTERVAL '1 day' AND to_date(create_date, 'YYYY-MM-DD HH24:MI:SS') < current_date;
      ```
-