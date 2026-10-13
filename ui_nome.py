# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'salnomeANY.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_salvarnome(object):
    def setupUi(self, salvarnome):
        if not salvarnome.objectName():
            salvarnome.setObjectName(u"salvarnome")
        salvarnome.resize(211, 95)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(salvarnome.sizePolicy().hasHeightForWidth())
        salvarnome.setSizePolicy(sizePolicy)
        salvarnome.setMinimumSize(QSize(211, 95))
        salvarnome.setMaximumSize(QSize(211, 95))
        self.centralwidget = QWidget(salvarnome)
        self.centralwidget.setObjectName(u"centralwidget")
        self.nome = QLabel(self.centralwidget)
        self.nome.setObjectName(u"nome")
        self.nome.setGeometry(QRect(10, 10, 47, 13))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 30, 191, 20))
        self.salvar = QPushButton(self.centralwidget)
        self.salvar.setObjectName(u"salvar")
        self.salvar.setGeometry(QRect(10, 60, 191, 23))
        salvarnome.setCentralWidget(self.centralwidget)

        self.retranslateUi(salvarnome)

        QMetaObject.connectSlotsByName(salvarnome)
    # setupUi

    def retranslateUi(self, salvarnome):
        salvarnome.setWindowTitle(QCoreApplication.translate("salvarnome", u"Salvar Nome", None))
        self.nome.setText(QCoreApplication.translate("salvarnome", u"NOME:", None))
        self.salvar.setText(QCoreApplication.translate("salvarnome", u"SALVAR", None))
    # retranslateUi

