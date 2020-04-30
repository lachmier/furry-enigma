#!/usr/bin/env python3
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


# Icons used: "38 Dice Icons" https://game-icons.net/tags/dice.html
# are Licensed under CC BY 3.0 http://creativecommons.org/licenses/by/3.0/

dice_map = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six"}


class dice_sim(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def rolldice(self):
        pixmap = QPixmap(self.roll_update())
        if not pixmap.isNull():
            self.dice.setPixmap(self.resize_pixmap(pixmap))

    def roll_update(self):
        return f"dice/dice-six-faces-{dice_map.get(random.randint(1, 6))}.svg"

    def resize_pixmap(self, pixmap):
        return pixmap.scaled(160, 300, Qt.KeepAspectRatio, Qt.FastTransformation)

    def initUI(self):
        QToolTip.setFont(QFont("SansSerif", 10))

        self.dice = QLabel(self)
        pixmap = QPixmap(self.roll_update())

        self.dice.setPixmap(self.resize_pixmap(pixmap))
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
        self.setWindowIcon(QIcon("icon/perspective-dice-six-faces-six.svg"))
        self.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = dice_sim()
    sys.exit(app.exec_())
