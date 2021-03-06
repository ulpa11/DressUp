# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainLoginPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #420516;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.NavLine = QtWidgets.QFrame(self.centralwidget)
        self.NavLine.setGeometry(QtCore.QRect(0, 80, 1366, 1))
        self.NavLine.setStyleSheet("color:white;")
        self.NavLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.NavLine.setLineWidth(1)
        self.NavLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.NavLine.setObjectName("NavLine")
        self.IconMain = QtWidgets.QLabel(self.centralwidget)
        self.IconMain.setGeometry(QtCore.QRect(14, 15, 111, 51))
        self.IconMain.setText("")
        self.IconMain.setPixmap(QtGui.QPixmap(":/logos/logos/hanger.png"))
        self.IconMain.setScaledContents(True)
        self.IconMain.setAlignment(QtCore.Qt.AlignCenter)
        self.IconMain.setOpenExternalLinks(False)
        self.IconMain.setObjectName("IconMain")
        self.Heading = QtWidgets.QLabel(self.centralwidget)
        self.Heading.setGeometry(QtCore.QRect(140, 20, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.Heading.setFont(font)
        self.Heading.setStyleSheet("color:rgb(200, 186, 194)")
        self.Heading.setObjectName("Heading")
        self.IconMain2 = QtWidgets.QLabel(self.centralwidget)
        self.IconMain2.setGeometry(QtCore.QRect(290, 100, 271, 161))
        self.IconMain2.setText("")
        self.IconMain2.setPixmap(QtGui.QPixmap(":/logos/logos/hanger.png"))
        self.IconMain2.setScaledContents(True)
        self.IconMain2.setAlignment(QtCore.Qt.AlignCenter)
        self.IconMain2.setOpenExternalLinks(False)
        self.IconMain2.setObjectName("IconMain2")
        self.Heading2 = QtWidgets.QLabel(self.centralwidget)
        self.Heading2.setGeometry(QtCore.QRect(620, 100, 441, 151))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(57)
        font.setBold(True)
        font.setWeight(75)
        self.Heading2.setFont(font)
        self.Heading2.setStyleSheet("color:rgb(200, 186, 194)")
        self.Heading2.setObjectName("Heading2")
        self.Content = QtWidgets.QLabel(self.centralwidget)
        self.Content.setGeometry(QtCore.QRect(400, 260, 671, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.Content.setFont(font)
        self.Content.setStyleSheet("color:rgb(200, 186, 194)")
        self.Content.setObjectName("Content")
        self.Content1 = QtWidgets.QLabel(self.centralwidget)
        self.Content1.setGeometry(QtCore.QRect(570, 330, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.Content1.setFont(font)
        self.Content1.setStyleSheet("color:rgb(200, 186, 194)")
        self.Content1.setObjectName("Content1")
        self.Content2 = QtWidgets.QLabel(self.centralwidget)
        self.Content2.setGeometry(QtCore.QRect(550, 380, 241, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.Content2.setFont(font)
        self.Content2.setStyleSheet("color:rgb(200, 186, 194)")
        self.Content2.setObjectName("Content2")
        self.Content3 = QtWidgets.QLabel(self.centralwidget)
        self.Content3.setGeometry(QtCore.QRect(420, 480, 531, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(20)
        self.Content3.setFont(font)
        self.Content3.setStyleSheet("color:rgb(200, 186, 194)")
        self.Content3.setObjectName("Content3")
        self.LoginMainBT = QtWidgets.QPushButton(self.centralwidget)
        self.LoginMainBT.setGeometry(QtCore.QRect(20, 640, 621, 81))
        font = QtGui.QFont()
        font.setFamily("Plus Jakarta Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(62)
        self.LoginMainBT.setFont(font)
        self.LoginMainBT.setStyleSheet("background: #C4C4C4;\n"
"border-radius: 10px;\n"
"font-family: Plus Jakarta Sans;\n"
"font-style: normal;\n"
"font-weight: 500;\\n\n"
"font-size: 24px;\\n\n"
"line-height: 90%;")
        self.LoginMainBT.setObjectName("LoginMainBT")
        self.SignupMainBT = QtWidgets.QPushButton(self.centralwidget)
        self.SignupMainBT.setGeometry(QtCore.QRect(680, 640, 661, 81))
        font = QtGui.QFont()
        font.setFamily("Plus Jakarta Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(62)
        self.SignupMainBT.setFont(font)
        self.SignupMainBT.setStyleSheet("background: #C4C4C4;\n"
"border-radius: 10px;\n"
"font-family: Plus Jakarta Sans;\n"
"font-style: normal;\n"
"font-weight: 500;\\n\n"
"font-size: 24px;\\n\n"
"line-height: 90%;")
        self.SignupMainBT.setObjectName("SignupMainBT")
        self.IconMainCut = QtWidgets.QPushButton(self.centralwidget)
        self.IconMainCut.setGeometry(QtCore.QRect(1242, 17, 101, 51))
        self.IconMainCut.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/logos/qut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IconMainCut.setIcon(icon)
        self.IconMainCut.setIconSize(QtCore.QSize(60, 60))
        self.IconMainCut.setObjectName("IconMainCut")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Heading.setText(_translate("MainWindow", "Dress UP"))
        self.Heading2.setText(_translate("MainWindow", "Dress UP"))
        self.Content.setText(_translate("MainWindow", "<h3>No Matter how you feel<h3>"))
        self.Content1.setText(_translate("MainWindow", "<h4>Get UP<h4>"))
        self.Content2.setText(_translate("MainWindow", "Dress UP"))
        self.Content3.setText(_translate("MainWindow", "Show up and Never give up"))
        self.LoginMainBT.setText(_translate("MainWindow", "LOGIN"))
        self.SignupMainBT.setText(_translate("MainWindow", "SIGNUP"))
import source


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
