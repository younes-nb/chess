from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGridLayout
from src.View.info_view import InfoView
from src.res import resource_path


class GameView(QWidget):
    def __init__(self, pieces):
        super().__init__()

        self.layout = QHBoxLayout(self)
        self.board = QGridLayout()
        self.board.setSpacing(0)
        self.board.setContentsMargins(0, 0, 0, 0)
        self.pieces = pieces
        for x in range(8):
            for y in range(8):
                self.board.addWidget(self.pieces[x][y], x, y)
        self.layout.addLayout(self.board)
        self.layout.addSpacing(20)

        info_container = QVBoxLayout()
        info_container.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.info_white = InfoView("White")
        self.info_black = InfoView("Black")
        self.info_black.setContentsMargins(0, 35, 0, 15)
        info_container.addLayout(self.info_white)
        info_container.addLayout(self.info_black)
        self.layout.addLayout(info_container)
        self.layout.setStretch(0, 1)
        self.info_white.turn_icon.setPixmap(QPixmap(resource_path("Icons/turn.png")))
        self.info_black.turn_icon.setPixmap(QPixmap(resource_path("Icons/turn-blank.png")))
        self.info_white.turn_icon.setToolTip("It's your turn!")
        self.info_black.turn_icon.setToolTip("Wait!")
