title:: PKUFlyingPig/cs-self-learning
tags:: #github #opensource #tutorial  #programming #roadmap/develop
created:: [[20230324]]
mark:: [计算机自学指南](https://github.com/PKUFlyingPig/cs-self-learning) ![](https://img.shields.io/github/stars/PKUFlyingPig/cs-self-learning)；[CS自学指南](https://csdiy.wiki/)

  - > *Everyone should enjoy CS if you have a good teacher to teach you a good course.*
    ![](https://raw.githubusercontent.com/PKUFlyingPig/cs-self-learning/master/docs/images/title.png)
- ## Contents
  - [前言](https://csdiy.wiki/)
  - [如何使用这本书](https://csdiy.wiki/%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97/)
    background-color:: red
    - ## ~~初入校园~~
    - ## 删繁就简
      background-color:: red
      id:: 6424f288-6c3f-46fc-b424-10131d09f0f3
      - 如果你已经本科毕业开始读研或者走上了工作岗位，亦或是从事着其他领域的工作想要利用业余时间转码，那么你也许并没有充足的业余时间来系统地学完 [一份仅供参考的CS学习规划](https://csdiy.wiki/CS%E5%AD%A6%E4%B9%A0%E8%A7%84%E5%88%92/) 里的内容，但又想弥补本科时期欠下的基础。考虑到这部分读者通常有一定的编程经验，入门课程没有必要再重复学习。而且从实用角度来说，==由于工作的大体方向已经确定，确实没有太大必要对于每个计算机分支都有特别深入的研究，更应该侧重一些通用性的原则和技能==。因此我结合自身经历，选取了个人感觉最重要也是质量最高的几门核心专业课，希望能更好地加深读者对计算机的理解。学完这些课程，无论你具体从事的是什么工作，我相信你将不可能沦为一个普通的调包侠，而是对计算机的底层运行逻辑有更深入的了解。
      - | 课程方向 | 课程名 |
        | ---- | ---- | ---- |
        | 离散数学和概率论 | [UCB CS70 : discrete Math and probability theory](https://csdiy.wiki/%E6%95%B0%E5%AD%A6%E8%BF%9B%E9%98%B6/CS70/) |
        | 数据结构与算法 | [Coursera: Algorithms I & II](https://csdiy.wiki/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E4%B8%8E%E7%AE%97%E6%B3%95/Algo/) |
        | 软件工程 | [MIT 6.031: Software Construction](https://csdiy.wiki/%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B/6031/) |
        | 全栈开发 | [MIT web development course](https://csdiy.wiki/Web%E5%BC%80%E5%8F%91/mitweb/) |
        | 计算机系统导论 | [CMU CS15213: CSAPP](https://csdiy.wiki/%E4%BD%93%E7%B3%BB%E7%BB%93%E6%9E%84/CSAPP/) |
        | 体系结构入门 | [Coursera: Nand2Tetris](https://csdiy.wiki/%E4%BD%93%E7%B3%BB%E7%BB%93%E6%9E%84/N2T/) |
        | 体系结构进阶 | [CS61C: Great Ideas in Computer Architecture](https://csdiy.wiki/%E4%BD%93%E7%B3%BB%E7%BB%93%E6%9E%84/CS61C/) |
        | 数据库原理 | [CMU 15-445: Introduction to Database System](https://csdiy.wiki/%E6%95%B0%E6%8D%AE%E5%BA%93%E7%B3%BB%E7%BB%9F/15445/) |
        | 计算机网络 | [Computer Networking: A Top-Down Approach](https://csdiy.wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/topdown/) |
        | 人工智能 | [Harvard CS50: Introduction to AI with Python](https://csdiy.wiki/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD/CS50/) |
        | 深度学习 | [Coursera: Deep Learning](https://csdiy.wiki/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/CS230/) |
    - ## 心有所属
      collapsed:: true
      - 如果你对于计算机领域的核心专业课都掌握得相当扎实，而且已经确定了自己的工作或研究方向，那么书中还有很多未在 [一份仅供参考的CS学习规划](https://csdiy.wiki/CS%E5%AD%A6%E4%B9%A0%E8%A7%84%E5%88%92/) 提到的课程供你探索。
  - [一个仅供参考的CS学习规划](https://csdiy.wiki/CS%E5%AD%A6%E4%B9%A0%E8%A7%84%E5%88%92/)
    collapsed:: true
    - 不过，在开始学习之前，先向小白们强烈推荐一个科普向系列视频 [Crash Course: Computer Science](https://www.bilibili.com/video/BV1EW411u7th)，在短短 8 个小时里非常生动且全面地科普了关于计算机科学的方方面面：计算机的历史、计算机是如何运作的、组成计算机的各个重要模块、计算机科学中的重要思想等等等等。正如它的口号所说的 *Computers are not magic!*，希望看完这个视频之后，大家能对计算机科学有个全貌性地感知，从而怀着兴趣去面对下面浩如烟海的更为细致且深入的学习内容。#crashcourse/computerscience
    - ## 必学工具
      collapsed:: true
      - > 俗话说：磨刀不误砍柴工。如果你是一个刚刚接触计算机的24k纯小白，学会一些工具将会让你事半功倍。
      - 学会提问：也许你会惊讶，提问也算计算机必备技能吗，还放在第一条？我觉得在开源社区中，学会提问是一项非常重要的能力，它包含两方面的事情。其一是会变相地培养你自主解决问题的能力，因为从形成问题、描述问题并发布、他人回答、最后再到理解回答这个周期是非常长的，如果遇到什么鸡毛蒜皮的事情都希望别人最好远程桌面手把手帮你完成，那计算机的世界基本与你无缘了。其二，如果真的经过尝试还无法解决，可以借助开源社区的帮助，但这时候如何通过简洁的文字让别人瞬间理解你的处境以及目的，就显得尤为重要。推荐阅读[提问的智慧](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/main/README-zh_CN.md)这篇文章，这不仅能提高你解决问题的概率和效率，也能让开源社区里无偿提供解答的人们拥有一个好心情。
        [MIT-Missing-Semester](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/MIT-Missing-Semester/) 这门课覆盖了这些工具中绝大部分，而且有相当详细的使用指导，强烈建议小白学习。不过需要注意的一点是，在课程中会不时提到一些与开发流程相关的术语。因此推荐至少在学完计算机导论级别的课程之后进行学习。
        [翻墙](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/%E7%BF%BB%E5%A2%99/)：由于一些众所周知的原因，谷歌、GitHub 等网站在大陆无法访问。然而很多时候，谷歌和 StackOverflow 可以解决你在开发过程中遇到的 99% 的问题。因此，学会翻墙几乎是一个内地 CSer 的必备技能。（考虑到法律问题，这个文档提供的翻墙方式仅对拥有北大邮箱的用户适用）。
        命令行：熟练使用命令行是一种常常被忽视，或被认为难以掌握的技能，但实际上，它会极大地提高你作为工程师的灵活性以及生产力。[命令行的艺术](https://github.com/jlevy/the-art-of-command-line/blob/master/README-zh.md)是一份非常经典的教程，它源于 Quora 的一个提问，但在各路大神的贡献努力下已经成为了一个 GitHub 十万 stars 的顶流项目，被翻译成了十几种语言。教程不长，非常建议大家反复通读，在实践中内化吸收。同时，掌握 Shell 脚本编程也是一项不容忽视的技术，可以参考这个[教程](https://www.shellscript.sh/)。
        IDE (Integrated Development Environment)：集成开发环境，说白了就是你写代码的地方。作为一个码农，IDE 的重要性不言而喻，但由于很多 IDE 是为大型工程项目设计的，体量较大，功能也过于丰富。其实如今一些轻便的文本编辑器配合丰富的插件生态基本可以满足日常的轻量编程需求。个人常用的编辑器是 VS Code 和 Sublime（前者的插件配置非常简单，后者略显复杂但颜值很高）。当然对于大型项目我还是会采用略重型的 IDE，例如 Pycharm (Python)，IDEA (Java) 等等（免责申明：所有的 IDE 都是世界上最好的 IDE）。
        [Vim](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/Vim/)：一款命令行编辑工具。这是一个学习曲线有些陡峭的编辑器，不过学会它我觉得是非常有必要的，因为它将极大地提高你的开发效率。现在绝大多数 IDE 也都支持 Vim 插件，让你在享受现代开发环境的同时保留极客的炫酷（yue）。
        [Git](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/Git/)：一款代码版本控制工具。Git的学习曲线可能更为陡峭，但出自 Linux 之父 Linus 之手的 Git 绝对是每个学 CS 的童鞋必须掌握的神器之一。
        [GitHub](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/GitHub/)：基于 Git 的代码托管平台。全世界最大的代码开源社区，大佬集聚地。
        [GNU Make](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/GNU_Make/)：一款工程构建工具。善用 GNU Make 会让你养成代码模块化的习惯，同时也能让你熟悉一些大型工程的编译链接流程。
        [CMake](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/CMake/)：一款功能比 GNU Make 更为强大的构建工具，建议掌握 GNU Make 之后再加以学习。
        [LaTex](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/LaTeX/)：~~逼格提升~~ 论文排版工具。
        [Docker](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/Docker/)：一款相较于虚拟机更轻量级的软件打包与环境部署工具。
        [实用工具箱](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/tools/)：除了上面提到的这些在开发中使用频率极高的工具之外，我还收集了很多实用有趣的免费工具，例如一些下载工具、设计工具、学习网站等等。
        [Thesis](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/thesis/)：毕业论文 Word 写作教程。
    - ## 好书推荐
      collapsed:: true
      - > 私以为一本好的教材应当是以人为本的，而不是炫技式的理论堆砌。告诉读者“是什么”固然重要，但更好的应当是教材作者将其在这个领域深耕几十年的经验融汇进书中，向读者娓娓道来“为什么”以及未来应该“怎么做”。
        [链接戳这里](https://csdiy.wiki/%E5%A5%BD%E4%B9%A6%E6%8E%A8%E8%8D%90/)
    - ## 环境配置
      collapsed:: true
      - > 你以为的开发 —— 在 IDE 里疯狂码代码数小时。
        实际上的开发 —— 配环境配几天还没开始写代码。
      - ### PC 端环境配置
        如果你是 Mac 用户，那么你很幸运，这份[指南](https://sourabhbajaj.com/mac-setup/) 将会手把手地带你搭建起整套开发环境。如果你是 Windows 用户，在开源社区的努力下，你同样可以获得与其他平台类似的体验：[Scoop](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/Scoop)。
        另外大家可以参考一份灵感来自 [6.NULL MIT-Missing-Semester](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/MIT-Missing-Semester/) 的 [环境配置指南](https://taylover2016.github.io/%E6%96%B0%E6%9C%BA%E5%99%A8%E4%B8%8A%E6%89%8B%E6%8C%87%E5%8D%97%EF%BC%88%E6%96%B0%E6%89%8B%E5%90%91%EF%BC%89/index.html)，重点在于终端的美化配置。此外还包括常用软件源（如 GitHub, Anaconda, PyPI 等）的加速与替换以及一些 IDE 的配置与激活教程。
      - ### 服务器端环境配置
        服务器端的运维需要掌握 Linux（或者其他类 Unix 系统）的基本使用以及进程、设备、网络等系统相关的基本概念，小白可以参考中国科学技术大学 Linux 用户协会编写的[《Linux 101》在线讲义](https://101.lug.ustc.edu.cn/)。如果想深入学习系统运维相关的知识，可以参考 [Aspects of System Administration](https://stevens.netmeister.org/615/) 这门课程。
        另外，如果需要学习某个具体的概念或工具，推荐一个非常不错的 GitHub 项目 [DevOps-Guide](https://github.com/Tikam02/DevOps-Guide)，其中涵盖了非常多的运维方面的基础知识和教程，例如 Docker, Kubernetes, Linux, CI-CD, GitHub Actions 等等。
    - ## 课程地图
      collapsed:: true
      - > 正如这章开头提到的，这份课程地图仅仅是一个**仅供参考**的课程规划，我作为一个临近毕业的本科生。深感自己没有权利也没有能力向别人宣扬“应该怎么学”。因此如果你觉得以下的课程分类与选择有不合理之处，我全盘接受，并深感抱歉。你可以在下一节[定制属于你的课程地图](https://csdiy.wiki/CS%E5%AD%A6%E4%B9%A0%E8%A7%84%E5%88%92/#yourmap)
        以下课程类别中除了含有 *基础* 和 *入门* 字眼的以外，并无明确的先后次序，大家只要满足某个课程的先修要求，完全可以根据自己的需要和喜好选择想要学习的课程。
      - ### 数学基础
        collapsed:: true
        - #### 微积分与线性代数
          作为大一新生，学好微积分线代是和写代码至少同等重要的事情，相信已经有无数的前人经验提到过这一点，但我还是要不厌其烦地再强调一遍：学好微积分线代真的很重要！你也许会吐槽这些东西岂不是考完就忘，那我觉得你是并没有把握住它们本质，对它们的理解还没有达到刻骨铭心的程度。如果觉得老师课上讲的内容晦涩难懂，不妨参考 MIT 的 [Calculus Course](https://csdiy.wiki/%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A1%80/MITmaths/) 和 [18.06: Linear Algebra](https://csdiy.wiki/%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A1%80/MITLA/) 的课程 notes，至少于我而言，它帮助我深刻理解了微积分和线性代数的许多本质。顺道再安利一个油管数学网红 [**3Blue1Brown**](https://www.youtube.com/c/3blue1brown)，他的频道有很多用生动形象的动画阐释数学本质内核的视频，兼具深度和广度，质量非常高。
        - #### 信息论入门
          作为计算机系的学生，及早了解一些信息论的基础知识，我觉得是大有裨益的。但大多信息论课程都面向高年级本科生甚至研究生，对新手极不友好。而 MIT 的 [6.050J: Information theory and Entropy](https://csdiy.wiki/%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A1%80/information/) 这门课正是为大一新生量身定制的，几乎没有先修要求，涵盖了编码、压缩、通信、信息熵等等内容，非常有趣。
      - ### 数学进阶
        collapsed:: true
        - #### 离散数学与概率论
          集合论、图论、概率论等等是算法推导与证明的重要工具，也是后续高阶数学课程的基础。但我觉得这类课程的讲授很容易落入理论化与形式化的窠臼，让课堂成为定理结论的堆砌，而无法使学生深刻把握理论的本质，进而造成学了就背，考了就忘的怪圈。如果能在理论教学中穿插算法运用实例，学生在拓展算法知识的同时也能窥见理论的力量和魅力。
          [UCB CS70 : discrete Math and probability theory](https://csdiy.wiki/%E6%95%B0%E5%AD%A6%E8%BF%9B%E9%98%B6/CS70/) 和 [UCB CS126 : Probability theory](https://csdiy.wiki/%E6%95%B0%E5%AD%A6%E8%BF%9B%E9%98%B6/CS126/) 是 UC Berkeley 的概率论课程，前者覆盖了离散数学和概率论基础，后者则涉及随机过程以及深入的理论内容。两者都非常注重理论和实践的结合，有丰富的算法实际运用实例，后者还有大量的 Python 编程作业来让学生运用概率论的知识解决实际问题。
        - #### 数值分析
          作为计算机系的学生，培养计算思维是很重要的，实际问题的建模、离散化，计算机的模拟、分析，是一项很重要的能力。而这两年开始风靡的，由 MIT 打造的 [Julia](https://julialang.org/) 编程语言以其 C 一样的速度和 Python 一样友好的语法在数值计算领域有一统天下之势，MIT 的许多数学课程也开始用 Julia 作为教学工具，把艰深的数学理论用直观清晰的代码展示出来。
          [ComputationalThinking](https://computationalthinking.mit.edu/Spring21/) 是 MIT 开设的一门计算思维入门课，所有课程内容全部开源，可以在课程网站直接访问。这门课利用 Julia 编程语言，在图像处理、社会科学与数据科学、气候学建模三个 topic 下带领学生理解算法、数学建模、数据分析、交互设计、图例展示，让学生体验计算与科学的美妙结合。内容虽然不难，但给我最深刻的感受就是，科学的魅力并不是故弄玄虚的艰深理论，不是诘屈聱牙的术语行话，而是用直观生动的案例，用简练深刻的语言，让每个普通人都能理解。
          上完上面的体验课之后，如果意犹未尽的话，不妨试试 MIT 的 [18.330 : Introduction to numerical analysis](https://csdiy.wiki/%E6%95%B0%E5%AD%A6%E8%BF%9B%E9%98%B6/numerical/)，这门课的编程作业同样会用 Julia 编程语言，不过难度和深度上都上了一个台阶。内容涉及了浮点编码、Root finding、线性系统、微分方程等等方面，整门课的主旨就是让你利用离散化的计算机表示去估计和逼近一个数学上连续的概念。这门课的教授还专门撰写了一本配套的开源教材 [Fundamentals of Numerical Computation](https://fncbook.github.io/fnc/frontmatter.html)，里面附有丰富的 Julia 代码实例和严谨的公式推导。
          如果你还意犹未尽的话，还有 MIT 的数值分析研究生课程 [18.335: Introduction to numerical method](https://ocw.mit.edu/courses/mathematics/18-335j-introduction-to-numerical-methods-spring-2019/index.htm) 供你参考。
        - #### 微分方程
          如果世间万物的运动发展都能用方程来刻画和描述，这是一件多么酷的事情呀！虽然几乎任何一所学校的 CS 培养方案中都没有微分方程相关的必修课程，但我还是觉得掌握它会赋予你一个新的视角来审视这个世界。
          由于微分方程中往往会用到很多复变函数的知识，所以大家可以参考 [MIT18.04: Complex variables functions](https://ocw.mit.edu/courses/mathematics/18-04-complex-variables-with-applications-spring-2018/) 的课程 notes 来补齐先修知识。
          [MIT18.03: differential equations](https://ocw.mit.edu/courses/mathematics/18-03sc-differential-equations-fall-2011/unit-i-first-order-differential-equations/) 主要覆盖了常微分方程的求解，在此基础之上 [MIT18.152: Partial differential equations](https://ocw.mit.edu/courses/mathematics/18-152-introduction-to-partial-differential-equations-fall-2011/index.htm) 则会深入偏微分方程的建模与求解。掌握了微分方程这一有力工具，相信对于你的实际问题的建模能力以及从众多噪声变量中把握本质的直觉都会有很大帮助。
      - ### 数学高阶
        collapsed:: true
        - 作为计算机系的学生，我经常听到数学无用论的论断，对此我不敢苟同但也无权反对，但若凡事都硬要争出个有用和无用的区别来，倒也着实无趣，因此下面这些面向高年级甚至研究生的数学课程，大家按兴趣自取所需。
        - #### 凸优化
          [Standford EE364A: Convex Optimization](https://csdiy.wiki/%E6%95%B0%E5%AD%A6%E8%BF%9B%E9%98%B6/convex/)
        - #### 信息论
          [MIT6.441: Information Theory](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-441-information-theory-spring-2016/syllabus/)
        - #### 应用统计学
          [MIT18.650: Statistics for Applications](https://ocw.mit.edu/courses/mathematics/18-443-statistics-for-applications-spring-2015/index.htm)
        - #### 初等数论
          [MIT18.781: Theory of Numbers](https://ocw.mit.edu/courses/mathematics/18-781-theory-of-numbers-spring-2012/index.htm)
        - #### 密码学
          [Standford CS255: Cryptography](http://crypto.stanford.edu/~dabo/cs255/)
      - ### 编程入门
        collapsed:: true
        - > Languages are tools, you choose the right tool to do the right thing. Since there's no universally perfect tool, there's no universally perfect language.
        - #### Shell
        - [MIT-Missing-Semester](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/MIT-Missing-Semester/)
        - #### Python
        - [CS50P: CS50's Introduction to Programming with Python](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/CS50P/)
        - [Harvard CS50: This is CS50x](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/CS50/)
        - [UCB CS61A: Structure and Interpretation of Computer Programs](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/CS61A/)
        - #### C++
        - [Stanford CS106B/X: Programming Abstractions](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/CS106B_CS106X/)
        - [Stanford CS106L: Standard C++ Programming](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/CS106L/)
        - #### Rust
        - [Stanford CS110L: Safety in Systems Programming](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/CS110L/)
        - #### OCaml
        - [Cornell CS3110 textbook: Functional Programming in OCaml](https://cs3110.github.io/textbook/cover.html)
      - ### 电子基础
        collapsed:: true
        - #### 电路基础
          作为计算机系的学生，了解一些基础的电路知识，感受从传感器收集数据到数据分析再到算法预测整条流水线，对于后续知识的学习以及计算思维的培养还是很有帮助的。[EE16A&B: Designing Information Devices and Systems I&II](https://csdiy.wiki/%E7%94%B5%E5%AD%90%E5%9F%BA%E7%A1%80/EE16/) 是伯克利 EE 学生的大一入门课，其中 EE16A 注重通过电路从实际环境中收集和分析数据，而 EE16B 则侧重从这些收集到的数据进行分析并做出预测行为。
        - #### 信号与系统
          信号与系统是一门我觉得非常值得一上的课，最初学它只是为了满足我对傅里叶变换的好奇，但学完之后我才不禁感叹，傅立叶变换给我提供了一个全新的视角去看待这个世界，就如同微分方程一样，让你沉浸在用数学去精确描绘和刻画这个世界的优雅与神奇之中。
          [MIT 6.003: signal and systems](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-003-signals-and-systems-fall-2011/lecture-videos/lecture-1-signals-and-systems/) 提供了全部的课程录影、书面作业以及答案。也可以去看这门课的[远古版本](https://csdiy.wiki/%E7%94%B5%E5%AD%90%E5%9F%BA%E7%A1%80/Signals_and_Systems_AVO/)
          而 [UCB EE120: Signal and Systems](https://csdiy.wiki/%E7%94%B5%E5%AD%90%E5%9F%BA%E7%A1%80/signal/) 关于傅立叶变换的 notes 写得非常好，并且提供了6 个非常有趣的 Python 编程作业，让你实践中运用信号与系统的理论与算法。
      - ### 数据结构与算法
        collapsed:: true
        - 算法是计算机科学的核心，也是几乎一切专业课程的基础。如何将实际问题通过数学抽象转化为算法问题，并选用合适的数据结构在时间和内存大小的限制下将其解决是算法课的永恒主题。如果你受够了老师的照本宣科，那么我强烈推荐伯克利的 [UCB CS61B: Data Structures and Algorithms](https://csdiy.wiki/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E4%B8%8E%E7%AE%97%E6%B3%95/CS61B/) 和普林斯顿的 [Coursera: Algorithms I & II](https://csdiy.wiki/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E4%B8%8E%E7%AE%97%E6%B3%95/Algo/)，这两门课的都讲得深入浅出并且会有丰富且有趣的编程实验将理论与知识结合起来。
          以上两门课程都是基于 Java 语言，如果你想学习 C/C++ 描述的版本，可以参考斯坦福的数据结构与基础算法课程 [Stanford CS106B/X: Programming Abstractions](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/CS106B_CS106X/)。偏好 Python 的同学可以学习 MIT 的算法入门课 [MIT 6.006: Introduction to Algorithms](https://csdiy.wiki/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E4%B8%8E%E7%AE%97%E6%B3%95/6.006/)
          对一些更高级的算法以及 NP 问题感兴趣的同学可以学习伯克利的算法设计与分析课程 [UCB CS170: Efficient Algorithms and Intractable Problems](https://csdiy.wiki/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E4%B8%8E%E7%AE%97%E6%B3%95/CS170/) 或者 MIT 的高阶算法 [MIT 6.046: Design and Analysis of Algorithms](https://csdiy.wiki/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E4%B8%8E%E7%AE%97%E6%B3%95/6.046/)。
      - ### 软件工程
        collapsed:: true
        - #### 入门课
          一份“能跑”的代码，和一份高质量的工业级代码是有本质区别的。因此我非常推荐低年级的同学学习一下 [MIT 6.031: Software Construction](https://csdiy.wiki/%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B/6031/) 这门课，它会以 Java 语言为基础，以丰富细致的阅读材料和精心设计的编程练习传授如何编写**不易出 bug、简明易懂、易于维护修改**的高质量代码。大到宏观数据结构设计，小到如何写注释，遵循这些前人总结的细节和经验，对于你此后的编程生涯大有裨益。
        - #### 专业课
          当然，如果你想系统性地上一门软件工程的课程，那我推荐的是伯克利的 [UCB CS169: software engineering](https://csdiy.wiki/%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B/CS169/)。但需要提醒的是，和大多学校（包括贵校）的软件工程课程不同，这门课不会涉及传统的 **design and document** 模式，即强调各种类图、流程图及文档设计，而是采用近些年流行起来的小团队快速迭代 **Agile Develepment** 开发模式以及利用云平台的 **Software as a service** 服务模式。
      - ### 体系结构
        collapsed:: true
        - #### 入门课
          从小我就一直听说，计算机的世界是由 01 构成的，我不理解但大受震撼。如果你的内心也怀有这份好奇，不妨花一到两个月的时间学习 [Coursera: Nand2Tetris](https://csdiy.wiki/%E4%BD%93%E7%B3%BB%E7%BB%93%E6%9E%84/N2T/) 这门无门槛的计算机课程。这门麻雀虽小五脏俱全的课程会从 01 开始让你亲手造出一台计算机，并在上面运行俄罗斯方块小游戏。一门课里涵盖了编译、虚拟机、汇编、体系结构、数字电路、逻辑门等等从上至下、从软至硬的各类知识，非常全面。难度上也是通过精心的设计，略去了众多现代计算机复杂的细节，提取出了最核心本质的东西，力图让每个人都能理解。在低年级，如果就能从宏观上建立对整个计算机体系的鸟瞰图，是大有裨益的。
        - #### 专业课
          当然，如果想深入现代计算机体系结构的复杂细节，还得上一门大学本科难度的课程 [UCB CS61C: Great Ideas in Computer Architecture](https://csdiy.wiki/%E4%BD%93%E7%B3%BB%E7%BB%93%E6%9E%84/CS61C/)。UC Berkeley 作为 RISC-V 架构的发源地，在体系结构领域算得上首屈一指。其课程非常注重实践，你会在 Project 中手写汇编构造神经网络，从零开始搭建一个 CPU，这些实践都会让你对计算机体系结构有更为深入的理解，而不是仅停留于“取指译码执行访存写回”的单调背诵里。
      - ### 系统入门
        collapsed:: true
        - 计算机系统是一个庞杂而深刻的主题，在深入学习某个细分领域之前，对各个领域有一个宏观概念性的理解，对一些通用性的设计原则有所知晓，会让你在之后的深入学习中不断强化一些最为核心乃至哲学的概念，而不会桎梏于复杂的内部细节和各种 trick。因为在我看来，学习系统最关键的还是想让你领悟到这些最核心的东西，从而能够设计和实现出属于自己的系统。
          [MIT6.033: System Engineering](http://web.mit.edu/6.033/www/) 是 MIT 的系统入门课，主题涉及了操作系统、网络、分布式和系统安全，除了知识点的传授外，这门课还会讲授一些写作和表达上的技巧，让你学会如何设计并向别人介绍和分析自己的系统。这本书配套的教材 *Principles of Computer System Design: An Introduction* 也写得非常好，推荐大家阅读。
          [CMU 15-213: Introduction to Computer System](https://csdiy.wiki/%E4%BD%93%E7%B3%BB%E7%BB%93%E6%9E%84/CSAPP/) 是 CMU 的系统入门课，内容覆盖了体系结构、操作系统、链接、并行、网络等等，兼具广度和深度，配套的教材 *Computer Systems: A Programmer's Perspective* 也是质量极高，强烈建议阅读。
      - ### 操作系统
        collapsed:: true
        - > 没有什么能比自己写个内核更能加深对操作系统的理解了。
          操作系统作为各类纷繁复杂的底层硬件虚拟化出一套规范优雅的抽象，给所有应用软件提供丰富的功能支持。了解操作系统的设计原则和内部原理对于一个不满足于当调包侠的程序员来说是大有裨益的。出于对操作系统的热爱，我上过国内外很多操作系统课程，它们各有侧重和优劣，大家可以根据兴趣各取所需。
          [MIT 6.S081: Operating System Engineering](https://csdiy.wiki/%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/MIT6.S081/)，MIT 著名 PDOS 实验室出品，11 个 Project 让你在一个实现非常优雅的类Unix操作系统xv6上增加各类功能模块。这门课也让我深刻认识到，做系统不是靠 PPT 念出来的，是得几万行代码一点点累起来的。
          [UCB CS162: Operating System](https://csdiy.wiki/%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/CS162/)，伯克利的操作系统课，采用和 Stanford 同样的 Project —— 一个教学用操作系统 Pintos。我作为北京大学2022年春季学期操作系统实验班的助教，引入并改善了这个 Project，课程资源也会全部开源，具体参见[课程网站](https://https//pku-os.github.io/sp22/)。
          [NJU: Operating System Design and Implementation](https://csdiy.wiki/%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/NJUOS/)，南京大学的蒋炎岩老师开设的操作系统课程。蒋老师以其独到的系统视角结合丰富的代码示例将众多操作系统的概念讲得深入浅出，此外这门课的全部课程内容都是中文的，非常方便大家学习。
      - ### 并行与分布式系统
        collapsed:: true
        - 想必这两年各类 CS 讲座里最常听到的话就是“摩尔定律正在走向终结”，此话不假，当单核能力达到上限时，多核乃至众核架构如日中天。硬件的变化带来的是上层编程逻辑的适应与改变，要想充分利用硬件性能，编写并行程序几乎成了程序员的必备技能。与此同时，深度学习的兴起对计算机算力与存储的要求都达到了前所未有的高度，大规模集群的部署和优化也成为热门技术话题。
        - #### 并行计算
          [CMU 15-418/Stanford CS149: Parallel Computing](https://csdiy.wiki/%E5%B9%B6%E8%A1%8C%E4%B8%8E%E5%88%86%E5%B8%83%E5%BC%8F%E7%B3%BB%E7%BB%9F/CS149/)
        - #### 分布式系统
          [MIT 6.824: Distributed System](https://csdiy.wiki/%E5%B9%B6%E8%A1%8C%E4%B8%8E%E5%88%86%E5%B8%83%E5%BC%8F%E7%B3%BB%E7%BB%9F/MIT6.824/)
      - ### 系统安全
        collapsed:: true
        - 不知道你当年选择计算机是不是因为怀着一个中二的黑客梦想，但现实却是成为黑客道阻且长。
        - #### 理论课程
          [UCB CS161: Computer Security](https://csdiy.wiki/%E7%B3%BB%E7%BB%9F%E5%AE%89%E5%85%A8/CS161/) 是伯克利的系统安全课程，会涵盖栈攻击、密码学、网站安全、网络安全等等内容。
          [ASU CSE365: Introduction to Cybersecurity](https://csdiy.wiki/%E7%B3%BB%E7%BB%9F%E5%AE%89%E5%85%A8/CSE365/) 亚利桑那州立大学的 Web 安全课程，主要涉及注入、汇编与密码学的内容。
          [ASU CSE466: Computer Systems Security](https://csdiy.wiki/%E7%B3%BB%E7%BB%9F%E5%AE%89%E5%85%A8/CSE466/) 亚利桑那州立大学的系统安全课程，涉及内容全面。门槛较高，需要对 Linux, C 与 Python 充分熟悉。
        - #### 实践课程
          掌握这些理论知识之后，还需要在实践中培养和锻炼这些“黑客素养”。[CTF 夺旗赛](https://ctf-wiki.org/)是一项比较热门的系统安全比赛，赛题中会融会贯通地考察你对计算机各个领域知识的理解和运用。北大今年也成功举办了[第 0 届和第 1 届](https://geekgame.pku.edu.cn/)，鼓励大家后期踊跃参与，在实践中提高自己。下面列举一些我平时学习（摸鱼）用到的资源：
        - [CTF-wiki](https://ctf-wiki.org/)
        - [CTF-101](https://ctf101.org/)
        - [Hacker-101](https://ctf.hacker101.com/)
      - ### 计算机网络
        collapsed:: true
        - > 没有什么能比自己写个 TCP/IP 协议栈更能加深对计算机网络的理解了。
          大名鼎鼎的 [Stanford CS144: Computer Network](https://csdiy.wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/CS144/)，8 个 Project 带你实现整个 TCP/IP 协议栈。
          如果你只是想在理论上对计算机网络有所了解，那么推荐计网著名教材《自顶向下方法》的配套学习资源 [Computer Networking: A Top-Down Approach](https://csdiy.wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/topdown/)。
      - ### 数据库系统
        collapsed:: true
        - > 没有什么能比自己写个关系型数据库更能加深对数据库系统的理解了。
          CMU 的著名数据库神课 [CMU 15-445: Introduction to Database System](https://csdiy.wiki/%E6%95%B0%E6%8D%AE%E5%BA%93%E7%B3%BB%E7%BB%9F/15445/) 会通过 4 个 Project 带你为一个用于教学的关系型数据库 [bustub](https://github.com/cmu-db/bustub) 添加各种功能。实验的评测框架也免费开源了，非常适合大家自学。此外课程实验会用到 C++11 的众多新特性，也是一个锻炼 C++ 代码能力的好机会。
          Berkeley 作为著名开源数据库 postgres 的发源地也不遑多让，[UCB CS186: Introduction to Database System](https://csdiy.wiki/%E6%95%B0%E6%8D%AE%E5%BA%93%E7%B3%BB%E7%BB%9F/CS186/) 会让你用 Java 语言实现一个支持 SQL 并发查询、B+ 树索引和故障恢复的关系型数据库。
      - ### 编译原理
        collapsed:: true
        - > 没有什么能比自己写个编译器更能加深对编译器的理解了。
          [Stanford CS143: Compilers](https://csdiy.wiki/%E7%BC%96%E8%AF%91%E5%8E%9F%E7%90%86/CS143/) 带你手写编译器。
      - ### Web开发
        collapsed:: true
        - 前后端开发很少在计算机的培养方案里被重视，但其实掌握这项技能还是好处多多的，例如搭建自己的个人主页，抑或是给自己的课程项目做一个精彩的展示网页。
        - #### 两周速成版
          [MIT web development course](https://csdiy.wiki/Web%E5%BC%80%E5%8F%91/mitweb/)
        - #### 系统学习版
          [Stanford CS142: Web Applications](https://csdiy.wiki/Web%E5%BC%80%E5%8F%91/CS142/)
      - ### 计算机图形学
        collapsed:: true
        - [Stanford CS148](https://csdiy.wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E5%9B%BE%E5%BD%A2%E5%AD%A6/CS148/)
        - [Games101](https://csdiy.wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E5%9B%BE%E5%BD%A2%E5%AD%A6/GAMES101/)
        - [Games103](https://csdiy.wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E5%9B%BE%E5%BD%A2%E5%AD%A6/GAMES103/)
        - [Games202](https://csdiy.wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E5%9B%BE%E5%BD%A2%E5%AD%A6/GAMES202/)
      - ### 数据科学
        collapsed:: true
        - 其实数据科学和机器学习与深度学习有着很紧密的联系，但可能更侧重于实践。Berkeley 的 [UCB Data100: Principles and Techniques of Data Science](https://csdiy.wiki/%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6/Data100/) 通过丰富的编程练习让你在实践中掌握各类数据分析工具和算法，并带领你体验从海量的数据集中提取出想要的结果，并对未来的数据或用户的行为做出相应的预测。但这只是一门基础课，如果想学习工业级别的数据挖掘与分析技术，可以尝试 Stanford 的大数据挖掘课程 [CS246: Mining Massive Data Sets](https://web.stanford.edu/class/cs246/)。
      - ### 人工智能
        collapsed:: true
        - 近十年人工智能应该算是计算机界最火爆的领域。如果你不满足于整日听各路媒体争相报道人工智能相关的进展，而想真正一探究竟，那么非常推荐学习 Harvard 神课 CS50 系列的人工智能课程 [Harvard CS50: Introduction to AI with Python](https://csdiy.wiki/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD/CS50/)。课程短小精悍，覆盖了传统人工智能领域的几大分支，并配有丰富有趣的 Python 编程练习来巩固你对人工智能算法的理解。美中不足的是这门课因为面向在线自学者的缘故内容较为精简，并且不会涉及特别深入的数学理论，如果想要系统深入地学习还需要一门本科生难度的课程，例如 Berkeley 的 [UCB CS188: Introduction to Artificial Intelligence](https://csdiy.wiki/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD/CS188/)。这门课的 Project 复刻了经典游戏糖豆人，让你运用人工智能算法玩游戏，非常有趣。
      - ### 机器学习
        collapsed:: true
        - 机器学习领域近些年最重要的进展就是发展出了基于神经网络的深度学习分支，但其实很多基于统计学习的算法依然在数据分析领域有着广泛的应用。如果你之前从未接触过机器学习的相关知识，而且不想一开始就陷入艰深晦涩的数学证明，那么不妨先从 Andrew Ng （吴恩达）的 [Coursera: Machine Learning](https://csdiy.wiki/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/ML/) 学起。这门课在机器学习领域基本无人不晓，吴恩达以其深厚的理论功底和出色的表达能力把很多艰深的算法讲得深入浅出，并且非常实用。其配套的作业也是质量相当上乘，可以帮助你快速入门。
          但上过这门课只能让你从宏观上对机器学习这一领域有一定了解，如果想真正理解那些“神奇”算法背后的数学原理甚至从事相关领域的科研工作，那么还需要一门更“数学”的课程，例如 [Stanford CS229: Machine Learning](https://csdiy.wiki/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/CS229/) 或者 [UCB CS189: Introduction to Machine Learning](https://csdiy.wiki/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/CS189/)。
      - ### 深度学习
        collapsed:: true
        - 前几年 AlphaGo 的大热让深度学习进入了大众的视野，不少大学甚至专门成立了相关专业。很多计算机的其他领域也会借助深度学习的技术来做研究，因此基本不管你干啥多少都会接触到一些神经网络、深度学习相关的技术需求。如果想快速入门，同样推荐 Andrew Ng （吴恩达）的 [Coursera: Deep Learning](https://csdiy.wiki/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/CS230/)，质量无需多言，Coursera 上罕见的满分课程。此外如果你觉得英文课程学习起来有难度，推荐李宏毅老师的 [国立台湾大学：机器学习](https://csdiy.wiki/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/LHY/) 课程。这门课打着机器学习的名号，却囊括了深度学习领域的几乎所有方向，非常全面，很适合你从宏观上对这个领域有一个大致的了解。而且老师本人也非常幽默，课堂金句频出。
          当然因为深度学习领域发展非常迅速，已经拥有了众多研究分支，如果想要进一步深入，可以按需学习下面罗列的代表课程，
        - #### 计算机视觉
        - [Stanford CS231n: CNN for Visual Recognition](https://csdiy.wiki/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/CS231/)
        - #### 自然语言处理
          [Stanford CS224n: Natural Language Processing](https://csdiy.wiki/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/CS224n/)
        - #### 图神经网络
          [Stanford CS224w: Machine Learning with Graphs](https://csdiy.wiki/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/CS224w/)
        - #### 强化学习
          [UCB CS285: Deep Reinforcement Learning](https://csdiy.wiki/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/CS285/)
    - ## 定制属于你的课程地图
      collapsed:: true
      - >  授人以鱼不如授人以渔。
        以上的课程规划难免带有强烈的个人偏好，不一定适合所有人，更多是起到抛砖引玉的作用。如果你想挑选自己感兴趣的方向和内容加以学习，可以参考我在下面列出来的资源。
      - [MIT OpenCourseWare](https://ocw.mit.edu/): 麻省理工学院的课程资源开放共享项目，收录了数以千计的各科课程资源，其中计算机类的课号是 6.xxx。
      - [MIT CS Course List](http://student.mit.edu/catalog/m6a.html): 麻省理工学院的 CS 课程列表。
      - [UC Berkeley EECS Course Map](https://hkn.eecs.berkeley.edu/courseguides): UC Berkeley 的 EECS 培养方案，以课程地图的方式将各门课程的类别和先修关系一目了然地呈现，其中绝大多数课程本书中均有收录。
      - [UC Berkeley CS Course List](https://www2.eecs.berkeley.edu/Courses/CS/): UC Berkeley 的 CS 课程列表。
      - [Stanford CS Course List](https://blog.csdn.net/qq_41220023/article/details/81976967): 斯坦福的 CS 课程列表。
  - 必学工具
    collapsed:: true
    - [翻墙](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/%E7%BF%BB%E5%A2%99/) #proxy
      collapsed:: true
      - [如何更新软件和订阅](https://wallesspku.com/walless/2022/04/21/upgrade.html)
      - [使用建议](https://wallesspku.com/walless/2021/09/25/advice.html)
        collapsed:: true
        - 如果你已经可以翻墙, 那你可以继续阅读我们的一些建议. 我们分 [功能](#function) 和 [服务器选择](#select) 两部分介绍.
        - WallessPKU 除了提供最基础的代理服务以外, 还有一些特殊的功能. 你首先需要熟悉如何操作它.
        - 你可以在 Proxy 中看到很多选项卡 (在 Mac 中是托盘图标处的右键菜单, 部分功能没有在 iOS 中实现), 这都是我们预设的功能. 我们依次介绍它们:
        - 这是一个通知系统. 我们在这里张贴一些消息. 它每隔十分钟和主服务交换一次信息, 你可以在这里看到你当前的流量余额, 以及我们的通知.
        - 请务必留意!
        - ## GFW
        - 这里你可以选择你的翻墙服务器. 我们会提供若干服务器供你选择. 你可以通过测速来决定使用哪台服务器. 注意这里的服务器分为 IPv4 和 IPv6; IPv4 可以在大部分环境中使用, IPv6 可能只能在校园网内使用.
        - 我们有的节点可能会故障, 或者和你的网络环境连接受阻, 这种时候你需要手动选择一台可以使用的服务器.
        - 请注意, 不是所有的流量都会被代理. 我们维护一个被墙域名列表, 如果监测到域名被墙, 才会被这里的流量代理. Google Scholar 的流量会被 [Scholar](#scholar) 选项卡中的流量代理. 如果想让所有海外连接都被代理, 请参考 [Accel.](#accel) 选项卡.
        - 不同的服务器有不同的权重, 流量消耗 = 实际流量 \* 服务器权重.
        - ## Scholar
        - Google Scholar 的代理不会被 GFW 选项卡中的服务器完成, 而是由这里的服务器负责. 如果 Google Scholar 不能访问, 你需要在这里换一台能访问 Scholar 的服务器.
        - ## AD
        - 我们收集了很多常见的广告服务器, 你可以选择不加载它们. 注意这个列表可能会误杀一些网站, 如果你已经有别的防广告手段, 可以忽略这个选项.
        - 如果这里选择 REJECT, 则一些广告将会被屏蔽. 如果选择 DIRECT 则不屏蔽.
        - 默认选项是 DIRECT.
        - ## Accel. (海外加速)
        - 有时候, 有些地址虽然没有被墙, 但是使用代理访问要比直接访问快. 如果这里选择 GFW, 则任何海外地址都会被代理; 如果选择 DIRECT 则不默认代理.
        - 另外, 我们的规则列表可能不够全面, 有些网站虽然被墙, 但是不会被代理. 这种情况下你可以启动 Accel. 来代理全部海外网址.
        - 默认选项是 DIRECT.
        - ## 6to4 (IPv6 隧道)
        - 这里的服务器都是 IPv4/IPv6 双栈的, 所以可以用来搭建 IPv4 到 IPv6 的隧道. 默认是 DIRECT, 即不做任何代理. 选择任意一台服务器即可开启代理服务.
        - 注意: WallessPKU 的初衷是提供稳定的翻墙服务, 6to4 属于附加功能, 我们不会对 6to4 服务提供任何技术支持, 也不会优化 6to4 的服务器线路.
        - _快_ 自然是使用代理服务的第一要义, 但这有两层含义, 即延迟低和速度快. 请注意 **Clash 的延迟毫秒数低不代表速度快**. 这是一个很复杂的问题, 每台服务器的带宽都可能不一样, 在不同时段的丢包率不同, 而用户的挤兑又可能会让服务器超载. 所以我们并不能给出一个很好的答案. 笼统来说, 你需要尝试不同的服务器.
        - 对我们而言, 我们希望你在保证速度和延迟的同时选择权重 (即 w 值) 尽可能小的服务器, 这非常有利于我们平衡服务器的负载.
      - [常见问题解答](https://wallesspku.com/walless/2021/04/23/faq.html)
        collapsed:: true
        - **如果您是从搜索引擎上找到这篇博文的, 那请注意: 虽然别的服务提供商也可能使用 Clash 作为客户端, 但这篇文章仅适用于 WallessPKU.**
        - ## 快速导航
        - ## 无法注册
        - ## 显示未收到邮件
        - 大概率是邮箱的延迟或者丢件. pku 邮箱, 特别是 163 托管的 stu 邮箱, 到服务器有非常高的延迟. 请耐心等待半小时; 另外为了避免垃圾邮件骚扰, 请最好使用 PKU 官方平台 (即 mail.pku.edu.cn 或者 163) 来发送邮件, 不要使用第三方软件代发. 如果还不行, 可以联系我们.
        - ## 无法订阅
        - 大部分关于订阅的问题都源自于订阅地址输入错误. 请确保您已经在 [这里](https://wallesspku.space/register) 注册, 并已经获得了形如 `https://941321.xyz/clash/邮箱/密码` 的订阅地址 (注意不是 `https://941321.xyz/profile/邮箱/密码`). 如果还有问题, 请继续阅读.
        - ## Clash 订阅获取失败.
        - 有很多可能, 最有可能是网络环境问题. 我们负责分发配置文件的服务器位于国外, 而国内网络环境复杂, 所以有可能会下载失败. 我们建议你换个网络环境试试, 比如手机的热点网络.
        - ## 获取订阅时提示 “yaml: line 35: mapping values are not allowed in this context”
        - 你不小心把 profile 的地址填入了订阅. 请区分 profile 地址和订阅地址, 前者可以在浏览器打开, 用于查看个人信息, 后者是 clash 读的配置文件地址.
        - ## 无法使用翻墙节点
        - ## 所有节点超时
        - ### 软件 / 配置过期了
        - 如果你很久没有使用 Clash, 那大概率是你的软件太旧, 或者是很久没有更新订阅配置了. 更新软件和配置的时候请记得关闭 Clash 的系统代理, 因为 Clash 已经不能用了. 请参考 [这篇文章](/walless/2022/04/21/upgrade.html).
        - ## 使用了 Global (全局) 模式
        - 如果您对 Clash 没有非常熟悉, 建议使用 Rule (规则) 模式.
        - ## 可以正常使用 IPv4 节点，但是无法连接 IPv6 节点
        - ### 请确认你有 IPv6 网络
        - 大部分校园网用户可以使用 IPv6 网络, 但家宽对 IPv6 的支持还没有普及. 请 [检测你的 IPv6 网络](https://ipv6-test.com).
        - ### (Windows) 需要手动开启 IPv6 支持
        - 部分版本的 Clash for Windows 修改了默认策略, 默认不使用IPV6\. 如果你在校园网内, 可以考虑手动开启对 IPv6 的支持. 在安装完 Clash 后, 如下图所示, 点击IPV6选项开启IPv6.![windows_ipv6](/assets/win_ipv6.png)
        - ## (Windows) 软件提示 “Could not connect to Clash core”.
        - 此时你的主界面会有 logs 文件夹的提示, 请你打开这个文件夹, 然后看看 log 文件.
        - ### logs 没有报错
        - 这种问题常常由 Pulse Secure 和 Clash 冲突造成. 我们建议普通用户不要尝试同时运行 Clash 和 Pulse Secure, 很可能会造成 Clash Core 运行崩溃. 一般而言重启即可解决问题. 如果不能, 请参考 “logs 为空” 章节.
        - ### logs 提示端口冲突
        - 那你可能有别的上网软件和你的 Clash 争夺端口. 你可以尝试关闭这些软件 (常见的有北大网盘, SSR 等), 然后启动 Clash. 如果想一劳永逸, 可以在 Clash 启动之后在主界面把冲突的端口修改掉.
        - ### logs 为空
        - 这种情况可能比较复杂. 可能是 Clash core 没有启动. 一般而言有两种解决方案.
        - 1. 在系统设置 “网络和 Internet” 选项卡中重置网络, 有时候可以解决问题.
        - 2. 重启一下系统试试?
        - ## Clash 启动了, 看到了服务器列表, 也看到连接速度, 但是不能翻墙.
        - ### 可能是和别的代理软件冲突了
        - 1. 软件冲突: 请检查你是否有别的代理软件在运行, 如果有, 关掉它. 常见的软件有各类翻墙代理软件, 以及 Pulse Secure;
        - 2. 浏览器插件冲突: 非常简单的测试方案是启动 Chrome/FireFox 的隐身模式, 看看在隐身模式下能不能翻墙. 如果可以, 那你需要自己看看浏览器有没有什么翻墙插件.
        - ### 你可能需要手动选择一台合适的服务器
        - 我们有很多服务器, 对于你的网络环境而言, 有些服务器可能速度不理想. 在 “GFW” 的选项中 (Windows 用户需要进入 proxies 选项卡), 请选择一台可用的服务器. 使用前你可以参考你到各个服务器的延迟.
        - ## 其他问题
        - ## (Windows) 我无法使用 UWP 应用:
        - 启用 System Proxy 后, UWP 应用 (包括 win10 中的应用商店) 将无法使用. 你需要选择侧边栏里的 General, 然后点击 EnableLoopback.exe, 在打开的应用列表里勾选 UWP 应用, 最后点击列表上面的 Save Changes 即可. 更多详情请查看 [Link](https://github.com/Fndroid/clash%5Ffor%5Fwindows%5Fpkg/wiki/UWP%E5%BA%94%E7%94%A8%E8%81%94%E7%BD%91).
        - ## 我想同时使用 Pulse Secure 和 Clash.
        - 我们 **并不建议这样做**. 如果你一定要同时翻墙和使用校内网络, 你可以先开启 Pulse Secure 再开启 Clash.
        - ## 我能翻墙, 能上 Google/Wikipedia/Facebook, 但是不能访问某个网站.
        - 我们有一个规则列表, 记录了一些已知的被墙的地址. 但墙是动态的, 每天总有网站莫名其妙被墙. 如果你发现某个你想上的网站被墙, 而且
        - 1. 这个网站你只是偶尔访问: 那你可以启动 Clash 的 Accel. 预设功能 (详情请见我们的 Clash 教程页面), 这个模式下所有海外网站都会被代理. 在一些极端情况下请尝试在 6to4 中选择一台能用的服务器.
        - 2. 这个网站你需要频繁访问: 那你可以用邮件 (见页底) 联系我们, 我们可以手动把这个地址加入我们的列表.
        - ## 我别的网站都能访问, 但是访问 Google Scholar 的时候会提示错误 403.
        - 有时候 Google Scholar 会屏蔽一些服务器 IP. 你可以在 Clash 的 Scholar 选项卡供更换 Google Scholar 的代理服务器, 一般换一台服务器就好了. 如果切换多台仍不能解决问题, 请联系我们.
        - ## 联系方式.
        - 抱歉这个 FAQ 手册还不全面. 请使用邮件直接联系我们.**请确保您是 WallessPKU 的用户. 我们不对别的商业机场提供任何技术支持**.
        - 请告诉我们你的
        - * 注册邮箱地址;
        - * 你在配置哪一步失败;
        - * 请提供你的 Clash 界面截图;
        - * (Windows) 请提供 Clash 的 logs 供我们参考. Clash 的 logs 位于 `C:\Users\%username%\.config\clash\logs`.
        - 我们的邮箱是: `wallesspku@googlegroups.com`, 来信请注明您已阅读 FAQ.
        - WallessPKU 纯属公益项目, 恕不解答除基本翻墙功能以外的问题. 如果有特殊需求, 例如 IPv6 隧道, 和别的软件的适配 (包括各类浏览器插件和 pulse secure 等代理软件), 请咨询上游软件开发商或者相关专业人员.
      - [感谢 Olink 捐赠一台独立服务器!](https://wallesspku.com/walless/2021/01/15/olink.html)
      - [如何使用 WallessPKU](https://wallesspku.com/walless/2020/05/28/manual.html)
      - [以墙制墙: 用白名单防火墙对抗 GFW 主动探测](https://wallesspku.com/misc/2020/04/13/eye4eye.html)
        collapsed:: true
        - GFW 会通过主动探测来识别运行 Shadowsocks 的服务器. 我们通过实验再次验证了这一结论, 同时我们提供了一种简单且有效的对抗策略: 在服务器端设置白名单防火墙. 实验证明我们的策略有效延长了服务器的生存时间, 而且并不会影响用户的使用体验.
        - ## 介绍
        - GFW 的工作原理非常复杂, 但总体而言可以划分为两个步骤, 被动的嗅探和主动的探测. 前者是墙抓取数据包分析流量特征, 从而识别翻墙流量. 后者是主动向翻墙服务器发出探测数据包, 以主动探测来抓取特征并识别翻墙服务器. 目前流行的翻墙软件 (如 Shadowsocks, V2RAy 等) 以防御被动检测为主, 并不能很好地防御主动探测. 一些翻墙软件 (如 ShadowsocksR) 设计了对抗重放攻击的模块 (如使用 nonce), 但实践中运行 ShadowsocksR 的服务器同样会被封禁.
        - 我们猜测 GFW 的工作策略是: 以被动探测筛选服务器, 再以主动探测的结果作为封禁的依据. 这样, 只要我们能够对抗墙的主动探测, 就能够让服务器生存下来. 我们没有针对墙主动探测方式设计防御策略, 而是以源 IP 地址作为依据, Drop 所有的入站数据包, 只保留用户的数据包, 即白名单防火墙策略. 对比不使用这样策略的服务器, 白名单策略使得服务器成功躲过了 GFW 的封禁. 这种策略易于部署, 适用于任何服务器和翻墙协议 (实验中我们尝试了 SS, SSR 和 MTProto), 而且通过巧妙的设计可以不增加用户的负担.
        - ## 白名单策略
        - 白名单策略是指, 我们通过数据过滤防火墙, 只允许服务器接收特定 IP 来源的入站流量, 而拒绝所有别的流量. 具体而言, 我们 Setup 了两种服务器, 主服务器和子节点: 主服务器负责联络所有的子节点, 子节点负责给用户提供翻墙服务. 用户在翻墙前通过主节点记录自己的 IP, 主节点会把 IP 广播给所有的子节点, 从而把这个特定 IP 加入到白名单中. 这样我们就可以成功避开防火墙的探测.
        - 但是这样操作会给用户带来不必要的负担. 用户的网络环境可能很复杂; 宽带的每次重新拨号, 从 WiFi 环境过度到蜂窝网, 或者在蜂窝网的不同基站之间穿梭都可能会导致 IP 的变化, 从而无法被服务器识别. 为了减轻用户的负担, 我们把 IP 注册功能和 SSR 的订阅更新功能绑定. 用户每次向 SSR 服务器请求订阅列表的时候, 我们会抽取用户的 IP, 然后广播到所有子节点上. 这样的策略大大减轻了用户的操作负担.
        - 简单地丢弃所有入站数据包未免过于粗糙. 事实上我们可以有更灵活的防火墙策略. 经过研究我们发现, 被 GFW 用作主动探测的服务器全部都是 Linux 服务器, 而很多用户使用的操作系统是 Windows. Windows 发出的数据包区别于 Linux 的一大特征是, Windows 数据包的起始 TTL 是 128, 而 Linux 则是 64\. 所以一个简单的思路就是, 我们可以无条件信任 TTL 大于 64 的数据包 (考虑到用户到服务器之间的距离不太可能超过 64 跳). 这样 Windows 用户就可以不被防火墙影响.
        - 实践中我们还发现开放 22 端口和接受 ICMP 包并不会导致服务器被墙. 为了避免开启防火墙导致失联, 我们可以考虑开放 ICMP 协议和 22 端口.
        - ## 实验结果
        - ## 服务器的生存挑战
        - 我们在我们运营的 SSR 机场的服务器上全部部署了防火墙, 并使用上述策略更新防火墙的白名单. 我们进行了为期 18 天的实验. 在实验中, 所有服务器都没有被墙 (除了一次意外撤除防火墙的事件). 这些服务器工作在 163 线路, CN2 GT 线路和 CN2 GIA 线路. 但是为了保护我们自己的安全, 我们不能公布实验的具体规模.
        - 为了对比, 我们尝试性撤除 4 台服务器的防火墙, 在这几次实验中, 这些服务器在数分钟到一小时之内都被迅速封禁. 这进一步证明了白名单防火墙确实是保护服务器的主要因素.
        - 除了 SSR, 我们还测试了 MTProto 协议. MTProto 是一个早就证明被特征识别的协议. 实验证明, 这样的策略同样可以保护 MTProto. 实验中我们部署了 4 台服务器, 设有保护的两台服务器一直生存至今, 而没有部署防火墙的两台服务器分别在第 20 分钟和第一小时被封禁. 这个实验再次印证了主动探测是墙封禁服务器的必要条件, 即使这个协议早已被特征识别.
        - ## 探测数据包的分析
        - 关于探测数据包的分析, [这篇文章](https://gfw.report/blog/gfw%5Fshadowsocks/zh.html) 已经有较为透彻的分析. 这里我们再次印证了它的一部分结论, 并有小部分新的发现. 我们主要有以下发现:
        - 1. GFW 探测服务器的源地址处于电信和联通网络, 以联通骨干网为主.
        - 2. 探测数据包的 TTL 全部小于 64.
        - 3. 只要有 Shadowsocks 流量记录, 墙会把各种可能的翻墙协议全部探测一次, 包括古老的已经不再适用的协议.
        - 4. 没有流量记录的端口, 即使在运行 Shadowsocks, 墙也不会探测, 即它不会穷举各种端口.
        - 5. 墙会用很多地址探测服务器, 但每个地址只会探测一个端口.
        - 6. 墙对 Shadowsocks 端口的探测频率大约是 10 分钟一次, 探测的概率和这个端口的流量大致呈正比关系, 但是也有一些端口从来没有被探测过 – 我们并不知道为什么.
        - 7. 每一次探测会持续数分钟, 之后墙不会发起同样的探测.
        - ## 具体配置方案
        - 我们使用的工具是 iptables. 我们假设用户的 IP 是 1.2.3.4, 具体的配置方案是
        - ```
           iptables -A INPUT -m ttl --ttl-gt 80 -j ACCEPT
           iptables -A INPUT -p icmp -j ACCEPT
           iptables -A INPUT -p tcp --dport 22 -j ACCEPT
           iptables -A INPUT -i lo -j ACCEPT
           iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
           iptables -A INPUT -s 1.2.3.4 -j ACCEPT
           iptables -P INPUT DROP
          ```
      - [为肺炎期间还加班工作的网络安全部门点赞!](https://wallesspku.com/misc/2020/02/02/covid.html)
        collapsed:: true
        - 肺炎肆虐中国, 全国上下百业凋零而人心惶惶. 在此国难之际, 中华民族理应众志成城, 抗击新冠. 然而这其中总是夹杂着一些不友好的声音. 在肺炎期间, 有很多居心叵测的网友在 YouTube, Twitter 等境外网站发布不当言论, 妄议中央, 诋毁攻击地方政府政策, 中医和红十字会, 大大损害了我国的国际形象. 在海外浏览诸如陈秋实, NY Times 这样未经权威认证的不实报道, 着实令人反感和愤怒.
        - 然而得益于我们优秀的政治制度, 我国有世界上最敬业的网络管理员和最优秀的防火墙, 这些意图抹黑中国的声音并没有传到长城之内. 我注意到在肺炎期间, 除了疫情防控的相关人员之外, 所有岗位延迟假期到 2 月 9 日, 这充分说明了网络安全长城也是抗击肺炎的重要一环. 我不禁为政策制定者和网络安全部门点赞! 正如非典期间我们用西药激素来维系生命, 用中药来对抗病毒, 在武汉肺炎中, 我们的白衣天使负责阻击新冠病毒, 而我们的网络管理员负责铲除人民毒瘤.
        - 最困难的时候, 也是最需要理解和牺牲的时候. 为了更多地了解网安部门的工作, 我特意购置了一些境外服务器模拟不法分子翻墙的行为, 这些服务器无一例外都被明察秋毫的管理员们轻松识破. 看到服务器一台一台地挂掉, 虽然我损失了一大笔钱, 但我的内心是多么的愉悦而满足! 相比于一个稳定而健康的舆论环境, 我个人的牺牲是不足为道的. 我完全不能理解身边的人因为不能翻墙气急败坏甚至恼羞成怒, 他们内心是多么的自私!
        - 虽然年味尚浓, 肺炎正盛, 但这丝毫不会影响到管理员的工作进度. 朝鲜战争的时候, 通讯员们躲在山洞里, 被敌人围困, 物资匮乏, 一个苹果都要一人一口地一起吃掉; 被敌人炸倒在地, 醒来后抖抖碎石便继续前进. 而现在, 我仿佛看到技术员们被新冠困在办公室, 防护用品稀缺, 一个口罩只能一人一口地轮流呼吸, 被肺炎击倒喝一杯双黄连就继续工作. 在这特殊的时刻, 我最急于告诉你们的, 是我思想感情的一段重要经历, 这就是: 我越来越深刻地感觉到谁是我们最可爱的人!
      - [翻墙者和管理者之间的有趣默契和微妙平衡](https://wallesspku.com/misc/2019/11/03/privity.html)
        collapsed:: true
        - 我认为, GFW 作为世界上最大, 最先进和最成功的封锁技术, 其所带来的社会影响已经远远超出了它的技术影响.
        - 为什么我不关心技术层面? 因为==我觉得个人的力量太渺小了. 我认为相对于 GFW 的实力而言, 各种加密混淆的代理协议都不值得一提. 不论是原始的 PPTP, L2TP, 还是加密和混淆协议 Shadowsocks(R), V2Ray, 在 GFW 面前都如同把 “我在翻墙” 写到 IP Header 里一样小儿科; 即使是 TLS 伪装的, 已经毫无破绽的协议, 同样可以被政府无差别干扰. 我们很难从技术层面战胜 GFW==.
        - 既然 GFW 如此强大, 为什么我们还能翻墙? 我认为, 这是管理者 (姑且如此称呼) 和翻墙者之间长期形成的默契. 翻墙者知道翻墙不被政府所允许, 但翻墙又是一件不得不做的事情, 特别是对于科研工作人员和特定行业从业人员而言. 政府不希望民众和墙外世界有太多的信息交流, 但同时也懂得大禹治水的道理. 于是两方逐渐形成了一种有趣的默契 – 政府 “允许” 翻墙者翻墙, 但翻墙者需要为 “违法行为” 付出更多的成本. ==管理者希望用这样粗粒度的方式来维持一种平衡, 即让有特殊需求的人翻墙, 大部分普通人不能或者很难翻墙==.
        - 这种平衡并不是一蹴而就的, 而是长期形成和不断调整的. ==在我有限的记忆中, 12 年之前, GFW 只会被动防御, 拦截 “不法网站”, 或者迫使海外互联网公司退出中国 (Facebook, Google, etc.) 和 “从良” (Microsoft, etc.); 正如胡编所说, 只要你想, 总能成功翻墙. 在 12 到 18 年之间, GFW 开始主动拦截 PPTP, L2TP 这些协议的流量, 封禁运行 Shadowsocks, V2Ray 这类软件的 VPS, 翻墙门槛开始提高. 我觉得 18 年年底是翻墙最困难的一段时间, 几乎没有服务器可以存活一周. 在 18 年之后, GFW 突然变得非常安静, 在 “和平时期”, 极少有服务器被封禁, 但是在 “敏感时期”, 如两会, 六四, x中全会, 几乎所有服务器都会被封禁, 无论它使用什么协议, 流量规模多大. GFW 已经强大无比, 已经极少有民用手段可以与之抗衡==.
        - 我总认为很多人低估了 GFW 的实力. 2019 年四中全会所带来的封禁给我印象最深刻的是, 我所创建的翻墙服务器寿命都短于一天, 而且是在某个时刻一起挂掉, 这说明 GFW 判断某台 VPS 是否在翻墙所需要收集的信息已经非常少. 在四中全会结束之后, 所有还在小黑屋里的 IP 全部被释放, 同步率之高令人咂舌, 而在往次的封禁中, 这个 “关押期” 至少需要数月. 管理者已经变得成熟而自信, 放任着翻墙者翻墙, 只在敏感的时期释放 GFW 的全部威力, 收放自如.
        - 而在立法层面, 政府对翻墙讳莫如深. 一方面政府不承认墙的存在, 亦不颁布任何法律禁止民众 “偷听敌台”; 另一方面政府又在用口袋罪名和擦边球逮捕具有代表性的商业 VPN 的负责人, 也用喝茶来威慑在墙外网站发表 “不当言论” 的人. ==我过去常常调侃说某些政策是 “严格立法, 普遍违法, 选择执法”; 而政府对 GFW 暧昧的态度却让我觉得管理者 “从不立法, 随机违法, 杀鸡儆猴”. 刑不可知, 则威不可测==.
        - 而翻墙者的态度也同样耐人寻味. 大家似乎已经非常习惯使用特殊手段访问不存在的网站; 这类行为极少被追究, 而我们似乎已经在潜意识中接受了墙的存在. 墙是我们生活的一部分, 是我国特殊国情所带来的 “战时共产主义”, 而我们为翻墙付出的代价也是不可避免和可以接受的. 互联网审查的存在是合理的, 而有特殊需求的人需要自行解决上网问题. 我们为了 “上外网” 学了很多技术, 但偶遇封禁也只得自认倒楣; 敏感的那几天更是 “战争时期”, 哀嚎遍野, 但是大家都可以 “理解”, 并静静等待 “战争” 过去.
        - 更有甚者, 在某些命题中, 墙已经是中国互联网生态和舆论环境的保护神, 其成就是九个指头, 而副作用只是一个指头. 由于 “境外敌对势力” 的存在和国人素质较低的事实存在不可调和的矛盾, 墙扮演了虽不光彩但不可替代的角色: ==只要 GFW 还在, 我们在和西方媒体的舆论高地攻坚战中永远能凯歌高奏. 封禁海外服务是为了打破西方公司的垄断: 在 GFW 的保护下, 我们的民族搜索引擎在 Google 这样的巨无霸面前也能不战而屈人之兵. “洗墙党” 的存在从另一个方面证明了墙的成功==.
        - 管理者和翻墙者之间形成了一种有趣的默契, 这种默契一方面体现在技术层面 – 我们可以私自翻墙, 但是主动权掌握在政府手里; 一方面体现在思想层面 – 我们虽然或多或少在翻墙, 但我们都知道这只是被默许的. 这种默契带来了 GFW 和 翻墙的一种微妙平衡: GFW 以粗粒度的方式过滤掉了大部分 “不需要翻墙” 的人. 我知道任何平衡最后都会被打破, 但是我不知道的是, 到时候天平会向哪一边倾斜?
      - [关于停用 ssr@pku.edu.cn 和我以后的调整](https://wallesspku.com/misc/2019/08/31/email.html)
        collapsed:: true
        - 您好,
        - 我没有任何途径能直接通知您我写了这封信. 它只能躺在我网站的某个角落. So, if you find it, you find it.
        - 从 2019 年 8 月 26 日开始, 我已经不能再使用 PKU 邮箱给您发邮件. 更准确来说, 我已经完全, 永久失去了 PKU 邮箱的所有权利 – 甚至不能读邮件, 包括过去收到的邮件. 封禁的理由是: 违反国家互联网相关管理条例.
        - 对你而言, 唯一的影响是可能你以后再也不会收到我群发的邮件. (我不愿意和学校的部门作对, 所以不计划用别的方式群发邮件) 如果你想看到一些通知, 你只能到我的 blog 来主动看. 对我而言, 我早已预料到学校会用某种方式制裁我, 所以不算惊讶. 我已经毕业, PKU 邮箱不再是必需品, 但是我之前论文中所署的 PKU 邮箱地址将再也没有回音.
        - “翻墙” 到底违法与否, 我不想过多争辩. 在一个并不法制的国家里, 讨论这个问题已经失去意义. 但我一直都相信, 互联网是一个开放的社会, 世界每一个角落的人都有访问它的权利, 而我不希望这个权利被任何人剥夺.
        - 当下次对我的制裁来临时, 我也许不得不停止网站的运营, 甚至可能没有机会再以 blog 的形式通知用户究竟发生了什么. 不过您也不用担心, 事实上有许多商业网站提供和我类似的服务, 在 Google 搜索 “SSR 机场” 就会有很多返回结果, 您可以甄别后使用.
        - 2019 年 8 月 28 日
        - hiaoxui
        - 2019 10 月 5 日记: 略有修改.
      - [WallessPKU](https://wallesspku.com/walless/2019/04/03/privacy.html)
        collapsed:: true
        - [Click](#eng) to scroll down to the English version.
        - ## 我能够收集什么信息?
          collapsed:: true
          - 由于代理服务的特殊性, ==您所被代理的流量, 无论是上行还是下行, 都必须经过我的服务器. 而作为服务器拥有者, 我可以得到您流量的几乎全部信息==, 包括但不限于:
            collapsed:: true
            - * 您流量的目的地. 即: 我可以知道您要访问的网站的域名.
            - * 您流量的内容. 我有能力收集您流量的每一个字节.
          - 这是否意味着您的流量在我面前已经完全透明? 并不是. ==事实上, 互联网上的大部分流量都是经过加密处理. 举例来说, 如果您访问一个 HTTPS 协议的网站 (比如 https://google.com), 您的流量虽然经过了我的服务器, 但我依然无法还原您所访问的内容. 在这种情况下, 我仅知道您访问了 Google, 以及您交换的流量**大小**, 您的内容是保密的==.
          - 但并非所有流量都是加密的. 如果您访问一个 HTTP 协议的网站 (比如 http://www.dean.pku.edu.cn/), 那您的流量对我而言就是完全透明的了. 如果您在这个时候交换了一些私密信息, 比如账号密码, 那您就处我的威胁之中. 这被称为 [中间人攻击](https://zh.wikipedia.org/zh-hans/%E4%B8%AD%E9%97%B4%E4%BA%BA%E6%94%BB%E5%87%BB).
          - 我承诺我不会对您进行中间人攻击. 但我非常建议您保护好您的隐私. 请不要随意在不安全的网站交换重要信息. **如果您的隐私不慎泄漏, 我不对此承担责任.**
        - ## 我在收集什么信息?
          collapsed:: true
          - 我不会对您的流量进行监控. 您的流量经过我的服务器也不会被保留副本. 但为了便于统计和控制每个人的流量, 我目前在收集以下信息:
          - * 您使用服务的时间. 即: 我会监控您什么时候使用服务, 什么时候不.
          - * 您流量的大小. 即: 我会监控您使用了多少流量.
          - 在最坏的条件下, 我可能会被迫记录:
          - 注意这并不包括域名之后的内容. 例如, 假如您访问 https://www.pku.edu.cn/admissions/index.htm, 我只知道您访问了 www.pku.edu.cn, 并不知道您具体在哪个页面停留.
        - ## What can you collect?
          collapsed:: true
          - All the data that proxied by my servers, no matter they’re uploading or downloading data, can be obtained by me. I can collect the information listed as the following:
          - * Your data destination: The website that you’re going to visit.
          - * Your data content: Every byte.
          - Does that mean your data are apparent to me? No. Most of the data on the Internet is encrypted. For example, if you’re going to visit an HTTPS website, e.g. https://google.com, even if your data is going through my server, I’m still unable to know what the data are. They’re just meaningless bytes to me. All I could know is that you just visited Google.
          - But not all the data are encrypted. If you’re going to visit an HTTP website, you’re under my threat, which is called man-in-the-middle attack. If you exchanged some private information, like the password, I would be able to get it.
          - I promise you that I will NOT perpetrate man-in-the-middle attack, but you should take the responsibility yourself. **If your private information was leaked, it wouldn’t be my fault.**
        - ## What are you collecting?
          collapsed:: true
          - I’m not censoring your data. Your data will not be duplicated in my servers. However, to monitor your data usage, I’m currently collecting the following information:
          - * The time that you use my service.
          - * The size/amount of your data usage.
          - In the extreme condition, I reserve the right to collect the following information:
          - Please note the data destination is not the full URL. E.g., if you visited https://www.pku.edu.cn/admissions/index.htm, all I would know is that you visited www.pku.edu.cn, but not the specific page that you stayed.
      - [WallessPKU About](https://wallesspku.com/about/)
        collapsed:: true
        - WallessPKU 由 [hiaoxui](https://gqin.top) 在 2017 年创建. 我 (hiaoxui) 经常被问到一些问题, 在这里做统一回答:
        - 因为翻墙对于几乎所有的科研人员和大部分学生都是 **刚需**. 很多国内无法提供的优质资源, 比如 Google Scholar, YouTube, 甚至处在被墙边缘的 GitHub, 都只能通过翻墙获取. 我自己在北京大学的时候曾经饱受折磨, 进而学会了怎么搭建自己的服务器. 因为常常与人共享, 索性公开了服务, 慢慢改进, 一直做到现在.
        - 服务器 **的确** 是完全免费的. 你找不到任何可以付费的渠道.
        - ==我反而想问问你 “为什么要付费”. 作为中国的网民, 在支付了足额的网费之后, 没有任何一条法律限制了你访问合法的海外互联网的自由, 也没有任何文件明确规定了哪些网站被审查, 或者审查的原则/依据是什么. 你**有权**访问完整的互联网, 你并无义务为自己的**权利**付费.==
        - 有一些不便公开的热心用户/老板曾经捐赠了一些服务器, 它们发挥了很大的作用.
        - 其余资金由我个人承担.
        - 我不方便接受人民币捐赠. 如果有美元账户, 可以通过 [PayPal](https://www.paypal.com/paypalme/hiaoxui) 向我资助. 如果您可以捐赠, 我不胜感激!
        - 是一个团队在维护.
        - 工程部分 (代码/服务器维护) 由我个人完成. 还有很多人选购服务器, 解决技术难题, 回答用户的疑问.
        - 因为安全问题, 暂时不能透露具体有什么人参与.
        -
    - [Vim](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/Vim/)
    - [Git](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/Git/)
    - [GitHub](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/GitHub/)
    - [GNU Make](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/GNU_Make/)
    - [CMake](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/CMake/)
    - [LaTeX](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/LaTeX/)
    - [Docker](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/Docker/)
    - [Scoop](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/Scoop/)
    - [日常学习工作流](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/workflow/)
      collapsed:: true
      - > Contributed by [@HardwayLinka](https://github.com/HardwayLinka)
      - 计算机领域的知识覆盖面很广并且更新速度很快，因此保持终身学习的习惯很重要。但在日常开发和学习的过程中，我们获取知识的来源相对复杂且细碎。有成百上千页的文档手册，也有寥寥数语的博客，甚至闲暇时手机上划过的某则新闻和公众号都有可能包含我们感兴趣的知识。因此，如何利用现有的各类工具，形成一套适合自己的学习工作流，将不同来源的知识碎片整合进属于自己的知识库，方便之后的查阅与复习，就显得尤为重要。经过两年工作之余的学习后，我磨合出了以下学习工作流：
      - ![](https://raw.githubusercontent.com/HardwayLinka/image/master/Drawing 2022-10-20 11.23.41.excalidraw.png)
      - ## 底层核心逻辑
        collapsed:: true
        - 一开始我学习新知识时会参考中文博客，但在代码实践时往往会发现漏洞和bug。我逐渐意识到我参考的信息可能是错误的，毕竟发博客的门槛低，文章可信度不高，于是我开始查阅一些相关的中文书籍。
        - 中文书籍的确是比较全面且系统地讲解了知识点，但众所周知，计算机技术更迭迅速，又因为老美在 CS 方面一直都是灯塔，所以一般中文书籍里的内容会滞后于当前最新的知识，导致我跟着中文书籍实践会出现软件版本差异的问题。这时我开始意识到一手信息的重要性，有些中文书籍是翻译英文书籍的，一般翻译一本书也要一两年，这会导致信息传递的延迟，还有就是翻译的过程中信息会有损失。如果一本中文书籍不是翻译的呢，那么它大概率也参考了其他书籍，参考的过程会带有对英文原著中语义理解的偏差。
        - 于是我就顺其自然地开始翻阅英文书籍。不得不说，英文书籍内容的质量整体是比中文书籍高的。后来随着学习的层层深入，以知识的时效性和完整性出发，我发现 `源代码` \> `官方文档` \> `英文书籍` \> `英文博客` \> `中文博客`，最后我得出了一张 ==`信息损失图`==：
        - ![](https://cdn.sspai.com/2022/10/11/bf07c1965a2e5bdf3f00644737789e2e.png)
        - 虽然一手信息很重要，但后面的 N 手信息并非一无是处，因为这 N 手资料里包含了作者对源知识的转化——例如基于某种逻辑的梳理（流程图、思维导图等）或是一些自己的理解（对源知识的抽象、类比、延伸到其他知识点），这些转化可以帮助我们更快地掌握和巩固知识的核心内容，就如同初高中学习时使用的辅导书。 此外，学习的过程中和别人的交流十分重要，这些 N 手信息同时起了和其他作者交流的作用，让我们能采百家之长。所以这提示我们学习一个知识点时先尽量选择质量更高的，信息损失较少的信息源，同时不妨参考多个信息源，让自己的理解更加全面准确。
        - 现实工作生活中的学习很难像学校里一样围绕某个单一知识点由浅入深，经常会在学习过程中涉及到其他知识点，比如一些新的专有名词，一篇没有读过的经典论文，一段未曾接触过的代码等等。这就要求我们勤于思考，刨根究底地“递归”学习，给多个知识点之间建立联系。
      - ## 选择合适的笔记软件
        collapsed:: true
        - 工作流的骨架围绕 `单个知识点多参考源，勤于提问给多个知识点之间建立联系` 的底层核心逻辑建立。我们写论文其实就是遵循这个底层逻辑的。论文一般会有脚注去解释一些关键字，并且论文末尾会有多个参考的来源，但是我们平时写笔记会随意得多，因此需要更灵活的方式。
        - 平时写代码习惯在 IDE 里一键跳转，把相关的函数和实现很好地联系在了一起。你也许会想，如果笔记也能像代码那样可以跳转就好了。现在市面上 `双链笔记软件` 就可以很好地解决这一痛点，例如 Roam Research、Logseq、Notion 和 Obsidian。Roam Research 和 Logseq 都是基于大纲结构的笔记软件，而 ==`大纲结构` 是劝退我使用这两款软件的原因。一是 `大纲结构` 做笔记容易使文章纵向篇幅太长，二是如果嵌套结构过多会占横向的篇幅==。Notion 页面打开慢，弃之。最终我选择了 Obsidian，原因如下：
        - * Obsidian 基于本地，打开速度快，且可存放很多电子书。我的笔记本是 32g 内存的华硕天选一代，拿来跑 Obsidian 可以快到飞起
        - * Obsidian 基于 Markdown。这也是一个优势，如果笔记软件写的笔记格式是自家的编码格式，那么不方便其他第三方拓展，也不方便将笔记用其他软件打开，比如 qq 音乐下载歌曲有自己的格式，其他播放器播放不了，这挺恶心人的
        - * Obsidian 有丰富的插件生态，并且这个生态既大又活跃，即插件数量多，且热门插件的 star 多，开发者会反馈用户 issue，版本会持续迭代。借助这些插件，可以使 Osidian 达到 `all in one` 的效果，即各类知识来源可以统一整合于一处
      - ## 信息的来源
        collapsed:: true
        - Obsidian 的插件使其可以支持 pdf 格式，而其本身又支持 Markdown 格式。如果想要 `all in one`，那么可以基于这两个格式，将其他格式文件转换为 pdf 或者 Markdown。 那么现在就面临着两个问题：
          collapsed:: true
          - * 有什么格式
          - * 怎么转换为 pdf 或 Markdown
          - ![](https://cdn.sspai.com/2022/10/11/3801b1c9b94286566fe677e3b12cc7b0.png)
        - ### 有什么格式
          collapsed:: true
          - 文件格式依托于其展示的平台，所以在看有什么格式之前，可以罗列一下我平时获取信息的来源：
          - ![](https://cdn.sspai.com/2022/10/11/07e97f372850054958d4961a3787a93f.png)
          - 可以看到主要分为`文章`、`论文`、`电子书`、`课程`四类，包含的格式主要有 `网页`、`pdf` 、`mobi`、`azw`、`azw3`。
        - ### 怎么转换为 pdf 或 Markdown
          collapsed:: true
          - 在线的文章和课程等大多以网页形式呈现，而将网页转换为 Markdown 可以使用剪藏软件，它可以将网页文章转换为多种文本格式文件。我选择的工具是简悦，使用简悦可以将几乎所有平台的文章很好地剪藏为 Markdown 并且导入到 Obsidian。
          - ![](https://cdn.sspai.com/2022/10/11/211cffa78f20a9e7286a7419e9e0b878.png)
          - 对于论文和电子书而言如果格式本身就是 pdf 则万事大吉，但如果是其他格式则可以使用 calibre 进行转换：
          - ![](https://cdn.sspai.com/2022/10/11/51575f65f6f4c6edfa6c5b97fd16d625.png)
          - 现在利用 Obsidian 的 pdf 插件和其原生的 markdown 支持就可以畅快无比地做笔记并且在这些文章的对应章节进行无缝衔接地引用跳转啦（具体操作参考下文的“信息的处理”模块）。
          - ![](https://cdn.sspai.com/2022/10/11/d64a9a2d6406d2d367dcb505ede69c83.png)
        - ### 如何统一管理信息来源
          collapsed:: true
          - 对于 pdf 等文件类资源可以本地或者云端存储，而网页类资源则可以分门别类地放入浏览器的收藏夹，或者剪藏成 markdown 格式的笔记，但是网页浏览器不能实现移动端的网页收藏。为了实现跨端网页收藏我选用了 Cubox，在手机端看到感兴趣的网页时只需小手一划，便能将网页统一保存下来。虽然免费版只能收藏 100 个网页，但其实够用了，还可以在收藏满时督促自己赶紧剪藏消化掉这些网页，让收藏不吃灰。
          - ![](https://cdn.sspai.com/2022/10/11/ad7ebfcb4619f64a41d328b88e0e3a12.png)
          - 除此之外，回想一下我们平时收藏的网页，就会发现有很多并不是像知乎、掘金这类有完整功能的博客平台，更多的是个人建的小站，而这些小站往往没有移动端应用，这样平时刷手机的时候也看不到，放到浏览器的收藏夹里又容易漏了看，有新文章发布我们也不能第一时间收到通知，这个时候就需要一种叫 `RSS` 的通信协议。
          - `RSS`（英文全称：RDF Site Summary 或 Really Simple Syndication），中文译作简易信息聚合，也称聚合内容，是一种消息来源格式规范，用以聚合多个网站更新的内容并自动通知网站订阅者。电脑端可以借助 `RSSHub Radar` 来快速发现和生成 `RSS` 订阅源，接着使用 `Feedly` 来订阅这些 `RSS` 订阅源（`RSSHub Radar` 和 `Feedly` 在 chrome 浏览器中均有官方插件）。
          - ![](https://cdn.sspai.com/2022/10/11/5df6cd9d967f190df35928e781f9185f.png)
          - 到这里为止，收集信息的流程已经比较完备了。但资料再多，分类规整得再漂亮，也得真正内化成自己的才管用。因此在收集完信息后就得进一步地处理信息，即阅读这些信息，如果是英文信息的话还得搞懂英文的语义，加粗高亮重点句子段落，标记有疑问的地方，发散联想相关的知识点，最后写上自己的总结。那么在这过程中需要使用到什么工具呢？
      - ## 信息的处理
        collapsed:: true
        - ### 英文信息
          collapsed:: true
          - 面对英文的资料，我以前是用 `有道词典` 来划词翻译，遇到句子的话就使用谷歌翻译，遇到大段落时就使用 `deepl`，久而久之，发现这样看英语文献太慢了，得用三个工具才能满足翻译这一个需求，如果有一个工具能够同时实现对单词、句子和段落的划词翻译就好了。我联想到研究生们应该会经常接触英语文献，于是我就搜 `研究生` \+ `翻译软件`，在检索结果里我最终选择了 `Quicker` \+ `沙拉查词` 这个搭配来进行划词翻译。
          - ![](https://cdn.sspai.com/2022/10/11/a7ebb1d3c46702b56bd6d171dfcfc075.png)
          - 使用这套组合可以实现在浏览器外的其他软件内进行划词翻译，并且支持单词、句子和段落的翻译，以及每次的翻译会有多个翻译平台的结果。btw，如果查单词时不着急的话，可以顺便看看 `科林斯高阶` 的翻译，这个词典的优点就是会用英文去解释英文，可以提供多个上下文帮助你理解，对于学习英文单词也有帮助，因为用英文解释英文才更接近英语的思维。
          - ![](https://cdn.sspai.com/2022/10/11/article/827c9a8048c83e504ccb15893702bf09)
        - ### 多媒体信息
          collapsed:: true
          - 处理完文本类的信息后，我们还得思考一下怎么处理多媒体类的信息。此处的多媒体我特指英文视频，因为我没有用播客或录音学习的习惯，而且我已经基本不看中文教程了。现在很多国外名校公开课都是以视频的形式，如果能对视频进行做笔记会不会有帮助呢？不知道大家有没这样的想法，就是如果能把老师上课讲的内容转换成文本就好了，因为平时学习时我们看书的速度往往会比老师讲课的速度快。刚好 `Language Reactor` 这个软件可以将油管和网飞内视频的字幕导出来，同时附上中文翻译。
          - 我们可以把 `Language Reactor` 导出的字幕复制到 `Obsidian` 里面作为文章来读。除了出于学习的需求，也可以在平时看油管的视频时打开这个插件，这个插件可以同时显示中英文字幕，并且可以单击选中英文字幕中你认为生僻的单词后显示单词释义。
          - ![](https://cdn.sspai.com/2022/10/11/364c8e6ed263affa84d9eee61338b4af.png)
          - 但阅读文本对于一些抽象的知识点来说并不是效率最高的学习方式。俗话说，一图胜千言，能不能将某一段知识点的文本和对应的图片甚至视频画面操作联系起来呢？我在浏览 `Obsidian` 的插件市场时，发现了一个叫 `Media Extended` 的插件，这个插件可以在你的笔记里添加跳转到视频指定时间进度的链接，相当于把你的笔记和视频连接起来了！这刚好可以和我上文提到的生成视频中英文字幕搭配起来，即每一句字幕对应一个时间，并且能根据时间点跳转到视频的指定进度，如此一来如果需要在文章中展示记录了操作过程的视频的话，就不需要自己去截取对应的视频片段，而是直接在文章内就能跳转！
          - ![](https://cdn.sspai.com/2022/10/11/17554cfdf662d5719ada453674012fdb.gif)
          - `Obsidian` 里还有一个很强大的插件，叫 `Annotator`，它可以实现笔记内跳转到 pdf 原文
          - ![](https://cdn.sspai.com/2022/10/11/article/b56994bf9a306830d8b0b8112677d3ec)
          - 现在，使用 `Obsidian` 自带的双链功能，可以实现笔记间相互跳转，结合上述两个插件，可以实现笔记到多媒体的跳转，信息的处理过程已经完备。一般我们学习的过程相当于上山和下山，刚学的时候就好像上山，很陌生、吃力，所谓学而时习之，复习或练习的过程就像下山，没有陌生感，不见得轻松，但非走不可。那么如何把复习这一过程纳入工作流的环节里呢？
      - ## 信息的回顾
        collapsed:: true
        - `Obsidian` 内已经有一个连接 `Anki` 的插件，`Anki` 就是大名鼎鼎的、基于间隔重复的记忆软件。使用该插件可以截取笔记的片段导出到 `Anki` 并变成一张卡片，卡片内也有跳转回笔记原文的链接
        - ![](https://cdn.sspai.com/2022/10/11/1f7cebd8dd28f664d77cbf0ab228c406.gif)
      - ## 总结
        collapsed:: true
        - 这个工作流是在我这两年业余时间学习时所慢慢形成的，在学习过程中因为对一些重复性的过程而感到厌倦，正是这种厌倦产生了某种特定的需求，恰好在平时网上冲浪时了解到的一些工具满足了我这些需求。不要为了虚无的满足感而将工具强行拼凑到自己的工作流中，人生苦短，做实事最紧要。
        - btw，此篇文章是讲解工作流的演化思路，如果对此工作流的实现细节感兴趣，建议阅读完本文后再按顺序阅读以下文章
        - 1. [3000 + 小时积累的学习工作流](https://sspai.com/post/75969)
        - 2. [Obsidian 的高级玩法 | 打造能跳转到任何格式文件的笔记](https://juejin.cn/post/7145351315705577485)
    - [实用工具箱](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/tools/) #[[navigation]]
      collapsed:: true
      - ## 下载工具
        collapsed:: true
        - [Sci-Hub](https://sci-hub.se/): Elbakyan 女神向你挥手，旨在打破知识壁垒的革命性网站。
        - [Library Genesis](http://libgen.is/): 电子书下载网站。
        - [Z-library](https://z-lib.is/): 电子书下载网站（在 [Tor](https://www.torproject.org/) 下运行较佳，[链接](http://loginzlib2vrak5zzpcocc3ouizykn6k5qecgj2tzlnab5wcbqhembyd.onion/)）。
        - [Z-ePub](https://z-epub.com/): ePub 电子书下载网站。
        - [PDF Drive](https://www.pdfdrive.com/): PDF 电子书搜索引擎。
        - [MagazineLib](https://magazinelib.com/): PDF 电子杂志下载网站。
        - [BitDownloader](https://bitdownloader.io/): 油管视频下载器。
        - [qBittorrent](https://www.qbittorrent.org/download.php): BitTorrent 客户端。
        - [uTorrent](https://www.utorrent.com/): BitTorrent 客户端。
        - [全国标准信息公共服务平台](https://std.samr.gov.cn/)：各类标准查询和下载官方平台。
        - [标准知识服务系统](http://www.standards.com.cn/)：检索与阅读所需标准。
      - ## 设计工具
        collapsed:: true
        - [excalidraw](https://excalidraw.com/): 一款手绘风格的绘图工具，非常适合绘制课程报告或者PPT内的示意图。
        - [tldraw](https://www.tldraw.com/): 一个绘图工具，适合画流程图，架构图等。
        - [origamiway](https://www.origamiway.com/paper-folding-crafts-step-by-step.shtml): 手把手教你怎么折纸。
        - [thingiverse](https://www.thingiverse.com/): 囊括各类 2D/3D 设计资源，其 STL 文件下载可直接 3D 打印。
        - [iconfont](https://www.iconfont.cn/): 国内最大的图标和插画资源库，可用于开发或绘制系统架构图。
        - [turbosquid](https://www.turbosquid.com/): 可以购买各式各样的模型。
        - [flaticon](https://www.flaticon.com/): 可下载免费且高质量的图标。
        - [标准地图服务系统](http://bzdt.ch.mnr.gov.cn/): 可以下载官方标准地图。
        - [PlantUML](https://plantuml.com/zh/): 可以使用代码快速编写 UML 图。
      - ## 编程相关
        collapsed:: true
        - [sqlfiddle](http://www.sqlfiddle.com/): 一个简易的在线 SQL Playground。
        - [sqlzoo](https://sqlzoo.net/wiki/SQL_Tutorial)：在线练习 sql 语句。
        - [godbolt](https://godbolt.org/): 非常方便的编译器探索工具。你可以写一段 C/C++ 代码，选择一款编译器，然后便可以观察生成的具体汇编代码。
        - [explainshell](https://explainshell.com/): 你是否曾为一段 shell 代码的具体含义感到困扰？manpage 看半天还是不明所以？试试这个网站！
        - [regex101](https://regex101.com/): 正则表达式调试网站，支持各种编程语言的匹配标准。
        - [typingtom](https://www.typingtom.com/lessons): 针对程序员的打字练习/测速网站。
        - [wrk](https://github.com/wg/wrk): 网站压测工具。
        - [gbmb](https://www.gbmb.org/): 数据单位转换。
        - [tools](https://tools.fun/): 在线工具合集。
        - [github1s](https://github1s.com/): 用网页版 VS Code 在线阅读 GitHub 代码。
        - [visualgo](https://visualgo.net/en): 算法可视化网站。
        - [DataStructureVisual](http://www.rmboot.com/): 数据结构可视化网站。
        - [Data Structure Visualizations](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html): 数据结构与算法的可视化网站。
        - [learngitbranching](https://learngitbranching.js.org/?locale=zh_CN): 可视化学习 git。
      - [UnicodeCharacter](https://unicode-table.com/en/): Unicode 字符集网站。
      - ## 学习网站
        collapsed:: true
        - [HFS](https://hepsoftwarefoundation.org/training/curriculum.html): 各类软件教程。
        - [os-wiki](https://wiki.osdev.org/Main_Page): 操作系统技术资源百科全书。
        - [Shadertoy](https://www.shadertoy.com/): 编写各式各样的 shader。
        - [comments-for-awesome-courses](https://conanhujinming.github.io/comments-for-awesome-courses/): 名校公开课评价网。
        - [codetop](https://codetop.cc/home): 企业题库。
        - [cs-video-courses](https://github.com/Developer-Y/cs-video-courses): 带有视频讲座的计算机科学课程列表。
        - [bootlin](https://elixir.bootlin.com/linux/v2.6.39.4/source/include/linux): 在线阅读 Linux 源码。
        - [ecust-CourseShare](https://github.com/tianyilt/ecnu-PGCourseShare): 华东师范大学研究生课程攻略共享计划。
        - [REKCARC-TSC-UHT](https://github.com/PKUanonym/REKCARC-TSC-UHT): 清华大学计算机系课程攻略。
        - [seu-master](https://github.com/oneman233/seu-master): 东南大学研究生课程资料整理。
      - ## 杂项
        collapsed:: true
        - [tophub](https://tophub.today/): 新闻热榜合集（综合了知乎、微博、百度、微信等）。
        - [feedly](https://feedly.com/): 著名的 RSS 订阅源阅读器。
        - [speedtest](https://www.speedtest.net/zh-Hans): 在线网络测速网站。
        - [public-apis](https://github.com/public-apis/public-apis): 公共 API 合集列表。
        - [numberempire](https://zh.numberempire.com/derivativecalculator.php): 函数求导工具。
        - [sustech-application](https://sustech-application.com/#/grad-application/computer-science-and-engineering/README): 南方科技大学经验分享网。
        - [vim-adventures](https://vim-adventures.com/): 一款基于 vim 键盘快捷键的在线游戏。
        - [vimsnake](https://vimsnake.com/): 利用 vim 玩贪吃蛇。
        - [keybr](https://www.keybr.com/): 学习盲打的网站。
    - [毕业论文](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/thesis/)
      collapsed:: true
      - 2022年，我本科毕业了。在开始动手写毕业论文的时候，我尴尬地发现，我对 Word 的掌握程度仅限于调节字体、保存导出这些傻瓜功能。曾想转战 Latex，但论文的段落格式要求调整起来还是用 Word 更为方便，经过一番痛苦缠斗之后，总算是有惊无险地完成了论文的写作和答辩。为了不让后来者重蹈覆辙，遂把相关资源整理成一份开箱即用的文档，供大家参考。
      - ## 如何用 Word 写毕业论文
        collapsed:: true
        - 正如将大象装进冰箱需要三步，用 Word 写毕业论文也只需要简单三步：
        - * 确定论文的格式要求：通常学院都会下发毕业论文的格式要求（各级标题的字体字号、图例和引用的格式等等），如果更为贴心的话甚至会直接给出论文模版（如是此情况请直接跳转到下一步）。很不幸的是，我的学院并没有下发标准的论文格式要求，还提供了一份格式混乱几乎毫无用处的论文模版膈应我，被逼无奈之下我找到了北京大学研究生的[论文格式要求](https://github.com/PKUFlyingPig/Thesis-Template/blob/master/%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6%E7%A0%94%E7%A9%B6%E7%94%9F%E5%AD%A6%E4%BD%8D%E8%AE%BA%E6%96%87%E5%86%99%E4%BD%9C%E6%8C%87%E5%8D%97.pdf)，并按照其要求制作了[一份模版](https://github.com/PKUFlyingPig/Thesis-Template/blob/master/%E8%AE%BA%E6%96%87%E6%A8%A1%E7%89%88.docx)，大家需要的话自取，本人不承担无法毕业等任何责任。
        - * 学习 Word 排版：到达这一步的童鞋分为两类，一是已经拥有了学院提供的标准模版，二是只有一份虚无缥缈的格式要求。那现在当务之急就是学习基础的 Word 排版技术，对于前者可以学会使用模版，对于后者则可以学会制作模版。此时切记不要雄心勃勃地选择一个十几个小时的 Word 教学视频开始头悬梁锥刺股，因为生产一份应付毕业的学术垃圾只要学半小时能上手就够了。我当时看的[一个 B 站的教学视频](https://www.bilibili.com/video/BV1YQ4y1M73G?p=1&vd%5Fsource=a4d76d1247665a7e7bec15d15fd12349)，短小精悍非常实用，全长半小时极速入门。
        - * 生产学术垃圾：最容易的一步，大家八仙过海，各显神通吧，祝大家毕业顺利～～
    - [信息检索](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/%E4%BF%A1%E6%81%AF%E6%A3%80%E7%B4%A2/)
  - [好书推荐](https://csdiy.wiki/%E5%A5%BD%E4%B9%A6%E6%8E%A8%E8%8D%90/)
    collapsed:: true
    - 由于版权原因，下面列举的图书中除了开源资源提供了链接，其他的资源请大家自行通过 [libgen](http://libgen.is/) 或 [z-lib](https://z-lib.org/) 查找。
    - ## 资源汇总
      collapsed:: true
      - [Free Programming Books](https://github.com/EbookFoundation/free-programming-books): 开源编程书籍资源汇总
      - [CS Textbook Recommendations](https://4chan-science.fandom.com/wiki/Computer_Science_and_Engineering): 计算机科学方向推荐教材列表
      - [C Book Guide and List](https://stackoverflow.com/questions/562303/the-definitive-c-book-guide-and-list): C语言相关的编程书籍推荐列表
      - [C++ Book Guide and List](https://stackoverflow.com/questions/388242/the-definitive-c-book-guide-and-list): C++语言相关的编程书籍推荐列表
      - [Python Book Guide and List](https://pythonbooks.org/): Python语言相关的编程书籍推荐列表
      - [Computer Vision Textbook Recommendations](https://www.folio3.ai/blog/best-computer-vision-books/): 计算机视觉方向推荐教材列表
      - [Deep Learning Textbook Recommendations](https://www.mostrecommendedbooks.com/lists/best-deep-learning-books): 深度学习方向推荐教材列表
    - ## 系统入门
      collapsed:: true
      - Computer Systems: A Programmer's Perspective [[豆瓣](https://book.douban.com/subject/26912767/)]
      - Principles of Computer System Design: An Introduction [[豆瓣](https://book.douban.com/subject/3707841/)]
    - ## 操作系统
      collapsed:: true
      - [现代操作系统: 原理与实现](https://ipads.se.sjtu.edu.cn/mospi/) [[豆瓣](https://book.douban.com/subject/35208251/)]
      - [Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) [[豆瓣](https://book.douban.com/subject/19973015/)]
      - Modern Operating Systems [[豆瓣](https://book.douban.com/subject/27096665/)]
      - Operating Systems: Principles and Practice [[豆瓣](https://book.douban.com/subject/25984145/)]
    - ## 计算机网络
      - [Computer Networks: A Systems Approach](https://book.systemsapproach.org/foreword.html) [[豆瓣](https://book.douban.com/subject/26417896/)]
      - [Computer Networking: A Top-Down Approach](https://www.ucg.ac.me/skladiste/blog_44233/objava_64433/fajlovi/Computer%20Networking%20_%20A%20Top%20Down%20Approach,%207th,%20converted.pdf) [[豆瓣](https://book.douban.com/subject/30280001/)]
      - How Networks Work [[豆瓣](https://book.douban.com/subject/26941639/)]
    - ## 分布式系统
      - [Patterns of Distributed System (Blog)](https://github.com/dreamhead/patterns-of-distributed-systems)
      - [Distributed Systems for Fun and Profit (Blog)](http://book.mixu.net/distsys/index.html)
      - [Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems](https://github.com/Vonng/ddia) [[豆瓣](https://book.douban.com/subject/26197294/)]
    - ## 数据库系统
      - [Architecture of a Database System](https://dsf.berkeley.edu/papers/fntdb07-architecture.pdf) [[豆瓣](https://book.douban.com/subject/17665384/)]
      - [Readings in Database Systems](http://www.redbook.io/) [[豆瓣](https://book.douban.com/subject/2256069/)]
      -
      - Database System Concepts [[豆瓣](https://book.douban.com/subject/10548379/)]
    - ## 编译原理
      collapsed:: true
      - Engineering a Compiler [[豆瓣](https://book.douban.com/subject/5288601/)]
      - Compilers: Principles, Techniques, and Tools [[豆瓣](https://book.douban.com/subject/1866231/)]
      - [Crafting Interpreters](https://craftinginterpreters.com/contents.html)[[豆瓣]](https://book.douban.com/subject/35548379/)[[开源中文翻译]](https://github.com/GuoYaxiang/craftinginterpreters_zh)
    - ## 计算机编程语言
      collapsed:: true
      - 计算机程序的构造和解释 [[豆瓣](https://book.douban.com/subject/1148282/)]
      - [Essentials of Programming Languages](https://eopl3.com/) [[豆瓣](https://book.douban.com/subject/3136252/)]
      - [Practical Foundations for Programming Languages](https://www.cs.cmu.edu/~rwh/pfpl.html) [[豆瓣](https://book.douban.com/subject/26782198/)]
      - [Software Foundations](https://softwarefoundations.cis.upenn.edu/) [[豆瓣](https://book.douban.com/subject/25712292/)] [[北大相关课程](https://xiongyingfei.github.io/SF/2021/)]
      - [Types and Programming Languages](https://www.cis.upenn.edu/~bcpierce/tapl/) [[豆瓣](https://book.douban.com/subject/1761910/)] [[北大相关课程](https://xiongyingfei.github.io/DPPL/2021/main.htm)]
    - ## 体系结构
      collapsed:: true
      - 超标量处理器设计: Superscalar RISC Processor Design [[豆瓣](https://book.douban.com/subject/26293546/)]
      - Computer Organization and Design RISC-V Edition [[豆瓣](https://book.douban.com/subject/27103952/)]
      - Computer Organization and Design: The Hardware/Software Interface [[豆瓣](https://book.douban.com/subject/26604008/)]
      - Computer Architecture: A Quantitative Approach [[豆瓣](https://book.douban.com/subject/6795919/)]
    - ## 理论计算机科学
      collapsed:: true
      - Introduction to the Theory of Computation [[豆瓣](https://book.douban.com/subject/1852515/)]
    - ## 密码学
      collapsed:: true
      - Cryptography Engineering: Design Principles and Practical Applications [[豆瓣](https://book.douban.com/subject/26416592/)]
      - Introduction to Modern Cryptography [[豆瓣](https://book.douban.com/subject/2678340/)]
    - ## 逆向工程
      collapsed:: true
      - 逆向工程核心原理 [[豆瓣](https://book.douban.com/subject/25866389/)]
      - 加密与解密 [[豆瓣](https://book.douban.com/subject/30288807/)]
    - ## 计算机图形学
      collapsed:: true
      - [Monte Carlo theory, methods and examples](https://artowen.su.domains/mc/)[[豆瓣](https://book.douban.com/subject/6089923/)]
      - Advanced Global Illumination [[豆瓣](https://book.douban.com/subject/2751153/)]
      - Fundamentals of Computer Graphics [[豆瓣](https://book.douban.com/subject/26868819/)]
      - [Fluid Simulation for Computer Graphics](http://wiki.cgt3d.cn/mediawiki/images/4/43/Fluid_Simulation_for_Computer_Graphics_Second_Edition.pdf) [[豆瓣](https://book.douban.com/subject/2584523/)]
      - [Physically Based Rendering: From Theory To Implementation](https://research.quanfita.cn/files/Physically_Based_Rendering_Third_Edition.pdf) [[豆瓣](https://book.douban.com/subject/4306242/)]
      - [Real-Time Rendering](https://research.quanfita.cn/files/Real-Time_Rendering_4th_Edition.pdf) [[豆瓣](https://book.douban.com/subject/30296179/)]
    - ## 游戏引擎
      collapsed:: true
      - 游戏编程模式: Game Programming Patterns [[豆瓣](https://book.douban.com/subject/26880704/)]
      - 实时碰撞检测算法技术 [[豆瓣](https://book.douban.com/subject/4861957/)]
      - [Game AI Pro Series](http://www.gameaipro.com/) [[豆瓣](https://search.douban.com/book/subject_search?search_text=Game+AI+Pro&cat=1001)]
      - Artificial Intelligence for Games [[豆瓣](https://book.douban.com/subject/3836472/)]
      - Game Engine Architecture [[豆瓣](https://book.douban.com/subject/25815142/)]
      - Game Programming Gems Series [[豆瓣](https://search.douban.com/book/subject_search?search_text=Game+Programming+Gems&cat=1001)]
    - ## 软件工程
      collapsed:: true
      - [Software Engineering at Google](https://abseil.io/resources/swe-book) [[豆瓣](https://book.douban.com/subject/34875994/)]
    - ## 设计模式
      collapsed:: true
      - 设计模式: 可复用面向对象软件的基础 [[豆瓣](https://book.douban.com/subject/1052241/)]
      - 大话设计模式 [[豆瓣](https://book.douban.com/subject/2334288/)]
      - [Head First 设计模式](https://awesome-programming-books.github.io/design-pattern/HeadFirst%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F.pdf) [[豆瓣](https://book.douban.com/subject/2243615/)]
    - ## 深度学习
      collapsed:: true
      - [动手学深度学习](https://zh.d2l.ai/) [[豆瓣](https://book.douban.com/subject/33450010/)]
      - [神经网络与深度学习](https://nndl.github.io/) [[豆瓣](https://book.douban.com/subject/35044046/)]
      - 深度学习入门 [[豆瓣](https://book.douban.com/subject/30270959/)]
      - [简单粗暴 TensorFlow 2 (Tutorial)](https://tf.wiki/)
      - [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/) [[豆瓣](https://book.douban.com/subject/5373023/)]
    - ## 计算机视觉
      collapsed:: true
      - [Multiple View Geometry in Computer Vision](https://github.com/DeepRobot2020/books/blob/master/Multiple%20View%20Geometry%20in%20Computer%20Vision%20(Second%20Edition).pdf) [[豆瓣](https://book.douban.com/subject/1841346/)]
    - ## 机器人
      collapsed:: true
      - [Probabilistic Robotics](https://docs.ufpr.br/~danielsantos/ProbabilisticRobotics.pdf) [[豆瓣](https://book.douban.com/subject/2861227/)]
    - ## 面试
      collapsed:: true
      - 剑指 Offer：名企面试官精讲典型编程题 [[豆瓣](https://book.douban.com/subject/27008702/)]
      - Cracking The Coding Interview [[豆瓣](https://book.douban.com/subject/10436668/)]
  - 数学基础
    collapsed:: true
    - [MIT18.01/18.02: Calculus](https://csdiy.wiki/%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A1%80/MITmaths/)
    - [MIT18.06: Linear Algebra](https://csdiy.wiki/%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A1%80/MITLA/)
    - [MIT6.050J: Information theory and Entropy](https://csdiy.wiki/%E6%95%B0%E5%AD%A6%E5%9F%BA%E7%A1%80/information/)
  - 数学进阶
    collapsed:: true
    - [UCB CS70: discrete Math and probability theory](https://csdiy.wiki/%E6%95%B0%E5%AD%A6%E8%BF%9B%E9%98%B6/CS70/)
      collapsed:: true
      - * 所属大学：UC Berkeley
      - * 先修要求：无
      - * 编程语言：无
      - * 课程难度：🌟🌟🌟
      - * 预计学时：60 小时
      - 伯克利的离散数学入门课程，个人觉得这门课最大的亮点在于并不是单纯的理论知识的讲授，而是在每个模块都会介绍理论知识在实际算法中的运用，让计算机系的学生在夯实理论基础的同时，跳脱出冰冷形式化的数学符号，在实际应用中感受和体会理论的本质。
      - 具体的理论与算法的对应关系列举如下：
        collapsed:: true
        - * 逻辑证明：稳定匹配算法
        - * 图论：网络拓扑设计
        - * 基础数论：RSA 算法
        - * 多项式环：纠错码设计
        - * 概率论：哈希表设计、负载均衡等等
      - 课程 notes 也写得非常深入浅出，公式推导与实际例子星罗棋布，阅读体验很好。
      - ## 课程资源
        collapsed:: true
        - * 课程网站： http://www.eecs70.org/
        - * 课程教材：参见课程 notes
        - * 课程作业：参见课程 Schedule
      - ## 资源汇总
        collapsed:: true
        - @PKUFlyingPig 在学习这门课中用到的所有资源和作业实现都汇总在 [PKUFlyingPig/UCB-CS70 - GitHub](https://github.com/PKUFlyingPig/UCB-CS70) 中。
    - [UCB CS126: probability theory](https://csdiy.wiki/%E6%95%B0%E5%AD%A6%E8%BF%9B%E9%98%B6/CS126/)
    - [MIT 6.042J: Mathematics for Computer Science](https://csdiy.wiki/%E6%95%B0%E5%AD%A6%E8%BF%9B%E9%98%B6/6.042J/) #mit/6.042_Mathematics_for_Computer_Science
      collapsed:: true
      - ## 课程简介
        collapsed:: true
        - 所属大学：MIT
        - 先修要求：Calculus, Linear Algebra
        - 编程语言：Python preferred
        - 课程难度：🌟🌟🌟
        - 预计学时：50-70 小时
        - MIT 的离散数学以及概率综合课程，导师是大名鼎鼎的 **Tom Leighton** ( Akamai 的联合创始人之一)。学完之后对于后续的算法学习大有裨益。
      - ## 课程资源
        collapsed:: true
        - 课程网站：[https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/)
        - 课程视频：[https://www.bilibili.com/video/BV1L741147VX](https://www.bilibili.com/video/BV1L741147VX)
        - 课程作业：[https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/assignments/](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/assignments/)
    - [MIT18.330: Introduction to numerical analysis](https://csdiy.wiki/%E6%95%B0%E5%AD%A6%E8%BF%9B%E9%98%B6/numerical/)
    - [Standford EE364A: Convex Optimization](https://csdiy.wiki/%E6%95%B0%E5%AD%A6%E8%BF%9B%E9%98%B6/convex/)
    - [The Information Theory, Pattern Recognition, and Neural Networks](https://csdiy.wiki/%E6%95%B0%E5%AD%A6%E8%BF%9B%E9%98%B6/The_Information_Theory_Pattern_Recognition_and_Neural_Networks/)
  - 编程入门
    collapsed:: true
    - [MIT-Missing-Semester](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/MIT-Missing-Semester/)
    - [Harvard CS50: This is CS50x](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/CS50/)
    - [CS50P: CS50's Introduction to Programming with Python](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/CS50P/)
    - [UCB CS61A: Structure and Interpretation of Computer Programs](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/CS61A/)
    - [Duke University: Introductory C Programming Specialization](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/Duke-Coursera-Intro-C/)
    - [Stanford CS106B/X](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/CS106B_CS106X/)
    - [Stanford CS106L: Standard C++ Programming](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/CS106L/)
    - [Stanford CS110L: Safety in Systems Programming](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/CS110L/)
    - [AmirKabir University of Technology AP1400-2: Advanced Programming](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/AUT1400/)
    - [Haskell MOOC](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/Haskell-MOOC/)
  - 电子基础
    collapsed:: true
    - [EE16A&B: Designing Information Devices and Systems I&II](https://csdiy.wiki/%E7%94%B5%E5%AD%90%E5%9F%BA%E7%A1%80/EE16/)
    - [UCB EE120 : Signal and Systems](https://csdiy.wiki/%E7%94%B5%E5%AD%90%E5%9F%BA%E7%A1%80/signal/)
    - [MIT 6.007 Signals and Systems](https://csdiy.wiki/%E7%94%B5%E5%AD%90%E5%9F%BA%E7%A1%80/Signals_and_Systems_AVO/)
  - 数据结构与算法
    collapsed:: true
    - [UCB CS61B: Data Structures and Algorithms](https://csdiy.wiki/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E4%B8%8E%E7%AE%97%E6%B3%95/CS61B/)
    - [Coursera: Algorithms I & II](https://csdiy.wiki/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E4%B8%8E%E7%AE%97%E6%B3%95/Algo/)
    - [MIT 6.006: Introduction to Algorithms](https://csdiy.wiki/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E4%B8%8E%E7%AE%97%E6%B3%95/6.006/)
    - [MIT 6.046: Design and Analysis of Algorithms](https://csdiy.wiki/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E4%B8%8E%E7%AE%97%E6%B3%95/6.046/)
    - [UCB CS170: Efficient Algorithms and Intractable Problems](https://csdiy.wiki/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E4%B8%8E%E7%AE%97%E6%B3%95/CS170/)
  - 软件工程
    collapsed:: true
    - [MIT 6.031: Software Construction](https://csdiy.wiki/%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B/6031/)
    - [UCB CS169: software engineering](https://csdiy.wiki/%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B/CS169/)
  - 体系结构
    collapsed:: true
    - [Coursera: Nand2Tetris](https://csdiy.wiki/%E4%BD%93%E7%B3%BB%E7%BB%93%E6%9E%84/N2T/)
    - [Digital Design and Computer Architecture](https://csdiy.wiki/%E4%BD%93%E7%B3%BB%E7%BB%93%E6%9E%84/DDCA/)
    - [UCB CS61C: Great Ideas in Computer Architecture](https://csdiy.wiki/%E4%BD%93%E7%B3%BB%E7%BB%93%E6%9E%84/CS61C/)
    - [CMU 15-213: CSAPP - CS自学指南](https://csdiy.wiki/%E4%BD%93%E7%B3%BB%E7%BB%93%E6%9E%84/CSAPP/) #csapp
      collapsed:: true
      - * 所属大学：CMU
      - * 先修要求：CS61A, CS61B
      - * 编程语言：C
      - * 课程难度：🌟🌟🌟🌟🌟
      - * 预计学时：150 小时
      - ==CMU 大名鼎鼎的镇系神课，以其内容庞杂，Project 巨难而闻名遐迩。课程内容覆盖了汇编语言、体系结构、操作系统、编译链接、并行、网络等，作为系统入门课，兼具深度和广度，如果自学确实需要相当的毅力和代码功底。==
      - 这门课配合的教材由 CMU 计算机系主任 Bryant 教授执笔，也即所谓的 CSAPP。这也是我第一本认认真真一页一页读过去的计算机教材，虽然很难啃，但着实收获良多。
      - 北大购买了这门课的版权并开设了 Introduction to Computer System 这门课，但其实 CSAPP 所有的课程资源和实验代码都能在它的官方主页上访问到（具体参见下方链接）。
      - 这门课由于过于出名，全世界的码农争相学习，导致其 Project 的答案在网上几乎唾手可得。但如果你真的想锻炼自己的代码能力，希望你不要借鉴任何第三方代码。
      - 认真学完这一门课，你对计算机系统的理解绝对会上升一个台阶。
      - ## 课程资源
        collapsed:: true
        - 课程网站：[http://csapp.cs.cmu.edu/](http://csapp.cs.cmu.edu/)
        - 课程视频：[https://www.bilibili.com/video/BV1iW411d7hd](https://www.bilibili.com/video/BV1iW411d7hd)
        - 课程教材：Computer Systems: A Programmer's Perspective, 3/E
        - 课程作业：11 个 Project，[代码框架全部开源](http://csapp.cs.cmu.edu/3e/labs.html)
        - 英语有困难的同学可以参考B站UP主[九曲阑干](https://space.bilibili.com/354767108/)对 CSAPP 的[中文讲解](https://www.bilibili.com/video/BV1cD4y1D7uR)（据说CMU的中国留学生也在CMU的课堂上看这个视频呢）。另外如果大家在看完 CSAPP 后对书中的第七章链接有一定的疑问，推荐阅读《程序员的自我修养》这本书，书的副标题是链接，装载与库。这本书能够帮助我们完善对程序链接的理解，相信你在看完这本书以后可以对程序的链接，ELF 文件，动态库都将有一个更加深入的理解。十分推荐在读完 CSAPP，对计算机系统有一定的了解以后作为补充资料来阅读。
  - 操作系统
    collapsed:: true
    - [MIT 6.S081: Operating System Engineering](https://csdiy.wiki/%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/MIT6.S081/)
    - [UCB CS162: Operating System](https://csdiy.wiki/%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/CS162/)
    - [NJU OS: Operating System Design and Implementation](https://csdiy.wiki/%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/NJUOS/)
  - 并行与分布式系统
    collapsed:: true
    - [CMU 15-418/Stanford CS149: Parallel Computing](https://csdiy.wiki/%E5%B9%B6%E8%A1%8C%E4%B8%8E%E5%88%86%E5%B8%83%E5%BC%8F%E7%B3%BB%E7%BB%9F/CS149/)
    - [MIT 6.824: Distributed System](https://csdiy.wiki/%E5%B9%B6%E8%A1%8C%E4%B8%8E%E5%88%86%E5%B8%83%E5%BC%8F%E7%B3%BB%E7%BB%9F/MIT6.824/)
  - 计算机系统安全
    collapsed:: true
    - [UCB CS161: Computer Security](https://csdiy.wiki/%E7%B3%BB%E7%BB%9F%E5%AE%89%E5%85%A8/CS161/)
    - [MIT 6.858: Computer System Security](https://csdiy.wiki/%E7%B3%BB%E7%BB%9F%E5%AE%89%E5%85%A8/MIT6.858/)
    - [ASU CSE365: Introduction to Cybersecurity](https://csdiy.wiki/%E7%B3%BB%E7%BB%9F%E5%AE%89%E5%85%A8/CSE365/)
    - [ASU CSE466: Computer Systems Security](https://csdiy.wiki/%E7%B3%BB%E7%BB%9F%E5%AE%89%E5%85%A8/CSE466/)
  - 计算机网络
    - [USTC Computer Networking:A Top-Down Approach](https://csdiy.wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/topdown_ustc/)
    - [Computer Networking: A Top-Down Approach](https://csdiy.wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/topdown/) #umass/453_computer_networking
      - * 所属大学：马萨诸塞大学
      - * 先修要求：有一定的计算机系统基础
      - * 编程语言：无
      - * 课程难度：🌟🌟🌟
      - * 预计学时：40 小时
      - 《自顶向下方法》是计算机网络领域的一本经典教材，两位作者 Jim Kurose 和 Keith Ross 精心制作了教材配套的课程网站，并且公开了自己录制的网课视频，交互式的在线章节测试，以及利用 WireShark 进行抓包分析的 lab。唯一遗憾的是这门课并没有硬核的编程作业，而 Stanford 的 [CS144](../CS144/) 能很好地弥补这一点。
      - ## 课程资源
        - 课程网站：[https://gaia.cs.umass.edu/kurose_ross/index.php](https://gaia.cs.umass.edu/kurose_ross/index.php)
        - 课程视频：[https://gaia.cs.umass.edu/kurose_ross/lectures.php](https://gaia.cs.umass.edu/kurose_ross/lectures.php)
        - 课程教材：Computer Networking: A Top-Down Approach
        - 课程作业：[https://gaia.cs.umass.edu/kurose_ross/wireshark.php](https://gaia.cs.umass.edu/kurose_ross/wireshark.php)
      - ## 资源汇总
        - @PKUFlyingPig 在学习这门课中用到的所有资源和作业实现都汇总在 [PKUFlyingPig/Computer-Network-A-Top-Down-Approach - GitHub](https://github.com/PKUFlyingPig/Computer-Network-A-Top-Down-Approach) 中。
    - [Stanford CS144: Computer Network](https://csdiy.wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/CS144/)
  - 数据库系统
    - [UCB CS186: Introduction to Database System](https://csdiy.wiki/%E6%95%B0%E6%8D%AE%E5%BA%93%E7%B3%BB%E7%BB%9F/CS186/)
    - [CMU 15-445: Database Systems](https://csdiy.wiki/%E6%95%B0%E6%8D%AE%E5%BA%93%E7%B3%BB%E7%BB%9F/15445/) #cmu/15-445_database_systems
      collapsed:: true
      - * 所属大学：CMU
      - * 先修要求：C++，数据结构与算法
      - * 编程语言：C++
      - * 课程难度：🌟🌟🌟🌟
      - * 预计学时：100 小时
      - 作为 CMU 数据库的入门课，这门课由数据库领域的大牛 Andy Pavlo 讲授（“这个世界上我只在乎两件事，一是我的老婆，二就是数据库”）。15-445 会自底向上地教你数据库系统的基本组成部分：存储、索引、查询，以及并发事务控制。 这门课的亮点在于 CMU db 专门为此课开发了一个教学用的关系型数据库 [bustub](https://github.com/cmu-db/bustub)，并要求你对这个数据库的组成部分进行修改，实现上述部件的功能。此外 bustub 作为一个 C++ 编写的中小型项目涵盖了程序构建、代码规范、单元测试等众多要求，可以作为一个优秀的开源项目学习。
      - ## 课程资源
        - 在 Fall2019 中，第二个 Project 是做哈希索引，第四个 Project 是做日志与恢复。
        - 在 Fall2020 中，第二个 Project 是做 B 树，第四个 Project 是做并发控制。
        - 在 Fall2021 中，第一个 Project 是做缓存池管理，第二个 Project 是做哈希索引，第四个 Project 是做并发控制。
        - 在 Fall2022 中，与 Fall2021 相比只有哈希索引换成了 B+ 树索引，其余都一样。
        - 如果大家有精力的话可以都去尝试一下，或者在对书中内容理解不是很透彻的时候，尝试用代码写一个会加深你的理解。
      - ## 资源汇总
        - 课程网站：[Fall2019](https://15445.courses.cs.cmu.edu/fall2019/schedule.html), [Fall2020](https://15445.courses.cs.cmu.edu/fall2020/schedule.html), [Fall2021](https://15445.courses.cs.cmu.edu/fall2021/schedule.html), [Fall2022](https://15445.courses.cs.cmu.edu/fall2022/schedule.html)
        - 课程视频：课程网站免费观看
        - 课程教材：Database System Concepts
        - 课程作业：4 个 Project
        - @ysj1173886760 在学习这门课中用到的所有资源和作业实现都汇总在 [ysj1173886760/Learning: db - GitHub](https://github.com/ysj1173886760/Learning/tree/master/db) 中。
        - 由于 Andy 的要求，仓库中没有 Project 的实现，只有 Homework 的 Solution。特别的，对于 Homework1，@ysj1173886760 还写了一个 Shell 脚本来帮大家执行自动判分。
        - 另外在课程结束后，推荐阅读一篇论文 [Architecture Of a Database System](https://github.com/ysj1173886760/paper%5Fnotes/tree/master/db)，对应的中文版也在上述仓库中。论文里综述了数据库系统的整体架构，让大家可以对数据库有一个更加全面的视野。
      - ## 后续课程
        - [CMU15-721](https://15721.courses.cs.cmu.edu/spring2020/) 主要讲主存数据库有关的内容，每节课都有对应的 paper 要读，推荐给希望进阶数据库的小伙伴。@ysj1173886760 目前也在跟进这门课，完成后会在这里提 PR 以提供进阶的指导。
    - [Caltech CS122: Database System Implementation](https://csdiy.wiki/%E6%95%B0%E6%8D%AE%E5%BA%93%E7%B3%BB%E7%BB%9F/CS122/)
    - [Stanford CS346: Database System Implementation](https://csdiy.wiki/%E6%95%B0%E6%8D%AE%E5%BA%93%E7%B3%BB%E7%BB%9F/CS346/)
    - [CMU 15-799: Special Topics in Database Systems](https://csdiy.wiki/%E6%95%B0%E6%8D%AE%E5%BA%93%E7%B3%BB%E7%BB%9F/15799/)
  - 编译原理
    collapsed:: true
    - [Stanford CS143: Compilers](https://csdiy.wiki/%E7%BC%96%E8%AF%91%E5%8E%9F%E7%90%86/CS143/)
  - 计算机图形学
    collapsed:: true
    - [GAMES101](https://csdiy.wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E5%9B%BE%E5%BD%A2%E5%AD%A6/GAMES101/)
    - [GAMES202](https://csdiy.wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E5%9B%BE%E5%BD%A2%E5%AD%A6/GAMES202/)
    - [GAMES103](https://csdiy.wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E5%9B%BE%E5%BD%A2%E5%AD%A6/GAMES103/)
    - [Stanford CS148](https://csdiy.wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E5%9B%BE%E5%BD%A2%E5%AD%A6/CS148/)
    - [CMU 15-462](https://csdiy.wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E5%9B%BE%E5%BD%A2%E5%AD%A6/15462/)
  - Web开发
    collapsed:: true
    - [MIT web development course](https://csdiy.wiki/Web%E5%BC%80%E5%8F%91/mitweb/)
    - [Stanford CS142: Web Applications](https://csdiy.wiki/Web%E5%BC%80%E5%8F%91/CS142/)
    - [University of Helsinki: Full Stack open 2022](https://csdiy.wiki/Web%E5%BC%80%E5%8F%91/fullstackopen/)
  - 数据科学
    collapsed:: true
    - [UCB Data100: Principles and Techniques of Data Science](https://csdiy.wiki/%E6%95%B0%E6%8D%AE%E7%A7%91%E5%AD%A6/Data100/)
  - 人工智能
    collapsed:: true
    - [Harvard CS50's Introduction to AI with Python](https://csdiy.wiki/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD/CS50/)
    - [UCB CS188: Introduction to Artificial Intelligence](https://csdiy.wiki/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD/CS188/)
  - 机器学习
    collapsed:: true
    - [Coursera: Machine Learning](https://csdiy.wiki/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/ML/)
    - [Stanford CS229: Machine Learning](https://csdiy.wiki/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/CS229/)
    - [UCB CS189: Introduction to Machine Learning](https://csdiy.wiki/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/CS189/)
  - 机器学习系统
    collapsed:: true
    - [智能计算系统](https://csdiy.wiki/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E7%B3%BB%E7%BB%9F/AICS/)
    - [CMU 10-414/714: Deep Learning Systems](https://csdiy.wiki/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E7%B3%BB%E7%BB%9F/CMU10-414/)
    - [Machine Learning Compilation](https://csdiy.wiki/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E7%B3%BB%E7%BB%9F/MLC/)
  - 深度学习
    collapsed:: true
    - [Coursera: Deep Learning](https://csdiy.wiki/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/CS230/)
    - [国立台湾大学：李宏毅机器学习](https://csdiy.wiki/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/LHY/)
    - [Stanford CS231n: CNN for Visual Recognition](https://csdiy.wiki/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/CS231/)
    - [Stanford CS224n: Natural Language Processing](https://csdiy.wiki/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/CS224n/)
    - [Stanford CS224w: Machine Learning with Graphs](https://csdiy.wiki/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/CS224w/)
    - [UCB CS285: Deep Reinforcement Learning](https://csdiy.wiki/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/CS285/)
  - 机器学习进阶
    collapsed:: true
    - [进阶路线图](https://csdiy.wiki/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E8%BF%9B%E9%98%B6/roadmap/)
    - [CMU 10-708: Probabilistic Graphical Models](https://csdiy.wiki/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E8%BF%9B%E9%98%B6/CMU10-708/)
    - [Columbia STAT 8201: Deep Generative Models](https://csdiy.wiki/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E8%BF%9B%E9%98%B6/STAT8201/)
    - [U Toronto STA 4273 Winter 2021: Minimizing Expectations](https://csdiy.wiki/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E8%BF%9B%E9%98%B6/STA4273/)
    - [Stanford STATS214 / CS229M: Machine Learning Theory](https://csdiy.wiki/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E8%BF%9B%E9%98%B6/CS229M/)
  - [后记](https://csdiy.wiki/%E5%90%8E%E8%AE%B0/)
-