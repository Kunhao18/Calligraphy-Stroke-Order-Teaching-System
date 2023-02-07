# -*- coding: utf-8 -*-

from torch import device, load
from sys import exit, argv
from PyQt5.QtWidgets import QApplication

import demo_windows
from models import Classifier

import warnings
warnings.filterwarnings("ignore")


if __name__ == '__main__':
    # 构建模型
    now_device = device("cpu")
    model = Classifier(now_device)
    model.load_state_dict(load(model.save_path))

    # 构建并启动窗口
    app = QApplication(argv)
    MainWindow = demo_windows.Demo_Widget(model)
    MainWindow.show()
    exit(app.exec_())
