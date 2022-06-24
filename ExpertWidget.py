from PyQt5.QtWidgets import QWidget,QMainWindow
from UI.UI_ExpertListWidget import Ui_ExpertList
from UI.UI_InstitutionIndexWidget import Ui_InstitutionIndex
from PyQt5.QtSql import QSqlQuery
from CreateDBConnect import SingleDBConnect


#专家学者页面
class ExpertIndexWidget(QWidget):

    def __init__(self,mainWin=QMainWindow):
        super().__init__()
        self.ui = Ui_ExpertList()
        self.ui.setupUi(self)
        self.mainWin = mainWin



if __name__ == '__main__':
    pass