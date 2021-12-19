from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QLabel


class InfoView(QVBoxLayout):
    def __init__(self, name):
        super().__init__()
        playerTitle = QHBoxLayout()
        self.playerName = QLabel(name)
        self.playerName.setStyleSheet("font-size:18px;")

        self.turnIcon = QLabel()
        playerTitle.addWidget(self.playerName)
        playerTitle.addWidget(self.turnIcon)
        playerTitle.setStretch(0, 1)
        self.addLayout(playerTitle)

        self.outPieces = QGridLayout()
        self.addLayout(self.outPieces)
