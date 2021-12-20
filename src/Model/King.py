from src.Model.Piece import Piece
from PyQt6.QtGui import QPixmap, QPainter
from src.res import resource_path


class King(Piece):
    def __init__(self, x, y, team):
        super().__init__(x, y)
        self.team = team
        self.image = None
        match self.team:
            case "White":
                self.image = QPixmap(resource_path("Pieces/white-king.png"))
                self.type = "WKing"
            case "Black":
                self.image = QPixmap(resource_path("Pieces/black-king.png"))
                self.type = "BKing"

    def allMoves(self):
        moves = []
        for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            x = self.position[0] + dx
            y = self.position[1] + dy
            if x not in range(8) or y not in range(8):
                continue
            moves.append((x, y))

        return moves

    def paintEvent(self, event):
        super().paintEvent(event)
        paint = QPainter(self)
        paint.drawPixmap(0, 0, self.width(), self.height(), QPixmap(self.image))
