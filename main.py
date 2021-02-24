import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor, QBrush
from ui_file import Ui_Form


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        a, b, c = random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)
        color = QColor(a, b, c)
        qp.setPen(color)

        x = random.randrange(50, 550)
        y = random.randrange(100, 250)
        r = random.randrange(50, 150)
        qp.setBrush(QColor(a, b, c))
        qp.drawEllipse(x, y, r, r)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
