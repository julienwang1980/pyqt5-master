# -*- coding: utf-8 -*-
'''

装载Gif动画

QMovie
'''

import sys
from PyQt5.QtWidgets import QApplication,  QLabel  ,QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
import time
import subprocess as sp

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import subprocess

def xunhuan():
    while True:
        print('print')

temp = ''
class WorkThread(QThread):
    star = pyqtSignal()
    end = pyqtSignal()

    def run(self):
        global temp
        while True:
        # print('pr')
            self.sleep(3)
            print(temp)
        # p = sp.Popen([xunhuan()], stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
        # p = sp.Popen([xunhuan()])
        # self.end.emit()


class LoadingGif(QWidget):
    def __init__(self):
        super(LoadingGif, self).__init__()
        # p = sp.Popen([xunhuan()], stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
        # xunhuan()
        global temp
        temp = 'temp'
        self.workThread = WorkThread()
        # self.workThread.start()
        self.label = QLabel("",self)
        self.setFixedSize(128,128)
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)
        self.movie = QMovie('./images/loading.gif')
        self.label.setMovie(self.movie)
        self.workThread.end.connect(lambda: self.endmov())
        self.workThread.star.connect(lambda: start(self))
        self.movie.start()
        # self.workThread.star.emit()

        p = sp.Popen(['ping ', 'www.baidu.com','-t'], stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
        strs = ''
        for bytes in p.stdout:
            str = bytes.decode('gbk')
            strs = strs + str
            print(strs)

    def endmov(self):
        self.stop()

    def start(slef):
        p = sp.Popen([xunhuan()])
        # print ('sta')
        self.workThread.start.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = LoadingGif()
    form.show()
    sys.exit(app.exec_())

