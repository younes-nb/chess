from .Piece import Piece
from PyQt6.QtGui import QPixmap
from res import resource_path


class Blank(Piece):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = QPixmap(resource_path("Images/blank.png"))
        self.type = "Blank"
