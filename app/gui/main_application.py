import sys

from PyQt5.QtWidgets import QApplication

from app.gui.windows import Windows
from app.gui.windows_ui import Windows_Ui


class Main_Form(Windows):
    def __init__(self):
        super(Main_Form, self).__init__()
        self.ui = Windows_Ui()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_form = Main_Form()
    main_form.show()

    sys.exit(app.exec_())
