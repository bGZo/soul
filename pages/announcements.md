also:: [[logseq/!announcements]]
created:: [[20240722]]
description:: 弱规则不是规则，仅仅只是一种建议
icon:: 📢
wikipedia:: https://en.wikipedia.org/wiki/Soft_law
title:: announcements

- #+BEGIN_PINNED
  **Keep maintaining those rules**. The half life of tool tutorials is really short, those soft rules following could be outdated soon as possible, especially in the active community. [^maintain-soft-rules]
  [[20230107]] 
  #+END_PINNED
- #+BEGIN_TIP
  Logseq is just a graph-driven note app[^toc-is-hard-thing], which means linearity support is  downside during several alternatives.
  [[20240722]] 
  #+END_TIP
- #+BEGIN_TIP
  **`#[[]]` instead of `#`**. They would be popped menu friendly, while editing again.
  [[20240722]] 
  #+END_TIP
- #+BEGIN_TIP
  Sort properties with dictionary order, `cover` property not included.
  [[20240722]] 
  #+END_TIP
- collapsed:: true
  #+BEGIN_TIP
  **Every main page should have a template**, which just put them on page properties is fine. And then, **all template should extend `page`**, then only add less properties as much as possible. 
  [[20230107]] 
  #+END_TIP
  - the `page` properties should be hided on graph by default.
- collapsed:: true
  #+BEGIN_TIP
  **Paste image from clipboard is pained**. Each type of images would be converted to `png`, increasing file size. especially on picgo, they would lost the transparent.
  [[20230107]] 
  #+END_TIP
  - The former has been fixed high then 0.8.6, you still could via https://discuss.logseq.com/t/pasting-photos-increases-the-size-of-the-image-file-massively/9363 see what happened. But the latter is still existed.
  - Is construction of assets matters?
    - In some case, keep 2 depth is the best.
- collapsed:: true
  #+BEGIN_WARNING
  I'd encourage you to delay your use of namespaces until you have refined your understanding of how they might suit your workflows.  
  https://www.logseqmastery.com/blog/logseq-namespaces  
  https://discuss.logseq.com/t/outline-overview-for-sidebar/740/19
  #logseq/namespace 
  #+END_WARNING
  - collapsed:: true
    #+BEGIN_TIP
    **Use plural of noun while placing something under namespace**, like book, using `books/xxx`instead of `book/xxx`, which could give you a chance to sepreate from each other. 
    [[20240722]] 
    #+END_TIP
    - I believe when I want to talk book, I would type `book`, then when I want to someone between them, I would type `books`.
  - collapsed:: true
    #+BEGIN_TIP
    All name under namespace should use alias to be redirected. 
    [[20240722]] 
    #+END_TIP
    - Firstly, the pay of renaming on git is high, which means the history of this files would be lost at all. Then secondly, without alternatives now is, the working of alias on logseq, should not appear on graph, because so much more properties, or connect, is so mess without ability to hide. [^alias-should-more-power]
- collapsed:: true
  #+BEGIN_WARNING
  If you consider performance of logseq, see those advices
  #+END_WARNING
  - collapsed:: true
    #+BEGIN_TIP
    Control the usage of plugin
    #+END_TIP
    - The memory using by logseq is huge by opening plugin, and some plugin I really need them, like [list / 🖍 logseq](https://github.com/stars/bGZo/lists/logseq)
    - I have not tool in [[electron]] debug, like task manager similar to [[chrome]]
    - But I notice the raindrop is really huge in them, and it's dynamic number, different with normal and using.
      collapsed:: true
      - ![Taskmgr_UJ8XZ7IQSf.png](../assets/2023/Taskmgr_UJ8XZ7IQSf_1673183725863_0.png)
        ![Taskmgr_lhEj4ujOSz.png](../assets/2023/Taskmgr_lhEj4ujOSz_1673183732509_0.png)
  - collapsed:: true
    #+BEGIN_TIP
    Control the usage of graph, **NOT ALL IN ONE**. Separate them to different pages.
    #+END_TIP
    - Most in [[archive]], I used to put it all in one block, but it's seem not well in export graph, the size of index is `58,872KB`, dame huge, and the page loading is `20,000`ms in local network.
    - ![chrome_wjeJBDT9Ch.png](../assets/2023/chrome_wjeJBDT9Ch_1673183842019_0.png)
      ![chrome_laTdXp2njm.png](../assets/2023/chrome_laTdXp2njm_1673183844588_0.png)
    - I cannot image put it into github page or vercel, maybe it's would be several times longer.
- ## Why
- ## How
- ## What
- ## Namespace
  - {{namespace announcements}}
- ## ↩ Reference
  - [^alias-should-more-power]: via: https://discuss.logseq.com/t/enhancement-of-aliases/14466, Towards non-native speakers in English, `alias` is a little bit interesting, more aliases makes graph more complex, which links every node duplicately. This is really funciton need to be enhanced.
  - [^toc-is-hard-thing]: via: https://discuss.logseq.com/t/outline-overview-for-sidebar/740/20, I choose use namespace instead of content side bar.
  - [^maintain-soft-rules]: Maybe the flow you have to change in next version, or the problem maybe solved, it's really not have too much value.
  - ?Don't add the `[[]]` in `page_name`
    id:: 6375b6b8-8628-4bf0-9027-668073dceec6