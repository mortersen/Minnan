# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/PIC/5450270016495582741.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_home = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/PIC/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_home.setIcon(icon1)
        self.action_home.setObjectName("action_home")
        self.action_close = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/PIC/退出.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_close.setIcon(icon2)
        self.action_close.setObjectName("action_close")
        self.action_quit = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/PIC/Quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_quit.setIcon(icon3)
        self.action_quit.setObjectName("action_quit")
        self.action_historyDB = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/PIC/古籍.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_historyDB.setIcon(icon4)
        self.action_historyDB.setObjectName("action_historyDB")
        self.action_modernDB = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/PIC/现代研究.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_modernDB.setIcon(icon5)
        self.action_modernDB.setObjectName("action_modernDB")
        self.action_institutionDB = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/PIC/机构.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_institutionDB.setIcon(icon6)
        self.action_institutionDB.setObjectName("action_institutionDB")
        self.action_expertDB = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/PIC/专家.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_expertDB.setIcon(icon7)
        self.action_expertDB.setObjectName("action_expertDB")
        self.toolBar.addAction(self.action_home)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_expertDB)
        self.toolBar.addAction(self.action_institutionDB)
        self.toolBar.addAction(self.action_historyDB)
        self.toolBar.addAction(self.action_modernDB)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_close)
        self.toolBar.addAction(self.action_quit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "闽南文化研究信息资源数据库"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_home.setText(_translate("MainWindow", "主页"))
        self.action_home.setToolTip(_translate("MainWindow", "主页面"))
        self.action_close.setText(_translate("MainWindow", "关闭"))
        self.action_close.setToolTip(_translate("MainWindow", "关闭当前页"))
        self.action_quit.setText(_translate("MainWindow", "退出"))
        self.action_quit.setToolTip(_translate("MainWindow", "退出数据库"))
        self.action_historyDB.setText(_translate("MainWindow", "历史文献库"))
        self.action_historyDB.setToolTip(_translate("MainWindow", "打开历史文献库"))
        self.action_modernDB.setText(_translate("MainWindow", "现代研究成果库"))
        self.action_modernDB.setToolTip(_translate("MainWindow", "打开现代研究成果库"))
        self.action_institutionDB.setText(_translate("MainWindow", "研究机构库"))
        self.action_institutionDB.setToolTip(_translate("MainWindow", "打开研究机构库"))
        self.action_expertDB.setText(_translate("MainWindow", "专家学者库"))
        self.action_expertDB.setToolTip(_translate("MainWindow", "打开专家学者库"))
import RES.img_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
