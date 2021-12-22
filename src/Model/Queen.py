from src.Model.Piece import Piece
from PyQt6.QtGui import QPixmap
from src.res import resource_path


class Queen(Piece):
    def __init__(self, game, x, y, team):
        super().__init__(game, x, y)
        self.team = team
        self.image = None
        match self.team:
            case "White":
                self.image = QPixmap(resource_path("Pieces/wq.svg"))
                self.type = "WQueen"
            case "Black":
                self.image = QPixmap(resource_path("Pieces/bq.svg"))
                self.type = "BQueen"

    def allMoves(self):
        moves = []
        for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            for i in range(1, 8):
                x = self.position[0] + (dx * i)
                y = self.position[1] + (dy * i)
                if x not in range(8) or y not in range(8):
                    continue
                if self.game.pieces[x][y].team == self.team:
                    break
                moves.append((x, y))
                if self.game.pieces[x][y].type != "Blank":
                    break

        return moves
