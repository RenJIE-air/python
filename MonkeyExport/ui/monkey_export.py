# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'monkey_export.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(784, 446)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        font = QFont()
        font.setFamily(u"Microsoft YaHei")
        self.groupBox_5.setFont(font)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.WholeMonkeyRadio = QRadioButton(self.groupBox_5)
        self.WholeMonkeyRadio.setObjectName(u"WholeMonkeyRadio")
        self.WholeMonkeyRadio.setChecked(True)

        self.horizontalLayout_5.addWidget(self.WholeMonkeyRadio)

        self.SingleMonkeyRadio = QRadioButton(self.groupBox_5)
        self.SingleMonkeyRadio.setObjectName(u"SingleMonkeyRadio")

        self.horizontalLayout_5.addWidget(self.SingleMonkeyRadio)


        self.verticalLayout.addWidget(self.groupBox_5)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setEnabled(True)
        self.groupBox_4.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.updateLogPathCheck = QCheckBox(self.groupBox_4)
        self.updateLogPathCheck.setObjectName(u"updateLogPathCheck")

        self.horizontalLayout_6.addWidget(self.updateLogPathCheck)

        self.LogPathInput = QLineEdit(self.groupBox_4)
        self.LogPathInput.setObjectName(u"LogPathInput")
        self.LogPathInput.setEnabled(False)

        self.horizontalLayout_6.addWidget(self.LogPathInput)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.updateOutPathCheck = QCheckBox(self.groupBox_4)
        self.updateOutPathCheck.setObjectName(u"updateOutPathCheck")

        self.horizontalLayout_7.addWidget(self.updateOutPathCheck)

        self.OutputPathInput = QLineEdit(self.groupBox_4)
        self.OutputPathInput.setObjectName(u"OutputPathInput")
        self.OutputPathInput.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.OutputPathInput)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Microsoft YaHei UI")
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel{color:red;font-weight:bold}")

        self.verticalLayout_4.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logCheck = QCheckBox(self.groupBox_4)
        self.logCheck.setObjectName(u"logCheck")
        self.logCheck.setChecked(True)

        self.horizontalLayout_2.addWidget(self.logCheck)

        self.bugreportCheck = QCheckBox(self.groupBox_4)
        self.bugreportCheck.setObjectName(u"bugreportCheck")
        self.bugreportCheck.setChecked(True)

        self.horizontalLayout_2.addWidget(self.bugreportCheck)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.exportButton = QPushButton(self.centralwidget)
        self.exportButton.setObjectName(u"exportButton")
        self.exportButton.setFont(font)

        self.verticalLayout.addWidget(self.exportButton)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        font2 = QFont()
        font2.setFamily(u"Microsoft YaHei UI")
        self.groupBox_3.setFont(font2)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.DevicesText = QTextBrowser(self.groupBox_3)
        self.DevicesText.setObjectName(u"DevicesText")

        self.verticalLayout_5.addWidget(self.DevicesText)

        self.pushButton_3 = QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_5.addWidget(self.pushButton_3)


        self.horizontalLayout_4.addWidget(self.groupBox_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font2)

        self.horizontalLayout.addWidget(self.label)

        self.clearButton = QPushButton(self.centralwidget)
        self.clearButton.setObjectName(u"clearButton")

        self.horizontalLayout.addWidget(self.clearButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.MessageText = QTextBrowser(self.centralwidget)
        self.MessageText.setObjectName(u"MessageText")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MessageText.sizePolicy().hasHeightForWidth())
        self.MessageText.setSizePolicy(sizePolicy1)
        self.MessageText.setFont(font2)

        self.verticalLayout_2.addWidget(self.MessageText)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.updateLogPathCheck.toggled.connect(self.LogPathInput.setEnabled)
        self.updateOutPathCheck.toggled.connect(self.OutputPathInput.setEnabled)
        self.updateOutPathCheck.toggled.connect(self.label_2.setVisible)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MonkeyExport", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9", None))
        self.WholeMonkeyRadio.setText(QCoreApplication.translate("MainWindow", u"\u6574\u5305monkey", None))
        self.SingleMonkeyRadio.setText(QCoreApplication.translate("MainWindow", u"\u5355\u5305monkey", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u8bbe\u7f6e", None))
        self.updateLogPathCheck.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539log\u8def\u5f84", None))
        self.LogPathInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165log\u8def\u5f84\uff0c\u9ed8\u8ba4\u8def\u5f84\u4e3a\uff1a/data/ylog", None))
        self.updateOutPathCheck.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u8f93\u51fa\u8def\u5f84", None))
        self.OutputPathInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u8f93\u51fa\u8def\u5f84", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u610f\uff1a\u8f93\u51fa\u8def\u5f84\u8bf7\u4e0d\u8981\u5305\u542b\u4e2d\u6587\u5b57\u7b26", None))
        self.logCheck.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51falog", None))
        self.bugreportCheck.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fabugreport", None))
        self.exportButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5bfc\u51fa", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5df2\u8fde\u63a5\u8bbe\u5907(\u8fde\u63a5\u591a\u53f0\u8bbe\u5907\u65f6\uff0c\u8bf7\u6ce8\u610fSN\u53f7\u662f\u5426\u6709\u76f8\u540c\u7684\u8bbe\u5907)", None))
        self.DevicesText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u672a\u8fde\u63a5\u8bbe\u5907...", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u5237\u65b0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c\u8fc7\u7a0b", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u6d88\u606f", None))
        self.MessageText.setPlaceholderText("")
    # retranslateUi

