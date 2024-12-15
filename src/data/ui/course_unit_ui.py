# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'course_unit.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(258, 198)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.image = QLabel(Form)
        self.image.setObjectName(u"image")
        font = QFont()
        font.setFamilies([u"Pretendard"])
        self.image.setFont(font)

        self.verticalLayout.addWidget(self.image, 0, Qt.AlignHCenter)

        self.name = QLabel(Form)
        self.name.setObjectName(u"name")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Pretendard"])
        font1.setPointSize(20)
        self.name.setFont(font1)

        self.verticalLayout.addWidget(self.name)

        self.datetime = QLabel(Form)
        self.datetime.setObjectName(u"datetime")
        sizePolicy.setHeightForWidth(self.datetime.sizePolicy().hasHeightForWidth())
        self.datetime.setSizePolicy(sizePolicy)
        self.datetime.setFont(font)

        self.verticalLayout.addWidget(self.datetime)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.image.setText("")
        self.name.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.datetime.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

