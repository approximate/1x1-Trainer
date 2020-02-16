from random import randint
#from PySide2 import QtCore, QtGui
#from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt)
#from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    #QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    #QRadialGradient)
# from PySide2.QtWidgets import *

from gui import Ui_MainWindow
#import sys

score = 0


import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
#from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

while False:
    a = randint(1, 10)
    b = randint(1, 10)
    d = (a * b)
    print(a, 'x', b, '= ', end='')
    c = int(input(''))
    if c == d:
        print('Right!')
        score += 1
    else:
        print('Game Over')
        print("Scores =", score)
        break


