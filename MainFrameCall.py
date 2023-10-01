import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from HomeUI.HomePageForm import HomePageForm


if __name__ == '__main__':
    # windows专用参数
    # sys._enablelegacywindowsfsencoding()

    app = QApplication(sys.argv)
    main_frame = HomePageForm()
    main_frame.show()
    sys.exit(app.exec())

