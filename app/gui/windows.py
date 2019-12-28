from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget


class Windows(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setWindowTitle("图像文本识别")
        self.setFixedSize(740, 480)