from src.Model.piece import Piece
from PyQt6.QtGui import QPixmap, QPainter, QColor
from src.res import resource_path


class King(Piece):
    def __init__(self, game, x, y, team):
        super().__init__(game, x, y)
        self.team = team
        self.image = None
        self.is_checked = False
        self.is_check_mate = False
        match self.team:
            case "White":
                self.image = QPixmap(resource_path("Pieces/wk.svg"))
                self.type = "WKing"
            case "Black":
                self.image = QPixmap(resource_path("Pieces/bk.svg"))
                self.type = "BKing"

    def all_moves(self):
        moves = []
        for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            x = self.position[0] + dx
            y = self.position[1] + dy
            if x not in range(8) or y not in range(8):
                continue
            if self.game.pieces[x][y].team == self.team:
                continue
            moves.append((x, y))

        return moves

    def paintEvent(self, event):
        super().paintEvent(event)
        paint = QPainter(self)
        if self.is_checked:
            paint.fillRect(0, 0, self.width(), self.height(), QColor(242, 39, 39))

        if self.is_check_mate:
            paint.fillRect(0, 0, self.width(), self.height(), QColor(145, 12, 12))
        paint.drawPixmap(0, 0, self.width(), self.height(), QPixmap(self.image))
