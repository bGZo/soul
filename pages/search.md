icon:: 📄
created:: [[20240730]]
description::
exclude-from-graph-view:: true

- ## Why
  -
- ## How
  -
- ## What
  - [[baidu]]
    collapsed:: true
    - 搜索参数 `tn` via: [如何追寻百度搜索结果url中的参数tn？ - 知乎](https://www.zhihu.com/question/20642243/answer/56522791)
      collapsed:: true
      - tn
        - 提交搜索请求的来源站点
        - 一个有用的tn：tn=baidulocal 表示百度站内搜索，返回的结果是很干净的，没有任何广告
        - 另外，从做百度联盟搜索的网站 A 搜索过来的都有这个tn参数，当你点击搜索结果中带“推广”的网站B，做百度“推广”的网站B的户主账户中就会被扣掉一部分费用，其中一部分百度留着，另外一小部分给网站A的户主，因为你从网站A搜索过来的
      - wd--查询的关键词
      - pn--已显示的结果条数，即当前页从pn条记录开始显示，该值为10的倍数
      - cl--搜索类型，cl=3为网页搜索 cl=2为图片搜索或新闻搜索，cl=0是所有结果，其他值未知。当搜索结果中出现“提示：为了提供最相关的结果，我们省略了一些内容相似的条目，点击这里可以看到所有搜索结果。”，点击之后的cl的值为0，而此时显示的结果相对比较多。
      - rn--搜索结果中每页显示的条数，取值范围在10、20、50、100，缺省设置rn=10
      - ie--查询输入文字的编码，缺省设置ie=gb2312，即为简体中文
      - lm--限定要搜索的网页的时间，值为0、1、7、30、360，以天为单位，例如搜索最近一个月的网页，lm=30。默认值为0，表示没有时间限制。
      - ct--语言，0-所有语言，1-简体中文网页，2-繁体中文网页；默认值为0。
      - bs--上一次搜索的关键词，应该与相关搜索有关。
      - ft--搜索的文档格式，pdf、doc、xls、ppt、rtf等，默认值为空。
      - q1--包含以下的全部的关键词
      - q2--包含以下的完整关键词
      - q3--包含以下任意一个关键词
      - q4--不包括以下关键词
      - q5--关键词位置，为空表示网页的任何地方，1表示仅网页标题中，2表示仅网页URL网址中。
      - q6--限定在某个指定的网站，比如q6=http://www.baidu.com/ 表示仅在http://www.baidu.com/ 中搜索
  - web enginee
    collapsed:: true
    - ```shell
      # Google
      https://www.google.com/search?q＝%s
      # Baidu
      https://www.baidu.com/s?wd=%s
      # Yahoo
      https://search.yahoo.com/search?p=%s
      # Bing
      https://www.bing.com/search?q=%s
      https://cn.bing.com/search?g＝%s
      # SeekWeb
      https://hk.seekweb.com/search?q=%s
      # 360 search
      https://www.so.com/s?q=%s
      # Bilibili
      https://search.bilibili.com/all?keyword=%s
      # Douban
      https://www.douban.com/search?q=%s
      # Zhihu
      https://www.zhihu.com/search?q=%s
      # Souhu
      https://www.sogou.com/web?query＝%s
      # Amazon
      https://www.amazon.cn/s?k=%s&__mk_zh_CN=亚马逊网站&ref=nb_sb_noss
      # Github (Login Required)
      https://github.com/search?q=%s
      # Stack Overflow
      https://stackoverflow.com/search?q=%s
      # Yuque (Login Required)
      https://www.yuque.com/search?type=content&scope=%2F&tab=related&p=1&sence=modal&q=%s
      # Google translation
      https://translate.google.com/?sl=auto&tl=zh-CN&op=translate&text=%s
      # Deepl translation
      https://www.deepl.com/zh/translator#en/zh/%s
      #Wikipedia
      https://zh.wikipedia.org/zh-cn/index.php?title=Special:搜索&search=%s
      # Baidu Baike
      https://baike.baidu.com/search?&word=%s
      # MAB Wiki
      https://wiki.mbalib.com/w/index.php?title=Special:Search&search=%s
      # 网易公开课
      https://open.163.com/newview/search/%s?type=all
      # cnblog
      https://zzk.cnblogs.com/s/blogpost?w=%s
      #Emoji
      https://emojipedia.org/search/?q=%s
      #Mobie
      https://quark.sm.cn/s?q=%s
      https://yz.m.sm.cn/s?q=%s
      https://m.toutiao.com/result?q=%s
      	# Not Supported
      	# v2ex.com
      	https://www.google.com/search?q=site:v2ex.com+%s
      ```
      - https://www.dogedoge.com/results?q=%s
- ## Namespace
  - {{namespace search}}
- ## ↩ Reference
  -
-
-