from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QLabel


class InfoView(QVBoxLayout):
    def __init__(self, name):
        super().__init__()
        self.capturedX = 0
        self.capturedY = 0

        playerTitle = QHBoxLayout()
        playerTitle.setContentsMargins(0, 0, 0, 15)
        self.playerName = QLabel(name)
        self.playerName.setStyleSheet("font-size:18px;")

        self.turnIcon = QLabel()
        playerTitle.addWidget(self.playerName)
        playerTitle.addWidget(self.turnIcon)
        playerTitle.setStretch(0, 1)
        self.addLayout(playerTitle)

        self.capturedPieces = QGridLayout()
        self.addLayout(self.capturedPieces)
