# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Trainer.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(366, 283)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"  background-color: black\n"
"}\n"
"QLabel{\n"
"color: white\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Titel = QLabel(self.centralwidget)
        self.Titel.setObjectName(u"Titel")
        self.Titel.setGeometry(QRect(10, 0, 361, 81))
        font = QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Titel.setFont(font)
        self.Titel.setStyleSheet(u"")
        self.Titel.setAlignment(Qt.AlignCenter)
        self.Frage = QLabel(self.centralwidget)
        self.Frage.setObjectName(u"Frage")
        self.Frage.setGeometry(QRect(50, 80, 131, 41))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setWeight(50)
        self.Frage.setFont(font1)
        self.Frage.setAlignment(Qt.AlignCenter)
        self.GameOver = QLabel(self.centralwidget)
        self.GameOver.setObjectName(u"GameOver")
        self.GameOver.setGeometry(QRect(130, 120, 131, 71))
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.GameOver.setFont(font2)
        self.GameOver.setAlignment(Qt.AlignCenter)
        self.ScoreText = QLabel(self.centralwidget)
        self.ScoreText.setObjectName(u"ScoreText")
        self.ScoreText.setGeometry(QRect(50, 190, 91, 41))
        font3 = QFont()
        font3.setPointSize(16)
        self.ScoreText.setFont(font3)
        self.ScoreText.setAlignment(Qt.AlignCenter)
        self.Antwort = QLineEdit(self.centralwidget)
        self.Antwort.setObjectName(u"Antwort")
        self.Antwort.setGeometry(QRect(200, 80, 121, 41))
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        font4.setWeight(75)
        self.Antwort.setFont(font4)
        self.Score = QLabel(self.centralwidget)
        self.Score.setObjectName(u"Score")
        self.Score.setGeometry(QRect(170, 190, 111, 41))
        self.Score.setFont(font3)
        self.Score.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Titel.setText(QCoreApplication.translate("MainWindow", u"1x1 Trainer", None))
        self.Frage.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.GameOver.setText(QCoreApplication.translate("MainWindow", u"Game Over", None))
        self.ScoreText.setText(QCoreApplication.translate("MainWindow", u"Score =", None))
        self.Antwort.setText("")
        self.Score.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

