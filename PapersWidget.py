from PyQt5.QtWidgets import QWidget,QAbstractItemView,QMessageBox,QMenu,QAction,QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont,QCursor
from PyQt5.QtSql import QSqlQuery,QSqlQueryModel
from threading import Thread
import os ,fitz
from UI.UI_PapersIndexWidget import Ui_PapersIndex
from UI.UI_PaperInfoWidget import Ui_PaperInfoView
from MinnanCSIRDB import MainWindow
from CreateDBConnect import SingleDBConnect
from PDFWidget import WidgetPDFStream

eachRecordPerPage =  10

class PapersIndexWidget(QWidget):

    def __init__(self,mainWin=MainWindow):
        super().__init__()
        self.ui = Ui_PapersIndex()
        self.ui.setupUi(self)
        self.mainWin = mainWin

        #设置地区结构树展开
        self.ui.Papers_treeWidget.expandAll()
       #隐藏第一列
        self.ui.Papers_treeWidget.hideColumn(1)

        # 应用数据库
        self.sqlQuery = QSqlQuery(SingleDBConnect().DB)
        self.totoalRecord = self.countRecord("")
        self.qryModel = QSqlQueryModel(self)
        self.currentPage = 0
        self.condition = ''
        self.totoalPage = self.countPages()

        #设置表，匹配数据库
        self.ui.PaperstableView.setModel(self.qryModel)
        self.query = "SELECT Title,Author,PaperName,Summary,Class1,ID from Papers  "

        self.excuteQuery(self.currentPage*eachRecordPerPage)
        self.initTableView()

        self.updateLabel()

        #设置表格允许右键自定义菜单
        self.ui.PaperstableView.setContextMenuPolicy(Qt.CustomContextMenu)
        #构建右键单击事件
        self.ui.PaperstableView.customContextMenuRequested.connect(self.generateMenu)

        # 信号，切换地区
        self.ui.Papers_treeWidget.clicked.connect(self.switchArea_callback)
        #信号，查询
        self.ui.QueryBtn.clicked.connect(self.query_callback)
        #信号，回车查询
        self.ui.QuerylineEdit.returnPressed.connect(self.query_callback)
        #信号，向下翻页
        self.ui.PageDownBtn.clicked.connect(self.pageDown_callback)
        #信号，向上翻页
        self.ui.PageUpBtn.clicked.connect(self.pageUp_callback)
        #信号，双击打开详细页查看
        self.ui.PaperstableView.doubleClicked.connect(self.openByDoubleClick_callback)


    def initTableView(self):
        self.ui.PaperstableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableView.setSelectionModel(QAbstractItemView.SingleSelection)
        self.ui.PaperstableView.setAlternatingRowColors(True)
        #设置默认行高
        self.ui.PaperstableView.verticalHeader().setDefaultSectionSize(60)
        self.ui.PaperstableView.setColumnWidth(0, 500)
        #self.ui.PaperstableView.setColumnWidth(2, 400)
        self.ui.PaperstableView.setColumnWidth(3, 500)
        #self.ui.PaperstableView.setColumnWidth(4, 600)
        self.qryModel.setHeaderData(0, Qt.Horizontal, "标题")
        self.qryModel.setHeaderData(1, Qt.Horizontal, "作者")
        self.qryModel.setHeaderData(2, Qt.Horizontal, "报刊名称")
        self.qryModel.setHeaderData(3, Qt.Horizontal, "内容简介")
        self.qryModel.setHeaderData(4, Qt.Horizontal, "分类")
        self.ui.PaperstableView.setColumnHidden(5, True)

    #统计总记录数
    def countRecord(self,condition):
        SqlTotoalQuery = "SELECT 1 from Papers" + condition
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

        item = self.ui.Papers_treeWidget.currentItem().text(0)
        if item == '重要报刊资料':
            self.condition = ""
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

    #槽，响应查询
    def query_callback(self):
        target = self.ui.QuerylineEdit.text().strip()
        #print(target)
        if target.__len__() == 0:
            self.condition = ""
            return
        else:
            self.condition = " WHERE Title LIKE \'%%%s%%\' or Summary LIKE \'%%%s%%\' or Keyword LIKE \'%%%s%%\' or Author LIKE \'%%%s%%\' or AuthorUnit LIKE \'%%%s%%\' or PaperName LIKE \'%%%s%%\' or PubYear LIKE \'%%%s%%\' " % (target, target, target,target,target,target,target)
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
        query =  "select * from Papers where ID=?"
        self.sqlQuery.prepare(query)
        self.sqlQuery.bindValue(0,ID)
        self.sqlQuery.exec()
        self.sqlQuery.last()
        title = self.sqlQuery.value("Title")
        paperInfoWidget = PaperInfoWidget(self.mainWin, title,self.sqlQuery.value("MD5"))
        paperInfoWidget.setTitle(title)
        paperInfoWidget.setAuthor(self.sqlQuery.value("Author"))
        paperInfoWidget.setAuthorUnit(self.sqlQuery.value("AuthorUnit"))
        paperInfoWidget.setSummary(self.sqlQuery.value("Summary"))
        paperInfoWidget.setKeyword(self.sqlQuery.value("Keyword"))
        paperInfoWidget.setPaperName(self.sqlQuery.value("PaperName"))
        paperInfoWidget.setVersionName(self.sqlQuery.value("VersionName"))
        paperInfoWidget.setVersionNO(self.sqlQuery.value("VersionNO"))
        paperInfoWidget.setPubYear(self.sqlQuery.value("PubYear"))
        paperInfoWidget.setPubDate(self.sqlQuery.value("PubDate"))
        paperInfoWidget.setClass(self.sqlQuery.value("Class1"))

        self.mainWin.cenTab.addTab(paperInfoWidget,title[0:11])
        self.mainWin.cenTab.setCurrentWidget(paperInfoWidget)


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
        for index in self.ui.PaperstableView.selectionModel().selectedRows():
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
class PaperInfoWidget(QWidget):

    def __init__(self,mainWin=MainWindow,Title=str,MD5=str):
        super().__init__()
        self.ui = Ui_PaperInfoView()
        self.ui.setupUi(self)
        self.mainWin = mainWin
        self.Title =Title
        self.MD5 = MD5
        #如果没有MD5值，代表没有PDF文件，设置不可读不可下载
        if self.MD5 == "":
            self.ui.btn_pdfRead.setText(False)
            self.ui.btn_pdfDownload.setEnabled(False)
        else:
            self.query = QSqlQuery(SingleDBConnect().DB)


        font = QFont()
        font.setPixelSize(32)
        font.setBold(True)
        self.ui.label_Title.setFont(font)

        #槽，阅读
        self.ui.btn_pdfRead.clicked.connect(self.on_PDFReader)


    def setTitle(self,value):
        self.ui.label_Title.setText(value)

    def setAuthor(self,value):
        self.ui.label_Author.setText(value)

    def setAuthorUnit(self,value):
        self.ui.label_AuthorUnit.setText(value)

    def setSummary(self,value):
        self.ui.label_Summary.setText(value)

    def setKeyword(self,value):
        self.ui.label_Keyword.setText(value)

    def setPaperName(self,value):
        self.ui.label_PaperName.setText(value)

    def setVersionName(self,value):
        self.ui.label_VersionName.setText(value)

    def setVersionNO(self,value):
        self.ui.label_VersionNO.setText(value)

    def setPubYear(self,value):
        self.ui.label_PubYear.setText(value)

    def setPubDate(self,value):
        self.ui.label_PubDate.setText(value)

    def setClass(self,value):
        self.ui.label_FL.setText(value)

    #阅读PDF
    def on_PDFReader(self,):

        bin = self.getPDFStream(self.MD5)
        if bin != None:
            tab = WidgetPDFStream(bin,self.Title)
            self.mainWin.cenTab.addTab(tab,"【阅】"+self.Title[0:12])
            self.mainWin.cenTab.setCurrentWidget(tab)
        else:
            QMessageBox.information(self,"提示","找不到文档文件。")

    #阅读辅助函数，负责查询，辅助返回PDF流，提供阅读PDF函数使用
    def getPDFStream(self,md5):
        sqQuery = "select FileBinary from PapersFile where md5=?"
        self.query.prepare(sqQuery)
        self.query.bindValue(0, self.MD5)
        self.query.exec()
        self.query.last()
        return self.query.value("FileBinary")
