icon:: 🛠
created:: [[20230728]]
document:: 
status:: tool/star
tags:: 
type:: tool

- ## Why
  - 版本管理
- ## How
  - Config
    - ```shell
      # sense with low-
      Git 大小写不敏感
      `git mv`
      `git config core.ignorecase false`
      windows 大小写
      https://juejin.cn/post/7135422871735631902
      总是显示另一个分支的文件没有提交，会被强制覆盖，让我提交，但是又检测不到，什么也提交不了，根本合并不了；
      `*Untracked Files Prevent Checkout* Move or commit them before checkout`
      https://www.xttblog.com/?p=5294
      甚至用 jetbrains 都切换不了分支，分支都是用命令行切换的；
      还是不清楚问题出在了哪里？
      ```
  - Init
    - ```shell
      git init
      ```
  - Clone
    - ```shell
      git clone ssh://user@domain.com/repo.git
      ```
  - Status
    - ```shell
      git status
      git diff # Changes to tracked files
      ```
  - Add
    - ```shell
      git add .
      git commit
      ```
  - History
    - ```shell
      git log
      git log --oneline
      git blame <file>
      ```
  - Push & Pull
    - ```shell
      git pull <remote> <branch>
      git push <remote> <branch>
      
      git remote -v # List all currently configured remotes
      git remote show <remote> # Show information about a remote
      git remote add <shortname> <url> # Add new remote repository, named <remote>
        # git submodule add <url>/<ssh>
      git fetch <remote> # Download all changes from <remote>
      
      git branch -dr <remote/branch> # Delete a branch on the remote
      git push --tags # Publish your tags
      ```
    - `git fetch` + `git merge` == `git pull` via https://www.jianshu.com/p/a5c4d2f99807
      collapsed:: true
      - ![](https://raw.githack.com/bGZo/assets/dev/2024/image_1645371143990_0-or8.png)
      - ```bash
        git fetch origin master
        git log -p master..origin/master
        git merge origin/master
        git fetch origin master:tmp
        git diff tmp
        git merge tmp
        # via: https://blog.csdn.net/hudashi/article/details/7664457
        ```
  - Rollback
    - add
      collapsed:: true
      - #+BEGIN_WARNING
        不要用 `git reset --hard (versionＨash)`, 修改会清空!
        #+END_WARNING
      - ```shell
        git reset --mixed
        # 保留修改, 退出暂存区, --mixed 为默认参数
        git reset HEAD
        # 撤销 add (绿字变红字)
        git checkout -- (file)
        # 撤销没 add 的修改 (红字变无)
        ```
    - commit
      collapsed:: true
      - ```shell
        git reset --soft HEAD^
        # 不删除工作空间改动代码, 撤销 commit, 不撤销 git add
        git commit --amend
        # commit 注释写错了, 只想改一下注释
        ```
        - `--hard`
          - 删除工作空间改动代码，撤销 `commit`，撤销 `git add .`
          - 注意完成这个操作后，就恢复到了上一次的commit状态
    - all things
      collapsed:: true
      - `git reflog`
    - references
      collapsed:: true
      - `revert` vs `checkout` vs `reset`, via: [atlassian](https://www.atlassian.com/git/tutorials/resetting-checking-out-and-reverting)
        collapsed:: true
        - `revert` -> `commit level`, no `file level`
          - __safe operation__ for 'public undos' as it creates new history which can be shared remotely and doesn't overwrite history remote team members may be dependent on.
        - `checkout` -> `commit level` & `file level`
          - A checkout is an operation that moves the HEAD ref pointer to a specified commit
        - `reset`
          - A reset is an operation that __takes a specified commit and resets the "three trees" to match the state of the repository at that specified commit__.
            - `three trees` -> `working directory` & `stagged snapshot` & `commit History`
            - `three different modes`??
          - `checkout` and `reset` are generally used for making local or private 'undos'. They modify the history of a repository that can cause conflicts when pushing to remote shared repositories.
      - ```bash
        git reset --hard HEAD
        git checkout HEAD <file> # Discard local changes in a specific file
        git revert <commit> # Revert a commit   (by producing a new commit with contrary changes)
        git reset --hard <commit> # Reset your HEAD pointer to a previous commit …and discard all changes since then
        git reset <commit> # and preserve all changes as unstaged changes
        git reset --keep <commit> # and preserve uncommitted local changes
        ```
  - Merge
    - [[jetbrains]] gui tools
    - ```bash
      git merge <branch>
      git rebase <branch>
      git rebase --abort
      git rebase --continue
      git mergetool
      git add <resolved-file>
      git rm <resolved-file>
      ```
    - `rebase` check https://juejin.cn/post/7038093620628422669
  - Merge force from `dev` branch
    - `git reset --hard dev/1197`
    - via: https://stackoverflow.com/a/59238409
  - Sub Modules
    - ```shell
      git submodule add https://github.com/yyy/xxx.git
      git submodule status
      git submodule deinit
      git clone https://github.com/yyy/xxx.git --recursive #子模块也一起 clone, or using for
      git submodule init && git submodule update # euqal following
      git submodule update --init
      git submodule update --init --recursive # 递归添加
      ```
    - via: https://knightyun.github.io/2021/03/21/git-submodule
  - Brach
    - ```shell
      git branch -av
      git checkout <branch> # Switch HEAD branch
      git branch <new-branch> # Create a new branch based
      git checkout --track <remote/branch> #Create a new tracking branch based on a remote branch
      git branch -d <branch> # Delete a local branch
      ```
  - Tag
    - ```shell
      git tag <tag-name>
      ```
    - `tag`: 每一个正式发布的版本merge到master 并且打一个tag
- ## What
  - Let your contributions graph running: {{gh liangzr/github-run}}
  - A tool for drawing a heat-map of Github contributions on HTML Canvas  {{gh sallar/github-contributions-canvas}}
  - Emojis supported by Github [^github-emoji-refer]
    collapsed:: true
    - | Commit type | Emoji |
      |---|---|
      | Initial commit | 🎉 `:tada:` |
      | Version tag | 🔖 `:bookmark:` |
      | New feature | ✨ `:sparkles:` |
      | Bugfix | 🐛 `:bug:` |
      | Metadata | 📇 `:card_index:` |
      | Documentation | 📚 `:books:` |
      | Documenting source code | 💡 `:bulb:` |
      | Performance | 🐎 `:racehorse:` |
      | Cosmetic | 💄 `:lipstick:` |
      | Tests | 🚨 `:rotating_light:` |
      | Adding a test | ✅ `:white_check_mark:` |
      | Make a test pass | ✔️ `:heavy_check_mark:` |
      | General update | ⚡ `:zap:` |
      | Improve format/structure | 🎨 `:art:` |
      | Refactor code | 🔨 `:hammer:` |
      | Removing code/files | 🔥 `:fire:` |
      | Continuous Integration | 💚 `:green_heart:` |
      | Security | 🔒 `:lock:` |
      | Upgrading dependencies | ⬆️ `:arrow_up:` |
      | Downgrading dependencies | ⬇️ `:arrow_down:` |
      | Lint | 👕 `:shirt:` |
      | Translation | 👽 `:alien:` |
      | Text | 📝 `:pencil:` |
      | Critical hotfix | 🚑 `:ambulance:` |
      | Deploying stuff | 🚀 `:rocket:` |
      | Fixing on MacOS | 🍎 `:apple:` |
      | Fixing on Linux | 🐧 `:penguin:` |
      | Fixing on Windows | 🏁 `:checkered_flag:` |
      | Work in progress | 🚧 `:construction:` |
      | Adding CI build system | 👷 `:construction_worker:` |
      | Analytics or tracking code | 📈 `:chart_with_upwards_trend:` |
      | Removing a dependency | ➖ `:heavy_minus_sign:` |
      | Adding a dependency | ➕ `:heavy_plus_sign:` |
      | Docker | 🐳 `:whale:` |
      | Configuration files | 🔧 `:wrench:` |
      | Package.json in JS | 📦 `:package:` |
      | Merging branches | 🔀 `:twisted_rightwards_arrows:` |
      | Bad code / need improv. | 💩 `:hankey:` |
      | Reverting changes | ⏪ `:rewind:` |
      | Breaking changes | 💥 `:boom:` |
      | Code review changes | 👌 `:ok_hand:` |
      | Accessibility | ♿ `:wheelchair:` |
      | Move/rename repository | 🚚 `:truck:` |
      | Other | [Be creative](http://www.emoji-cheat-sheet.com/) |
- ## ↩ Reference
  - [^github-emoji-refer]: gist from https://gist.github.com/parmentf/035de27d6ed1dce0b36a, Inspired by [dannyfritz/commit-message-emoji](https://github.com/dannyfritz/commit-message-emoji) See also [gitmoji](https://gitmoji.carloscuesta.me/).
  - ![git-cheatsheet.pdf](../../soul/assets/git-cheatsheet_1645371794288_0.pdf)
  - https://www.v2ex.com/t/828792
  - [撤销git add - SegmentFault 思否](https://segmentfault.com/q/1010000006864939)
  - https://learnxinyminutes.com/docs/zh-cn/git-cn/
  - https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control
  - [git使用情景2：commit之后，想撤销commit_天空还是那么蓝的博客-CSDN博客_git 撤回commit](https://blog.csdn.net/w958796636/article/details/53611133)
-
-