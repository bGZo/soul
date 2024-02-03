tags:: #Tools

- ## [[Quickref]]
  - [Vim Cheat Sheet & Quick Reference](https://quickref.me/vim)
  - [Awesome Vim list with stars count🌟](https://awesome-repos.ecp.plus/vim.html)
  - [byte-of-vim](https://github.com/swaroopch/byte-of-vim)
    - "A Byte of Vim" is a book which aims to help you to learn how to use the Vim editor (version 7), even if all you know is how to use the computer keyboard
-
- `vi` vs vim vs gedit vs namo
  collapsed:: true
  - 系统都会自带nano和vi这两个最基本的编辑器。
  - Nnno非常適合編輯配置文件，但是如果要進行編程，最好使用Vim或Emacs。 Nano支持突出顯示。但這是非常主觀的。
  - vi是老式的文字处理器，功能已经很齐全。不管好不好用，既然大家这么推崇，肯定有他的好处，我们先学习了肯定不会有坏处。vi使用于文本编辑，但是vim更适用于coding。
  - vim是vim 的升级版, Vim是模態的意思是每個鍵在不同的模式中意味著不同的東西。
    - 多级撤消 : vi里按 u只能撤消上次命令
    - 易用性: 运行于unix,windows ,mac等操作平台
    - 语法加亮: vim可以用不同的颜色来加亮你的代码。
    - 可视化操作: 即vim不仅可以在终端运行，也可以运行于x window、 mac os、 windows。
    - 对vi的完全兼容: 某些情况下，你可以把vim当成vi来使用。
  - Geany 有很好的功能，內置終端窗口非常好。我將它用於大多數編程項目。
  - Gedit 是图形化的编辑程序, 学习成本低, 簡單輕巧，但你必須安裝一堆插件才能趕上Geany的普通內置功能，比如代碼折疊等。而Geany插件將為您提供額外的功能，如版本控製集成，可選和non-intrusive項目管理，在功能定義和聲明等之間跳轉。而Geany中可用的可配置鍵綁定允許您幾乎完全按照自己的喜好進行設置 – 盡管默認值也很不錯。 Gedit可以捆綁Python解釋器，但是Geany捆綁了整個虛擬終端。
  - Emacs 具有語法突出顯示並支持擴展, 並且可以通過其嵌入的Lisp(elisp)方言進行擴展。它還具有許多統計程序的模式，支持tex，日曆，郵件閱讀實用程序，俄羅斯方塊甚至精神科醫生。 Emacs(或Vim，但對於統計數據不太好)值得學習，因為它們都是跨平台的，並且支持世界上幾乎所有的編程語言。
- Refs
  - [简明 VIM 练级攻略](https://coolshell.cn/articles/5426.html)
  - [GVIM配置](https://www.jianshu.com/p/6bb4e8491132)
  - [vim插入模式快捷键_目标码神的博客-CSDN博客_vim 插入模式快捷键](https://blog.csdn.net/HappyCodeFly/article/details/86684827)
  - [apt - How do I install vim-gnome on Ubuntu 19.10? - Ask Ubuntu](https://askubuntu.com/questions/1208159/how-do-i-install-vim-gnome-on-ubuntu-19-10)
  - [vi和vim的区别-阿里云开发者社区](https://developer.aliyun.com/article/309383)
  - [Ubuntu中的文本編輯器之間的比較：Vim vs. Emacs vs. Nano - Ubuntu問答](https://ubuntuqa.com/zh-tw/article/1230.html)
  - [在 VIM 下写 C++ 能有多爽？](https://harttle.land/2015/07/18/vim-cpp.html)
  - [妈呀，终于搞定VIM的复制粘贴问题了！_Dartagnan的博客-CSDN博客](https://blog.csdn.net/dadoneo/article/details/6003415)
  - [vim中的复制粘贴问题_asin929的博客-CSDN博客](https://blog.csdn.net/u012948976/article/details/50493431)
    > vim中默认有多个寄存器(粘贴板)，其中使用命令y和p是将内容复制粘贴到vim内部剪切板中，即意味着不能用到其他程序中。但是 `“*` 和 `“+` 这两个寄存器与系统相通, 可以将vim中的内容复制到其他程序中.