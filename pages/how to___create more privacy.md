tags:: #Privacy
- #+BEGIN_NOTE
  The composition of this article was assisted by ChatGPT.
  #+END_NOTE
- ---
- collapsed:: true
  #+BEGIN_TIP
  **TL;DR**: Replace the default Search Engine in [[Microsoft Edge]] as followed:
  `https://google.com/search?q=%s&ie=UTF-8`
  #+END_TIP
  - When you type some in default, such as `test`, then they will default jump to the url as followed like this:
    - ```
      https://www.google.com/search?q=test&oq=test&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTINCAEQABiDARixAxiABDINCAIQABiDARixAxiABDINCAMQABiDARixAxiABDINCAQQABiDARixAxiABDIGCAUQRRg8MgYIBhBFGDwyBggHEEUYQTIGCAgQRRhB0gEIMTA4OGowajGoAgCwAgA&sourceid=chrome&ie=UTF-8
      ```
    - The meaning of those params could be found on [Stack Exchange](https://webapps.stackexchange.com/questions/116105/what-are-the-different-parameters-used-in-google-search). The `gs_lcrp` could be found on [Git at Google](https://chromium.googlesource.com/chromium/src.git/+/e2ad407421b119f069f44fa4d8f9a01ee2d3ee73), which meaning is `Google Search Link Click Rank Position`. ==That's used to record which link users click on the search result page and transmits the link's ranking position to Google when users click on it, allowing Google to track user behavior and the effectiveness of search results==.
  - #+BEGIN_CAUTION
    The most funny thing is the `sourceid` is set to `chrome` )
    #+END_CAUTION
- ---
-
-