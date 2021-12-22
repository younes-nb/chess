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
        y = None
        match self.team:
            case "White":
                y = self.position[1] + 1
            case "Black":
                y = self.position[1] - 1

        for dx in (-1, 0, 1):
            x = self.position[0] + dx
            if x not in range(8) or y not in range(8):
                continue
            moves.append((x, y))

        return moves
