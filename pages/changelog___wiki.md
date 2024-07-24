also:: logseq/changelog
description:: start begin Beta 0.6.5; [Changelog](https://docs.logseq.com/#/page/changelog); [docs/Changelog.md](https://github.com/logseq/docs/blob/master/pages/Changelog.md?plain=1)

- Apr 26st, 2023  Beta 0.9.4
  collapsed:: true
  - Add `:remove-block-children?` query option for advanced queries [#9229](https://github.com/logseq/logseq/pull/9229)
- Apr 19st, 2023  Beta 0.9.3
  collapsed:: true
  - Advanced queries have a new :group-by-page? option [#9133](https://github.com/logseq/logseq/pull/9133)
- Apr 13st, 2023  Beta 0.9.2
  collapsed:: true
  - Support exporting to image  [#9037](https://github.com/logseq/logseq/pull/9037)
  - Make publishing accessible to CLIs [#9033](https://github.com/logseq/logseq/pull/9033)
- Mar 29st, 2023  Beta 0.9.1
- Mar 28st, 2023 Beta 0.9.0
  collapsed:: true
  - Refactored file system handling to fix filename issues on mobile platforms, requiring re-indexing of your working graph [#8792](https://github.com/logseq/logseq/pull/8792)
  - Added a simple [Query Builder](https://docs.logseq.com/#/page/Query%20Builder) [#8774](https://github.com/logseq/logseq/pull/8774)
  - Made [Whiteboards](https://docs.logseq.com/#/page/whiteboard) publicly available to all users [#8853](https://github.com/logseq/logseq/pull/8853)
  - Whiteboards
    - Paste and dnd behavior (also add a placeholder to shape labels) [#8753](https://github.com/logseq/logseq/pull/8753)
    - Publishing [#8899](https://github.com/logseq/logseq/pull/8899)
    - Refine UX [#8797](https://github.com/logseq/logseq/pull/8797)
  - Several copy-as/export enhancements [#8814](https://github.com/logseq/logseq/pull/8814)
  - Add better error messages for duplicate key in `config.edn` [#8488](https://github.com/logseq/logseq/pull/8488)
  - Add config option to handle default block refs expanding behavior [#8839](https://github.com/logseq/logseq/pull/8839). A new setting item `:ui/auto-expand-block-refs?` is added.
- Mar 1st, 2023 Beta 0.8.18
  collapsed:: true
  - Support cues for Cloze cards [#8654](https://github.com/logseq/logseq/pull/8654) [Documentation](https://docs.logseq.com/#/page/cloze)
  - Add support for [block refs](https://docs.logseq.com/#/page/block%20reference) in properties to backlink to blocks [#8695](https://github.com/logseq/logseq/pull/8695)
  - Add command for copying a page url [#8538](https://github.com/logseq/logseq/pull/8538)
  - Shortcuts can be disabled with `false` now  [#8618](https://github.com/logseq/logseq/pull/8618)
  - PDF viewer enhancements [#8616](https://github.com/logseq/logseq/pull/8616)
  - [Local HTTP Server](https://docs.logseq.com/#/page/local%20http%20server) now supports CORS for use from another web page or browser extension [#8651](https://github.com/logseq/logseq/pull/8651)
- Feb 10th, 2023 Beta 0.8.17
  collapsed:: true
  - Adds support for `:query-page` as an input [#8449](https://github.com/logseq/logseq/pull/8449) - [Documentation](https://docs.logseq.com/#/page/advanced%20queries/block/query%20inputs)
  - Support dragging the PDF viewer head to move the window [#8305](https://github.com/logseq/logseq/pull/8305)
  - Add `{date}` template variable to quick-capture [#8560](https://github.com/logseq/logseq/pull/8560)
  - Add `:default-page` to `quick-capture-options` [#8529](https://github.com/logseq/logseq/pull/8529)
  - Add +/- syntax, (w)eek (m)onth (y)ear, and time support to query :inputs [#8387](https://github.com/logseq/logseq/pull/8387) - [Documentation](https://docs.logseq.com/#/page/advanced%20queries/block/query%20inputs)
- Jan 12th, 2023 Beta 0.8.16
  collapsed:: true
  - PDF highlight drag & drop [#8103](https://github.com/logseq/logseq/pull/8103)
  - New query inputs for advanced query [#5674](https://github.com/logseq/logseq/pull/5674) [Document: Query Inputs](https://docs.logseq.com/#/page/advanced%20queries/block/query%20inputs)
  - Add a new option `:ui/show-full-blocks?` to show full blocks in references [#8124](https://github.com/logseq/logseq/pull/8124)
- Dec 29th, 2022 Beta 0.8.15
  collapsed:: true
  - Use shortcut  `mod+a`  to select parent blocks up to the whole page [#7803](https://github.com/logseq/logseq/pull/7803)
  - Local Http server for API invoke [#7699](https://github.com/logseq/logseq/pull/7699)
- Dec 19th, 2022 Beta 0.8.13
  collapsed:: true
  - Logseq Whiteboards now become a Beta Feature
  - Introduce a new config property  `:logseq.query/nlp-date` . Default to  `false` . Query without  `logseq.query/nlp-date:: true`  would disable date normalization [#7708](https://github.com/logseq/logseq/pull/7708)
- Dec 2nd, 2022 Beta 0.8.12
  collapsed:: true
  - Add  `page`  and  `append`  parameters to quickCapture URL, add corresponding config in  `config.edn`  [Documentation: Logseq Protocol](https://docs.logseq.com/#/page/Logseq%20Protocol)
- Nov 16th, 2022 Beta 0.8.11
  collapsed:: true
  - [On-disk encryption is removed](https://discuss.logseq.com/t/deprecation-of-on-disk-encryption/12334) [#7221](https://github.com/logseq/logseq/pull/7221). You should follow the instructions to decrypt your graph files.
  - `logseq/pages-metadata.edn`  is deprecated. Now it can be safely deleted.
- Nov 1st, 2022 Beta 0.8.10
  collapsed:: true
  - Presentation bugs
- Oct 19th, 2022 Beta 0.8.9 **New Filename format**
  collapsed:: true
  - Breaking Changes -- **Filename format**
    collapsed:: true
    - `:legacy`  and  `:triple-lowbar`
  - **PDF enhancements**
    collapsed:: true
    - Full-text search 🎉
    - Highlights list and colored label from the toolbar
  - A new theme-based highlighting system and a lot of enhancements to colors
- Sep 13th, 2022 Beta 0.8.6
  collapsed:: true
  - Support for global config file, shared across all graphs [#6531](https://github.com/logseq/logseq/pull/6531) Global configuration
- Sep 1st, 2022 Beta 0.8.3
  collapsed:: true
  - ==Config option to allow for longer, richer property values, new config option `:rich-property-values?` [#6336](https://github.com/logseq/logseq/pull/6336)==
  - Find in page on electron, use `CMD+F` or `Ctrl+F` to search term in current page [Documentation](https://docs.logseq.com/#/page/Find%20in%20page) [#6443](https://github.com/logseq/logseq/pull/6443)
- Aug 17th, 2022 Beta 0.8.1 **New  Electron Version**
  collapsed:: true
  - **NOTE**: This release updates Electron to version 19. If you encounter any errors, Clear Cache and re-add your graphs.
- Jul 20th, 2022 Beta 0.7.7
  collapsed:: true
  - Auto-complete support for both block properties and their values [#5922](https://github.com/logseq/logseq/pull/5922)
- Jun 21st, 2022 Beta 0.7.5
  collapsed:: true
  - Add request support, toolbar button pin/unpin to plugin API [#5712](https://github.com/logseq/logseq/pull/5712)
- Jun 9th, 2022 Beta 0.7.3
  collapsed:: true
  - Support mod+e to copy block embed to current block
- May 31st, 2022 Beta 0.7.1
  collapsed:: true
  - copy & Paste with rich-text formats, Use `Cmd+shift+v` or `Ctrl+shift+v` for copying/pasting without formatting [#5471](https://github.com/logseq/logseq/pull/5471)
- May 25th, 2022 Beta 0.7.0
  collapsed:: true
  - Add `video` macro to embed various video URLs, deprecates old `youtube`, `vimeo` and `bilibili` macros [#5396](https://github.com/logseq/logseq/pull/5396)
- May 16th, 2022 Beta 0.6.9
  collapsed:: true
  - lazy-loading for journals and queries, with loading skeleton
- May 10th, 2022 Beta 0.6.8
  collapsed:: true
  - Support idiomatic shortcut `ctrl+n` for auto-complete navigation [#5202](https://github.com/logseq/logseq/pull/5202)
- Apr 29th, 2022 Beta 0.6.7
  collapsed:: true
  - Parsing progress bar [#4980](https://github.com/logseq/logseq/pull/4980)
- Apr 18th, 2022 Beta 0.6.6
  collapsed:: true
  - Open action for `logseq://` protocol, enabling cross-graph reference [#4881](https://github.com/logseq/logseq/pull/4881)
- Mar 8th, 2022 Beta 0.6.2
  collapsed:: true
  - Add custom https proxy options for settings [#4373](https://github.com/logseq/logseq/pull/4373)
    collapsed:: true
    - https://cn.logseq.com/t/topic/1847