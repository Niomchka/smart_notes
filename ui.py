# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(812, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(3, 6, 531, 581))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(540, 10, 261, 581))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.notes_list = QtWidgets.QListWidget(parent=self.verticalLayoutWidget)
        self.notes_list.setObjectName("notes_list")
        self.verticalLayout.addWidget(self.notes_list)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_note = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.add_note.setObjectName("add_note")
        self.horizontalLayout.addWidget(self.add_note)
        self.del_note = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.del_note.setObjectName("del_note")
        self.horizontalLayout.addWidget(self.del_note)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.save_note = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.save_note.setObjectName("save_note")
        self.verticalLayout.addWidget(self.save_note)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.tags_list = QtWidgets.QListWidget(parent=self.verticalLayoutWidget)
        self.tags_list.setObjectName("tags_list")
        self.verticalLayout.addWidget(self.tags_list)
        self.tag_input = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.tag_input.setObjectName("tag_input")
        self.verticalLayout.addWidget(self.tag_input)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add_tag = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.add_tag.setObjectName("add_tag")
        self.horizontalLayout_2.addWidget(self.add_tag)
        self.del_teg = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.del_teg.setObjectName("del_teg")
        self.horizontalLayout_2.addWidget(self.del_teg)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.search_btn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.search_btn.setObjectName("search_btn")
        self.verticalLayout.addWidget(self.search_btn)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "список нотаток"))
        self.add_note.setText(_translate("MainWindow", "додати нотатку"))
        self.del_note.setText(_translate("MainWindow", "видалити нотатку"))
        self.save_note.setText(_translate("MainWindow", "зберегти"))
        self.label_2.setText(_translate("MainWindow", "список тегів"))
        self.tag_input.setPlaceholderText(_translate("MainWindow", "введіть тег"))
        self.add_tag.setText(_translate("MainWindow", "додати тег"))
        self.del_teg.setText(_translate("MainWindow", "видалитит тег"))
        self.search_btn.setText(_translate("MainWindow", "шукати нотатку по тегу"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
