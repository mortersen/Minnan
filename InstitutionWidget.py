from PyQt5.QtWidgets import QWidget,QAbstractItemView,QMessageBox,QMenu,QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont,QCursor
from PyQt5.QtSql import QSqlQuery,QSqlQueryModel
from UI.UI_InstitutionIndexWidget import Ui_InstitutionIndex
from UI.UI_InstitutionInfoWidget import Ui_InstitutionInfoWidget
from MinnanCSIRDB import MainWindow
from CreateDBConnect import SingleDBConnect

eachRecordPerPage =  10
areaCode = {"地区":"","北京":"BJDQ","福建":"FJDQ","大陆其他地区":"DLQT","海外地区":"HWDQ","福州":"FZ","泉州":"QZ","泉州厦门":"QZXM","厦门":"XM","漳州":"ZZ","省内其他":"FJQT"}

#机构库首页面
class InstitutionIndexWidget(QWidget):

    def __init__(self,mainWin=MainWindow):
        super().__init__()
        self.ui = Ui_InstitutionIndex()
        self.ui.setupUi(self)
        self.mainWin = mainWin

        #设置地区结构树展开
        self.ui.Institution_treeWidget.expandAll()

        # 应用数据库
        self.sqlQuery = QSqlQuery(SingleDBConnect().DB)
        self.totoalRecord = self.countRecord("")
        self.qryModel = QSqlQueryModel(self)
        self.currentPage = 0
        self.condition = ''
        self.totoalPage = self.countPages()

        #设置表，匹配数据库
        self.ui.InstitutiontableView.setModel(self.qryModel)
        self.query = "SELECT Name,Type,AcademicPoint,AcademicJournals,ID from Institution  "

        self.excuteQuery(self.currentPage*eachRecordPerPage)
        self.initTableView()

        self.updateLabel()

        #设置表格允许右键自定义菜单
        self.ui.InstitutiontableView.setContextMenuPolicy(Qt.CustomContextMenu)
        #构建右键单击事件
        self.ui.InstitutiontableView.customContextMenuRequested.connect(self.generateMenu)

        # 信号，切换地区
        self.ui.Institution_treeWidget.clicked.connect(self.switchArea_callback)
        #信号，查询
        self.ui.QueryBtn.clicked.connect(self.query_callback)
        #信号，回车查询
        self.ui.QuerylineEdit.returnPressed.connect(self.query_callback)
        #信号，向下翻页
        self.ui.PageDownBtn.clicked.connect(self.pageDown_callback)
        #信号，向上翻页
        self.ui.PageUpBtn.clicked.connect(self.pageUp_callback)
        #信号，双击打开详细页查看
        self.ui.InstitutiontableView.doubleClicked.connect(self.openByDoubleClick_callback)


    def initTableView(self):
        self.ui.InstitutiontableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableView.setSelectionModel(QAbstractItemView.SingleSelection)
        self.ui.InstitutiontableView.setAlternatingRowColors(True)
        #设置默认行高
        self.ui.InstitutiontableView.verticalHeader().setDefaultSectionSize(60)
        self.ui.InstitutiontableView.setColumnWidth(0, 400)
        self.ui.InstitutiontableView.setColumnWidth(2, 600)
        self.ui.InstitutiontableView.setColumnWidth(3, 400)
        self.qryModel.setHeaderData(0, Qt.Horizontal, "机构名称")
        self.qryModel.setHeaderData(1, Qt.Horizontal, "类型")
        self.qryModel.setHeaderData(2, Qt.Horizontal, "学术指向")
        self.qryModel.setHeaderData(3, Qt.Horizontal, "学术刊物")
        self.ui.InstitutiontableView.setColumnHidden(4, True)

    #统计总记录数
    def countRecord(self,condition):
        SqlTotoalQuery = "SELECT 1 from Institution" + condition
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
        self.ui.InfoLable.setText("收录机构信息{0}家".format(str(self.totoalRecord)))

    #执行查询
    def excuteQuery(self,index):
        limit = " limit %d,%d" % (index, eachRecordPerPage)
        query = self.query + self.condition + limit
        self.qryModel.setQuery(query)

    #槽，相应树节点切换
    def switchArea_callback(self):
        item = areaCode[self.ui.Institution_treeWidget.currentItem().text(0)]
        if item == '':
            self.condition = ""
        elif item in ['BJDQ','FJDQ','DLQT','HWDQ']:
            self.condition = " WHERE AreaClass LIKE \'%%%s%%\' " % (item)
        elif item in ['FZ','QZ','QZXM','XM','ZZ','FJQT']:
            self.condition = " WHERE Area LIKE \'%%%s%%\' " % (item)
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
            self.condition = " WHERE Name LIKE \'%%%s%%\' or AcademicPoint LIKE \'%%%s%%\' or Type LIKE \'%%%s%%\' or AcademicJournals LIKE \'%%%s%%\' or Summary LIKE \'%%%s%%\' or Remark LIKE \'%%%s%%\' or CompetentOrganization LIKE \'%%%s%%\' " % (target, target, target,target,target,target,target)
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
        query =  "select * from Institution where ID=?"
        self.sqlQuery.prepare(query)
        self.sqlQuery.bindValue(0,ID)
        self.sqlQuery.exec()
        self.sqlQuery.last()
        infoInstitutionWidget = InstitutionInfoWidget()
        name = self.sqlQuery.value("Name")
        infoInstitutionWidget.setName(name)
        infoInstitutionWidget.setLocation(self.sqlQuery.value("Location"))
        infoInstitutionWidget.setType(self.sqlQuery.value("Type"))
        infoInstitutionWidget.setSummary(self.sqlQuery.value("Summary"))
        infoInstitutionWidget.setLeadingOfficial(self.sqlQuery.value("LeadingOfficial"))
        infoInstitutionWidget.setLinkman(self.sqlQuery.value("Linkman"))
        infoInstitutionWidget.setContact(self.sqlQuery.value("Contact"))
        infoInstitutionWidget.setPostAddress(self.sqlQuery.value("PostalAddress"))
        infoInstitutionWidget.setWebsite(self.sqlQuery.value("Website"))
        infoInstitutionWidget.setFoundingTime(self.sqlQuery.value("FoundingTime"))
        infoInstitutionWidget.setCompetentOrganization(self.sqlQuery.value("CompetentOrganization"))
        infoInstitutionWidget.setProperty(self.sqlQuery.value("Property"))
        infoInstitutionWidget.setAcademicPoint(self.sqlQuery.value("AcademicPoint"))
        infoInstitutionWidget.setAcademicJournals(self.sqlQuery.value("AcademicJournals"))
        infoInstitutionWidget.setRemark(self.sqlQuery.value("Remark"))
        self.mainWin.cenTab.addTab(infoInstitutionWidget,name[0:11])
        self.mainWin.cenTab.setCurrentWidget(infoInstitutionWidget)


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
        for index in self.ui.InstitutiontableView.selectionModel().selectedRows():
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

