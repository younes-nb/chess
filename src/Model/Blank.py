from src.Model.Piece import Piece
from PyQt6.QtGui import QPixmap
from src.res import resource_path


class Blank(Piece):
    def __init__(self, x, y, game):
        super().__init__(x, y, game)
        self.image = QPixmap(resource_path("Media/Pieces/blank.png"))
        self.team = "None"
        self.type = "Blank"
