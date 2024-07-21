tags:: #github #logseq #tutorial
source:: [mschmidtkorth/logseq-msk-docs: Unofficial Logseq documentation.](https://github.com/mschmidtkorth/logseq-msk-docs) ![](https://img.shields.io/github/stars/mschmidtkorth/logseq-msk-docs)
created:: 20221218

- [Queries/Advanced Queries/Tutorial](https://mschmidtkorth.github.io/logseq-msk-docs/#/page/queries%2Fadvanced%20queries%2Ftutorial)
  - `{{query [[MyTag]]}}`
    - ```clojure
      #+BEGIN_QUERY
      {:title "Find tag: MyTag"
      :query [:find (pull ?b [*])
                  :where
                    [?b :block/ref-pages ?p]
                    [?p :block/name "MyTag"]
      	       ]
      }
      #+END_QUERY
      ```
      - \#1 and \#9 indicate the start and end of a code block. Add them with <q, and select query (fun fact: this comes from [[Emacs]] [[org-mode]])
      - \#5 block/ref-pages is the **reference where tags are stored** - that's what we are looking for!
      - **#6**  `block/name`  is not the name of the *page*, but of **the reference from the previous line #5**. We store the name of the tags in  `?p`  (again this could be anything, you can rename it to  `?tagIamLookingFor` )
    -