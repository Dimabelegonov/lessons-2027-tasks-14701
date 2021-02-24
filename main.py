import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor, QBrush


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui.ui", self)
        self.flag = False
        self.pushButton.clicked.connect(self.set_update)

    def set_update(self):
        self.flag = True
        self.update()

    def paintEvent(self, QPaintEvent):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.drawEll(qp)
            qp.end()
            self.flag = False

    def drawEll(self, qp):
        color = QColor("yellow")
        qp.setPen(color)

        x = random.randrange(100, 600)
        y = random.randrange(100, 400)
        r = random.randrange(50, 200)
        qp.setBrush(QColor("yellow"))
        qp.drawEllipse(x, y, r, r)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
