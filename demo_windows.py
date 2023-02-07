# -*- coding: utf-8 -*-

import cv2
import os
import numpy as np
from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtGui import QImage, QPixmap, QMovie

import torch
import torchvision.transforms as transforms

import ui_mainwindow
from time import time
from tqdm import tqdm


class Demo_Widget(QWidget):
    def __init__(self, model):
        super().__init__()
        self.ui = ui_mainwindow.Ui_Form()
        self.ui.setupUi(self)
        self.ui.now_img.setScaledContents(True)
        self.ui.gen_img.setScaledContents(True)

        self.ui.up_button.clicked.connect(self.upload_img)
        self.model = model
        self.labels_vec, self.label_dict = self.load_label_vecs()

    def load_label_vecs(self):
        """
        读取数据库图片并计算编码
        """
        label_vecs = []
        label_dict = []
        transform1 = transforms.Compose([transforms.ToTensor()])
        for root, dirs, files in os.walk('dataset/labels'):
            cnt = 0
            tmp_batch = None
            for file in tqdm(files):
                char_name = file.split('.')[0]
                label_dict.append(char_name)
                file_name = os.path.join(root, file)
                label_img = cv2.imdecode(np.fromfile(file_name, dtype=np.uint8), -1)
                label_img = cv2.resize(label_img, (64, 64), interpolation=cv2.INTER_AREA)
                label_img = transform1(label_img)
                label_img = label_img.unsqueeze(0)
                if cnt == 0:
                    tmp_batch = label_img
                else:
                    tmp_batch = torch.cat((tmp_batch, label_img), dim=0)
                cnt += 1
                if cnt % 128 == 0:
                    with torch.no_grad():
                        out = self.model.get_encode(tmp_batch)
                        label_vecs.append(out)
                    cnt = 0
            if cnt > 0:
                with torch.no_grad():
                    out = self.model.get_encode(tmp_batch)
                    label_vecs.append(out)
        return label_vecs, label_dict

    def upload_img(self):
        """
        上传图片
        """
        path = QFileDialog.getOpenFileName(self, "Open　Image", ".", "Image　Files(*.jpg　*.png)")
        if path[0] == '':
            return

        # 文字识别，计算用时
        begin_time = time()
        self.img_classify(path[0])
        end_time = time()
        run_time = end_time - begin_time
        print('用时', run_time)

    def img_classify(self, path):
        """
        文字识别
        """
        self.model.eval()
        max_char = None
        max_result = -1

        # 读入图片
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (64, 64), interpolation=cv2.INTER_AREA)

        # 展示当前图片
        display = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width, depth = display.shape
        display = QImage(display, width, height, width * depth, QImage.Format_RGB888)
        self.ui.now_img.setPixmap(QPixmap.fromImage(display))

        # 获取当前图片编码
        transform1 = transforms.Compose([transforms.ToTensor()])
        img = transform1(img)
        test_sample = img.unsqueeze(0)
        with torch.no_grad():
            test_sample = self.model.get_encode(test_sample)

        # 对比识别
        offset = 0
        for vecs in self.labels_vec:
            temp_input = test_sample.repeat(vecs.shape[0], 1)
            with torch.no_grad():
                out = self.model.get_result(temp_input, vecs)
                result = out[:, 1].float()
                idx = np.argmax(result)
                if result[idx] > max_result:
                    max_char = self.label_dict[offset + idx]
                    max_result = result[idx]
                offset += vecs.shape[0]

        # 展示结果
        result_path = 'dataset/src/{}.gif'.format(max_char)
        gif_img = QMovie(result_path)
        self.ui.gen_img.setMovie(gif_img)
        gif_img.start()
