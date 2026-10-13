# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainANYDESK.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(313, 308)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(313, 308))
        MainWindow.setMaximumSize(QSize(313, 308))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.txcon_1 = QLabel(self.centralwidget)
        self.txcon_1.setObjectName(u"txcon_1")
        self.txcon_1.setGeometry(QRect(20, 10, 281, 16))
        self.ipcon = QLineEdit(self.centralwidget)
        self.ipcon.setObjectName(u"ipcon")
        self.ipcon.setGeometry(QRect(20, 30, 171, 20))
        self.conectar = QPushButton(self.centralwidget)
        self.conectar.setObjectName(u"conectar")
        self.conectar.setGeometry(QRect(20, 60, 171, 23))
        self.table = QTableWidget(self.centralwidget)
        if (self.table.columnCount() < 2):
            self.table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(20, 121, 271, 161))
        self.zerar = QPushButton(self.centralwidget)
        self.zerar.setObjectName(u"zerar")
        self.zerar.setGeometry(QRect(20, 90, 171, 23))
        self.txcon_2 = QLabel(self.centralwidget)
        self.txcon_2.setObjectName(u"txcon_2")
        self.txcon_2.setGeometry(QRect(20, 10, 281, 16))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 100, 61, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 10, 47, 13))
        self.seuid = QLabel(self.centralwidget)
        self.seuid.setObjectName(u"seuid")
        self.seuid.setGeometry(QRect(200, 20, 61, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Anydesk Gestor", None))
        self.txcon_1.setText(QCoreApplication.translate("MainWindow", u"IP DE CONEX\u00c3O:", None))
        self.conectar.setText(QCoreApplication.translate("MainWindow", u"CONECTAR", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"IP", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        self.zerar.setText(QCoreApplication.translate("MainWindow", u"ZERAR TEMPO", None))
        self.txcon_2.setText(QCoreApplication.translate("MainWindow", u"CONECTANDO...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"By: Cronos", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"SeuID:", None))
        self.seuid.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">TextLabel</span></p></body></html>", None))
    # retranslateUi

