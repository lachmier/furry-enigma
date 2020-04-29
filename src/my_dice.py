import random
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QToolTip,
    QPushButton,
    QApplication,
    QWidget,
    QLabel,
)
from PyQt5.QtGui import QIcon, QPixmap, QFont


class dicesimulator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def rolldice(self):
        roll = str(random.randint(1, 6))

        pixmap = QPixmap("dice/dice_" + roll + ".png")
        smaller_pixmap = pixmap.scaled(
            160, 300, Qt.KeepAspectRatio, Qt.FastTransformation
        )
        if not pixmap.isNull():
            self.dice.setPixmap(smaller_pixmap)
            self.dice.adjustSize()
            self.resize(pixmap.size())

    def initUI(self):
        roll = str(random.randint(1, 6))

        QToolTip.setFont(QFont("SansSerif", 10))

        self.dice = QLabel(self)
        pixmap = QPixmap("dice/dice_" + roll + ".png")
        smaller_pixmap = pixmap.scaled(
            160, 300, Qt.KeepAspectRatio, Qt.FastTransformation
        )
        self.dice.setPixmap(smaller_pixmap)
        self.dice.move(1, 1)

        btn = QPushButton("Roll", self)
        btn.setFont(QFont("SansSerif", 20))
        btn.setToolTip("Click to Roll Die")
        btn.clicked.connect(self.rolldice)
        btn.resize(162, 40)
        btn.move(0, 161)

        self.setGeometry(1427, 30, 162, 201)
        self.setFixedSize(self.size())
        self.setWindowTitle("Dice Simulator")
        self.setWindowIcon(QIcon("icon.png"))
        self.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = dicesimulator()
    sys.exit(app.exec_())
