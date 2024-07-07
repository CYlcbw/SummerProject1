from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(590, 486)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\PycharmProject\project2\pythonProject1\data\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("D:\PycharmProject\project2\pythonProject1\data\logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setStyleSheet("""
            QWidget#LoginWindow {
                background-image: url(D:\PycharmProject\project2\pythonProject1\data\che.png);
                background-repeat: no-repeat;
                background-position: center;
            }
        """)

        LoginWindow.setProperty("fixedSize", QtCore.QSize(560, 485))
        self.verticalLayout = QtWidgets.QVBoxLayout(LoginWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.title_label = QtWidgets.QLabel(LoginWindow)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.password_input = QtWidgets.QLineEdit(LoginWindow)
        self.password_input.setMinimumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.password_input.setFont(font)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.gridLayout.addWidget(self.password_input, 2, 1, 1, 2)
        self.username_input = QtWidgets.QLineEdit(LoginWindow)
        self.username_input.setMinimumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.username_input.setFont(font)
        self.username_input.setObjectName("username_input")
        self.gridLayout.addWidget(self.username_input, 1, 1, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.login_button = QtWidgets.QPushButton(LoginWindow)
        self.login_button.setMinimumSize(QtCore.QSize(150, 40))
        self.login_button.setObjectName("login_button")
        self.horizontalLayout.addWidget(self.login_button)
        self.register_button = QtWidgets.QPushButton(LoginWindow)
        self.register_button.setMinimumSize(QtCore.QSize(150, 40))
        self.register_button.setObjectName("register_button")
        self.horizontalLayout.addWidget(self.register_button)
        self.reset_password_button = QtWidgets.QPushButton(LoginWindow)
        self.reset_password_button.setMinimumSize(QtCore.QSize(150, 40))
        self.reset_password_button.setObjectName("reset_password_button")
        self.horizontalLayout.addWidget(self.reset_password_button)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem14)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem15)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem16)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem17)

        self.retranslateUi(LoginWindow)
        self.login_button.clicked.connect(LoginWindow.l_login)  # type: ignore
        self.register_button.clicked.connect(LoginWindow.l_register)  # type: ignore
        self.reset_password_button.clicked.connect(LoginWindow.l_reset_password)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setStyleSheet("""
                    QWidget#LoginWindow {
                        background-image: url(D:\PycharmProject\project2\pythonProject1\data\che.png);
                        background-repeat: no-repeat;
                        background-position: center;
                    }
                """)
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.title_label.setText(_translate("LoginWindow", "监控管理系统"))
        self.password_input.setPlaceholderText(_translate("LoginWindow", "密码"))
        self.username_input.setPlaceholderText(_translate("LoginWindow", "账号"))
        self.login_button.setStyleSheet(_translate("LoginWindow", """
          QPushButton {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
          }
          QPushButton:hover {
            background-color: #45a049;
          }
        """))
        self.login_button.setText(_translate("LoginWindow", "登录"))
        self.register_button.setStyleSheet(_translate("LoginWindow", """
          QPushButton {
            background-color: #008CBA;
            color: white;
            border-radius: 10px;
          }
          QPushButton:hover {
            background-color: #007BB5;
          }
        """))
        self.register_button.setText(_translate("LoginWindow", "注册"))
        self.reset_password_button.setStyleSheet(_translate("LoginWindow", """
          QPushButton {
            background-color: #f44336;
            color: white;
            border-radius: 10px;
          }
          QPushButton:hover {
            background-color: #da190b;
          }
        """))
        self.reset_password_button.setText(_translate("LoginWindow", "找回密码"))
