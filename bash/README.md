# Favourite tricks for bash

## Showing your git branch in the terminal prompt:
add to `.bashrc`:
```
parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
export PS1="\u@\h \[\033[34m\]\w\[\033[35m\]\$(parse_git_branch)\[\033[00m\] $ "
```

