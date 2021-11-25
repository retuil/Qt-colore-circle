from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint
import sys


class QT(QMainWindow):
    def __init__(self):
        super().__init__()
        Interface.__init__(self)
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
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        rad = randint(5, 400)
        qp.drawEllipse(randint(0, 800), randint(0, 600), rad, rad)


class Interface():
    def __init__(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Рисование')
        self.pushButton = QPushButton('Окружность', self)
        self.pushButton.setGeometry(340, 250, 111, 61)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


app = QtWidgets.QApplication(sys.argv)
ex = QT()
ex.show()
sys.excepthook = except_hook
sys.exit(app.exec())