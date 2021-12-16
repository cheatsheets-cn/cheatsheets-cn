???+ cs "数据库"

    >cstable
    >| use DATABASE_NAME || 切换到指定数据库，如不存在则新建 |<
    >| db                || 查看当前数据库 |<
    >| show dbs          || 查看所有数据库 |<
    <cstable

???+ cs "集合"

    >cstable
    >| show collections || 查看所有集合 |<
    <cstable

???+ cs "用户"

    >cstable
    >| use admin
    db.system.users.find().pretty() || 查看所有用户 |<
    >| show users || 查看当前数据库下所有用户 |<
    >| db.createUser({
        user:"USERNAME",
        pwd:"PASSWORD",
        roles:[
            {role:"readWrite", db:"mydb"},
        ]
    }) || 创建用户 |<
    >| db.grantRolesToUser(
        "USERNAME",
        [{role:"readWrite", db:"mydb"}]
    ) || 修改用户权限 |<
    <cstable
