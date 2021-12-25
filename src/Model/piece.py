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
        self.is_painted = False

    def mousePressEvent(self, event):
        QLabel.mousePressEvent(self, event)
        if self.is_painted:
            self.game.move_piece(self)
        else:
            self.game.select_piece(self)

    def paintEvent(self, event):
        QLabel.paintEvent(self, event)
        paint = QPainter(self)
        white_color = QColor(190, 190, 190)
        black_color = QColor(60, 60, 60)
        selected_color = QColor(QRgba64.fromRgba(120, 150, 200, 150))
        painted_color = QColor(QRgba64.fromRgba(100, 70, 220, 150))

        if (self.position[0] + self.position[1]) % 2 == 0:
            paint.fillRect(0, 0, self.width(), self.height(), white_color)

        else:
            paint.fillRect(0, 0, self.width(), self.height(), black_color)

        if self.selected:
            paint.fillRect(0, 0, self.width(), self.height(), selected_color)

        if self.is_painted:
            paint.fillRect(0, 0, self.width(), self.height(), painted_color)

        paint.drawPixmap(0, 0, self.width(), self.height(), QPixmap(self.image))
