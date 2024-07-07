import json
import os

class User:
    def __init__(self, username, password, secret_question, secret_answer):
        """初始化用户对象"""
        self.username = username
        self.password = password
        self.secret_question = secret_question
        self.secret_answer = secret_answer

class UserManager:
    def __init__(self, file_path='data/user_data.txt'):
        """初始化用户管理器"""
        self.file_path = file_path
        self.users = self.load_users()

    def load_users(self):
        """从文件中加载用户数据"""
        if not os.path.exists(self.file_path):
            return {}
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def save_users(self):
        """将用户数据保存到文件"""
        with open(self.file_path, 'w') as file:
            json.dump(self.users, file, indent=4)

    def add_user(self, user):
        """添加新用户"""
        if user.username in self.users:
            return False  # 用户名已存在，返回False
        self.users[user.username] = user.__dict__  # 将用户对象转换为字典并添加到用户数据中
        self.save_users()  # 保存用户数据
        return True  # 用户添加成功，返回True

    def update_user(self, username, password=None, secret_question=None, secret_answer=None):
        """更新用户信息"""
        if username not in self.users:
            return False  # 用户名不存在，返回False
        if password is not None:
            self.users[username]['password'] = password
        if secret_question is not None:
            self.users[username]['secret_question'] = secret_question
        if secret_answer is not None:
            self.users[username]['secret_answer'] = secret_answer
        self.save_users()  # 保存更新后的用户数据
        return True  # 用户信息更新成功，返回True

    def get_user(self, username):
        """获取用户信息"""
        return self.users.get(username)

    def validate_user(self, username, password):
        """验证用户名和密码"""
        user = self.get_user(username)
        if user and user['password'] == password:
            return True
        return False

    def validate_secret_answer(self, username, secret_answer):
        """验证秘密答案"""
        user = self.get_user(username)
        if user and user['secret_answer'] == secret_answer:
            return True
        return False

    def update(self):
        """更新用户管理器"""
        self.users = self.load_users()

