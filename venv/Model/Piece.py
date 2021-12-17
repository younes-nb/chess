from PyQt6.QtWidgets import QLabel, QSizePolicy
from PyQt6.QtGui import QPainter, QColor, QPixmap
from PyQt6.QtCore import Qt
from res import resource_path


class Piece(QLabel):
    def __init__(self, x, y):
        super().__init__()
        self.position = [x, y]
        self.selected = False

    def paintEvent(self, event):
        QLabel.paintEvent(self, event)
        paint = QPainter(self)
        whiteColor = QColor(255, 255, 255)
        blackColor = QColor(180, 180, 180)

        if (self.position[0] + self.position[1]) % 2 == 0:
            paint.fillRect(0, 0, self.width(), self.height(), whiteColor)
        else:
            paint.fillRect(0, 0, self.width(), self.height(), blackColor)
        paint.drawPixmap(0, 0, self.width(), self.height(), QPixmap(self.image))
