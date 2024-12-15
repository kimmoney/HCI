# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1480, 924)
        font = QFont()
        font.setFamilies([u"Pretendard"])
        MainWindow.setFont(font)
        self.mainWindow = QWidget(MainWindow)
        self.mainWindow.setObjectName(u"mainWindow")
        self.horizontalLayout = QHBoxLayout(self.mainWindow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stacked_main = QStackedWidget(self.mainWindow)
        self.stacked_main.setObjectName(u"stacked_main")
        self.stacked_main.setStyleSheet(u"")
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.gridLayout = QGridLayout(self.login)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_login_geust = QPushButton(self.login)
        self.btn_login_geust.setObjectName(u"btn_login_geust")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_login_geust.sizePolicy().hasHeightForWidth())
        self.btn_login_geust.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Pretendard"])
        font1.setPointSize(28)
        font1.setBold(True)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.btn_login_geust.setFont(font1)
        self.btn_login_geust.setStyleSheet(u"border:0px solid none;\n"
"color:#7F7E7E;\n"
"background-color:rgba(0,0,0,0);")

        self.gridLayout.addWidget(self.btn_login_geust, 3, 1, 1, 1)

        self.noname = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.noname, 0, 1, 1, 1)

        self.spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.spacer, 4, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.login_area = QWidget(self.login)
        self.login_area.setObjectName(u"login_area")
        self.login_area.setStyleSheet(u"#login_area{\n"
"	border-radius:30px;\n"
"	background-color:#F5F5F5;\n"
"}\n"
"QLineEdit{\n"
"border-radius:15px;\n"
"padding:30px;\n"
"}\n"
"QPushButton{\n"
"border : 0px solid nont;\n"
"color:#595858;\n"
"}\n"
"#btn_login_auto:checked{\n"
"background-image: url(:/login/images/login/check_circle.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: left center;\n"
"    background-origin: content;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.login_area)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(50, 80, 50, 80)
        self.label_login_error = QLabel(self.login_area)
        self.label_login_error.setObjectName(u"label_login_error")

        self.verticalLayout.addWidget(self.label_login_error)

        self.input_login_id = QLineEdit(self.login_area)
        self.input_login_id.setObjectName(u"input_login_id")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.input_login_id.sizePolicy().hasHeightForWidth())
        self.input_login_id.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(22)
        self.input_login_id.setFont(font2)

        self.verticalLayout.addWidget(self.input_login_id)

        self.input_login_pw = QLineEdit(self.login_area)
        self.input_login_pw.setObjectName(u"input_login_pw")
        sizePolicy1.setHeightForWidth(self.input_login_pw.sizePolicy().hasHeightForWidth())
        self.input_login_pw.setSizePolicy(sizePolicy1)
        self.input_login_pw.setFont(font2)

        self.verticalLayout.addWidget(self.input_login_pw)

        self.btn_login_auto = QPushButton(self.login_area)
        self.btn_login_auto.setObjectName(u"btn_login_auto")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_login_auto.sizePolicy().hasHeightForWidth())
        self.btn_login_auto.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u"Pretendard"])
        font3.setPointSize(22)
        self.btn_login_auto.setFont(font3)
        self.btn_login_auto.setStyleSheet(u"")
        self.btn_login_auto.setCheckable(True)
        self.btn_login_auto.setChecked(False)

        self.verticalLayout.addWidget(self.btn_login_auto, 0, Qt.AlignRight)

        self.btn_login_getPw = QPushButton(self.login_area)
        self.btn_login_getPw.setObjectName(u"btn_login_getPw")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_login_getPw.sizePolicy().hasHeightForWidth())
        self.btn_login_getPw.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamilies([u"Pretendard"])
        font4.setPointSize(20)
        self.btn_login_getPw.setFont(font4)

        self.verticalLayout.addWidget(self.btn_login_getPw)

        self.btn_login_signUp = QPushButton(self.login_area)
        self.btn_login_signUp.setObjectName(u"btn_login_signUp")
        sizePolicy3.setHeightForWidth(self.btn_login_signUp.sizePolicy().hasHeightForWidth())
        self.btn_login_signUp.setSizePolicy(sizePolicy3)
        self.btn_login_signUp.setFont(font4)

        self.verticalLayout.addWidget(self.btn_login_signUp)

        self.btn_login_login = QPushButton(self.login_area)
        self.btn_login_login.setObjectName(u"btn_login_login")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_login_login.sizePolicy().hasHeightForWidth())
        self.btn_login_login.setSizePolicy(sizePolicy4)
        font5 = QFont()
        font5.setFamilies([u"Pretendard"])
        font5.setPointSize(30)
        font5.setBold(True)
        self.btn_login_login.setFont(font5)

        self.verticalLayout.addWidget(self.btn_login_login, 0, Qt.AlignRight)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 3)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 2)

        self.gridLayout.addWidget(self.login_area, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.label = QLabel(self.login)
        self.label.setObjectName(u"label")
        self.label.setFont(font5)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 6)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)
        self.stacked_main.addWidget(self.login)
        self.menu = QWidget()
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"#menu{\n"
"border-radius:0px;\n"
"background-color:white;\n"
"}\n"
"QWidget#menu_profile{\n"
"	border-radius:30px;\n"
"	background-color:#F5F5F5;\n"
"}\n"
"QWidget#menu_section{\n"
"	border-radius:30px;\n"
"	background-color:#F5F5F5;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.menu)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.menu_profile = QWidget(self.menu)
        self.menu_profile.setObjectName(u"menu_profile")
        self.verticalLayout_2 = QVBoxLayout(self.menu_profile)
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(40, 100, 40, 100)
        self.label_2 = QLabel(self.menu_profile)
        self.label_2.setObjectName(u"label_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy5)
        self.label_2.setMinimumSize(QSize(200, 200))
        self.label_2.setMaximumSize(QSize(200, 200))
        self.label_2.setStyleSheet(u"border-image: url(:/menu/images/menu/profile_img.png);")

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.line = QFrame(self.menu_profile)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_2.addWidget(self.line)

        self.label_3 = QLabel(self.menu_profile)
        self.label_3.setObjectName(u"label_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy6)
        font6 = QFont()
        font6.setFamilies([u"Pretendard"])
        font6.setPointSize(33)
        self.label_3.setFont(font6)

        self.verticalLayout_2.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(self.menu_profile)
        self.label_4.setObjectName(u"label_4")
        sizePolicy6.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy6)
        font7 = QFont()
        font7.setFamilies([u"Pretendard"])
        font7.setPointSize(25)
        self.label_4.setFont(font7)

        self.verticalLayout_2.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.line_2 = QFrame(self.menu_profile)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_2.addWidget(self.line_2)

        self.pushButton = QPushButton(self.menu_profile)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy6.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy6)
        font8 = QFont()
        font8.setFamilies([u"Pretendard"])
        font8.setPointSize(22)
        font8.setStyleStrategy(QFont.PreferAntialias)
        self.pushButton.setFont(font8)
        self.pushButton.setStyleSheet(u"border:0px solid none;\n"
"color:#ED633F;\n"
"background-color:rgba(0,0,0,0);")

        self.verticalLayout_2.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.verticalLayout_2.setStretch(0, 8)
        self.verticalLayout_2.setStretch(2, 3)
        self.verticalLayout_2.setStretch(3, 2)
        self.verticalLayout_2.setStretch(5, 2)

        self.gridLayout_2.addWidget(self.menu_profile, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(682, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(42, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.menu_section = QWidget(self.menu)
        self.menu_section.setObjectName(u"menu_section")
        self.menu_section.setFont(font)
        self.menu_section.setStyleSheet(u"QPushButton{\n"
"border:0px solid none;\n"
"color:#535353;\n"
"text-align:left;\n"
"background-color:rgba(0,0,0,0);\n"
"	image: url(:/menu/images/menu/Keyboard arrow right.png);\n"
"    image-position: right center;\n"
"}\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.menu_section)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(60, 80, 50, 80)
        self.pushButton_2 = QPushButton(self.menu_section)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy7)
        font9 = QFont()
        font9.setFamilies([u"Pretendard"])
        font9.setPointSize(45)
        font9.setBold(True)
        self.pushButton_2.setFont(font9)

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.line_3 = QFrame(self.menu_section)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_3.addWidget(self.line_3)

        self.pushButton_3 = QPushButton(self.menu_section)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy7.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy7)
        self.pushButton_3.setFont(font9)

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.line_4 = QFrame(self.menu_section)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_3.addWidget(self.line_4)

        self.pushButton_4 = QPushButton(self.menu_section)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy7.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy7)
        self.pushButton_4.setFont(font9)

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.line_5 = QFrame(self.menu_section)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_3.addWidget(self.line_5)

        self.pushButton_5 = QPushButton(self.menu_section)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy7.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy7)
        self.pushButton_5.setFont(font9)

        self.verticalLayout_3.addWidget(self.pushButton_5)

        self.line_6 = QFrame(self.menu_section)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setLineWidth(2)
        self.line_6.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_3.addWidget(self.line_6)


        self.gridLayout_2.addWidget(self.menu_section, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 10)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 12)
        self.gridLayout_2.setColumnStretch(2, 18)
        self.gridLayout_2.setColumnStretch(3, 1)
        self.stacked_main.addWidget(self.menu)

        self.horizontalLayout.addWidget(self.stacked_main)

        MainWindow.setCentralWidget(self.mainWindow)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stacked_main.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_login_geust.setText(QCoreApplication.translate("MainWindow", u"Guest Login", None))
        self.label_login_error.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.input_login_id.setText("")
        self.input_login_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id", None))
        self.input_login_pw.setText("")
        self.input_login_pw.setPlaceholderText(QCoreApplication.translate("MainWindow", u"password", None))
        self.btn_login_auto.setText(QCoreApplication.translate("MainWindow", u"     \uc790\ub3d9 \ub85c\uadf8\uc778", None))
        self.btn_login_getPw.setText(QCoreApplication.translate("MainWindow", u"\ube44\ubc00\ubc88\ud638 \ucc3e\uae30", None))
        self.btn_login_signUp.setText(QCoreApplication.translate("MainWindow", u"\uacc4\uc815 \uc0dd\uc131\ud558\uae30", None))
        self.btn_login_login.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uadf8\uc778   >", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dot Canvas", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"id_name", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uadf8\uc544\uc6c3", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Learning Courses", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Create Canvas", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"My Drawing", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Dot Drive", None))
    # retranslateUi

