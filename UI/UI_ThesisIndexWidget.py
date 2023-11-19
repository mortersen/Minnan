# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_ThesisIndexWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ThesisIndex(object):
    def setupUi(self, ThesisIndex):
        ThesisIndex.setObjectName("ThesisIndex")
        ThesisIndex.resize(696, 356)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(ThesisIndex)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.QuerylineEdit = QtWidgets.QLineEdit(ThesisIndex)
        self.QuerylineEdit.setMinimumSize(QtCore.QSize(0, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QuerylineEdit.setFont(font)
        self.QuerylineEdit.setObjectName("QuerylineEdit")
        self.horizontalLayout.addWidget(self.QuerylineEdit)
        self.QueryBtn = QtWidgets.QPushButton(ThesisIndex)
        self.QueryBtn.setMinimumSize(QtCore.QSize(0, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.QueryBtn.setFont(font)
        self.QueryBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/PIC/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.QueryBtn.setIcon(icon)
        self.QueryBtn.setIconSize(QtCore.QSize(20, 22))
        self.QueryBtn.setFlat(True)
        self.QueryBtn.setObjectName("QueryBtn")
        self.horizontalLayout.addWidget(self.QueryBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.Thesis_treeWidget = QtWidgets.QTreeWidget(ThesisIndex)
        self.Thesis_treeWidget.setItemsExpandable(True)
        self.Thesis_treeWidget.setObjectName("Thesis_treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.Thesis_treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.Thesis_treeWidget.header().setVisible(False)
        self.verticalLayout.addWidget(self.Thesis_treeWidget)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.InfoLable = QtWidgets.QLabel(ThesisIndex)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.InfoLable.setFont(font)
        self.InfoLable.setObjectName("InfoLable")
        self.horizontalLayout_4.addWidget(self.InfoLable)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.ThesistableView = QtWidgets.QTableView(ThesisIndex)
        self.ThesistableView.setSortingEnabled(True)
        self.ThesistableView.setObjectName("ThesistableView")
        self.verticalLayout_2.addWidget(self.ThesistableView)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.PageUpBtn = QtWidgets.QPushButton(ThesisIndex)
        self.PageUpBtn.setObjectName("PageUpBtn")
        self.horizontalLayout_3.addWidget(self.PageUpBtn)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.CurrentPageLable = QtWidgets.QLabel(ThesisIndex)
        self.CurrentPageLable.setObjectName("CurrentPageLable")
        self.horizontalLayout_2.addWidget(self.CurrentPageLable)
        self.label = QtWidgets.QLabel(ThesisIndex)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.TotoalPageLable = QtWidgets.QLabel(ThesisIndex)
        self.TotoalPageLable.setObjectName("TotoalPageLable")
        self.horizontalLayout_2.addWidget(self.TotoalPageLable)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.PageDownBtn = QtWidgets.QPushButton(ThesisIndex)
        self.PageDownBtn.setObjectName("PageDownBtn")
        self.horizontalLayout_3.addWidget(self.PageDownBtn)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.label_7 = QtWidgets.QLabel(ThesisIndex)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.gotoPageLineEidit = QtWidgets.QLineEdit(ThesisIndex)
        self.gotoPageLineEidit.setMinimumSize(QtCore.QSize(25, 22))
        self.gotoPageLineEidit.setMaximumSize(QtCore.QSize(30, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gotoPageLineEidit.setFont(font)
        self.gotoPageLineEidit.setText("")
        self.gotoPageLineEidit.setObjectName("gotoPageLineEidit")
        self.horizontalLayout_6.addWidget(self.gotoPageLineEidit)
        self.label_8 = QtWidgets.QLabel(ThesisIndex)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.pbn_PageGo = QtWidgets.QPushButton(ThesisIndex)
        self.pbn_PageGo.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/PIC/5b483c0e7f8f41a5bebc1f7d7cd5d87c.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pbn_PageGo.setIcon(icon1)
        self.pbn_PageGo.setIconSize(QtCore.QSize(16, 16))
        self.pbn_PageGo.setDefault(False)
        self.pbn_PageGo.setFlat(False)
        self.pbn_PageGo.setObjectName("pbn_PageGo")
        self.horizontalLayout_6.addWidget(self.pbn_PageGo)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(1, 6)
        self.horizontalLayout_5.setStretch(2, 1)
        self.horizontalLayout_5.setStretch(3, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.horizontalLayout_8.setStretch(0, 4)
        self.horizontalLayout_8.setStretch(1, 14)

        self.retranslateUi(ThesisIndex)
        QtCore.QMetaObject.connectSlotsByName(ThesisIndex)

    def retranslateUi(self, ThesisIndex):
        _translate = QtCore.QCoreApplication.translate
        ThesisIndex.setWindowTitle(_translate("ThesisIndex", "Form"))
        self.QuerylineEdit.setPlaceholderText(_translate("ThesisIndex", "请输入查询关键字"))
        self.Thesis_treeWidget.headerItem().setText(0, _translate("ThesisIndex", "1"))
        self.Thesis_treeWidget.headerItem().setText(1, _translate("ThesisIndex", "2"))
        __sortingEnabled = self.Thesis_treeWidget.isSortingEnabled()
        self.Thesis_treeWidget.setSortingEnabled(False)
        self.Thesis_treeWidget.topLevelItem(0).setText(0, _translate("ThesisIndex", "学位论文"))
        self.Thesis_treeWidget.topLevelItem(0).setText(1, _translate("ThesisIndex", "0"))
        self.Thesis_treeWidget.topLevelItem(0).child(0).setText(0, _translate("ThesisIndex", "闽南方言"))
        self.Thesis_treeWidget.topLevelItem(0).child(0).setText(1, _translate("ThesisIndex", "1"))
        self.Thesis_treeWidget.topLevelItem(0).child(1).setText(0, _translate("ThesisIndex", "闽南海丝文化"))
        self.Thesis_treeWidget.topLevelItem(0).child(1).setText(1, _translate("ThesisIndex", "2"))
        self.Thesis_treeWidget.topLevelItem(0).child(2).setText(0, _translate("ThesisIndex", "闽南华侨文化"))
        self.Thesis_treeWidget.topLevelItem(0).child(2).setText(1, _translate("ThesisIndex", "3"))
        self.Thesis_treeWidget.topLevelItem(0).child(3).setText(0, _translate("ThesisIndex", "闽南家族文化"))
        self.Thesis_treeWidget.topLevelItem(0).child(3).setText(1, _translate("ThesisIndex", "4"))
        self.Thesis_treeWidget.topLevelItem(0).child(4).setText(0, _translate("ThesisIndex", "闽南建筑"))
        self.Thesis_treeWidget.topLevelItem(0).child(4).setText(1, _translate("ThesisIndex", "5"))
        self.Thesis_treeWidget.topLevelItem(0).child(5).setText(0, _translate("ThesisIndex", "闽南历史地理"))
        self.Thesis_treeWidget.topLevelItem(0).child(5).setText(1, _translate("ThesisIndex", "6"))
        self.Thesis_treeWidget.topLevelItem(0).child(6).setText(0, _translate("ThesisIndex", "闽南民间信仰"))
        self.Thesis_treeWidget.topLevelItem(0).child(6).setText(1, _translate("ThesisIndex", "7"))
        self.Thesis_treeWidget.topLevelItem(0).child(7).setText(0, _translate("ThesisIndex", "闽南民俗"))
        self.Thesis_treeWidget.topLevelItem(0).child(7).setText(1, _translate("ThesisIndex", "8"))
        self.Thesis_treeWidget.topLevelItem(0).child(8).setText(0, _translate("ThesisIndex", "闽南名人"))
        self.Thesis_treeWidget.topLevelItem(0).child(8).setText(1, _translate("ThesisIndex", "9"))
        self.Thesis_treeWidget.topLevelItem(0).child(8).child(0).setText(0, _translate("ThesisIndex", "李贽"))
        self.Thesis_treeWidget.topLevelItem(0).child(8).child(0).setText(1, _translate("ThesisIndex", "10"))
        self.Thesis_treeWidget.topLevelItem(0).child(8).child(1).setText(0, _translate("ThesisIndex", "黄道周"))
        self.Thesis_treeWidget.topLevelItem(0).child(8).child(1).setText(1, _translate("ThesisIndex", "11"))
        self.Thesis_treeWidget.topLevelItem(0).child(8).child(2).setText(0, _translate("ThesisIndex", "林语堂"))
        self.Thesis_treeWidget.topLevelItem(0).child(8).child(2).setText(1, _translate("ThesisIndex", "12"))
        self.Thesis_treeWidget.topLevelItem(0).child(8).child(3).setText(0, _translate("ThesisIndex", "陈嘉庚"))
        self.Thesis_treeWidget.topLevelItem(0).child(8).child(3).setText(1, _translate("ThesisIndex", "13"))
        self.Thesis_treeWidget.topLevelItem(0).child(8).child(4).setText(0, _translate("ThesisIndex", "郑芝龙"))
        self.Thesis_treeWidget.topLevelItem(0).child(8).child(4).setText(1, _translate("ThesisIndex", "14"))
        self.Thesis_treeWidget.topLevelItem(0).child(8).child(5).setText(0, _translate("ThesisIndex", "郑成功"))
        self.Thesis_treeWidget.topLevelItem(0).child(8).child(5).setText(1, _translate("ThesisIndex", "15"))
        self.Thesis_treeWidget.topLevelItem(0).child(8).child(6).setText(0, _translate("ThesisIndex", "郑经"))
        self.Thesis_treeWidget.topLevelItem(0).child(8).child(6).setText(1, _translate("ThesisIndex", "16"))
        self.Thesis_treeWidget.topLevelItem(0).child(8).child(7).setText(0, _translate("ThesisIndex", "其他名人"))
        self.Thesis_treeWidget.topLevelItem(0).child(8).child(7).setText(1, _translate("ThesisIndex", "17"))
        self.Thesis_treeWidget.topLevelItem(0).child(9).setText(0, _translate("ThesisIndex", "闽南文化交流"))
        self.Thesis_treeWidget.topLevelItem(0).child(9).setText(1, _translate("ThesisIndex", "24"))
        self.Thesis_treeWidget.topLevelItem(0).child(10).setText(0, _translate("ThesisIndex", "闽南文化总论"))
        self.Thesis_treeWidget.topLevelItem(0).child(10).setText(1, _translate("ThesisIndex", "18"))
        self.Thesis_treeWidget.topLevelItem(0).child(11).setText(0, _translate("ThesisIndex", "闽南文物"))
        self.Thesis_treeWidget.topLevelItem(0).child(11).setText(1, _translate("ThesisIndex", "19"))
        self.Thesis_treeWidget.topLevelItem(0).child(12).setText(0, _translate("ThesisIndex", "闽南文学"))
        self.Thesis_treeWidget.topLevelItem(0).child(12).setText(1, _translate("ThesisIndex", "20"))
        self.Thesis_treeWidget.topLevelItem(0).child(13).setText(0, _translate("ThesisIndex", "闽南艺术"))
        self.Thesis_treeWidget.topLevelItem(0).child(13).setText(1, _translate("ThesisIndex", "21"))
        self.Thesis_treeWidget.topLevelItem(0).child(14).setText(0, _translate("ThesisIndex", "闽南宗教"))
        self.Thesis_treeWidget.topLevelItem(0).child(14).setText(1, _translate("ThesisIndex", "22"))
        self.Thesis_treeWidget.topLevelItem(0).child(15).setText(0, _translate("ThesisIndex", "其他"))
        self.Thesis_treeWidget.topLevelItem(0).child(15).setText(1, _translate("ThesisIndex", "23"))
        self.Thesis_treeWidget.setSortingEnabled(__sortingEnabled)
        self.InfoLable.setText(_translate("ThesisIndex", "共有信息{XXX}条"))
        self.PageUpBtn.setText(_translate("ThesisIndex", "上一页"))
        self.CurrentPageLable.setText(_translate("ThesisIndex", "11"))
        self.label.setText(_translate("ThesisIndex", "/"))
        self.TotoalPageLable.setText(_translate("ThesisIndex", "100"))
        self.PageDownBtn.setText(_translate("ThesisIndex", "下一页"))
        self.label_7.setText(_translate("ThesisIndex", "前往第"))
        self.label_8.setText(_translate("ThesisIndex", "页"))
import RES.img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ThesisIndex = QtWidgets.QWidget()
    ui = Ui_ThesisIndex()
    ui.setupUi(ThesisIndex)
    ThesisIndex.show()
    sys.exit(app.exec_())
