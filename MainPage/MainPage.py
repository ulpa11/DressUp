# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPage.ui'
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
        self.IconMainCut = QtWidgets.QPushButton(self.centralwidget)
        self.IconMainCut.setGeometry(QtCore.QRect(1242, 17, 101, 51))
        self.IconMainCut.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/logos/qut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IconMainCut.setIcon(icon)
        self.IconMainCut.setIconSize(QtCore.QSize(60, 60))
        self.IconMainCut.setObjectName("IconMainCut")
        self.MainTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.MainTabs.setGeometry(QtCore.QRect(-10, 80, 1381, 691))
        self.MainTabs.setAutoFillBackground(False)
        self.MainTabs.setTabPosition(QtWidgets.QTabWidget.East)
        self.MainTabs.setIconSize(QtCore.QSize(120, 120))
        self.MainTabs.setElideMode(QtCore.Qt.ElideMiddle)
        self.MainTabs.setObjectName("MainTabs")
        self.ClosetTab = QtWidgets.QWidget()
        self.ClosetTab.setObjectName("ClosetTab")
        self.CategoryTab = QtWidgets.QTabWidget(self.ClosetTab)
        self.CategoryTab.setGeometry(QtCore.QRect(10, 0, 1251, 691))
        self.CategoryTab.setTabPosition(QtWidgets.QTabWidget.West)
        self.CategoryTab.setIconSize(QtCore.QSize(100, 100))
        self.CategoryTab.setObjectName("CategoryTab")
        self.TshirtTab = QtWidgets.QWidget()
        self.TshirtTab.setObjectName("TshirtTab")
        self.TshirtLabel = QtWidgets.QLabel(self.TshirtTab)
        self.TshirtLabel.setGeometry(QtCore.QRect(450, 40, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.TshirtLabel.setFont(font)
        self.TshirtLabel.setStyleSheet("color:white;")
        self.TshirtLabel.setObjectName("TshirtLabel")
        self.TshirtTabDeleteBT = QtWidgets.QPushButton(self.TshirtTab)
        self.TshirtTabDeleteBT.setGeometry(QtCore.QRect(960, 40, 91, 131))
        self.TshirtTabDeleteBT.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logos/logos/trash-bin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TshirtTabDeleteBT.setIcon(icon1)
        self.TshirtTabDeleteBT.setIconSize(QtCore.QSize(100, 100))
        self.TshirtTabDeleteBT.setObjectName("TshirtTabDeleteBT")
        self.TabviewImage = QtWidgets.QLabel(self.TshirtTab)
        self.TabviewImage.setGeometry(QtCore.QRect(370, 190, 371, 291))
        self.TabviewImage.setText("")
        self.TabviewImage.setPixmap(QtGui.QPixmap(":/logos/logos/hanger (1).png"))
        self.TabviewImage.setScaledContents(True)
        self.TabviewImage.setObjectName("TabviewImage")
        self.TshirtTabNextBT = QtWidgets.QPushButton(self.TshirtTab)
        self.TshirtTabNextBT.setGeometry(QtCore.QRect(930, 540, 80, 80))
        self.TshirtTabNextBT.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/logos/logos/PreviousBtnFm - Copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TshirtTabNextBT.setIcon(icon2)
        self.TshirtTabNextBT.setIconSize(QtCore.QSize(100, 100))
        self.TshirtTabNextBT.setObjectName("TshirtTabNextBT")
        self.TshirtTabPreviousBT = QtWidgets.QPushButton(self.TshirtTab)
        self.TshirtTabPreviousBT.setGeometry(QtCore.QRect(90, 540, 80, 80))
        self.TshirtTabPreviousBT.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/logos/logos/PreviousBtnFm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TshirtTabPreviousBT.setIcon(icon3)
        self.TshirtTabPreviousBT.setIconSize(QtCore.QSize(100, 100))
        self.TshirtTabPreviousBT.setObjectName("TshirtTabPreviousBT")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/logos/logos/t-shirt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CategoryTab.addTab(self.TshirtTab, icon4, "")
        self.PantTab = QtWidgets.QWidget()
        self.PantTab.setObjectName("PantTab")
        self.PantLabel = QtWidgets.QLabel(self.PantTab)
        self.PantLabel.setGeometry(QtCore.QRect(490, 40, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.PantLabel.setFont(font)
        self.PantLabel.setStyleSheet("color:white;")
        self.PantLabel.setObjectName("PantLabel")
        self.PantTabviewImage = QtWidgets.QLabel(self.PantTab)
        self.PantTabviewImage.setGeometry(QtCore.QRect(370, 190, 371, 291))
        self.PantTabviewImage.setText("")
        self.PantTabviewImage.setPixmap(QtGui.QPixmap(":/logos/logos/hanger (1).png"))
        self.PantTabviewImage.setScaledContents(True)
        self.PantTabviewImage.setObjectName("PantTabviewImage")
        self.PantTabDeleteBT = QtWidgets.QPushButton(self.PantTab)
        self.PantTabDeleteBT.setGeometry(QtCore.QRect(960, 40, 91, 131))
        self.PantTabDeleteBT.setText("")
        self.PantTabDeleteBT.setIcon(icon1)
        self.PantTabDeleteBT.setIconSize(QtCore.QSize(100, 100))
        self.PantTabDeleteBT.setObjectName("PantTabDeleteBT")
        self.PantTabPreviousBT = QtWidgets.QPushButton(self.PantTab)
        self.PantTabPreviousBT.setGeometry(QtCore.QRect(90, 540, 80, 80))
        self.PantTabPreviousBT.setText("")
        self.PantTabPreviousBT.setIcon(icon3)
        self.PantTabPreviousBT.setIconSize(QtCore.QSize(100, 100))
        self.PantTabPreviousBT.setObjectName("PantTabPreviousBT")
        self.PantTabNextBT = QtWidgets.QPushButton(self.PantTab)
        self.PantTabNextBT.setGeometry(QtCore.QRect(930, 540, 80, 80))
        self.PantTabNextBT.setText("")
        self.PantTabNextBT.setIcon(icon2)
        self.PantTabNextBT.setIconSize(QtCore.QSize(100, 100))
        self.PantTabNextBT.setObjectName("PantTabNextBT")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/logos/logos/trousers.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CategoryTab.addTab(self.PantTab, icon5, "")
        self.BootTab = QtWidgets.QWidget()
        self.BootTab.setObjectName("BootTab")
        self.BootLabel = QtWidgets.QLabel(self.BootTab)
        self.BootLabel.setGeometry(QtCore.QRect(490, 40, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.BootLabel.setFont(font)
        self.BootLabel.setStyleSheet("color:white;")
        self.BootLabel.setObjectName("BootLabel")
        self.BootTabviewImage = QtWidgets.QLabel(self.BootTab)
        self.BootTabviewImage.setGeometry(QtCore.QRect(370, 190, 371, 291))
        self.BootTabviewImage.setText("")
        self.BootTabviewImage.setPixmap(QtGui.QPixmap(":/logos/logos/hanger (1).png"))
        self.BootTabviewImage.setScaledContents(True)
        self.BootTabviewImage.setObjectName("BootTabviewImage")
        self.BootTabDeleteBT = QtWidgets.QPushButton(self.BootTab)
        self.BootTabDeleteBT.setGeometry(QtCore.QRect(960, 40, 91, 131))
        self.BootTabDeleteBT.setText("")
        self.BootTabDeleteBT.setIcon(icon1)
        self.BootTabDeleteBT.setIconSize(QtCore.QSize(100, 100))
        self.BootTabDeleteBT.setObjectName("BootTabDeleteBT")
        self.BootTabNextBT = QtWidgets.QPushButton(self.BootTab)
        self.BootTabNextBT.setGeometry(QtCore.QRect(930, 540, 80, 80))
        self.BootTabNextBT.setText("")
        self.BootTabNextBT.setIcon(icon2)
        self.BootTabNextBT.setIconSize(QtCore.QSize(100, 100))
        self.BootTabNextBT.setObjectName("BootTabNextBT")
        self.BootTabPreviousBT = QtWidgets.QPushButton(self.BootTab)
        self.BootTabPreviousBT.setGeometry(QtCore.QRect(90, 540, 80, 80))
        self.BootTabPreviousBT.setText("")
        self.BootTabPreviousBT.setIcon(icon3)
        self.BootTabPreviousBT.setIconSize(QtCore.QSize(100, 100))
        self.BootTabPreviousBT.setObjectName("BootTabPreviousBT")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/logos/logos/boots.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CategoryTab.addTab(self.BootTab, icon6, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/logos/logos/fashion.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainTabs.addTab(self.ClosetTab, icon7, "")
        self.ManageTab = QtWidgets.QWidget()
        self.ManageTab.setObjectName("ManageTab")
        self.ManageTabDeleteBT = QtWidgets.QPushButton(self.ManageTab)
        self.ManageTabDeleteBT.setGeometry(QtCore.QRect(1060, 40, 91, 131))
        self.ManageTabDeleteBT.setText("")
        self.ManageTabDeleteBT.setIcon(icon1)
        self.ManageTabDeleteBT.setIconSize(QtCore.QSize(100, 100))
        self.ManageTabDeleteBT.setObjectName("ManageTabDeleteBT")
        self.AddBT = QtWidgets.QPushButton(self.ManageTab)
        self.AddBT.setGeometry(QtCore.QRect(200, 40, 100, 100))
        self.AddBT.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/logos/logos/add12.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AddBT.setIcon(icon8)
        self.AddBT.setIconSize(QtCore.QSize(100, 100))
        self.AddBT.setObjectName("AddBT")
        self.ManageTabviewImage = QtWidgets.QLabel(self.ManageTab)
        self.ManageTabviewImage.setGeometry(QtCore.QRect(470, 250, 371, 291))
        self.ManageTabviewImage.setText("")
        self.ManageTabviewImage.setPixmap(QtGui.QPixmap(":/logos/logos/hanger (1).png"))
        self.ManageTabviewImage.setScaledContents(True)
        self.ManageTabviewImage.setObjectName("ManageTabviewImage")
        self.MSelectcomboBox = QtWidgets.QComboBox(self.ManageTab)
        self.MSelectcomboBox.setGeometry(QtCore.QRect(450, 150, 441, 51))
        self.MSelectcomboBox.setStyleSheet("color:white;\n"
"background-color:#420516;")
        self.MSelectcomboBox.setEditable(False)
        self.MSelectcomboBox.setCurrentText("")
        self.MSelectcomboBox.setObjectName("MSelectcomboBox")
        self.MSelectcomboBox.addItem("None")
        #self.SelectcomboBox.addItem("select Occassion")
        self.MSelectcomboBox.addItem("Upper Wear")
        self.MSelectcomboBox.addItem("Lower Wear")
        self.MSelectcomboBox.addItem("FootWear")  
        self.ManageTabGenerateBT = QtWidgets.QPushButton(self.ManageTab)
        self.ManageTabGenerateBT.setGeometry(QtCore.QRect(1090, 500, 91, 131))
        self.ManageTabGenerateBT.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/logos/logos/play-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ManageTabGenerateBT.setIcon(icon9)
        self.ManageTabGenerateBT.setIconSize(QtCore.QSize(80, 80))
        self.ManageTabGenerateBT.setObjectName("ManageTabGenerateBT")
        self.ADDLabel = QtWidgets.QLabel(self.ManageTab)
        self.ADDLabel.setGeometry(QtCore.QRect(510, 60, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.ADDLabel.setFont(font)
        self.ADDLabel.setStyleSheet("color:white;")
        self.ADDLabel.setObjectName("ADDLabel")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/logos/logos/setting1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainTabs.addTab(self.ManageTab, icon10, "")
        self.RecommendTab = QtWidgets.QWidget()
        self.RecommendTab.setObjectName("RecommendTab")
        self.RecommendTabviewImage = QtWidgets.QLabel(self.RecommendTab)
        self.RecommendTabviewImage.setGeometry(QtCore.QRect(30, 200, 350, 250))
        self.RecommendTabviewImage.setText("")
        self.RecommendTabviewImage.setPixmap(QtGui.QPixmap(":/logos/logos/hanger (1).png"))
        self.RecommendTabviewImage.setScaledContents(True)
        self.RecommendTabviewImage.setObjectName("RecommendTabviewImage")
        self.RecommendTabviewImage1 = QtWidgets.QLabel(self.RecommendTab)
        self.RecommendTabviewImage1.setGeometry(QtCore.QRect(440, 200, 350, 250))
        self.RecommendTabviewImage1.setText("")
        self.RecommendTabviewImage1.setPixmap(QtGui.QPixmap(":/logos/logos/hanger (1).png"))
        self.RecommendTabviewImage1.setScaledContents(True)
        self.RecommendTabviewImage1.setObjectName("RecommendTabviewImage1")
        self.RecommendTabviewImage2 = QtWidgets.QLabel(self.RecommendTab)
        self.RecommendTabviewImage2.setGeometry(QtCore.QRect(850, 200, 350, 250))
        self.RecommendTabviewImage2.setText("")
        self.RecommendTabviewImage2.setPixmap(QtGui.QPixmap(":/logos/logos/hanger (1).png"))
        self.RecommendTabviewImage2.setScaledContents(True)
        self.RecommendTabviewImage2.setObjectName("RecommendTabviewImage2")
        self.RecommendTabNextBT = QtWidgets.QPushButton(self.RecommendTab)
        self.RecommendTabNextBT.setGeometry(QtCore.QRect(1110, 570, 80, 80))
        self.RecommendTabNextBT.setText("")
        self.RecommendTabNextBT.setIcon(icon2)
        self.RecommendTabNextBT.setIconSize(QtCore.QSize(100, 100))
        self.RecommendTabNextBT.setObjectName("RecommendTabNextBT")
        self.RecommendTabPreviousBT = QtWidgets.QPushButton(self.RecommendTab)
        self.RecommendTabPreviousBT.setGeometry(QtCore.QRect(70, 570, 80, 80))
        self.RecommendTabPreviousBT.setText("")
        self.RecommendTabPreviousBT.setIcon(icon3)
        self.RecommendTabPreviousBT.setIconSize(QtCore.QSize(100, 100))
        self.RecommendTabPreviousBT.setObjectName("RecommendTabPreviousBT")
        self.SelectcomboBox = QtWidgets.QComboBox(self.RecommendTab)
        self.SelectcomboBox.setGeometry(QtCore.QRect(30, 40, 381, 51))
        self.SelectcomboBox.setStyleSheet("color:white;\n"
"background-color:#420516;")
        self.SelectcomboBox.setEditable(False)
        self.SelectcomboBox.setCurrentText("")
        self.SelectcomboBox.setObjectName("SelectcomboBox")
        self.SelectcomboBox.addItem("Party")
        self.SelectcomboBox.addItem("Casual")
        self.SelectcomboBox.addItem("Winter")
        self.SelectcomboBox.addItem("Formal")
        self.RecommendTabGenerateBT = QtWidgets.QPushButton(self.RecommendTab)
        self.RecommendTabGenerateBT.setGeometry(QtCore.QRect(1100, 30, 91, 131))
        self.RecommendTabGenerateBT.setText("")
        self.RecommendTabGenerateBT.setIcon(icon9)
        self.RecommendTabGenerateBT.setIconSize(QtCore.QSize(80, 80))
        self.RecommendTabGenerateBT.setObjectName("RecommendTabGenerateBT")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/logos/logos/gjhgjh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainTabs.addTab(self.RecommendTab, icon11, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.MainTabs.setCurrentIndex(2)
        self.CategoryTab.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Heading.setText(_translate("MainWindow", "Dress UP"))
        self.TshirtLabel.setText(_translate("MainWindow", "T-Shirt"))
        self.PantLabel.setText(_translate("MainWindow", "Pants"))
        self.BootLabel.setText(_translate("MainWindow", "Boots"))
        self.ADDLabel.setText(_translate("MainWindow", "Add to Closet"))
import source


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
