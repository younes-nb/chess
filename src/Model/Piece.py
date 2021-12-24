from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPainter, QColor, QPixmap, QRgba64


class Piece(QLabel):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.position = [x, y]
        self.team = None
        self.type = None
        self.image = None
        self.selected = False
        self.isPainted = False

    def mousePressEvent(self, event):
        QLabel.mousePressEvent(self, event)
        if self.isPainted:
            self.game.movePiece(self)
        else:
            self.game.selectPiece(self)

    def paintEvent(self, event):
        QLabel.paintEvent(self, event)
        paint = QPainter(self)
        whiteColor = QColor(190, 190, 190)
        blackColor = QColor(60, 60, 60)
        selectedColor = QColor(QRgba64.fromRgba(120, 150, 200, 150))
        paintedColor = QColor(QRgba64.fromRgba(100, 70, 220, 150))

        if (self.position[0] + self.position[1]) % 2 == 0:
            paint.fillRect(0, 0, self.width(), self.height(), whiteColor)

        else:
            paint.fillRect(0, 0, self.width(), self.height(), blackColor)

        if self.selected:
            paint.fillRect(0, 0, self.width(), self.height(), selectedColor)

        if self.isPainted:
            paint.fillRect(0, 0, self.width(), self.height(), paintedColor)

        paint.drawPixmap(0, 0, self.width(), self.height(), QPixmap(self.image))
