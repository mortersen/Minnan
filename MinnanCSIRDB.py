import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QTabWidget,QWidget
from PyQt5.Qt import QIcon
from UI.UI_MainWin import Ui_MainWindow
from UI.UI_MainWidget import Ui_MainWidget
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
        #打开对应的数据库
        self.ui.action_BookDB.triggered.connect(self.on_openBookDB)
        self.ui.action_expertDB.triggered.connect(self.on_openExpertDB)
        self.ui.action_institutionDB.triggered.connect(self.on_openInstitutionDB)
        self.ui.action_PapersDB.triggered.connect(self.on_openPapersDB)
        self.ui.action_PeriodicalDB.triggered.connect(self.on_openPeriodicalDB)
        self.ui.Action_meetDB.triggered.connect(self.on_openMeetDB)
        self.ui.action_historyDB.triggered.connect(self.on_openHistroyDB)
        self.ui.action_ThesisDB.triggered.connect(self.on_openThesisDB)

        #打开简介主页面
        self.ui.action_home.triggered.connect(self.on_openHome)

        # 设置标签主显示页
        self.cenTab = QTabWidget()
        self.cenTab.setTabsClosable(True)
        self.cenTab.tabCloseRequested.connect(self.on_cenTab_close)
        self.setCentralWidget(self.cenTab)

        #简介主页面
        self.home = MainWidget()
        #专家库
        from ExpertWidget import ExpertIndexWidget
        self.expert = ExpertIndexWidget(self)
        #机构库
        from InstitutionWidget import InstitutionIndexWidget
        self.institution=InstitutionIndexWidget(self)
        #重要报刊库
        from PapersWidget import PapersIndexWidget
        self.papers = PapersIndexWidget(self)
        #学位论文库
        from ThesisWidget import ThesisIndexWidget
        self.thesis = ThesisIndexWidget(self)
        #图书库
        from BookWidget import BookIndexWidget
        self.book = BookIndexWidget(self)
        #会议论文库
        from MeetThesisWidget import MeetThesisIndexWidget
        self.meetThesis = MeetThesisIndexWidget(self)
        #期刊库
        from PeriodicalWidget import PeriodicalIndexWidget
        self.periodical = PeriodicalIndexWidget(self)
        #历史文献库
        from HistoryWidget import HistoryIndexWidget
        self.history = HistoryIndexWidget(self)

        self.ui.action_home.triggered.emit()

    #槽函数，关闭当前标签页
    def on_cenTab_close(self,index):
        self.cenTab.removeTab(index)
    # 槽函数，关闭当前标签页
    def on_closeCurrentTab(self):
        while self.cenTab.count() > 0:
            self.cenTab.removeTab(self.cenTab.currentIndex())
    #槽函数，最小化窗口
    def on_miniWidget(self):
        if self.isFullScreen():
            self.showMinimized()
        else:
            self.showFullScreen()

    #槽，打开简介主页面
    def on_openHome(self):
        self.cenTab.insertTab(0,self.home,QIcon(":/PIC/home.png"),"数据库简介")
        self.cenTab.setCurrentWidget(self.home)
    #槽，打开对应的数据库页
    def on_openBookDB(self):
        self.cenTab.insertTab(0,self.book,QIcon(":/PIC/图书.png"),"现代｜图书库",)
        self.cenTab.setCurrentWidget(self.book)
    def on_openExpertDB(self):
        self.cenTab.insertTab(0,self.expert, QIcon(":/PIC/专家.png"),"｜专家学者库｜")
        self.cenTab.setCurrentWidget(self.expert)
    def on_openInstitutionDB(self):
        self.cenTab.insertTab(0, self.institution, QIcon(":/PIC/机构.png"),"｜机 构 库｜")
        self.cenTab.setCurrentWidget(self.institution)
    def on_openPapersDB(self):
        self.cenTab.insertTab(0, self.papers,QIcon(":/PIC/报纸.png"), "现代｜报刊库")
        self.cenTab.setCurrentWidget(self.papers)
    def on_openPeriodicalDB(self):
        self.cenTab.insertTab(0, self.periodical, QIcon(":/PIC/期刊.png"),"现代｜期刊库")
        self.cenTab.setCurrentWidget(self.periodical)
    def on_openMeetDB(self):
        self.cenTab.insertTab(0, self.meetThesis, QIcon(":/PIC/会议.png"),"现代｜会议论文库")
        self.cenTab.setCurrentWidget(self.meetThesis)
    def on_openHistroyDB(self):
        self.cenTab.insertTab(0, self.history, QIcon(":/PIC/古籍.png"),"｜历史文献库｜")
        self.cenTab.setCurrentWidget(self.history)
    def on_openThesisDB(self):
        self.cenTab.insertTab(0, self.thesis, QIcon(":/PIC/论文.png"),"现代｜学位论文库")
        self.cenTab.setCurrentWidget(self.thesis)



class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWidget()
        self.ui.setupUi(self)



if __name__ == "__main__":
    mainApp = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.showFullScreen()
    sys.exit(mainApp.exec_())