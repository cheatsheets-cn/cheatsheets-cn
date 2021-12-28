>cstable
>| docker tag IMAGE_ID REPOSITORY:TAG            || 重命名镜像名称和 tag |<
>| docker stats                                  || 实时显示容器资源使用状况 |<
>| docker stats $(docker ps --format={{.Names}}) || 实时显示容器资源使用状况（显示容器名） |<
<cstable