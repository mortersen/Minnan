from PyQt5.QtWidgets import QWidget,QAbstractItemView
from PyQt5.QtCore import Qt
from UI.UI_ExpertListWidget import Ui_ExpertList
from PyQt5.QtSql import QSqlQuery,QSqlQueryModel
from CreateDBConnect import SingleDBConnect
from MinnanCSIRDB import MainWindow

eachRecordPerPage = 22

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

        self.ui.pageupBtn.clicked.connect(self.pageUp_callback)
        self.ui.pagedownBtn.clicked.connect(self.pageDown_callback)




    #初始化表格
    def initTable(self):
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableView.setSelectionModel(QAbstractItemView.SingleSelection)
        self.ui.tableView.setAlternatingRowColors(True)
        # 设置默认行高
        self.ui.tableView.verticalHeader().setDefaultSectionSize(60)
        self.ui.tableView.setColumnWidth(0, 400)
        self.ui.tableView.setColumnWidth(1, 600)
        self.ui.tableView.setColumnWidth(2, 800)
        self.ui.tableView.setColumnWidth(3, 900)
        self.qryModel.setHeaderData(0, Qt.Horizontal, "姓名")
        self.qryModel.setHeaderData(1, Qt.Horizontal, "研究方向")
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



if __name__ == '__main__':
    pass