from PyQt5.QtWidgets import QWidget,QAbstractItemView,QMessageBox,QMenu,QAction,QFileDialog
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.QtGui import QFont,QCursor,QIcon
from PyQt5.QtSql import QSqlQuery,QSqlQueryModel
from threading import Thread
import os
from UI.UI_PeriodicalIndexWidget import Ui_PeriodicalIndex
from UI.UI_PeriodicalInfoWidget import Ui_PeriodicalInfoView
from MinnanCSIRDB import MainWindow
from CreateDBConnect import SingleDBConnect
from PDFWidget import WidgetPDFStream

eachRecordPerPage =  10

class PeriodicalIndexWidget(QWidget):

    def __init__(self,mainWin=MainWindow):
        super().__init__()
        self.ui = Ui_PeriodicalIndex()
        self.ui.setupUi(self)
        self.mainWin = mainWin

        #设置地区结构树展开
        self.ui.Periodical_treeWidget.expandAll()
       #隐藏第一列
        self.ui.Periodical_treeWidget.hideColumn(1)

        # 应用数据库
        self.sqlQuery = QSqlQuery(SingleDBConnect().DB)
        self.totoalRecord = self.countRecord("")
        self.qryModel = QSqlQueryModel(self)
        self.currentPage = 0
        self.condition = ''
        self.totoalPage = self.countPages()

        #设置表，匹配数据库
        self.ui.PeriodicaltableView.setModel(self.qryModel)
        self.query = "SELECT Title,Author,Summary,Keyword,Name,Riqi,ID from Periodical  "

        self.excuteQuery(self.currentPage*eachRecordPerPage)
        self.initTableView()

        self.updateLabel()

        #设置表格允许右键自定义菜单
        self.ui.PeriodicaltableView.setContextMenuPolicy(Qt.CustomContextMenu)
        #构建右键单击事件
        self.ui.PeriodicaltableView.customContextMenuRequested.connect(self.generateMenu)

        # 信号，切换地区
        self.ui.Periodical_treeWidget.clicked.connect(self.switchArea_callback)
        #信号，查询
        self.ui.QueryBtn.clicked.connect(self.query_callback)
        #信号，回车查询
        self.ui.QuerylineEdit.returnPressed.connect(self.query_callback)
        #信号，向下翻页
        self.ui.PageDownBtn.clicked.connect(self.pageDown_callback)
        #信号，向上翻页
        self.ui.PageUpBtn.clicked.connect(self.pageUp_callback)
        #信号，双击打开详细页查看
        self.ui.PeriodicaltableView.doubleClicked.connect(self.openByDoubleClick_callback)
        #信号，跳转页码,输入框回车信号
        self.ui.gotoPageLineEidit.returnPressed.connect(self.gotoPage)
        #信号，跳转页码，点击跳转按钮
        self.ui.pbn_PageGo.clicked.connect(self.gotoPage)


    def initTableView(self):
        self.ui.PeriodicaltableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableView.setSelectionModel(QAbstractItemView.SingleSelection)
        self.ui.PeriodicaltableView.setAlternatingRowColors(True)
        #设置默认行高
        self.ui.PeriodicaltableView.verticalHeader().setDefaultSectionSize(60)
        self.ui.PeriodicaltableView.setColumnWidth(0, 400)
        #self.ui.PaperstableView.setColumnWidth(2, 400)
        self.ui.PeriodicaltableView.setColumnWidth(2, 580)
        self.ui.PeriodicaltableView.setColumnWidth(3, 150)
        self.qryModel.setHeaderData(0, Qt.Horizontal, "标题")
        self.qryModel.setHeaderData(1, Qt.Horizontal, "作者")
        self.qryModel.setHeaderData(2, Qt.Horizontal, "摘要")
        self.qryModel.setHeaderData(3, Qt.Horizontal, "关键字")
        self.qryModel.setHeaderData(4, Qt.Horizontal, "期刊名")
        self.qryModel.setHeaderData(5, Qt.Horizontal, "刊发日期")
        self.ui.PeriodicaltableView.setColumnHidden(6, True)

    #统计总记录数
    def countRecord(self,condition):
        SqlTotoalQuery = "SELECT 1 from Periodical" + condition
        #print(SqlTotoalQuery)
        try:
            self.sqlQuery.exec(SqlTotoalQuery)
            self.sqlQuery.last()
            return self.sqlQuery.at() + 1
        except Exception:
            print(Exception.__str__())

    #统计总页数
    def countPages(self):
        if self.totoalRecord > 0:
            if self.totoalRecord > eachRecordPerPage:
                countPages = self.totoalRecord//eachRecordPerPage
                if  self.totoalRecord % eachRecordPerPage !=0:
                    return countPages + 1
                else:
                    return countPages
            else:
                return  1
        else:
            return 1

    #刷新标签
    def updateLabel(self):
        self.ui.CurrentPageLable.setText(str(self.currentPage+1))
        self.ui.TotoalPageLable.setText(str(self.totoalPage))
        self.ui.InfoLable.setText("收录资料{0}条".format(str(self.totoalRecord)))

    #执行查询
    def excuteQuery(self,index):
        limit = " limit %d,%d" % (index, eachRecordPerPage)
        query = self.query + self.condition + limit
        self.qryModel.setQuery(query)

    #槽，相应树节点切换
    def switchArea_callback(self):

        item = self.ui.Periodical_treeWidget.currentItem().text(0)
        if item == '期刊':
            self.condition = ""
        else:
            code = int(self.ui.Periodical_treeWidget.currentItem().text(1))
            print(code)
            if code in range(1,19):
                self.condition = " WHERE Class1 LIKE \'%%%s%%\' " % (item)
            elif code in range(100,111):
                self.condition = " WHERE Class1 LIKE \'闽台交流\' AND Class2 LIKE \'%%%s%%\' " % (item)
            elif code in range(201,206):
                self.condition = " WHERE Class1 LIKE \'闽台交流\' AND Class2 LIKE \'艺术交流\'  AND Class3 LIKE \'%%%s%%\' " % (item)
            elif code in range(111,118):
                self.condition = " WHERE Class1 LIKE \'闽南海丝文化\' AND Class2 LIKE \'%%%s%%\' " % (item)
            elif code in range(118,120):
                self.condition = " WHERE Class1 LIKE \'闽南民间信仰\' AND Class2 LIKE \'%%%s%%\' " % (item)
            elif code in range(121,127):
                self.condition = " WHERE Class1 LIKE \'闽南民俗\' AND Class2 LIKE \'%%%s%%\' " % (item)
            elif code in range(127,130):
                self.condition = " WHERE Class1 LIKE \'闽南名人\' AND Class2 LIKE \'%%%s%%\' " % (item)
            elif code in range(130,138):
                self.condition = " WHERE Class1 LIKE \'闽南文物与考古\' AND Class2 LIKE \'%%%s%%\' " % (item)
            elif code in range(138,142):
                self.condition = " WHERE Class1 LIKE \'闽南艺术\' AND Class2 LIKE \'%%%s%%\' " % (item)
            elif code in range(142,149):
                self.condition = " WHERE Class1 LIKE \'闽南宗教\' AND Class2 LIKE \'%%%s%%\' " % (item)
            elif code in range(201,235):
                self.condition = " WHERE Class1 LIKE \'闽南名人\' AND Class2 LIKE \'泉州\' AND Class3 LIKE \'%%%s%%\' " % (item)
            elif code in range(235,241):
                self.condition = " WHERE Class1 LIKE \'闽南名人\' AND Class2 LIKE \'厦门\' AND Class3 LIKE \'%%%s%%\' " % (item)
            elif code in range(241,257):
                self.condition = " WHERE Class1 LIKE \'闽南名人\' AND Class2 LIKE \'漳州\' AND Class3 LIKE \'%%%s%%\' " % (item)
            elif code in range(257,260):
                self.condition = "WHERE Class1 LIKE \'闽南艺术\' AND Class2 LIKE \'工艺美术\' AND Class3 LIKE \'%%%s%%\' " % (item)
            elif code in range(260,267):
                self.condition = " WHERE Class1 LIKE \'闽南艺术\' AND Class2 LIKE \'戏曲\' AND Class3 LIKE \'%%%s%%\' " % (item)
            elif code in range(267,270):
                self.condition = " WHERE Class1 LIKE \'闽南艺术\' AND Class2 LIKE \'音乐\' AND Class3 LIKE \'%%%s%%\' " % (item)
            elif code in range(301,315):
                self.condition = " WHERE Class1 LIKE \'闽南名人\' AND Class2 LIKE \'泉州\' AND Class3 LIKE \'郑成功\' AND Class4 LIKE \'%%%s%%\' " % (item)
            else:
                self.condition = ""

        self.totoalRecord = self.countRecord(self.condition)
        self.totoalPage = self.countPages()
        self.currentPage = 0
        self.excuteQuery(0)
        self.updateLabel()

    #槽，响应向下翻页
    def pageDown_callback(self):
        if self.currentPage < self.totoalPage-1:
            self.currentPage += 1
            self.excuteQuery(self.currentPage*eachRecordPerPage)
            self.updateLabel()
        else:
            return

    #槽，响应向上翻页
    def pageUp_callback(self):
        if self.currentPage == 0:
            return
        else:
            self.currentPage -= 1
            self.excuteQuery(self.currentPage*eachRecordPerPage)
            self.updateLabel()

    #槽，响应页跳转
    def gotoPage(self):
        getPage = self.ui.gotoPageLineEidit.text()
        if getPage.isdigit() :
            page = int(getPage)
            if page > 0 and page <= self.totoalPage:
                self.currentPage = page - 1
                self.excuteQuery(self.currentPage*eachRecordPerPage)
                self.updateLabel()
            else:
                QMessageBox.warning(self, "警告", "请检查页码范围！", QMessageBox.Ok)
                self.ui.gotoPageLineEidit.setText('')
        else:
            QMessageBox.warning(self,"警告","请输入数字页码!",QMessageBox.Ok)
            self.ui.gotoPageLineEidit.setText('')

    #槽，响应查询
    def query_callback(self):
        target = self.ui.QuerylineEdit.text().strip()
        #print(target)
        if target.__len__() == 0:
            self.condition = ""
            return
        else:
            self.condition = " WHERE Title LIKE \'%%%s%%\' or Summary LIKE \'%%%s%%\' or Keyword LIKE \'%%%s%%\' or Author LIKE \'%%%s%%\' or Name LIKE \'%%%s%%\' or AuthorUnit LIKE \'%%%s%%\'  or Year LIKE \'%%%s%%\' " % (target, target, target,target,target,target,target)
            records = self.countRecord(self.condition)
            #查询到记录
            if records > 0:
                self.totoalRecord = records
                self.totoalPage = self.countPages()
                self.currentPage = 0
                self.excuteQuery(0)
                self.updateLabel()
            else:
                #没有查询到记录
                self.condition = ""
                QMessageBox.information(self,"提示","无查询信息！",QMessageBox.Yes)
                return
    #槽，响应双击行打开详细查看页
    def openByDoubleClick_callback(self,index):
        curRec = self.qryModel.record(index.row())
        #print(curRec)
        ID = curRec.value("ID")
        #print(ID)
        query =  "select * from Periodical where ID=?"
        self.sqlQuery.prepare(query)
        self.sqlQuery.bindValue(0,ID)
        self.sqlQuery.exec()
        self.sqlQuery.last()
        title = self.sqlQuery.value("Title")
        periodicalInfoWidget = PeriodicalInfoWidget(self.mainWin, title,self.sqlQuery.value("MD5"))
        periodicalInfoWidget.setTitle(title)
        periodicalInfoWidget.setAuthor(self.sqlQuery.value("Author"))
        periodicalInfoWidget.setAuthorUnit(self.sqlQuery.value("AuthorUnit"))
        periodicalInfoWidget.setSummary(self.sqlQuery.value("Summary"))
        periodicalInfoWidget.setKeyword(self.sqlQuery.value("Keyword"))
        periodicalInfoWidget.setName(self.sqlQuery.value("Name"))
        periodicalInfoWidget.setYear(self.sqlQuery.value("Year"))
        periodicalInfoWidget.setVolume(self.sqlQuery.value("Volume"))
        periodicalInfoWidget.setPeriod(self.sqlQuery.value("Period"))
        periodicalInfoWidget.setPages(self.sqlQuery.value("Pages"))
        periodicalInfoWidget.setRiqi(self.sqlQuery.value("Riqi"))
        periodicalInfoWidget.setFL(self.sqlQuery.value("Class1")+ ' | ' + self.sqlQuery.value("Class2")+ ' | ' + self.sqlQuery.value("Class3")+ ' | ' + self.sqlQuery.value("Class4"))

        self.mainWin.cenTab.addTab(periodicalInfoWidget,title[0:11])
        self.mainWin.cenTab.setCurrentWidget(periodicalInfoWidget)


    #构建表格右键单击事件
    def generateMenu(self,pos):
        menu = QMenu(self)
        item_open = QAction("打开",self)
        item_open.triggered.connect(self.openContextMenu_callback)
        menu.addAction(item_open)
        menu.addSeparator()
        item_fresh = QAction("全部重载（刷新）",self)
        item_fresh.triggered.connect(self.freshContextMenu_callback)
        menu.addAction(item_fresh)
        menu.addSeparator()
        item_firstPage = QAction("首页",self)
        item_firstPage.triggered.connect(self.firstPageContextMenu_callback)
        menu.addAction(item_firstPage)
        item_lastPage = QAction("最后一页",self)
        item_lastPage.triggered.connect(self.lastPageContextMenu_callback)
        menu.addAction(item_lastPage)
        item = menu.exec(QCursor.pos())

    #右键响应打开选中行的详细页
    def openContextMenu_callback(self):
        for index in self.ui.ThesistableView.selectionModel().selectedRows():
            self.openByDoubleClick_callback(index)

    #右键响应回到第一页
    def firstPageContextMenu_callback(self):
        self.currentPage = 0
        self.excuteQuery(self.currentPage*eachRecordPerPage)
        self.updateLabel()

    #右键响应到最后一页
    def lastPageContextMenu_callback(self):
        self.currentPage = self.totoalPage - 1
        self.excuteQuery(self.currentPage * eachRecordPerPage)
        self.updateLabel()

    #右键刷新，全部重载
    def freshContextMenu_callback(self):
        self.condition = ""
        self.currentPage = 0
        self.totoalRecord = self.countRecord(self.condition)
        self.totoalPage = self.countPages()
        self.excuteQuery(self.currentPage*eachRecordPerPage)
        self.updateLabel()


