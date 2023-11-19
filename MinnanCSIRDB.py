import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QTabWidget
from UI.UI_MainWin import Ui_MainWindow

#主窗口
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #设置工具栏按钮动作
        #退出程序
        self.ui.action_quit.triggered.connect(self.close)
        #关闭当前页面
        self.ui.action_close.triggered.connect(self.on_closeCurrentTab)
        #最小化界面
        self.ui.action_mini.triggered.connect(self.on_miniWidget)


        # 设置标签主显示页
        self.cenTab = QTabWidget()
        self.cenTab.setTabsClosable(True)
        self.cenTab.tabCloseRequested.connect(self.on_cenTab_close)
        self.setCentralWidget(self.cenTab)

        from ExpertWidget import ExpertIndexWidget,ExpertInfoWidget
        #self.cenTab.addTab(ExpertInfoWidget(),"测试")
        self.cenTab.addTab(ExpertIndexWidget(self),"《学者专家库》")
        # from InstitutionWidget import InstitutionIndexWidget
        # self.cenTab.addTab(InstitutionIndexWidget(self),"《机 构 库》")
        # from PapersWidget import PapersIndexWidget
        # self.cenTab.addTab(PapersIndexWidget(self),"《重要报刊库》")
        # from ThesisWidget import ThesisIndexWidget
        # self.cenTab.addTab(ThesisIndexWidget(self),"《学位论文库》")
        # from BookWidget import BookIndexWidget
        # self.cenTab.addTab(BookIndexWidget(self),"《图书库》")
        #
        # from MeetThesisWidget import MeetThesisIndexWidget
        # self.cenTab.addTab(MeetThesisIndexWidget(self), "《会议论文》")

        from PeriodicalWidget import PeriodicalIndexWidget
        self.cenTab.addTab(PeriodicalIndexWidget(self),"《期刊》")

    #槽函数，关闭当前标签页
    def on_cenTab_close(self,index):
        self.cenTab.removeTab(index)
    # 槽函数，关闭当前标签页
    def on_closeCurrentTab(self):
        self.cenTab.removeTab(self.cenTab.currentIndex())
    #槽函数，最小化窗口
    def on_miniWidget(self):
        if self.isFullScreen():
            self.showMinimized()
        else:
            self.showFullScreen()


if __name__ == "__main__":
    mainApp = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.showFullScreen()
    sys.exit(mainApp.exec_())