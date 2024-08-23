icon:: 📦
created:: [[20240727]]
exclude-from-graph-view:: true

  - template:: github
    template-including-parent:: true
    icon:: 📦
    created:: ``ref(date.now.format('YYYYMMDD'))``
    description:: 
    exclude-from-graph-view:: true
    tags:: 
    type:: ``'github/repo'``
    source::  ``'{{gh ' + c.page.name + '}}'``
- ## Why
- ## How
- ## What
- ## Namespace
  - {{query (property :type "github/repo")}}
    query-table:: true
    query-properties:: [:page :tags :description :created :source]
    query-sort-by:: page
    query-sort-desc:: false
- ## ↩ Reference
  - [[mirror]] [[navigation]]
    - {{nav https://hub.xn--p8jhe.tw}}
      logseq.order-list-type:: number
    - {{nav https://hub.xn--gzu630h.xn--kpry57d}}
      logseq.order-list-type:: number
    - {{nav https://hub.fastgit.xyz}}
      logseq.order-list-type:: number
    - {{nav https://cdn.githubjs.cf}}
      logseq.order-list-type:: number
    - {{nav https://gitclone.com}}
      logseq.order-list-type:: number
    - {{nav https://hub.gitfast.tk}}
      logseq.order-list-type:: number
    - {{nav https://hub.gitslow.tk}}
      logseq.order-list-type:: number
    - {{nav https://hub.verge.tk}}
      logseq.order-list-type:: number
    - {{nav https://raw.gitfast.tk}}
      logseq.order-list-type:: number
    - {{nav https://raw.gitslow.tk}}
      logseq.order-list-type:: number
    - {{nav https://raw.verge.tk}}
      logseq.order-list-type:: number
  - Fork somebody repo cannot change to private?
    - [What security issue is caused by changing the visibility of a fork on Github? - Stack Overflow](https://stackoverflow.com/questions/71446341/what-security-issue-is-caused-by-changing-the-visibility-of-a-fork-on-github)
    - [Dependency versions | GitHub Pages](https://pages.github.com/versions/)
    - [Features • GitHub Actions](https://github.com/features/actions)