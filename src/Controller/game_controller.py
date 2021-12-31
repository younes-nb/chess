from functools import partial

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel

from src.Controller.winner_controller import WinnerController
from src.Model.bishop import Bishop
from src.Model.blank import Blank
from src.Model.king import King
from src.Model.knight import Knight
from src.Model.pawn import Pawn
from src.Model.piece import Piece
from src.Model.piece_copy import *
from src.Model.queen import Queen
from src.Model.rook import Rook
from src.View.game_view import GameView
from src.res import resource_path


class GameController(GameView):
    def __init__(self, controller, white_name, black_name):
        super().__init__(self.create_pieces(), white_name, black_name)
        self.controller = controller
        self.winner = WinnerController(self)
        self.winner.hide()
        self.promoted_pawn = None
        self.selected_piece = None
        self.turn = "White"
        self.init_promote_buttons()

    def create_pieces(self):
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

        self.pieces[target.position[0]][target.position[1]], self.pieces[self.selected_piece.position[0]][
            self.selected_piece.position[1]] = self.pieces[self.selected_piece.position[0]][
                                                   self.selected_piece.position[1]], self.pieces[target.position[0]][
                                                   target.position[1]]
        self.un_paint()
        self.selected_piece.selected = False
        target.update()
        self.selected_piece.update()

        if target.team != "None":
            self.capture_piece(target, True)

        self.promotion()
        self.check()
        self.selected_piece = None
        self.change_turn()
        self.board.update()
        self.update()

    def capture_piece(self, piece: Piece, add_icon):
        blank = Blank(self, piece.position[0], piece.position[1])
        self.pieces[blank.position[0]][blank.position[1]] = blank
        self.board.removeWidget(piece)
        self.board.addWidget(blank, blank.position[0], blank.position[1])
        self.board.update()
        if add_icon:
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
                    captured_label.setToolTip("Queen")
                case "WBishop":
                    captured_label.setPixmap(QPixmap(resource_path("Pieces/out-white-bishop.png")))
                    captured_label.setToolTip("Bishop")
                case "WKnight":
                    captured_label.setPixmap(QPixmap(resource_path("Pieces/out-white-knight.png")))
                    captured_label.setToolTip("Knight")
                case "WRook":
                    captured_label.setPixmap(QPixmap(resource_path("Pieces/out-white-rook.png")))
                    captured_label.setToolTip("Rook")
                case "WPawn":
                    captured_label.setPixmap(QPixmap(resource_path("Pieces/out-white-pawn.png")))
                    captured_label.setToolTip("Pawn")

            self.info_white.captured_pieces.addWidget(captured_label, self.info_white.captured_x,
                                                      self.info_white.captured_y)
            self.info_white.captured_y += 1
            if self.info_white.captured_y > 3:
                self.info_white.captured_x += 1
                self.info_white.captured_y = 0
            self.info_white.captured_pieces.update()
        elif piece[0] == 'B':
            match piece:
                case "BQueen":
                    captured_label.setPixmap(QPixmap(resource_path("Pieces/out-black-queen.png")))
                    captured_label.setToolTip("Queen")
                case "BBishop":
                    captured_label.setPixmap(QPixmap(resource_path("Pieces/out-black-bishop.png")))
                    captured_label.setToolTip("Bishop")
                case "BKnight":
                    captured_label.setPixmap(QPixmap(resource_path("Pieces/out-black-knight.png")))
                    captured_label.setToolTip("Knight")
                case "BRook":
                    captured_label.setPixmap(QPixmap(resource_path("Pieces/out-black-rook.png")))
                    captured_label.setToolTip("Rook")
                case "BPawn":
                    captured_label.setPixmap(QPixmap(resource_path("Pieces/out-black-pawn.png")))
                    captured_label.setToolTip("Pawn")
            self.info_black.captured_pieces.addWidget(captured_label, self.info_black.captured_x,
                                                      self.info_black.captured_y)
            self.info_black.captured_y += 1
            if self.info_black.captured_y > 3:
                self.info_black.captured_x += 1
                self.info_black.captured_y = 0
            self.info_black.captured_pieces.update()

    def check(self):
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
        self.board.update()

    def checked_king(self, check):
        white_king = None
        black_king = None
        for row in self.pieces:
            for piece in row:
                if piece.type == "WKing":
                    white_king = piece
                elif piece.type == "BKing":
                    black_king = piece
        if check:
            match self.turn:
                case "White":
                    return black_king
                case "Black":
                    return white_king
        else:
            match self.turn:
                case "White":
                    return white_king
                case "Black":
                    return black_king

    def check_mate(self):
        opponent_king = self.checked_king(False)
        mate = True
        for row in self.pieces:
            if not mate:
                break
            for piece in row:
                if not mate:
                    break
                self.selected_piece = piece
                if piece.team == opponent_king.team:
                    for movement in piece.all_moves():
                        if movement_validation(movement, self.create_copy()):
                            mate = False
                            break
        self.selected_piece = None
        if mate:
            for row in self.pieces:
                for piece in row:
                    if piece.team != opponent_king.team and piece.team != "None":
                        for movement in piece.all_moves():
                            if self.pieces[movement[0]][movement[1]].type == opponent_king.type:
                                piece.checker = True
                                piece.update()
                                break
            opponent_king.is_check_mate = True
            opponent_king.update()
            match opponent_king.team:
                case "White":
                    self.winner.set_name(self.black_name)
                case "Black":
                    self.winner.set_name(self.white_name)
            self.winner.update()
            self.winner.show()
        return mate

    def promotion(self):
        for row in self.pieces:
            for piece in row:
                if piece.type[1::] == "Pawn":
                    match piece.team:
                        case "White":
                            if piece.position[0] == 0:
                                self.promoted_pawn = piece
                                self.info_white.promotion_text.show()
                                self.info_white.queen.show()
                                self.info_white.bishop.show()
                                self.info_white.knight.show()
                                self.info_white.rook.show()
                                self.disable_board(True)

                        case "Black":
                            if piece.position[0] == 7:
                                self.promoted_pawn = piece
                                self.info_black.promotion_text.show()
                                self.info_black.queen.show()
                                self.info_black.bishop.show()
                                self.info_black.knight.show()
                                self.info_black.rook.show()
                                self.disable_board(True)

    def disable_board(self, disable: bool):
        for row in self.pieces:
            for piece in row:
                piece.setDisabled(disable)
                piece.update()

    def init_promote_buttons(self):
        self.info_white.queen.clicked.connect(partial(self.add_promoted, "Queen"))
        self.info_white.bishop.clicked.connect(partial(self.add_promoted, "Bishop"))
        self.info_white.knight.clicked.connect(partial(self.add_promoted, "Knight"))
        self.info_white.rook.clicked.connect(partial(self.add_promoted, "Rook"))
        self.info_black.queen.clicked.connect(partial(self.add_promoted, "Queen"))
        self.info_black.bishop.clicked.connect(partial(self.add_promoted, "Bishop"))
        self.info_black.knight.clicked.connect(partial(self.add_promoted, "Knight"))
        self.info_black.rook.clicked.connect(partial(self.add_promoted, "Rook"))

    def add_promoted(self, promoted):
        try:
            self.info_white.promotion_text.hide()
            self.info_white.queen.hide()
            self.info_white.bishop.hide()
            self.info_white.knight.hide()
            self.info_white.rook.hide()
            self.info_black.promotion_text.hide()
            self.info_black.queen.hide()
            self.info_black.bishop.hide()
            self.info_black.knight.hide()
            self.info_black.rook.hide()
            promoted_piece = None
            match promoted:
                case "Queen":
                    promoted_piece = Queen(self, self.promoted_pawn.position[0], self.promoted_pawn.position[1],
                                           self.promoted_pawn.team)
                case "Bishop":
                    promoted_piece = Bishop(self, self.promoted_pawn.position[0], self.promoted_pawn.position[1],
                                            self.promoted_pawn.team)
                case "Knight":
                    promoted_piece = Knight(self, self.promoted_pawn.position[0], self.promoted_pawn.position[1],
                                            self.promoted_pawn.team)
                case "Rook":
                    promoted_piece = Rook(self, self.promoted_pawn.position[0], self.promoted_pawn.position[1],
                                          self.promoted_pawn.team)

            self.pieces[promoted_piece.position[0]][promoted_piece.position[1]] = promoted_piece
            self.board.removeWidget(self.promoted_pawn)
            self.board.addWidget(promoted_piece, promoted_piece.position[0], promoted_piece.position[1])
            self.board.update()
            self.promoted_pawn.destroy(False, False)
            self.promoted_pawn.update()
            self.promoted_pawn = None
            self.disable_board(False)
            promoted_piece.update()
            opponent_king = self.checked_king(False)
            for movement in promoted_piece.all_moves():
                if self.pieces[movement[0]][movement[1]].type == opponent_king.type:
                    opponent_king.is_checked = True
                    opponent_king.update()
                    break

            self.update()
        except Exception as e:
            print(e)

    def paint(self):
        if self.selected_piece:
            movements = self.selected_piece.all_moves()
            for movement in movements:
                if movement_validation(movement, self.create_copy()):
                    if self.pieces[movement[0]][movement[1]].team != "None":
                        self.pieces[movement[0]][movement[1]].target = True
                    else:
                        self.pieces[movement[0]][movement[1]].is_painted = True
                    self.pieces[movement[0]][movement[1]].update()

    def un_paint(self):
        for i in self.pieces:
            for piece in i:
                piece.is_painted = False
                piece.target = False
                piece.update()

    def create_copy(self):
        pieces_copy = []
        for i in range(8):
            pieces_copy.append([])
            for j in range(8):
                pieces_copy[i].append(None)

        for row in self.pieces:
            for piece in row:
                x = piece.position[0]
                y = piece.position[1]
                match piece.type:
                    case "WKing":
                        pieces_copy[x][y] = KingCopy(pieces_copy, x, y, "White")
                    case "BKing":
                        pieces_copy[x][y] = KingCopy(pieces_copy, x, y, "Black")
                    case "WQueen":
                        pieces_copy[x][y] = QueenCopy(pieces_copy, x, y, "White")
                    case "BQueen":
                        pieces_copy[x][y] = QueenCopy(pieces_copy, x, y, "Black")
                    case "WBishop":
                        pieces_copy[x][y] = BishopCopy(pieces_copy, x, y, "White")
                    case "BBishop":
                        pieces_copy[x][y] = BishopCopy(pieces_copy, x, y, "Black")
                    case "WKnight":
                        pieces_copy[x][y] = KnightCopy(pieces_copy, x, y, "White")
                    case "BKnight":
                        pieces_copy[x][y] = KnightCopy(pieces_copy, x, y, "Black")
                    case "WRook":
                        pieces_copy[x][y] = RookCopy(pieces_copy, x, y, "White")
                    case "BRook":
                        pieces_copy[x][y] = RookCopy(pieces_copy, x, y, "Black")
                    case "WPawn":
                        pieces_copy[x][y] = PawnCopy(pieces_copy, x, y, "White")
                    case "BPawn":
                        pieces_copy[x][y] = PawnCopy(pieces_copy, x, y, "Black")
                    case "Blank":
                        pieces_copy[x][y] = BlankCopy(pieces_copy, x, y)

        for row in pieces_copy:
            for piece in row:
                if piece.position == self.selected_piece.position:
                    piece.selected = True
                    break
        return pieces_copy


def movement_validation(movement: tuple, pieces_copy: list):
    selected_piece = None
    for row in pieces_copy:
        for piece in row:
            if piece.selected:
                selected_piece = piece
    target = pieces_copy[movement[0]][movement[1]]
    target.position, selected_piece.position = selected_piece.position, target.position
    pieces_copy[target.position[0]][target.position[1]], \
    pieces_copy[selected_piece.position[0]][
        selected_piece.position[1]] = pieces_copy[selected_piece.position[0]][
                                          selected_piece.position[1]], \
                                      pieces_copy[target.position[0]][
                                          target.position[1]]
    if target.team != "None":
        pieces_copy[target.position[0]][target.position[1]] = BlankCopy(pieces_copy, target.position[0],
                                                                        target.position[1])
    king = None
    found = False
    for row in pieces_copy:
        if found:
            break
        for piece in row:
            if piece.team == selected_piece.team and piece.type[1::] == "King":
                king = piece
                found = True
                break

    for row in pieces_copy:
        for piece in row:
            if piece.team != selected_piece.team and piece.team != "None":
                for move in piece.all_moves():
                    if pieces_copy[move[0]][move[1]].type == king.type:
                        return False
    return True
