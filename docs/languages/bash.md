## Bash 执行参数

>cstable
>| -e || 在有错误时退出 |<
>| -n || 读一遍脚本中的命令但不执行，用于检查脚本中的语法错误 |<
>| -v || 一边执行脚本，一边将执行过的脚本命令打印到标准错误输出 |<
>| -x || 提供跟踪执行信息，将执行的每一条命令和结果依次打印出来 |<
<cstable

## 代码片段

>cstable
>| cat FILENAME | while read line
do
    echo "LINE: ${line}"
done || 逐行处理文件 |<
<cstable

## 工具

>cstable
>| seq -w 1 10          || 输出连续等宽数字 |<
>| echo XXX | column -t || 格式化对齐输出 |<
<cstable