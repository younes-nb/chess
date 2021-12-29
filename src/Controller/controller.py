from src.View.view import View
from src.Controller.game_controller import GameController


class Controller(View):
    def __init__(self):
        super().__init__()
        self.game = GameController()
        self.setCentralWidget(self.game)
