from PyQt5.QtWidgets import QWidget,QAbstractItemView,QMessageBox,QMenu,QAction,QFileDialog
from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.QtGui import QFont,QCursor,QIcon
from PyQt5.QtSql import QSqlQuery,QSqlQueryModel
from threading import Thread
import os
from UI.UI_BookIndexWidget import Ui_BookIndex
from UI.UI_BookInfoWidget import Ui_BookInfoView
from MinnanCSIRDB import MainWindow
from CreateDBConnect import SingleDBConnect
from PDFWidget import WidgetPDFStream

eachRecordPerPage =  10

class BookIndexWidget(QWidget):

    def __init__(self,mainWin=MainWindow):
        super().__init__()
        self.ui = Ui_BookIndex()
        self.ui.setupUi(self)
        self.mainWin = mainWin

        #设置地区结构树展开
        self.ui.Book_treeWidget.expandAll()
       #隐藏第一列
        self.ui.Book_treeWidget.hideColumn(1)

        # 应用数据库
        self.sqlQuery = QSqlQuery(SingleDBConnect().DB)
        self.totoalRecord = self.countRecord("")
        self.qryModel = QSqlQueryModel(self)
        self.currentPage = 0
        self.condition = ''
        self.totoalPage = self.countPages()

        #设置表，匹配数据库
        self.ui.BooktableView.setModel(self.qryModel)
        self.query = "SELECT Title,Author,Summary,Press,PubDate,ID from Book  "

        self.excuteQuery(self.currentPage*eachRecordPerPage)
        self.initTableView()

        self.updateLabel()

        #设置表格允许右键自定义菜单
        self.ui.BooktableView.setContextMenuPolicy(Qt.CustomContextMenu)
        #构建右键单击事件
        self.ui.BooktableView.customContextMenuRequested.connect(self.generateMenu)

        # 信号，切换地区
        self.ui.Book_treeWidget.clicked.connect(self.switchArea_callback)
        #信号，查询
        self.ui.QueryBtn.clicked.connect(self.query_callback)
        #信号，回车查询
        self.ui.QuerylineEdit.returnPressed.connect(self.query_callback)
        #信号，向下翻页
        self.ui.PageDownBtn.clicked.connect(self.pageDown_callback)
        #信号，向上翻页
        self.ui.PageUpBtn.clicked.connect(self.pageUp_callback)
        #信号，双击打开详细页查看
        self.ui.BooktableView.doubleClicked.connect(self.openByDoubleClick_callback)
        #信号，跳转页码,输入框回车信号
        self.ui.gotoPageLineEidit.returnPressed.connect(self.gotoPage)
        #信号，跳转页码，点击跳转按钮
        self.ui.pbn_PageGo.clicked.connect(self.gotoPage)


    def initTableView(self):
        self.ui.BooktableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableView.setSelectionModel(QAbstractItemView.SingleSelection)
        self.ui.BooktableView.setAlternatingRowColors(True)
        #设置默认行高
        self.ui.BooktableView.verticalHeader().setDefaultSectionSize(60)
        self.ui.BooktableView.setColumnWidth(0, 400)
        #self.ui.PaperstableView.setColumnWidth(2, 400)
        self.ui.BooktableView.setColumnWidth(2, 580)
        self.ui.BooktableView.setColumnWidth(3, 150)
        self.qryModel.setHeaderData(0, Qt.Horizontal, "书名")
        self.qryModel.setHeaderData(1, Qt.Horizontal, "作者")
        self.qryModel.setHeaderData(2, Qt.Horizontal, "摘要")
        self.qryModel.setHeaderData(3, Qt.Horizontal, "出版社")
        self.qryModel.setHeaderData(4, Qt.Horizontal, "出版日期")
        self.ui.BooktableView.setColumnHidden(5, True)

    #统计总记录数
    def countRecord(self,condition):
        SqlTotoalQuery = "SELECT 1 from Book" + condition
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

        item = self.ui.Book_treeWidget.currentItem().text(0)
        if item == '图书':
            self.condition = ""
        else:
            code = int(self.ui.Book_treeWidget.currentItem().text(1))
            print(code)
            if code in range(50,53):
                self.condition = " WHERE Class1 LIKE \'闽南艺术\' AND Class2 LIKE \'音乐\' AND  Class3 LIKE \'%%%s%%\' " % (item)
            elif code in range(33,37):
                self.condition = " WHERE Class1 LIKE \'闽南名人\' AND Class2 LIKE \'漳州\' AND Class3 LIKE \'%%%s%%\' " % (item)
            elif code  in range(29,32):
                self.condition = " WHERE Class1 LIKE \'闽南名人\' AND Class2 LIKE \'厦门\' AND Class3 LIKE \'%%%s%%\' " % (item)
            elif code in range(19,28):
                self.condition = " WHERE Class1 LIKE \'闽南名人\' AND Class2 LIKE \'泉州\' AND Class3 LIKE \'%%%s%%\' " % (item)
            elif code in range(7,10):
                self.condition = " WHERE Class1 LIKE \'现代方志\' AND Class2  LIKE \'%%%s%%\' " % (item)
            elif code in range(17,19) or code == 28 or code == 32:
                self.condition = " WHERE Class1 LIKE \'闽南名人\' AND Class2 LIKE \'%%%s%%\' " % (item)
            elif code in range(43,46):
                self.condition = " WHERE Class1 LIKE \'闽南文史资料\' AND Class2 LIKE \'%%%s%%\' " % (item)
            elif code in range(53,57) or code == 49:
                self.condition = " WHERE Class1 LIKE \'闽南艺术\' AND Class2 LIKE \'%%%s%%\' " % (item)
            else:
                self.condition = " WHERE Class1 LIKE \'%%%s%%\' " % (item)

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
            self.condition = " WHERE Title LIKE \'%%%s%%\' or Summary LIKE \'%%%s%%\' or Keyword LIKE \'%%%s%%\' or Author LIKE \'%%%s%%\' or Press LIKE \'%%%s%%\' or SeriesName LIKE \'%%%s%%\' or Category LIKE \'%%%s%%\' " % (target, target, target,target,target,target,target)
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
        query =  "select * from Book where ID=?"
        self.sqlQuery.prepare(query)
        self.sqlQuery.bindValue(0,ID)
        self.sqlQuery.exec()
        self.sqlQuery.last()
        title = self.sqlQuery.value("Title")
        bookInfoWidget = BookInfoWidget(self.mainWin, title,self.sqlQuery.value("MD5"))
        bookInfoWidget.setTitle(title)
        bookInfoWidget.setAuthor(self.sqlQuery.value("Author"))
        bookInfoWidget.setSeriesName(self.sqlQuery.value("SeriesName"))
        bookInfoWidget.setSummary(self.sqlQuery.value("Summary"))
        bookInfoWidget.setKeyword(self.sqlQuery.value("Keyword"))
        bookInfoWidget.setPress(self.sqlQuery.value("Press"))
        bookInfoWidget.setCategory(self.sqlQuery.value("Category"))
        bookInfoWidget.setVolume(self.sqlQuery.value("Volume"))
        bookInfoWidget.setCe(self.sqlQuery.value("Ce"))
        bookInfoWidget.setPages(self.sqlQuery.value("Pages"))
        bookInfoWidget.setPubDate(self.sqlQuery.value("PubDate"))

        bookInfoWidget.setFL(self.sqlQuery.value("Class1")+ ' | ' + self.sqlQuery.value("Class2") + ' | ' + self.sqlQuery.value("Class3"))

        self.mainWin.cenTab.addTab(bookInfoWidget,title[0:11])
        self.mainWin.cenTab.setCurrentWidget(bookInfoWidget)


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
class BookInfoWidget(QWidget):
    signal_SaveOver = pyqtSignal(str)

    def __init__(self,mainWin=MainWindow,Title=str,MD5=str):
        super().__init__()
        self.ui = Ui_BookInfoView()
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

    def setSeriesName(self,value):
        self.ui.label_SeriesName.setText(value)

    def setSummary(self,value):
        self.ui.label_Summary.setText(value)

    def setKeyword(self,value):
        self.ui.label_Keyword.setText(value)

    def setPress(self,value):
        self.ui.label_Press.setText(value)

    def setCategory(self,value):
        self.ui.label_Category.setText(value)

    def setVolume(self,value):
        self.ui.label_Volume.setText(value)

    def setCe(self,value):
        self.ui.label_Ce.setText(value)

    def setPages(self,value):
        self.ui.label_Pages.setText(value)

    def setPubDate(self,value):
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
        sqQuery = "select FileBinary from BookFile where md5=?"
        self.query.prepare(sqQuery)
        self.query.bindValue(0, self.MD5)
        self.query.exec()
        self.query.last()
        return self.query.value("FileBinary")
