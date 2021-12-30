from src.View.winner_view import WinnerView


class WinnerController(WinnerView):
    def __init__(self, game):
        super(WinnerController, self).__init__()
        self.game = game
        self.reset_button.clicked.connect(self.init_reset_button)

    def init_reset_button(self):
        self.game.controller.reset_game()
        self.close()
