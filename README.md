<div align="center">
  <h1>Cheatsheets CN</h1>
  
  <i>中文开发者速查表。</i>
  
  <a href="https://cheatsheets-cn.github.io/cheatsheets-cn">https://cheatsheets-cn.github.io/cheatsheets-cn</a>
</div>

## 安装

### 直接安装

安装前请确保你已经安装了 Python3。

进入项目根目录，执行：

```bash
# 安装依赖
pip install --no-cache-dir mkdocs mkdocs-material
cd extensions/cstable/; python setup.py install; cd ../../

# 启动服务
mkdocs serve
```

### 使用 venv 安装

安装前请确保你已经安装了：

- python3
- python3-pip
- python3-venv

进入项目根目录，执行：

```bash
# 初始化并激活虚拟环境
python3 -m venv ./venv
source ./venv/bin/activate

# 安装依赖
pip install --no-cache-dir mkdocs mkdocs-material
cd extensions/cstable/; python setup.py install; cd ../../

# 启动服务
mkdocs serve
```

## FAQ

### 速查表设计的原则是？

- 尽量精简的语言表达。
- 只会收集基础的命令、用法示例，不会涉及深入的原理讲解。

### 哪些工具未来可能会加到速查表中？

开发过程中常见通用的语言、工具等。也欢迎大家提 PR 贡献内容。

判断工具是否常见的一个简单依据：如果这个工具在 [Simple Icons](https://simpleicons.org/) 中可以找到，那么就可以认为它是比较常见的。
