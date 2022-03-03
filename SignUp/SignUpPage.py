# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginPage.ui'
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
        self.IconMain2.setGeometry(QtCore.QRect(150, 100, 271, 161))
        self.IconMain2.setText("")
        self.IconMain2.setPixmap(QtGui.QPixmap(":/logos/logos/hanger.png"))
        self.IconMain2.setScaledContents(True)
        self.IconMain2.setAlignment(QtCore.Qt.AlignCenter)
        self.IconMain2.setOpenExternalLinks(False)
        self.IconMain2.setObjectName("IconMain2")
        self.Heading2 = QtWidgets.QLabel(self.centralwidget)
        self.Heading2.setGeometry(QtCore.QRect(500, 100, 441, 151))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(57)
        font.setBold(True)
        font.setWeight(75)
        self.Heading2.setFont(font)
        self.Heading2.setStyleSheet("color:rgb(200, 186, 194)")
        self.Heading2.setObjectName("Heading2")
        self.SignupBtn = QtWidgets.QPushButton(self.centralwidget)
        self.SignupBtn.setGeometry(QtCore.QRect(380, 660, 591, 71))
        font = QtGui.QFont()
        font.setFamily("Plus Jakarta Sans")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(62)
        self.SignupBtn.setFont(font)
        self.SignupBtn.setStyleSheet("background: #C4C4C4;\n"
"border-radius: 10px;\n"
"font-family: Plus Jakarta Sans;\n"
"font-style: normal;\n"
"font-weight: 500;\\n\n"
"font-size: 24px;\\n\n"
"line-height: 90%;")
        self.SignupBtn.setObjectName("SignupBtn")
        self.IconMainCut = QtWidgets.QPushButton(self.centralwidget)
        self.IconMainCut.setGeometry(QtCore.QRect(1242, 17, 101, 51))
        self.IconMainCut.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/logos/qut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IconMainCut.setIcon(icon)
        self.IconMainCut.setIconSize(QtCore.QSize(60, 60))
        self.IconMainCut.setObjectName("IconMainCut")
        self.emailalbel = QtWidgets.QLabel(self.centralwidget)
        self.emailalbel.setGeometry(QtCore.QRect(300, 300, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Plus Jakarta Sans Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.emailalbel.setFont(font)
        self.emailalbel.setStyleSheet("color:white;")
        self.emailalbel.setObjectName("emailalbel")
        self.emailinput = QtWidgets.QLineEdit(self.centralwidget)
        self.emailinput.setGeometry(QtCore.QRect(600, 290, 581, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.emailinput.setFont(font)
        self.emailinput.setStyleSheet("border:2px solid white;\n"
"border-radius:10px;\n"
"color:white;\n"
"")
        self.emailinput.setObjectName("emailinput")
        self.passwrodlabel = QtWidgets.QLabel(self.centralwidget)
        self.passwrodlabel.setGeometry(QtCore.QRect(300, 360, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Plus Jakarta Sans Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.passwrodlabel.setFont(font)
        self.passwrodlabel.setStyleSheet("color:white;")
        self.passwrodlabel.setObjectName("passwrodlabel")
        self.PasswordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordInput.setGeometry(QtCore.QRect(600, 350, 581, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PasswordInput.setFont(font)
        self.PasswordInput.setStyleSheet("border:2px solid white;\n"
"border-radius:10px;\n"
"color:white;\n"
"")
        self.PasswordInput.setObjectName("PasswordInput")
        self.genderlabel = QtWidgets.QLabel(self.centralwidget)
        self.genderlabel.setGeometry(QtCore.QRect(300, 420, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Plus Jakarta Sans Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.genderlabel.setFont(font)
        self.genderlabel.setStyleSheet("color:white;")
        self.genderlabel.setObjectName("genderlabel")
        self.GenderInput = QtWidgets.QComboBox(self.centralwidget)
        self.GenderInput.setEnabled(True)
        self.GenderInput.setGeometry(QtCore.QRect(600, 410, 581, 51))
        self.GenderInput.setStyleSheet("border:2px solid white;\n"
"border-radius:10px;\n"
"color:white;\n"
"")
        self.GenderInput.setEditable(False)
        self.GenderInput.setCurrentText("")
        self.GenderInput.setObjectName("GenderInput")
        self.GenderInput.addItem("Female")
        self.GenderInput.addItem("Male")

        self.DOB = QtWidgets.QLineEdit(self.centralwidget)
        self.DOB.setGeometry(QtCore.QRect(600, 470, 581, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DOB.setFont(font)
        self.DOB.setStyleSheet("border:2px solid white;\n"
"border-radius:10px;\n"
"color:white;\n"
"")
        self.DOB.setObjectName("DOB")

        self.DOBlabel = QtWidgets.QLabel(self.centralwidget)
        self.DOBlabel.setGeometry(QtCore.QRect(300, 480, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Plus Jakarta Sans Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.DOBlabel.setFont(font)
        self.DOBlabel.setStyleSheet("color:white;")
        self.DOBlabel.setObjectName("DOBlabel")
        self.skintonecontent = QtWidgets.QLabel(self.centralwidget)
        self.skintonecontent.setGeometry(QtCore.QRect(300, 520, 931, 51))
        font = QtGui.QFont()
        font.setFamily("Plus Jakarta Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.skintonecontent.setFont(font)
        self.skintonecontent.setStyleSheet("color:white;")
        self.skintonecontent.setObjectName("skintonecontent")
        self.skintonelabel = QtWidgets.QLabel(self.centralwidget)
        self.skintonelabel.setGeometry(QtCore.QRect(300, 580, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Plus Jakarta Sans Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.skintonelabel.setFont(font)
        self.skintonelabel.setStyleSheet("color:white;")
        self.skintonelabel.setObjectName("skintonelabel")
        self.skintoneinput = QtWidgets.QComboBox(self.centralwidget)
        self.skintoneinput.setEnabled(True)
        self.skintoneinput.setGeometry(QtCore.QRect(600, 580, 581, 51))
        self.skintoneinput.setStyleSheet("border:2px solid white;\n"
"border-radius:10px;\n"
"color:white;\n"
"")
        self.skintoneinput.setEditable(False)
        self.skintoneinput.setCurrentText("")
        self.skintoneinput.setObjectName("skintoneinput")
        #self.skintoneinput.setCurrentText("select SkinTone")
        self.skintoneinput.setObjectName("skintoneinput")
        #self.skintoneinput.addItem("select SkinTone")
        self.skintoneinput.addItem("Warm Tone")
        self.skintoneinput.addItem("Cold Tone")
        self.skintoneinput.addItem("Neutral Tone")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.GenderInput.setCurrentIndex(-1)
        self.skintoneinput.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Heading.setText(_translate("MainWindow", "Dress UP"))
        self.Heading2.setText(_translate("MainWindow", "SIGNUP"))
        self.SignupBtn.setText(_translate("MainWindow", "SIGNUP"))
        self.emailalbel.setText(_translate("MainWindow", "Email ID"))
        self.emailinput.setText(_translate("MainWindow", "please enter your email id"))
        self.passwrodlabel.setText(_translate("MainWindow", "Password"))
        self.PasswordInput.setText(_translate("MainWindow", "create your password"))
        self.genderlabel.setText(_translate("MainWindow", "Gender"))
        self.DOB.setText(_translate("MainWindow", "dd/mm/yyyy"))
        self.DOBlabel.setText(_translate("MainWindow", "DOB"))
        self.skintonecontent.setText(_translate("MainWindow", "Take  a  look  at  your  arm. If  the  veins  on  your  wrist  are  more  blue  than  green,  you  have  cool-toned  skin.\n"
" If  they’re  more  green, your  skin  is  warm-toned. If  it’s  hard  to  tell, you  likely  have  a  neutral  skin  tone."))
        self.skintonelabel.setText(_translate("MainWindow", "Skin Tone"))
import source


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
