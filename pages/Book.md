alias:: 书
icon:: 📖
tags:: #Hobby

created:: 20230602
title:: Book

  - template:: book
    template-including-parent:: false
    collapsed:: true
    - ---
      cover: {:width 225}
      alias: books/``{ c.page.name }``
      author: 
      translator: 
      icon: 📖
      isbn: 
      publisher: 
      published-date: 
      tags: 
      douban: 
      goodreads: 
      weread: 
      created: ``{ date.now.format('YYYYMMDD') }``
      title: ``{ c.page.name }``
      ---
    - ## [[Comment]]
      -
  - template:: book/public
    template-including-parent:: false
    collapsed:: true
    - ---
      cover: {:width 225}
      alias: books/
      author: 
      translator: 
      icon: 📖
      isbn: 
      publisher: 
      published-date: 
      tags: 
      douban: 
      goodreads: 
      weread: 
            date: ``{ date.now.format('YYYYMMDD') }``
      title: ``{ c.page.name }``
      ---
    - ## [[Comment]]
      -
- ## Why
  - collapsed:: true
    #+BEGIN_QUOTE
    三种单纯然而极其强烈的激情支配着我的一生。那就是对于爱情的渴望，对于知识的追求，以及对于人类苦难痛彻肺腑的怜悯。这些激情犹如狂风，把我伸展到绝望边缘的深深的苦海上东抛西掷，使我的生活没有定向。
    
    「我追求爱情，首先因为它叫我消魂」。爱情使人消魂的魅力使我常常乐意为了几小时这样的快乐而牺牲生活中的其他一切。
    
    我追求爱情，又因为它减轻孤独感－－那种一个颤抖的灵魂望着世界边缘之外冰冷而无生命的无底深渊时所感到的可怕的孤独。
    
    我追求爱情，还因为爱的结合使我在一种神秘的缩影中提前看到了圣者和诗人曾经想像过的天堂。这就是我所追求的，尽管人的生活似乎还不配享有它，但它毕竟是我终于找到的东西。
    
    我以同样的热情追求知识，「我想理解人类的心灵，我想了解星辰为何灿烂，我还试图弄懂毕达哥拉斯学说的力量」，是这种力量使我在无常之上高踞主宰地位。我在这方面略有成就，但不多。
    
    爱情和知识只要存在，总是向上导往天堂。但是，怜悯又总是把我带回人间。痛苦的呼喊在我心中反响回荡，孩子们受饥荒煎熬，无辜者被压迫者折磨，孤弱无助的老人在自己的儿子眼中变成可恶的累赘，以及世上触目皆是的孤独、贫困和痈苦－－这些都是对人类应该过的生活的嘲弄。我渴望能减少罪恶，可我做不到，于是我感到痛苦。
    
    这就是我的一生。我觉得这一生是值得活的，如果真有可能再给我一次机会，我将欣然再重活—次。
    #+END_QUOTE
    - #+BEGIN_QUOTE
      > What I have lived for?
      Bertrand Russell
      
      Three passions, simple but overwhelmingly strong, have governed my life: the longing for love, the search for knowledge, and unbearable pity for the suffering of mankind. These passions, like great winds, have blown me hither and thither, in a wayward course, over a great ocean of anguish, reaching to the very verge of despair.
      
      I have sought love, first, because it brings ecstasy - ecstasy so great that I would often have sacrificed all the rest of life for a few hours of this joy. I have sought it, next, because it relieves loneliness--that terrible loneliness in which one shivering consciousness looks over the rim of the world into the cold unfathomable lifeless abyss. I have sought it finally, because in the union of love I have seen, in a mystic miniature, the prefiguring vision of the heaven that saints and poets have imagined. This is what I sought, and though it might seem too good for human life, this is what--at last--I have found.
      
      With equal passion I have sought knowledge. I have wished to understand the hearts of men. I have wished to know why the stars shine. And I have tried to apprehend the Pythagorean power by which number holds sway above the flux. A little of this, but not much, I have achieved.
      
      Love and knowledge, so far as they were possible, led upward toward the heavens. But always pity brought me back to earth. Echoes of cries of pain reverberate in my heart. Children in famine, victims tortured by oppressors, helpless old people a burden to their sons, and the whole world of loneliness, poverty, and pain make a mockery of what human life should be. I long to alleviate this evil, but I cannot, and I too suffer.
      
      This has been my life. I have found it worth living, and would gladly live it again if the chance were offered me.
      #+END_QUOTE
