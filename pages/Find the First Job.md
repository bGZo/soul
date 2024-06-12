created:: 20220801
tags:: #Job, #DONE, byd

-
- ## Why
  -
- ## How
  -
- ## What
  -
-
- ## 2022 秋招
  background-color:: pink
  collapsed:: true
  - Waiting Poll/Queue
    collapsed:: true
    - [[dream]]
      collapsed:: true
      - 豆瓣
      - One
      - 看理想
      - 网易
      - **外企** (招聘信息都是英文...)
        collapsed:: true
        - [Amazon.jobs](https://www.amazon.jobs/zh/jobs/2158897/software-dev-engineer-ai-lab-ml-commons)
        - Shopee
          collapsed:: true
          - > 可能需要一个VPN，取决于你能不能打开 https://codeshare.io
          - **golang**!!!
          - via: [Job-Recommend/Shopee.md at master · CyC2018/Job-Recommend](https://github.com/CyC2018/Job-Recommend/blob/master/infos/Shopee.md)
          - [Sophon Tech](https://github.com/CyC2018/Job-Recommend/blob/master/infos/Sophon%20Tech.md)
        - [2023 eBay 校园招聘正式启动！](https://mp.weixin.qq.com/s?srcid=0907gQG8XN88RaaD13honZFY&scene=23&sharer_sharetime=1662547836546&mid=2247518258&sharer_shareid=b18b5e5ef03f880c42f4c81d0bac68d4&sn=76f03e14680765845b1d97539d909f3c&idx=4&__biz=MzUyNzcxOTI0Mg%3D%3D&chksm=fa798617cd0e0f013db7f3ddc41a0087680deb11794d60051a73d1e81eb6f866c01e7881cbe4&mpshare=1#rd)
        - [Nestlé 2022 Campus Recruitment](https://www.ajinga.com/company-detail-new/12262/?aj_source=Nestle_campus2023&aj_code=Wechat_offical)
    - SAP
    - LINE
    - 花旗
    - 思科
    - 富达
    - Oracle
    - 乐天
    - 英特尔
    - 索尼
    - 爱立信
    - 金兰
    - 惠普
    - 松下
    - 拜耳
    - 艾昆纬
  - Expanded "Have Dead"
    query-table:: true
    background-color:: grey
    collapsed:: true
    - query-table:: true
      query-properties:: [:block :mark]
      #+BEGIN_QUERY
      { :title "Current Members"
        :query [:find (pull ?b [*])
                :in $ ?current-page
                :where
                [?b :block/page ?p]
                [?p :block/name ?current-page]
                [?b :block/parent ?parent]
                [?parent :block/content "Have Dead"]]
        :inputs [:current-page] }
      #+END_QUERY
    - Have Dead
      collapsed:: true
      - TCL 中环
        source:: [TCL 校园招聘](http://campus.tcl.com/); [牛客 TCL 校招内推码:evnpow](https://www.nowcoder.com/discuss/1024990)
        mark:: Base Hohhot 没有研发; 所以投的是 **TCL中环信息技术岗...**
      - 银联招聘
        source:: [2022银联招聘，专属内推码来啦，推荐人工号:TJU220001、PKU220001（任选其一；长期有效；校招、实习、社招均可） - 力扣（LeetCode）](https://leetcode.cn/circle/discuss/Jmfish/); [应聘者更新简历elink](https://cloud.italent.cn/PageHome/Index?product=Recruitment&keyName=Nusion&pageCode=RecruitPerfectResume&appCode=Recruitment&inviteKey=b1e8eb6e-4281-43b1-83af-66c62d6cc4e0&needsign=1&shadow_context=%7B%22elinkId%22:%22229f0ec8-d743-4f74-8e4f-36e9fd1dbfa8%22%7D&bc_sign=8697be66a83dbf3c772a3f4c842a7b2f350085b9&bc_ts=1663748647979&bc_nonce=z30l6y#/viewDynamic?t=t&shadow_context=%7BappModel:%22italent%22,uppid:%22%22%7D )
        collapsed:: true
        - ((635742ac-1c01-4109-aca5-c1149bc15cb8))
        - [20221012银联数据面试（一面）_笔经面经_牛客网](https://www.nowcoder.com/discuss/1075078)
        - [银联数据服务有限公司是一家怎样的IT企业？ - 知乎](https://www.zhihu.com/question/53083355)
        - [银联数据面试经验|面试题（共26条）- 职朋](https://www.job592.com/pay/comms32096.html)
      - 中国农业银行/信息科技岗
        source:: [中国农业银行欢迎您](https://career.abchina.com.cn/build/index.html#/99); [招430人！中国农业银行 | 内蒙古自治区分行2023年度校园招聘公告](https://mp.weixin.qq.com/s?srcid=0911Yn8sNoTKgPN3zD7LCU2e&scene=23&sharer_sharetime=1662900200205&mid=2247516410&sharer_shareid=ed465edf35aa5b7978ee21fadcb5544f&sn=f729fd090f210ba9a790cdb635d398d0&idx=3&__biz=MzUxMTY4NDY3Ng%3D%3D&chksm=f96d39d1ce1ab0c764f111a0554548720eab3bd9dd4c898caabbfa5fb967157e4f599a022012&mpshare=1#rd)
      - 招商银行
        source:: [招商银行招聘](https://career.cloud.cmbchina.com/index.html#jobDetail?id=4d55b13c-dcce-4957-8589-9b0f9d2903b5&returnUrl=#jobList?id=96574F8D-C7ED-4772-AE7C-BAC896D190C1); [【持续招聘中】招商银行总分行内推2022校园招聘社会招聘_招聘信息_牛客网](https://www.nowcoder.com/discuss/740738?type=7&order=0&pos=3&page=7&ncTraceId=&channel=-1&source_id=discuss_tag_nctrack)
      - 建设银行
        tags:: TODO
        mark:: edge 还需要继续投; 选择信息技术类/综合类;
        source:: [中国建设银行—招聘](https://job1.ccb.com/cn/job/apply_job.html?planType=XY&orgId=2017283&planId=2022090511972949&planPost=20220905111009613754&secondOrgId=2019740); [建设银行笔试如何准备？笔试科目是什么？ - 知乎](https://www.zhihu.com/question/390444369)
      - 工商银行
        source:: [中国工商银行人才招聘](https://job.icbc.com.cn/pc/index.html#/main/personal/delivery); [有人了解工行的科技菁英计划吗？ - 知乎](https://www.zhihu.com/question/390165735)
      - 隆基绿能
        source:: [隆基绿能招聘官网-总部应用系统(018153)](https://longi.hotjob.cn/wt/LONGI/web/index/applyPositionN300!listApplyPosition?brandCode=1&operational=0b2e50a55fb57c0f5e596251256fc53864317a65ae774294a9321ea4ee967f58f6573a8fac28e9cde39a55debb9ebd98bbd2451484724a4d8eef99cce681e3eb6c053616eeb87558b84d989caa1bc67f822fabda092f0129393dfc460c74c860);[请问西安隆基绿能公司怎么样？ - 知乎](https://www.zhihu.com/question/379375885)
      - 人大金仓
        mark:: 岗位不符(C)
        source:: [校园招聘](https://app.mokahr.com/campus-recruitment/kingbase/47259#/job/9a50fedc-8606-49e0-9c2c-5fe8dfb52070)
        collapsed:: true
        - WAITING [Linux后台开发面试高频题经验分享 - 掘金](https://juejin.cn/post/6844904062538907661)
        - WAITING [人大金仓信息技术股份有限公司面试经验|面试题（共13条）- 职朋](https://www.job592.com/pay/comms29813784.html)
        - WAITING [秋招04-人大金仓1面-Linux c软件开发工程师_笔经面经_牛客网](https://www.nowcoder.com/discuss/1004483)
        - WAITING [「人大金仓信息技术股份有限公司c面试题目|面试经验」-看准网](https://www.kanzhun.com/firm/interview/j479451_1XZ73929.html)
      - 比亚迪 BYD
        mark:: 深圳 7500;水电不包; 西安Java已无消息;
        source:: http://job.byd.com/zpweb/zpweb/planList.do
        collapsed:: true
        - > 比亚迪是去学校签吧一般。综合面加技术面，然后就是逼签，流程特别快一般一个星期整个流程结束。签的时候要慎重考虑，迪子是直接三方不是offer，签了主动权就不在你手上了。
          >
          > via: https://www.nowcoder.com/feed/main/detail/dc45a0aa252342cca3bcf44be2c7a7d1
        - Refs
          collapsed:: true
          - [[discuss]]
            collapsed:: true
            - 来比亚迪十个月后宿舍变化
              collapsed:: true
              - {{video https://www.bilibili.com/video/BV1xU4y1S7BK}}
            - 比亚迪单人间
              collapsed:: true
              - {{video https://www.bilibili.com/video/BV1N3411L7mZ}}
            - 比亚迪你可以加点工资吗？
              collapsed:: true
              - {{video https://www.bilibili.com/video/BV1p34y1a7tk}}
          - [比亚迪校招面试为啥那么简单? - 知乎](https://www.zhihu.com/question/489806055)
          - [(深圳坪山/西安高新) 比亚迪汽车内推 - V2EX](https://de.v2ex.com/t/837320)
          - [(深圳坪山)比亚迪汽车招聘内推 - V2EX](https://v2ex.com/t/873782)
          - [比亚迪（BYD）面试经验|面试题（共491条）- 职朋](https://www.job592.com/pay/comms29499190.html)
      - 蒙牛
        source:: [蒙牛校园招聘](http://mengniu.zhiye.com/xiaoyuan?k=&c=&p=1^31,3^-1&d=#zw )
        mark:: 数字化管培生 硕士起步
      - 内蒙古东部电力有限公司
        source:: [国家电网！内蒙古东部电力有限公司2023年招聘公告](https://mp.weixin.qq.com/s?srcid=1002vu4GJUwYAwnewHlv7YW0&scene=23&sharer_sharetime=1665225961438&mid=2247516951&sharer_shareid=41b07940e3c2478dcec2bf71ef0fa999&sn=dae232cf198c2af0181f8d3b058741fb&idx=1&__biz=MzUxMTY4NDY3Ng%3D%3D&chksm=f96d3a3cce1ab32ac9cd150860c0ec0a24123be81101fcd2e291a8a1794c787647bd735e181c&mpshare=1#rd); [中国高等教育学生信息网（学信网）](https://www.chsi.com.cn/)
      - 畅游－运维工程师申请职位
        source:: [搜狐畅游 - 校园招聘](https://app.mokahr.com/campus_apply/cyou-inc/42233?recommendCode=NTALgk3#/job/0c8531e4-a3ca-494f-8e9b-f6bd06783459/campus_apply/thanks?jobId=0c8531e4-a3ca-494f-8e9b-f6bd06783459&recommendCode=NTALgk3&codeType=1&isRecommendation=false&applyInfo%5BaimWorkCity%5D=%E5%8C%97%E4%BA%AC%E5%B8%82&applyInfo%5BrecommendCode%5D=NTALgk3&candidateName=%E9%B2%81%E4%B8%B0%E5%8D%8E&candidateId=372662636)
      - 伯乐科技 - 服务端开发工程师（python）
        source:: [北京博乐科技有限公司 - 校园招聘](https://app.mokahr.com/campus_apply/bolegames/37643?recommendCode=DSYTZEDX#/job/e73c1132-bf7f-45b6-b294-5829bc201c50/campus_apply/thanks?jobId=e73c1132-bf7f-45b6-b294-5829bc201c50&codeType=2&isRecommendation=false&applyInfo%5BaimWorkCity%5D=%E5%8C%97%E4%BA%AC%E5%B8%82&applyInfo%5BrecommendCode%5D=DSYTZEDX&candidateName=%E9%B2%81%E4%B8%B0%E5%8D%8E&candidateId=372643661)
      - 滴滴打车－后端研发工程师（Golang/Java/C++/PHP）
        mark:: 应该投测试的
        source:: [滴滴 - 校园招聘](https://campus.didiglobal.com/campus_apply/didiglobal/6223#/candidateHome/applications)；[2023届滴滴校招正式批开始啦！！！_招聘信息_牛客网](https://www.nowcoder.com/discuss/1027785)
      - Thoughtworks - 海外 - 软件开发工程师
        source:: [Thoughtworks](https://join.thoughtworks.cn/)
        mark:: 感谢信
      - 中国邮政
        mark:: Base深圳放弃
        source:: [中邮消费金融2023校园招聘](http://2023.yingjiesheng.com/youcash/)
      - 交通银行
      - 京东方
        source:: [在「京东方」工作或实习是一种怎样的体验？ - 知乎](https://www.zhihu.com/question/341516244); [我的申请](http://campus.boe.com/Portal/Apply/Index); [申请职位](http://campus.boe.com/Portal/Resume/ResumeItem?jid=880065277&stepId=0&sId=0&pId=1)
        mark:: 群面挂(3 个 985 硕士)
      - 中国银行
      - 福建新大陆自动识别技术有限公司
        source:: [福建新大陆自动识别技术有限公司](https://imu.nmbys.cn/teachin/view/id/7056); [我的申请](https://nlscan.zhiye.com/Portal/Apply/Index)
      - 比特大陆
        mark:: "挖矿的, 感觉容易被端"
        source:: [在比特大陆上班是一个怎样的体验？ - 知乎](https://www.zhihu.com/question/34468645)
      - 帆软
        mark:: 后台开发工程师 -> 测试工程师 -> 项目运维工程师
        source:: [帆软2023届校园招聘](https://t6ixa9nyl6.jiandaoyun.com/f/625e75b9fa406f0007ca777a)
      - 绿盟科技
        mark:: 秋招研发工程师-北京
        source:: [绿盟科技2023校园招聘](https://app.mokahr.com/campus_apply/nsfocus/29118#/job/22eab09c-1636-4778-ba14-68525f834891/campus_apply/thanks?jobId=22eab09c-1636-4778-ba14-68525f834891&codeType=2&isRecommendation=false&applyInfo%5BaimWorkCity%5D=%E5%8C%97%E4%BA%AC%E5%B8%82&applyInfo%5BrecommendCode%5D=DSKPEqJ4&candidateName=%E9%B2%81%E4%B8%B0%E5%8D%8E&candidateId=371491173)
      - 海康威视
        mark:: 只有C++硬件嵌入式开发
        source:: [校园招聘](https://mcampus.hikvision.com/#/school)
      - 华信咨询设计研究院有限公司
      - 北京时代数维
        mark:: 笔试挂
        source:: https://www.jobui.com/company/15391187/
      - Zoom
        mark:: 笔试挂
      - 4399
        mark:: 笔试挂
        source:: [4399](https://hr.4399om.com/?r=UserCenter)
      - 科大讯飞
        mark:: 笔试挂
        source:: [科大讯飞](https://campus.iflytek.com/official-pc/jobList); [科大讯飞2021校招笔试攻略 - 知乎](https://zhuanlan.zhihu.com/p/353333447)；[【科大讯飞】23届内推 内推码【fengwang26】#内推_招聘信息_牛客网](https://www.nowcoder.com/discuss/988104)
      - 用友 Java开发工程师 薪资面议
        source:: [用友校招](https://www.nowcoder.com/jobs/school/detail?jobId=126760&pageSource=7001&sponsorType=3)
      - 去哪儿旅行
      - [联想-招聘岗位](https://talent.lenovo.com.cn/joblist) - 异地线下宣讲
      - 翼支付
        source:: [翼支付](https://xyz.51job.com/external/MyResume/ResumeEnd.aspx?ctmid=b73cf57a-22ae-40ce-97fc-edb18707a273&css=%2f%2fimg03.51jobcdn.com%2fehireplus%2f2022%2fstyle%2fehireplus2009%2fnewcp1_2%2finc%2f&CtmName=%e7%bf%bc%e6%94%af%e4%bb%98&resumeid=eb4cfa0b-cc7e-4b61-9e4c-72915bdd2ece&jobid=f9b6a10f-2b03-4c49-b2fb-67a3e9ea3444,a2b2da4a-bad6-4b00-acf1-4772bc6f2b7a )
      - 北森
        source:: [北森 Java 南京](https://cloud.italent.cn/PageHome/Index?product=MicroRecommend&keyName=Nusion&pageCode=DeliveryForm&appCode=MicroRecommend&submissionKey=18a4373b-d99f-45a1-958d-b13753dd2e7c&shadow_context=%7B%22elinkId%22:%225550f74a-902d-4f06-a5ee-c7331bf0304a%22%7D#/viewDynamic?t=t)
      - 衡泰技术股份有限公司(杭州)
        source:: [衡泰技术股份有限公司(杭州)](https://app.mokahr.com/campus_apply/xquant/45053?sourceToken=2e4f4a7deba9dd8dd799d041ef822062#/job/3c99f6a4-7ff1-4b25-b40c-0f760aa3b2d0/campus_apply/thanks?jobId=3c99f6a4-7ff1-4b25-b40c-0f760aa3b2d0&isRecommendation=false&applyInfo%5BaimWorkCity%5D=%E6%9D%AD%E5%B7%9E%E5%B8%82&candidateName=%E9%B2%81%E4%B8%B0%E5%8D%8E&candidateId=358943664)
      - 旷视 MEGVII 校园招聘 北京 后端
        source:: [旷视 MEGVII 校园招聘 北京 后端](https://app.mokahr.com/campus-recruitment/megviihr/38642#/job/a7f8bde6-15d2-410c-b64d-e622b0472dba/campus_apply/thanks?jobId=a7f8bde6-15d2-410c-b64d-e622b0472dba&isRecommendation=false&applyInfo%5BaimWorkCity%5D=%E5%8C%97%E4%BA%AC%E5%B8%82&candidateName=%E9%B2%81%E4%B8%B0%E5%8D%8E&candidateId=358958721)
      - 依图科技 - 后端 杭州
        source:: [依图科技 - 后端 杭州](https://www.yitutech.com/cn/career?mode=campus)
      - 快手 - Java开发工程师
        source:: [快手校招 - Java开发工程师](https://campus.kuaishou.cn/recruit/campus/e/#/campus/my-apply)
      - 恒生 - 校园招聘
        mark:: "大概率简历挂, 没有招聘宣讲城市, 投出去也没有反应"
        source:: [恒生校招-校园招聘](https://campus.hundsun.com/campus/jobs);
      - 青岛特锐德电气股份有限公司
        source:: [青岛特锐德电气股份有限公司-智联招聘官网](https://xiaoyuan.zhaopin.com/company/CC000273317); [投递结果成功页](https://xiaoyuan.zhaopin.com/scrd/delivery/completed?rid=27331&rnum=CC000273317&taskId=&productId=3&channelId=2&scjobs=CC000273317J00101519105)
      - 中国联通
        source:: [投递结果成功页](https://xiaoyuan.zhaopin.com/scrd/delivery/completed?rid=89021&rnum=CC000890214&taskId=&productId=&channelId=&scjobs=CC000890214J00101553543)
      - 浪潮
        source:: [浪潮集团招聘](https://inspur.hcmcloud.cn/recruit#/portal_job_list?job_class=campus); [职位详情](https://inspur.hcmcloud.cn/recruit#/portal_job_detail?id=35590);
      - 厦门市美亚柏科信息股份有限公司
        source:: [厦门市美亚柏科信息股份有限公司 (2)](https://www.xmrc.com.cn/NewNet/Zone/XyYzp/Recruit.aspx?id=679569&companyId=853716&RecruitType=4&JobFairId=2140); [厦门人才网·校园云招聘平台](https://www.xmrc.com.cn/NewNet/Zone/XyYzp/Recruit.aspx?id=679569&companyId=853716&RecruitType=4&JobFairId=2140);
      - 厦门市美亚柏科信息股份有限公司 (10)
        source:: [厦门市美亚柏科信息股份有限公司 (10)](https://www.xmrc.com.cn/NewNet/Zone/XyYzp/Recruit.aspx?id=679290&companyId=6652&RecruitType=4&JobFairId=2140); [厦门人才网-个人会员管理中心](https://www.xmrc.com.cn/net/talent/Main.aspx)
      - 麦科田
        source:: [麦科田医疗2023届校园招聘空中宣讲会](https://video.51job.com/watch/3298323) to [感谢您应聘麦科田医疗](https://xyz.51job.com/External/MyResume/ResumeEnd.aspx?ctmid=7974a897-439c-4f13-b69f-eeb4ff00dcd9&css=%2f%2fimg03.51jobcdn.com%2fehireplus%2f2022%2fstyle%2fehireplus2009%2fnewcp1_1%2finc%2f&CtmName=%e9%ba%a6%e7%a7%91%e7%94%b0%e5%8c%bb%e7%96%97&resumeid=1ff43259-ebb1-4a5a-85aa-1b68953cca39&jobid=9b7b74f2-e431-4fc9-8197-679988e6ec25,b1f5dc82-6604-4ce0-962a-b87f5288d148&accountid=214547440&entype=&ismap3=False )
      - 特来电; 软件开发工程师（南京)(J10019)
        source:: [投递结果成功页](https://xiaoyuan.zhaopin.com/scrd/delivery/completed?rid=96036&rnum=CC000960368&taskId=null&productId=7&channelId=null&scjobs=CC000960368J00101522367)
      - 华信咨询设计研究院有限公司
        source:: [华信设计院-应届生招聘 - 智联招聘](http://hxdi2023.zhaopin.com/graduates_position2.html?deptid=4); [投递结果成功页](https://xiaoyuan.zhaopin.com/scrd/delivery/completed?rid=29365&rnum=CC000293655&taskId=null&productId=7&channelId=null&scjobs=CC000293655J00101532967)
      - 上汽通用五菱汽车股份有限公司
        source:: [上汽通用五菱招聘](https://wecruit.hotjob.cn/SU611bbe3c2f9d24229e014abb/pb/school.html?currentPage=3); [上汽通用五菱招聘](https://wecruit.hotjob.cn/SU611bbe3c2f9d24229e014abb/pb/posDetail.html?postId=62f5f8670dcad44f7a13b08b&postType=campus&isFollowTimeRules=true)
      - ASMPT
        source:: [我的申请](https://atcrecruit.zhiye.com/Portal/Apply/Index)
      - 锐捷网络股份有限公司
        source:: [锐捷网络股份有限公司 - 校园招聘](https://app.mokahr.com/campus_apply/ruijie/68094#/job/1e8c9bb6-7f39-43e2-a721-00d73474e04b)
      - 奇安信科技集团股份有限公司
        source:: [奇安信科技集团股份有限公司 - 校园招聘](https://app.mokahr.com/campus_apply/qianxin/29182#/job/4509fe79-b1ac-4916-a2a2-565917020d96)
      - 无锡信捷电气股份有限公司
        source:: [投递结果成功页](https://xiaoyuan.zhaopin.com/scrd/delivery/completed?rid=53897&rnum=CC000538976&taskId=&productId=3&channelId=2&scjobs=CC000538976J00101383244)
      - 亿纬动力
        source:: [2023亿纬动力校园大使报名通道](https://www.wjx.cn/wjx/join/completemobile2.aspx?activityid=wlLMb0p&joinactivity=114186406004&sojumpindex=163&comsign=2A2B55280519A6C2AB38E80781CBCBBF119ABBC2&educ=4&nw=1&jpm=52) wx: `echo1875`
      - 中国中化
        source:: [中国中化招聘官网](https://sinochem.hotjob.cn/SU610b91ee0dcad4106ff11c21/pb/posDetail.html?postId=630dae3abef57c3179fd65fa&postType=campus&isFollowTimeRules=true)
      - 威努特
        mark:: Java 只有社招
        source:: [校园招聘 - 威努特](http://www.winicssec.com/about/l180.html)~~
      - 美的集团
        source:: [美的集团-校园招聘官网-Midea校招/实习生招聘](https://careers.midea.com/schoolOut/post/details?projectRuleId=cf176940-20cc-4651-a0d7-b64b8c452399&positionId=8a928eaf826e136d0182aa81357a0576&recruitCategoryId=85ed0569354a46578240983830fe0c5b&tabActive=1)
        mark:: 笔试挂; 没有面试城市
      - 爱奇艺
        mark:: 校招0
        source:: [爱奇艺 - 校园招聘](https://campus.iqiyi.com/campus_apply/iqiyi/38597#/jobs)
      - 小马智行
        mark:: "偏硬件, 自动驾驶, 嵌入式开发"
        source:: [小马智行 Pony.ai - 校园招聘](https://app.mokahr.com/campus-recruitment/pony/42966/#/jobs?zhineng=15065)
      - 顺丰
        mark:: 简历挂
        source:: [顺丰2023届校园招聘](http://campus.sf-express.com/#/recruitmentList?intern=1)
      - 猿辅导
        mark:: "做客户端的多, 没有 Java"
        source:: [2023猿辅导在线教育 - 校园招聘](https://hr.yuanfudao.com/campus-recruitment/fenbi/47742/#/)
      - 鹰角网络
        mark:: "游戏公司, 做动漫的"
        source:: [鹰角网络校园招聘](https://app.mokahr.com/campus_apply/hypergryph/26326?sourceToken=58b0eaa4804d0e9a762bd363f341577a#/)
      - 美团
        mark:: 好像没有 Java 的
        source:: [职位列表 | 美团招聘官网](https://campus.meituan.com/jobs?jobType=1)
      - 微众银行招聘
        mark:: 人工智能?...
        source:: [微众银行招聘](https://job.webank.com/campus_apply/webankhr/69#/)
      - Grab
        mark:: 只要社招
        source:: [Grab](https://github.com/CyC2018/Job-Recommend/blob/master/infos/Grab.md)
      - 涂鸦智能
        mark:: 没有 Java 后端
        source:: [涂鸦智能 - 校园招聘](https://app.mokahr.com/campus_apply/tuya/3235#/jobs?keyword=%E5%90%8E%E7%AB%AF)
      - 字节跳动
        mark:: 简历挂
        source:: [字节跳动校园招聘](https://jobs.bytedance.com/campus/position); [投递成功 - 加入字节跳动](https://jobs.bytedance.com/campus/resume/applied?spread=62PP8M5)
      - 虎牙
        source:: [【虎牙内推】2022届虎牙校招正式批/社招内推中_招聘信息_牛客网](https://www.nowcoder.com/discuss/716676); [虎牙直播-校园招聘](https://app.mokahr.com/campus_apply/huya/4112#/job/9b7aa223-180b-4404-b509-6bed5f1721c2/campus_apply/thanks?jobId=9b7aa223-180b-4404-b509-6bed5f1721c2&recommendCode=NTAF80f&codeType=1&isRecommendation=false&applyInfo%5BaimWorkCity%5D=%E5%B9%BF%E5%B7%9E%E5%B8%82&applyInfo%5BrecommendCode%5D=NTAF80f&candidateName=%E9%B2%81%E4%B8%B0%E5%8D%8E&candidateId=371859818)
      - 携程集团
        mark:: "忘写内推码了, 淦... NTAH8Ma"
        source:: [携程集团 - 校园招聘](https://campus.ctrip.com/campus-recruitment/trip/37757#/job/e2d3d24f-e064-4c6a-bd22-695316d64408/campus_apply/thanks?jobId=e2d3d24f-e064-4c6a-bd22-695316d64408&recommendCode=NTAH8Ma&codeType=1&isRecommendation=false&applyInfo%5BaimWorkCity%5D=%E5%8C%97%E4%BA%AC%E5%B8%82&applyInfo%5BrecommendCode%5D=NTAH8Ma&candidateName=%E9%B2%81%E4%B8%B0%E5%8D%8E&candidateId=371877327)
      - OPPO
        mark:: "面试地点没有线上, 没有呼和浩特"
        source:: [校园招聘](https://careers.oppo.com/campus/resume?fromPage=postDetail&projectName=2023%E5%B1%8A%E7%A7%8B%E5%AD%A3%E6%A0%A1%E5%9B%AD%E6%8B%9B%E8%81%98&acceptStr=%E7%AC%AC%E4%B8%80%E6%84%8F%E5%90%91&positionName=%E5%90%8E%E7%AB%AF%E5%B7%A5%E7%A8%8B%E5%B8%88&idJobObjective=361728&acceptCity=%E5%8D%97%E4%BA%AC%E3%80%81%E6%88%90%E9%83%BD&id=581&isDone=N&positionTypeName=%E8%BD%AF%E4%BB%B6%E7%B1%BB&isNeedKey=true)
      - 腾讯
        source:: [岗位投递 | 腾讯校招](https://join.qq.com/post.html?query=p_1&keyword=Java);[如何看待 2023 腾讯 9.15 开启秋招? - 知乎](https://www.zhihu.com/question/553790535)
      - 蔚来
        mark:: "没有 Java， 嵌入式"
        source:: [蔚来校园招聘](https://nio.jobs.feishu.cn/campus/?keywords=&category=&location=&project=7107135604417464612&type=&job_hot_flag=¤t=1&limit=10&functionCategory=&spread=SAYV33H ); [NIO内推](https://nio.jobs.feishu.cn/referral/campus/position?keywords=%E8%BD%AF%E4%BB%B6&category=6937213309162752293&location=&project=&type=&job_hot_flag=&current=2&limit=10&functionCategory=&token=MzsxNjU1NzEwNTQ1MjgxOzcwMzMwNjM2MDgzOTc1Nzk3ODk7MA)
      - 阿里巴巴
        mark:: 没有 Java
        source:: [阿里巴巴集团校园招聘](https://talent.alibaba.com/campus/position-list?campusType=freshman&lang=zh)
  - Progressing
    collapsed:: true
    - 笔试
    - 面试
      collapsed:: true
      - 1 面
      - 2 面
      - 3 面
  - Offer
    collapsed:: true
    - 1. 呼市 ((897e08e2-21cc-49f5-a802-86c9921c2828))
    - 2. ((bf150140-9372-4b57-87bd-f87d492d28fa))
    - collapsed:: true
      3. 华宇（大连）信息服务有限公司
      source:: [华宇（大连）信息服务有限公司](http://www.dl-hr.com/company!view?company.id=860ed51e-626e-4c1a-97a0-6fd906685282 ); [华宇（大连）Java怎么样？-看准网](https://www.kanzhun.com/firm/review/1nFy3dy5Fw~~/j100101/p2.html);
      mark:: 暴雷公司; 不如东软; 连个官网都没有;
      - 埃森哲 > 华宇
        collapsed:: true
        - [搜索埃森哲最新职位 | 埃森哲](https://www.accenture.cn/cn-zh/careers/jobsearch?jk=&sb=1&pg=1&vw=0&is_rj=0&ct=%E5%A4%A7%E8%BF%9E)
      - Refs
        collapsed:: true
        - > 大连东软 vs 大连华宇, 老哥们给个意见
          前提: 边缘211本, 大学前几年卷保研了, 然后显然失败了, 基础 CRUD 会, 然后 Java 基础最近
        - [华宇(大连)信息服务有限公司怎么样？ - 知乎](https://www.zhihu.com/question/358628053)
        - [在华宇信息工作是种什么体验？ - 知乎](https://www.zhihu.com/question/393732351)
        - [有没有大连华宇的同学，你们一般租房都在那块租，感谢交流！ - V2EX](https://www.v2ex.com/t/650286)
        - [大连有哪些比较值得去的软件公司? - 知乎](https://www.zhihu.com/question/29759447)
-
- ## 2023 春招
  background-color:: red
  -
-
- ## Conclusion
  - ### Wikis
    collapsed:: true
    - 编制
      mark:: 中华人民共和国各级机构编制管理机关核定的行政机构、事业单位的机构设置、人员数额和领导职数. 以及人民政府劳动行政部门核定的国有企业组织机构和人员数额. 分为**国家行政编制**、**事业编制**、**企业编制**三大类
      source:: [编制 - 维基百科，自由的百科全书](https://zh.wikipedia.org/zh-cn/%E7%BC%96%E5%88%B6); [长期看，编制还重要吗？ - 知乎](https://www.zhihu.com/question/356545782/answer/948511722)
      collapsed:: true
      - > 编制这个问题，如果大家都没有的话，无所谓，大家都是一样的，如果你身处在这样的大环境中，别人有而你没有，那你就感觉很不爽了
      - 编制 #vs 非编制
        collapsed:: true
        - 退休后有无正常的工资以及医疗、住房等保障
          编制基本属于事业单位，财政发工资, 无编制的主要是单位发工资
        - 大多无编制的学校教师是合同制，不享受各种待遇, 如**职称评选+奖金**等
        - PS:
          collapsed:: true
          - 现在大多私立学校都解决了这个问题，但是私立学校都是合同制，这就意味着随时可以淘汰你
    - HC (Head Count)
      mark:: 人头; 稍微专业点讲就是这家公司打算招的人数
    - Base地
      mark:: 基地、总部
      source:: [工作签约时说的base是什么意思_百度知道](https://zhidao.baidu.com/question/427575976.html)
      collapsed:: true
      - 总部在上海，假设 base 地点为A地
        - 按照公司的说法，**你们应该是和总部签订的合同，关系在上海，相当于上海某公司的员工，所以交社保在上海**；同时，你们的工作地点应该就安排在A地，相当于长期外派在A地工作
    - 应届毕业生
      mark:: "即将毕业, 但未拿到毕业证, 或已经停止学习，处于实习状态的; 拿到毕业证且时间不超过2年或三年择业期年限的 (超过则为往届生)"
      mark:: 白纸一张(背景调查+事业脱节+人品和能力都差+精力充足+婚育问题); 国家层面解决就业问题(12月国考+3-5月省考+事业单位招考/统考/人才引进);
      source:: [为什么应届生的身份这么值钱？ - 知乎](https://www.zhihu.com/question/296366864/answer/1735907342);  https://www.zhihu.com/question/296366864/answer/1321546761;
      collapsed:: true
      - 国家统一招生的普通高校毕业生离校时和在择业期内（国家规定择业期为二年，有些地方延长至三年）未落实工作单位、其户口、档案、组织关系保留在原毕业学校，或业生就业主管部门（毕业生就业指导服务中心）、各级人才交流服务机构和各级公共就业服务机构的毕业生，可按应届高校毕业生对待。
      -
    - 校园招聘 #vs 社会招聘
      collapsed:: true
      - 难度: 校园招聘 < 社会招聘
      - 找工作这事不能图省心省力
      - 应届生找工作本来就是体力活，不要觉得是浪费时间，能浪费你啥时间啊，不就是泡妞、睡觉、打lol的时间嘛，如果有1%的希望，就要投100份简历，如果只有1‰的希望，那就投1000份简历，别烦，总结经验、方法。
      - 前程无忧 / 智联招聘 / 大街网
      - via: [校园招聘还是社会招聘？ - 知乎](https://www.zhihu.com/question/36426108)
    - ~~考研~~
      collapsed:: true
      - [SSHeRun/CS-Xmind-Note: 计算机专业课（408）思维导图和笔记：计算机组成原理（第五版 王爱英），数据结构（王道），计算机网络（第七版 谢希仁），操作系统（第四版 汤小丹）](https://github.com/SSHeRun/CS-Xmind-Note)
      - http://www.cskaoyan.com/thread-80610-1-1.html
    - 劳务派遣公司 (低等外包) #outsourcing-dispatcher
      - 目的
        collapsed:: true
        - 促进就业
        - 意在规范临时性、辅助性与替代性的工作岗位制度。
      - 形式
        collapsed:: true
        - 完全派遣
        - 转移派遣
        - 减员派遣
    - 内推
      collapsed:: true
      - 速度
        collapsed:: true
        - 被看到和获得反馈的速度都会比非内推快一些
          collapsed:: true
          - **阿里的校园招聘甚至会直接给内推开快速通道提前面试和发通知**
      - 职位
        collapsed:: true
        - 内推简历质量通常比较高
          collapsed:: true
          - 如果内推就招到人了这个职位可能压根就不会发布到招聘网站上
      - 真实性
        collapsed:: true
        - 常年在招聘网站上挂一些职位看简历但并不急着招人
        - 内推的职位基本上都比较着急需要用人
      - 反馈更有可能
      - 坏处
        collapsed:: true
        - 同事考量
        - 公司派系
          collapsed:: true
          - 内推进入的团队就是默认的派系，如果这个团队在公司内部发展并不好，也会对之后的职业发展有相应的影响；
        - 短时间调换部门
          collapsed:: true
          - 如果内推的部门不是你最终想去的部门，过早换部门可能会得罪内推的人，落下不好的名声。
    - 三方协议
      collapsed:: true
      - 三方协议是企业，学生，学校三方之间就毕业事项达成的一项协议，严格来说，它属于一种要约，是具有法律效力的。
      - 一般来说，学校的就业率是通过三方协议的签订率来计算的。当然公务员，考研等也可以计入就业率之中。学校为了更好地达成就业率指标，就要尽可能安排学生在毕业季更多地参加校园招聘会来获得更多的签约。对于企业来说，校园招聘一般都希望招到正规学校正规毕业的大学生。与社会招聘不同，校园招聘有一个被学校认可的过程，没有三方协议的话，你的简历再漂亮也不能算作“应届毕业生”。对于学生来说，通过签订三方协议首先可以确定该公司是经过学校认可的正规公司，也就是说能签三方协议的公司不会是骗子。这一点有保障。注意是“三方”协议，也就是说学校企业和个人都是要承担责任的。
      - [三方协议到底是什么？对于应届生来讲，有哪些权利与义务？ - 知乎](https://www.zhihu.com/question/35895097/answer/65350485)
    - 劳务报酬税
      collapsed:: true
      - 劳务报酬所得、稿酬所得、特许权使用费所得，属于一次性收入的，以取得该项收入为一次；属于同一项目连续性收入的，以一个月内取得的收入为一次。
      - More in [个人所得税税率表（劳务报酬所得、稿酬所得、特许权使用费所得 2020年）_税屋——第一时间传递财税政策法规！](https://www.shui5.cn/article/7f/109610.html)
    - TODO 大学上学期间要不要跨省实习??
      collapsed:: true
      - [如何看待学校大四上学期不让去外地实习的事情？ - 知乎](https://www.zhihu.com/question/303431012)
      - [大四实习该去外地吗？ - 知乎](https://www.zhihu.com/question/271943273)
      - [大四上学期应该继续找实习还是参加校园招聘? - 知乎](https://www.zhihu.com/question/34513124)
  -
  - ### Judge Standards
    collapsed:: true
    - 世界企业 500 强
    - 中电科四小肥羊
      - 南京14所、合肥38所、成都29所、石家庄54所。
      - [中国电子科学研究院工作怎么样？ - 知乎](https://www.zhihu.com/question/38944380/answer/522961446)
  -
  - ### Sources
    collapsed:: true
    - [内蒙古大学就业信息网](https://imu.nmbys.cn)
    - [内蒙古24365大学生就业服务平台](https://www.nmbys.cn)
    - [秋招信息汇总，求职不孤单~](https://www.nowcoder.com/discuss/1055444)
    - [【2023秋招补录&春招】互联网招聘信息汇总4月26日更新_牛客网](https://www.nowcoder.com/discuss/438620729433780224)
    - [力扣夏令营 - 力扣（LeetCode）](https://leetcode.cn/circle/discuss/w35d6E/)
    - [内蒙古人才网,内蒙古招聘网,呼和浩特人才网,内蒙古人才招聘网](http://www.nmgzp.com/)
    - [校园招聘_应届大学生求职网_最新校园招聘信息-智联招聘官网](https://xiaoyuan.zhaopin.com/)
    - outdated
      collapsed:: true
      - [CyC2018/Job-Recommend: 🔎 互联网内推信息（社招、校招、实习）](https://github.com/CyC2018/Job-Recommend)
        - 精通编程语言
  -
  - ### Written Exam
    collapsed:: true
    - 截至面试结束, 我数了一下, 纸的边缘横七竖八躺着重复的四句话, "我是傻逼", 不知道这是第几次面试了, 但这简短的评价了我整个大学的四年生活, 其实也没有多少波澜, 就像正常人过日子一样, 平平淡淡的大学四年, 没有什么
    - Interview
      - ToString 是多态吗
    - Java
      - 选择
        - 阅读程序
          collapsed:: true
          - `i=i++`
            - ```java
              public class Solution {
                  public static void main(String[] args) {
                      Solution so = new Solution();
                      int i = 0;
                      so.fermin(i);
                      i = i++;
                      System.out.println(i);
                  }
                  void fermin(int i){
                      i++;
                  }
              }
              ```
              - `x++` increments `x` and returns its old value.
              - `x =` assigns the old value back to itself.
              - via: [java - What is x after "x = x++"? - Stack Overflow](https://stackoverflow.com/questions/7911776/what-is-x-after-x-x)
                more: [理解在java “”i=i++;”所发生的事情_个人文章 - SegmentFault 思否](https://segmentfault.com/a/1190000015858080)
              - Result: `0`
        - [[jvm]]
          - 以下哪项不属于java类加载过程？
            - 执行static块代码
            - 类方法解析
            - 生成java.lang.Class对象
            - int类型对象成员变量赋予默认值
      - 编程
        - 金额数字转换大写
          collapsed:: true
          - via: [java 金额数字转换大写算法 - 问北 - 博客园](https://www.cnblogs.com/ibigboy/p/10980861.html)
          - ```java
              public class MoneyToChiness{
                public static void main(String[] args) {
                    long l = System.currentTimeMillis();
                    System.out.println(MoneyToChiness.moneyToChinese(new BigDecimal("999999999999.99")));
                    System.out.println(System.currentTimeMillis()-l);
                }
                public static String moneyToChinese(BigDecimal i_money) {
                    if(i_money.equals(BigDecimal.ZERO)){
                        return "零圆整";
                    }
                    Double max = 1000000000000D;
                    Double min = 0.01D;
                    if (i_money.doubleValue() >= max  || i_money.doubleValue() < min) {
                        return "大于1万亿或小于1分了";
                    }
                    i_money = i_money.setScale(2, RoundingMode.HALF_UP);
                    String numStr = i_money.toString();
                    int pointPos = numStr.indexOf('.');
                    //整数部分
                    String s_int = null;
                    //小数部分
                    String s_point = null;
                    if (pointPos >= 0) {
                        s_int = numStr.substring(0, pointPos);
                        s_point = numStr.substring(pointPos + 1);
                    } else {
                        s_int = numStr;
                    }
                    StringBuilder sb = new StringBuilder();
                    if(!"0".equals(s_int)){
                        int groupCount = (int) Math.ceil(s_int.length() / 4.0);
                        for (int group = 0; group < groupCount; group++) {
                            boolean zeroFlag = true;
                            boolean noZeroFlag = false;
                            int start = (s_int.length() % 4 == 0 ? 0 : (s_int.length() % 4 - 4)) + 4 * group;
                            for (int i = 0; i < 4; i++) {
                                if (i + start >= 0) {
                                    int value = s_int.charAt(i + start) - '0';
                                    if (value > 0) {
                                        sb.append(CN_UPPER_NUMBER[value]);
                                        if (i < 3) {
                                            sb.append(CN_UPPER_UNIT[i]);
                                        }
                                        zeroFlag = true;
                                        noZeroFlag = true;
                                    } else if (zeroFlag) {
                                        sb.append('零');
                                        zeroFlag = false;
                                    }
                                }
                            }
                            if(sb.charAt(sb.length() - 1) == '零'){
                                sb.deleteCharAt(sb.length() - 1);
                            }
                            if(noZeroFlag || groupCount - group == 1){
                                sb.append(CN_GROUP[groupCount - group - 1]);
                            }
                        }
                    }
                    if (s_point == null || "00".equals(s_point)) {
                        sb.append('整');
                    }else{
                        int j = s_point.charAt(0) - '0';
                        int f = s_point.charAt(1) - '0';
                        if(j > 0){
                            sb.append(CN_UPPER_NUMBER[j]).append('角');
                            if(f != 0){
                                sb.append(CN_UPPER_NUMBER[f]).append('分');
                            }
                        }else if("0".equals(s_int)){
                            sb.append(CN_UPPER_NUMBER[f]).append('分');
                        }else {
                            sb.append('零').append(CN_UPPER_NUMBER[f]).append('分');
                        }
                    }
                    return sb.toString();
                }
                private static final char[] CN_UPPER_NUMBER = "零壹贰叁肆伍陆柒捌玖".toCharArray();
                private static final char[] CN_UPPER_UNIT = "仟佰拾".toCharArray();
                private static final char[] CN_GROUP = "圆万亿".toCharArray();
            }
            ```
            -
    - 百一测评 by 蒙泰集团
      - Spring 包装 Hibernate 之后的Hibernate的DAO应该继承 {{cloze HibernateDaoSupport}} 类
        collapsed:: true
        - `public abstract class HibernateDaoSupport extends DaoSupport`
          - Convenient superclass for Hibernate-based data access objects.
          - Requires a [`SessionFactory`](https://docs.jboss.org/jbossas/javadoc/7.1.2.Final/org/hibernate/SessionFactory.html) to be set, providing a [`HibernateTemplate`](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/orm/hibernate5/HibernateTemplate.html) based on it to subclasses through the [`getHibernateTemplate()`](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/orm/hibernate5/support/HibernateDaoSupport.html#getHibernateTemplate()) method. Can alternatively be initialized directly with a HibernateTemplate, in order to reuse the latter's settings such as the SessionFactory, exception translator, flush mode, etc.
          - This class will create its own HibernateTemplate instance if a SessionFactory is passed in. The "allowCreate" flag on that HibernateTemplate will be "true" by default. A custom HibernateTemplate instance can be used through overriding [`createHibernateTemplate(org.hibernate.SessionFactory)`](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/orm/hibernate5/support/HibernateDaoSupport.html#createHibernateTemplate(org.hibernate.SessionFactory)).
          - [HibernateDaoSupport (Spring Framework 6.0.7 API)](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/orm/hibernate5/support/HibernateDaoSupport.html)
      -
  -
  - ### [[interview]]
    collapsed:: true
    - 0. 自我介绍 | Elevator Pitch
      - Elevator Pitch | 电梯游说
        collapsed:: true
        - More via: [Elevator pitch - Wikipedia](https://en.wikipedia.org/wiki/Elevator_pitch)
        - {{video https://www.youtube.com/watch?v=Lb0Yz_5ZYzI}}
      - ```
        (xxx) 的面试官您好, 首先谢谢您今天面试我.
        我就读 (内蒙古) 大学的 (软件工程) 专业，目前 (大四) 在读
        我曾 1 次获得校奖学金, 刚入学也有参与一些大学的组织, 有过和别人一起举办活动的经验.
        也参加过几次竞赛, 获得了满意的名次.
        主修课程有数据结构与算法, 计网, 设计模式, 以及软件过程的相关理论.
        课余时间关注国内外先进的技术, 虽然就读计算机, 但也有户外运动的爱好
        我希望面试贵公司的 (xxx) 岗位, 希望面试官多考验考验我.
        最后再次谢谢您, 我简单的介绍就大致是这些, 谢谢.
        ```
    - 1. 深挖项目
      - 说说你简历上面的项目, 去梳理梳理你做这个东西的思路
      - 你用到的设计模式
      - 你设计的数据库表
      - 你项目中用到的加密技术, 遭到攻击怎么办法?
      - 去做一点压力测试, 更简单的理财系统和我的秒杀系统相比到底差在哪???
      - 少一点并发造假的知识 !!!
      - 整个项目用到的架构模式等等
    - 2. [[java]] 基本面试的 八股文
      - 内/外模式
      - 索引
      - 经典的 Sql 问题, 刷 Leetcode!! 打印!!
      - 容器的部署, 打包等等问题???
    - 3. 性格问题
      - 闹矛盾, 抗压, 不顺?
      - 传统软件行业 / 互联网行业?
      - 总包是什么?
      - 传统软件开发 vs 互联网软件开发
        collapsed:: true
        - [传统行业码农想跳槽互联网需要熟知哪些技能 - V2EX](https://cn.v2ex.com/t/714471)
      - 你为什么来这个城市工作而不回家乡呢？
        collapsed:: true
        - [面试官问：你为什么要到这个城市工作呢？](https://www.bilibili.com/video/BV1m64y1S7tZ)
          collapsed:: true
          - {{video https://www.bilibili.com/video/BV1m64y1S7tZ}}
        - ❌ 心血来潮
        - ❌ 父母左右, 照顾
        - ✔ 城市发展多
        - ✔ 自己做过很多城市的调查和职业规划
        - ✔ 希望长期发展
        - ✔ 机会多
        - ✔ 男女朋友 -> 谈婚论嫁
        - More via
          collapsed:: true
          - [面试最容易被刷的题：你为什么来这个城市工作而不回家乡呢？ - 知乎](https://zhuanlan.zhihu.com/p/32814546?utm_id=0)
          - [面试官问“为什么应聘这个岗位”，应该如何回答？_校招VIP的博客-CSDN博客_为什么要应聘这个岗位的回答](https://blog.csdn.net/shuize123/article/details/124348932)
    - 4. 我需要发问的几个问题:
      - 工作的性质是什么? 我日常的任务是什么?
      - 工资的成分是什么? 绩效整体占比是多少?
    - Prepared Progress
      - [[cv]]
      - [[java]] 开发(后端) [[roadmap/develop]]
        - [[java multithreading]] 学习
          - **synchronized**
          - **LockSupport**
          - **yield + 原子类**
          - **ReentrantLock + Condition**
          - **ReentrantLock + Condition**
          - **Semaphore**
          - **SynchronousQueue**
          - **LinkedBlockingQueue**
            - 使用 **BlockingQueue** 的其他子类，也可以类似的解出来
          - **CyclicBarrier**
          - **Exchanger**
          - **Phaser**
          - **CountDownLatch**
        - 并发
        - [[Spring]]
          - Spring 官方教程
        - [[Spring Boot]]
        - 看到的几套很好的教程
          - [KuangStudy](https://www.kuangstudy.com/course)
            collapsed:: true
            - Java常用类学习
            - 集合框架详解
            - I/O详解
            - 多线程详解
            - 网络编程详解
            - 注解和反射
            - JUC并发编程
            - JVM深入研究
            - ---
            - ==JavaWeb==
            - HTTP协议详解
            - Servlet详解
            - Cookie/Session
            - Filter过滤器
            - 监听器详解
            - 原生Web应用开发
            - ---
            - ==微服务开发==
            - ---
            - Linux-==Nginx详解==
            - Jenkins详解
            - Kubernetes详解
            - ---
            - ==常用中间件==
            - Redis详解
            - ElasticSearch
            - RabbitMQ详解
            - Kafka详解
            - MyCat详解
            - ShardingJDBC
            - ---
            - ==企业常用第三方技术==
            - POI技术详解
            - 第三方短信接入
            - 视频点播技术
            - 视频直播技术
            - CDN技术介绍
            - 第三方登录技术
            - 第三方支付技术
            - ---
            - ==源码探究、设计模式学习==
            - Dubbo源码分析
            - Netty源码分析
      - 计算机基础
        - [[algo]]
          - [greyireland/algorithm-pattern: 算法模板，最科学的刷题方式，最快速的刷题路径，你值得拥有~](https://github.com/greyireland/algorithm-pattern)
        - [[os]]
        - [[networking]]
        - [[database]]
        - [[frameworks]]
        - [[software/pattern]]
        - [[leetcode]]
        - [[Book]]
      - More
        - MBTI-Results
          - 人格类型
            collapsed:: true
            - **INFJ**
          - 职业推荐
            collapsed:: true
            - **教育家,园林设计师,心理咨询师,诗人**
          - 最佳拍档
            collapsed:: true
            - ENFP
          - “提倡者”人格
            collapsed:: true
            - > 坚持意志伟大的事业需要矢志不渝的精神。
              ——伏尔泰
            - “故立志者，为学之心也；为学者，立志之事也”，如王阳明一般，提倡者们生活在思想的世界。你是独立的、有独创性的思想家，具有强烈的感情、坚定的原则和正直的人性。即使面对怀疑，背负重压，你仍相信自己的看法与决定。你的评价高于其他的一切，包括流行的观点和存在的权威，这种内在的观念激发着你的积极性。通常提倡者具有本能的洞察力，能够看到事物更深层的含义。即使他人无法分享你的热情，但灵感因对于你重要而令人信服。
            - 提倡者忠诚、坚定、富有理想化。你珍视正直，十分坚定以至达到倔强的地步。因为你的说服能力，以及那些对公共利益最有利且清晰的看法，所以提倡者会成为伟大的领导者。由于你的贡献，通常会受到他人的尊重或尊敬。
          - 只有在人群中间，才能认识自己
            collapsed:: true
            - 因为珍视友好和和睦，提倡者喜欢说服别人，使之相信你的观点是正确的。通过运用嘉许和赞扬，而不是争吵和威胁，赢得了他人的合作。你愿意毫无保留地激励同伴，避免争吵。通常提倡者是深思熟虑的决策者，你认为问题使人兴奋，在行动之前你通常要仔细地考虑。你喜欢每次全神贯注于一件事情，这会造成一段时期的专心致志。
            - 满怀热情与同情心，你强烈地渴望为他人的幸福做贡献。你是注意其他人的情感和利益，能够很好地处理复杂的人。提倡者本身具有深厚复杂的性格．既敏感又热切。你内向，很难被人了解，但是愿意同自己信任的人分享内在的自我。你往往有一个交往深厚、持久的小规模的朋友圈，在合适的氛围中能产生充分的个人热情和激情。
          - More
            collapsed:: true
            - [“提倡者” 人格 (INFJ) | 16Personalities](https://www.16personalities.com/ch/infj-%E4%BA%BA%E6%A0%BC)
            - [INFJ - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/INFJ)
      - [[bank]]
      - [[job/civil-service]]
  -
  - ### Special: [[programming]] #learning #roadmap/develop
    -
    - TODO  Java exercise;
      SCHEDULED: <2024-03-11 Mon 00:00 .+1d>
      - [Nowcoder](https://www.nowcoder.com/)
        logseq.order-list-type:: number
      - [LeetCode](https://leetcode.cn/problemset/all/)；
        logseq.order-list-type:: number
        collapsed:: true
        - [Java算法模板_牛客博客](https://blog.nowcoder.net/zxc/90706)
        - [labuladong/fucking-algorithm: 刷算法全靠套路 ](https://github.com/labuladong/fucking-algorithm) ![](https://img.shields.io/github/stars/labuladong/fucking-algorithm)
        - [geekxh/hello-algorithm: 🌍 针对小白的算法训练 | 包括四部分：①.大厂面经 ②.力扣图解 ③.千本开源电子书 ④.百张技术思维导图（项目花了上百小时，希望可以点 star 支持，🌹感谢~）点击下方网站，马上开始刷题！](https://github.com/geekxh/hello-algorithm) ![](https://img.shields.io/github/stars/geekxh/hello-algorithm)
        - [halfrost/LeetCode-Go: ✅ Solutions to LeetCode by Go, 100% test coverage, runtime beats 100% / LeetCode 题解](https://github.com/halfrost/LeetCode-Go) ![](https://img.shields.io/github/stars/halfrost/LeetCode-Go)
        - [chefyuan/algorithm-base 立志用动画将算法说的通俗易懂](https://github.com/chefyuan/algorithm-base) ![](https://img.shields.io/github/stars/chefyuan/algorithm-base)
          collapsed:: true
          - [algorithm-base/BF算法.md at main · chefyuan/algorithm-base](https://github.com/chefyuan/algorithm-base/blob/main/animation-simulation/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E5%92%8C%E7%AE%97%E6%B3%95/BF%E7%AE%97%E6%B3%95.md?plain=1)
          - [algorithm-base/KMP.md at main · chefyuan/algorithm-base](https://github.com/chefyuan/algorithm-base/blob/main/animation-simulation/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E5%92%8C%E7%AE%97%E6%B3%95/KMP.md)
        - [dairongpeng/algorithm-note 数据结构与算法的讲解及代码实现](https://github.com/Dairongpeng/algorithm-note) ![](https://img.shields.io/github/stars/Dairongpeng/algorithm-note)
        - [krahets/LeetCode-BookLeetBook 图解算法数据结构 配套代码仓](https://github.com/krahets/LeetCode-Book) ![](https://img.shields.io/github/stars/krahets/LeetCode-Book)
        - [dunwu/algorithm-tutorial: 算法和数据结构教程](https://github.com/dunwu/algorithm-tutorial) ![](https://img.shields.io/github/stars/dunwu/algorithm-tutorial)
      - Interview；
        logseq.order-list-type:: number
        collapsed:: true
        - [[java]] / [[Spring]] / [[networking]]
        - [[nowcoder/review_java]]
        - [Java校招面试题目合集_Java工程师/Java开发_牛客网](https://www.nowcoder.com/ta/review-java)
        - [[BV17K411Z7EB]] Spring 面试题
        - [DreamCats/java-notes: 自己的学习笔记。包含：个人秋招经历、🐂客面经问题按照频率总结、Java一系列知识、数据库、分布式、微服务、前端、技术面试、每日文章等(持续更新)](https://github.com/DreamCats/java-notes)![](https://img.shields.io/github/stars/DreamCats/java-notes)
        - [CyC2018/CS-Notes: 技术面试必备基础知识、Leetcode、计算机操作系统、计算机网络、系统设计](https://github.com/CyC2018/CS-Notes) ![](https://img.shields.io/github/stars/CyC2018/CS-Notes)
        - [hadyang/interview: Java 笔试、面试 知识整理](https://github.com/hadyang/interview) ![](https://img.shields.io/github/stars/hadyang/interview)
        - [[Snailclimb/JavaGuide]]
        - [doocs/advanced-java Java 工程师进阶知识完全扫盲](https://github.com/doocs/advanced-java) ![](https://img.shields.io/github/stars/doocs/advanced-java)
        - [AobingJava/JavaFamily](https://github.com/AobingJava/JavaFamily) ![](https://img.shields.io/github/stars/AobingJava/JavaFamily)
        - [DuGuQiuBai/Java: 27天成为Java大神](https://github.com/DuGuQiuBai/Java) ![](https://img.shields.io/github/stars/DuGuQiuBai/Java)
        - [singgel/JAVA 存放JAVA开发的设计思想、算法](https://github.com/singgel/JAVA) ![](https://img.shields.io/github/stars/singgel/JAVA)
          collapsed:: true
          - 《剑指Offer》、《编程珠玑》、《深入理解Java虚拟机：JVM高级特性与最佳实践》、《重构-改善既有代码的设计 中文版》、《clean_code(中文完整版)》、《Java编程思想(第4版)》、《Java核心技术 卷I (第8版)》、《Quartz_Job+Scheduling_Framework》
        - [hansonwang99/JavaCollection](https://github.com/hansonwang99/JavaCollection) ![](https://img.shields.io/github/stars/hansonwang99/JavaCollection)
        - [[EN] learning-zone/Java Interview Questions ( v8 )](https://github.com/learning-zone/java-interview-questions) ![](https://img.shields.io/github/stars/learning-zone/java-interview-questions)
        - [CyC2018/CS-Notes: 技术面试必备基础知识、Leetcode、计算机操作系统、计算机网络、系统设计](https://github.com/CyC2018/CS-Notes) ![](https://img.shields.io/github/stars/CyC2018/CS-Notes)
        - [介绍 | Java面试之旅](https://heiye.site/java-interview/)
        - [18-尚硅谷-Web-CS和BS的异同点_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1AS4y177xJ/?p=18)
        - [20-e.target和this区别_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1k4411w7sV/?p=64)
        - [053-api-java-同步异步接收结果_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Tt4y1772f/?p=39)
        - [尚硅谷__JavaWeb全套教程2020__哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Y7411K7zz)
        - [Java学到什么水平能够出去找工作！！_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1TK4y187Ak/)
        - [【手写Spring】手写Spring介绍_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1r5411A7hZ)
        - [前阿里大佬带你深入JVM字节码执行引擎_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1gv411678m/)
        - [【Java并发】并发编程的意义是什么？月薪30K必知必会的Java AQS机制_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV12K411G7Fg/)
        - [[Java编程思想]] | JDK 5/6,  有点太老了  Σ( ° △ °|||
        - [[mooc/javaee]]
        - [[geekbang/Java核心技术]]
    - TODO Submit [[cv]];
    - DOING [[books/spring in action]] daily until you done;
      :LOGBOOK:
      * State "DONE" from "TODO" [2023-05-05 Fri 21:14]
      * State "DONE" from "TODO" [2023-05-06 Sat 17:51]
      * State "DONE" from "TODO" [2023-08-21 Mon 23:54]
      :END:
    - Second citizens (Font-End);
      collapsed:: true
      - [qianguyihao/Web: 千古前端图文教程，超详细的前端入门到进阶知识库。从零开始学前端，做一名精致优雅的前端工程师。](https://github.com/qianguyihao/Web) ![](https://img.shields.io/github/stars/qianguyihao/Web)
      - [ftTony/learning-map: 前端知识思维导图](https://github.com/ftTony/learning-map)![](https://img.shields.io/github/stars/ftTony/learning-map)
      - [CavsZhouyou/Front-End-Interview-Notebook: 前端面试复习笔记](https://github.com/CavsZhouyou/Front-End-Interview-Notebook) ![](https://img.shields.io/github/stars/CavsZhouyou/Front-End-Interview-Notebook)
      - 学会用 [[Javascript]] 爬虫
        collapsed:: true
        - [使用JavaScript写爬虫 - 知乎](https://zhuanlan.zhihu.com/p/53763115)
    - Pass the verify;
      collapsed:: true
      - PAT 考试
        collapsed:: true
        - ACM/pat顶级(大一大二可以考乙级和甲级练练手，大三考完顶级，名次越高面试越稳)/蓝桥/ccf+开源
        - ccf csp 没有用, 直接去刷 PTA. via: [想问下Ｖ友， ccf csp 考试含金量如何？企业认可度如何？ - V2EX](https://v2ex.com/t/306204)
      - 微软认证考试、Adobe认证考试、Oracle认证（OCA证书、OCP证书、OCM证书）、JAVA认证、Cisco认证等+华为认证+计算机技术与软件专业资格考试证书+思科认证+微软认证
      - 全国计算机等级考试（NCRE)和中国计算机技术职业资格网(软考)高级
      - PMP考试
  -
  - ### Special: [[bank]]
    collapsed:: true
    - [[China]] #.ol
      - 中国建设银行——CCB(China Constuction Bank)
      - 中国农业银行——ABC(Agricultural Bank of China)
      - 中国工商银行——ICBC(Industrial and Commercial Bank of China)
      - 中国银行——BOC（Bank of China)
      - 中国民生银行 ——CMBC（China Minsheng Banking Co. Ltd）
      - 招商银行 ——CMB(China Merchants Bank Ltd)
      - 兴业银行 ——CIB (Industrial Bank Co.， Ltd)
      - 北京银行——BOB(Bank of Beijing)
      - 交通银行——BCM(Bank of Communications)
      - 中国光大银行——CEB(Chiana Everbright Bank)
      - 中信银行——(China CITIC Bank)
      - 广东发展银行——GDB(Guangdong Development Bank)
      - 上海浦东发展银行——SPDB/SPDBank(Shanghai Pudong Development Bank)
      - 深圳发展银行——SDB(Shenzhen Development Bank)
    - 工商银行 准备
      collapsed:: true
      - 考情
        - 概况
          collapsed:: true
          - 840101，中国工商银行正式成立；
          - 051028，整体改制为股份有限公司；
          - 061027，成功在上交所和香港联交所同日挂牌上市。
        - 考情分析
          collapsed:: true
          - 行测题量分布
            collapsed:: true
            - 资料分析 1
            - 逻辑推理 26
            - 数量关系 32
            - 言语理解 18
      - 准备面试题
        - 介绍一下你自己?
          collapsed:: true
          - ```shell
            工商银行 的面试官您好, 首先谢谢您今天面试我.
            我就读 (内蒙古) 大学的 (软件工程) 专业，目前 (大四) 在读
            主修课程为计算机相关理论与开发, 我曾 1 次获得校奖学金, 曾有 1 次远程实习经历
            也参加过几次竞赛, 获得了满意的名次.
            在大一刚入学也有参与一些校组织, 有过和别人一起举办活动的经验.
            课余时间关注国内外先进的技术, 虽然就读计算机, 但对金融, 经济学比较感兴趣
            我希望面试贵公司的 科技菁英 岗位, 希望面试官多考验考验我.
            最后再次谢谢您, 我简单的介绍就大致是这些, 谢谢.
            ```
        - 对工行的了解
          collapsed:: true
          - 中国工商银行股份有限公司 (Industrial and Commercial Bank of China，缩写：ICBC). 简称工商银行、工行，成立于1984年1月1日，是中国大陆五大国有商业银行之一，总部设在北京市，由中国人民银行的工商信贷和储蓄业务分离而设立，为中国大陆最大的银行
          - 文化
            - 使命：提供卓越金融服务：服务客户、回报股东、成就员工、奉献社会。
            - 愿景：建设最盈利、最优秀、最受尊重的国际一流现代金融企业。
            - 价值观：工于至诚，行以致远。诚信、人本、稳健、创新、卓越。
          -
          - 成就
            collapsed:: true
            - 福布斯, 银行家, 财富 名列前茅
            - 2020年9月28日，入选2020中国企业500强榜单，排名第5
            - 2022, 入选《福布斯》2022年全球区块链50强榜单
          - 业务范围:
            collapsed:: true
            - 公司金融业务
            - 个人金融业务
            - 资产管理业务
            - 金融市场业务
          - via
            collapsed:: true
            - [中国工商银行 - 维基百科，自由的百科全书](https://zh.wikipedia.org/zh-cn/%E4%B8%AD%E5%9B%BD%E5%B7%A5%E5%95%86%E9%93%B6%E8%A1%8C)
            - [中国工商银行_百度百科](https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%B7%A5%E5%95%86%E9%93%B6%E8%A1%8C/283912)
        - 假如你入职后，遇到了重重困难，业务不熟悉，工作不顺心，你怎么办？
          collapsed:: true
          - 关键词：入职后、业务不熟悉、工作不顺心
            解题思路：
              * 思想上：正常现象
              * 行动上：
                * 工作方面：提升专业技能
                * 人际关系方面：主动融入
          - 作为刚入职的新人，难免会遇到业务不熟悉、工作不顺心等困难。这时，我会正视目前的状态，调整好心态，积极融入同事中，通过自己努力改变这种情况。
          - 首先，我会加强业务上的学习，努力提升业务水平。尽快熟悉工作制度和工作流程，熟悉相关业务的操作，让客户满意；
          - 其次，我会虚心向有经验的同事请教，学习工作上的方法和技巧，用心尝试，注意总结，让同事认可我。
          - 最后，我也会积极融入同事，让大家了解我，互相熟悉，和同事处好关系。通过这些努力，我一定会克服重重困难，最终适应环境，很好地完成工作。
        - 你所在的银行要开展一次“送金融知识下乡”活动，领导让你来负责，你会重点做好哪些工作？
          collapsed:: true
          - 关键词：送金融知识下乡、负责
            解题思路：
            * 目标：普及金融知识、展现我行整体精神面貌
            * 具体执行：
              * 对象：
                * 农民，因此在资料的准备上要尽可能的通俗易懂，多采用图片的形式，吸引注意力。在介绍银行推出的产品的时候要严谨细致，表达要通俗易懂。
                * 员工：进行培训。
              * 宣传方式：
                * 迎合农民喜好。现场宣讲的形式来讲解金融政策，并设置问答环节，回答银行常见的问题。活动现场布置可以弄一些特别引人注目的横幅，写上显眼的标语，例如“银行送金融知识下乡咨询服务”。
                * 联系媒体予以报道，提高我行本次活动的影响力。
              * 应急预案：考虑一切可能发生的突发状况
          - “送金融知识下乡”活动不但对银行的未来发展具有重大的影响和意义，同时也是展现我行整体精神面貌的好机会。
          - 这次活动的重点工作有：
          - 第一，宣传的内容一定要符合活动对象的需求，要有针对性。这次面对的是农民朋友，相对来说整体文化水平偏低，因此在资料的准备上要尽可能的通俗易懂，多采用图片的形式，吸引注意力。在介绍银行推出的产品的时候要严谨细致，表达要通俗易懂。
          - 第二，宣传方式要迎合农民喜好。农民朋友比较喜欢热闹，可以采用现场宣讲的形式来讲解金融政策，并设置问答环节，回答银行常见的问题。活动现场可以布置一些特别引人注目的横幅，写上显眼的标语，例如“银行送金融知识下乡咨询服务”。
          - 第三，对所有参与宣传的员工统一培训，展现银行良好的精神面貌。参与活动的银行员工统一佩戴绶带，上面写明“银行欢迎您”。农民朋友都很淳朴，老实，因此在向过往农民朋友发放宣传单页的时候要更加主动热情，面带微笑。
          - 第四，提前制定应急预案，考虑一切可能发生的突发状况，对农民朋友的问题要认真答疑解惑，耐心的介绍。还可以联系媒体予以报道，提高我行本次活动的影响力。相信做好以上几点一定可以将本次活动办好，给农民朋友送去福音，让农民朋友真正的了解到金融知识对生活的重要性。
        - 有些突如其来的变化会彻底改变你的计划和安排，请谈谈你在这方面印象最深刻的一次经历。
          collapsed:: true
          - 关键词：
            * 经历、改变计划和安排解题思路：
            * STAR
              T：任务 S：背景 A：行为 R：结果／收获
          - 人生在世，世事无常，总会有些突如其来的事情发生，在这样的情况下，总会带来些改变。
          - 我是在距离家1000多公里外的广州读的研究生，3年来我按照自己的计划努力学习，在毕业前的2月份找到了工作，和坐落在该市的知名企业签订了就业协议。但是，就在我等待毕业答辩，对未来憧憬着的时候，一场突如其来的变故发生了，父亲突然去世了，母亲身体还不好，而我作为家里的长子，我觉得不能再离家这么远了，亲情需要温暖，家人需要我照顾，我当时心理挣扎了很久，因为找到的那份工作我的确很喜欢，导师也是大力推荐。但是，最终我还是选择了放弃，改变了自己的计划，回到了家乡。
          - 我并不后悔，毕竟我相信是金子一定能发光，在哪都能实现我的价值。同时，回到了家乡，我对于周围的环境也都很熟悉，还能尽心照顾家人，这样的改变也是很好的。
        - 请用不超过30个字给出一个最能让我们录用你的理由
          collapsed:: true
          - 关键词：最、30
            解题思路：
              * 曾多次在银行实习，业务操作熟练，能快速胜任工作。
              * 学习能力强，能快速适应和胜任岗位
            * 营销能力强，最高单笔营销5万元
          - 曾多次在银行实习，业务操作熟练，能快速胜任工作。
        - 最近你单位来了一批实习生，领导安排你组织一次实习生培训，你认为培训的重点内容是什么？并简单说明理由。
          collapsed:: true
          - 关键词：培训、实习生
            解题思路：
            * 目标：熟悉单位文化和规章制度、适应单位的人际关系和氛围，更快地为单位做出成绩。
            * 具体执行：
              * 单位文化和制度的宣讲
              * 工作技能的专业培训
              * 人际关系和团队合作意识
          - 在一个组织之中，实习生是最新鲜的血液，能给团队带来活力和热情，同时也是工作上的新手，免不了出现各个方面的问题。因此对初次进入职场的实习生进行培训，有助于实习生熟悉单位文化和规章制度、适应单位的人际关系和氛围，更快地为单位做出成绩。我会将培训的重点内容放在以下三个方面：
          - 一是单位文化和制度的宣讲。对单位文化的认同能够让新人产生荣誉感和归属感，让新人与单位的关系更加紧密，因此可以请单位的分管领导对实习生进行宣讲，帮助他们更好地了解我们的单位文化和规章制度。
          - 二是工作技能的专业培训。专业的技能和素质是独立工作能力的基础，也是每个新人必备的能力。培训形式主要是由各部门的资深员工给实习生们就本岗位的职责和工作要求进行讲解，并安排一些小测试，让实习生们巩固工作内容。
          - 三是团队合作意识。就工作中人际关系的一些特点对实习生们进行讲解，将实习生分为几个小组，安排他们共同完成任务，增进动手能力，加强沟通交流，让他们在分工、协作和解决问题的过程中，相互了解，增进团队成员间的感情，学会与他人合作，培养团队精神，可以使我们的工作更加良好地向前发展。
        - 你接到客户非常紧急的需求，你不会；你想找人请教，却发现别的同事都很忙，对你爱搭不理，你怎么办呢？
          collapsed:: true
          - 关键词:紧急需求、求人帮忙
            解题思路：
            * 安抚下他的心情，环节客户焦急的情绪
            * 找平时关系较好或者较好说话的同事认真听取同事指点
            * 按照相关内容帮助客户处理
            * 向同事感谢，加强业务学习。
          - 考虑到客户的业务需求非常紧急，我会先安抚下他的心情，向他告知我已了解他的需求，但我需要同事的协助，因此请他先稍等片刻，我会尽快处理好。同时，示意大堂值班的同事帮我接待一下，缓解客户焦急的情绪。
          - 虽然同事都很忙，对我爱搭不理，但是考虑到当前的情况，我还是要尽最大的努力寻求同事的帮助，尽快为客户办理业务。我会找平时关系较好或者较好说话的同事，借他工作的空档抓紧时间说明情况，承认自己平时没好好注意学习相关业务，希望同事可以给予帮助。仔细认真听取同事指点后，按照相关内容帮助客户处理，使客户可以对办理的结果满意。
          - 事后，我会在工作休息时间找到给予我帮助的同事，再次向他表示感谢。而我也会向这位同事学习，在别人遇到问题向我寻求帮助时，尽最大能力给予帮助。同时，我会认真吸取经验教训，加强业务学习，避免因为不懂业务而耽误客户和同事的时间。
        - 你为什么选择来银行工作
          collapsed:: true
          - 银行业是金融体系的基石 需求广泛
          - 银行一直伴随时代的发展转型 成长非常快
          - 自己的专业或者性格与面试的某某岗位匹配
          - 父母或者亲近的学长学姐在银行工作, 能够感受到银行业是一个非常好的职业发展方向
        - 你觉得我们的缺点是什么? (确定宽泛了说)
          collapsed:: true
          - 疫情下减少人员流动, 简化业务流程, 增加智能终端
          - 手机银行细化客群, 提升用户体验
        - 互联网银行(支付宝的冲击)
          collapsed:: true
          - 既是机遇, 又是挑战
          - 冲击, 倒逼传统技术创新和流程简化, 但是银行立足于规模和资本还是有巨大的优势的, 能够为客户提供一整套金融服务方案, 后续应该进一步延申金融服务链条, 抓住大数据时代的机遇, 让金融服务无处不在, 增强客户粘性
        - 如何转型发展
          collapsed:: true
          - 金融科技赋能业务发展, 在基本业务上发展金融产品多样化, 个性化, 以客户为中心, 围绕客户需求, 将金融服务嵌入客户生活,
          - 去人工化, 用智能网点, 线上渠道代替线下网点
        - **怎么看待你投递的岗位**
          collapsed:: true
          - 柜员
            - 了解柜员的主要职责是办理客户的柜面业务, 需要有过硬的专业素质, 而且是直接面向客户群体的, 代表了银行的形象, 需要具备良好的服务能力和服务态度
          - 客户经理
            - 银行的产品和服务接触市场和客户的重要桥梁, 需要具备过硬的营销能力, 还有对业务知识的精准把控等等.
          - 后台
            - ...
        - 你和这个岗位的匹配度高吗
          collapsed:: true
          - 前台
            - 服务能力
            - 抗压能力
            - 营销能力
            - 客户至上, 亲和力, 沟通能力
          - 后台
            - 专业知识的储备
            - 实习经历
        - 实习经历
          collapsed:: true
          - 银行实习> 金融类非银行实习 == 其他行业同岗位实习 > 其他行业不同岗位实习 > 无实习
        - 超出你能力范围之外的事情, 怎么办
          collapsed:: true
          - 把这件事情当作是对我自己的磨练, 以及积累工作经验的好机会
          - 首先梳理工作思路，并冷静思考完成这项工作我还需要什么支持，技术or资源or时间or人力
          - 其次，通过查询资料、寻求同事帮助、学习同行先进经验等方式来补上缺失的能力
          - 第三，及时向领导反馈工作进展并向领导申请资源
        - 如果安排你长期做重复的工作，你会怎么做
          collapsed:: true
          - 首先，我会认真完成领导给我安排的工作，这是我的职责
          - 其次，我会保持学习的心态，每一次做完都要有进步，提升效率；
          - 第三，我会在完成工作之余积极寻找挑战自我的机会，为自己争取一些更有难度的工作，保持自我提升）
        - 你有其他的offer吗?
          collapsed:: true
          - 可以回答暂时还没有，有几家公司还在终面环节，也可以回答手里有一个其他offer，但一定要突出说明即使有其他的也会坚定的选这家银行，把它的优点结合你的找工作标准去说，比如自己更偏向于什么样的成长节奏，希望能有完善的应届生培养机制，再或者聊聊情怀，说这家银行一直是你的首选，你第一张银行卡／你们全家的银行卡是这的，每次来这家银行办业务都很喜欢它的氛围和文化）
        - [三家银行都面试通过！我发现了银行面试通关密码！_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1hV4y1L7Zx/)
          collapsed:: true
          [牛客网 - 找工作神器|笔试题库|面试经验|实习招聘内推，求职就业一站解决_牛客网](https://www.nowcoder.com/discuss/post/408747927236091904)
          - 思路
            - 缺点宽泛说, 优点具体说
            - 我爱银行, 最爱你们行
            - 我和这个岗位最合适
            - 银行业的发展非常有前途
          - 常用话术
            - 后台
              - 金融科技赋能业务发展
              - 加强金融产品创新
              - 提升用户体验
              - 精细化金融服务设计
              - 沉浸式交互体验
              - 数字金融服务
            - 前台 / 中台
              collapsed:: true
              - 拓宽R资渠道、简化D款手续
              - 把控风险、牢守防线
              - 主动防范金融风险
              - 保证资金安全及流动性
              - 增强客户粘性、拓展业务范围
              - 提升服务能力 普惠金融
      - 互联网 + 金融
        collapsed:: true
        - 量化交易
          collapsed:: true
          - 利用计算机根据**数据挖掘**以指定策略从而达到**超额收益或降低风险**的目的，避免投资者情绪波动从而做出非理性决策
          - 对于资产不高的个体户, 更迭的应该是资产管理, 所以更加需要互联网辅助来做更加理性的决策.
          - 门派
            - 选股 & 择时
            - 高频 & 低频
            - 基本面 & 技术面（情绪面）
              - 基本面
                collapsed:: true
                - 宏观择时
                - Alpha多因子模型
                - 排名选股策略
                - 行业主题轮动模型
                - 基于时间序列波动性的预警系
                - NLP 自动财报阅读
              - 量化套利
                collapsed:: true
                - 跨期套利
                - 期现套利
                - 跨品种套利
                - 跨市场套利
              - 事件驱动
                collapsed:: true
                - 公司业绩
                  collapsed:: true
                  - 业绩预告
                  - 业绩快报
                - 分红行为
                - 股权结构变动
                  collapsed:: true
                  - 大股东增减持
                  - 限售股解禁
                  - 定增
                  - 并购重组
                - 信誉调整
                  collapsed:: true
                  - ST摘帽
                  - 评级上下调
              - 大数据模型
                collapsed:: true
                - 传统机器学习
                  collapsed:: true
                  - 支持向量机（SVM）
                  - 随机森林（RF）
                  - 高斯混合模型（GMM）
                - 深度学习
                  collapsed:: true
                  - CGAN
                  - LSTM
                  - CNN
              - 异类指标
                collapsed:: true
                - 风水诊股
                - 老黄历诊股
          - via: [【量化入門】你是適不適合做量化投資？為什麽虧錢的總是你？投資門派介紹 | 時間序列模型 | 基本面量化 | 量化套利 | 大數據模型 - YouTube](https://www.youtube.com/watch?v=1lORPttsMiY)
        - [金融科技到底是什么？就业情况到底怎么样！_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1ZS4y1v7oZ/)
    - 提取关键字也非常重要, 一个经验就是对于不同的搜索字, 拿到的搜索结果也完全不同, 为了找一个简单的面经, 你可以直接去搜面经, `xxx行 面经`, 你也可以直接去搜 `xxx岗 面试`, 把每一个关键字找出来, 然后把所有种可能都去检验一遍. 就是这样
      #search #thought
  -
  - ### Special: 电力
  -
  - #Closed
    collapsed:: true
    - [[postgraduate]] | 研究生考试
      collapsed:: true
      - [csseky/cskaoyan: 提供计算机考研和软件工程考研专业的各个学校 考研真题](https://github.com/csseky/cskaoyan) ![](https://img.shields.io/github/stars/csseky/cskaoyan)
      - [521xueweihan/HelloGitHub: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub.](https://github.com/521xueweihan/HelloGitHub) ![](https://img.shields.io/github/stars/521xueweihan/HelloGitHub)
    - [[civil-service]] | 公考
      mark:: 没有做好准备，可能上考场也是去当分母；还需要缴纳 120 报名费；
-
-
- ## References
  - [2021年各大城市人才引进政策-本硕博必看 - 知乎](https://zhuanlan.zhihu.com/p/269625043)
    collapsed:: true
    - [郑州要放开落户了 - V2EX](https://www.v2ex.com/t/880552)
  - [想知道现在还有多少22届待业的毕业生？ - 知乎](https://www.zhihu.com/question/516392700)
  - > 总结一下回答里提及的天坑专业，包括计算机、金融、生化环材以及哲学类、经济学类、法学类、教育学类、文学类、历史学类、理学类、工学类、农学类、医学类、管理学类、艺术学类、军事学类学科。普遍反应这些专业教授的内容过时落后，过于注重理论研究，变现速度慢，人才供大于求，内卷严重。
    > 回答中没有提及的专业有：厨师、汽修、装载机、塔吊、叉车、美容美发、挖掘机、中西糕点、汽车美容钣金、金属焊接、数控机床。这些都是下一个风口专业，轻理论，重实践，变现快，人才少，缺口大，收分低，薪资高。不看家境看实力，独自闯出一片天，脚踩金融业；不用留在北上广，回乡也有好工作，完爆计算机。
    > via: [下一个天坑会是哪个专业? - 知乎](https://www.zhihu.com/question/402480681/answer/1295258807) & answer/1302710617
  - > 1-3 年是最尴尬的时候，比不上应届生有政策支持，比不上 3 年工作后的人有经验，别说今年，20 年疫情冲击没那么严重的时候都不好找 via: [今年这行情还有金九银十吗？ - V2EX](https://www.v2ex.com/t/874659)
  - > 动手能力跟考试成绩没啥关系，懂不懂算法跟能不能写出C语言程序也没啥关系
    >
    > 最大的问题不是程序员够不够，而是程序员这个工作能不能留住人。在大多数的中国企业管理层眼里，程序员就是农，就是当牲口用的。虽然拿着高工资，却严重透支了体力，且没又让你有思考的时间和发展的空间。很多人写代码写着写着就跑了，要不当管理层，要不就转行。特别是转行的人很多还是非常优秀的开发人员。
    >
    > via: [中国的程序员群体是否已经过多了？ - 知乎](https://www.zhihu.com/question/51359754/answer/126111988) & answer/324682548
  - > 做技术能干一辈子，都是那些有好奇心，对技术本身就喜欢的。
    这些人就算不做这个行业，他也会去关注技术发展，尝试新的技术，自己写写代码。
    > 如果没什么兴趣，只是为了赚钱而工作学习的话，技术发展快本身就会不断淘汰老人。建议趁早转行。
    > via: [如果想在计算机行业干一辈子，应该怎么办 - V2EX](https://www.v2ex.com/t/880497)
    > 直接说结论：国内最多的所有应用软件技术都不能！
    > 国内所有写业务的程序员技术栈，顶多算框架熟练工！
    > 行了，不装了，我的意思是：
    > 在座的各位都是辣鸡！包括我自己。
    > 这里讲过了，如何为他人评估 or 为自己建造一个职业护城河
    > via: [程序员靠纯技术能渡过中年危机吗？ - V2EX](https://v2ex.com/t/879797#r_12105497)
  - > 什么是卷? 你做的很多东西, 被量化到 A4 大小的纸上, 因为上面有的选, 你的未来完全取决于你的竞争对手, 虽然生活中人都是各异的, 但是社会中的很多人还是会有很多人直接使用刻板印象来看人看物, "宁愿错杀三千, 不愿意放过一个", 说多了真难受.
    — [外包真的这么毁简历？ - V2EX](https://www.v2ex.com/t/880617)
  - [猛背了几个月的八股文, 跟面试官对答如流, 万万没想到, 这也能成为被拒的理由 - V2EX](https://www.v2ex.com/t/880727)
  - [ruanyf on Twitter: "2022年7月份的《谁在招人？》，正在找工作的朋友可以看看下面的岗位。详情 GitHub： https://t.co/fZHhU15amN 如果你们团队想招程序员，也欢迎发布到那里。 https://t.co/UMOXcIBhm8" / Twitter](https://twitter.com/ruanyf/status/1542441375668797441)
  - [面试者如何回应面试官问的「你有哪些要问我的？」？ - 知乎](https://www.zhihu.com/question/28058827)
  - [那些尴尬又不得不回答的面试题](https://www.zhihu.com/pub/book/119560841)
  - ### 试用期被裁
    collapsed:: true
    - [好尴尬， 6 个月试用期最后几天被辞退，这样做合理么？ - V2EX](https://www.v2ex.com/t/674202)
      - 对于试用期，很多人的观念是试试而已，合适再签合同，不合就散。其实不然。
      - 几个要点
        1. 用人单位用工之日起即与劳动者建立劳动关系，并应最迟 1 个月内订立书面合同。
        2. 劳动期限 3 年以上的，才可以有 6 个月的试用期。试用期包含在劳动合同期限内。合同只约定试用期而未约定劳动期限的，试用期就是劳动合同期限期限。
        3. 试用期用人单位单方解除劳动合同的条件有是劳动者不符合录用条件，或严重违章，失职，营私舞弊，犯罪等。不符合录用条件要有充足的证据，不能随意认定。
        4. 试用期结束就辞退的，实质是用人单位单方解除劳动合同，应当补偿劳动者。标准是按工作年限每年 1 个月工资，工作满 6 个月按 1 年计，不满 6 个月补偿半个月工资。
        5. 用人单位违法解除劳动合同，按补偿标准 2 倍支付赔偿。在试用期内单方无理辞退就是违法解除。
    - [距离试用期结束 11 天被通知 能力不足不能给我转正 让我自行离职 - V2EX](https://v2ex.com/t/823405)
      - 我曾经遇到过一个无良公司，想开除我又不想赔钱。说我上班玩手机（移动开发），还说我顶撞领导（需求讨论而已），想以此违纪开除威胁我自主离职。跟 HR 谈判后 HR 自知没法无偿开除我，提出让我回去继续上班，当时真的人都傻了，继续上班的境地可想而知。
      - 跟公司谈判，以上情况虽然很不可思议，但万一公司真那么不要脸了你就会非常难受，我至今也不知何解。
      - 所以，遇到这种情况就让他开除，坐实了违法解雇后直接仲裁。
      - 还有，常备热线：
      - 12345 市长热线，日常问题都可以打这个
      - 12348 法律援助，法律相关问题打这个
      - 12333 人力资源和社会保障
      - 除了市长热线主要就是接线记录工作没啥专业知识，下面两个专业性的热线接线员专业水平良莠不齐，一定要多打几个咨询不同的接线员。
    - [试用期六个月的公司靠谱吗？ - 知乎](https://www.zhihu.com/question/277181556)
    - [试用期没通过，下家怎么写原因？ - V2EX](https://www.v2ex.com/t/789339)
  - ### 银行
    collapsed:: true
    - > 银行这个工作，**如果你去的是股份制银行，而不是国有四大，并且你的职位不高，只是基层人员，那银行确实是不是人呆的地方**。
      >我没有在银行系统呆过，但是我们律所代理的有银行的案子。股份银行和国有银行最大的区别有两个，股份银行事巨多，每天开会、开会还是开会，各种指标轮番轰炸，甚至于那个工作群每天就是xx回款了，喜报连连，这无疑让我感觉跟个传销机构似的；国有银行就很简单，给你案子你就弄，我也不催你，我有案子就给你。但当然，股份银行给的律师费也会高很多。
      >为什么会感觉银行基层工作人员不是人干的，我们作为委外律师，每天电话轮番轰炸，当然与我们对接的已经是银行的算是中层人员了，对我们态度也算稍微客气，即使这样依然是每天轮番轰炸，有些时候感觉非常心累，因为你前一秒刚刚解释过了，下一秒他又会打电话问你。每次去银行对接材料，大部分人不是在开会就是在开会，每天还要催我们要各种无效（自认）的表格，一大部分时间甚至于不是在做案子，而是在完成银行给的某些与诉讼无关的工作。不要问我既然这么多事为什么还要干，因为他们给的代理费高。
      >所以，如果只拿少的可怜的薪资，而且晋升无望的话，也没有爱好，那就早点脱离苦海。
      via: [我在银行干不下去了，真的是我的问题吗？ - 知乎](https://www.zhihu.com/question/538507858/answer/2550887429)
    - > 我妹子前年去的银行软开，抱着不想努力了，找个稳定工作躺平的心态去的。
      结果呢：
      1. 各大银行开始剥离开发岗到软开中心，铁饭碗不再稳定
      2. 各大行在招行和互联网的刺激下开始学习互联网内卷，开发岗加班变得严重
      3. 银行学了互联网的加班，但是没学互联网的高待遇，没有加班费，周末免费加班是常态
      4. 银行内部是外行管理内行，技术岗的领导都是业务过来的你敢信！天天搞办公室政治，吹牛做虚
      5. 我妹子去了两年，现在整个人都很憔悴，但因为银行这两年快把人搞废了，现在想出来互联网也不要银行经历的。
      >
      LZ 可以现在脉脉上看看各大行开发的吐槽 特别是中信这样排头兵的
      via: [校招，银行软件开发岗位和互联网大厂软件开发的 offer 比较，希望发表一下意见 - V2EX](https://v2ex.com/t/800929#r_10864403)
    - >大学同宿舍校招去了交行数据中心，收入比互联网公司少点，不过忙也挺忙的，有项目投产值班，项目上线值班，国庆大练兵之类的，最忙的时候接近 996 。稳是稳，不过工作用他的话说就是”越来越不像程序员了“，实质工作内容越来越偏项目经理，对接银行不同部门的需求然后分给手下的一堆外包开发
      >
      看来 OP 还是渴望卓越的人呢
      「人生三阶段，知道父母是普通人，知道自己是普通人，知道孩子是普通人」
      你还没过第二阶段啊，绝大多数的人都是普通人，别太看轻自己，但更多时候别太看高自己。
      >
      工作这么多年，没在大厂待过，也没拿到过你这种薪资。不过还是能说一说的，我觉得你要是觉得自己缺钱的话，那还是首选互联网大厂，不然银行还是好点，至少干到 35 岁轻轻松松，后续基本也没有互联网被辞退的风险，属于是能养老的地方了。
      >
      如果不是外包，必须建总。
      中国五大行不是吹的，他们没有发展的天花板，各个行业都触及到，你可以转向金融科技，也可以金融，也可以走体制内提拔，也可以干几年转去大厂，记住是去大厂，而不是小厂。上下都可行，为啥不去？再不济，还能读个博，当研究员。
      如果你觉得银行特别传统，特别 low ，那就是被那些互联网概念洗脑了。你去看看银行的金融科技，他们以稳重为前提，人工智能，智能银行，大数据，那点没涉及到？？传统业务哪点没有深入到社会各个领域？你所知道的各种云，那个不管银行叫爹，你见过银行叫谁爹的了么？你见过有谁说比银行的科技海量要高嘛？？银行构架在生后之外的科技，需要不断有外面的第三方公司去验证，验证合适了自己才来用，你觉得那个公司的用户比银行多？？哪怕微信日活真么强，他能跟银行卡比嘛？？？他敢说比银联还强???我不信。。。。。
      >
      如果你家里条件还行，对钱的渴望不是那么那么强烈，建议去银行。。。
      银行的科技化也是大趋势，虽然很多东西非自研都是采购，但用的、买的肯定都是一流的，毕竟谁都不敢乱来，接触的也是非常棒的技术。
      我大学室友在某银行上海公司，应届生身份进去的有编制，非劳务派遣，我嘛也算在大厂，但从生活状态来看，明显他的幸福指数高太多了。银行也会在各种特殊时期加班加点做保障，但其他 99%的时间都是到点就下班。
      网上很多或者大部分关于银行相关回复都是劳务派遣那些的，因为应届进去的很少，珍惜这种应届生身份，硕士的话一辈子真的就这一次了（本科还可以通过工作后再读专职研究生重新获得一次）
      via: [银行总部和互联网 Offer 该怎么选 - V2EX](https://www.v2ex.com/t/833168)
    - [四大国有银行未来会大规模裁员吗? - 知乎](https://www.zhihu.com/question/349940052)
    - [应届毕业生推荐去银行工作吗? - 知乎](https://www.zhihu.com/question/531853259)
    - [秋招 offer 选择&&建议 - V2EX](https://www.v2ex.com/t/814297)
    - [为什么春招我收到的回复全是银行的，是银行简历门槛会比国企低吗？ — 匿名用户 的回答 - 知乎](https://www.zhihu.com/question/532332416/answer/2508757033)
    - [秋招了，想了解一下在银行 IT 工作是什么感觉 - V2EX](https://www.v2ex.com/t/584013)
    - [各种银行卡的缩写_百度知道](https://zhidao.baidu.com/question/583173541.html)
    - [招商银行信用卡中心2018秋招部分编程题汇总_牛客网](https://www.nowcoder.com/test/question/analytic?tid=61905467)
    - [EPI？行测？ 傻傻分不清楚 - 知乎](https://zhuanlan.zhihu.com/p/39318978)
    - [银行科技岗秋招怎么准备笔试啊？ - 知乎](https://www.zhihu.com/question/549780017)
    - [建设银行笔试如何准备？笔试科目是什么？ - 知乎](https://www.zhihu.com/question/390444369)
    - [就银行招聘来说，中公教育，课观哪个比较好？ - 知乎](https://www.zhihu.com/question/294234091)
    - [无领导小组面试太容易了！资深HR分享_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1mv411T72R/)
    - [“好不容易收到工商银行的面试”，还不来掌握工行面试密码吗！_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV11Z4y1t7SD)
    - [工商银行科技菁英岗面试都会问一些什么问题？ - 知乎](https://www.zhihu.com/question/351758649)
    - [边际效用 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E8%BE%B9%E9%99%85%E6%95%88%E7%94%A8)
    - [拿了6家银行信息科技岗offer的一些经验 - 知乎](https://zhuanlan.zhihu.com/p/89581753)
      - 一面
        - 通常偏技术面，通常数据库、操作系统、计算机网络和java问的比较多（尤其农行面试数据库问的比较多），这个如果基础不错的同学一般都没有问题。农行面经还是可以看看的。如果编程基础薄弱的同学还是要提前抓紧时间补一补相关知识的。如果数据库、计算机网络等知识比较薄弱，可以尝试自己用写个服务端相信会有比较深刻的理解，推荐可以找一些比较好的JAVA书籍学习一下，我当时是看的《疯狂JAVA讲义》，当时是正好实验室有同学有，就直接拿来看了，感觉还不错。如果希望对数据库、计算机网络知识有深入了解的同学可以看下的。
        - 通常采用半结构化面试，即面试官采用我问你答的形式对应聘者进行面试。面试的内容通常是1分钟自我介绍+面试官针对性提问环节+面试官自由提问环节。基础知识面试主要侧重考察面试者专业知识的熟悉程度。
      - 二面（无领导小组面、半结构化面试）
        - 通常采用无领导小组面试，部分银行也可能仍然采用半结构化面试的形式，只是面试的侧重点会有所调整。无领导小组面试可能会有团队协作型、主题辩论型等不同的形式。综合素质面试主要侧重考察面试者的组织能力、沟通能力、团队协作能力等。
        - 由于大家都是程序猿，所以在表达能力上不可避免的有所欠缺，但是由于我之前参加过一些演讲和在公共场所经常做一些presentation,所以我反而觉得这是我的翻盘局，我感觉这也是我拿到诸多银行offer的主要原因。当然我觉得这个里面还是有很多技巧的，只要稍加训练完全没有问题。
        - **无领导面试、半结构化面试是在银行面试中十分重要的一部分**
        - （比如农行软开面试、农行数据中心面试、工行软开面试以及工行数据中心面试就是半结构化、工行北京就是无领导面试），很多技术特别牛的大佬往往挂在这一步，往往是因为没有把自己的优点完美的表现出来。
    - [秋招银行面试连挂10场，想向大家求助？ - 知乎](https://www.zhihu.com/question/53472964)
    - [银行科技岗要不要转业务部门，比如公司部？ — 风控牛牛 的回答 - 知乎](https://www.zhihu.com/question/537839237/answer/2535556557)
    - [在银行工作，有关系和没关系有什么区别？ — 银行生活图鉴 的回答 - 知乎](https://www.zhihu.com/question/370707200/answer/1083767345)