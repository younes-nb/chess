from src.model.piece import Piece
from PyQt6.QtGui import QPixmap
from src.res import resource_path


class Pawn(Piece):
    def __init__(self, game, x, y, team):
        super(Pawn, self).__init__(game, x, y)
        self.team = team
        self.image = None
        match self.team:
            case "White":
                self.image = QPixmap(resource_path("pieces/wp.svg"))
                self.type = "WPawn"
            case "Black":
                self.image = QPixmap(resource_path("pieces/bp.svg"))
                self.type = "BPawn"

    def all_moves(self):
        moves = []
        x = None
        y = self.position[1]
        match self.team:
            case "White":
                x = self.position[0] - 1
                if self.position[0] == 6:
                    if self.game.pieces[x][y].team == "None" and self.game.pieces[x - 1][y].team == "None":
                        moves.append((x - 1, y))
            case "Black":
                x = self.position[0] + 1
                if self.position[0] == 1:
                    if self.game.pieces[x][y].team == "None" and self.game.pieces[x + 1][y].team == "None":
                        moves.append((x + 1, y))

        for dy in (-1, 0, 1):
            y = self.position[1] + dy
            if x not in range(8) or y not in range(8):
                continue
            if dy != 0:
                if self.game.pieces[x][y].team != self.team and self.game.pieces[x][y].team != "None":
                    moves.append((x, y))
                else:
                    continue
            if self.game.pieces[x][y].team == "None":
                moves.append((x, y))

        return moves
