# Widge.Python.Grpc.ECG

### 环境依赖

> [python](https://www.python.org/downloads/)版本>=3.8, 如果版本过低，案例中的部分用法可能不支持，请根据实际情况选择更新 python 版本或调整代码。依赖管理工具为 pipenv，详细文档请参考[pipenv](https://github.com/pypa/pipenv)

```bash
# 安装命令
pip install pipenv -i https://mirrors.aliyun.com/pypi/simple/
# 检测安装是否成功
pipenv --version
```

> 环境设置

```bash
# 初始化虚拟环境
pipenv --three
# 切换到虚拟环境
pipenv shell
# 安装依赖
pipenv install
# 查看已安装依赖
pipenv graph
# 卸载依赖
pipenv uninstall <package>
# 通过requirements文件安装依赖
pipenv install -r requirements.txt
```

## 项目运行

> 编译 proto

```bash
# MacOS & Linux
bash build.bash
# Windows
./build.ps1
```

编译说明：Linux 环境下请保证`build.bash`文件的换行符格式为 Unix 格式，否则会出现编译失败的情况。

由于目前编译器对 python 模块化支持不够，编译完成后，需要手动调整 import 路径（在`src/packages/grpc/greeter_pb2_grpc.py`文件添加`packages.grpc.`，把`import greeter_pb2 as greeter__pb2`改为的`import packages.grpc.greeter_pb2 as greeter__pb2`）。

> 运行项目

```bash
# 启动服务
python src/main.py

# 客户端测试
python src/client.py
```

## 镜像打包

```bash
docker build --pull --rm -f "Dockerfile" -t <name=grpc.testing>:<version=latest> <workspace=".">
# example: docker build --pull --rm -f "Dockerfile" -t grpc.testing:latest "."
```

## 远程开发

1. 安装 [Visual Studio Code](https://code.visualstudio.com/Download) 编辑器
1. 安装 Remote 插件
    1. [remote-ssh](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)
    1. [remote-ssh-edit](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh-edit)
1. 配置 ssh

```
Host <display_name>
    HostName <ip|doname>
    User <username>
    IdentityFile <pem_path>
```
