import sys

from PyQt5.QtCore import QMetaObject, Qt, QDir, QTimer
from PyQt5.QtGui import QIcon, QPixmap, QScreen
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSizePolicy, QGroupBox, QHBoxLayout, QSpinBox, \
    QCheckBox, QSpacerItem, QPushButton, qApp, QFileDialog
from PyQt5.uic.properties import QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)


class Ui_ScrShot(object):
    def setupUi(self, ScrShot):
        ScrShot.setObjectName(_fromUtf8("ScrShot"))
        ScrShot.resize(270, 270)
        self.verticalLayout = QVBoxLayout(ScrShot)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelShow = QLabel(ScrShot)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelShow.sizePolicy().hasHeightForWidth())
        self.labelShow.setSizePolicy(sizePolicy)
        self.labelShow.setText(_fromUtf8(""))
        self.labelShow.setObjectName(_fromUtf8("labelShow"))
        self.verticalLayout.addWidget(self.labelShow)
        self.groupBox = QGroupBox(ScrShot)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelSpinBox = QLabel(self.groupBox)
        self.labelSpinBox.setObjectName(_fromUtf8("labelSpinBox"))
        self.horizontalLayout_2.addWidget(self.labelSpinBox)
        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.checkBoxHideThis = QCheckBox(self.groupBox)
        self.checkBoxHideThis.setObjectName(_fromUtf8("checkBoxHideThis"))
        self.verticalLayout_2.addWidget(self.checkBoxHideThis)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonNew = QPushButton(ScrShot)
        self.pushButtonNew.setObjectName(_fromUtf8("pushButtonNew"))
        self.horizontalLayout.addWidget(self.pushButtonNew)
        self.pushButtonSave = QPushButton(ScrShot)
        self.pushButtonSave.setObjectName(_fromUtf8("pushButtonSave"))
        self.horizontalLayout.addWidget(self.pushButtonSave)
        self.pushButton_Quit = QPushButton(ScrShot)
        self.pushButton_Quit.setObjectName(_fromUtf8("pushButton_Quit"))
        self.horizontalLayout.addWidget(self.pushButton_Quit)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ScrShot)
        QMetaObject.connectSlotsByName(ScrShot)

    def retranslateUi(self, ScrShot):
        ScrShot.setWindowTitle(_translate("ScrShot", "Form", None))
        self.groupBox.setTitle(_translate("ScrShot", "Options", None))
        self.labelSpinBox.setText(_translate("ScrShot", "Screenstot Delay:", None))
        self.checkBoxHideThis.setText(_translate("ScrShot", "Hide This Window", None))
        self.pushButtonNew.setText(_translate("ScrShot", "新建", None))
        self.pushButtonSave.setText(_translate("ScrShot", "保存", None))
        self.pushButton_Quit.setText(_translate("ScrShot", "退出", None))


class MainFrom(QWidget):
    def __init__(self):
        super(MainFrom, self).__init__()
        self.Ui = Ui_ScrShot()
        self.Ui.setupUi(self)
        self.Ui.labelShow.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # size 策略为 可扩展 expanding
        self.Ui.labelShow.setAlignment(Qt.AlignCenter)  # alignment 对齐方式 居中
        self.Ui.labelShow.setMinimumSize(240, 160)  # 最小为 240 X 160
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 设置总是在最前
        self.setWindowTitle(u'截图工具')
        self.setWindowIcon(QIcon(':qq.ico'))

        self.shootScreen()
        self.Ui.spinBox.setSuffix(' s')
        self.Ui.spinBox.setMaximum(60)
        self.Ui.spinBox.setValue(5)

        self.Ui.pushButtonNew.clicked.connect(self.newScreenshot)  # 从新开始新建截图
        self.Ui.pushButtonSave.clicked.connect(self.saveScreenshot)  # 保存截图
        self.Ui.pushButton_Quit.clicked.connect(self.close)  # 退出

    # 截图
    def shootScreen(self):
        if self.Ui.spinBox.value() != 0:
            qApp.beep()  # 操作带上系统的响铃
        screen = QApplication.primaryScreen()
        self.originalPixmap = screen.grabWindow(QApplication.desktop().winId())  # 获取 屏幕桌面截图
        self.updateScreenshotLabel()
        self.Ui.pushButtonNew.setDisabled(False)
        if self.Ui.checkBoxHideThis.isChecked():  # 当选择隐藏按钮为True时， 截图完成显示窗体
            self.show()

        #  获取图片显示在label上

    def updateScreenshotLabel(self):
        # self.originalPixmap.scaled()  scaled()函数的声明const返回一个Qpixmap
        # QtCore.Qt.KeepAspectRatio 尽可能大的在一个给定的矩形大小缩放到一个矩形且保持长宽比。
        # QtCore.Qt.SmoothTransformation 平滑转换
        self.Ui.labelShow.setPixmap(self.originalPixmap.scaled(self.Ui.labelShow.size(), Qt.KeepAspectRatio,
                                                               Qt.SmoothTransformation))
        # 保存截图图片

    def saveScreenshot(self):
        format = 'png'
        initialPath = QDir.currentPath() + "/untitled." + format

        fileName = QFileDialog.getSaveFileName(self, u"另存为",
                                               initialPath,
                                               "%s Files (*.%s)" % (format.upper(), format))
        print(fileName)
        if fileName:
            self.originalPixmap.save(fileName[0])

        # 新创建截图

    def newScreenshot(self):
        if self.Ui.checkBoxHideThis.isChecked():
            self.hide()
        self.Ui.pushButtonNew.setDisabled(True)
        QTimer.singleShot(self.Ui.spinBox.value() * 1000, self.shootScreen)  # * 秒后触发截图

    # 重载 resizeEvent 方法
    def resizeEvent(self, event):
        scaledSize = self.originalPixmap.size()
        scaledSize.scale(self.Ui.labelShow.size(), Qt.KeepAspectRatio)

        if not self.Ui.labelShow.pixmap() or scaledSize != self.Ui.labelShow.pixmap().size():  # 当pixmap改变大小时候重新加载updateScreenshotLabel
            self.updateScreenshotLabel()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    MainApp = MainFrom()
    MainApp.show()
    sys.exit(App.exec_())
