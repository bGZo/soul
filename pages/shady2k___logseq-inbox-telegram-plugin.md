icon:: 📦
created::  [[20221120]]
description:: 
exclude-from-graph-view:: true
tags:: #[[logseq]]
type:: github/repo
source:: {{gh shady2k/logseq-inbox-telegram-plugin}}

- ~~Enable journals cause https://github.com/shady2k/logseq-inbox-telegram-plugin.~~
  collapsed:: true
  #telegram #deprecated
  - I think the journals more like tasks with #[[getting-things-done]]
- Sub block will gone #issue
  - Test case:
    collapsed:: true
    - ```
      Test
        * sub test
          * sub test
      Here show something
      Test
        + sub test
          + sub test
      Here show something
      - Test
        - sub test
          - sub test
      Here show something
      ```
      Get:
  - Solution:
    collapsed:: true
    - Regex. Turn `(^[ ]*)-` to `$1\-`/`$1+`/`$1*`
    - Looking in logseq how to write original format.
-
-