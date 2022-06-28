from PyQt5.QtWidgets import QWidget,QMainWindow
from UI.UI_ExpertListWidget import Ui_ExpertList
from PyQt5.QtSql import QSqlQuery,QSqlQueryModel
from CreateDBConnect import SingleDBConnect
from MinnanCSIRDB import MainWindow


#专家学者页面
class ExpertIndexWidget(QWidget):


    def __init__(self,mainWin=MainWindow):
        super().__init__()
        self.ui = Ui_ExpertList()
        self.ui.setupUi(self)
        self.mainWin = mainWin

        #普通数据库链接对象
        self.sqlQuery = QSqlQuery(SingleDBConnect().DB)
        #与表格关联数据库链接对象
        self.qryModel = QSqlQueryModel(self)


    #初始化表格
    def initTable(self):
        pass

if __name__ == '__main__':
    pass