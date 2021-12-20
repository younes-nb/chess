from src.Model.Piece import Piece
from PyQt6.QtGui import QPixmap
from src.res import resource_path


class Knight(Piece):
    def __init__(self, x, y, team):
        super().__init__(x, y)
        self.team = team
        self.image = None
        match self.team:
            case "White":
                self.image = QPixmap(resource_path("Pieces/white-knight.png"))
                self.type = "WKnight"
            case "Black":
                self.image = QPixmap(resource_path("Pieces/black-knight.png"))
                self.type = "BKnight"

    def allMoves(self):
        moves = []
        for (dx, dy) in ((2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)):
            x = self.position[0] + dx
            y = self.position[1] + dy
            if x not in range(8) or y not in range(8):
                continue
            moves.append((x, y))
