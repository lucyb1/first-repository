# Git

is **VCS** - version control system
  (other: svm, mercury,...)

**ssh** - krptovane pripojenie (secure shell)

**daemon**- proces kt bezi na pozadi, napr Dropbox, linux update

git nema daemona, treba mu "explicitne povedat"

`git init` - povedat gitu ze tento adresar chceme pod version control

snaz sa pouzivat **dlhe options**, lepsie --help ako -h
	lebo si si ista co to urobi

git ignoruje prazdne adresare

`git status` - status of current repozitory

`commit` - fixed point in time (development process)

```bash
git config --global user.email 'b1katka@gmail.com'
git config --global user.name 'Katarina Baxova'
```

`vi ~/.gitconfig` - tu je moj global git configuration file

`alt+tab` - prepinanie okien
`ctrl+s` save (vacsinou)

**untracked file** - subor kt nieje pridany do VCS
- musi byt pridane do VCS pred commitom
- pretoze to inak nejde, commit ho nevidi/ignoruje
- commit ignoruje vsetko co mu nepovies ze nema ignorovat
- co si donho explicitne nepridala (git add)

`git add <file>`

**git add +tab** - navrhuje mi subory zmenene od posledneho commitu

`git status --short`
A  asdf		A = added

`git commit` - otvori sa commit message editor, napisat spravu
- co a ako menim/pridavam/...
- ctrl+o ulozit
- ctrl+x zavriet

toto je *LOKALNE* - commit je lokalna operacia

```bash
git remote add origin https://github.com/lucyb1/first-repository.git
```

prepojim to v mojom pc s vecou v githube na internete, tam to nazvem `origin` -
su rovnocenne, ale hram sa, ze tam je to nadradene

v *man pages* sa vyhladava: `/` co_chcem_vyhladat, `n` na dalsi ony

`git push origin master --set-upstream`  push changes to remote thing (node) and remember to pust it there from now

**ctrl+r** reload browser page

### DU

- precitat o markdown-e/rst a nastudovat ho do buducej hodiny
- precitaj nieco a skus nieco
- optimalne commitni cosi s tym na Github (extra bodiky)
- atom (pycharm with extension) ma markdown
preview, atom ma aj rst
- pozri si to
- ak markdown - CommonMark od J Atwood -a