- ## How
  - How to find / search  books?
    collapsed:: true
    - ~~[Z-Library. The world's largest ebook library.](https://z-lib.org/)~~ #R.I.P
    - [Library Genesis](http://libgen.rs/) / [Library Genesis](https://libgen.li/)
    - [Free eBooks | Project Gutenberg](https://www.gutenberg.org/)
    - [Download free eBooks for students and read business books for professionals online | Bookboon](https://bookboon.com/)
    - [Academia.edu - Share research](https://www.academia.edu/)
    - [Free Computer, Programming, Mathematics, Technical Books, Lecture Notes and Tutorials](https://freecomputerbooks.com/)
    - [Free-eBooks.net | Download free Fiction, Health, Romance and many more books](https://www.free-ebooks.net/)
  - How to [[unlock]] book DRM?
    collapsed:: true
    - [apprenticeharper/DeDRM_tools: DeDRM tools for ebooks](https://github.com/apprenticeharper/DeDRM_tools/wiki/Exactly-how-to-remove-DRM#removing-drm#removing-drm) ![](https://img.shields.io/github/stars/apprenticeharper/DeDRM_tools)
    - [FreeMyPDF.com - Removes passwords from viewable PDFs](http://freemypdf.com/)
  - How to convert [[markdown]] to pdf?
    collapsed:: true
    - [Customizing pandoc to generate beautiful pdf and epub from markdown](https://learnbyexample.github.io/customizing-pandoc/)
  - WAITING How to build reading system [[opensource]], especially without commercial way!
    collapsed:: true
    - No [[weread]] !!
    - [Moon+ Pro and Calibre Integration - MobileRead Forums](https://www.mobileread.com/forums/showthread.php?t=328164)
    - [电脑上有哪些好用的 ePub 阅读器？ - 知乎](https://www.zhihu.com/question/19979089)
    - [云书库calibre-web搭建（1） | J.F's BLOG](https://blog.zzbd.org/2020/02/29/calibre-web/)
    - [这可能是安卓端最强的电子书阅读APP（“静读天下”使用技巧）_电子书刊_什么值得买](https://post.smzdm.com/p/a3g7dzkd/)
  - WAITING How to import book using scanning? #Anime #Movie #Game
    collapsed:: true
    - GET_ISBN_INFO
      - Similar products: GET_ANIME, GET_VIDEO, GET_GAME
    - [实体图书扫描导入 Notion 实践 · 豆瓣评分版 - Linmi](https://linmi.cc/42154.html)
- ## What
  - What I mostly care when I read? #.ol
    collapsed:: true
    - **Digest** ≫ *Print Book* in most cases.
      collapsed:: true
      - `equb` > `awz3` >= `mobi` > `PDF` (**手写UP**)
        - > PDF 是输出文件，不推荐编辑。打个比方，你用什么肥料灌溉米饭？ 
          via: [你用什么编辑 pdf? - V2EX](https://www.v2ex.com/t/863307#; ) #Discuss
        - 前 3 者可以转换 `PDF`, 过程不可逆. 但 `PDF` 更加通用, 可以直接做文章的引用(准确到页)
          - `mobi/azw*`
            - Amazon 私有格式, 亚马逊利用 `azw` 对电子书做 `DRM` 版权保护
            - `azw3`
              - `KF8`(2011), 填补 `Mobi` 对复杂排版支持, 支持很多 HTML5
          - `epub`
            - 开放标准, 已取代了先前的 Open eBook 开放电子书标准, 对复杂的排版, 图表, 公式等元素的兼容性及在脚本, 公式, 矢量图形的支持方面也强过 `mobi` 格式.
            - via: [电子书格式 MOBI、AZW3、KFX、EPUB 有什么区别 – 书伴](https://bookfere.com/post/27.html)
        - `chm`
          - 微软 1998 年替代早先的 WinHelp 帮助系统,基于 HTML 文件特性的帮助文件系统。它在 Windows 98 中把 CHM 类型文件称作“编译的 HTML 帮助文件”
      - Most case: 出行/检索/保存/传播; 大多数出版 1-2 年的书, 可以选择纸质书购买之后, 做成电子般, 然后把纸质转手处理 (多抓鱼/闲鱼); 年份比较久远 (2年以上) 基本就都有电子的了
    - 判断是否收藏: Market Price / Hobbies
      collapsed:: true
      - 要留一套书珍藏 -> 扫码看回收价 / 书本身是否稀缺 / 自己喜好.
  - WAITING What's your reading list?
    collapsed:: true
    - 163 网易云课堂
      collapsed:: true
      - 经典
        collapsed:: true
        - 平凡的世界
        - 呼啸山庄
        - 美丽新世界
        - 权力与爱情的互：棘鸟
        - 霍乱时期的爱情
        - 丧钟为谁而鸣
        - 中国科幻文学 里程碑：三体
        - 追风筝的人
        - 岛上书店：每本书都是一个世界
        - 芳华：到底是谁摸了谁
        - 月亮和六便士
        - 白鹿原：中国文学的不朽史诗
        - 麦田里的守望者
        - 感动千万青年的励志名篇：人生
        - 干般人物的百态人生：围城
        - 以笑的方式哭在死亡的伴随：活着
        - 玛格丽特小镇
        - 文学史上最纯净的文本：边城
        - 傲慢与偏见
        - 日瓦戈医生
        - 我不是潘金莲
        - 肖申克的救赎
        - 跨越战争的凄美恋情：广岛之恋
        - 一本探讨时间与爱情的小说：情人
        - 了不起的盖茨比
        - 寻找时间的人
        - 时间停止的那一天
        - 当呼吸化为空气
        - 令人发指的犯罪：白夜行
        - 德语文学巨匠黑寒巨作：悉达多
        - 一个女人横跨四十年人生：长恨歌
        - 红高梁家族
        - 辛德勒名单
        - 挪威的森林
        - 嫌疑犯X的献身
        - 冰与火之歌：权力的游戏
        - 红与黑：一人短暂一生奋斗消亡史
        - 一个献给成年人的童话：小王子
        - 在乡村人和动物忙着生死：生死场
        - 玩偶之家：妇女解放运动的宣言书
        - 世界上的另一个你
        - 浮生六记：晚晴小红楼
        - 不能承受的生命之轻
        - 战争与和平
        - 永别了，武器
      - 高效
        collapsed:: true
        - 战胜拖拉：让你高效工作的红宝书
        - 里奥巴伯塔："少”的力量
        - 创业达人熊谷正寿：三个记事本
        - 时间管理：如何分H24 时
        - 如何像学霸一样高效搭建知识结构
        - 时间投资法，轻松管理你的时间
        - 拖延心理学：如何克服拖延？
        - 专注力：如何让自己更专注？
        - 意志力：关于自控与效率的心理学
        - 请停止无效努力：把握天赋与优势
      - 职场
        collapsed:: true
        - 深度工作：彻底告别低效忙碌
        - 卡内基沟通与人际关系：社交技巧
        - 互联网营销的终极方法论：引爆点
        - 职场小白脱菜手册：脱菜必备
        - 12个工作的基本能力：竞争力
        - OKR工作法：如何让目标聚焦
        - 番茄工作法：简单高效的工作模式
        - 风格感觉：21世纪写作指南
        - 靠谱：什么样的人才算靠谱？
        - 麦肯锡工作方法
        - 每天必做的3件事儿
        - 你为什么而工作：满足感
        - 清单革命：有序、高效的秘密
        - 销售圣经：学习如何成为赢家
        - 销售中的心理学
        - 一个广告人的自白
      - 管理
        collapsed:: true
        - 孤独：如何正确看待孤独
        - 安静：内向性格的竞争力
        - 稻盛和夫：阿米巴经营
        - 知道做到：抓住专注力的金线
        - 创新与企业家精神
        - 从优秀到卓越
        - 细节：如何轻松影响他人
        - 心流：如何让你有用不完的力气
        - 重新定义公司
        - 如何做出正确决策：赢家的秘诀
        - 商业的本质：重新定义创新
        - 取悦症：不懂拒绝的老好人
        - 管理十诫：管理者必看
        - 领导力21法则：普通人变领导者
        - 你的哪些生存本能正在杀死你？
        - 放弃的艺术：正确放弃的生活指南
        - 掌控力：让所有人对你讲真话
        - 这不是你的错：无条件接纳自己
      - 习惯
        collapsed:: true
        - 从行动开始：如何让自己行动起来
        - 断舍离：让人生舒适的行动技术
        - 极简主义，让你看清生活的重点
        - 坚持，一种可以养成的习惯
        - 精要主义：提高执行力的实用法
        - 刻意练习：如何从新手到大师
        - 怦然心动的整理术
        - 少即是多：北欧自由生活意见指南
        - 微习惯：简单到不肯能失败！
        - 习惯的力量：创造习惯的3个要素
      - 思考
        collapsed:: true
        - 智识分子：不换思想就换人
        - 简单的逻辑学（文稿国拆掉思维里的墙：人生开窍手册
        - 反直觉思考：互联网思维方式
        - 决断力：有效规避阻碍因素
        - 零秒思考：像麦肯锡精英一样思考
        - 六顶思考帽：创意思考的帽子戏法
        - 你的灯亮着吗？分析与策略的艺术
        - 逆转：如何面对强大的敌人？
        - 失败的逻辑：应当如何避免失败？
        - 人生总会有办法：打破思维惯性
        - 思考，快与慢：人类思维的奇妙思维改变生活：实用心理管理手册
        - 提问的力量：11种问题模型
        - 万万没想到：用理性思维审视世界
        - 走出思维的误区：学会批判
      - 沟通
        collapsed:: true
        - 非暴力沟通
        - 像TED一样演讲
        - 蔡康永的说话之道
        - 好好说话：新鲜有趣的话术精进
        - 6个问题竞能说服各种人
        - 洗脑术：怎样有逻辑地说服他人
        - 高难度谈话
        - 好好说话第一步：学会倾听
      - 心理
        collapsed:: true
        - 狂热分子：码头工人哲学家的沉思
        - 理性动物 文稿E FB教你超级读心术
        - 稀缺：我们是如何陷入贫穷与忙碌
        - 洞察人性
        - 何为良好生活
        - 怪诞心理学
        - 输赢心理学
        - 说谎心理学：不说谎我们活不下？
        - 丘吉尔的黑狗
        - 我知道你在想什么
        - 心理学与生活
        - 梦的解析
        - 读心术：不为人知的情况下影响人
      - 情绪
        collapsed:: true
        - 活出最乐观的自己
        - 情绪急救
        - 我的情绪为何总被他人左右
        - 拆除你的情绪地雷
        - 控制焦虑
        - 控制愤怒
        - 身份的焦虑
        - 成功心理学
        - 我们内心的冲突
        - 如何停止忧虑开创人生
      - 心态
        collapsed:: true
        - 吸引力法则
        - 全新思维：决胜未来的6大能力
        - 超越智商
        - 正念的奇迹
        - 初学者的冥想书
        - 成功者的大脑
        - 改变，从心开始
        - 活出生命的意义
        - 成功这件小事
        - 赢家法则
        - 异类：不一样的成功启示录
        - 人生中不可不想的事
      - 互联网
        collapsed:: true
        - 浅薄：你是互联网的奴隶还是主宰
        - 免费：商业的未来
        - 认知盈余
        - 数字化生存
        - 长尾理论
        - 流量池
        - 疯传：让你的产品像病毒一样入侵
        - 增长黑客：如何低成本实现爆发
        - 上瘾：让用户养成使用习惯的产品
        - 从零开始做运营
      - 投资
        collapsed:: true
        - 货币战争
        - 小狗钱钱
        - 聪明的投资者
        - 投资最重要的事
        - 财务自由之路
        - 白银帝国
        - 思考致富
        - 反脆弱
        - 伟大的博弈
        - 疯狂的投资
        - 富人的逻辑：如何创造财富
      - 经济
        collapsed:: true
        - 牛奶可乐经济学
        - 解读中国经济
        - 小岛经济学
        - 斯坦福极简经济学
        - 无价：洞悉大众心理玩转价格游戏
        - 中央帝国的财政密码
        - 集装箱改变世界
        - 实力、运气与成功
      - 历史
        collapsed:: true
        - 昨日的世界：一个欧洲人的回忆
        - 战争与革命中的西南联大
        - 南京大屠杀
        - 天朝的崩溃
        - 你一定爱读的极简欧洲史
        - 中国大历史
        - 罗马人的故事2：汉尼拔战纪
        - 晚清七十年
        - 秦谜-——重新发现秦始皇
        - 全球通史
        - 大明王朝的七张面孔
        - 天国之秋
        - 南渡北归
        - 罗马人的故事
        - 唐朝穿越指南
        - 中国近代史
        - 穿越百年中东
        - 美国种族简史
        - 袁氏当国
        - 一口气读完欧洲史
        - 重说中国近代史
        - 拜占庭帝国
        - 丝绸之路：一部全新的世界史
        - 百年战争简史
        - 荷马史诗中的生与死
        - 海洋与文明
        - 奥斯维辛：一部历史
        - 极简德国史
      - 传记
        collapsed:: true
        - 人类群星闪耀时
        - 莱昂纳德科恩传
        - 萧红传
        - 奥黛丽赫本传
        - 张爱玲传
        - 宋美龄传
        - 约瑟夫富歇传
        - 周恩来传
        - 陈寅恪的最后20年
        - 蒋介石与现代中国
        - 狄仁杰传
        - 苏东坡传
        - 李白传：道教徒诗人李白及其痛苦
        - 李鸿章传
        - 朱元璋传
        - 曾国藩的正面与侧面
        - 梵高传
        - 知行合一王阳明
        - 佛陀传
        - 沈从文的后半生
      - 探索人生
        collapsed:: true
        - 亲情、感人至深的文集：目送
        - 全景领略舆论传播现象：舆论
        - 老后破产：名为长寿的噩梦
        - 爱情社会学
        - 单身社会
        - 下流社会
        - 人情、面子与权力的再生产
        - 厚黑学
        - 历史深处的忧虑
        - 神风特攻队、樱花与民族主义
        - 房间里的大象
        - 寻路中国
        - 格调：社会等级与生活品味
        - 中国人为什么活得累
        - 路西法效应：好人是如何变成恶魔
        - 我们时代的神经病人格
        - 社会性动物
        - 日常生活中的自我呈现
        - 叫魂1768年中国妖术大恐慌
        - 趣味生活简史
        - 气质：如何成为一名优雅女人
        - 优雅女人的气质修养与社交礼仪
        - 跟巴黎名媛学到的事
        - 生活十讲
        - 最好的告别
        - 你要如何衡量你的人生
        - 幸福的方法
        - 活法：从稻盛和夫人生中寻找真谛
        - 原则
        - 关于爱与性的一切，你全错了
        - 男人来自火星，女人来自金星
        - 如何在爱中修行
        - 为何越爱越孤独
        - 亲密关系
        - 爱的艺术
        - 女性的圣经：第二性
        - 爱有8种习惯
        - 情感暴力：你会和亲近的人相互伤
        - 性学二论爱情心理学
      - 品人生
        collapsed:: true
        - 艺术
        - 耶鲁大学公开课：死亡
        - 人间词话
        - 中国国民性演变历程
        - 美的历程
        - 美学理论体系中的重要著作：谈美
        - 艺术的故事
        - 如何阅读一本文学书
        - 东北游记
        - 科学与宗教的领地
        - 花朵的秘密生命
        - 一百年漂泊：台湾的故事
        - 一只特立独行的猪
        - 沉默的大多数
        - 神的故事
        - 江湖丛谈
        - 金刚经说什么
        - 千古文人侠客梦
        - 中国神话研究初探
        - 病隙碎笔
        - 中国古代文化识
        - 西藏生死书
        - 国学常识
        - 儒教中国及其现代命运
        - 我们台湾这些年
        - 唐诗的读法
        - 责任的重负
        - 曾国藩家书
        - 丧家狗：我读《论语》
      - 提视野
        collapsed:: true
        - 知识的边界
        - 大国大城：当代中国的统一、发展
        - 文明是副产品
        - 自私的基因
        - 枪炮、病菌与钢铁
        - 七堂极简物理课
        - 睡眠革命
        - 植物的欲望
        - 性别战争
        - 量子物理史话：上帝掷骰子吗？
        - 笑什么笑，我们搞的是科学
        - 从一到无穷大：科学中的事实
        - 寂静的春天
        - 记忆的风景：我们为什么想起
        - 众病之王：癌症传
        - 纽约：一座超级城市是如何运转的
        - 果壳中的宇宙
        - 生命的跃升
    - [「ONE · 一个」](http://wufazhuce.com/)
    - [微信读书排行榜 ~ 热门标注 - Klib.me](http://klib.me/weread/hot/all.html)
    - [意林在线阅读_就爱意林网(92yilin.com)](http://www.92yilin.com/)
    - [繁體中文書庫](http://www.bwsk.net); [王小波](http://www.bwsk.net/xd/w/wangxiaobo/index.html)
    - [马克思主义文库](https://www.marxists.org/chinese/index.html)
    - [中国哲学书电子化计划](https://ctext.org/zhs)
    - [programthink/books: 【编程随想】收藏的电子书清单（多个学科，含下载链接）](https://github.com/programthink/books) ![](https://img.shields.io/github/stars/programthink/books)
    - [hehonghui/awesome-english-ebooks: 经济学人(含音频)、纽约客、卫报、连线、大西洋月刊等英语杂志免费下载,支持epub、mobi、pdf格式, 每周更新](https://github.com/hehonghui/awesome-english-ebooks) ![](https://img.shields.io/github/stars/hehonghui/awesome-english-ebooks)
    - [lancetw/ebook-1: A collection of classic computer science books from Internet](https://github.com/lancetw/ebook-1) ![](https://img.shields.io/github/stars/lancetw/ebook-1)
    - [0voice/expert_readed_books: 2021年最新总结，推荐工程师合适读本，计算机科学，软件技术，创业，思想类，数学类，人物传记书籍](https://github.com/0voice/expert_readed_books) ![](https://img.shields.io/github/stars/0voice/expert_readed_books)
    - [yuanliangding/books: "我的阅历"](https://github.com/yuanliangding/books) ![](https://img.shields.io/github/stars/yuanliangding/books)
      [netkiller/netkiller.github.io: Netkiller Free ebook - 免费电子书](https://github.com/netkiller/netkiller.github.io)
    - [jyfc/ebook: classic books of computer science](https://github.com/jyfc/ebook) ![](https://img.shields.io/github/stars/jyfc/ebook)
    - [rmlzy/my-ebook: 我收集的电子书, 主要是软件开发方向](https://github.com/rmlzy/my-ebook) ![](https://img.shields.io/github/stars/rmlzy/my-ebook)
    - [AMKhalifa/books](https://github.com/AMKhalifa/books) ![](https://img.shields.io/github/stars/AMKhalifa/books)
    - [wnma3mz/Reading-Books: save books](https://github.com/wnma3mz/Reading-Books) ![](https://img.shields.io/github/stars/wnma3mz/Reading-Books)
    - [ShawnLeee/the-book](https://github.com/ShawnLeee/the-book) ![](https://img.shields.io/github/stars/ShawnLeee/the-book)
    - [cq0206/good-books: 程序员需要的读的书](https://github.com/cq0206/good-books) ![](https://img.shields.io/github/stars/cq0206/good-books)
  - [shurain/chm2pdf: Automatically exported from code.google.com/p/chm2pdf](https://github.com/shurain/chm2pdf)
    collapsed:: true
    - pip intsall [pychm](https://pypi.org/project/pychm/).
    - [chmlib](http://www.jedrea.com/chmlib/) lib support. [via](https://blog.51cto.com/mengix/1547830)
  - [推荐一个GitHub的开源电子书仓库，值得收藏_Java_C语言与CPP编程_InfoQ写作社区](https://xie.infoq.cn/article/207aab244ae44b9fc5c71a059)
  - [理解数字世界中的纸张：PDF | 科普 - 少数派](https://sspai.com/post/47092)
  - [PDF加密、解密内幕（一）- (PDF加密字典对象分析)_pdfMaker的博客-CSDN博客](https://blog.csdn.net/pdfMaker/article/details/1039046)
  - [17 Best Z-Library Alternatives of 2022](https://rarathemes.com/blog/best-z-library-alternatives/)
  - JEL分类系统
    collapsed:: true
    - > JEL分类系统, 是美国经济学会《经济文献杂志》（Journal of Economic Literature)所创立的对经济学文献的主题分类系统, 并被现代西方经济学界广泛采用。 该分类方法主要采用开头的一个英文字母与随后的两位阿拉伯数字一起对经济学各部类进行“辞书式”编码分类。