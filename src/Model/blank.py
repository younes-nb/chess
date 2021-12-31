from src.Model.piece import Piece
from PyQt6.QtGui import QPixmap
from src.res import resource_path


class Blank(Piece):
    def __init__(self, game, x, y):
        super(Blank, self).__init__(game, x, y)
        self.image = QPixmap(resource_path("Media/Pieces/blank.png"))
        self.team = "None"
        self.type = "Blank"
