# Git

### (Mostly) Git Commands

`git init` - tell Git we want this folder under VCS; Git ignores empty folders

`git status` - status of the current repository

```bash
git config --global user.email 'b1katka@gmail.com'
git config --global user.name 'Katarina Baxova'
```

`vi ~/.gitconfig` - here is my Git configuration file

`git add <file>`

**git add + tab** - suggests files changed after the last commit

`git status --short`
- *A* - added
- *M* - modified
- *D* - deleted
- *R* - renamed
- *?* - unknown

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
  (other: svm, mercury,...)

**ssh** - crypted connection (secure shell)

**daemon** - process running on the background, for example Dropbox, Linux Update; Git does not have a daemon, it needs *to be told exactly*

try to use *the long options*, better `--help` than `-h`, you are then absolutely sure what command will be executed

**commit**
- fixed point in time (development process)
- is a *LOCAL* operation

`alt+tab` - window switching

`ctrl+s` - save (in most environments)

**untracked file** - file not added to the VCS
- must be added before commit
- no other option, commit ignores it/does not see it
- commit ignors anything you don't tell him *not* to ignore = anything you did not explicitly added (`git add`)

searching in *man pages*: `/`*thing_to_search*; `n` - jump to another result

`ctrl+r` - reload browser page
