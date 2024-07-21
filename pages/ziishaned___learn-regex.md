author:: ziishaned
description:: Learn regex the easy way
tags:: #regex, #github
source::  [ziishaned/learn-regex: Learn regex the easy way](https://github.com/ziishaned/learn-regex) ![](https://img.shields.io/github/stars/ziishaned/learn-regex)
created:: 2021
closed:: [[2021]]

- Meta
  - Shorth and Character Sets / Single Char
    - ```bash
      . # Any character except new line
      \w # Matches alphanumeric characters: [a-zA-Z0-9_]
      \W # Matches non-alphanumeric characters: [^\w]
      \d # Matches digits: [0-9]
      \D # Matches non-digits: [^\d]
      \s # Matches whitespace characters: [\t\n\f\r\p{Z}]
      \S # Matches non-whitespace characters: [^\s]
      \f # Match a form feed
      \n # Match a newline character
      \r # Matches a carriage return
      \t # Matches a tab
      \v # Matches a vertical tab
      \p # Match CR/LF (equivalent to \r\n), used to match DOS line terminator
      ```
  - Quantifiers(数量)
    - ```shell
      * # expression >=0,
      .* # anything
      + # expression >=1
      a*  -> a{0,}  -> Match a or aa or aaaaa or an empty string
      a+  -> a{1,}  -> Match a or aa or aaaa but not a string empty
      # from:https://stackoverflow.com/questions/10763820/difference-between-and-regex
      ? # none greedy
      colou?rs? # colors colours colour
      {min, max} # range of quantifiers
      {n} # quantifiers is n
      ```
  - Position(位置)
    - ```shell
      ^ # start of line, in [^n] means anything except n
      $ # end of line
      \b #word bounds
      \b\w{5}\b # words included five char
      ```
  - Char Class
    - ```shell
      [] # classifier
      [-.] # char - or char . which means any character outside, like \. outside. cause in [] character don't need escaped.
      l[yi (]nk # lynk  link  l nk   l(nk
      (a|b) # a or b
      ```
  - Capturing Groups
    - ```shell
      () # groups and backreferences
      \([0-9]\) #[a-zA-Z] / [A-Z] / [a-z] / [0123456789]
      what diff with \ & $ ????
      ```
- Lookarounds
  collapsed:: true
  - ```shell
    ?= # Positive Lookahead
    "(T|t)he(?=\sfat)" => The fat cat sat on the mat.
    ?! # Negative Lookahead
    "(T|t)he(?!\sfat)" => The fat cat sat on the mat.
    ?<= # Positive Lookbehind
    "(?<=(T|t)he\s)(fat|mat)" => The fat cat sat on the mat.
    ?<! # Negative Lookbehind
    "(?<!(T|t)he\s)(cat)" => The cat sat on cat.
    ```
- Flags
  collapsed:: true
  - ```shell
    g # global, Don't return after first match
    m # multi line, ^and $ match startiend of line
    i # insensitive, case insensitive match
    x # extended, Ignore whitespace
    X # eXtra, Disallow meaningless escapes.
    s # single line, Dot matches newline
    u # unicode, Match with full unicode
    U # Ungreedy, Make quantifiers lazy
    A # Anchored, Anchor to start of pattern or at the end of the most recent match
    J # Jchanged, Allow duplicate subpattern names
    D # Dollar end only, $ matches only end of pattern
    ```