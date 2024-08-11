icon:: 💾
author:: 
created:: [[20240810]]
exclude-from-graph-view:: true
source:: https://www.coolapk.com/feed/53858973?shareKey=ZWViYTUyZTM3OTcwNjZhZjQ0YzI~
type:: archives-web

- oneplus11，ColorOS刷OxygenOS失败经验小记 序言：由于类原生的rom采用的内核是不支持加载gki内核模块的lineageOS的msm8550-5.15内核，所以我决定选择使用支持gki内核的oxygenOS 失败阶段是这样的。我首先通过9008模式刷了ColorOS13-A29版，然后通过fastboot enhance工具进入fastbootd模式刷入oxygenod14…501全球版（可视与欧版一致）。结果ocdt无论是刷cph2449还是保持国行原厂（PHB110）的，均可进入系统，扬声器无声音且播放视频时常卡顿（原因不明。属硬件解码不正常？），打电话听筒时是有声的。cph2449基带正常，国行ocdt显示无基带（其实基带相关文件还在，只是不正常工作了）。同样方式刷了oxygenod14…304欧版也是一样。刷机后均进recovery清过数据，且排除abl分区影响。 后经多番尝试，成功刷入工作正常的oxygen 步骤如此。先刷oxygen13欧版(我用的是13.1.0.595)且刷cph2449的ocdt（顺序忘了，但我肯定地认为不重要），然后开机激活进系统确认扬声器正常（这个步骤的必要性不确定）。随即我又尝试了通过OTA(本地更新)的方式刷了oxygenod14…501全球版（可视与欧版一致），进系统后扬声器正常，视频播放正常。进recovery再次清除数据后，激活进系统，扬声器与视频播放仍然正常。 下面时失败过程中获取的有帮助的信息的截图。感谢各机油帮助，以及相关教程和工具的提供者，恕不表名
- 如果发现文中有遗留的细节，我会在评论区补充
- ![](http://image.coolapk.com/feed/2024/0224/19/506153_ce93fc6e_2486_0243_784@1668x2388.jpg.m.jpg)
- ![](http://image.coolapk.com/feed/2024/0224/19/506153_c56db513_2486_025_190@1668x2388.jpg.m.jpg)
- ![](http://image.coolapk.com/feed/2024/0224/19/506153_cf8019c6_2486_0258_953@1668x2388.jpg.m.jpg)
- ![](http://image.coolapk.com/feed/2024/0224/19/506153_25da7488_2486_0263_663@1668x2388.jpg.m.jpg)
- [ ![](http://image.coolapk.com/product_logo/2023/0104/16/0_0199_2739_939@320x320.png.t.jpg) 一加11 ](/product/2980)
  - 更多功能，丰富内容，尽在酷安APP