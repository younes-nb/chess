from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from src.Model.bishop import Bishop
from src.Model.blank import Blank
from src.Model.knight import Knight
from src.Model.pawn import Pawn
from src.Model.queen import Queen
from src.Model.rook import Rook
from src.Model.king import King
from src.Model.piece import Piece
from src.View.info import Info
from src.res import resource_path


class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.black_king = King(self, 0, 4, "Black")
        self.white_king = King(self, 7, 4, "White")
        self.selected_piece = None
        self.turn = "White"

        self.layout = QHBoxLayout(self)
        self.board = QGridLayout()
        self.board.setSpacing(0)
        self.board.setContentsMargins(0, 0, 0, 0)
        self.layout.addLayout(self.board)
        self.layout.addSpacing(20)

        self.pieces = self.create_board()
        for x in range(8):
            for y in range(8):
                self.board.addWidget(self.pieces[x][y], x, y)

        info_container = QVBoxLayout()
        info_container.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.info_white = Info("White")
        self.info_black = Info("Black")
        self.info_black.setContentsMargins(0, 35, 0, 15)
        info_container.addLayout(self.info_white)
        info_container.addLayout(self.info_black)
        self.layout.addLayout(info_container)
        self.layout.setStretch(0, 1)
        self.set_turn_icon(QPixmap(resource_path("Icons/turn.png")), QPixmap(resource_path("Icons/turn-blank.png")))
        self.info_white.turn_icon.setToolTip("It's your turn!")
        self.info_black.turn_icon.setToolTip("Wait!")

    def create_board(self):
        pieces = [
            [Rook(self, 0, 0, "Black"), Knight(self, 0, 1, "Black"),
             Bishop(self, 0, 2, "Black"), Queen(self, 0, 3, "Black"),
             self.black_king, Bishop(self, 0, 5, "Black"),
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
             self.white_king, Bishop(self, 7, 5, "White"),
             Knight(self, 7, 6, "White"), Rook(self, 7, 7, "White")]
        ]
        return pieces

    def set_turn_icon(self, white_turn_icon: QPixmap, black_turn_icon: QPixmap):
        self.info_white.turn_icon.setPixmap(white_turn_icon)
        self.info_black.turn_icon.setPixmap(black_turn_icon)
        self.info_white.turn_icon.update()
        self.info_black.turn_icon.update()

    def select_piece(self, piece):
        if self.turn == piece.team and piece.type != "Blank":
            if self.selected_piece and self.selected_piece != piece:
                self.selected_piece.selected = False
                self.un_paint()
                self.selected_piece.update()
            if piece.selected:
                piece.selected = False
                self.selected_piece = None
                self.un_paint()
                piece.update()
            else:
                self.selected_piece = piece
                self.selected_piece.selected = True
                self.paint()
                self.selected_piece.update()

    def change_turn(self):
        match self.turn:
            case "White":
                self.turn = "Black"
                self.info_black.turn_icon.setToolTip("It's your turn!")
                self.info_white.turn_icon.setToolTip("Wait!")
                self.set_turn_icon(QPixmap(resource_path("Icons/turn-blank.png")),
                                   QPixmap(resource_path("Icons/turn.png")))

            case "Black":
                self.turn = "White"
                self.info_white.turn_icon.setToolTip("It's your turn!")
                self.info_black.turn_icon.setToolTip("Wait!")
                self.set_turn_icon(QPixmap(resource_path("Icons/turn.png")),
                                   QPixmap(resource_path("Icons/turn-blank.png")))

    def move_piece(self, target: Piece):
        self.board.removeWidget(target)
        self.board.removeWidget(self.selected_piece)
        target.position, self.selected_piece.position = self.selected_piece.position, target.position
        self.board.addWidget(target, target.position[0], target.position[1])
        self.board.addWidget(self.selected_piece, self.selected_piece.position[0], self.selected_piece.position[1])

        self.pieces[target.position[0]][target.position[1]], \
        self.pieces[self.selected_piece.position[0]][self.selected_piece.position[1]] = \
            self.pieces[self.selected_piece.position[0]][self.selected_piece.position[1]], \
            self.pieces[target.position[0]][target.position[1]]

        self.un_paint()
        self.selected_piece.selected = False
        target.update()
        self.selected_piece.update()
        self.selected_piece = None
        self.board.update()
        if target.team != "None":
            self.capture_piece(target)
        self.check()
        self.change_turn()
        self.update()

    def capture_piece(self, piece: Piece):
        blank = Blank(self, piece.position[0], piece.position[1])
        self.pieces[blank.position[0]][blank.position[1]] = blank
        self.board.removeWidget(piece)
        self.board.addWidget(blank, blank.position[0], blank.position[1])
        self.board.update()
        self.add_captured_piece_icon(piece.type)
        piece.destroy(False, False)
        piece.update()
        blank.update()

    def add_captured_piece_icon(self, piece):
        captured_label = QLabel()
        if piece[0] == 'W':
            match piece:
                case "WQueen":
                    captured_label.setPixmap(QPixmap(resource_path("Pieces/out-white-queen.png")))
                case "WBishop":
                    captured_label.setPixmap(QPixmap(resource_path("Pieces/out-white-bishop.png")))
                case "WKnight":
                    captured_label.setPixmap(QPixmap(resource_path("Pieces/out-white-knight.png")))
                case "WRook":
                    captured_label.setPixmap(QPixmap(resource_path("Pieces/out-white-rook.png")))
                case "WPawn":
                    captured_label.setPixmap(QPixmap(resource_path("Pieces/out-white-pawn.png")))

            self.info_white.captured_pieces.addWidget(captured_label, self.info_white.captured_x,
                                                      self.info_white.captured_y)
            self.info_white.captured_y += 1
            if self.info_white.captured_y > 2:
                self.info_white.captured_x += 1
                self.info_white.captured_y = 0
            self.info_white.captured_pieces.update()
        elif piece[0] == 'B':
            match piece:
                case "BQueen":
                    captured_label.setPixmap(QPixmap(resource_path("Pieces/out-black-queen.png")))
                case "BBishop":
                    captured_label.setPixmap(QPixmap(resource_path("Pieces/out-black-bishop.png")))
                case "BKnight":
                    captured_label.setPixmap(QPixmap(resource_path("Pieces/out-black-knight.png")))
                case "BRook":
                    captured_label.setPixmap(QPixmap(resource_path("Pieces/out-black-rook.png")))
                case "BPawn":
                    captured_label.setPixmap(QPixmap(resource_path("Pieces/out-black-pawn.png")))

            self.info_black.captured_pieces.addWidget(captured_label, self.info_black.captured_x,
                                                      self.info_black.captured_y)
            self.info_black.captured_y += 1
            if self.info_black.captured_y > 2:
                self.info_black.captured_x += 1
                self.info_black.captured_y = 0
            self.info_black.captured_pieces.update()

    def check(self):
        try:
            opponent_king = self.checked_king(True)
            king = self.checked_king(False)
            found_opponent_king = False
            found_king = False
            for row in self.pieces:
                if found_opponent_king:
                    break
                for piece in row:
                    if found_opponent_king:
                        break
                    if piece.team != self.turn and piece.team != "None":
                        for movement in piece.all_moves():
                            if self.pieces[movement[0]][movement[1]].type == king.type:
                                found_king = True
                    if piece.team == self.turn:
                        for movement in piece.all_moves():
                            if self.pieces[movement[0]][movement[1]].type == opponent_king.type:
                                found_opponent_king = True
                                opponent_king.is_checked = True
                                opponent_king.update()
                                break
            if not found_opponent_king:
                opponent_king.is_checked = False
                opponent_king.update()
            if not found_king:
                king.is_checked = False
                king.update()

        except Exception as e:
            print(e.__str__())

    def checked_king(self, check):
        if check:
            match self.turn:
                case "White":
                    return self.black_king
                case "Black":
                    return self.white_king
        else:
            match self.turn:
                case "White":
                    return self.white_king
                case "Black":
                    return self.black_king

    def paint(self):
        if self.selected_piece:
            movements = self.selected_piece.all_moves()
            for movement in movements:
                self.pieces[movement[0]][movement[1]].is_painted = True
                self.pieces[movement[0]][movement[1]].update()

    def un_paint(self):
        for i in self.pieces:
            for piece in i:
                piece.is_painted = False
                piece.update()
