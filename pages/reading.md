also:: 阅读

- ## [[reading]] [[flow]] | 阅读工作流
  - If they have full content rss, it's the best.
    - I hate wordpress output recent 10 posts by default.
    - Import into [yang991178/fluent-reader](https://github.com/yang991178/fluent-reader).
    - Found interesting content;
    - Make highlights in [Raindrop.io](https://raindrop.io/)
    - Put them all in [[logseq]] page ready for refer.
  - They don't, but their url have some rules
    - like this blog, they don't even have an archived page :(
      - Generate bookmark file then import into [Raindrop.io](https://raindrop.io/) and go on above.
        - ```js
          var length = 80,
              length_len = 0,
              length_tmp = length;
          while( length_tmp >= 1 ){
              length_tmp /= 10;
              length_len++;
          }
          // get the loop number
          for(var i = 1; i<=length; i++){
              var str_num = "" + i;
              while(str_num.length < length_len){
                  str_num = "0" + str_num;
              }
              console.log('<DT><A HREF="https://blog.yitianshijie.net/page/' + i + '/">Bookmark '+ str_num +'</A>');
          }
          ```
          - ```js
            var length = 80,
                length_len = 0,
                length_tmp = length;
            while( length_tmp > 0 ){
                length_tmp /= 10;
                console.log(length_tmp);
                length_len++;
            }
            console.log(length_len);
            ```
            #this-code/weird
            - ```
              8
              0.8
              0.08
              0.008
              0.0008
              0.00008
              0.000008000000000000001
              8.000000000000002e-7
              8.000000000000001e-8
              8.000000000000002e-9
              8.000000000000002e-10
              ...
              326
              ```
        - The template for bookmark is following:
          inspired via: [browser - Documentation or reference for "NETSCAPE-Bookmark-file-1" DOCTYPE - Stack Overflow](https://stackoverflow.com/questions/72772176/)
        - ```html
          <!DOCTYPE NETSCAPE-Bookmark-file-1>
          	<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
              <!--This is an automatically generated file.
              It will be read and overwritten.
              Do Not Edit! -->
              <Title>Bookmarks</Title>
              <H1>Bookmarks</H1>
              <DL><p>
                <DT><H3 FOLDED PERSONAL_TOOLBAR_FOLDER="true">Bookmarks</H3>
                <DL><p>
                  <DT><A HREF="https://blog.yitianshijie.net/page/1/">Bookmark 1</A>
                  <DT><A HREF="https://blog.yitianshijie.net/page/2/">Bookmark 2</A>
                  <!-- ...... -->
                </DL><p>
              </DL><p>
          ```
          #template/bookmark
        - Full standard via: [Netscape Bookmark File Format (Internet Explorer) | Microsoft Learn](https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa753582(v=vs.85))
        -
      - But when blogger update and the highlight would be deprecate.