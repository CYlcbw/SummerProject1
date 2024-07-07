from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ResetPasswordWindow(object):
    def setupUi(self, ResetPasswordWindow):
        ResetPasswordWindow.setObjectName("ResetPasswordWindow")
        ResetPasswordWindow.resize(591, 487)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icons/reset_password_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ResetPasswordWindow.setWindowIcon(icon)

        # 设置背景图片
        ResetPasswordWindow.setStyleSheet("""
            QWidget#ResetPasswordWindow {
                background-image: url(D:/PycharmProject/project2/pythonProject1/data/che.png);
                background-repeat: no-repeat;
                background-position: center;
            }
        """)

        self.verticalLayout = QtWidgets.QVBoxLayout(ResetPasswordWindow)
        self.verticalLayout.setObjectName("verticalLayout")

        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        # 添加标题
        self.title_label = QtWidgets.QLabel(ResetPasswordWindow)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)

        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)

        self.username_input = QtWidgets.QLineEdit(ResetPasswordWindow)
        self.username_input.setMinimumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.username_input.setFont(font)
        self.username_input.setObjectName("username_input")
        self.gridLayout.addWidget(self.username_input, 0, 1, 1, 2)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 3, 1, 1)

        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)

        self.new_password_input = QtWidgets.QLineEdit(ResetPasswordWindow)
        self.new_password_input.setMinimumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.new_password_input.setFont(font)
        self.new_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_password_input.setObjectName("new_password_input")
        self.gridLayout.addWidget(self.new_password_input, 1, 1, 1, 2)

        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 3, 1, 1)

        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 0, 1, 1)

        self.secret_question_input = QtWidgets.QLineEdit(ResetPasswordWindow)
        self.secret_question_input.setMinimumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.secret_question_input.setFont(font)
        self.secret_question_input.setReadOnly(True)
        self.secret_question_input.setObjectName("secret_question_input")
        self.gridLayout.addWidget(self.secret_question_input, 2, 1, 1, 2)

        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 2, 3, 1, 1)

        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 3, 0, 1, 1)

        self.secret_answer_input = QtWidgets.QLineEdit(ResetPasswordWindow)
        self.secret_answer_input.setMinimumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.secret_answer_input.setFont(font)
        self.secret_answer_input.setObjectName("secret_answer_input")
        self.gridLayout.addWidget(self.secret_answer_input, 3, 1, 1, 2)

        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 3, 3, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem10)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)

        self.reset_button = QtWidgets.QPushButton(ResetPasswordWindow)
        self.reset_button.setMinimumSize(QtCore.QSize(200, 40))
        self.reset_button.setObjectName("reset_button")
        self.horizontalLayout.addWidget(self.reset_button)

        self.back_button = QtWidgets.QPushButton(ResetPasswordWindow)
        self.back_button.setMinimumSize(QtCore.QSize(200, 40))
        self.back_button.setObjectName("back_button")
        self.horizontalLayout.addWidget(self.back_button)

        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem12)

        self.verticalLayout.addLayout(self.horizontalLayout)

        spacerItem13 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem13)

        self.retranslateUi(ResetPasswordWindow)
        self.reset_button.clicked.connect(ResetPasswordWindow.r_reset_password)  # type: ignore
        self.back_button.clicked.connect(ResetPasswordWindow.r_back)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ResetPasswordWindow)

    def retranslateUi(self, ResetPasswordWindow):
        _translate = QtCore.QCoreApplication.translate
        ResetPasswordWindow.setWindowTitle(_translate("ResetPasswordWindow", "Reset Password"))
        self.title_label.setText(_translate("ResetPasswordWindow", "重置密码"))
        self.secret_question_input.setPlaceholderText(_translate("ResetPasswordWindow", "密保"))
        self.username_input.setPlaceholderText(_translate("ResetPasswordWindow", "账号"))
        self.secret_answer_input.setPlaceholderText(_translate("ResetPasswordWindow", "答案"))
        self.new_password_input.setPlaceholderText(_translate("ResetPasswordWindow", "新密码"))
        self.reset_button.setStyleSheet(_translate("ResetPasswordWindow", """
                  QPushButton {
                    background-color: #f44336;
                    color: white;
                    border-radius: 10px;
                  }
                  QPushButton:hover {
                    background-color: #da190b;
                  }
                """))
        self.reset_button.setText(_translate("ResetPasswordWindow", "修改"))
        self.back_button.setStyleSheet(_translate("ResetPasswordWindow", """
          QPushButton {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
          }
          QPushButton:hover {
            background-color: #45a049;
          }
        """))
        self.back_button.setText(_translate("ResetPasswordWindow", "返回"))
