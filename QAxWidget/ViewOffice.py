#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2017年4月6日
@author: Irony."[讽刺]
@site: https://pyqt5.com , https://github.com/892768447
@email: 892768447@qq.com
@file: ViewOffice
@description: 
'''
from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog,\
    QMessageBox


__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2017 Irony.\"[讽刺]"
__Version__ = "Version 1.0"


class AxWidget(QWidget):

    #基本上是主界面的几个布置的函数就不详细注解了
    def __init__(self, *args, **kwargs):
        super(AxWidget, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        layout = QVBoxLayout(self)
        self.axWidget = QAxWidget(self)
        layout.addWidget(self.axWidget)
        layout.addWidget(QPushButton('选择excel,word,pdf文件',
                                   self, clicked=self.onOpenFile)) #这个clicked是一个回调吗?        QPushButton()
    def onOpenFile(self):
        #这个很关键，学习了QT如何打开文件
        path, _ = QFileDialog.getOpenFileName(
            self, '请选择文件', '', 'excel(*.xlsx *.xls);;word(*.docx *.doc);;pdf(*.pdf);;file(*)')
        #分别是俩个按钮的显示，以及过滤器
        #下面就是进行判断，然后选择执行哪个函数，打开哪个软件
        if not path:
            return
        if _.find('*.doc'):
            return self.openOffice(path, 'Word.Application')
        if _.find('*.xls'):
            return self.openOffice(path, 'Excel.Application')
        if _.find('*.pdf'):
            return self.openPdf(path)

    def openOffice(self, path, app):
        self.axWidget.clear()#需要清除，不然会进程一直在
        if not self.axWidget.setControl(app):
            return QMessageBox.critical(self, '错误', '没有安装  %s' % app)

        #下面这几行都不太能看懂是在干什么，我裂开
        self.axWidget.dynamicCall(
            'SetVisible (bool Visible)', 'false')  # 不显示窗体
        self.axWidget.setProperty('DisplayAlerts', False)
        self.axWidget.setControl(path)

    def openPdf(self, path):
        self.axWidget.clear()
        if not self.axWidget.setControl('Adobe PDF Reader'):
            return QMessageBox.critical(self, '错误', '没有安装 Adobe PDF Reader')
        self.axWidget.dynamicCall('LoadFile(const QString&)', path)


    #这个应该是一个父类函数，直接会关闭窗口时，回调到这里
    #先是重写，关闭了一些东西，然后重写执行了一下父类的closeEvent函数
    def closeEvent(self, event):
        self.axWidget.close()
        self.axWidget.clear()
        self.layout().removeWidget(self.axWidget)
        del self.axWidget
        super(AxWidget, self).closeEvent(event)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = AxWidget()
    w.show()
    sys.exit(app.exec_())
