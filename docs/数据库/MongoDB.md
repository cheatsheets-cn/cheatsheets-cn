???+ note "数据库"

    <table class="cs-table">
    <tr><td> use DATABASE_NAME </td><td> 切换到指定数据库，如不存在则新建 </td></tr>
    <tr><td> db                </td><td> 查看当前数据库 </td></tr>
    <tr><td> show dbs          </td><td> 查看所有数据库 </td></tr>
    </table>

???+ note "集合"

    <table class="cs-table">
    <tr><td> show collections </td><td> 查看所有集合 </td></tr>
    </table>

???+ note "用户"

    <table class="cs-table">
    <tr><td> <pre>use admin
    db.system.users.find().pretty()</pre> </td><td> 查看所有用户 </td></tr>
    <tr><td> show users </td><td> 查看当前数据库下所有用户 </td></tr>
    <tr><td> <pre>db.createUser({
        user:"USERNAME",
        pwd:"PASSWORD",
        roles:[
            {role:"readWrite", db:"mydb"},
        ]
    })</pre> </td><td> 创建用户 </td></tr>
    <tr><td> <pre>db.grantRolesToUser(
        "USERNAME",
        [{role:"readWrite", db:"mydb"}]
    )</pre> </td><td> 修改用户权限 </td></tr>
    </table>
