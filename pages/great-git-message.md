also:: Git 提交规范
icon:: 📝
created:: [[20240810]]
status:: writing/draft
tags:: #git

- ```shell
  feat: add hat wobble
  ^--^  ^------------^
  |     |
  |     +-> Summary in present tense.
  |
  +-------> Type: chore, docs, feat, fix, refactor, style, or test.
  ```
  - `feat`
    - 添加新特性、新功能（ feature ）
  - `fix`
    - 修复 bug
  - `docs`
    - 仅仅修改了文档
  - `style`
    - 仅仅修改了空格、格式缩进、逗号等等，不改变代码逻辑
  - `refactor`
    - 代码重构，没有加新功能或者修复 bug
  - `perf`
    - 性能测试
  - `test`
    - 测试用例
  - `chore`
    - 改变构建流程、或者增加依赖库、工具等
- ## ↩ Reference
  - https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716
  - https://www.conventionalcommits.org/
  - https://seesparkbox.com/foundry/semantic_commit_messages
  - http://karma-runner.github.io/1.0/dev/git-commit-msg.html
-