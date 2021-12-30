from src.View.main_view import MainView
from src.Controller.game_controller import GameController


class MainController(MainView):
    def __init__(self, white_name, black_name):
        super().__init__()
        self.white_name = white_name
        self.black_name = black_name
        self.game = GameController(self, self.white_name, self.black_name)
        self.setCentralWidget(self.game)

    def reset_game(self):
        self.game = GameController(self, self.white_name, self.black_name)
        self.setCentralWidget(self.game)
