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
