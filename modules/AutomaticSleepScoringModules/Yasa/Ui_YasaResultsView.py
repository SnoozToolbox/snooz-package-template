# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_YasaResultsView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import themes_rc

class Ui_YasaResultsView(object):
    def setupUi(self, YasaResultsView):
        if not YasaResultsView.objectName():
            YasaResultsView.setObjectName(u"YasaResultsView")
        YasaResultsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        YasaResultsView.resize(483, 360)
        self.verticalLayout = QVBoxLayout(YasaResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.retranslateUi(YasaResultsView)

        QMetaObject.connectSlotsByName(YasaResultsView)
    # setupUi

    def retranslateUi(self, YasaResultsView):
        YasaResultsView.setWindowTitle(QCoreApplication.translate("YasaResultsView", u"Form", None))
    # retranslateUi

