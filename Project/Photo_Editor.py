import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QInputDialog, QColorDialog
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
        self.tools = Editor_tools('init.jpg', 1310, 920, self)
        self.base()

    def base(self):
        self.lbl.setPixmap(QPixmap(self.tools.name))
        self.btn_new.clicked.connect(self.tools.new_picture)
        self.btn_copy.clicked.connect(self.tools.copy_picture)
        self.btn_rename.clicked.connect(self.tools.rename_picture)
        self.btn_roted_l.clicked.connect(self.tools.roted_l)
        self.btn_roted_r.clicked.connect(self.tools.roted_r)
        self.btn_sepia.clicked.connect(self.tools.sepia)
        self.btn_black.clicked.connect(self.tools.black)
        self.btn_negativ.clicked.connect(self.tools.negativ)
        self.btn_frame.clicked.connect(self.tools.frame)
        '''self.btn_cut.clicked.connect(self.tools.cut)'''


class Editor_tools:
    def __init__(self, name, x, y, base):
        self.name = name
        self.x = x
        self.y = y
        self.base = base
        self.copy_ind = 1
        self.im = I.open(self.name)

    def copy_picture(self):
        i, okBtnPressed = QInputDialog.getText(self.base, "Введите название картинки",
                                               "Копия")
        if okBtnPressed:
            if not (os.path.isfile(i)):
                if i == '':
                    str = '({}).'.format(self.copy_ind)
                    if os.path.isfile(
                            str.join(self.name.split('.'))):
                        self.copy_ind += 1
                        str = '({}).'.format(self.copy_ind)
                    i = str.join(self.name.split('.'))
                self.im.save(i)
                self.exit_picture(i)
            else:
                self.error1 = Error('Указанный файл уже существует')
                self.error1.show()

    def rename(self):
        i, okBtnPressed = QInputDialog.getText(self.base, "Введите новое название картинки",
                                               "Новое название")
        if okBtnPressed:
            self.im.save(i)
            self.exit_picture(i)

    def new_picture(self):
        i, okBtnPressed = QInputDialog.getText(self.base, "Введите название картинки",
                                               "Картинка")
        if okBtnPressed:
            self.copy_ind = 1
            self.exit_picture(i)

    def exit_picture(self, i):
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
                self.base.lbl.resize(x, y)
                self.base.lbl.move(570 + 655 - x // 2, 490 - y // 2)
                self.name = i
                self.x = x
                self.y = y
                self.base.lbl.setPixmap(QPixmap(self.name))

    def roted_l(self):
        if self.name != 'init.jpg':
            if 1310 < self.y or 920 < self.x:
                self.error2 = Error('Невозможно перевернуть картинку')
                self.error2.show()
            else:
                self.im.transpose(I.ROTATE_270).save(self.name)
                self.exit_picture(self.name)

    def roted_r(self):
        if self.name != 'init.jpg':
            if 1310 < self.y or 920 < self.x:
                self.error2 = Error('Невозможно перевернуть картинку')
                self.error2.show()
            else:
                self.im.transpose(I.ROTATE_90).save(self.name)
                self.exit_picture(self.name)

    def sepia(self):
        if self.name != 'init.jpg':
            pixels = self.im.load()
            for i in range(self.x):
                for j in range(self.y):
                    r, g, b = pixels[i, j]
                    o = (r + g + b) // 3
                    pixels[i, j] = int(o + 48), int(o + 32), int(o)
            self.im.save(self.name)
            self.exit_picture(self.name)

    def negativ(self):
        if self.name != 'init.jpg':
            pixels = self.im.load()
            for i in range(self.x):
                for j in range(self.y):
                    r, g, b = pixels[i, j]
                    pixels[i, j] = 255 - r, 255 - g, 255 - b
            self.im.save(self.name)
            self.exit_picture(self.name)

    def black(self):
        if self.name != 'init.jpg':
            pixels = self.im.load()
            for i in range(self.x):
                for j in range(self.y):
                    r, g, b = pixels[i, j]
                    c = (r + g + b) // 3
                    pixels[i, j] = c, c, c
            self.im.save(self.name)
            self.exit_picture(self.name)

    def frame(self):
        if self.name != 'init.jpg':
            color = QColorDialog.getColor()
            fr = self.base.wheight.value()
            im_n = I.new("RGB", (self.x + fr * 2, self.y + fr * 2), color.name())
            pixels = self.im.load()
            pixels1 = im_n.load()
            for i in range(self.x):
                for j in range(self.y):
                    pixels1[i + fr, j + fr] = pixels[i, j]
            self.im = im_n
            self.x += fr * 2
            self.y += fr * 2
            im_n.save(self.name)
            self.exit_picture(self.name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Photo_Editor()
    ex.show()
    sys.exit(app.exec_())
