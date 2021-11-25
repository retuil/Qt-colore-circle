from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint
import sys


class QT(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.start = False
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.start = True
        self.repaint()

    def paintEvent(self, event):
        if self.start:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        rad = randint(5, 400)
        qp.drawEllipse(randint(0, 800), randint(0, 600), rad, rad)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


app = QtWidgets.QApplication(sys.argv)
ex = QT()
ex.show()
sys.excepthook = except_hook
sys.exit(app.exec())