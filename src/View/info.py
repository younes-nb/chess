from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QLabel


class Info(QVBoxLayout):
    def __init__(self, name):
        super().__init__()
        self.captured_x = 0
        self.captured_y = 0

        player_title = QHBoxLayout()
        player_title.setContentsMargins(0, 0, 0, 15)
        self.player_name = QLabel(name)
        self.player_name.setStyleSheet("font-size:18px;")

        self.turn_icon = QLabel()
        player_title.addWidget(self.player_name)
        player_title.addWidget(self.turn_icon)
        player_title.setStretch(0, 1)
        self.addLayout(player_title)

        self.captured_pieces = QGridLayout()
        self.addLayout(self.captured_pieces)
