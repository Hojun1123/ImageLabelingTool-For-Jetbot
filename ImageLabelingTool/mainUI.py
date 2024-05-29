# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'p1.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QListView, QMainWindow, QMenuBar,
    QSizePolicy, QSlider, QSpinBox, QStatusBar, QListWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(989, 667)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.spinBox_2 = QSpinBox(self.centralwidget)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.gridLayout.addWidget(self.spinBox_2, 1, 2, 1, 1)

        self.imageArea = QFrame(self.centralwidget)
        self.imageArea.setObjectName(u"imageArea")
        self.imageArea.setMinimumSize(QSize(448, 448))
        self.imageArea.setMaximumSize(QSize(448, 448))
        self.imageArea.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.imageArea.setFrameShape(QFrame.StyledPanel)
        self.imageArea.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.imageArea, 2, 1, 1, 3)

        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout.addWidget(self.spinBox, 0, 2, 1, 1)

        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")

        self.gridLayout.addWidget(self.label_1, 0, 1, 1, 1)

        self.bar_2 = QSlider(self.centralwidget)
        self.bar_2.setObjectName(u"bar_2")
        self.bar_2.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.bar_2, 1, 3, 1, 2)

        self.bar_1 = QSlider(self.centralwidget)
        self.bar_1.setObjectName(u"bar_1")
        self.bar_1.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.bar_1, 0, 3, 1, 2)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout.addWidget(self.listWidget, 2, 4, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 989, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.spinBox.valueChanged.connect(MainWindow.input1)
        self.spinBox_2.valueChanged.connect(MainWindow.input2)
        self.bar_1.valueChanged.connect(MainWindow.input1)
        self.bar_2.valueChanged.connect(MainWindow.input2)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Image Number", None))
    # retranslateUi

