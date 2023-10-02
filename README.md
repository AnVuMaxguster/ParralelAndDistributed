# ParralelAndDistributed
Giải thuật xử lý song song và phân bố - NT538.O11.MMCL

* RULES:
  1) Mỗi người chia **1 branch làm việc của mình** ( tên tùy thích ), code chính thức được **merge** vào **branch main**. 
  2) Commit code theo structure như sau:
     |- **Lecture n** ( folder )
           |- **Tên bài toán** ( folder )
                  |- ( code files )
  3) ...
     
* GIT BASH COMMANDS:
  ( Ae có thể note đóng góp vào đây các cmd Git Bash thông dụng để tiện ghi nhớ, edit thẳng vào Readme này của **branch main** )


-BAO
Clone from an existing repo with:    git clone “repo url”

git remote add origin https://github.com/....	- use to link local folder to a remote repo

Status:
git status - check files status locally

Commit:
Cd to the local folder need to be commited
Git Add .
Git Commit -m “{your message}”
Git push

Pull data from repo:
Git pull


Branch:
Git fetch	- up-to-date with remote repo
Git checkout -b {local branch name }     -  only -b if local branch has not been created, use to change to/create a new local branch

Git branch --set-upstream-to=origin/{repoBranchName} {localbranch name}  - use to connect local branch to track repo branch

