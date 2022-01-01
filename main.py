###########################################################
# File Purpose : To call the pyQt Application
# Techs : Qt Designer and Pyside6
# Version : v1.0.1
###########################################################

import sys
import platform
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, QEvent)
from PySide2.QtGui import (QColor, QBrush, QConicalGradient, QCursor, QFont, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

#GUI FILE
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
    """
    Python-GUI-Pomodoro-Clock
    ...

    Attributes :
    -------------
    NA

    Methods :
    -------------
    NA

    """

    def __init__(self):
        """

        Parameters:

        """
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Calling MainWindow to render the Widget
    window = MainWindow()
    sys.exit(app.exec_())
