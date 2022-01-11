## 比较

>cstable
>| git difftool --extcmd vimdiff filename || 指定使用 vimdiff 查看文件改动 |<
<cstable

## Tag

>cstable
>| git tag -l <pattern> || 列出符合 pattern 的 tag。
如果没有提供 pattern，列出所有 tag |<
<cstable

## Stash

>cstable
>| git stash list          || 显示隐藏的工作现场 |<
>| git stash               || 隐藏当前工作现场 |<
>| git stash push FILENAME || 隐藏指定文件 |<
>| git stash pop           || 恢复隐藏的工作现场 |<
<cstable

## Log

>cstable
>| git log                  || 显示提交日志 |<
>| git log --pretty=oneline || 以每次一行显示提交日志 |<
<cstable

## 远程仓库

>cstable
>| git fetch origin pull/PRID/head:本地分支 || 拉取 pr |<
<cstable