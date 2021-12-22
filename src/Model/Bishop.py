from src.Model.Piece import Piece
from PyQt6.QtGui import QPixmap
from src.res import resource_path


class Bishop(Piece):
    def __init__(self, game, x, y, team):
        super().__init__(game, x, y)
        self.team = team
        self.image = None
        match self.team:
            case "White":
                self.image = QPixmap(resource_path("Pieces/wb.svg"))
                self.type = "WBishop"
            case "Black":
                self.image = QPixmap(resource_path("Pieces/bb.svg"))
                self.type = "BBishop"

    def allMoves(self):
        moves = []
        for (dx, dy) in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            for i in range(1, 8):
                x = self.position[0] + (dx * i)
                y = self.position[1] + (dy * i)
                if x not in range(8) or y not in range(8):
                    continue
                moves.append((x, y))

        return moves