# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_ThesisInfoWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ThesisInfoView(object):
    def setupUi(self, ThesisInfoView):
        ThesisInfoView.setObjectName("ThesisInfoView")
        ThesisInfoView.resize(486, 593)
        ThesisInfoView.setMinimumSize(QtCore.QSize(48, 48))
        ThesisInfoView.setAutoFillBackground(False)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(ThesisInfoView)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(18, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_home = QtWidgets.QPushButton(ThesisInfoView)
        self.btn_home.setMinimumSize(QtCore.QSize(32, 32))
        self.btn_home.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/PIC/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QtCore.QSize(32, 32))
        self.btn_home.setAutoDefault(False)
        self.btn_home.setFlat(True)
        self.btn_home.setObjectName("btn_home")
        self.horizontalLayout.addWidget(self.btn_home)
        self.btn_goback = QtWidgets.QPushButton(ThesisInfoView)
        self.btn_goback.setMinimumSize(QtCore.QSize(32, 32))
        self.btn_goback.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_goback.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/PIC/goback.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_goback.setIcon(icon1)
        self.btn_goback.setIconSize(QtCore.QSize(32, 32))
        self.btn_goback.setFlat(True)
        self.btn_goback.setObjectName("btn_goback")
        self.horizontalLayout.addWidget(self.btn_goback)
        self.btn_pdfRead = QtWidgets.QPushButton(ThesisInfoView)
        self.btn_pdfRead.setMinimumSize(QtCore.QSize(32, 32))
        self.btn_pdfRead.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_pdfRead.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/PIC/READPDF.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_pdfRead.setIcon(icon2)
        self.btn_pdfRead.setIconSize(QtCore.QSize(32, 32))
        self.btn_pdfRead.setAutoDefault(False)
        self.btn_pdfRead.setFlat(True)
        self.btn_pdfRead.setObjectName("btn_pdfRead")
        self.horizontalLayout.addWidget(self.btn_pdfRead)
        self.btn_pdfDownload = QtWidgets.QPushButton(ThesisInfoView)
        self.btn_pdfDownload.setMinimumSize(QtCore.QSize(32, 32))
        self.btn_pdfDownload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_pdfDownload.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/PIC/PDF下载.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_pdfDownload.setIcon(icon3)
        self.btn_pdfDownload.setIconSize(QtCore.QSize(32, 32))
        self.btn_pdfDownload.setAutoDefault(False)
        self.btn_pdfDownload.setFlat(True)
        self.btn_pdfDownload.setObjectName("btn_pdfDownload")
        self.horizontalLayout.addWidget(self.btn_pdfDownload)
        self.horizontalLayout_14.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem2)
        self.horizontalLayout_14.setStretch(0, 8)
        self.horizontalLayout_14.setStretch(1, 1)
        self.horizontalLayout_14.setStretch(2, 2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        spacerItem3 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_Title = QtWidgets.QLabel(ThesisInfoView)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        self.label_Title.setFont(font)
        self.label_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Title.setObjectName("label_Title")
        self.verticalLayout_3.addWidget(self.label_Title)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Author = QtWidgets.QLabel(ThesisInfoView)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Author.setFont(font)
        self.label_Author.setStyleSheet("color: rgb(0, 170, 255);")
        self.label_Author.setText("")
        self.label_Author.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Author.setObjectName("label_Author")
        self.verticalLayout.addWidget(self.label_Author)
        self.label_School = QtWidgets.QLabel(ThesisInfoView)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_School.setFont(font)
        self.label_School.setStyleSheet("color: rgb(0, 170, 255);")
        self.label_School.setText("")
        self.label_School.setAlignment(QtCore.Qt.AlignCenter)
        self.label_School.setObjectName("label_School")
        self.verticalLayout.addWidget(self.label_School)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 3)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(ThesisInfoView)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_Summary = QtWidgets.QLabel(ThesisInfoView)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Summary.setFont(font)
        self.label_Summary.setText("")
        self.label_Summary.setWordWrap(True)
        self.label_Summary.setObjectName("label_Summary")
        self.horizontalLayout_2.addWidget(self.label_Summary)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(ThesisInfoView)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_Keyword = QtWidgets.QLabel(ThesisInfoView)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Keyword.setFont(font)
        self.label_Keyword.setText("")
        self.label_Keyword.setObjectName("label_Keyword")
        self.horizontalLayout_3.addWidget(self.label_Keyword)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(ThesisInfoView)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.label_Teacher = QtWidgets.QLabel(ThesisInfoView)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Teacher.setFont(font)
        self.label_Teacher.setText("")
        self.label_Teacher.setObjectName("label_Teacher")
        self.horizontalLayout_4.addWidget(self.label_Teacher)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(ThesisInfoView)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.label_Type = QtWidgets.QLabel(ThesisInfoView)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Type.setFont(font)
        self.label_Type.setText("")
        self.label_Type.setObjectName("label_Type")
        self.horizontalLayout_5.addWidget(self.label_Type)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_ = QtWidgets.QLabel(ThesisInfoView)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_.setFont(font)
        self.label_.setObjectName("label_")
        self.horizontalLayout_6.addWidget(self.label_)
        self.label_Pages = QtWidgets.QLabel(ThesisInfoView)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Pages.setFont(font)
        self.label_Pages.setText("")
        self.label_Pages.setObjectName("label_Pages")
        self.horizontalLayout_6.addWidget(self.label_Pages)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(ThesisInfoView)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.label_Year = QtWidgets.QLabel(ThesisInfoView)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Year.setFont(font)
        self.label_Year.setText("")
        self.label_Year.setObjectName("label_Year")
        self.horizontalLayout_7.addWidget(self.label_Year)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_11 = QtWidgets.QLabel(ThesisInfoView)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.label_Period = QtWidgets.QLabel(ThesisInfoView)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Period.setFont(font)
        self.label_Period.setText("")
        self.label_Period.setObjectName("label_Period")
        self.horizontalLayout_8.addWidget(self.label_Period)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_12 = QtWidgets.QLabel(ThesisInfoView)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_13.addWidget(self.label_12)
        self.label_FL = QtWidgets.QLabel(ThesisInfoView)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_FL.setFont(font)
        self.label_FL.setText("")
        self.label_FL.setObjectName("label_FL")
        self.horizontalLayout_13.addWidget(self.label_FL)
        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 8)
        self.horizontalLayout_15.addLayout(self.verticalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem6)
        self.horizontalLayout_15.setStretch(0, 2)
        self.horizontalLayout_15.setStretch(1, 6)
        self.horizontalLayout_15.setStretch(2, 2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        spacerItem7 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 4)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.setStretch(3, 12)
        self.verticalLayout_4.setStretch(4, 2)

        self.retranslateUi(ThesisInfoView)
        QtCore.QMetaObject.connectSlotsByName(ThesisInfoView)

    def retranslateUi(self, ThesisInfoView):
        _translate = QtCore.QCoreApplication.translate
        ThesisInfoView.setWindowTitle(_translate("ThesisInfoView", "Form"))
        self.label_Title.setText(_translate("ThesisInfoView", "我是标题"))
        self.label.setText(_translate("ThesisInfoView", "摘要："))
        self.label_2.setText(_translate("ThesisInfoView", "关键字："))
        self.label_3.setText(_translate("ThesisInfoView", "指导老师："))
        self.label_4.setText(_translate("ThesisInfoView", "论文类别："))
        self.label_.setText(_translate("ThesisInfoView", "页数："))
        self.label_6.setText(_translate("ThesisInfoView", "发表年份："))
        self.label_11.setText(_translate("ThesisInfoView", "发表期次："))
        self.label_12.setText(_translate("ThesisInfoView", "分类："))
import RES.img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ThesisInfoView = QtWidgets.QWidget()
    ui = Ui_ThesisInfoView()
    ui.setupUi(ThesisInfoView)
    ThesisInfoView.show()
    sys.exit(app.exec_())
