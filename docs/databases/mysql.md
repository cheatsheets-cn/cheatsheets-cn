## 数据库

>cstable
>| SHOW DATABASES;        || 显示所有数据库 |<
>| DROP DATABASE db_name; || 删除指定数据库 |<
<cstable

## 索引

>cstable
>| SHOW INDEX FROM table_name; || 查看指定表的索引 |<
<cstable

## SELECT

>cstable
>| SELECT DISTINCT column_name FROM table_name; || 从表中查询指定列去重结果 |<
<cstable

## 日期

>cstable
>| SELECT DATEDIFF('1997-12-31 23:59:59', '1997-12-30'); | 两个时间相减，返回天数 |
>| SELECT NOW(); | 返回当前日期、时间 |<
>| SELECT CURRENT_TIMESTAMP; | 返回当前日期、时间 |<
>| SELECT CURRENT_TIMESTAMP(); | 返回当前日期、时间 |<
>| SELECT CURDATE(); | 返回当前日期 |<
>| SELECT DATE_ADD(NOW(), INTERVAL 1 DAY); | 日期加 1 天 |<
<cstable