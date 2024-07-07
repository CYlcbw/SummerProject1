# main_frame.py
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QStackedWidget, QWidget
from pyqt5_plugins.examplebuttonplugin import QtGui
from management.user import User, UserManager
from ui.login import Ui_LoginWindow
from ui.register import Ui_RegisterWindow
from ui.reset_password import Ui_ResetPasswordWindow
from ui.monitor_frame import MonitorFrame

class MainDialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.user_id = None
        self.initUI()

    def initUI(self):
        """初始化UI"""
        self.setWindowTitle('监控管理系统')
        self.setGeometry(200, 100, 800, 600)

        self.setWindowIcon(QIcon('D:\PycharmProject\project2\pythonProject1\data\logo.png'))
        # 创建QStackedWidget用于切换页面
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # 创建页面实例
        self.login_page = LoginPage(self)
        self.register_page = RegisterPage(self)
        self.reset_password_page = ResetPasswordPage(self)
        self.monitor_frame = MonitorFrame(self)

        # 将页面添加到 QStackedWidget 中
        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.register_page)
        self.stacked_widget.addWidget(self.reset_password_page)
        self.stacked_widget.addWidget(self.monitor_frame)

        # 显示登录页面
        self.stacked_widget.setCurrentWidget(self.login_page)

    def switch_window(self, window_name, user_id=None):
        """切换窗口"""
        if window_name == 'login':
            self.stacked_widget.setCurrentWidget(self.login_page)
        elif window_name == 'register':
            self.stacked_widget.setCurrentWidget(self.register_page)
        elif window_name == 'reset_password':
            self.stacked_widget.setCurrentWidget(self.reset_password_page)
        elif window_name == 'monitor':
            self.monitor_frame.set_user_id(user_id)
            self.stacked_widget.setCurrentWidget(self.monitor_frame)

class LoginPage(QWidget):
    def __init__(self, main_dialog):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.main_dialog = main_dialog
        self.user_manager = UserManager()

    def l_login(self):
        """登录"""
        self.user_manager.update()  # 调用 update 方法
        username = self.ui.username_input.text()
        password = self.ui.password_input.text()
        if self.user_manager.validate_user(username, password):
            QMessageBox.information(self, "提示", "登录成功")
            self.main_dialog.switch_window('monitor', username)
        else:
            QMessageBox.warning(self, "错误", "账号或密码错误")

    def l_register(self):
        """切换到注册页面"""
        self.main_dialog.switch_window('register')

    def l_reset_password(self):
        """切换到重置密码页面"""
        self.main_dialog.switch_window('reset_password')

class RegisterPage(QWidget):
    def __init__(self, main_dialog):
        super().__init__()
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self)
        self.main_dialog = main_dialog
        self.user_manager = UserManager()

    def r_register(self):
        """注册"""
        username = self.ui.username_input.text()
        password = self.ui.password_input.text()
        secret_question = self.ui.secret_question_input.text()
        secret_answer = self.ui.secret_answer_input.text()

        if not username or not password:
            QMessageBox.warning(self, "错误", "账号或密码不能为空")
        elif self.user_manager.get_user(username):
            QMessageBox.warning(self, "错误", "账号已存在")
        else:
            new_user = User(username, password, secret_question, secret_answer)
            if self.user_manager.add_user(new_user):
                self.user_manager.update()  # 调用 update 方法
                QMessageBox.information(self, "提示", "注册成功")
                self.r_back()
            else:
                QMessageBox.warning(self, "错误", "注册失败")

    def r_back(self):
        """返回登录页面"""
        self.main_dialog.switch_window('login')

class ResetPasswordPage(QWidget):
    def __init__(self, main_dialog):
        super().__init__()
        self.ui = Ui_ResetPasswordWindow()
        self.ui.setupUi(self)
        self.main_dialog = main_dialog
        self.user_manager = UserManager()
        self.ui.username_input.textChanged.connect(self.load_secret_question)

    def load_secret_question(self):
        """加载密保问题"""
        username = self.ui.username_input.text()
        self.user_manager.update()  # 调用 update 方法
        user = self.user_manager.get_user(username)
        if user:
            self.ui.secret_question_input.setText(user['secret_question'])
        else:
            self.ui.secret_question_input.clear()

    def r_reset_password(self):
        """重置密码"""
        username = self.ui.username_input.text()
        new_password = self.ui.new_password_input.text()
        secret_answer = self.ui.secret_answer_input.text()

        if self.user_manager.validate_secret_answer(username, secret_answer):
            self.user_manager.update_user(username, password=new_password)
            self.user_manager.update()  # 调用 update 方法
            QMessageBox.information(self, "提示", "密码修改成功")
            self.r_back()
        else:
            QMessageBox.warning(self, "错误", "账号或密保答案错误")

    def r_back(self):
        """返回登录页面"""
        self.main_dialog.switch_window('login')

