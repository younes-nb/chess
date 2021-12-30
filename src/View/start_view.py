from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit

from src.res import resource_path


class StartView(QWidget):
    def __init__(self):
        super(StartView, self).__init__()
        self.setWindowTitle("Chess")
        self.setWindowIcon(QIcon(resource_path("Icons/icon.png")))

        self.layout = QVBoxLayout(self)

        self.start_image = QLabel()
        self.start_image.setPixmap(QPixmap(resource_path("Icons/start-image.png")))
        self.start_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.start_image.setContentsMargins(0, 10, 0, 30)

        white_player_image = QLabel()
        white_player_image.setPixmap(QPixmap(resource_path("Icons/white-player.png")))

        self.white_player_name = QLineEdit("White")
        self.white_player_name.setPlaceholderText("Please Enter Your Name")
        self.white_player_name.setStyleSheet("font-size: 16px;padding: 5px")

        white_player_container = QHBoxLayout()
        white_player_container.setContentsMargins(0, 0, 0, 20)
        white_player_container.addWidget(white_player_image)
        white_player_container.addWidget(self.white_player_name)

        black_player_image = QLabel()
        black_player_image.setPixmap(QPixmap(resource_path("Icons/black-player.png")))

        self.black_player_name = QLineEdit("Black")
        self.black_player_name.setPlaceholderText("Please Enter Your Name")
        self.black_player_name.setStyleSheet("font-size: 16px;padding: 5px")

        black_player_container = QHBoxLayout()
        black_player_container.setContentsMargins(0, 0, 0, 20)
        black_player_container.addWidget(black_player_image)
        black_player_container.addWidget(self.black_player_name)

        self.play_button = QPushButton("Play")
        self.play_button.setStyleSheet("font-size: 18px;")

        self.layout.addWidget(self.start_image)
        self.layout.addLayout(white_player_container)
        self.layout.addLayout(black_player_container)
        self.layout.addWidget(self.play_button)
