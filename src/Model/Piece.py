from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPainter, QColor, QPixmap


class Piece(QLabel):
    def __init__(self, x, y):
        super().__init__()
        self.position = [x, y]
        self.selected = False
        self.image = None

    def paintEvent(self, event):
        QLabel.paintEvent(self, event)
        paint = QPainter(self)
        whiteColor = QColor(190, 190, 190)
        blackColor = QColor(60, 60, 60)

        if (self.position[0] + self.position[1]) % 2 == 0:
            paint.fillRect(0, 0, self.width(), self.height(), whiteColor)
        else:
            paint.fillRect(0, 0, self.width(), self.height(), blackColor)
        paint.drawPixmap(0, 0, self.width(), self.height(), QPixmap(self.image))
