tags:: #tools 
public:: true
start:: 20230728
title:: git

- ## Why
- ## How
  - ### Commands References
    collapsed:: true
    - CEEATE
      collapsed:: true
      - ```bash
        git clone ssh://user@domain.com/repo.git
        git init
        ```
    - LOCAL CHANGES
      collapsed:: true
      - ```bash
        git status
        git diff # Changes to tracked files
        git add .
        git add -p <file> # Add some changes in <file> to the next commit
        git commit -a # Commit all local changes in tracked files
        git commit
        git commit --amend # Change the last commit, Don‘t amend published commits
        ```
    - COMMIT HISTORY
      collapsed:: true
      - ```bash
        git log
        git log -p <file> # Show changes over time for a specific file
        git blame <file> # Who changed what and when in <file>
        ```
    - BRANCHES & TAGS
      collapsed:: true
      - ```bash
        git branch -av
        git checkout <branch> # Switch HEAD branch
        git branch <new-branch> # Create a new branch based
        git checkout --track <remote/branch> #Create a new tracking branch based on a remote branch
        git branch -d <branch> # Delete a local branch
        git tag <tag-name>
        ```
      - `tag`: 每一个正式发布的版本merge到master 并且打一个tag
    - UPDATE & PUBLISH
      collapsed:: true
      - ```bash
        git remote -v # List all currently configured remotes
        git remote show <remote> # Show information about a remote  
        git remote add <shortname> <url> # Add new remote repository, named <remote>
          # git submodule add <url>/<ssh>
        git fetch <remote> # Download all changes from <remote>
        git pull <remote> <branch>
        git push <remote> <branch>
        git branch -dr <remote/branch> # Delete a branch on the remote
        git push --tags # Publish your tags
        ```
      - `git fetch` -> why don't integrate into HEAD?
        - `git fetch` + `git merge` == `git pull` via https://www.jianshu.com/p/a5c4d2f99807
        - ![image.png](../assets/image_1645371143990_0.png){:height 188, :width 632}
        - ```bash
          git fetch origin master
          git log -p master..origin/master
          git merge origin/master
          
          git fetch origin master:tmp
          git diff tmp 
          git merge tmp
          # via: https://blog.csdn.net/hudashi/article/details/7664457
          ```
      - ` git submodule add https://github.com/yyy/xxx.git`
        - via: https://knightyun.github.io/2021/03/21/git-submodule
    - MERGE & REBASE
      collapsed:: true
      - ```bash
        git merge <branch>
        git rebase <branch>  
        git rebase --abort
        git rebase --continue
        git mergetool
        git add <resolved-file> 
        git rm <resolved-file>
        ```
      - `rebase` tutorial
    - UNDO
      collapsed:: true
      - ```bash
        git reset --hard HEAD
        git checkout HEAD <file> # Discard local changes in a specific file
        git revert <commit> # Revert a commit   (by producing a new commit with contrary changes)  
        git reset --hard <commit> # Reset your HEAD pointer to a previous commit …and discard all changes since then
        git reset <commit> # and preserve all changes as unstaged changes
        git reset --keep <commit> # and preserve uncommitted local changes  
        ```
      - `revert` vs `checkout` vs `reset`, via: [atlassian](https://www.atlassian.com/git/tutorials/resetting-checking-out-and-reverting)
        - `revert` -> `commit level`, no `file level`
          - __safe operation__ for 'public undos' as it creates new history which can be shared remotely and doesn't overwrite history remote team members may be dependent on.
        - `checkout` -> `commit level` & `file level`
          - A checkout is an operation that moves the HEAD ref pointer to a specified commit
        - `reset`
          - A reset is an operation that __takes a specified commit and resets the "three trees" to match the state of the repository at that specified commit__.
            - `three trees` -> `working directory` & `stagged snapshot` & `commit History`
            - `three different modes`??
          - `checkout` and `reset` are generally used for making local or private 'undos'. They modify the history of a repository that can cause conflicts when pushing to remote shared repositories.
    - Submodule
      collapsed:: true
      - ```shell
        git submodule add https://github.com/yyy/xxx.git
        git submodule status
        git submodule deinit
        
        git clone https://github.com/yyy/xxx.git --recursive #子模块也一起 clone, or using for
        git submodule init && git submodule update # euqal following
        git submodule update --init
        git submodule update --init --recursive # 递归添加
        ```
  - Add -> Commit
    collapsed:: true
    - Add 错了怎么办?
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
    - Commit 错了怎么办?
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
- ## What
  - ![git-cheatsheet.pdf](../assets/git-cheatsheet_1645371794288_0.pdf)
  - Emojis supported by Github
    collapsed:: true
    - gist from https://gist.github.com/parmentf/035de27d6ed1dce0b36a
    - Inspired by [dannyfritz/commit-message-emoji](https://github.com/dannyfritz/commit-message-emoji) See also [gitmoji](https://gitmoji.carloscuesta.me/).
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
  - TODO heat map commit
    collapsed:: true
    - [GitHub - sallar/github-contributions-canvas: A tool for drawing a heat-map of Github contributions on HTML Canvas](https://github.com/sallar/github-contributions-canvas)
  - TODO GitHub 贡献图 模仿
    collapsed:: true
    - [GitHub - liangzr/github-run: Let your contributions graph running](https://github.com/liangzr/github-run)
  - More tutorials
    - https://learnxinyminutes.com/docs/zh-cn/git-cn/
    - https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control
  - Refs
    - [撤销git add - SegmentFault 思否](https://segmentfault.com/q/1010000006864939)
    - [git使用情景2：commit之后，想撤销commit_天空还是那么蓝的博客-CSDN博客_git 撤回commit](https://blog.csdn.net/w958796636/article/details/53611133)
-