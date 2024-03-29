# Form implementation generated from reading ui file 'ui\main_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 495)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.b_generate = QtWidgets.QPushButton(parent=self.centralwidget)
        self.b_generate.setGeometry(QtCore.QRect(560, 0, 71, 21))
        self.b_generate.setObjectName("b_generate")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(440, 30, 381, 271))
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        item.setFlags(QtCore.Qt.ItemFlag.ItemIsSelectable|QtCore.Qt.ItemFlag.ItemIsEnabled)
        self.tableWidget.setItem(0, 0, item)
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(440, 0, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.b_save = QtWidgets.QPushButton(parent=self.centralwidget)
        self.b_save.setGeometry(QtCore.QRect(640, 0, 51, 21))
        self.b_save.setObjectName("b_save")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 421, 221))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setObjectName("frame")
        self.out_names1 = QtWidgets.QListWidget(parent=self.frame)
        self.out_names1.setGeometry(QtCore.QRect(130, 30, 111, 151))
        self.out_names1.setAutoFillBackground(False)
        self.out_names1.setStyleSheet("QListWidget{ background-color: transparent; }")
        self.out_names1.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.out_names1.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.out_names1.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.out_names1.setDragEnabled(True)
        self.out_names1.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DragOnly)
        self.out_names1.setFlow(QtWidgets.QListView.Flow.TopToBottom)
        self.out_names1.setViewMode(QtWidgets.QListView.ViewMode.ListMode)
        self.out_names1.setItemAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.out_names1.setObjectName("out_names1")
        self.b_clear_inputs1 = QtWidgets.QPushButton(parent=self.frame)
        self.b_clear_inputs1.setGeometry(QtCore.QRect(10, 190, 41, 21))
        self.b_clear_inputs1.setStyleSheet("background-color: rgb(255, 157, 159);")
        self.b_clear_inputs1.setObjectName("b_clear_inputs1")
        self.out_characters1 = QtWidgets.QListWidget(parent=self.frame)
        self.out_characters1.setGeometry(QtCore.QRect(300, 30, 111, 121))
        self.out_characters1.setAcceptDrops(True)
        self.out_characters1.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DropOnly)
        self.out_characters1.setObjectName("out_characters1")
        self.cb_location1 = QtWidgets.QComboBox(parent=self.frame)
        self.cb_location1.setGeometry(QtCore.QRect(10, 30, 111, 22))
        self.cb_location1.setMaximumSize(QtCore.QSize(111, 16777215))
        self.cb_location1.setObjectName("cb_location1")
        self.label_11 = QtWidgets.QLabel(parent=self.frame)
        self.label_11.setGeometry(QtCore.QRect(130, 10, 111, 20))
        self.label_11.setToolTip("")
        self.label_11.setToolTipDuration(-1)
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.b_clear_out_characters1 = QtWidgets.QPushButton(parent=self.frame)
        self.b_clear_out_characters1.setGeometry(QtCore.QRect(300, 190, 41, 21))
        self.b_clear_out_characters1.setStyleSheet("background-color: rgb(255, 157, 159);")
        self.b_clear_out_characters1.setObjectName("b_clear_out_characters1")
        self.in_name1 = QtWidgets.QLineEdit(parent=self.frame)
        self.in_name1.setGeometry(QtCore.QRect(300, 160, 111, 22))
        self.in_name1.setText("")
        self.in_name1.setObjectName("in_name1")
        self.b_clear_out_names1 = QtWidgets.QPushButton(parent=self.frame)
        self.b_clear_out_names1.setGeometry(QtCore.QRect(130, 190, 41, 21))
        self.b_clear_out_names1.setStyleSheet("background-color: rgb(255, 157, 159);")
        self.b_clear_out_names1.setObjectName("b_clear_out_names1")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 49, 16))
        self.label_2.setObjectName("label_2")
        self.cb_name1 = QtWidgets.QComboBox(parent=self.frame)
        self.cb_name1.setGeometry(QtCore.QRect(10, 130, 111, 22))
        self.cb_name1.setMaximumSize(QtCore.QSize(111, 16777215))
        self.cb_name1.setObjectName("cb_name1")
        self.label_10 = QtWidgets.QLabel(parent=self.frame)
        self.label_10.setGeometry(QtCore.QRect(300, 10, 111, 20))
        self.label_10.setToolTip("")
        self.label_10.setToolTipDuration(-1)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.cb_group1 = QtWidgets.QComboBox(parent=self.frame)
        self.cb_group1.setGeometry(QtCore.QRect(10, 80, 111, 22))
        self.cb_group1.setMaximumSize(QtCore.QSize(111, 16777215))
        self.cb_group1.setObjectName("cb_group1")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 49, 16))
        self.label.setToolTip("")
        self.label.setToolTipDuration(-1)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setGeometry(QtCore.QRect(260, 160, 41, 21))
        self.label_4.setObjectName("label_4")
        self.b_shift1 = QtWidgets.QPushButton(parent=self.frame)
        self.b_shift1.setGeometry(QtCore.QRect(250, 80, 41, 41))
        self.b_shift1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/przem/Downloads/right_arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.b_shift1.setIcon(icon)
        self.b_shift1.setIconSize(QtCore.QSize(31, 31))
        self.b_shift1.setObjectName("b_shift1")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 220, 421, 221))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_2.setObjectName("frame_2")
        self.out_names2 = QtWidgets.QListWidget(parent=self.frame_2)
        self.out_names2.setGeometry(QtCore.QRect(130, 30, 111, 151))
        self.out_names2.setAutoFillBackground(False)
        self.out_names2.setStyleSheet("QListWidget{ background-color: transparent; }")
        self.out_names2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.out_names2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.out_names2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.out_names2.setDragEnabled(True)
        self.out_names2.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DragOnly)
        self.out_names2.setFlow(QtWidgets.QListView.Flow.TopToBottom)
        self.out_names2.setViewMode(QtWidgets.QListView.ViewMode.ListMode)
        self.out_names2.setItemAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.out_names2.setObjectName("out_names2")
        self.b_clear_inputs2 = QtWidgets.QPushButton(parent=self.frame_2)
        self.b_clear_inputs2.setGeometry(QtCore.QRect(10, 190, 41, 21))
        self.b_clear_inputs2.setStyleSheet("background-color: rgb(255, 157, 159);")
        self.b_clear_inputs2.setObjectName("b_clear_inputs2")
        self.out_characters2 = QtWidgets.QListWidget(parent=self.frame_2)
        self.out_characters2.setGeometry(QtCore.QRect(300, 30, 111, 121))
        self.out_characters2.setAcceptDrops(True)
        self.out_characters2.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DropOnly)
        self.out_characters2.setObjectName("out_characters2")
        self.cb_location2 = QtWidgets.QComboBox(parent=self.frame_2)
        self.cb_location2.setGeometry(QtCore.QRect(10, 30, 111, 22))
        self.cb_location2.setMaximumSize(QtCore.QSize(111, 16777215))
        self.cb_location2.setObjectName("cb_location2")
        self.label_13 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(130, 10, 111, 20))
        self.label_13.setToolTip("")
        self.label_13.setToolTipDuration(-1)
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.b_clear_out_characters2 = QtWidgets.QPushButton(parent=self.frame_2)
        self.b_clear_out_characters2.setGeometry(QtCore.QRect(300, 190, 41, 21))
        self.b_clear_out_characters2.setStyleSheet("background-color: rgb(255, 157, 159);")
        self.b_clear_out_characters2.setObjectName("b_clear_out_characters2")
        self.in_name2 = QtWidgets.QLineEdit(parent=self.frame_2)
        self.in_name2.setGeometry(QtCore.QRect(300, 160, 111, 22))
        self.in_name2.setText("")
        self.in_name2.setObjectName("in_name2")
        self.b_clear_out_names2 = QtWidgets.QPushButton(parent=self.frame_2)
        self.b_clear_out_names2.setGeometry(QtCore.QRect(130, 190, 41, 21))
        self.b_clear_out_names2.setStyleSheet("background-color: rgb(255, 157, 159);")
        self.b_clear_out_names2.setObjectName("b_clear_out_names2")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 49, 16))
        self.label_6.setObjectName("label_6")
        self.cb_name2 = QtWidgets.QComboBox(parent=self.frame_2)
        self.cb_name2.setGeometry(QtCore.QRect(10, 130, 111, 22))
        self.cb_name2.setMaximumSize(QtCore.QSize(111, 16777215))
        self.cb_name2.setObjectName("cb_name2")
        self.label_14 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(300, 10, 111, 20))
        self.label_14.setToolTip("")
        self.label_14.setToolTipDuration(-1)
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.cb_group2 = QtWidgets.QComboBox(parent=self.frame_2)
        self.cb_group2.setGeometry(QtCore.QRect(10, 80, 111, 22))
        self.cb_group2.setMaximumSize(QtCore.QSize(111, 16777215))
        self.cb_group2.setObjectName("cb_group2")
        self.label_7 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 49, 16))
        self.label_7.setToolTip("")
        self.label_7.setToolTipDuration(-1)
        self.label_7.setObjectName("label_7")
        self.label_15 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_15.setGeometry(QtCore.QRect(260, 160, 41, 21))
        self.label_15.setObjectName("label_15")
        self.b_shift2 = QtWidgets.QPushButton(parent=self.frame_2)
        self.b_shift2.setGeometry(QtCore.QRect(250, 80, 41, 41))
        self.b_shift2.setText("")
        self.b_shift2.setIcon(icon)
        self.b_shift2.setIconSize(QtCore.QSize(31, 31))
        self.b_shift2.setObjectName("b_shift2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.b_generate.setText(_translate("MainWindow", "Generate"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "-"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "-"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "0"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_8.setText(_translate("MainWindow", "Relation matrix"))
        self.b_save.setText(_translate("MainWindow", "Save"))
        self.b_clear_inputs1.setText(_translate("MainWindow", "clear"))
        self.label_11.setText(_translate("MainWindow", "List of names"))
        self.b_clear_out_characters1.setText(_translate("MainWindow", "clear"))
        self.b_clear_out_names1.setText(_translate("MainWindow", "clear"))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_2.setText(_translate("MainWindow", "Group"))
        self.label_10.setText(_translate("MainWindow", "Characters"))
        self.label.setText(_translate("MainWindow", "Location"))
        self.label_4.setText(_translate("MainWindow", "Name"))
        self.b_clear_inputs2.setText(_translate("MainWindow", "clear"))
        self.label_13.setText(_translate("MainWindow", "List of names"))
        self.b_clear_out_characters2.setText(_translate("MainWindow", "clear"))
        self.b_clear_out_names2.setText(_translate("MainWindow", "clear"))
        self.label_5.setText(_translate("MainWindow", "Name"))
        self.label_6.setText(_translate("MainWindow", "Group"))
        self.label_14.setText(_translate("MainWindow", "Characters"))
        self.label_7.setText(_translate("MainWindow", "Location"))
        self.label_15.setText(_translate("MainWindow", "Name"))
