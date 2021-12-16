from PyQt6.QtWidgets import QWidget


class View(QWidget):
    def __init__(self):
        super().__init__()
        self.move(100, 100)
        self.setFixedSize(800, 600)
        self.setWindowTitle("Chess")
