- 卷面是 80 分 (20分简答 + 60分==案例==) + 平时 20 分
  - 第一次开课?
  - 傻逼???
- 作业
  - 需求管理工具比较
    collapsed:: true
    - via: https://www.docin.com/p-1664474036.html
    - <style>
      </style>
      | **条目**                                       | **DOORS**                                                                                                               | **AnalysetStudio**                                           | **Borland Caliber**                                       |
      | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | --------------------------------------------------------- |
      | **项目开发可扩展性**                                 | 是企业级的产品：即，一个 DOORS<br> Database 能够同时支持许多个不同的项目开发，从而使得新的项目能够复用和共享过去的文件和信息。不同项目（文件）之间的追踪关系可以跨项目建立。                        | 将需求的数据存放在数据库中，而把与需求相关的上下文信息存放在Word文档中，用户使用ReqPro时必须安装Word    | 只支持单个项目的开发，即，一个 Database 只能支持一个项目的开发，因此无法支持对过去文件和信息的复用和共享 |
      | **对需求变更的管理**                                 | 本身支持变更管理系统，即变更的提交，评审，应用，并因此可以给指定的用户分配不同的角色                                                                              | 本身没有变更管理系统，只能依赖于与Rational的配置/变更管理工具集成Clear Quest             | 本身没有变更管理系统，只能依赖于与配置管理工具的集成，但集成的功能比较弱，无法支持追踪关系             |
      | **对需求基线的管理**                                 | 本身具备对需求的基线管理功能， 可比较不同基线的需求差异，实现需求基线管理；                                                                                  | 只能依赖于与 Rational 的配置/变更管理工具集成，但只能存储版本，无法比较需求差异                |                                                           |
      | **多个需求项及追踪关系的显示**                            | 能够在屏幕上给用户一次显示一个文件中的多个或所有需求项和相互之间的追踪关系(即支持横向和纵向的需求追踪)，从而支持用户同时观看所有相互依赖的需求项。                                              | 一次只能显示一个需求项供用户观看，限制了用户同时直接阅读其它需求项，因此也不能在屏幕上一次显示相互连接的多个需求项和文件 |                                                           |
      | **权限控制**                                     | 具有灵活的权限控制，包括：只读， 修改，创建，删除，管理等五种级 别。权限控制可以针对每一个用户 在每一个 database，项目目录，文件，需求项，属性上实施等                                       | 无法对不同的用户对数据库结构自上到下的每一个层次做到灵活有效的权限控制。                         |                                                           |
      | **可疑**   **link** **（需求变更）<br> 的通知**         | 当 link 的一方产生变更时，Doors 可以自动产生提示符通知另一方， 而不需要在 link 的矩阵上查找；                                                                | 没有自动提示，必须通过追踪关系矩阵来查找,当追踪矩阵比较大时，非常费时费力                        | 没有自动提示，必须通过矩阵来查找，当矩阵比较大时，非常费时费力                           |
      | **数据备份和恢复**                                  | DOORS 在恢复备份的数据时能够保证数据库中已有的文件不会被覆盖。当数据库中已有同名的文件时，数<br> 据库系统会自动的给被恢复的文件 另外的名字； 由于 Doors 把所有数据均存放在数据库中，因此数据的备份和恢复过 程又安全既简单 |                                                              |                                                           |
      | **与其他工具的集**                                  | 作为独立的软件供应商，Telelogic DOORS 不但可与 Telelogic 自身的其他软件工具集成，还可与Microsoft, IBM Rational, Mercury 等厂商的工具集成                      | 只能与自身的软件工具集成                                                 |                                                           |
      | **异地需求管理**                                   | Doors 提供灵活的方式实现需求异地管理的方式；Doors 强大的性能优势也保障了大型项目异地需求开发/管理的可能                                                              | 只能与自身的软件工具集成                                                 |                                                           |
      | **Import and Export** **（文件** **的导入****导出）** | DOORS 在从 Word 导入文件时，会把Word 文件中的表格，图形和 OLE 对象原封不动导入，并可以在 DOORS 中对导入的表格和 OLE 对象（如 MS Visio 图形）进行编辑。                       |                                                              | 在从Word导入文件时，会丢失所有 Word 中的表格，图形和 OLE 对象，也就谈不上对他们的编辑操作了     |
  - 故障分析软件比较 word 报告
  - 读论文，写调研报告
