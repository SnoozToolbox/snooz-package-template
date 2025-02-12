# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_YasaSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_YasaSettingsView(object):
    def setupUi(self, YasaSettingsView):
        if not YasaSettingsView.objectName():
            YasaSettingsView.setObjectName(u"YasaSettingsView")
        YasaSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        YasaSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(YasaSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.raw_horizontalLayout = QHBoxLayout()
        self.raw_horizontalLayout.setObjectName(u"raw_horizontalLayout")
        self.raw_label = QLabel(YasaSettingsView)
        self.raw_label.setObjectName(u"raw_label")

        self.raw_horizontalLayout.addWidget(self.raw_label)

        self.raw_lineedit = QLineEdit(YasaSettingsView)
        self.raw_lineedit.setObjectName(u"raw_lineedit")

        self.raw_horizontalLayout.addWidget(self.raw_lineedit)


        self.verticalLayout.addLayout(self.raw_horizontalLayout)

        self.hpy_horizontalLayout = QHBoxLayout()
        self.hpy_horizontalLayout.setObjectName(u"hpy_horizontalLayout")
        self.hpy_label = QLabel(YasaSettingsView)
        self.hpy_label.setObjectName(u"hpy_label")

        self.hpy_horizontalLayout.addWidget(self.hpy_label)

        self.hpy_lineedit = QLineEdit(YasaSettingsView)
        self.hpy_lineedit.setObjectName(u"hpy_lineedit")

        self.hpy_horizontalLayout.addWidget(self.hpy_lineedit)


        self.verticalLayout.addLayout(self.hpy_horizontalLayout)

        self.additional_horizontalLayout = QHBoxLayout()
        self.additional_horizontalLayout.setObjectName(u"additional_horizontalLayout")
        self.additional_label = QLabel(YasaSettingsView)
        self.additional_label.setObjectName(u"additional_label")

        self.additional_horizontalLayout.addWidget(self.additional_label)

        self.additional_lineedit = QLineEdit(YasaSettingsView)
        self.additional_lineedit.setObjectName(u"additional_lineedit")

        self.additional_horizontalLayout.addWidget(self.additional_lineedit)


        self.verticalLayout.addLayout(self.additional_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(YasaSettingsView)

        QMetaObject.connectSlotsByName(YasaSettingsView)
    # setupUi

    def retranslateUi(self, YasaSettingsView):
        YasaSettingsView.setWindowTitle(QCoreApplication.translate("YasaSettingsView", u"Form", None))
        self.raw_label.setText(QCoreApplication.translate("YasaSettingsView", u"raw", None))
        self.hpy_label.setText(QCoreApplication.translate("YasaSettingsView", u"hpy", None))
        self.additional_label.setText(QCoreApplication.translate("YasaSettingsView", u"additional", None))
    # retranslateUi

