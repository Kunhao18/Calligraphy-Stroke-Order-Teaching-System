# Chinese Calligraphy Stroke Order Teaching System

### 1 Environment Requirement

- pytorch 1.9.0
- torchvision 0.10.0
- pyqt5 5.9.7
- opencv-python 4.5.2.54

### 2 Directory Hierarchy

- dataset/
  - labels/  # label images
  - src/  # gifs for displaying
- model_dict/  # model parameters
- test_sample/  # test samples
- demo_windows.py  # GUI controller code
- main.py  # main script
- models.py  # model code
- ui_mainwindow.py  # GUI layout code

### 2 使用说明

##### 2.1 对联生成

python 环境运行 run-gen.py 即可运行生成demo

##### 2.2 对联评分

python 环境运行 run-score.py 即可运行评分demo

##### 2.3 对联系统服务器

> 由于客户端为 Qt 动态编译实现，需根据错误提示配置动态链接库环境

python 环境运行 run-server.py 即可启动本地服务器，启动成功后打印 “server start”

运行 Qt GUI 可执行文件即可连接服务器使用系统
