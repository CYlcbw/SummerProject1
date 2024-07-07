import os
import json

class Monitor:
    def __init__(self, name, category, address):
        """初始化监控器对象"""
        self.name = name
        self.category = category
        self.address = address

class MonitorManager:
    def __init__(self, filename="data/monitor_data.txt"):
        """初始化监控器管理器对象"""
        self.filename = filename
        self.monitors = self.load_monitors()

    def load_monitors(self):
        """从文件中加载监控器列表"""
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as file:
            return json.load(file)

    def save_monitors(self):
        """将监控器列表保存到文件"""
        with open(self.filename, 'w') as file:
            json.dump(self.monitors, file)

    def add_monitor(self, monitor):
        """添加一个监控器"""
        if any(m['name'] == monitor.name for m in self.monitors):
            return False
        self.monitors.append(monitor.__dict__)
        self.save_monitors()
        return True

    def delete_monitor(self, name):
        """删除一个监控器"""
        self.monitors = [m for m in self.monitors if m['name'] != name]
        self.save_monitors()

    def update_monitor(self, old_name, new_name, new_address):
        """更新一个监控器"""
        for monitor in self.monitors:
            if monitor['name'] == old_name:
                monitor['name'] = new_name
                monitor['address'] = new_address
                self.save_monitors()
                return True
        return False

    def get_monitor(self, name):
        """获取一个监控器"""
        for monitor in self.monitors:
            if monitor['name'] == name:
                return monitor
        return None

    def get_monitors_by_category(self, category):
        """获取指定类别的所有监控器"""
        return [m for m in self.monitors if m['category'] == category]

    def get_all_monitors(self):
        """获取所有监控器"""
        return self.monitors
