# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(648, 365)
        self.up_button = QtWidgets.QPushButton(Form)
        self.up_button.setGeometry(QtCore.QRect(90, 290, 121, 51))
        self.up_button.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.up_button.setObjectName("up_button")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 20, 251, 251))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.now_img = QtWidgets.QLabel(self.frame)
        self.now_img.setGeometry(QtCore.QRect(0, 0, 251, 251))
        self.now_img.setText("")
        self.now_img.setObjectName("now_img")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(300, 20, 321, 321))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.gen_img = QtWidgets.QLabel(self.frame_2)
        self.gen_img.setGeometry(QtCore.QRect(0, 0, 321, 321))
        self.gen_img.setText("")
        self.gen_img.setObjectName("gen_img")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Lab3"))
        self.up_button.setText(_translate("Form", "Upload"))
