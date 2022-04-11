import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QTabWidget

from CustomWidget import ExpertListWidget

from UI.UI_MainWin import Ui_MainWindow

from PyQt5.QtSql import QSqlQuery

from CreateDBConnect import SingleDBConnect


#主窗口
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        SingleDBConnect()

        # 设置标签主显示页
        self.cenTab = QTabWidget()
        self.cenTab.setTabsClosable(True)
        self.cenTab.tabCloseRequested.connect(self.on_cenTab_close)
        self.setCentralWidget(self.cenTab)

        self.cenTab.addTab(ExpertListWidget(self),"学者专家")


    #槽函数，关闭当前标签页
    def on_cenTab_close(self,index):
        self.cenTab.removeTab(index)
if __name__ == "__main__":
    mainApp = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.showMaximized()
    sys.exit(mainApp.exec_())