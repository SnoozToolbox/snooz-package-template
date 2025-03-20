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
        self.filename_horizontalLayout = QHBoxLayout()
        self.filename_horizontalLayout.setObjectName(u"filename_horizontalLayout")
        self.filename_label = QLabel(YasaSettingsView)
        self.filename_label.setObjectName(u"filename_label")

        self.filename_horizontalLayout.addWidget(self.filename_label)

        self.filename_lineedit = QLineEdit(YasaSettingsView)
        self.filename_lineedit.setObjectName(u"filename_lineedit")

        self.filename_horizontalLayout.addWidget(self.filename_lineedit)


        self.verticalLayout.addLayout(self.filename_horizontalLayout)

        self.signals_horizontalLayout = QHBoxLayout()
        self.signals_horizontalLayout.setObjectName(u"signals_horizontalLayout")
        self.signals_label = QLabel(YasaSettingsView)
        self.signals_label.setObjectName(u"signals_label")

        self.signals_horizontalLayout.addWidget(self.signals_label)

        self.signals_lineedit = QLineEdit(YasaSettingsView)
        self.signals_lineedit.setObjectName(u"signals_lineedit")

        self.signals_horizontalLayout.addWidget(self.signals_lineedit)


        self.verticalLayout.addLayout(self.signals_horizontalLayout)

        self.sleep_stages_horizontalLayout = QHBoxLayout()
        self.sleep_stages_horizontalLayout.setObjectName(u"sleep_stages_horizontalLayout")
        self.sleep_stages_label = QLabel(YasaSettingsView)
        self.sleep_stages_label.setObjectName(u"sleep_stages_label")

        self.sleep_stages_horizontalLayout.addWidget(self.sleep_stages_label)

        self.sleep_stages_lineedit = QLineEdit(YasaSettingsView)
        self.sleep_stages_lineedit.setObjectName(u"sleep_stages_lineedit")

        self.sleep_stages_horizontalLayout.addWidget(self.sleep_stages_lineedit)


        self.verticalLayout.addLayout(self.sleep_stages_horizontalLayout)

        self.events_horizontalLayout = QHBoxLayout()
        self.events_horizontalLayout.setObjectName(u"events_horizontalLayout")
        self.events_label = QLabel(YasaSettingsView)
        self.events_label.setObjectName(u"events_label")

        self.events_horizontalLayout.addWidget(self.events_label)

        self.events_lineedit = QLineEdit(YasaSettingsView)
        self.events_lineedit.setObjectName(u"events_lineedit")

        self.events_horizontalLayout.addWidget(self.events_lineedit)


        self.verticalLayout.addLayout(self.events_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(YasaSettingsView)

        QMetaObject.connectSlotsByName(YasaSettingsView)
    # setupUi

    def retranslateUi(self, YasaSettingsView):
        YasaSettingsView.setWindowTitle(QCoreApplication.translate("YasaSettingsView", u"Form", None))
        self.filename_label.setText(QCoreApplication.translate("YasaSettingsView", u"filename", None))
        self.signals_label.setText(QCoreApplication.translate("YasaSettingsView", u"signals", None))
        self.sleep_stages_label.setText(QCoreApplication.translate("YasaSettingsView", u"sleep_stages", None))
        self.events_label.setText(QCoreApplication.translate("YasaSettingsView", u"events", None))
    # retranslateUi

