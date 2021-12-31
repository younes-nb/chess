from src.Controller.main_controller import MainController
from src.View.start_view import StartView


class StartController(StartView):
    def __init__(self):
        super(StartController, self).__init__()
        self.main_controller = MainController("White", "Black")
        self.play_button.clicked.connect(self.init_play_button)

    def init_play_button(self):
        white_name = "White"
        black_name = "black"
        if self.white_player_name.text():
            white_name = self.white_player_name.text()
        if self.black_player_name.text():
            black_name = self.black_player_name.text()

        self.main_controller = MainController(white_name, black_name)
        self.main_controller.show()
        self.hide()
