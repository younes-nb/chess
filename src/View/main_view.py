from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QMainWindow
from src.res import resource_path


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 900, 700)
        self.setWindowTitle("Chess")
        self.setWindowIcon(QIcon(resource_path("Icons/icon.png")))

        menu_bar = self.menuBar()

        options = menu_bar.addMenu("Options")

        self.undo = QAction(QIcon(resource_path("Icons/undo.png")), "Undo")
        self.undo.setShortcut("Ctrl+Z")
        options.addAction(self.undo)

        self.redo = QAction(QIcon(resource_path("Icons/redo.png")), "Redo")
        self.redo.setShortcut("Ctrl+Y")
        options.addAction(self.redo)

        self.reset = QAction(QIcon(resource_path("Icons/reset.png")), "Reset")
        self.reset.setShortcut("Ctrl+R")
        options.addAction(self.reset)

        self.exit = QAction(QIcon(resource_path("Icons/exit.png")), "Exit")
        options.addAction(self.exit)