#机构信息详细页面
class InstitutionInfoWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_InstitutionInfoWidget()
        self.ui.setupUi(self)
        font = QFont()
        font.setPixelSize(28)
        font.setBold(True)
        self.ui.NameLabel.setFont(font)

    def setName(self,value):
        self.ui.NameLabel.setText(value)

    def setType(self,value):
        self.ui.TypeLabel.setText(value)

    def setLocation(self,value):
        self.ui.LocationLabel.setText(value)

    def setSummary(self,value):
        self.ui.SummarytextEdit.setText(value)

    def setAcademicPoint(self,value):
        self.ui.AcademicPointtextEdit.setText(value)

    def setAcademicJournals(self,value):
        self.ui.AcademicJournalslineEdit.setText(value)

    def setLeadingOfficial(self,value):
        self.ui.LeadingOfficiallineEdit.setText(value)

    def setLinkman(self,value):
        self.ui.LinkManlineEdit.setText(value)

    def setContact(self,value):
        self.ui.ContactlineEdit.setText(value)

    def setPostAddress(self,value):
        self.ui.PostalAddresslineEdit.setText(value)

    def setWebsite(self,value):
        self.ui.WebsitelineEdit.setText(value)

    def setFoundingTime(self,value):
        self.ui.FoundingTimelineEdit.setText(value)

    def setCompetentOrganization(self,value):
        self.ui.CompetentOrganizationlineEdit.setText(value)

    def setProperty(self,value):
        self.ui.PropertylineEdit.setText(value)

    def setRemark(self,value):
        self.ui.RemarktextEdit.setText(value)







