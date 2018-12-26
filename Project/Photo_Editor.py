import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import os.path
from PIL import Image as I


class Error(QWidget):
    def __init__(self, message):
        super().__init__()
        self.setGeometry(800, 470, 230, 80)
        self.setWindowTitle('ERROR')

        self.txt = QLabel(self)
        self.txt.setText(message)
        self.txt.resize(250, 40)
        self.txt.move(5, 5)


class Photo_Editor(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('дизайн.ui', self)
        self.name = 'init.jpg'
        self.x = 1310
        self.y = 920
        self.base()

    def base(self):
        self.lbl.setPixmap(QPixmap(self.name))
        self.btn_new.clicked.connect(self.new_picture)
        '''self.btn_roted_l.clicked.connect(self.roted_l)
        self.btn_roted_r.clicked.connect(self.roted_r)
        self.btn_sepia.clicked.connect(self.sepia)
        self.btn_black.clicked.connect(self.black)
        self.btn_negativ.clicked.connect(self.negativ)
        self.btn_frame.clicked.connect(self.frame)
        self.btn_cut.clicked.connect(self.cut)'''

    def new_picture(self):
        i, okBtnPressed = QInputDialog.getText(self, "Введите название картинки",
                                               "Картинка")
        if okBtnPressed:
            if not (os.path.isfile(i)):
                self.error1 = Error('Указанный файл не существует')
                self.error1.show()
            else:
                self.im = I.open(i)
                x, y = self.im.size
                if 1310 < x or 920 < y:
                    self.error2 = Error('Неверный размер картинки')
                    self.error2.show()
                else:
                    self.lbl.resize(x, y)
                    self.lbl.move(570 + 655 - x // 2, 460 - y // 2)
                    self.name = i
                    self.x = x
                    self.y = y
                    self.lbl.setPixmap(QPixmap(self.name))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Photo_Editor()
    ex.show()
    sys.exit(app.exec_())
