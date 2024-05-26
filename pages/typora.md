alias:: tool/typora
- Shortcuts
  collapsed:: true
  - |     Operation      |              Effections              |
    | :----------------: | :----------------------------------: |
    |       Ctrl+/       |         代码和预览的快速切换         |
    |   shift + enter    |                软换行                |
    |       enter        |                硬换段                |
    |      Ctrl + /      |            调出源代码格式            |
    |      Ctrl + K      |     将选中词变为剪切板的网页索引     |
    | Ctrl + Shief + 1/2 | 关闭/隐藏侧边任务栏（源码模式无效）  |
    | Ctrl + Shief + 1/2 | 大纲和文件的互相切换（源码模式无效） |
    |         F8         |               专注模式               |
    |         F9         |               翻译模式               |
    |        F11         |               全屏模式               |
- Themes via: [xiaolai/markdownhere.css](https://gist.github.com/xiaolai/aa190255b7dde302d10208ae247fc9f2)
  collapsed:: true
  - ```css
    /*
    References:
      1. https://gist.github.com/xiaolai/aa190255b7dde302d10208ae247fc9f2
      2. https://support.typora.io/Backgound/
      3. https://ethanschoonover.com/solarized/ from https://www.v2ex.com/t/703380
    */
    .markdown-here-wrapper {
        font-size: 16px;
        line-height: 1.8em;
        letter-spacing: 0.1em;
      }
    content, body{ /*body change top bar*/
      background-color: #fdf6e3;/*#pink: f9f5f5*/
    }
    pre, code {
      font-size: 14px;
      font-family: Roboto, 'Courier New', Consolas, Inconsolata, Courier, monospace;
      margin: auto 5px;
    }
    code {
      white-space: pre-wrap;
      border-radius: 2px;
      display: inline;
    }
    pre {
      font-size: 15px;
      line-height: 1.4em;
      display: block; !important;
    }
    pre code {
      white-space: pre;
      overflow: auto;
      border-radius: 3px;
      padding: 1px 1px;
      display: block !important;
    }
    strong, b{
      color: #BF360C;
    }
    em, i {
      color: #009688;
    }
    hr {
      border: 1px solid #BF360C;
      margin: 1.5em auto;
    }
    p {
      margin: 1.5em 5px !important;
    }
    table, pre, dl, blockquote, q, ul, ol {
      margin: 10px 5px;
    }
    ul, ol {
      padding-left: 15px;
    }
    li {
      margin: 10px;
    }
    li p {
      margin: 10px 0 !important;
    }
    ul ul, ul ol, ol ul, ol ol {
      margin: 0;
      padding-left: 10px;
    }
    ul {
      list-style-type: circle;
    }
    dl {
      padding: 0;
    }
    dl dt {
      font-size: 1em;
      font-weight: bold;
      font-style: italic;
    }
    dl dd {
      margin: 0 0 10px;
      padding: 0 10px;
    }
    blockquote, q {
      border-left: 2px solid #009688;
      padding: 0 10px;
      color: #777;
      quotes: none;
      margin-left: 1em;
    }
    blockquote::before, blockquote::after, q::before, q::after {
      content: none;
    }
    h1, h2, h3, h4, h5, h6 {
      margin: 20px 0 10px;
      padding: 0;
      font-style: bold !important;
      color: #009688 !important;
      text-align: center !important;
      margin: 1.5em 5px !important;
      padding: 0.5em 1em !important;
    }
    h1 {
      font-size: 24px !important;
      border-bottom: 1px solid #ddd !important;
    }
    h2 {
      font-size: 20px !important;
      border-bottom: 1px solid #eee !important;
    }
    h3 {
      font-size: 18px;
    }
    h4 {
      font-size: 16px;
    }
    table {
      padding: 0;
      border-collapse: collapse;
      border-spacing: 0;
      font-size: 1em;
      font: inherit;
      border: 0;
      margin: 0 auto;
    }
    tbody {
      margin: 0;
      padding: 0;
      border: 0;
    }
    table tr {
      border: 0;
      border-top: 1px solid #CCC;
      background-color: white;
      margin: 0;
      padding: 0;
    }
    table tr:nth-child(2n) {
      background-color: #F8F8F8;
    }
    table tr th, table tr td {
      font-size: 16px;
      border: 1px solid #CCC;
      margin: 0;
      padding: 5px 10px;
    }
    table tr th {
      font-weight: bold;
      color: #eee;
      border: 1px solid #009688;
      background-color: #009688;
    }
    ```