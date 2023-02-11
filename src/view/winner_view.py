from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QMovie
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from src.res import resource_path


class WinnerView(QWidget):
    def __init__(self):
        super(WinnerView, self).__init__()
        self.layout = QVBoxLayout(self)
        self.name = "None"
        self.setWindowTitle("{} Won!".format(self.name))
        self.setWindowIcon(QIcon(resource_path("icons/icon.png")))

        label = QLabel("Winner Winner Chicken Dinner!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 20px;")

        trophy = QLabel()
        trophy.setAlignment(Qt.AlignmentFlag.AlignCenter)
        trophy.setContentsMargins(0, 20, 0, 20)
        trophy_gif = QMovie(resource_path("icons/trophy.gif"))
        trophy.setMovie(trophy_gif)
        trophy_gif.start()

        self.reset_button = QPushButton("Reset Game")
        self.reset_button.setStyleSheet("font-size: 18px;")
        self.layout.addWidget(label)
        self.layout.addWidget(trophy)
        self.layout.addWidget(self.reset_button)
        self.layout.addStretch(1)

    def set_name(self, name):
        self.name = name
        self.setWindowTitle("{} Won!".format(self.name))
