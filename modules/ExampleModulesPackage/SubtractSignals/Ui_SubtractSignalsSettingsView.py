# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SubtractSignalsSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_SubtractSignalsSettingsView(object):
    def setupUi(self, SubtractSignalsSettingsView):
        if not SubtractSignalsSettingsView.objectName():
            SubtractSignalsSettingsView.setObjectName(u"SubtractSignalsSettingsView")
        SubtractSignalsSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        SubtractSignalsSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(SubtractSignalsSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_signal_horizontalLayout = QHBoxLayout()
        self.main_signal_horizontalLayout.setObjectName(u"main_signal_horizontalLayout")
        self.main_signal_label = QLabel(SubtractSignalsSettingsView)
        self.main_signal_label.setObjectName(u"main_signal_label")

        self.main_signal_horizontalLayout.addWidget(self.main_signal_label)

        self.main_signal_lineedit = QLineEdit(SubtractSignalsSettingsView)
        self.main_signal_lineedit.setObjectName(u"main_signal_lineedit")

        self.main_signal_horizontalLayout.addWidget(self.main_signal_lineedit)


        self.verticalLayout.addLayout(self.main_signal_horizontalLayout)

        self.signal_to_subtract_horizontalLayout = QHBoxLayout()
        self.signal_to_subtract_horizontalLayout.setObjectName(u"signal_to_subtract_horizontalLayout")
        self.signal_to_subtract_label = QLabel(SubtractSignalsSettingsView)
        self.signal_to_subtract_label.setObjectName(u"signal_to_subtract_label")

        self.signal_to_subtract_horizontalLayout.addWidget(self.signal_to_subtract_label)

        self.signal_to_subtract_lineedit = QLineEdit(SubtractSignalsSettingsView)
        self.signal_to_subtract_lineedit.setObjectName(u"signal_to_subtract_lineedit")

        self.signal_to_subtract_horizontalLayout.addWidget(self.signal_to_subtract_lineedit)


        self.verticalLayout.addLayout(self.signal_to_subtract_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(SubtractSignalsSettingsView)

        QMetaObject.connectSlotsByName(SubtractSignalsSettingsView)
    # setupUi

    def retranslateUi(self, SubtractSignalsSettingsView):
        SubtractSignalsSettingsView.setWindowTitle(QCoreApplication.translate("SubtractSignalsSettingsView", u"Form", None))
        self.main_signal_label.setText(QCoreApplication.translate("SubtractSignalsSettingsView", u"main_signal", None))
        self.signal_to_subtract_label.setText(QCoreApplication.translate("SubtractSignalsSettingsView", u"signal_to_subtract", None))
    # retranslateUi

