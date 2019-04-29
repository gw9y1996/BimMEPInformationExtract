# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import os
from 接口测试 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox, QWidget,QDialog

class Ui_mainWindow(QWidget):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(864, 574)
        mainWindow.setStyleSheet("#mainWindow{border-image:url(./school.jpg);}")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        spacerItem4 = QtWidgets.QSpacerItem(10, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem6 = QtWidgets.QSpacerItem(50, 0, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem7)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_3.addWidget(self.widget)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem10 = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem10)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.widget.setStyleSheet("#widget{border-image:url(./back3.jpg);;border-radius:5px}")
        self.lineEdit.setStyleSheet("#lineEdit{border-style:none;border-radius:2px;margin: 10px 2px;background:rgba(255,255,255,.5);color: white;}")
        self.lineEdit_2.setStyleSheet("#lineEdit_2{border-style:none;border-radius:2px;margin: 10px 0px;background:rgba(255,255,255,.5);color: white;}")
        self.pushButton.setStyleSheet("""#pushButton{background-color:#87CEFA;
                                                                    border: none;
                                                                    color: #000000;
                                                                    padding: 10px 24px;
                                                                    text-align: center;
                                                                    text-decoration: none;
                                                                    font-size: 18px;
                                                                    margin: 10px 2px;
                                                                    border-radius:10px;}""")
        self.pushButton_2.setStyleSheet("""#pushButton_2{background-color:#87CEFA;
                                                                            background-position:center; 
                                                                            border: none;
                                                                            color: black;
                                                                            font-size: 14px;
                                                                            padding: 10px 24px;
                                                                            border-radius:10px;}""")
        self.label_3.setStyleSheet("#label_3{color: white;text-align:center;}")
        self.retranslateUi(mainWindow)
        self.pushButton.clicked.connect(self.button1_clieck)
        self.pushButton_2.clicked.connect(self.button2_clieck)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowIcon(QIcon('./1.jpg'))
        mainWindow.setWindowTitle(_translate("mainWindow", "MEP信息提取"))
        self.label_3.setText(_translate("mainWindow", "MEP信息提取系统"))
        self.lineEdit.setText(_translate("mainWindow", "请输入用户密匙"))
        self.lineEdit_2.setText(_translate("mainWindow", "请输入模型ID"))
        self.pushButton.setText(_translate("mainWindow", "开始提取"))
        self.pushButton_2.setText(_translate("mainWindow", "打开目录"))

    def button1_clieck(self):
        if self.lineEdit.text() == "请输入用户密匙" :
            key = "bca8aff0c925e3275f58a9bbbe11e59e"
        else:
            key = self.lineEdit.text()
        if self.lineEdit_2.text() == "请输入模型ID":
            id = '79428850'
        else:
            id = self.lineEdit_2.text()
        # QMessageBox.about(self,"信息","数据处理中！")
        child.show()
        runall(id, key)
        child.close()
        



    def button2_clieck(self):
        mulu = os.path.abspath('.')
        print(mulu)

        os.system('explorer.exe /n' + ',' + mulu)
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("提示")
        Dialog.resize(300, 50)
        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 60, 1, 1))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(28)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "数据处理中，请稍后！"))
        self.label_4.setText(_translate("Dialog", "数据处理中，请稍后！"))
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(MainWindow)
    child = QDialog()
    child_ui = Ui_Dialog()
    child_ui.setupUi(child)
    MainWindow.show()
    sys.exit(app.exec_())
