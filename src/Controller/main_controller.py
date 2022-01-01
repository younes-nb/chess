from src.Controller.game_controller import GameController
from src.Controller.movements import Movements
from src.Model.bishop import Bishop
from src.Model.knight import Knight
from src.Model.pawn import Pawn
from src.Model.queen import Queen
from src.Model.rook import Rook
from src.Model.movement import Movement
from src.View.main_view import MainView


class MainController(MainView):
    def __init__(self, white_name, black_name, start_page):
        super(MainController, self).__init__()
        self.start_page = start_page
        self.white_name = white_name
        self.black_name = black_name
        self.game = GameController(self, self.white_name, self.black_name)
        self.setCentralWidget(self.game)
        self.movements = Movements()
        self.init_actions()

    def init_actions(self):
        self.undo.triggered.connect(self.undo_move)
        self.redo.triggered.connect(self.redo_move)
        self.reset.triggered.connect(self.reset_game)
        self.back.triggered.connect(self.back_to_start)
        self.exit.triggered.connect(self.exit_game)

    def undo_move(self):
        movement: Movement = self.movements.undo()
        if movement is not None:
            piece = self.game.pieces[movement.destination[0]][movement.destination[1]]
            target = self.game.pieces[movement.source[0]][movement.source[1]]
            if movement.captured is not None:
                captured = None
                self.game.move_piece(target, piece, True)
                team = str()
                match movement.captured[0]:
                    case 'W':
                        team = "White"
                        self.game.info_white.removeWidget(self.game.captured_pieces_white[-1])
                        self.game.captured_pieces_white.remove(self.game.captured_pieces_white[-1])
                        self.game.info_white.captured_y -= 1
                        if self.game.info_white.captured_y < 0:
                            self.game.info_white.captured_x -= 1
                            self.game.info_white.captured_y = 3

                    case 'B':
                        team = "Black"
                        self.game.info_black.removeWidget(self.game.captured_pieces_black[-1])
                        self.game.captured_pieces_black.remove(self.game.captured_pieces_black[-1])
                        self.game.info_black.captured_y -= 1
                        if self.game.info_black.captured_y < 0:
                            self.game.info_black.captured_x -= 1
                            self.game.info_black.captured_y = 3

                match movement.captured[1::]:
                    case "Queen":
                        captured = Queen(self.game, target.position[0], target.position[1], team)
                    case "Bishop":
                        captured = Bishop(self.game, target.position[0], target.position[1], team)
                    case "Knight":
                        captured = Knight(self.game, target.position[0], target.position[1], team)
                    case "Rook":
                        captured = Rook(self.game, target.position[0], target.position[1], team)
                    case "Pawn":
                        captured = Pawn(self.game, target.position[0], target.position[1], team)

                self.game.pieces[captured.position[0]][captured.position[1]] = captured
                self.game.board.removeWidget(target)
                self.game.board.addWidget(captured, captured.position[0], captured.position[1])
                self.game.board.update()
                target.update()
                captured.update()

            elif movement.promoted is not None:
                team = str()
                match movement.promoted[0]:
                    case 'W':
                        team = "White"
                    case 'B':
                        team = "Black"

                self.game.move_piece(target, piece, True)
                pawn = Pawn(self.game, piece.position[0], piece.position[1], team)
                self.game.pieces[pawn.position[0]][pawn.position[1]] = pawn
                self.game.board.removeWidget(piece)
                self.game.board.addWidget(pawn, pawn.position[0], pawn.position[1])
                self.game.board.update()
                piece.update()
                pawn.update()
                self.game.check()

            else:
                self.game.move_piece(target, piece, True)

    def redo_move(self):
        movement: Movement = self.movements.redo()
        if movement is not None:
            piece = self.game.pieces[movement.source[0]][movement.source[1]]
            target = self.game.pieces[movement.destination[0]][movement.destination[1]]
            if movement.promoted is not None:
                team = str()
                match movement.promoted[0]:
                    case 'W':
                        team = "White"
                    case 'B':
                        team = "Black"
                promoted = None
                match movement.promoted[1::]:
                    case "Queen":
                        promoted = Queen(self.game, piece.position[0], piece.position[1], team)

                self.game.pieces[promoted.position[0]][promoted.position[1]] = promoted
                self.game.board.removeWidget(piece)
                self.game.board.addWidget(promoted, promoted.position[0], promoted.position[1])
                self.game.board.update()
                self.game.move_piece(target, promoted, True)
            else:
                self.game.move_piece(target, piece, True)

    def reset_game(self):
        self.game = GameController(self, self.white_name, self.black_name)
        self.setCentralWidget(self.game)

    def back_to_start(self):
        self.close()
        self.start_page.show()

    def exit_game(self):
        self.close()
