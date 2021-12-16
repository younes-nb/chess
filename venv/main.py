import sys
from PyQt6.QtWidgets import QApplication
from Controller.Controller import Controller


def main():
    app = QApplication(sys.argv)
    window = Controller()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
