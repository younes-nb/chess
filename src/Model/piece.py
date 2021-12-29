from PyQt6.QtGui import QPainter, QColor, QPixmap, QRgba64
from PyQt6.QtWidgets import QLabel


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
        self.target = False
        self.checker = False

    def mousePressEvent(self, event):
        QLabel.mousePressEvent(self, event)
        if self.is_painted or self.target:
            self.game.move_piece(self)
            if self.game.checked_king(False).is_checked:
                if self.game.check_mate():
                    self.game.setDisabled(True)

        else:
            self.game.select_piece(self)

    def paintEvent(self, event):
        QLabel.paintEvent(self, event)
        paint = QPainter(self)
        white_color = QColor(190, 190, 190)
        black_color = QColor(60, 60, 60)
        selected_color = QColor(227, 218, 50)
        painted_color = QColor(QRgba64.fromRgba(43, 167, 224, 190))
        target_color = QColor(QRgba64.fromRgba(41, 207, 23, 190))
        checker_color = QColor(QRgba64.fromRgba(209, 54, 54, 190))

        if (self.position[0] + self.position[1]) % 2 == 0:
            paint.fillRect(0, 0, self.width(), self.height(), white_color)

        else:
            paint.fillRect(0, 0, self.width(), self.height(), black_color)

        if self.selected:
            paint.fillRect(0, 0, self.width(), self.height(), selected_color)

        if self.is_painted:
            paint.fillRect(0, 0, self.width(), self.height(), painted_color)

        if self.target:
            paint.fillRect(0, 0, self.width(), self.height(), target_color)

        if self.checker:
            paint.fillRect(0, 0, self.width(), self.height(), checker_color)

        paint.drawPixmap(0, 0, self.width(), self.height(), QPixmap(self.image))
