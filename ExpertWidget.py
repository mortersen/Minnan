from PyQt5.QtWidgets import QWidget,QAbstractItemView,QMessageBox,QMenu,QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from UI.UI_ExpertListWidget import Ui_ExpertList
from UI.UI_ExpertInfoWidget import Ui_ExpertInfoWidget
from PyQt5.QtSql import QSqlQuery,QSqlQueryModel
from CreateDBConnect import SingleDBConnect
from MinnanCSIRDB import MainWindow

eachRecordPerPage = 22
FirstClass = {"SXZY":"闽南思想及综合研究","MNFY":"闽南方言","WXWX":"闽南文学与文献","MNJZ":"闽南建筑",
              "MNYS":"闽南艺术","MNLX":"闽南理学","MNMS":"闽南民俗","JYSY":"闽南教育与书院","ZJXY":"闽南宗教与民间信仰",
              "JIAZ": "闽南家族","HQHR":"海丝与华侨华人","KGWB":"闽南考古与文博","TWYJ":"台湾研究"}
SecondClass = {"2JYY":"闽南音乐","2JWD":"闽南舞蹈","2JXQ":"闽南戏曲","2JQT":"闽南其他艺术","":""}

ResearchAreaCode = ["","SXZY","MNFY","WXWX","MNJZ","MNYS","2JYY","2JWD","2JXQ","2JQT","MNLX","MNMS","JYSY","ZJXY","JIAZ","HQHR","KGWB","TWYJ"]

