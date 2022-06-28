import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QTabWidget
from UI.UI_MainWin import Ui_MainWindow

#主窗口
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 设置标签主显示页
        self.cenTab = QTabWidget()
        self.cenTab.setTabsClosable(True)
        self.cenTab.tabCloseRequested.connect(self.on_cenTab_close)
        self.setCentralWidget(self.cenTab)

        from ExpertWidget import ExpertIndexWidget
        self.cenTab.addTab(ExpertIndexWidget(self),"《学者专家库》")
        from InstitutionWidget import InstitutionIndexWidget
        self.cenTab.addTab(InstitutionIndexWidget(self),"《机 构 库》")


    #槽函数，关闭当前标签页
    def on_cenTab_close(self,index):
        self.cenTab.removeTab(index)
if __name__ == "__main__":
    mainApp = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.showMaximized()
    sys.exit(mainApp.exec_())