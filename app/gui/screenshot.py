import sys
import random
import time

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, QPoint
from PyQt5.QtGui import QPalette, QBrush
from PyQt5.QtWidgets import QWidget, QApplication, QRubberBand


class Trans(QWidget):

    def __init__(self):
        super(Trans, self).__init__()
        self.cutPic = False
        self.screen = QApplication.primaryScreen()
        self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
        pal = QPalette()
        pal.setBrush(QPalette.Highlight, QBrush(QtCore.Qt.green))
        self.rubberBand.setPalette(pal)
        self.cutP()

    def cutP(self):
        self.cutPic = True
        self.setCursor(QtCore.Qt.CrossCursor)

    # 鼠标左键开始截图
    def mousePressEvent(self, event):
        # self.cutP()
        if self.cutPic == True:
            self.old = event.globalPos()  # 这两行代码
            self.old.x, self.old.y = self.old.x(), self.old.y()  # 是记录鼠标初始位置
        else:
            # self.rubberBand.close()
            self.save_image()
            # self.rubberBand.close()
            self.close()

    # 鼠标移动，生成截图框
    def mouseMoveEvent(self, event):
        if self.cutPic == True:
            self.new = event.globalPos()
            self.new.x, self.new.y = self.new.x(), self.new.y()
            if self.new.x < self.old.x and self.new.y < self.old.y:
                self.rect = QtCore.QRect(QPoint(self.new.x, self.new.y), QPoint(self.old.x, self.old.y))
            elif self.new.x < self.old.x:
                self.rect = QtCore.QRect(QPoint(self.new.x, self.old.y), QPoint(self.old.x, self.new.y))
            elif self.new.y < self.old.y:
                self.rect = QtCore.QRect(QPoint(self.old.x, self.new.y), QPoint(self.new.x, self.old.y))
            else:
                self.rect = QtCore.QRect(QPoint(self.old.x, self.old.y), QPoint(self.new.x, self.new.y))
            self.rubberBand.setGeometry(self.rect)
            self.rubberBand.show()

    # 松开鼠标，截图完成
    def mouseReleaseEvent(self, event):
        if self.cutPic == True:
            self.setCursor(QtCore.Qt.ArrowCursor)  # 设置鼠标形状，自行baidu
            self.cutPic = False

    def save_image(self):
        x, y = self.rubberBand.x(), self.rubberBand.y()
        width, height = self.rubberBand.width(), self.rubberBand.height()

        # 再截取图片
        self.screenshot = self.screen.grabWindow(QApplication.desktop().winId(), x, y,
                                                 width, height)
        # self.rubberBand.setGeometry(self.rect)
        # self.rubberBand.show()
        # 显示橡皮筋类
        # save，随机一个名字
        dt = 'pic'
        while 1:
            n = random.randint(0, 10)
            dt += str(n)
            if n == 5:
                break
        self.screenshot.save('cut' + str(dt) + '.png', 'png')  # 保存图片
        # self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    trans = Trans()
    trans.showFullScreen()
    trans.setWindowOpacity(0.3)
    trans.raise_()
    trans.show()
    sys.exit(app.exec_())
