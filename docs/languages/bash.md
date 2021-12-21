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