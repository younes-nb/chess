import os
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QMenuBar, QMenu
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt
from .GameView import GameView
from res import resource_path


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowState(Qt.WindowState.WindowMaximized)
        self.setWindowTitle("Chess")
        self.setWindowIcon(QIcon(resource_path("Images/icon.png")))
        self.gameView = GameView()
        self.setCentralWidget(self.gameView)

        menuBar = self.menuBar()
        options = menuBar.addMenu("Options")

        self.undo = QAction(QIcon(resource_path("Images/undo.png")), "Undo")
        self.undo.setShortcut("Ctrl+Z")
        options.addAction(self.undo)

        self.redo = QAction(QIcon(resource_path("Images/redo.png")), "Redo")
        self.redo.setShortcut("Ctrl+Y")
        options.addAction(self.redo)

        self.reset = QAction(QIcon(resource_path("Images/reset.png")), "Reset")
        self.reset.setShortcut("Ctrl+R")
        options.addAction(self.reset)

        self.exit = QAction(QIcon(resource_path("Images/exit.png")), "Exit")
        options.addAction(self.exit)
