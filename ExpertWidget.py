from PyQt5.QtWidgets import QWidget,QMainWindow
from UI.UI_ExpertListWidget import Ui_ExpertList
from PyQt5.QtSql import QSqlQuery,QSqlQueryModel
from CreateDBConnect import SingleDBConnect
from MinnanCSIRDB import MainWindow

eachRecordPerPage = 12

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
        self.ui.tableWidget.setModel(self.qryModel)
        self.query = "SELECT Name,Post,,ResearchFindings,,ID from Institution  "


    #初始化表格
    def initTable(self):
        pass

    #按条件统计数据库记录数
    def countRecord(self,condition):
        SqlTotoalQuery = "SELECT 1 from Expert" + condition
        try:
            self.sqlQuery.exec(SqlTotoalQuery)
            self.sqlQuery.last()
            return self.sqlQuery.at() + 1
        except Exception:
            print(Exception.__str__())

    #计算页数
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

if __name__ == '__main__':
    pass