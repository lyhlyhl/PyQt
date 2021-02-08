#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2019年5月2日
@author: weike32
@site: https://pyqt5.com ,https://github.com/weike32
@email: 394967319@qq.com
@file: CopyContent
@description: 查阅了很多博客，如果有异，可以联系作者邮箱。本Demo仅作学习参考用，保有后续相关权益。
'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QHBoxLayout
from PyQt5 import QtCore
import numpy as np
import pyqtgraph as pg

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")  #wideget的类名
        Form.resize(640, 470)   #设置widget的大小
        self.graphicsView = pg.PlotWidget(Form)
        self.graphicsView.setGeometry(QtCore.QRect(15, 13, 621, 441))  #画一个长方形方形
        self.graphicsView.setBackground((200,200,200,255))#摸索到了一个设置背景的函数
        #@quesetion:加上这个Qtcore.QRect和不加有什么区别
        #初步理解是Qtcore有一些好处，然后可以让功能变得多一些
        self.graphicsView.setObjectName("graphicsView")
        #一样的设置对象的名字
class MyWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        #下面俩行都是弄一个sina函数
        x = np.linspace(-100, 100, 1000)
        data = np.sin(x) / x
        #画图
        self.graphicsView.plot(x, data, pen=(255, 255, 0, 255))
        #写字
        self.label = pg.TextItem(text="横坐标：{}".format(0))
        self.label2 = pg.TextItem(text="dad")
        self.graphicsView.addItem(self.label)
        #获得鼠标的回调
        self.setMouseTracking(True)
        self.graphicsView.scene().sigMouseMoved.connect(self.onMouseMoved)


    #这个函数很神奇，a的传参是怎么传的，我感觉是一个鼠标一样
    #其他的基本上很简单，就是获得鼠标位置，显示出来
    def onMouseMoved(self, a):
        if self.graphicsView.plotItem.vb.mapSceneToView(a):
            point =self.graphicsView.plotItem.vb.mapSceneToView(a)
            self.label.setHtml("<p style='color:white'>横坐标：{0}</p>".format(point.x()))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())