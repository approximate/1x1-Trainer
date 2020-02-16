from random import randint
from gui import Ui_MainWindow
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.keyPressed = pyqtSignal(int)

    def keyPressEvent(self, event):
        super(MainWindow, self).keyPressEvent(event)
        self.keyPressed.emit(event.key())

app = QApplication(sys.argv)

score = 0

window = MainWindow()
window.show()

window.ui.GameOver.hide()

def keyPress():
    pass

window.ui.keyPressed.connect(keyPress)

while True:
    a = randint(1, 10)
    b = randint(1, 10)
    d = (a * b)
    LabelText = str(a) + ' x ' + str(b) + ' = '
    window.ui.Frage.setText(LabelText)
    window.ui.Score.setText(str(score))
    window.ui.Antwort.setText('')
    # c = int(input(''))
    c = 0
    if c == d:
        # print('Right!')
        score += 1
    else:
        window.ui.GameOver.show()
        break


sys.exit(app.exec_())
