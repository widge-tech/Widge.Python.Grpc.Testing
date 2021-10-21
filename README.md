# Widge.Python.Grpc.ECG

### 环境依赖

> 如果没有 pipenv，先安装

```bash
# 安装命令
pip install pipenv -i https://mirrors.aliyun.com/pypi/simple/
```

> 环境设置

```bash

# 初始化虚拟环境
pipenv --three

# 切换到虚拟环境
pipenv shell

# 安装依赖
pipenv install
```

## 项目运行

> 编译 proto

```bash
# MacOS & Linux
bash build.bash
# Windows
./build.ps1
```

由于目前编译器对 python 模块化支持不够，编译完成后，需要手动调整 import 路径（添加`packages.grpc.`前缀）。

> 运行项目

```bash
python src/main.py
```
