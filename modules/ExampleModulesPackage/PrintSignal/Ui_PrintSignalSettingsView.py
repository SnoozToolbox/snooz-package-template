# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_PrintSignalSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_PrintSignalSettingsView(object):
    def setupUi(self, PrintSignalSettingsView):
        if not PrintSignalSettingsView.objectName():
            PrintSignalSettingsView.setObjectName(u"PrintSignalSettingsView")
        PrintSignalSettingsView.resize(838, 333)
        self.verticalLayout = QVBoxLayout(PrintSignalSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(PrintSignalSettingsView)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.signal_horizontalLayout = QHBoxLayout()
        self.signal_horizontalLayout.setObjectName(u"signal_horizontalLayout")
        self.filename_label = QLabel(PrintSignalSettingsView)
        self.filename_label.setObjectName(u"filename_label")

        self.signal_horizontalLayout.addWidget(self.filename_label)

        self.filename_lineedit = QLineEdit(PrintSignalSettingsView)
        self.filename_lineedit.setObjectName(u"filename_lineedit")

        self.signal_horizontalLayout.addWidget(self.filename_lineedit)

        self.choose_pushButton = QPushButton(PrintSignalSettingsView)
        self.choose_pushButton.setObjectName(u"choose_pushButton")

        self.signal_horizontalLayout.addWidget(self.choose_pushButton)


        self.verticalLayout.addLayout(self.signal_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(PrintSignalSettingsView)
        self.choose_pushButton.clicked.connect(PrintSignalSettingsView.choose_filename)

        QMetaObject.connectSlotsByName(PrintSignalSettingsView)
    # setupUi

    def retranslateUi(self, PrintSignalSettingsView):
        PrintSignalSettingsView.setWindowTitle(QCoreApplication.translate("PrintSignalSettingsView", u"Form", None))
        self.label.setText(QCoreApplication.translate("PrintSignalSettingsView", u"Please select the file where the signal will be saved.", None))
        self.filename_label.setText(QCoreApplication.translate("PrintSignalSettingsView", u"Output filename:", None))
        self.choose_pushButton.setText(QCoreApplication.translate("PrintSignalSettingsView", u"Choose", None))
    # retranslateUi

