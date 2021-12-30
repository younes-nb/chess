from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGridLayout
from src.View.info_view import InfoView
from src.res import resource_path


class GameView(QWidget):
    def __init__(self, pieces, white_name, black_name):
        super().__init__()
        self.white_name = white_name
        self.black_name = black_name
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

        self.info_white = InfoView(self.white_name)
        self.info_white.player_icon.setPixmap(QPixmap(resource_path("Icons/white-player.png")))
        self.info_white.turn_icon.setPixmap(QPixmap(resource_path("Icons/turn.png")))
        self.info_white.turn_icon.setToolTip("It's your turn!")

        self.info_black = InfoView(self.black_name)
        self.info_black.player_icon.setPixmap(QPixmap(resource_path("Icons/black-player.png")))
        self.info_black.turn_icon.setPixmap(QPixmap(resource_path("Icons/turn-blank.png")))
        self.info_black.turn_icon.setToolTip("Wait!")
        self.info_black.setContentsMargins(0, 35, 0, 15)

        info_container = QVBoxLayout()
        info_container.setAlignment(Qt.AlignmentFlag.AlignTop)
        info_container.addLayout(self.info_white)
        info_container.addLayout(self.info_black)

        self.layout.addLayout(info_container)
        self.layout.setStretch(0, 1)
