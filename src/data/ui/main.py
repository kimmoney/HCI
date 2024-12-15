# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QVBoxLayout, QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1279, 901)
        font = QFont()
        font.setFamilies([u"Pretendard"])
        MainWindow.setFont(font)
        self.mainWindow = QWidget(MainWindow)
        self.mainWindow.setObjectName(u"mainWindow")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainWindow.sizePolicy().hasHeightForWidth())
        self.mainWindow.setSizePolicy(sizePolicy)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_login_geust.sizePolicy().hasHeightForWidth())
        self.btn_login_geust.setSizePolicy(sizePolicy1)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.input_login_id.sizePolicy().hasHeightForWidth())
        self.input_login_id.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(22)
        self.input_login_id.setFont(font2)

        self.verticalLayout.addWidget(self.input_login_id)

        self.input_login_pw = QLineEdit(self.login_area)
        self.input_login_pw.setObjectName(u"input_login_pw")
        sizePolicy2.setHeightForWidth(self.input_login_pw.sizePolicy().hasHeightForWidth())
        self.input_login_pw.setSizePolicy(sizePolicy2)
        self.input_login_pw.setFont(font2)

        self.verticalLayout.addWidget(self.input_login_pw)

        self.btn_login_auto = QPushButton(self.login_area)
        self.btn_login_auto.setObjectName(u"btn_login_auto")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_login_auto.sizePolicy().hasHeightForWidth())
        self.btn_login_auto.setSizePolicy(sizePolicy3)
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
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_login_getPw.sizePolicy().hasHeightForWidth())
        self.btn_login_getPw.setSizePolicy(sizePolicy4)
        font4 = QFont()
        font4.setFamilies([u"Pretendard"])
        font4.setPointSize(20)
        self.btn_login_getPw.setFont(font4)

        self.verticalLayout.addWidget(self.btn_login_getPw)

        self.btn_login_signUp = QPushButton(self.login_area)
        self.btn_login_signUp.setObjectName(u"btn_login_signUp")
        sizePolicy4.setHeightForWidth(self.btn_login_signUp.sizePolicy().hasHeightForWidth())
        self.btn_login_signUp.setSizePolicy(sizePolicy4)
        self.btn_login_signUp.setFont(font4)

        self.verticalLayout.addWidget(self.btn_login_signUp)

        self.btn_login_login = QPushButton(self.login_area)
        self.btn_login_login.setObjectName(u"btn_login_login")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_login_login.sizePolicy().hasHeightForWidth())
        self.btn_login_login.setSizePolicy(sizePolicy5)
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
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy6)
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
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy7)
        font6 = QFont()
        font6.setFamilies([u"Pretendard"])
        font6.setPointSize(33)
        self.label_3.setFont(font6)

        self.verticalLayout_2.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(self.menu_profile)
        self.label_4.setObjectName(u"label_4")
        sizePolicy7.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy7)
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
        sizePolicy7.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy7)
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
        self.btn_learning = QPushButton(self.menu_section)
        self.btn_learning.setObjectName(u"btn_learning")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.btn_learning.sizePolicy().hasHeightForWidth())
        self.btn_learning.setSizePolicy(sizePolicy8)
        font9 = QFont()
        font9.setFamilies([u"Pretendard"])
        font9.setPointSize(45)
        font9.setBold(True)
        self.btn_learning.setFont(font9)

        self.verticalLayout_3.addWidget(self.btn_learning)

        self.line_3 = QFrame(self.menu_section)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_3.addWidget(self.line_3)

        self.pushButton_3 = QPushButton(self.menu_section)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy8.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy8)
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
        sizePolicy8.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy8)
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
        sizePolicy8.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy8)
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
        self.course = QWidget()
        self.course.setObjectName(u"course")
        self.course.setStyleSheet(u"#cource{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.course)
        self.verticalLayout_6.setSpacing(40)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(40, 40, 40, 40)
        self.widget = QWidget(self.course)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"border-radius: 20px;\n"
"background: #F3F3F3;")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(50, 20, 50, 20)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"border-radius: 30px;\n"
"background: #FFF;")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 0, 20, 0)
        self.btn_curse2home = QPushButton(self.widget_2)
        self.btn_curse2home.setObjectName(u"btn_curse2home")
        sizePolicy5.setHeightForWidth(self.btn_curse2home.sizePolicy().hasHeightForWidth())
        self.btn_curse2home.setSizePolicy(sizePolicy5)
        self.btn_curse2home.setFont(font4)
        self.btn_curse2home.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.btn_curse2home)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        font10 = QFont()
        font10.setFamilies([u"Pretendard"])
        font10.setPointSize(31)
        self.label_5.setFont(font10)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.pushButton_8 = QPushButton(self.widget_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy5.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy5)
        self.pushButton_8.setFont(font4)
        self.pushButton_8.setStyleSheet(u"border-radius: 23px;\n"
"background: white;\n"
"color:white;")

        self.horizontalLayout_3.addWidget(self.pushButton_8)


        self.verticalLayout_5.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(300, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.widget_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy9)
        self.pushButton_6.setFont(font4)
        self.pushButton_6.setStyleSheet(u"border-radius: 23px;\n"
"background: #ED633F;\n"
"color:white;")

        self.horizontalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_2 = QPushButton(self.widget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy9.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy9)
        self.pushButton_2.setFont(font4)
        self.pushButton_2.setStyleSheet(u"border-radius: 23px;\n"
"background: #979797;\n"
"color:white;")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout_5.addWidget(self.widget_3, 0, Qt.AlignRight)

        self.verticalLayout_5.setStretch(0, 3)
        self.verticalLayout_5.setStretch(1, 2)

        self.verticalLayout_6.addWidget(self.widget)

        self.course_tab = QTabWidget(self.course)
        self.course_tab.setObjectName(u"course_tab")
        self.course_tab.setFont(font6)
        self.course_tab.setStyleSheet(u"QTabWidget{\n"
"background-color:rgba(0,0,0,0);\n"
"}\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    background-color:rgb(249, 249, 250);  /* \ud0ed \ubc14\uc758 \uc804\uccb4 \ubc30\uacbd\uc0c9 */\n"
"	border:none;\n"
"}\n"
"QTabWidget::tab-bar {\n"
"    left: 10px; /* move to the right by 5px */\n"
"	border:0px solid black;\n"
"	\n"
"    background-color: None;  /* \ud0ed \ubc14\uc758 \uc804\uccb4 \ubc30\uacbd\uc0c9 */\n"
"}\n"
"QTabBar::tab {\n"
"    background-color: #979797;\n"
"    border: 1px solid gray;\n"
"    min-width: 188px;\n"
"	min-height:54px;\n"
"    color: white;\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color:#ED633F;\n"
"	border:none;\n"
"    color: white;\n"
"}\n"
"\n"
"QWidget{background-color:rgba(0,0,0,0);}\n"
"#level1{\n"
"background-color:#F3F3F3;\n"
"border:0px solid black;\n"
"border-radius:10px;}\n"
"#level2{\n"
"background-color:#F3F3F3;\n"
"border:0px solid black;\n"
"border-radius:10"
                        "px;}\n"
"#level3{\n"
"background-color:#F3F3F3;\n"
"border:0px solid black;\n"
"border-radius:10px;}")
        self.level1 = QWidget()
        self.level1.setObjectName(u"level1")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.level1.sizePolicy().hasHeightForWidth())
        self.level1.setSizePolicy(sizePolicy10)
        self.gridLayout_3 = QGridLayout(self.level1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_23 = QFrame(self.level1)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"background:white;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_23, 0, 0, 1, 1)

        self.frame_21 = QFrame(self.level1)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"background:white;")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_21, 0, 1, 1, 1)

        self.frame_22 = QFrame(self.level1)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"background:white;")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_22, 0, 2, 1, 1)

        self.frame_24 = QFrame(self.level1)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"background:white;")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_24, 0, 3, 1, 1)

        self.frame_25 = QFrame(self.level1)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"background:white;")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_25, 1, 0, 1, 1)

        self.frame_20 = QFrame(self.level1)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"background:white;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_20, 1, 1, 1, 1)

        self.frame_19 = QFrame(self.level1)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"background:white;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_19, 1, 2, 1, 1)

        self.frame_18 = QFrame(self.level1)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"background:white;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_18, 1, 3, 1, 1)

        self.course_tab.addTab(self.level1, "")
        self.level2 = QWidget()
        self.level2.setObjectName(u"level2")
        self.gridLayout_4 = QGridLayout(self.level2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_9 = QFrame(self.level2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background:white;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_9, 1, 0, 1, 1)

        self.frame = QFrame(self.level2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background:white;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.level2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background:white;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_4, 0, 2, 1, 1)

        self.frame_5 = QFrame(self.level2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background:white;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_5, 0, 3, 1, 1)

        self.frame_3 = QFrame(self.level2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background:white;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_3, 0, 1, 1, 1)

        self.frame_8 = QFrame(self.level2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background:white;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_8, 1, 1, 1, 1)

        self.frame_7 = QFrame(self.level2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background:white;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_7, 1, 2, 1, 1)

        self.frame_6 = QFrame(self.level2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background:white;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_6, 1, 3, 1, 1)

        self.course_tab.addTab(self.level2, "")
        self.level3 = QWidget()
        self.level3.setObjectName(u"level3")
        self.gridLayout_5 = QGridLayout(self.level3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_15 = QFrame(self.level3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"background:white;")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_15, 0, 0, 1, 1)

        self.frame_13 = QFrame(self.level3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background:white;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_13, 0, 1, 1, 1)

        self.frame_14 = QFrame(self.level3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"background:white;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_14, 0, 2, 1, 1)

        self.frame_16 = QFrame(self.level3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"background:white;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_16, 0, 3, 1, 1)

        self.frame_17 = QFrame(self.level3)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"background:white;")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_17, 1, 0, 1, 1)

        self.frame_12 = QFrame(self.level3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"background:white;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_12, 1, 1, 1, 1)

        self.frame_11 = QFrame(self.level3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background:white;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_11, 1, 2, 1, 1)

        self.frame_10 = QFrame(self.level3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background:white;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_10, 1, 3, 1, 1)

        self.course_tab.addTab(self.level3, "")

        self.verticalLayout_6.addWidget(self.course_tab)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 3)
        self.stacked_main.addWidget(self.course)
        self.connecting = QWidget()
        self.connecting.setObjectName(u"connecting")
        self.verticalLayout_4 = QVBoxLayout(self.connecting)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.connecting_label = QLabel(self.connecting)
        self.connecting_label.setObjectName(u"connecting_label")
        font11 = QFont()
        font11.setFamilies([u"Pretendard"])
        font11.setPointSize(40)
        self.connecting_label.setFont(font11)
        self.connecting_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.connecting_label)

        self.stacked_main.addWidget(self.connecting)
        self.painting = QWidget()
        self.painting.setObjectName(u"painting")
        self.layout_painting = QHBoxLayout(self.painting)
        self.layout_painting.setObjectName(u"layout_painting")
        self.stacked_main.addWidget(self.painting)
        self.validation = QWidget()
        self.validation.setObjectName(u"validation")
        self.stacked_main.addWidget(self.validation)

        self.horizontalLayout.addWidget(self.stacked_main)

        MainWindow.setCentralWidget(self.mainWindow)

        self.retranslateUi(MainWindow)

        self.stacked_main.setCurrentIndex(0)
        self.course_tab.setCurrentIndex(0)


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
        self.btn_learning.setText(QCoreApplication.translate("MainWindow", u"Learning Courses", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Create Canvas", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"My Drawing", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Dot Drive", None))
        self.btn_curse2home.setText(QCoreApplication.translate("MainWindow", u"< HOME", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Learning Courses", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"< HOME", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\uc774\uc5b4\ud558\uae30", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9", None))
        self.course_tab.setTabText(self.course_tab.indexOf(self.level1), QCoreApplication.translate("MainWindow", u"\ub808\ubca81", None))
        self.course_tab.setTabText(self.course_tab.indexOf(self.level2), QCoreApplication.translate("MainWindow", u"\ub808\ubca82", None))
        self.course_tab.setTabText(self.course_tab.indexOf(self.level3), QCoreApplication.translate("MainWindow", u"\ub808\ubca83", None))
        self.connecting_label.setText(QCoreApplication.translate("MainWindow", u"DotPad\uc640 \uc5f0\uacb0\uc911\uc785\ub2c8\ub2e4.", None))
    # retranslateUi

