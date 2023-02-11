from src.model.piece import Piece
from PyQt6.QtGui import QPixmap
from src.res import resource_path


class Knight(Piece):
    def __init__(self, game, x, y, team):
        super(Knight, self).__init__(game, x, y)
        self.team = team
        self.image = None
        match self.team:
            case "White":
                self.image = QPixmap(resource_path("pieces/wn.svg"))
                self.type = "WKnight"
            case "Black":
                self.image = QPixmap(resource_path("pieces/bn.svg"))
                self.type = "BKnight"

    def all_moves(self):
        moves = []
        for (dx, dy) in ((2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)):
            x = self.position[0] + dx
            y = self.position[1] + dy
            if x not in range(8) or y not in range(8):
                continue
            if self.game.pieces[x][y].team == self.team:
                continue
            moves.append((x, y))

        return moves
