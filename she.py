# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'she.ui'
#
# Created by: PyQt4 UI code generator 4.12
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_She(object):
    def setupUi(self, She):
        She.setObjectName(_fromUtf8("She"))
        She.resize(722, 679)
        She.setIconSize(QtCore.QSize(80, 80))
        self.centralwidget = QtGui.QWidget(She)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Devanagari MT"))
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_13.setMargin(0)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.label = QtGui.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_11.addWidget(self.label)
        self.label_4 = QtGui.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_11.addWidget(self.label_4)
        self.label_12 = QtGui.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_11.addWidget(self.label_12)
        self.label_13 = QtGui.QLabel(self.tab_3)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_11.addWidget(self.label_13)
        self.label_14 = QtGui.QLabel(self.tab_3)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_11.addWidget(self.label_14)
        self.label_16 = QtGui.QLabel(self.tab_3)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_11.addWidget(self.label_16)
        self.label_19 = QtGui.QLabel(self.tab_3)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.verticalLayout_11.addWidget(self.label_19)
        self.label_20 = QtGui.QLabel(self.tab_3)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayout_11.addWidget(self.label_20)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_23 = QtGui.QLabel(self.tab_3)
        self.label_23.setMaximumSize(QtCore.QSize(50, 50))
        self.label_23.setText(_fromUtf8(""))
        self.label_23.setPixmap(QtGui.QPixmap(_fromUtf8(":/image/imge/play.png")))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_14.addWidget(self.label_23)
        self.label_24 = QtGui.QLabel(self.tab_3)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.horizontalLayout_14.addWidget(self.label_24)
        self.verticalLayout_12.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_25 = QtGui.QLabel(self.tab_3)
        self.label_25.setMaximumSize(QtCore.QSize(55, 55))
        self.label_25.setText(_fromUtf8(""))
        self.label_25.setPixmap(QtGui.QPixmap(_fromUtf8(":/image/imge/help.png")))
        self.label_25.setScaledContents(True)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.horizontalLayout_15.addWidget(self.label_25)
        self.label_26 = QtGui.QLabel(self.tab_3)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.horizontalLayout_15.addWidget(self.label_26)
        self.verticalLayout_12.addLayout(self.horizontalLayout_15)
        self.verticalLayout_13.addLayout(self.verticalLayout_12)
        spacerItem = QtGui.QSpacerItem(20, 138, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_9.setMargin(0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_12.addLayout(self.verticalLayout)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_10 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Devanagari MT"))
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout.addWidget(self.label_10)
        self.she_pdb_LineEdit = QtGui.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.she_pdb_LineEdit.setFont(font)
        self.she_pdb_LineEdit.setObjectName(_fromUtf8("she_pdb_LineEdit"))
        self.horizontalLayout.addWidget(self.she_pdb_LineEdit)
        self.pdb_button = QtGui.QPushButton(self.tab)
        self.pdb_button.setObjectName(_fromUtf8("pdb_button"))
        self.horizontalLayout.addWidget(self.pdb_button)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_10.addLayout(self.verticalLayout_7)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_11 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_7.addWidget(self.label_11)
        spacerItem4 = QtGui.QSpacerItem(129, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        spacerItem5 = QtGui.QSpacerItem(127, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        spacerItem6 = QtGui.QSpacerItem(129, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_18 = QtGui.QLabel(self.tab)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_2.addWidget(self.label_18)
        self.she_saxs_LineEdit = QtGui.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.she_saxs_LineEdit.setFont(font)
        self.she_saxs_LineEdit.setObjectName(_fromUtf8("she_saxs_LineEdit"))
        self.horizontalLayout_2.addWidget(self.she_saxs_LineEdit)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.saxs_button = QtGui.QPushButton(self.tab)
        self.saxs_button.setObjectName(_fromUtf8("saxs_button"))
        self.verticalLayout_2.addWidget(self.saxs_button)
        self.saxs_show_pushButton = QtGui.QPushButton(self.tab)
        self.saxs_show_pushButton.setObjectName(_fromUtf8("saxs_show_pushButton"))
        self.verticalLayout_2.addWidget(self.saxs_show_pushButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_2)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem7)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem8)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.she_method_comboBox = QtGui.QComboBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.she_method_comboBox.setFont(font)
        self.she_method_comboBox.setObjectName(_fromUtf8("she_method_comboBox"))
        self.she_method_comboBox.addItem(_fromUtf8(""))
        self.she_method_comboBox.setItemText(0, _fromUtf8("she"))
        self.she_method_comboBox.addItem(_fromUtf8(""))
        self.she_method_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.she_method_comboBox)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem10)
        self.horizontalLayout_9.addLayout(self.verticalLayout_6)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem11)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem12)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem13)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_9 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_8.addWidget(self.label_9)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem14)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem15)
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem16)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        self.starting_q_LineEdit = QtGui.QLineEdit(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.starting_q_LineEdit.sizePolicy().hasHeightForWidth())
        self.starting_q_LineEdit.setSizePolicy(sizePolicy)
        self.starting_q_LineEdit.setMinimumSize(QtCore.QSize(29, 40))
        self.starting_q_LineEdit.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.starting_q_LineEdit.setFont(font)
        self.starting_q_LineEdit.setText(_fromUtf8(""))
        self.starting_q_LineEdit.setObjectName(_fromUtf8("starting_q_LineEdit"))
        self.verticalLayout_3.addWidget(self.starting_q_LineEdit)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        spacerItem17 = QtGui.QSpacerItem(44, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem17)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_4.addWidget(self.label_7)
        self.stopping_q_LineEdit = QtGui.QLineEdit(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.stopping_q_LineEdit.sizePolicy().hasHeightForWidth())
        self.stopping_q_LineEdit.setSizePolicy(sizePolicy)
        self.stopping_q_LineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.stopping_q_LineEdit.setMaximumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.stopping_q_LineEdit.setFont(font)
        self.stopping_q_LineEdit.setText(_fromUtf8(""))
        self.stopping_q_LineEdit.setObjectName(_fromUtf8("stopping_q_LineEdit"))
        self.verticalLayout_4.addWidget(self.stopping_q_LineEdit)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem18)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_5.addWidget(self.label_8)
        self.number_of_n_LineEdit = QtGui.QLineEdit(self.tab)
        self.number_of_n_LineEdit.setMinimumSize(QtCore.QSize(40, 40))
        self.number_of_n_LineEdit.setMaximumSize(QtCore.QSize(80, 40))
        self.number_of_n_LineEdit.setSizeIncrement(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.number_of_n_LineEdit.setFont(font)
        self.number_of_n_LineEdit.setText(_fromUtf8(""))
        self.number_of_n_LineEdit.setObjectName(_fromUtf8("number_of_n_LineEdit"))
        self.verticalLayout_5.addWidget(self.number_of_n_LineEdit)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_6)
        spacerItem19 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem19)
        spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem20)
        spacerItem21 = QtGui.QSpacerItem(58, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem21)
        self.verticalLayout_8.addLayout(self.horizontalLayout_13)
        spacerItem22 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem22)
        spacerItem23 = QtGui.QSpacerItem(368, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem23)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_14.setMargin(0)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_17 = QtGui.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Devanagari MT"))
        font.setPointSize(18)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_4.addWidget(self.label_17)
        spacerItem24 = QtGui.QSpacerItem(17, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem24)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        self.textBrowser = QtGui.QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_10.addWidget(self.textBrowser)
        self.verticalLayout_14.addLayout(self.verticalLayout_10)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout_15.addWidget(self.tabWidget)
        She.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(She)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 722, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        She.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(She)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        She.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(She)
        self.toolBar.setIconSize(QtCore.QSize(60, 60))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        She.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionQuit = QtGui.QAction(She)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/imge/quit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionRun = QtGui.QAction(She)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/imge/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRun.setIcon(icon1)
        self.actionRun.setObjectName(_fromUtf8("actionRun"))
        self.actionHelp = QtGui.QAction(She)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/imge/help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon2)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.toolBar.addAction(self.actionQuit)
        self.toolBar.addAction(self.actionRun)
        self.toolBar.addAction(self.actionHelp)

        self.retranslateUi(She)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(She)

    def retranslateUi(self, She):
        She.setWindowTitle(_translate("She", "SASTBX Intensity Calculation", None))
        self.label.setText(_translate("She", "Sastbx Intensity Calculation", None))
        self.label_4.setText(_translate("She", "Compute theoretical scattering intensity curve for the given PDB models", None))
        self.label_12.setText(_translate("She", "The Model (PDB Coordinate File)  is the only required", None))
        self.label_13.setText(_translate("She", "Optional control parameters:", None))
        self.label_14.setText(_translate("She", "SAXS file:the experimental data, columns are q, I(q), and std", None))
        self.label_16.setText(_translate("She", "Method: type of theoretical model", None))
        self.label_19.setText(_translate("She", "q start, q stop:  defines the range of Q array", None))
        self.label_20.setText(_translate("She", "n step: bin size", None))
        self.label_24.setText(_translate("She", "Start the program", None))
        self.label_26.setText(_translate("She", "To obtain the example of  input and output files", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("She", "introduction", None))
        self.label_2.setText(_translate("She", "Intensity Calculation", None))
        self.label_3.setText(_translate("She", "Compute theoretical scattering intensity curve for the given PDB models", None))
        self.label_10.setText(_translate("She", "Model (PDB format)", None))
        self.pdb_button.setText(_translate("She", "openfile *", None))
        self.label_11.setText(_translate("She", "optional", None))
        self.label_18.setText(_translate("She", "SAXS file", None))
        self.saxs_button.setText(_translate("She", "Brower", None))
        self.saxs_show_pushButton.setText(_translate("She", "Show", None))
        self.label_5.setText(_translate("She", "Method", None))
        self.she_method_comboBox.setItemText(1, _translate("She", "debye", None))
        self.she_method_comboBox.setItemText(2, _translate("She", "zernike", None))
        self.label_9.setText(_translate("She", "Intensity calculation parameters", None))
        self.label_6.setText(_translate("She", "q start", None))
        self.label_7.setText(_translate("She", "q stop", None))
        self.label_8.setText(_translate("She", "n step", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("She", "Input", None))
        self.label_17.setText(_translate("She", "Result", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("She", "Output", None))
        self.toolBar.setWindowTitle(_translate("She", "toolBar", None))
        self.actionQuit.setText(_translate("She", "quit", None))
        self.actionRun.setText(_translate("She", "run", None))
        self.actionHelp.setText(_translate("She", "help", None))

import resource_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    She = QtGui.QMainWindow()
    ui = Ui_She()
    ui.setupUi(She)
    She.show()
    sys.exit(app.exec_())