#专家学者页面
class ExpertIndexWidget(QWidget):


    def __init__(self,mainWin=MainWindow):
        super().__init__()
        self.ui = Ui_ExpertList()
        self.ui.setupUi(self)
        self.mainWin = mainWin

        #普通数据库链接对象
        self.sqlQuery = QSqlQuery(SingleDBConnect().DB)
        self.totoalRecord = self.countRecord("")
        self.currentPage = 0
        self.condition = ""
        self.totoalPage = self.countPage()

        #与表格关联数据库链接对象
        self.qryModel = QSqlQueryModel(self)
        self.ui.tableView.setModel(self.qryModel)
        self.query = "SELECT Name,ResearchArea,ResearchFindings,FundProject,ID from Expert  "
        self.excuteQuery(self.currentPage*eachRecordPerPage)
        self.initTable()
        self.updateLabel()

        # 设置表格允许右键自定义菜单
        self.ui.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        # 构建右键单击事件
        self.ui.tableView.customContextMenuRequested.connect(self.generateMenu)

        self.ui.pageupBtn.clicked.connect(self.pageUp_callback)
        self.ui.pagedownBtn.clicked.connect(self.pageDown_callback)
        self.ui.researchAreaCombox.currentIndexChanged.connect(self.currentIndexChanged_callback)
        self.ui.reloadBtn.clicked.connect(self.freshContextMenu_callback)
        self.ui.queryBtn.clicked.connect(self.query_callback)
        self.ui.queryforLineEdit.returnPressed.connect(self.query_callback)
        self.ui.pbn_PageGo.clicked.connect(self.gotoPage_callback)
        self.ui.gotoPageLineEidit.returnPressed.connect(self.gotoPage_callback)
        #双击打开详细页
        self.ui.tableView.doubleClicked.connect(self.doubleClick_callback)



    #初始化表格
    def initTable(self):
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableView.setSelectionModel(QAbstractItemView.SingleSelection)
        self.ui.tableView.setAlternatingRowColors(True)
        # 设置默认行高
        self.ui.tableView.verticalHeader().setDefaultSectionSize(60)
        self.ui.tableView.setColumnWidth(0, 200)
        self.ui.tableView.setColumnWidth(1, 600)
        self.ui.tableView.setColumnWidth(2, 800)
        self.ui.tableView.setColumnWidth(3, 900)
        self.qryModel.setHeaderData(0, Qt.Horizontal, "姓名")
        self.qryModel.setHeaderData(1, Qt.Horizontal, "研究领域")
        self.qryModel.setHeaderData(2, Qt.Horizontal, "研究成果")
        self.qryModel.setHeaderData(3, Qt.Horizontal, "基金项目")
        self.ui.tableView.setColumnHidden(4, True)

    #更新UI状态
    def updateLabel(self):
        self.ui.currentPageLabel.setText(str(self.currentPage + 1))
        self.ui.totoalPageLabel.setText(str(self.totoalPage))
        self.ui.label_3.setText("共有记录{0}条".format(str(self.totoalRecord)))

    #按条件统计数据库记录数
    def countRecord(self,condition):
        SqlTotoalQuery = "SELECT 1 from Expert" + condition
        try:
            self.sqlQuery.exec(SqlTotoalQuery)
            self.sqlQuery.last()
            return self.sqlQuery.at() + 1
        except Exception:
            print(Exception.__str__())

    # 统计总页数
    def countPage(self):
            if self.totoalRecord > 0:
                if self.totoalRecord > eachRecordPerPage:
                    countPages = self.totoalRecord // eachRecordPerPage
                    if self.totoalRecord % eachRecordPerPage != 0:
                        return countPages + 1
                    else:
                        return countPages
                else:
                    return 1
            else:
                return 1

    #执行表格查询
    def excuteQuery(self,index):
        limit = " limit %d,%d" % (index, eachRecordPerPage)
        query = self.query + self.condition + limit
        self.qryModel.setQuery(query)

    #槽，往前翻页
    def pageUp_callback(self):
        if self.currentPage == 0:
            return
        else:
            self.currentPage -= 1
            self.excuteQuery(self.currentPage*eachRecordPerPage)
            self.updateLabel()

    #槽，向后翻页
    def pageDown_callback(self):
        if self.currentPage < self.totoalPage - 1:
            self.currentPage += 1
            self.excuteQuery(self.currentPage * eachRecordPerPage)
            self.updateLabel()
        else:
            return

    #槽，双击打开详细页
    def doubleClick_callback(self,index):
        curRec = self.qryModel.record(index.row())
        print(curRec)
        ID = curRec.value("ID")
        print(ID)
        query = "select * from Expert where ID=?"
        self.sqlQuery.prepare(query)
        self.sqlQuery.bindValue(0, ID)
        self.sqlQuery.exec()
        self.sqlQuery.last()
        infoExpertWidget = ExpertInfoWidget()
        name = self.sqlQuery.value("Name")
        infoExpertWidget.setName(name)
        infoExpertWidget.setSummary(self.sqlQuery.value("Summary"))
        infoExpertWidget.setPost(self.sqlQuery.value("Post"))
        infoExpertWidget.setRecord(self.sqlQuery.value("Record"))
        infoExpertWidget.setResearchArea(self.sqlQuery.value("ResearchArea"))
        infoExpertWidget.setResearchFindings(self.sqlQuery.value("ResearchFindings"))
        infoExpertWidget.setFundProject(self.sqlQuery.value("FundProject"))
        infoExpertWidget.setReward(self.sqlQuery.value("Reward"))
        infoExpertWidget.setContact(self.sqlQuery.value("Contact"))
        infoExpertWidget.setClass(FirstClass[self.sqlQuery.value("First")],SecondClass[self.sqlQuery.value("Second")])
        self.mainWin.cenTab.addTab(infoExpertWidget, name[0:11])
        self.mainWin.cenTab.setCurrentWidget(infoExpertWidget)

    #槽，选择研究方向
    def currentIndexChanged_callback(self,index):
        print(ResearchAreaCode[index])
        if index == 0:
            self.condition = ''
        elif index >= 6 and index <= 9:
            self.condition = " WHERE Second LIKE \'%s\'" % (ResearchAreaCode[index])
        else:
            self.condition = ' WHERE First LIKE \'%s\'' % (ResearchAreaCode[index])
        print(self.condition)
        self.totoalRecord = self.countRecord(self.condition)
        self.totoalPage = self.countPage()
        self.currentPage = 0
        self.excuteQuery(0)
        self.updateLabel()

    #槽，重新载入
    # def reload_callback(self):
    #     self.ui.queryforLineEdit.setText("")
    #     self.ui.researchAreaCombox.setCurrentIndex(0)

    #槽，关键字查询
    def query_callback(self):
        target = self.ui.queryforLineEdit.text().strip()
        #print(target)
        if target.__len__() == 0:
            self.condition = ""
            QMessageBox.warning(self,"警告","请输入查询关键字或条件！",QMessageBox.Yes)
            return
        else:
            self.condition = " WHERE Name LIKE \'%%%s%%\' or Summary LIKE \'%%%s%%\' or ResearchArea LIKE \'%%%s%%\' or ResearchFindings LIKE \'%%%s%%\' or FundProject LIKE \'%%%s%%\' or Reward LIKE \'%%%s%%\' or Post LIKE \'%%%s%%\' " % (target, target, target,target,target,target,target)
            records = self.countRecord(self.condition)
            #print(records)
            #查询到记录
            if records > 0:
                self.totoalRecord = records
                self.totoalPage = self.countPage()
                self.currentPage = 0
                self.excuteQuery(0)
                self.updateLabel()
            else:
                #没有查询到记录
                self.condition = ""
                QMessageBox.information(self,"提示","无查询信息！",QMessageBox.Yes)
                return

    #槽，跳转页面
    def gotoPage_callback(self):
        target = self.ui.gotoPageLineEidit.text().strip()
        if target.isnumeric() is False:
            QMessageBox.warning(self,"警告","请输入正确的页码数字!",QMessageBox.Yes)
            self.ui.gotoPageLineEidit.setText("")
            return
        targetPage = int(target)
        if targetPage < 1 or targetPage > self.totoalPage:
            QMessageBox.warning(self, "警告", "请输入正确的页码数字!", QMessageBox.Yes)
            self.ui.gotoPageLineEidit.setText("")
        else:
            self.currentPage = targetPage - 1
            self.excuteQuery(self.currentPage * eachRecordPerPage)
            self.updateLabel()

    #槽，右键
    def generateMenu(self):
        menu = QMenu(self)
        item_open = QAction("打开", self)
        item_open.triggered.connect(self.openContextMenu_callback)
        menu.addAction(item_open)
        menu.addSeparator()
        item_fresh = QAction("全部重载（刷新）", self)
        item_fresh.triggered.connect(self.freshContextMenu_callback)
        menu.addAction(item_fresh)
        menu.addSeparator()
        item_firstPage = QAction("首页", self)
        item_firstPage.triggered.connect(self.firstPageContextMenu_callback)
        menu.addAction(item_firstPage)
        item_lastPage = QAction("最后一页", self)
        item_lastPage.triggered.connect(self.lastPageContextMenu_callback)
        menu.addAction(item_lastPage)
        item = menu.exec(QCursor.pos())

    #槽,右键打开详细页
    def openContextMenu_callback(self):
        for index in self.ui.tableView.selectionModel().selectedRows():
            self.doubleClick_callback(index)

    #槽，重新载入
    def freshContextMenu_callback(self):
        self.condition = ""
        self.currentPage = 0
        self.totoalRecord = self.countRecord(self.condition)
        self.totoalPage = self.countPage()
        self.ui.queryforLineEdit.setText("")
        self.ui.gotoPageLineEidit.setText("")
        self.excuteQuery(self.currentPage * eachRecordPerPage)
        self.updateLabel()

    #槽，载入第一页
    def firstPageContextMenu_callback(self):
        self.currentPage = 0
        self.excuteQuery(self.currentPage * eachRecordPerPage)
        self.updateLabel()

    def lastPageContextMenu_callback(self):
        self.currentPage = self.totoalPage - 1
        self.excuteQuery(self.currentPage * eachRecordPerPage)
        self.updateLabel()

class ExpertInfoWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_ExpertInfoWidget()
        self.ui.setupUi(self)

    def setName(self,value):
        self.ui.Namelabel.setText(value)

    def setClass(self,value1,value2):
        self.ui.Classlabel.setText("{}|{}".format(value1,value2))

    def setSummary(self,value):
        self.ui.SummarylineEdit.setText(value)

    def setPost(self,value):
        self.ui.PostlineEdit.setText(value)

    def setRecord(self,value):
        self.ui.RecordtextEdit.setText(value)

    def setResearchArea(self,value):
        self.ui.ResearchArealineEdit.setText(value)

    def setResearchFindings(self,value):
        self.ui.ResearchFindingstextEdit.setText(value)

    def setFundProject(self,value):
        self.ui.FundProjecttextEdit.setText(value)

    def setReward(self,value):
        self.ui.RewardtextEdit.setText(value)

    def setContact(self,value):
        self.ui.ContactlineEdit.setText(value)



if __name__ == '__main__':
    pass