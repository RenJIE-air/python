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
        MainWindow.resize(947, 598)
        MainWindow.setStyleSheet(u"QMainWindow{background-color:#34495e}")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        icon = QIcon()
        icon.addFile(u"../../../../../\u4e0b\u8f7d/google/icons8-inquiry-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action.setIcon(icon)
        self.actionbangzu = QAction(MainWindow)
        self.actionbangzu.setObjectName(u"actionbangzu")
        self.action_history = QAction(MainWindow)
        self.action_history.setObjectName(u"action_history")
        icon1 = QIcon()
        icon1.addFile(u"../../../../../\u4e0b\u8f7d/google/icons8-time-machine-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_history.setIcon(icon1)
        self.action_feedback = QAction(MainWindow)
        self.action_feedback.setObjectName(u"action_feedback")
        icon2 = QIcon()
        icon2.addFile(u"../../../../../\u4e0b\u8f7d/google/icons8-comments-16.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_feedback.setIcon(icon2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"background:transparent;\n"
"color:white;\n"
"	font: 10pt \"\u82f9\u65b9 \u5e38\u89c4\";\n"
"font-weight:bold\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        font = QFont()
        font.setFamily(u"\u82f9\u65b9 \u5e38\u89c4")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet(u"QGroupBox{border-width: 1px;border-style:solid;padding:20px;border-color:orange;border-radius:10px}")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.WholeMonkeyRadio = QRadioButton(self.groupBox_5)
        self.WholeMonkeyRadio.setObjectName(u"WholeMonkeyRadio")
        self.WholeMonkeyRadio.setAutoFillBackground(False)
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
        self.groupBox_4.setStyleSheet(u"QGroupBox{border-width: 1px;border-style:solid;padding:20px;border-color:orange;border-radius:10px}")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.updateLogPathCheck = QCheckBox(self.groupBox_4)
        self.updateLogPathCheck.setObjectName(u"updateLogPathCheck")
        self.updateLogPathCheck.setTristate(False)

        self.verticalLayout_4.addWidget(self.updateLogPathCheck)

        self.LogPathInput = QLineEdit(self.groupBox_4)
        self.LogPathInput.setObjectName(u"LogPathInput")
        self.LogPathInput.setEnabled(False)
        self.LogPathInput.setStyleSheet(u"QLineEdit{border-bottom-width: 2px;border-style: solid;border-color:white}")

        self.verticalLayout_4.addWidget(self.LogPathInput)

        self.updateOutPathCheck = QCheckBox(self.groupBox_4)
        self.updateOutPathCheck.setObjectName(u"updateOutPathCheck")

        self.verticalLayout_4.addWidget(self.updateOutPathCheck)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel{color:#27ae60;font-weight:bold}")

        self.verticalLayout_4.addWidget(self.label_2)

        self.OutputPathInput = QLineEdit(self.groupBox_4)
        self.OutputPathInput.setObjectName(u"OutputPathInput")
        self.OutputPathInput.setEnabled(False)
        self.OutputPathInput.setStyleSheet(u"QLineEdit{border-bottom-width: 2px;border-style: solid;border-color:white}")

        self.verticalLayout_4.addWidget(self.OutputPathInput)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

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
        self.exportButton.setStyleSheet(u"QPushButton{background-color:#3498db;color:white;}")
        icon3 = QIcon()
        icon3.addFile(u"../../../../../\u4e0b\u8f7d/google/\u8fd0\u884c.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exportButton.setIcon(icon3)

        self.verticalLayout.addWidget(self.exportButton)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet(u"QGroupBox{border-width: 1px;border-style:solid;padding:20px;border-color:orange;border-radius:10px}")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.DevicesText = QTextBrowser(self.groupBox_3)
        self.DevicesText.setObjectName(u"DevicesText")
        self.DevicesText.setStyleSheet(u"QTextBrowser{border-bottom-width:2px;border-style:solid;border-color:white}")

        self.verticalLayout_3.addWidget(self.DevicesText)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_3 = QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton{background:#00b894;color:white;}")
        icon4 = QIcon()
        icon4.addFile(u"E:/desktop/\u5237\u65b0.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon4)

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.stopMonkeyButton = QPushButton(self.groupBox_3)
        self.stopMonkeyButton.setObjectName(u"stopMonkeyButton")
        self.stopMonkeyButton.setStyleSheet(u"QPushButton{background:#e67e22}")
        icon5 = QIcon()
        icon5.addFile(u"../../../../../\u4e0b\u8f7d/google/\u505c\u6b621.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stopMonkeyButton.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.stopMonkeyButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)


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
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.clearButton = QPushButton(self.centralwidget)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setStyleSheet(u"QPushButton{background:#16a085}")
        icon6 = QIcon()
        icon6.addFile(u"../../../../../\u4e0b\u8f7d/google/\u6e05\u7a7a.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clearButton.setIcon(icon6)

        self.horizontalLayout.addWidget(self.clearButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.MessageText = QTextBrowser(self.centralwidget)
        self.MessageText.setObjectName(u"MessageText")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MessageText.sizePolicy().hasHeightForWidth())
        self.MessageText.setSizePolicy(sizePolicy1)
        self.MessageText.setFont(font)
        self.MessageText.setStyleSheet(u"QTextBrowser{border-width:1px;border-style:solid;border-color:#fdcb6e;border-radius:10px}")

        self.verticalLayout_2.addWidget(self.MessageText)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 947, 23))
        self.menuBar.setStyleSheet(u"QMenuBar{background:#2c3e50;color:white;font-weight:bold}")
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menuBar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_2.setStyleSheet(u"")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_history)
        self.menu_2.addAction(self.action_feedback)

        self.retranslateUi(MainWindow)
        self.updateLogPathCheck.toggled.connect(self.LogPathInput.setEnabled)
        self.updateOutPathCheck.toggled.connect(self.OutputPathInput.setEnabled)
        self.updateOutPathCheck.toggled.connect(self.label_2.setVisible)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MonkeyExport", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.actionbangzu.setText(QCoreApplication.translate("MainWindow", u"bangzu", None))
        self.action_history.setText(QCoreApplication.translate("MainWindow", u"\u5386\u53f2\u7248\u672c", None))
        self.action_feedback.setText(QCoreApplication.translate("MainWindow", u"\u53cd\u9988", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9", None))
        self.WholeMonkeyRadio.setText(QCoreApplication.translate("MainWindow", u"\u6574\u5305monkey", None))
        self.SingleMonkeyRadio.setText(QCoreApplication.translate("MainWindow", u"\u5355\u5305monkey", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u8bbe\u7f6e", None))
        self.updateLogPathCheck.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539log\u8def\u5f84", None))
        self.LogPathInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165log\u8def\u5f84\uff0c\u9ed8\u8ba4\u8def\u5f84\u4e3a\uff1a/data/ylog", None))
        self.updateOutPathCheck.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u8f93\u51fa\u8def\u5f84", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u610f\uff1a\u8f93\u51fa\u8def\u5f84\u8bf7\u4e0d\u8981\u5305\u542b\u4e2d\u6587\u5b57\u7b26\u53ca\u7a7a\u683c", None))
        self.OutputPathInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u8f93\u51fa\u8def\u5f84", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5176\u4ed6\u5bfc\u51fa\u9879\u76ee", None))
        self.logCheck.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51falog", None))
        self.bugreportCheck.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fabugreport", None))
        self.exportButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5bfc\u51fa", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5df2\u8fde\u63a5\u8bbe\u5907(\u8fde\u63a5\u591a\u53f0\u8bbe\u5907\u65f6\uff0c\u8bf7\u52ff\u8fde\u63a5\u6709\u76f8\u540cSN\u53f7\u7684\u8bbe\u5907)", None))
        self.DevicesText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u672a\u8fde\u63a5\u8bbe\u5907...", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u5237\u65b0", None))
        self.stopMonkeyButton.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62Monkey", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c\u65e5\u5fd7", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u65e5\u5fd7", None))
        self.MessageText.setPlaceholderText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u9879", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u66f4\u591a", None))
    # retranslateUi

