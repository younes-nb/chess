from src.Model.Piece import Piece
from PyQt6.QtGui import QPixmap
from src.res import resource_path


class Pawn(Piece):
    def __init__(self, game, x, y, team):
        super().__init__(game, x, y)
        self.team = team
        self.image = None
        match self.team:
            case "White":
                self.image = QPixmap(resource_path("Pieces/wp.svg"))
                self.type = "WPawn"
            case "Black":
                self.image = QPixmap(resource_path("Pieces/bp.svg"))
                self.type = "BPawn"

    def allMoves(self):
        moves = []
        x = None
        y = self.position[1]
        match self.team:
            case "White":
                x = self.position[0] - 1
                if self.position[0] == 6:
                    moves.append((x - 1, y))
            case "Black":
                x = self.position[0] + 1
                if self.position[0] == 1:
                    moves.append((x + 1, y))

        for dy in (-1, 0, 1):
            y = self.position[1] + dy
            if x not in range(8) or y not in range(8):
                continue
            if dy != 0:
                match self.team:
                    case "White":
                        if self.game.pieces[x][y].team != "Black":
                            continue
                    case "Black":
                        if self.game.pieces[x][y].team != "White":
                            continue
            if self.game.pieces[x][y].team == "None":
                moves.append((x, y))

        return moves
