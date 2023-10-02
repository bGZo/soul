title:: zsh/prompt

- TODO Have No Idea...
  - ```
    # In bashrc you should write folling:
    # export PS1="%K{red}%n@%m%k%B%F{cyan}%(4~|...|)%3~%F{white}\$#%b%f%k" #{blue}
    # export PS1="\[\033[0;31m\]\342\224\214\342\224\200$([[ $? != 0 ]] && echo "[\[\033[0;31m\]\342\234\227\[\033[0;37m\]]\342\224\200")[\[\033[0;39m\]\u\[\033[01;33m\]@\[\033[01;96m\]\h\[\033[0;31m\]]\342\224\200[\[\033[0;32m\]\w\[\033[0;31m\]]\n\[\033[0;31m\]\342\224\224\342\224\200\342\224\200\342\225\274 \[\033[0m\]\[\e[01;33m\]\$\[\e[0m\]"
    # Initialize command prompt
    export PS1="%n@%m:%~%# "
    # not oh-my-zsh's prompt
    # first: %K{blue}%n@%m%k %B%F{cyan} %(4~|...|)%3~%F{white} %# %b%f%k
    # then : %K{blue}%n@%m%k%B%F{cyan}%(4~|...|)%3~%F{white}%#%b%f%k
    # `man zshmisc`
    # - `%F-%f`: 如果支持，则使用其他前景色开始（停止） 通过终端
    # `％F {red}`
    # - `％K-%k`: 使用其他背景色开始（停止）
    # - `%n`: 用户名
    # - `%m`: 主机名（在第一个句号之前截断）
    # - `%B-%b`: 粗体打印
    # - `36 cyan 46 bg-cyan` 
    # 
    # also in bash is
    # PS1='\[\033[0;31m\]\342\224\214\342\224\200$([[ $? != 0 ]] && echo "[\[\033[0;31m\]\342\234\227\[\033[0;37m\]]\342\224\200")[\[\033[0;39m\]\u\[\033[01;33m\]@\[\033[01;96m\]\h\[\033[0;31m\]]\342\224\200[\[\033[0;32m\]\w\[\033[0;31m\]]\n\[\033[0;31m\]\342\224\224\342\224\200\342\224\200\342\225\274 \[\033[0m\]\[\e[01;33m\]\$\[\e[0m\]'
    # refer: https://github.com/zsh-users/zsh/blob/master/Functions/Misc/colors
    # https://unix.stackexchange.com/questions/32273/16-colors-in-zshell/32304
    # more could see: https://blog.csdn.net/u014218108/article/details/51195582
    ```