- ---
- Homework
  - 请说明需求的3个层次分别是什么，并对其进行简要说明
    collapsed:: true
    - **业务**需求 (business requirement)
      - 主要目的
        collapsed:: true
        - 对企业目前的业务流程进行评估，得出一个业务前景
      - 作用
        collapsed:: true
        - 业务需求的确定对后面的用户需求和功能需求起到了限制作用
      - 反映了组织结构或客户对系统、产品高层次的目标要求
      - 在项目视图与范围文档中予以说明
    - **用户**需求 (user requirement)
      id:: 63085063-310e-4c0c-acd2-a8e5a8654e28
      - 文档描述了用户使用系统而完成的任务集合
      - 用户需求在用户案例 (user case) 文档或方案脚本中予以说明
      - 收集/分析 用户需求 不容易
        collapsed:: true
        - **隐形**需求，难保证需求**完整**，需求**易变**，
          - 充分的交流
    - **功能**需求 (functional requirement)
      - 源于 ((63085063-310e-4c0c-acd2-a8e5a8654e28))
      - 定义了开发人员必须实现的软件功能
      - 在开发、测试、质量保证、项目管理以及相关项目功能中都起到了重要的作用
      - 非功能需求
        - 描述了**系统**展现给用户的**行为**和执行的**操作**等
          - 包括要遵从的**业务规则、人机接口、安全性和可靠性等要求**
  - 请阐述需求分析的主要步骤和方法
    collapsed:: true
    - 确定**要解决的问题**
      - **定义**问题
        collapsed:: true
        - 简单地将问题记录下来, 和用户讨论, 对问题达成一致
        - 讨论之后列出的问题需要是**双方都认可**的问题。
      - 分析问题根本**原因**
        collapsed:: true
        - 例如
          collapsed:: true
          - 造成订单输入速度慢的原因是什么？
            - 是不是模块中某个查询语句使用不当从而造成速度受到影响？
        - 在分析过程中可以采用**鱼骨图**法
          collapsed:: true
          - 对于**原因分析**非常有效
      - 分析**涉众**
        collapsed:: true
        - 最终目的
          - 为了满足相关人员的需要
      - 定义**系统边界**
        collapsed:: true
        - 可能非常清晰
          - 例如一个单机版的游戏，人机交互界面就是系统的边界
        - 可能需要考虑更多的问题(复杂系统)
          - 例如，是否和其他系统共享数据，是否支持在线访问，如何与其他系统交互等
      - 确定**约束条件**
        collapsed:: true
        - 例如
          - 系统开发是否有预算限制？
          - 是否允许使用新技术？
          - 在完成时间上有限制吗？
    - 分析过程中可以**采用的几种方法**
      - 需求研讨会
        collapsed:: true
        - 需要将所有涉众尽可能集中到一起对用户存在的问题和需求进行讨论
        - 目的
          - 在较短的时间内鼓励与会者在应用需求上达成共识，尽快取得一致意见。
        - 1-2 day
      - 头脑风暴
        collapsed:: true
        - 需要**新意见**或者**创造性**地解决问题的方案时
          - **自由讨论**是一个非常有用的技术
            - 它简单而且非常有趣
        - 头脑风暴激发所有与会者尽可能地提出自己的意见，而在收集了大量的意见后则需要裁减，产生出真正的意见
      - 用例模型
        collapsed:: true
        - 用例描述了用户和系统之间的交互，其重点是系统为用户做什么。用例模型由系统的所有参与者以及参与者与系统交互的用例组成，从而描述系统全部功能性行为。用例模型也显示了用例之间的关系，有助于进一步理解系统。
      - 访谈
        collapsed:: true
        - 一种简单、直接的需求获取方法
        - 在访谈的过程中应该尽量使用与可能的解决方案无关的问题，以使被访者的答案不具偏向性
          collapsed:: true
          - 访谈中的问题和答案都应该记录下来，以便在考虑解决方案时参考。
      - 角色扮演
        collapsed:: true
        - 允许开发团队**从用户的角度**体验用户的世界
        - 必要性
          - 仅通过观察和分析难以对系统有完全清晰的认识
      - 原型法
        collapsed:: true
        - 软件系统的早期缩型
        - 显示
          - 新系统的部分功能
        - 可以帮助软件开发人员和用户更好地理解软件需求
  - 请说明基于用例的需求分析过程
    collapsed:: true
    - ![image.png](../assets/imu/sp/image_1661334759834_0.png)
    - 用户需求
      id:: 63085063-dba8-4077-909d-9a74f8341418
      - 主要任务
        - 找出和描述系统中的执行者和用例 (必须确认)
          - 执行者不属于系统，但直接（或间接）驱动与之关联的用例的执行
        - 用例描述了**系统外部的执行者要实现的目标**，反映的是用户需求，但并**没有涉及系统应提供的相关的具体功能细节**
    - 功能需求
      - 获取阶段
        - 需对 ((63085063-dba8-4077-909d-9a74f8341418)) 的用例进行**重新分解和整合**，并最终形成完整的用例规格文档
        - 精化用例步骤如下
          - 从用户需求阶段获取的所有用例中选择一个具有**最高优先级用例**
            - 如购物网站的商品购买
          - 场景分析
            - 根据执行者的目标确定顺利完成目标的基本的最简单的交互序列，即先确定用例的主要场景。
            - 根据主要场景中每个基本步骤**考虑其异常情况和其他可选项确定次要场景** -> 得到用例的所有场景后
          - 用例分解
            - 用例是场景的集合，场景中的每一步都可看成是一个小的子用例
              collapsed:: true
              - 这些子用例是场景所属外部用例的下级用例
              - 执行者称为系统的内部执行者，包括系统、子系统和对象三类实体
              - 这些内部执行者是下级用例中与外部用例执行者交互的实体对象
          - 用例判定
            - 根据场景中下级用例的粒度做出判定
              - 像更新数据库这类的简单操作，因其粒度太小，将它继续看成用例只能造成用例数量的膨胀，毫无益处。故应该把它**当作系统实现的简单行为**，这个简单行为就是系统要实现的一个**功能需求**
            - 对于较大粒度的下级用例，因其本身代表了一个复杂的子交互序列，其执行者有明确的目标，应将其当作新的待求精用例，重复2～4步获取其功能需求
          - 对剩余的用例，重复2～4步。当再没有用例可以求精时，最终得到的所有用例中的简单行为的集合就是系统的功能需求
  - 请简要说明需求变更控制的流程和注意事项
    collapsed:: true
    - ![image.png](../assets/imu/sp/image_1661334861970_0.png)
      collapsed:: true
      - 需求变更的时候，要提出变更申请，还要由需求变更控制委员会（Change ControlBoard，CCB）对提出的申请进行评估，评估的内容包括需求的重要性、时间和资金等。评估之后要做出通过与否的决定。如果CCB确认了提交的变更请求，则将指派某个人对原来的需求进行修改，并对其进行验证，最终才实施该需求的变更。
    - 注意事项
      collapsed:: true
      - 需求一定要与投入成本有联系
        collapsed:: true
        - **需求变，软件开发的投入也要变**
          collapsed:: true
          - 如果需求变更的成本由开发方来承担，则项目需求的变更就成为必然了
          - 需求的变更要经过出资者的认可
            - 才会对需求的变更有成本的概念，能够慎重地对待需求的变更
      - 小的需求变更也要经过正规的需求管理流程，否则会积少成多
        collapsed:: true
        - > 不愿意为小的需求变更去执行正规的需求管理过程，认为降低了开发效率，费了时间
          - 使**需求**逐渐变为**不可控**，最终导致项目的失败
      - 精确的需求与范围定义并不会阻止需求的变更
        collapsed:: true
        - 并非对需求定义得越细，就越能避免需求的渐变，这是两个层面的问题。太细的需求定义对需求渐变没有任何效果。因为需求的变化是永恒的，并非需求写细了，它就不会变化了。
      - 注意沟通的技巧
        collapsed:: true
        - 实际情况是用户、开发者都认识到了上面的几点问题，但是由于需求的变更可能来自客户方，也可能来自开发方，因此，作为需求管理者，项目经理需要采用各种沟通技巧来使项目的各方各得其所
  - 请简述软件过程与软件质量的关系
    collapsed:: true
    - 软件过程包括软件质量.
    - 软件质量
      collapsed:: true
      - 软件产品的特性可以满足用户的功能性能需求的能力, 即客户的满意度
    - 软件过程
      collapsed:: true
      - 软件生命周期中的活动
      - 一般包括软件需求分析、软件设计、软件编码、软件测试、交付、安装和软件维护
    - 软件过程的优劣决定了软件质量的高低，好的过程是高效高质量的前提
      collapsed:: true
      - **人员和过程**是决定软件质量的关键因素，高质量的人员和好的过程应该得到好的产品
  - 举出一些具体的例子说明过程不成熟性
    collapsed:: true
    - > 1996年6月4日，Ariane 5(阿丽亚娜) 火箭在法属圭亚那库鲁航天中心首次发射。火箭在发射37秒之后偏离其飞行路径并突然发生爆炸，与Ariane5火箭一同化为灰烬的还有4颗太阳风观察卫星。这是世界航天史上的一大悲剧，也是历史上损失最惨重的软件故障事件。
      事后的调查显示，控制惯性导航系统的计算机向控制引擎喷嘴的计算机发送了一个无效数据，其原因在于将一个64位浮点数转换成16位有符号整数时产生了溢出。这个溢出值测量的是火箭的水平速率，开发人员在设计Ariane 4火箭的软件时，认真分析了火箭的水平速率，确定其值绝不会超出一个16位的数。而Ariane 5火箭比Ariane 4的速度高出近5倍，显然会超出一个16位数的范围。不幸的是，开发人员在设计Ariane 5火箭时只是简单地重用了这部分程序，并没有检查它所基于的假设。
    - 这充分说明软件过程的不成熟，没有具体过程检测数据类型转换会出现的问题
  - 阅读完全部的 CMM(Capability Maturity Model, 能力成熟度模型) 内容，选择出你认为最有价值的十条关键实践，并说出理由
    id:: 63085063-bf2c-46b2-bf6b-62e31a207fe9
    - 项目实际情况 -> 选定遵循的标准、规范
      collapsed:: true
      - 好的编码规范可以
        collapsed:: true
        - 改善软件的可读性，可以让开发人员尽快而彻底地理解新的代码
        - 最大限度的提高团队开发的合作效率；
    - 项目软件的质量 -> 确定采用的软件开发方法
      collapsed:: true
      - 开发时选择
        collapsed:: true
        - 面向数据结构的开发方法
        - 面向对象的开发方法
      - 直接会影响到小组的开发进度。
        collapsed:: true
        - 要根据成员的擅长情况制定方法。
    - 任命项目负责人
      collapsed:: true
      - 需要理解所有需求，软件开发架构，人员任务安排分配
    - 根据项目要求，建立软件有关组（例如工程组、软件测试组等）
      collapsed:: true
      - 在进行开发的时候不可能一个组就完成所有工作，编程组，视觉组，产品组，文案组等都要人员来做
    - 确定设计、编程、测试人员，并实施三分离
      collapsed:: true
      - 实现了三分离可以**防止成员思维固话**，提高项目质量，减少隐患。
    - 制定正式评审规程、建立相应的评审机构
      collapsed:: true
      - 项目评审工作是对整个项目的执行，未来进行评审，对项目的财务进行规划获取管理层的信任
    - 项目软件负责的职责明确
      collapsed:: true
      - 每一项责任工作要具体分配到每一个人，如果某个环节出现问题，也可以对应责任到人
    - 具有各阶段活动所需要的软／硬件环境、支持工具，并提供足够的经费
      collapsed:: true
      - 基本的项目所需要的设备，环境，经费是必须的，合理的经费分配花费，才能合理的高效的任务
    - 软件版本管理员，以及设计、编程、测试人员的职责明确
      collapsed:: true
      - 软件开发形成后，需要版本更新，测试维护，这些职责同样很重要，软件运营时的维护开发也要对应到每一个人，明确责任
    - 项目软件负责人，设计／编程／测试人员、软件版本管理员均已得到相应的培训，具备了完成其职责所需要和的知识和技能
      collapsed:: true
      - 减少再培训所花费的时间，使项目开发人员更加熟练，降低人力成本，减少错误，减少时间花费。
  - 进一步了解 **系统工程能力模型 SECM** ，分析和 **能力成熟度模型集成 CMMI** 有什么不同?
    collapsed:: true
    - 同
      - 都秉承了 EI—CMM 的框架和基本原则
      - 都以过程域（或焦点域）为主要构成要素
      - 把特定实践和通用实践的完成情况作为系统工程能力等级的评价标准
      - SECM 和 CMMI为系统工程过程能力的评价和改进提供了有效途径
      - 都继承了CMM模型的局限性，在**对系统工程能力等级的评价上具有明显的不完整性**
        - 因为它们仅仅考虑了系统工程过程这单一要素，而未涉及其他要素
        - NASA把系统工程能力的构成要素定义为过程、技术和人员三项，其中过程包含系统设计、系统实现和技术管理方面的若干过程，技术指系统工程方法、工具、标准规范等，人员要素包含人员知识、能力、经验和职业道德等。因此，系统工程过程能力并不完全等同于系统工程能力，系统工程能力的全面评价要素应包含过程、技术和人员三个方面。
    - 异
      - SECM 根据系统工程的特点，开发了连续表示的能力等级模型，对系统工程过程域及特定实践进行了全面设置，对通用实践进行了明确规定，为系统工程个别过程域（即焦点域）的评价及改进提供了有效工具
      - CMMI 是集成软件、系统工程等领域成熟度模型的统一框架，为满足不同组织需求开发了连续表示和分级表示两种成熟度模型，设计了通用于软件开发、系统工程及集成产品开发的过程域和实践，适用于企业的全面过程改进
  - 如何更好地构造一个适合型软件组织的、成熟的过程框架？
    collapsed:: true
    - 框架的内容很广泛，不仅包括技术，还包括项目经验、软件过程、管理思想和组织设计等内容
    - 软件过程, 建设好一个软件组织的过程文化
      - 识别文化差异。比如，通过识别成员同一性、对人的关注度、控制、风险和报酬标准等多个指标来进行衡量。
      - 文化敏感性训练。加强人们对不同文化环境的适应能力，方法有拓展训练、模拟式的培训、宣传和案例分析等。
      - 创建共同文化。即创造与组织商业目标相结合的一致的文化。
    - 管理思想, 根据 CMM/PSP/TSP 建立了指导原则。
      collapsed:: true
      - CMM 是过程改善的第一步，它提供了评价组织的能力、识别优先改善需求和追踪改善进展的管理方式。企业只有开始CMM改善后，才能接受需要规划的事实，认识到质量的重要性，才能注对员工经常进行培训，合理分配项目人员，并且建立起有效的项目小组。然而，它实现的成功与否与组织内部有关人员的积极参加和创造性活动密不可分。
      - PSP 能够指导软件工程师如何保证自己的工作质量，估计和规划自身的工作，度量和追踪个人的表现，管理自身的软件过程和产品质量。经过PSP学习和实践的正规训练，软件工程师们能够在他们参与的项目工作之中充分运用PSP，从而有助于CMM目标的实现。
      - TSP 结合了 CMM 的管理方法和 PSP 的工程技能，通过告诉软件工程师如何将个体过程结合进小组软件过程，并将后者与组织进而整个管理系统相联系；通过告诉管理层如何支持和授权项目小组，坚持高质量的工作，并且依据数据进行项目的管理，向组织展示如何应用CMM的原则和PSP的技能去生产高质量的产品。
    - 组织设计, 建立有效的软件组织的过程，处理好组织、过程和环境的关系
    - ![image.png](../assets/imu/sp/image_1661335142985_0.png)
  - Other
    collapsed:: true
    - PSP 分为哪 4 个等级？对各个等级进行简单说明?
      collapsed:: true
      - PSP0 个体**度量**过程
        collapsed:: true
        - 目的
          - 建立个体过程基线
        - 通过这一步，学会使用 PSP 的各种表格采集过程的有关数据，此时执行的是该软件开发单位的当前过程，通常包括计划、开发（包括设计、编码、编译和测试）以及后置处理三个阶段，并要作一些必要的试题，如测定软件开发时间，按照选定的缺陷类型标准、度量引入的缺陷个数和排除的缺陷个数等，用作为测量在 PSP 的过程中进步的基准。
      - PSP1 个体**规划**过程
        collapsed:: true
        - 重点
          collapsed:: true
          - 个体计划
        - 引入了**基于估计的计划方法** PROBE（PROxy Based Estimating），
          collapsed:: true
          - 用自己的历史数据来预测新程序的大小和需要的开发时间，并使用线性回归方法计算估计参数，确定置信区间以评价预测的可信程度
      - PSP2 个体**质量管理**过程
        collapsed:: true
        - 重点
          - 个体质量管理
        - 根据程序的缺陷建立检测表
          collapsed:: true
          - 按照检测表进行设计复查和代码复查（"代码走查"），以便及早发现缺陷，使修复缺陷的代价最小
        - 随着个人经验和技术的积累，还应学会怎样改进检测表以适应自己的要求。
      - PSP3 个体**循环**过程
        collapsed:: true
        - 目标
          collapsed:: true
          - 把个体开发小程序所能达到的生产效率和生产质量，延伸到大型程序
        - 方法
          collapsed:: true
          - 螺旋式上升过程 / 迭代增量式开发
            - 首先把大型程序分解成小的模块，然后对每个模块按照 PSP2.1 所描述的过程进行开发，最后把这些模块逐步集成为完整的软件产品。
    - 简要说明 TSP 的工作流程?
      collapsed:: true
      - TSP -> 工作 -> 划分周期(包含一套完整的需求, 设计, 实现和测试)
        - 策略和计划
          collapsed:: true
          - 确定策略标准
          - 概念设计
          - 估计规模和时间
          - 风险估计
          - 策略 归档
        - 需求
          collapsed:: true
          - 与客户沟通
          - 需求评审
          - 制定需求规格说明书
        - 设计和实现
        - 测试和后期维护
          - 测试
          - 跟踪和度量测试情况
          - 后期维护分析缺陷评价质量
    - 简述成本的基本估算方法?
      collapsed:: true
      - 最主要的是**对直接成本进行估算**。同时为了有效的控制风险，除了给出预算的成本之外，还可以适当给出成本的浮动范围。
      - 基本估算方法
        collapsed:: true
        - 经验估算法
          - 进行估算的人应有专门的知识和丰富的经验，据此提出一个近似的数字
          - 这种方法是一种最原始的方法，还称不上估算，只是一种近似的猜测
          - 它对要求很快拿出一个大概的数字的项目是可以的，但对要求详细的估算显然是不能满足需求的
        - 比例法
          - 比例法是比较科学的一种传统估算方法
          - 它以过去的项目为参考来预算目前的项目成本
        - 工作分解结构 (Work Breakdown Structure / WBS) 全面计算
          - WBS 是一种比较准确的一种成本估算方法
          - WBS 估算要求先把项目任务进行合理的划分，分到可以确认的程度
            - 如某种材料，某种设备和某一活动单元等
          - 然后估算每个 WBS 要素的费用
          - WBS 成本估算又分为自上而下和自下而上两种估算方法
    - 资源管理的主要内容包括哪些?
      collapsed:: true
      - **项目管理**中重要的一环
      - 主要分为两个部分
        collapsed:: true
        - 人力资源管理
          - 人力资源管理是要在对项目目标、规划、任务、进展情况以及各种内外因变量进行合理、有序的分析、规划和统筹的基础上，采用科学的方法，对项目过程的所有人员予以有效的协调、控制和管理。
          - 对人力资源的获取，培训、保留和使用等方面所进行的计划、组织、指挥和控制活动
          - 主要内容有 (3)
            - 项目组织规划
            - 建立项目组织
            - 组织建设
        - 软硬件资源管理
          - 硬件资源管理
          - 软件资源管理
    - 有哪些指标可以用来测量软件过程质量？
      collapsed:: true
      - 缺陷发现率
        collapsed:: true
        - 缺陷发现的频率
        - 计量单位
          - bug/KLOC
            - KLOC是指千行代码
            - 每千行代码平均产生的缺陷数量
            - 这个数据不仅可以用来衡量产品的 质量，也可以用来衡量过程的质量
          - 产品的质量越差，缺陷率越高;
            过程质量(相反)，质量越差，缺陷率越低
            - **当统计的缺陷发现率较低时，需要从多方面考虑原因**
              - 产品质量很好以致很难发现产品中的缺陷，从而造成缺陷率偏低
              - 工作的方法和策略不当，造成不能发现产品中的缺陷
      - 质量成本
        collapsed:: true
        - 产品成本的一部分
        - 定义
          collapsed:: true
          - 将产品质量保持在规定的水平上所需的费用
        - 包括
          - 预防成本
          - 鉴定成本
          - 内部 / 外部 损失成本
      - 过程缺陷密度
        collapsed:: true
        - 它是一种度量标准
        - 判定过程产品的质量以及检验过程的执行程度
        - $DIPF=Dn/Sp$
          - $Dn$ 是被发现的缺陷数
          - $Sp$ 是指被测试的软件产品规模
      - 缺陷到达模式, 产品的缺陷密度、或者测试阶段的缺陷率是一个概括性指标
        - 用于整个软件开发周期或某个特定的开发阶段
        - 扩展到对于修正的和关闭的缺陷，获取有关开发工作人员工作效率、缺陷修正进程和质量进程等方面的信息
    - 将 项目过程的集成管理 和 产品集成的过程管理 进行对比，找出他们的共同点和不同点
      collapsed:: true
      - 焦点
        collapsed:: true
        - 项目过程集成管理
          - 组织单元之间关系的协调和处理
        - 产品集成管理
          - 产品构件接口标准、约定和验证
      - 相同点
        collapsed:: true
        - 都需要制定集成管理的管理规范，过程
        - 需要制定一个过程计划
        - 根据需求者，利益者的要求，设计相关需求文档
        - 任务和进度都要按照过程计划进行，安排
        - 要每日的识别、跟踪和解决问题，持续集成
      - 不同点
        collapsed:: true
        - 产品过程管理需要
          - 符合国内或国际标准的接口规范设计规格
          - 接口先行设计
          - 项目必须按照组织标准软件过程来制定项目计划
        - 项目过程集成需要
          - 协调各相关利益者的关系
          - 有其他必要的项目管理内容，技术活动
    - 举一个例子，如何运用 IPD 提高产品集成的质量
      collapsed:: true
      - 华为是国内第一家引进和实施 IPD 的公司，也是受益最大的国内企业。
      - 华为 IPD 可以分为两个大的阶段
        collapsed:: true
        - IBM 介入之前
        - IBM 介入之后
      - IPD 组成
        - 主要由**固化的结构化研发流程**和**支持流程实施的跨部门团队**组成
          collapsed:: true
          - 以前华为的产品开发完全是研发部门的事情，技术方向由关键人物来选择。在 IPD 模式下，各部门都要有人参与到规划和实施的过程里，组成跨部门的团队,IPMT 与 PDT（IPT）。
          - 跨部门的团队基本上要在产品开发之前做出相关联的规划，并且在产品开发的过程中相互协调，以保证这个产品从始至终都是技术领先、成本合理并且符合市场需求。
          - 华为共有约一百多个产品线，类似的产品线再一起组成一个大的产品线。每个大的研发产品线都有一个 IPMT，他们是由总监级（现在改为产品线总裁）或者资深的产品专家 组成，负责对旗下各个产品线的研发活动作关键环节（立项评估，计划决策，实验局评估等） 的监控和评估。
          - 监控和评估的主要依据就是看这个产品研发成本投入和未来市场效益的比 较，以及技术、资金、人力等方面的可行性。
        - **决策评审点**
          - 决策评审点实际上是一种喇叭口的结构。也就是通过仔细的调查、研究和分析之后筛选出最有潜力的项目，并且在“动手”之 前尽可能地进行“瞄准”和计算“提前量”。使得最后进入开发阶段的项目都是最健康和最明确的。应该说这种研发管道管理，是华为在以前最欠缺的。
        - **异步开发模式**
          - IPD在开发过程中为华为第一次引进了“异步开发”的概念。这种流程实际上很好地使用了并行工程的思想，它比华为原来串行研发流程的效率要高很多
    - 模拟题
      - 名词解释
        collapsed:: true
        - 软件过程
          collapsed:: true
          - 软件⽣存周期所涉及的⼀系列相关过程
          - 过程是活动的集合, 活动是任务的集合
            - 任务要起着把输⼊进⾏加⼯然后输出的作⽤
            - 活动的执⾏可以是顺序的, 重复的, 并⾏的, 嵌套的或者是有条件地引发的
        - IBM-Raional 统⼀过程 (RUP）
          collapsed:: true
          - 定义了⼀系列的过程元素，如⾓⾊, 活动和产物，通过适当的组合，能够帮助软件开发组织有效地管理软件过程
        - 软件过程成熟度
          collapsed:: true
          - ⼀个特定的软件过程被定义, 管理, 度量, 控制和有效性的程度
        - 项⽬定义软件过程
          collapsed:: true
          - 对项⽬所⽤软件过程的可操作的定义
          - ⼀个已很好特征化的和已理解的软件过程
          - ⽤软件标准, 规程, ⼯具和⽅法予以描述.
        - 软件过程评估
          collapsed:: true
          - 根据过程评估模型以⼀系列的标准为依据，进⾏相应的检查并判断在质量, 成本和进度等多⽅⾯控制的过程能⼒.
          - 涉及过程评估的⽬标, 内容, ⽅式和⽅法
        - 过程规范
          collapsed:: true
          - 是⼈们需要遵守的约定和规则，包括已定义的操作⽅法, 流程和⽂档模板. 软件过程在整个软件开发的过程中约束着开发流程按⼈们预定进⾏，软件过程会不会对软件过程的创新, 技术创新有约束，产⽣消极的影响呢？没有⼀点影响是 不可能的，创新和约束⼀直都是对⽴的，约束得死，创新能⼒就会变弱. 但是如果过程规范制定得好的话，约束不是绝对的.
        - 微软软件框架 (MSF)
          collapsed:: true
          - 基于⼀套制定好的原理, 模型, 准则, 概念和指南⽽形成的⼀种成熟的, 系统的技术项⽬规划,  构建和部署的指导体系.
        - 团队软件过程
          collapsed:: true
          - 团队软件过程 (Team Software Process ，简称 TSP) 是为开发软件产品的开发团队提供指导， TSP 的早期 实践侧重于帮助开发团队改善其质量和⽣产率，以使其更好的满⾜成本及进度的⽬标.
        - 缺陷
          collapsed:: true
          - 缺陷是指程序中存在的错误，例如语法错误, 标点符号错误或者是⼀个不正确的程序语句，是任何影响程序完整⽽ 有效的满⾜⽤户要求的东西，是可以表⽰, 描述和统计的客观事物.
        - 软件过程剪裁
          collapsed:: true
          - 参照业界的标准 (如 CMMI) ，根据组织⾃⾝实际情况进⾏调整来量⾝定做，叫软件过程剪裁.
        - 软件能⼒成熟度模型 (CMM/CMM)
          - CMM 是指 “ 能⼒成熟度模型 ” ，其英⽂全称为 Capability Maturity Model for Software， 英⽂缩写为SW-CMM ，简称 CMM . 它是对于软件组织在定义, 实施, 度量, 控制和改善其软件过程的实践中各个发展阶段的描述. CMM 的核⼼是把软件开发视为⼀个过程，并根据这⼀原则对软件开发和维护进⾏过程监控和研究，以使其更加科学化, 标准化, 使企业能够更好地实现商业⽬标.
        - 软件过程能⼒
          collapsed:: true
          - 软件过程能⼒是软件过程本⾝具有的按预定计划⽣产产品的固有能⼒，或者说是遵循软件过程能够实现预 期结果的程度.
        - 组织过程焦点
          collapsed:: true
          - 规定软件开发组织在改进其总体软件过程能⼒的过程活动中的职责. 组织过程焦点活动所得到的是⼀组软件过程财富，它们在组织的过程定义中被描述. 这些财富如集成软件管理中所述，是供各个软件项⽬使⽤.
        - 变更控制
          collapsed:: true
          - 变更控制是通过对变更请求 (Change Request ，简称 CR) 进⾏分类, 追踪和管理的过程来实现的.
        - MSF 的过程模型
          collapsed:: true
          - 过程模型是 MSF 中⼀个⾮常重要的内容，分为构思 (规划）阶段，计划 (设计）阶段，开发阶段，稳定 阶段，部署阶段，通过每个阶段交付不同的成果，可以促进项⽬的依次交付，增加项⽬的可预见性和可控制性，使最终项⽬成 果与预期⽬标保持⼀致，各个阶段的衔接也给项⽬提供⼀个从开始到结束的过渡.
        - 个体软件过程 (PSP)
          collapsed:: true
          - 个体软件过程 (PSP) 是⼀种可⽤于控制, 管理和改进个⼈⼯作⽅式的⾃我持续改进过程，是⼀ 个包括软件开发表格, 指南和规程的结构化框架.
        - 软件过程性能
          collapsed:: true
          - 表⽰遵循软件过程所得到或软件过程执⾏的实际结果.
        - 标准软件过程
          collapsed:: true
          - 组织标准软件过程是基本过程的可操作的定义，基本过程指导在组织中建⽴⼀个针对所有软件项⽬的共⽤ 的软件过程，是项⽬定义软件过程的基础.
        - 评审
          collapsed:: true
          - 评审是对软件元素或者项⽬状态的⼀种评估⼿段，以确定其是否与计划的结果保持⼀致，并使其得到改进.
        - 软件过程度量
          collapsed:: true
          - 软件过程度量是收集, 分析和解释关于过程的定量信息，是软件过程评估和改进的基础. 基于度量可以更好地⽤数据来描述软件过程的能⼒, 效率和质量等.
      - 简答题
        - 软件过程的有哪些分类？
          collapsed:: true
          - 软件基本过程
            collapsed:: true
            - 软件获取
            - 供应
            - 开发
            - 运⾏
            - 维护
            - 包括
              - 需求分析
              - 软件设计
              - 编码等
          - 软件⽀持过程
            collapsed:: true
            - 对软件主要过程提供⽀持的过程
            - 包括
              - ⽂档编制过程
              - 配置管理过程
              - 质量保证过程
              - 验证和确认过程（测试过程）
              - 评审过程等
          - 软件组织过程
            collapsed:: true
            - 对软件主要过程和⽀持过程的组织保证过程
            - 包括
              - 管理过程
              - 基础设施过程
              - 改进过程
              - 培训过程
        - 能⼒成熟度模型的基本出发点是什么？能⼒成熟度模型由哪些部分组成？
          collapsed:: true
          - ⼀种⽤于评价软件承包商能⼒并帮助改善软件质量的⽅法
          - 帮助软件企业对软件⼯程过程进⾏管理和改进，增强开发与改进能⼒，从⽽能按时地、不超预算地开发出⾼质量的软件
          - 想法是
            - 只要集中精⼒持续努⼒去建⽴有效的软件⼯程过程的基础结构，不断进⾏管理的实践和过程的改进，就可以克服软件⽣产中的困难
          - CMM 建⽴了⼀个软件过程能⼒成熟度的分级标准，为软件过程不断改进奠定了循序渐进的基础
            - 初始级（Initial）
            - 可重复级（Repeatable）
            - 已定义级（Defined）
            - 已管理级（Managed）
            - 优化级（Optimizing）
        - 评审⽅法有哪些？
          collapsed:: true
          - 临时评审（Adhoc review ）
            collapsed:: true
            - 最不正式的，通常应⽤于⼩组合作
          - 轮查（Passroud）/ 分配审查⽅法
            collapsed:: true
            - 作者将需要评审的内容发给各位评审员，并收集他们的反馈意见，缺点是不太及时
          - ⾛查（Walkthrough）
          - ⼩组评审（Group Review）
          - 审查（Inspection ）
        - 软件过程成熟的标准?
          collapsed:: true
          - 软件过程
            - **能⼒**⾼，具有全组织范围的管理软件开发和维护过程的能⼒。
            - **性能可预见性**，对进度、预算和质量做出现实的和准确的估计和预测
            - **规范化**，可遵循的标准、规则和指导性原则
            - **⼀致性**
            - **丰富性**
            - 可视性软件组织的能⼒是已知的, **具有清晰的、充分的定义**
            - **稳定性**
            - **不断改进**
        - 能力成熟度模型 CMM (Capability Maturity Model of Software) 的 4 项基本元素是什么？
          collapsed:: true
          - 成熟度等级
            collapsed:: true
            - CMM 划分为五个等级，描述了每个等级的组织过程特征
              - 每个等级代表⼀种组织的过程能⼒等级
            - 指明了组织级过程改进的整体策略（关注于那些过程域）
          - 关键过程域（KPA）
            collapsed:: true
            - 每个等级包括⼏个过程域，说明了在⼀个等级中必要的过程
            - 是⼀组学科或者逻辑上紧密联系的活动的集合。
          - ⽬标
            collapsed:: true
            - 每个过程域均有⾃⼰的⽬标，这些⽬标⽤于⽀持过程能⼒等级特征。
          - 关键实践（KP）
            collapsed:: true
            - 组成⼀个过程域的活动，从逻辑上描述了实现这个过程域⽬标必须或者推荐执⾏的活动
            - 属于具体的操作指导
        - 软件缺陷的作⽤?
          collapsed:: true
          - 通过缺陷分析，发现各种类型缺陷发⽣的概率，掌握缺陷集中的区域、明晰缺陷发展趋势、了解缺陷产⽣主要原因。
- ---
- Outline `软件过程 +`
  - 1. 规范 (*)
    - 过程的定义
      collapsed:: true
      - 过程的定义
      - 软件过程的分类和组成
      - 软件过程定义的层次性
    - 过程规范
      collapsed:: true
      - 什么是过程规范
      - 过程规范的内容和示例
      - 过程规范的影响和作用
    - 软件生命周期的过程需求
      collapsed:: true
      - 软件工程过程
      - 软件支持过程
      - 软件管理过程
      - 软件组织过程
      - 软件客户－供应商的过程
    - ==软件生命周期标准== | **软件声明、周期标准**
      collapsed:: true
      - 国际标准 / 指南性标准
        - ISO／IEC 标准体系
          - 一系列覆盖软件生命周期活动过程的标准
          - 两个代表
            - ISO／IEC12207
              - 1995 — **软件生存周期过程**
              - 多个角度说明了软件生命周期各个过程中的活动
                - 指导作用 -> 规范软件开发过程，协调各类人员之间的关系
            - ISO／IEC15504
              - **软件过程评估标准**
              - 推荐软件工程实践方法，建立统一的软件过程评估的判断基础
              - 期望在世界范围内确保软件过程评估结果具有一定的可比性
              - 提供模式 (3)
                - 能力确定模式
                  - 帮助 评估并确定一个**潜在软件供应商的能力**
                - 过程改进模式
                  - 提高 **软件开发过程的水平**
                - 自我评估模式
                  - 判断是否能 **承接新项目的开发**
              - 针对软件不同类型的组织实现目标
                - 购买方
                  - 评估软件供应商的能力，并预测选择风险
                - 获取者
                  - 判断软件供应商当前以及潜在的软件过程能力
                - 软件供应商
                  - 用一个过程评估计划代替多个计划
                  - 判断决定其软件过程当前以及潜在的能力 => 改进范围 / 优先级
                  - 框架化软件过程改进的实施步骤
                - 软件开发组织
                  - 标准可作为一种工具用于建立最初的过程改进并推进持续的过程改进活动
          - ![image.png](../assets/imu/sp/image_1661318630776_0.png)
        - IEEE 标准体系
          - 由软件工程标准工作小组 (Software Engineering Standards Subcommittee，**SESS**) 创立
            collapsed:: true
            - 隶属于软件工程技术委员会 (Technical Committee on Software Engineering，TCSE)
          - 每一种标准下细分
            - 需求标准 (requirement standards)
            - 建议惯例 (recommended practices)
            - 指南 (guides)
          - 顾客标准
            - 软件获得 (software acquisition) .
            - 软件安全 (software safety) .
            - 软件需求 (system requirements) .
            - 软件生命周期流程 (software life cycle processes) .
          - 流程标准
            - 软件质量保证 (software quality assurance) .
            - 软件配置管理 (software configuration management) .
            - 软件单元测试 (software unit testing) .
            - 软件验证与确认 (software verification andvalidation) .
            - 软件维护 (software maintenance) .
            - 软件项目管理 (software project management) .
            - 软件生命周期流程 (software life cycle processes) .
          - 产品标准
            - 软件可靠性度量 (measures to produce reliable software) .
            - 软件质量度量 (software quality metrics) .
            - 软件用户文档 (software user documentation) .
          - 资源与技术标准
            - 软件测试文件 (software test documentation) .
            - 软件需求规格 (software requirements specifications) .
            - 软件设计描述 (software design descriptions) .
            - 再用链接库的运作概念 (concept of operations for interoperating reuse libraries) .
            - 辅助工具的评估与选择 (evaluation and selection of case tools) .
          - 常用的IEEE软件过程标准
            - IEEE1074：1997. 生命周期过程的标准.
            - IEEE1540—01. 软件风险管理.
            - 1EEE1517—99. 软件复用过程.
            - IEEE1219—1998. 软件维护过程.
            - IEEE Std730—2001. 软件质量保证计划.
          - 软件过程管理
            - IEEE Std1012. 验证与确认.
            - IEEE Std1028. 评审.
      - 国内标准 / 强制性标准
      - 美国软件生产力公司 (Software Productivity Consortium NFP) 总结了目前已有的标准, 根据其演变, 发展的历史过程, 绘制了一张标准体系的全貌图
        collapsed:: true
        - ![image.png](../assets/imu/sp/image_1661322309750_0.png)
    - 软件过程建模
      collapsed:: true
      - 软件过程建模型
      - 基于UML的过程建模
      - 基于IDEF3的过程建模
      - 基于Agent的自适应软件过程模型
      - 基于SOA的软件过程模型
  - 2. 成熟度
    - 过程成熟度标准
      collapsed:: true
      - 软件过程不成熟的特点
      - 软件过程成熟的标准
    - 能力成熟度模型概述
      collapsed:: true
      - CMM的基本内容
      - 系统工程能力模型
      - 集成化产品开发模型
      - CMMI介绍
    - 过程成熟度级别
      collapsed:: true
      - 成熟度等级的行为特征
      - 理解成熟度等级
      - 成熟度等级的过程特征
      - CMMI过程域
      - CMM和CMMI过程域的比较分析
    - 软件过程的可视性
    - 过程能力和效能预测
    - 软件过程框架
      collapsed:: true
      - 软件过程环境和过程框架
      - 软件过程文化
      - PSP/TSP和CMM组成的软件过程框架
  - 3. 组织管理
    - 组织过程焦点
      collapsed:: true
      - 组织过程焦点的基础
      - 组织过程焦点的活动
      - 组织过程焦点的评估
    - 组织过程定义
      collapsed:: true
      - 软件过程定义基础
      - 剪裁标准软件过程的指南和准则
    - PSP过程框架和成熟度模型
      collapsed:: true
      - PSP原则和思想
      - PSP过程框架
      - PSP成熟度模型
    - PSP设计与实践
      collapsed:: true
      - PSP0/PSP  - --------个体度量过程
      - PSP1/PSP  - --------个体计划过程
      - PSP2/PSP  - --------个体质量管理过程
      - PSP3--------个体循环过程
    - TSP的结构和启动过程
      collapsed:: true
      - TSP的原则和思想
      - TSP结构
      - TSP启动过程
    - TSP工作流程
      collapsed:: true
      - 策略和计划
      - 需求
      - 设计和实现
      - 测试和后期维护
  - 4. 需求管理
    - 需求管理的模型和流程
      collapsed:: true
      - 软件需求工程概述
      - 需求过程系统模型
    - 需求开发
      collapsed:: true
      - 需求获取的过程和方法
      - 基于用例的需求获取和分析
      - 需求定义
    - 需求管理
      collapsed:: true
      - 需求确认
      - 需求跟踪
      - 需求变更控制
  - 5. 技术管理
    - 软件过程的技术架构
      collapsed:: true
      - 过程技术架构的层次和内容
      - 软件过程资源的管理
    - 软件过程的问题分析和决策方法
      collapsed:: true
      - 过程问题解决的系统方法
      - 原因分析和缺陷分析
      - 决策分析与决定
    - 软件过程的技术路线
      collapsed:: true
      - 软件项目过程的技术解决流程
      - 技术解决计划的建立和实施
      - 开发设计
      - 编程和单元测试
      - 验证、确认与测试
    - 知识传递
    - 软件过程管理工具
      collapsed:: true
      - 需求管理工具
      - 面向对象的分析设计工具
      - 配置管理和变更管理工具
  - 6. 项目管理 (*)
    - ==软件配置管理(SCM, Software Configuration Management)==
      - 任务 / 定义
        - 管理软件的变化
      - 基本概念
        - 配置
          - 在技术文档中明确说明最终组成软件产品的**功能或物理属性**
          - 包括 (更多的内容, 易变性)
            - 即将受控的所有产品特性, 内容, 相关文档
            - 软件版本
            - 变更文档
            - 软件运行的支持数据
            - 其他一切保证软件一致性的组成要素
        - 配置项
          - 在软件生存周期内所产生的各种应纳入管理范围的系统构成成分
            - 软件开发过程中出现的许多独立的**信息项**, 需要得到妥善管理, 以便后续使用
              - 逻辑上组成软件系统的各组成成分
          - 确定配置项 == 决定哪些文档需要被保存、管理
            - 技术性文档随着开发而演化, 相互衔接, 后期版本对前期的修正和扩展，具有继承关系
          - 包括
            - 各种管理文档和技术文档
            - 源程序与目标代码
            - 运行所需的各种数据等（配置管理的资源对象）
        - 基线 baseline / 里程碑 milestone
          - 评审和认可过的一组软件配置项, 作为下一步开发的基础
          - 在这些特定点上，阶段工作已结束，并且已经取得了正式的阶段性产品
        - 配置管理库 / 受控库
          - 用于存储软件配置项以及相关配置管理信息
      - 工作流程
        - ![image.png](../assets/imu/sp/image_1661324395755_0.png)
        - 软件配置控制
          - 软件配置管理的**核心工作**
          - 包含方面
            - 存取控制
              - 设定了软件开发人员**对软件基准库的存取权限**
              - 软件开发过程及软件产品的**一致性和安全性**
                - 使得组织在任何时刻都可获得配置项的任何一个版本
            - 版本控制
              - 记录了软件系统的中间状态，**避免软件开发行为出现混乱或失控的情况**
              - 便于软件开发工作**以基线渐进方式进行**
            - 变更控制
              - 为软件产品变更提供了一个明确的流程
              - 要求任何进行配置管理的软件产品变更都要经过相应的授权与批准才能实施
            - 产品发布
              - **保证**了提交给客户的软件产品是**完整的、正确的**
      - 基线控制
        - 项目存储库中每个工件版本在特定时期的一个**快照 (snapshot)**
        - 配置项分为
          - 基线配置项
            - 设计文档
            - 源程序
          - 非基线配置项
            - 项目的各类计划和报告
        - 优点
          - 为了把各个阶段的工作划分得更加明确
            - 使得本来连续开展的软件工作在这些点上被割开
            - 有利于检验和肯定阶段性的成果
          - 变更控制
            - 有了基线的规定后，就可以禁止跨越里程碑去修改另一阶段“已冻结”的工作成果
        - ![image.png](../assets/imu/sp/image_1661324444053_0.png)
          - “需求基线”
            - 软件过程中的第一条基线
            - 整个软件生命周期的起点和终结点
          - 跨越的需求视作被“冻结”, 原则上不允许轻易变更
            - 以需求基线为例, 用户可能会提出新的需求，即需求发生了变化; 但是如果项目的进展已经跨越了需求基线，开始进行设计工作，那么，需求的变更需要受到严格的控制，原则上不允许轻易变更。
      - 版本控制
        - 版本的访问和同步控制
          - ![image.png](../assets/imu/sp/image_1661324947374_0.png)
            - 根据**经批准**的变更请求和变更实施方案，软件工程师从配置库中检出要变更的配置对象
              - 存取控制功能保证了软件工程师有检出该对象的权限
              - 同步控制功能则锁定了项目数据库中的这个对象，使得当前检出的版本在没有被置换前不能再更新它
              - 当然，对这个对象还可以检出另外的副本，但是对它不能更新。
            - 软件工程师在对这种成为基线的对象做了变更，并经过适当的软件质量保证和测试之后，把修改的版本检入配置库，再解锁。
        - 版本的分支
        - 版本的合并
        - 变更请求控制 (7)
          - ![image.png](../assets/imu/sp/image_1661324966442_0.png)
            - 提交
            - 接受
            - 评估
            - 决策
            - 实现
            - 验证
            - 完成
    - 项目估算和资源管理
      - 规模度量
      - 成本估算
      - 资源管理
    - 项目风险评估
      - 风险识别
      - 风险分析和评估
    - 制定项目计划
      - WBS-工作分解结构
    - 项目跟踪和监督
      - 项目跟踪的重要性
  - 7. ==软件质量管理 (*)== via: ((6305e7eb-0fd0-4a17-80be-4e269738a37e))
    - 7.1 质量管理概述
      - 缺陷的消除并不能真正保证软件的质量，更重要的是缺陷的预防和管理
      - ![image.png](../assets/imu/sp/image_1661330135275_0.png)
        - 需要制定项目的**质量计划**
        - 在软件开发的过程中，需要进行**技术评审**和**软件测试**，并进行**缺陷跟踪**
        - **对整个过程进行检查**，并进行有效的过程改进，以便在以后的项目中进一步提高软件质量
    - 7.2 软件质量方针和计划
      - ? 软件质量方针
      - 质量计划
        - 制定步骤
          - 编制
          - 实施
          - 检查调整
          - 总结
        - 目的
          - 确保项目的质量标准能够得以满意的实现
        - 关键
          - 在项目的计划期内确保项目按期完成
          - 处理与其他项目计划之间的关系
        - 方法和技术
          - 利益/成本分析
          - 基准
          - 流程图
          - 试验设计
      - 项目质量计划工作在项目管理，特别是项目质量管理中具有非常重要的地位和指导作用。
        - 加强项目的质量计划，可以充分体现项目质量管理的目的性。
          - 有利于克服质量管理工作中的盲目性和随意性，从而增加工作的主动性、针对性和积极性，对确保项目工期、降低项目成本和圆满实现项目质量目标将会产生积极的促进作用
    - 7.3 ?软件评审过程和方法
      - 角色和责任
      - 软件评审过程
      - 软件评审方法
    - 7.4 ?缺陷分析和预防
      - 缺陷分析
      - 鱼骨图
      - 缺陷预防
    - 7.5 质量度量
      - 度量要素
      - 基于缺陷的质量度量
    - 7.6 PSP过程质量管理
      - 过程质量度量
      - 缺陷移除和预防
    - 背景
    - 意义
    - 作用
  - 8. 集成管理
    - 集成项目管理
      collapsed:: true
      - 项目过程的集成管理
      - 集成管理流程
    - 集成项目的合成计划
      collapsed:: true
      - 合成项目计划
      - 合成项目计划的管理
      - 合成项目计划的实施
      - 组间协调
    - 产品集成的过程管理
      collapsed:: true
      - 软件产品工程
      - 产品集成的管理流程
      - 软件产品工程的实践
    - 集成产品开发模式
      collapsed:: true
      - IPD产生的背景
      - 产品及周期优化方法
      - IPD核心思想
      - IPD的过程框架模式
    - IPD方法应用和实践
      collapsed:: true
      - IPD的方法体系
      - IPD的方法启动和建立
      - 市场过程管理
      - 流程重整
      - 产品重整
      - 新产品开发
  - 9. 评估和改进
    - 过程模型的剪裁
      collapsed:: true
      - 软件开发组织的类型
      - CMMI表示方法
      - 模型剪裁的用途
      - 连续式表示模型的剪裁
    - 软件过程度量
      collapsed:: true
      - 过程度量的内容
      - 过程度量的流程
      - 过程度量的方法
      - 过程度量技术
      - 过程能力度量
      - 软件过程生产率的度量
    - 过程评估参考模型
      collapsed:: true
      - ISO/IEC 15504评估模型
      - Bootstrap评估模型
      - Trillium评估模型
      - CMM/CMMI的评估体系
    - 过程评估
      collapsed:: true
      - 软件过程评估的目标和期望
      - 软件过程评估的内容和范围
      - 软件过程评估的方式和类型
      - 软件过程评估的方法
    - 过程改进的模型和方法
      collapsed:: true
      - 质量改进范例
      - 过程改进的 IDEAL模型
      - 过程改进的 Raytheon方法
      - 过程改进的 6 Sigma方法
    - 组织和技术革新
    - 软件过程改进的实施
      collapsed:: true
      - 过程改进的原则和策略
      - 过程改进的组织支持
      - 过程改进计划
      - 过程改进的具体实施步骤
      - 软件过程改进的自动化实现
  - 10. 管理实践
    - IBM-Rational 业务驱动开发的过程管理
      collapsed:: true
      - RUP的迭代过程
      - 提高过程的适应性
      - 需求开发和质量改进
      - 架构设计和组件复用
      - 跨团队协作
      - 过程实施的最佳实践
    - 微软公司的软件开发过程模式
      collapsed:: true
      - MSF的过程模型
      - MSF的团队模型
      - MSF过程模型的特点和原则
      - MSF过程模型的应用
    - 敏捷模型的软件过程管理
      collapsed:: true
      - 敏捷方法的过程模型
      - 敏捷过程的最佳实践
    - 面向构件的软件过程
      collapsed:: true
      - 面向构件软件过程的思想
      - 面向构件软件过程的阶段划分
    - 软件过程的自定义体系
      collapsed:: true
      - 过程模式的对比分析
      - 自我定义的理想管理过程
- ---
- More
  - [[software/process]]
- Refs
  - 软件过程管理 - 朱少民 - 清华大学出版社 - 2007-4
    isbn:: 9787302146407
    source:: https://book.douban.com/subject/2035607
  - [软件过程与管理总复习_一指流沙q的博客-CSDN博客](https://blog.csdn.net/qq_51165234/article/details/125250711)
  - [软件过程与管理复习题_一指流沙q的博客-CSDN博客_软件过程管理期末考试题](https://blog.csdn.net/qq_51165234/article/details/125234900)
    collapsed:: true
    - 选择题
  - [华为引入IPD的背景及实施 | 课程笔记](https://www.sohu.com/a/228480543_283333)
  - [软件过程之软件成熟度模型（CMM）_wx5d42b021b4f1f的技术博客_51CTO博客](https://blog.51cto.com/u_14479502/3117001)
  - [软件缺陷是什么以及缺陷的管理 - 腾讯云开发者社区-腾讯云](https://cloud.tencent.com/developer/article/1647103)
-