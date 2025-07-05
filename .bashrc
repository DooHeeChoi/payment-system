source /usr/share/git-core/contrib/completion/git-prompt.sh
export PS1='\u@\h:\w$(__git_ps1 " (%s)")\$ '