#重要报刊资料详细页
class PeriodicalInfoWidget(QWidget):
    signal_SaveOver = pyqtSignal(str)

    def __init__(self,mainWin=MainWindow,Title=str,MD5=str):
        super().__init__()
        self.ui = Ui_PeriodicalInfoView()
        self.ui.setupUi(self)
        self.mainWin = mainWin
        self.Title =Title
        self.MD5 = MD5

        #如果没有MD5值，代表没有PDF文件，设置不可读不可下载
        if self.MD5 == "":
            self.ui.btn_pdfRead.setEnabled(False)
            self.ui.btn_pdfDownload.setEnabled(False)
        else:
            self.query = QSqlQuery(SingleDBConnect().DB)



        font = QFont()
        font.setPixelSize(32)
        font.setBold(True)
        self.ui.label_Title.setFont(font)

        #槽，阅读
        self.ui.btn_pdfRead.clicked.connect(self.on_PDFReader)
        self.ui.btn_pdfDownload.clicked.connect(self.on_SavePDF)

        #槽，信号处理
        self.signal_SaveOver.connect(self.onSignalSaveOver)


    def setTitle(self,value):
        self.ui.label_Title.setText(value)

    def setAuthor(self,value):
        self.ui.label_Author.setText(value)

    def setAuthorUnit(self,value):
        self.ui.label_AuthorUnit.setText(value)

    def setSummary(self, value):
        self.ui.label_Summary.setText(value)

    def setKeyword(self, value):
        self.ui.label_Keyword.setText(value)

    def setName(self,value):
        self.ui.label_Name.setText(value)

    def setYear(self,value):
        self.ui.label_Year.setText(value)

    def setVolume(self,value):
        self.ui.label_Volume.setText(value)

    def setPeriod(self,value):
        self.ui.label_Period.setText(value)

    def setPages(self,value):
        self.ui.label_Pages.setText(value)

    def setRiqi(self,value):
        self.ui.label_PubDate.setText(value)

    def setFL(self,value):
        self.ui.label_FL.setText(value)



    #阅读PDF
    def on_PDFReader(self,):

        bin = self.getPDFStream(self.MD5)
        if bin != None:
            tab = WidgetPDFStream(bin,self.Title)
            self.mainWin.cenTab.addTab(tab,QIcon(":/PIC/阅读.png"),self.Title[0:12])
            self.mainWin.cenTab.setCurrentWidget(tab)
        else:
            QMessageBox.information(self,"提示","找不到文档文件。")

    #下载PDF
    def on_SavePDF(self,):
        filePath, fname = os.path.split(os.path.abspath("./" + self.Title + ".pdf"))
        newfileName, ok = QFileDialog.getSaveFileName(self, "文件下载到", fname, "*.pdf")
        #print(newfileName)
        if ok:
            def func():
                with open(newfileName,'wb') as wbf:
                    fileBinary = self.getPDFStream(self.MD5)
                    wbf.write(fileBinary)
                self.signal_SaveOver.emit(fname)
            saveThread = Thread(target=func)
            saveThread.start()
        else:
            return

    def onSignalSaveOver(self,title):
        QMessageBox.information(self, "提示", title + "文件下载成功！")
    #阅读辅助函数，负责查询，辅助返回PDF流，提供阅读或下载PDF函数使用
    def getPDFStream(self,md5):
        sqQuery = "select FileBinary from PeriodicalFile where md5=?"
        self.query.prepare(sqQuery)
        self.query.bindValue(0, self.MD5)
        self.query.exec()
        self.query.last()
        return self.query.value("FileBinary")
