from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QPushButton


class InfoView(QVBoxLayout):
    def __init__(self, name):
        super(InfoView, self).__init__()
        self.captured_x = 0
        self.captured_y = 0

        self.player_name = QLabel(name)
        self.player_name.setContentsMargins(0, 0, 20, 0)
        self.player_name.setStyleSheet("font-size:20px;")

        self.turn_icon = QLabel()

        self.player_icon = QLabel()

        player_title = QHBoxLayout()
        player_title.setContentsMargins(0, 0, 0, 20)
        player_title.addWidget(self.player_icon)
        player_title.addWidget(self.player_name)
        player_title.addWidget(self.turn_icon)
        player_title.setStretch(1, 1)

        self.captured_pieces = QGridLayout()

        promotion_container = QVBoxLayout()
        self.promotion_text = QLabel("Promote your pawn".format(name))
        self.promotion_text.setStyleSheet("font-size: 16px;")
        self.promotion_text.setContentsMargins(0, 20, 0, 20)
        self.promotion_text.hide()

        self.queen = QPushButton("Queen")
        self.queen.setStyleSheet("font-size: 16px;")
        self.queen.hide()

        self.bishop = QPushButton("Bishop")
        self.bishop.setStyleSheet("font-size: 16px;")
        self.bishop.hide()

        self.knight = QPushButton("Knight")
        self.knight.setStyleSheet("font-size: 16px;")
        self.knight.hide()

        self.rook = QPushButton("Rook")
        self.rook.setStyleSheet("font-size: 16px;")
        self.rook.hide()

        pieces = QVBoxLayout()
        pieces.addWidget(self.queen)
        pieces.addWidget(self.bishop)
        pieces.addWidget(self.knight)
        pieces.addWidget(self.rook)

        promotion_container.addWidget(self.promotion_text)
        promotion_container.addLayout(pieces)

        self.addLayout(player_title)
        self.addLayout(self.captured_pieces)
        self.addLayout(promotion_container)
