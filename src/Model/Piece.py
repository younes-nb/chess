from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPainter, QColor, QPixmap, QRgba64


class Piece(QLabel):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.position = [x, y]
        self.image = None
        self.selected = False
        self.paint = False

    def select(self):
        pass

    def mousePressEvent(self, event):
        QLabel.mousePressEvent(self, event)

        self.game.selectPiece(self)
        self.update()

    def paintEvent(self, event):
        QLabel.paintEvent(self, event)
        paint = QPainter(self)
        whiteColor = QColor(190, 190, 190)
        blackColor = QColor(60, 60, 60)
        selectedColor = QColor(QRgba64.fromRgba(120, 150, 200, 150))

        if (self.position[0] + self.position[1]) % 2 == 0:
            paint.fillRect(0, 0, self.width(), self.height(), whiteColor)

        else:
            paint.fillRect(0, 0, self.width(), self.height(), blackColor)

        if self.selected:
            paint.fillRect(0, 0, self.width(), self.height(), selectedColor)

        paint.drawPixmap(0, 0, self.width(), self.height(), QPixmap(self.image))
