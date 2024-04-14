# EqualNine, 2023г

import sys
from PyQt5.QtWidgets import QApplication

from window import Window


if __name__ == '__main__':
    app = QApplication([])
    application = Window()
    application.show()

    sys.exit(app.exec())
