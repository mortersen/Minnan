from PyQt5.QtWidgets import QWidget,QMainWindow
from UI.UI_ExpertListWidget import Ui_ExpertList


#专家学者页面
class ExpertListWidget(QWidget):

    def __init__(self,mainWin=QMainWindow):
        super().__init__()
        self.ui = Ui_ExpertList()
        self.ui.setupUi(self)
        self.mainWin = mainWin



if __name__ == '__main__':
    pass