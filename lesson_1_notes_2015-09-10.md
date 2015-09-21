# Git

### (Mostly) Git Commands

`git init` - tell Git we want this folder under VCS; Git ignores empty folders

`git status` - status of the current repository

```bash
git config --global user.email 'b1katka@gmail.com'
git config --global user.name 'Katarína Baxová'
```

`vi ~/.gitconfig` - here is my global Git configuration file

`git add <file>`

**git add + tab** - suggests files changed after the last commit

`git status --short`
- `A_`  - added
- `_M` - modified unstaged
- `M_` - modified staged (added)
- `_D` - deleted (with `rm` not `git rm`)
- `D_` - deleted properly (with `git rm`)
- `R_` - renamed
- `??` - unknown (not under VCS)

`git commit` - opens message editor, write a message:
- what and how do I change/add...
- `ctrl+o` save
- `ctrl+x` close

```bash
git remote add origin https://github.com/lucyb1/first-repository.git
```

connect file in my PC with the thing in github on the internet, call it there *origin* - they are peers, but I will pretend *origin* is superior

`git push origin master --set-upstream` - push changes to remote thing (node) and from now on remember to push it there

### Other Notes
**VCS** - version control system
  (other: svn, mercury,...)

**ssh** - encrypted connection (secure shell)

**daemon** - process running in the background, for example Dropbox, Linux Update; Git does not have a daemon, it needs *to be told exactly*

try to use *the long options*, better `--help` than `-h`, you are then absolutely sure what command will be executed

**commit**
- fixed point in time (development process)
- is a *LOCAL* operation

`alt+tab` - window switching

`ctrl+s` - save (in most environments)

**untracked file** - file not added to the VCS
- must be added before commit
- no other option, commit ignores it/does not see it
- commit ignores anything you don't tell him *not* to ignore = anything you did not explicitly add (`git add`)

searching in *man pages*: `/`*thing_to_search*; `n` - jump to **n**ext result

`ctrl+r` - reload browser page
