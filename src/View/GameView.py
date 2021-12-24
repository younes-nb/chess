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
from src.Model.Piece import Piece
from src.View.InfoView import InfoView


class GameView(QWidget):
    def __init__(self):
        super().__init__()
        self.selectedPiece = None
        self.turn = "White"

        self.layout = QHBoxLayout(self)
        self.board = QGridLayout()
        self.board.setSpacing(0)
        self.board.setContentsMargins(0, 0, 0, 0)
        self.layout.addLayout(self.board)
        self.layout.addSpacing(20)

        self.pieces = self.createBoard()
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

    def createBoard(self):
        pieces = [
            [Rook(self, 0, 0, "Black"), Knight(self, 0, 1, "Black"),
             Bishop(self, 0, 2, "Black"), Queen(self, 0, 3, "Black"),
             King(self, 0, 4, "Black"), Bishop(self, 0, 5, "Black"),
             Knight(self, 0, 6, "Black"), Rook(self, 0, 7, "Black")],
            [Pawn(self, 1, 0, "Black"), Pawn(self, 1, 1, "Black"),
             Pawn(self, 1, 2, "Black"), Pawn(self, 1, 3, "Black"),
             Pawn(self, 1, 4, "Black"), Pawn(self, 1, 5, "Black"),
             Pawn(self, 1, 6, "Black"), Pawn(self, 1, 7, "Black")],
            [Blank(self, 2, 0), Blank(self, 2, 1), Blank(self, 2, 2), Blank(self, 2, 3),
             Blank(self, 2, 4), Blank(self, 2, 5), Blank(self, 2, 6), Blank(self, 2, 7)],
            [Blank(self, 3, 0), Blank(self, 3, 1), Blank(self, 3, 2), Blank(self, 3, 3),
             Blank(self, 3, 4), Blank(self, 3, 5), Blank(self, 3, 6), Blank(self, 3, 7)],
            [Blank(self, 4, 0), Blank(self, 4, 1), Blank(self, 4, 2), Blank(self, 4, 3),
             Blank(self, 4, 4), Blank(self, 4, 5), Blank(self, 4, 6), Blank(self, 4, 7)],
            [Blank(self, 5, 0), Blank(self, 5, 1), Blank(self, 5, 2), Blank(self, 5, 3),
             Blank(self, 5, 4), Blank(self, 5, 5), Blank(self, 5, 6), Blank(self, 5, 7)],
            [Pawn(self, 6, 0, "White"), Pawn(self, 6, 1, "White"),
             Pawn(self, 6, 2, "White"), Pawn(self, 6, 3, "White"),
             Pawn(self, 6, 4, "White"), Pawn(self, 6, 5, "White"),
             Pawn(self, 6, 6, "White"), Pawn(self, 6, 7, "White")],
            [Rook(self, 7, 0, "White"), Knight(self, 7, 1, "White"),
             Bishop(self, 7, 2, "White"), Queen(self, 7, 3, "White"),
             King(self, 7, 4, "White"), Bishop(self, 7, 5, "White"),
             Knight(self, 7, 6, "White"), Rook(self, 7, 7, "White")]
        ]
        return pieces

    def setTurnIcon(self, whiteTurnIcon: QPixmap, blackTurnIcon: QPixmap):
        self.infoWhite.turnIcon.setPixmap(whiteTurnIcon)
        self.infoBlack.turnIcon.setPixmap(blackTurnIcon)

    def addOutPieceWhite(self, row, column, pieceIcon: QPixmap):
        outPiece = QLabel()
        outPiece.setPixmap(pieceIcon)
        self.infoBlack.outPieces.addWidget(outPiece, row, column)

    def selectPiece(self, piece):
        if self.turn == piece.team and piece.type != "Blank":
            if self.selectedPiece and self.selectedPiece != piece:
                self.selectedPiece.selected = False
                self.unPaint()
                self.selectedPiece.update()
            if piece.selected:
                piece.selected = False
                self.selectedPiece = None
                self.unPaint()
                piece.update()
            else:
                self.selectedPiece = piece
                self.selectedPiece.selected = True
                self.paint()
                self.selectedPiece.update()

    def movePiece(self, target: Piece):

        self.board.removeWidget(target)
        self.board.removeWidget(self.selectedPiece)
        target.position, self.selectedPiece.position = self.selectedPiece.position, target.position
        self.board.addWidget(target, target.position[0], target.position[1])
        self.board.addWidget(self.selectedPiece, self.selectedPiece.position[0], self.selectedPiece.position[1])

        self.pieces[target.position[0]][target.position[1]], \
        self.pieces[self.selectedPiece.position[0]][self.selectedPiece.position[1]] = \
            self.pieces[self.selectedPiece.position[0]][self.selectedPiece.position[1]], \
            self.pieces[target.position[0]][target.position[1]]

        self.unPaint()
        self.selectedPiece.selected = False
        target.update()
        self.selectedPiece.update()
        self.selectedPiece = None
        self.board.update()
        match self.turn:
            case "White":
                self.turn = "Black"
            case "Black":
                self.turn = "White"
        self.update()
        if target.team != "None":
            self.capturePiece(target)

    def capturePiece(self, piece: Piece):
        blank = Blank(self, piece.position[0], piece.position[1])
        self.pieces[blank.position[0]][blank.position[1]] = blank
        self.board.removeWidget(piece)
        self.board.addWidget(blank, blank.position[0], blank.position[1])
        self.board.update()
        piece.destroy(False, False)
        piece.update()
        blank.update()

    def paint(self):
        if self.selectedPiece:
            movements = self.selectedPiece.allMoves()
            for movement in movements:
                self.pieces[movement[0]][movement[1]].isPainted = True
                self.pieces[movement[0]][movement[1]].update()

    def unPaint(self):
        for i in self.pieces:
            for piece in i:
                piece.isPainted = False
                piece.update()
