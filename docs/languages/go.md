## 变量和常量

>cstable
>| var msg string
msg = "Hello" n       ||| 变量声明 |<
>| msg := "Hello"     |<
>| const Phi = 1.618  || 常量可以是 character，string，boolean 或数值。
<cstable

## 数据类型

### 字符串

>cstable
>| for i := 0; i < len(str); i++ {
    fmt.Println(str[i])
} || 遍历字符串的 byte (uinit8) |<
>| for _, s := range str {
    fmt.Println(s)
} || 遍历字符串的 rune (int32) |<
<cstable

### slice

>cstable
>| var s []type                         || 声明一个 slice，但没有分配空间。此时 s 等于 nil |<
>| s := make([]type, length)            ||| 使用 make() 创建 slice，指定了 slice 的 length（capacity 为可选参数）  |<
>| s := make([]type, length, capacity)  |<
>| s := []int{1, 2, 3}                  || 声明一个 slice 并初始化 |<
>| s := arr[:]                          ||| 从数组 arr 初始化 slice |<
>| s := arr[2:4]                        |<
>| s2 := s[2:4]                         || 从 slice s 初始化 slice |<
>| s = append(s, 1)                     || 向 slice s 追加一个元素 |<
>| s = append(s, 1, 2)                  || 向 slice s 追加两个元素 |<
>| s = append(s, []int{1, 2, 3}...)     || 追加一个 slice，slice 需要使用...运算符 |<
>| s = append([]int{1, 2, 3}, s...)     || 向 slice 前面追加元素 |<
>| for _, item := range s {
	fmt.Println(item)
} || 遍历 slice |<
<cstable

### map

>cstable
>| var m map[key_type]value_type       || 声明一个 map，但没有分配空间。此时 m 等于 nil |<
>| m := make(map[key_type]value_type)  || 使用 make() 创建 map  |<
>| m := map[string]int {
    "item1": 1,
    "item2": 2,
}                    || 声明一个map并初始化 |<
>| _, ok := m["key"] || 判断 map 中 key 是否存在，ok 为 true 则 key 存在，为 false 则 key 不存在 |<
>| delete(m, "key")  || 删除 map 中的元素。如果 key 不存在，不操作也不报错 |<
>| for key, value := range m {
    fmt.Println(key, value)
}                    || 遍历 map 中的内容 |<
<cstable