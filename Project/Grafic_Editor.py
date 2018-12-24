import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QInputDialog
from PyQt5 import uic


class Grafic_Editor(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('дизайн.ui', self)
        self.name = 'init.png'
        self.base()

    def base(self):
        self.lbl.
        self.btn_new.clicked.connect(self.new)
        self.btn_roted_l.clicked.connect(self.roted_l)
        self.btn_roted_r.clicked.connect(self.roted_r)
        self.btn_sepia.clicked.connect(self.sepia)
        self.btn_black.clicked.connect(self.black)
        self.btn_negativ.clicked.connect(self.negativ)
        self.btn_frame.clicked.connect(self.frame)
        self.btn_cut.clicked.connect(self.cut)

    def new_picture(self):
        i, okBtnPressed = QInputDialog.getText(
            self, "Введите название картинки",
        )
        if okBtnPressed:
            self.name = i




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Grafic_Editor()
    sys.exit(app.exec_())
