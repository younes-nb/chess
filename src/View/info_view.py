from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QLabel


class InfoView(QVBoxLayout):
    def __init__(self, name):
        super().__init__()
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
        player_title.setStretch(0, 1)

        self.captured_pieces = QGridLayout()

        self.addLayout(player_title)
        self.addLayout(self.captured_pieces)
