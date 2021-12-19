from src.Model.Piece import Piece
from PyQt6.QtGui import QPixmap
from src.res import resource_path


class Bishop(Piece):
    def __init__(self, x, y, team):
        super().__init__(x, y)
        self.team = team
        self.image = None
        match self.team:
            case "White":
                self.image = QPixmap(resource_path("Pieces/white-bishop.png"))
                self.type = "WBishop"
            case "Black":
                self.image = QPixmap(resource_path("Pieces/black-bishop.png"))
                self.type = "BBishop"
