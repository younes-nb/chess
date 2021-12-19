from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from src.Model.Bishop import Bishop
from src.Model.Blank import Blank
from src.Model.Knight import Knight
from src.Model.Pawn import Pawn
from src.Model.Queen import Queen
from src.Model.Rook import Rook
from src.Model.King import King
from src.View.InfoView import InfoView


def createBoard():
    pieces = [
        [Rook(0, 0, "Black"), Knight(0, 1, "Black"), Bishop(0, 2, "Black"), Queen(0, 3, "Black"),
         King(0, 4, "Black"), Bishop(0, 5, "Black"), Knight(0, 6, "Black"), Rook(0, 7, "Black")],
        [Pawn(1, 0, "Black"), Pawn(1, 1, "Black"), Pawn(1, 2, "Black"), Pawn(1, 3, "Black"),
         Pawn(1, 4, "Black"), Pawn(1, 5, "Black"), Pawn(1, 6, "Black"), Pawn(1, 7, "Black")],
        [Blank(2, 0), Blank(2, 1), Blank(2, 2), Blank(2, 3), Blank(2, 4), Blank(2, 5), Blank(2, 6), Blank(2, 7)],
        [Blank(3, 0), Blank(3, 1), Blank(3, 2), Blank(3, 3), Blank(3, 4), Blank(3, 5), Blank(3, 6), Blank(3, 7)],
        [Blank(4, 0), Blank(4, 1), Blank(4, 2), Blank(4, 3), Blank(4, 4), Blank(4, 5), Blank(4, 6), Blank(4, 7)],
        [Blank(5, 0), Blank(5, 1), Blank(5, 2), Blank(5, 3), Blank(5, 4), Blank(5, 5), Blank(5, 6), Blank(5, 7)],
        [Pawn(6, 0, "White"), Pawn(6, 1, "White"), Pawn(6, 2, "White"), Pawn(6, 3, "White"),
         Pawn(6, 4, "White"), Pawn(6, 5, "White"), Pawn(6, 6, "White"), Pawn(6, 7, "White")],
        [Rook(7, 0, "White"), Knight(7, 1, "White"), Bishop(7, 2, "White"), Queen(7, 3, "White"),
         King(7, 4, "White"), Bishop(7, 5, "White"), Knight(7, 6, "White"), Rook(7, 7, "White")]
    ]
    return pieces


class GameView(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.board = QGridLayout()
        self.board.setSpacing(0)
        self.board.setContentsMargins(0, 0, 0, 0)
        self.layout.addLayout(self.board)
        self.layout.addSpacing(20)

        self.pieces = createBoard()
        for x in range(8):
            for y in range(8):
                self.board.addWidget(self.pieces[x][y], x, y)

        infoContainer = QVBoxLayout()
        infoContainer.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.infoWhite = InfoView("White")
        self.infoBlack = InfoView("Black")
        self.infoBlack.setContentsMargins(0, 30, 0, 0)

        infoContainer.addLayout(self.infoWhite)
        infoContainer.addLayout(self.infoBlack)
        self.layout.addLayout(infoContainer)
        self.layout.setStretch(0, 1)

    def setTurnIcon(self, whiteTurnIcon: QPixmap, blackTurnIcon: QPixmap):
        self.infoWhite.turnIcon.setPixmap(whiteTurnIcon)
        self.infoBlack.turnIcon.setPixmap(blackTurnIcon)

    def addOutPieceWhite(self, row, column, pieceIcon: QPixmap):
        outPiece = QLabel()
        outPiece.setPixmap(pieceIcon)
        self.infoBlack.outPieces.addWidget(outPiece, row, column)
