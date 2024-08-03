icon:: 📄
also:: 统一资源定位符
created:: [[20240713]]
description:: 提供了互联网上资源的网络地址或位置。它通常用于指定网页、文件或服务的位置。URL 提供了一种标准化的格式来访问网络上的资源。它是网络浏览、链接和互联网通信的关键组成部分。

- ## Why
  -
- ## How
  - 一个中文域名会如何编码？为什么会出现 `xn--` 的字样？
    #encoding #chinese
    - 中文网址编码是一种将中文域名转换为英文域名的方法，它使用了一种叫做 Punycode 的算法。Punycode 是一种将 Unicode 字符串编码为 ASCII 字符串的方式，它使用了 xn-- 前缀和一些数字和字母来表示原始的 Unicode 字符串，因为 DNS 不支持 Unicode。例如，中文网址 `编码.com` 的 Punycode 编码是 `xn–fiqz59cpva341l.com`。这样做的目的是为了让不支持 Unicode 的浏览器和服务器能够识别和访问中文域名[^Punycode]
    - more via: https://github.com/mingyun/mingyun.github.io/blob/master/Characterencoding.html
    - [^Punycode]: https://stackoverflow.com/questions/9724379/xn-on-domain-what-it-means
  -
- ## What
  - URL 的构造？via: https://www.v2ex.com/t/1050461
    - URL 由几个部分组成，这些部分一起定义了资源的地址和用于访问它的协议。让我们解析下面的 URL 作为例子，一一解释每个部分的功能。
    - ```
      https://example.logto.io:8080/blogs/index.html?param1=value1&param2=value2#introduction
      ```
    - **Scheme:** 指定了用于访问资源的协议或方案，如 HTTP （超文本传输协议）、HTTPS （安全的 HTTP ）、FTP （文件传输协议）或 [其他](https://en.wikipedia.org/wiki/List_of_URI_schemes)。
      logseq.order-list-type:: number
      - 此 URL 中的 scheme 是 `https`。
        logseq.order-list-type:: number
    - **Host:** 主机指定了托管资源的服务器的域名或 IP 地址。
      logseq.order-list-type:: number
      - 此 URL 中的 host 是 [example.logto.io](http://example.logto.io)。
        logseq.order-list-type:: number
    - **Port:** （可选）端口表示在主机上访问资源的特定端口号。如果没有指定端口，它默认为给定方案的标准端口。
      logseq.order-list-type:: number
      - HTTP 的默认端口是 80 ，而 HTTPS 的默认端口是 443 。
        logseq.order-list-type:: number
      - 此 URL 中的 port 是 `8080`。
        logseq.order-list-type:: number
    - **Path:** （可选）路径指示服务器上资源所在的特定位置或目录，可以包括目录和文件名。
      logseq.order-list-type:: number
      - 此 URL 中的 path 应为 `/blogs/index.html`。
        logseq.order-list-type:: number
    - **Query parameters:** （可选）查询参数是传递给资源的额外参数，通常用于动态网络应用。它们出现在路径之后，由 `?` 符号分隔。
      logseq.order-list-type:: number
      - 此 URL 中的 query parameters 是 `params1=value1&param2=value2`，通常以键值对的形式表示，对之间由 `&` 符号分隔。在实际使用场景中，通常需要编码以避免空格等字符。
        logseq.order-list-type:: number
    - **Fragment identifier:** （可选）它也可以被称为锚，用于定位资源中的特定位置。
      logseq.order-list-type:: number
      - 此 URL 中的锚是 `#introduction`。
        logseq.order-list-type:: number
      - 此外，使用文件服务或许多网页上的 "联系我们" 按钮都链接到 URL ，例如：
        logseq.order-list-type:: number
        - [ftp://documents.logto.io/files/legal/soc_ii.pdf](ftp://documents.logto.io/files/legal/soc_ii.pdf)
          logseq.order-list-type:: number
        - [mailto:contact@logto.io?subject=Enterprise%20quota%20request](mailto:contact@logto.io?subject=Enterprise%20quota%20request)
          logseq.order-list-type:: number
-
-