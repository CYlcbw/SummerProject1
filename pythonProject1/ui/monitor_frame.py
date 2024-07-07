from PyQt5.QtWidgets import QWidget, QStackedWidget, QHBoxLayout, QTableWidgetItem, QMessageBox, QInputDialog, \
    QPushButton, QComboBox, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QImage, QPixmap
from ui.car_detection import Ui_CarDetectionPage
from ui.people_detection import Ui_PeopleDetectionPage
from ui.car_monitor import Ui_CarMonitorPage
from ui.people_monitor import Ui_PeopleMonitorPage
from ui.modify_info import Ui_ModifyInfoPage
from ui.button_panel import Ui_ButtonPanel  # 导入生成的UI类
from management.monitor import Monitor, MonitorManager  # 导入监控管理类
from management.user import UserManager
from management.video import Video  # 导入视频类

class MonitorFrame(QWidget):
    def __init__(self, main_dialog):
        super().__init__()
        self.main_dialog = main_dialog
        self.monitor_manager = MonitorManager()
        self.video_threads = {}
        self.user_manager = UserManager()  # 添加用户管理实例
        self.used_cameras = []  # 添加用于跟踪已被选择的摄像头列表
        self.total_vehicle_info = {'car': 0, 'tricycle': 0, 'motorbike': 0, 'bus': 0, 'truck': 0, 'carplate': 0, 'people': 0}
        self.initUI()
        self.car_state = True
        self.people_state = False
        self.now_state = False
        #设置固定窗口大小
        self.setFixedSize(2000, 1500)
    def set_user_id(self, user_id):
        """设置登录用户id"""
        self.user_id = user_id
        self.user_manager.update()  # 调用 update 方法
        self.current_user = self.user_manager.get_user(self.user_id)  # 获取当前用户信息

    def initUI(self):
        """初始化UI"""
        main_layout = QVBoxLayout()  # 使用垂直布局
        self.setLayout(main_layout)

        # 初始化按钮面板
        self.button_panel = QWidget()
        self.ui_button_panel = Ui_ButtonPanel()
        self.ui_button_panel.setupUi(self.button_panel)

        # 连接按钮点击事件到对应的方法
        self.ui_button_panel.car_detection_button.clicked.connect(self.show_car_detection)
        self.ui_button_panel.people_detection_button.clicked.connect(self.show_people_detection)
        self.ui_button_panel.car_monitor_button.clicked.connect(self.show_car_monitor)
        self.ui_button_panel.people_monitor_button.clicked.connect(self.show_people_monitor)
        self.ui_button_panel.modify_info_button.clicked.connect(self.show_modify_info)
        self.ui_button_panel.exit_button.clicked.connect(self.exit_to_login)

        main_layout.addWidget(self.button_panel)

        # 初始化页面
        self.stack = QStackedWidget()
        self.initPages()
        main_layout.addWidget(self.stack)

    def initPages(self):
        """初始化页面"""
        self.car_detection_page = QWidget()
        self.ui_car_detection = Ui_CarDetectionPage()
        self.ui_car_detection.setupUi(self.car_detection_page)
        self.ui_car_detection.queryButton.clicked.connect(self.search_carplate)  # 添加查询按钮点击事件
        self.init_camera_comboboxes(self.ui_car_detection, "car")

        self.people_detection_page = QWidget()
        self.ui_people_detection = Ui_PeopleDetectionPage()
        self.ui_people_detection.setupUi(self.people_detection_page)
        self.init_camera_comboboxes(self.ui_people_detection, "people")

        self.car_monitor_page = QWidget()
        self.ui_car_monitor = Ui_CarMonitorPage()
        self.ui_car_monitor.setupUi(self.car_monitor_page)
        self.ui_car_monitor.addButton.clicked.connect(self.add_car_monitor)# 添加添加监控增加按钮点击事件
        self.load_car_monitors()

        self.people_monitor_page = QWidget()
        self.ui_people_monitor = Ui_PeopleMonitorPage()
        self.ui_people_monitor.setupUi(self.people_monitor_page)
        self.ui_people_monitor.addButton.clicked.connect(self.add_people_monitor)# 添加添加监控增加按钮点击事件
        self.load_people_monitors()

        self.modify_info_page = QWidget()
        self.ui_modify_info = Ui_ModifyInfoPage()
        self.ui_modify_info.setupUi(self.modify_info_page)
        self.ui_modify_info.submitButton.clicked.connect(self.modify_user_info)  # 连接提交按钮

        self.stack.addWidget(self.car_detection_page)
        self.stack.addWidget(self.people_detection_page)
        self.stack.addWidget(self.car_monitor_page)
        self.stack.addWidget(self.people_monitor_page)
        self.stack.addWidget(self.modify_info_page)

    def show_modify_info(self):
        """显示修改信息页面"""
        self.update_ui_with_user_info()
        self.stack.setCurrentWidget(self.modify_info_page)

    def update_ui_with_user_info(self):
        """用当前用户信息更新UI"""
        if self.current_user:
            print(self.current_user['username'])
            self.ui_modify_info.usernameEdit.setText(self.current_user['username'])
            self.ui_modify_info.usernameEdit.setReadOnly(True)  # 设置用户名文本框为只读
            self.ui_modify_info.passwordEdit.setText(self.current_user['password'])
            self.ui_modify_info.securityQuestionEdit.setText(self.current_user['secret_question'])
            self.ui_modify_info.securityAnswerEdit.setText(self.current_user['secret_answer'])

    def modify_user_info(self):
        """修改用户信息"""
        username = self.user_id
        password = self.ui_modify_info.passwordEdit.text()
        security_question = self.ui_modify_info.securityQuestionEdit.text()
        security_answer = self.ui_modify_info.securityAnswerEdit.text()

        if self.user_manager.update_user(username, password, security_question, security_answer):
            QMessageBox.information(self, "成功", "用户信息已更新")
        else:
            QMessageBox.warning(self, "错误", "更新用户信息失败")
    def search_carplate(self):
        """查找车牌"""
        target_plate = self.ui_car_detection.carPlateInput.text()
        for label in self.video_threads:
            self.video_threads[label].target_plate = target_plate

    def start_video_stream(self, video_path, label, detection_mode, category):
        """开始视频"""
        print("this category:",category)
        if video_path in self.used_cameras:
            QMessageBox.warning(self, "错误", "该摄像头已被选择")
            return
        video_thread = Video(video_path, label, detection_mode, category)
        video_thread.send.connect(self.update_video_display)
        self.video_threads[label] = video_thread  # 保存引用防止线程被垃圾回收
        video_thread.start()
        self.used_cameras.append(video_path)

    def stop_video_stream(self, video_path):
        """停止视频"""
        if video_path in self.used_cameras:
            self.used_cameras.remove(video_path)

    def on_camera_selected(self, idx, combo_box):
        """处理摄像头选择事件"""
        label = self.get_label_by_combobox(combo_box)
        control_box = self.get_control_box_by_combobox(combo_box)
        detection_mode = control_box.currentText() if control_box else "关闭检测"
        category = "car" if self.stack.currentWidget() == self.car_detection_page else "people"

        if idx == 0:  # "选择摄像头"
            if label in self.video_threads:
                video_path = self.video_threads[label].video_path
                self.video_threads[label].stop()
                del self.video_threads[label]
                self.stop_video_stream(video_path)
            label.clear()
            label.setStyleSheet("background-color: black;")
            return

        camera_name = combo_box.currentText()
        monitors = self.monitor_manager.get_all_monitors()
        selected_monitor = next((m for m in monitors if m['name'] == camera_name), None)

        if selected_monitor:
            video_address = selected_monitor['address']
            if video_address in self.used_cameras and not self.now_state:
                self.now_state = False
                QMessageBox.warning(self, "错误", "该摄像头已被选择")
                combo_box.setCurrentIndex(0)
                return
            if label in self.video_threads:
                old_video_path = self.video_threads[label].video_path
                self.video_threads[label].stop()
                del self.video_threads[label]
                self.stop_video_stream(old_video_path)
            if label:
                if self.car_state:
                    category = "car"
                elif self.people_state:
                    category = "people"
                self.start_video_stream(video_address, label, detection_mode, category)

    def on_detection_mode_selected(self, idx, combo_box):
        """处理检测模式选择事件"""
        camera_box = self.get_camera_box_by_control_box(combo_box)
        if camera_box.currentIndex() == 0:  # 没有选择摄像头
            return
        self.now_state = True
        self.on_camera_selected(camera_box.currentIndex(), camera_box)

    def get_label_by_combobox(self, combo_box):
        """根据组合框获取对应的显示标签"""
        if combo_box == self.ui_car_detection.cameraCombo1:
            return self.ui_car_detection.monitorDisplay1
        elif combo_box == self.ui_car_detection.cameraCombo2:
            return self.ui_car_detection.monitorDisplay2
        elif combo_box == self.ui_car_detection.cameraCombo3:
            return self.ui_car_detection.monitorDisplay3
        elif combo_box == self.ui_car_detection.cameraCombo4:
            return self.ui_car_detection.monitorDisplay4
        elif combo_box == self.ui_people_detection.cameraCombo1:
            return self.ui_people_detection.monitorDisplay1
        elif combo_box == self.ui_people_detection.cameraCombo2:
            return self.ui_people_detection.monitorDisplay2
        elif combo_box == self.ui_people_detection.cameraCombo3:
            return self.ui_people_detection.monitorDisplay3
        elif combo_box == self.ui_people_detection.cameraCombo4:
            return self.ui_people_detection.monitorDisplay4
        return None

    def get_control_box_by_combobox(self, combo_box):
        """根据组合框获取对应的控制框"""
        if combo_box == self.ui_car_detection.cameraCombo1:
            return self.ui_car_detection.monitorControl1
        elif combo_box == self.ui_car_detection.cameraCombo2:
            return self.ui_car_detection.monitorControl2
        elif combo_box == self.ui_car_detection.cameraCombo3:
            return self.ui_car_detection.monitorControl3
        elif combo_box == self.ui_car_detection.cameraCombo4:
            return self.ui_car_detection.monitorControl4
        elif combo_box == self.ui_people_detection.cameraCombo1:
            return self.ui_people_detection.monitorControl1
        elif combo_box == self.ui_people_detection.cameraCombo2:
            return self.ui_people_detection.monitorControl2
        elif combo_box == self.ui_people_detection.cameraCombo3:
            return self.ui_people_detection.monitorControl3
        elif combo_box == self.ui_people_detection.cameraCombo4:
            return self.ui_people_detection.monitorControl4
        return None

    def get_camera_box_by_control_box(self, control_box):
        """根据控制框获取对应的组合框"""
        if control_box == self.ui_car_detection.monitorControl1:
            return self.ui_car_detection.cameraCombo1
        elif control_box == self.ui_car_detection.monitorControl2:
            return self.ui_car_detection.cameraCombo2
        elif control_box == self.ui_car_detection.monitorControl3:
            return self.ui_car_detection.cameraCombo3
        elif control_box == self.ui_car_detection.monitorControl4:
            return self.ui_car_detection.cameraCombo4
        elif control_box == self.ui_people_detection.monitorControl1:
            return self.ui_people_detection.cameraCombo1
        elif control_box == self.ui_people_detection.monitorControl2:
            return self.ui_people_detection.cameraCombo2
        elif control_box == self.ui_people_detection.monitorControl3:
            return self.ui_people_detection.cameraCombo3
        elif control_box == self.ui_people_detection.monitorControl4:
            return self.ui_people_detection.cameraCombo4
        return None

    def update_video_display(self, h, w, c, img_bytes, label, info):
        """更新监控区域显示"""
        image = QImage(img_bytes, w, h, w * c, QImage.Format_BGR888)
        pix = QPixmap.fromImage(image)
        label.setPixmap(pix)

        # 更新UI上的流量信息
        if label == self.ui_car_detection.monitorDisplay1:
            text = f"车流数量: {info['car']}<br>违规人数: {info['people']}"
            self.ui_car_detection.trafficLabel1.setText(text)
        elif label == self.ui_car_detection.monitorDisplay2:
            text = f"车流数量: {info['car']}<br>违规人数: {info['people']}"
            self.ui_car_detection.trafficLabel2.setText(text)
        elif label == self.ui_car_detection.monitorDisplay3:
            text = f"车流数量: {info['car']}<br>违规人数: {info['people']}"
            self.ui_car_detection.trafficLabel3.setText(text)
        elif label == self.ui_car_detection.monitorDisplay4:
            text = f"车流数量: {info['car']}<br>违规人数: {info['people']}"
            self.ui_car_detection.trafficLabel4.setText(text)
        elif label == self.ui_people_detection.monitorDisplay1:
            text = f"行人数量: {info['people']}<br>违规车数: {info['car']}"
            self.ui_people_detection.peopleLabel1.setText(text)
        elif label == self.ui_people_detection.monitorDisplay2:
            text = f"行人数量: {info['people']}<br>违规车数: {info['car']}"
            self.ui_people_detection.peopleLabel2.setText(text)
        elif label == self.ui_people_detection.monitorDisplay3:
            text = f"行人数量: {info['people']}<br>违规车数: {info['car']}"
            self.ui_people_detection.peopleLabel3.setText(text)
        elif label == self.ui_people_detection.monitorDisplay4:
            text = f"行人数量: {info['people']}<br>违规车数: {info['car']}"
            self.ui_people_detection.peopleLabel4.setText(text)

        # 更新汇总信息
        self.update_total_info(info)

    def update_total_info(self, info):
        """更新总的汇总信息"""
        # 重新计算每个检测区域的汇总信息
        self.total_vehicle_info = {key: 0 for key in self.total_vehicle_info}  # 重置为0
        for thread_label in self.video_threads:
            thread_info = self.video_threads[thread_label].info
            for key in self.total_vehicle_info:
                self.total_vehicle_info[key] += thread_info.get(key, 0)

        # 更新UI上的汇总信息
        total_info_text = "\n".join([f"{key}: {value}" for key, value in self.total_vehicle_info.items()])
        self.ui_car_detection.totalInfoLabel.setText(total_info_text)

    def show_car_detection(self):
        """显示车流检测页面"""
        self.car_state = True
        self.people_state = False
        self.check_and_update_camera_status(self.ui_car_detection, "car")
        self.stack.setCurrentWidget(self.car_detection_page)

    def show_people_detection(self):
        """显示人流检测页面"""
        self.people_state = True
        self.car_state = False
        self.check_and_update_camera_status(self.ui_people_detection, "people")
        self.stack.setCurrentWidget(self.people_detection_page)

    def show_car_monitor(self):
        """显示车流监控管理页面"""
        self.stack.setCurrentWidget(self.car_monitor_page)

    def show_people_monitor(self):
        """显示人流监控管理页面"""
        self.stack.setCurrentWidget(self.people_monitor_page)

    def exit_to_login(self):
        """退出到登录页面"""
        self.main_dialog.switch_window('login')

    def load_car_monitors(self):
        """加载车流监控"""
        self.ui_car_monitor.table.setRowCount(0)
        monitors = self.monitor_manager.get_monitors_by_category("车流")
        for monitor in monitors:
            self.add_car_monitor_row(monitor)

    def add_car_monitor_row(self, monitor):
        """添加车流监控行"""
        row_position = self.ui_car_monitor.table.rowCount()
        self.ui_car_monitor.table.insertRow(row_position)

        name_item = QTableWidgetItem(monitor['name'])
        self.ui_car_monitor.table.setItem(row_position, 0, name_item)

        edit_button = QPushButton("修改")
        edit_button.clicked.connect(lambda _, row=row_position: self.edit_car_monitor(row))
        self.ui_car_monitor.table.setCellWidget(row_position, 1, edit_button)

        delete_button = QPushButton("删除")
        delete_button.clicked.connect(lambda _, row=row_position: self.delete_car_monitor(row))
        self.ui_car_monitor.table.setCellWidget(row_position, 2, delete_button)

        address_item = QTableWidgetItem(monitor['address'])
        self.ui_car_monitor.table.setItem(row_position, 3, address_item)

    def add_car_monitor(self):
        """增加车流监控"""
        name, ok = QInputDialog.getText(self, "增加监控", "输入监控名称:")
        if not ok or not name:
            return

        address, ok = QInputDialog.getText(self, "增加监控", "输入监控地址:")
        if not ok or not address:
            return

        monitor = Monitor(name, "车流", address)
        if self.monitor_manager.add_monitor(monitor):
            self.add_car_monitor_row(monitor.__dict__)
        else:
            QMessageBox.warning(self, "错误", "监控名称已存在")

    def edit_car_monitor(self, row):
        """修改车流监控"""
        name_item = self.ui_car_monitor.table.item(row, 0)
        old_name = name_item.text()

        new_name, ok = QInputDialog.getText(self, "修改监控", "输入新的监控名称:", text=old_name)
        if not ok or not new_name:
            return

        address, ok = QInputDialog.getText(self, "修改监控", "输入新的监控地址:")
        if not ok or not address:
            return

        if self.monitor_manager.update_monitor(old_name, new_name, address):
            name_item.setText(new_name)
            address_item = self.ui_car_monitor.table.item(row, 3)
            address_item.setText(address)
        else:
            QMessageBox.warning(self, "错误", "修改监控失败")

    def delete_car_monitor(self, row):
        """删除车流监控"""
        name_item = self.ui_car_monitor.table.item(row, 0)
        name = name_item.text()

        self.monitor_manager.delete_monitor(name)
        self.ui_car_monitor.table.removeRow(row)

    def load_people_monitors(self):
        """加载人流监控"""
        self.ui_people_monitor.table.setRowCount(0)
        monitors = self.monitor_manager.get_monitors_by_category("人流")
        for monitor in monitors:
            self.add_people_monitor_row(monitor)

    def add_people_monitor_row(self, monitor):
        """添加人流监控行"""
        row_position = self.ui_people_monitor.table.rowCount()
        self.ui_people_monitor.table.insertRow(row_position)

        name_item = QTableWidgetItem(monitor['name'])
        self.ui_people_monitor.table.setItem(row_position, 0, name_item)

        edit_button = QPushButton("修改")
        edit_button.clicked.connect(lambda _, row=row_position: self.edit_people_monitor(row))
        self.ui_people_monitor.table.setCellWidget(row_position, 1, edit_button)

        delete_button = QPushButton("删除")
        delete_button.clicked.connect(lambda _, row=row_position: self.delete_people_monitor(row))
        self.ui_people_monitor.table.setCellWidget(row_position, 2, delete_button)

        address_item = QTableWidgetItem(monitor['address'])
        self.ui_people_monitor.table.setItem(row_position, 3, address_item)

    def add_people_monitor(self):
        """增加人流监控"""
        name, ok = QInputDialog.getText(self, "增加监控", "输入监控名称:")
        if not ok or not name:
            return

        address, ok = QInputDialog.getText(self, "增加监控", "输入监控地址:")
        if not ok or not address:
            return

        monitor = Monitor(name, "人流", address)
        if self.monitor_manager.add_monitor(monitor):
            self.add_people_monitor_row(monitor.__dict__)
        else:
            QMessageBox.warning(self, "错误", "监控名称已存在")

    def edit_people_monitor(self, row):
        """修改人流监控"""
        name_item = self.ui_people_monitor.table.item(row, 0)
        old_name = name_item.text()

        new_name, ok = QInputDialog.getText(self, "修改监控", "输入新的监控名称:", text=old_name)
        if not ok or not new_name:
            return

        address, ok = QInputDialog.getText(self, "修改监控", "输入新的监控地址:")
        if not ok or not address:
            return

        if self.monitor_manager.update_monitor(old_name, new_name, address):
            name_item.setText(new_name)
            address_item = self.ui_people_monitor.table.item(row, 3)
            address_item.setText(address)
        else:
            QMessageBox.warning(self, "错误", "修改监控失败")

    def delete_people_monitor(self, row):
        """删除人流监控"""
        name_item = self.ui_people_monitor.table.item(row, 0)
        name = name_item.text()

        self.monitor_manager.delete_monitor(name)
        self.ui_people_monitor.table.removeRow(row)

    def init_camera_comboboxes(self, ui_page, category):
        """初始化摄像头组合框"""
        # 读取监控数据
        if category == "car":
            monitors = self.monitor_manager.get_monitors_by_category("车流")
        else:
            monitors = self.monitor_manager.get_monitors_by_category("人流")

        # 读取所有的 QComboBox
        combo_boxes = [
            ui_page.cameraCombo1,
            ui_page.cameraCombo2,
            ui_page.cameraCombo3,
            ui_page.cameraCombo4
        ]

        for combo_box in combo_boxes:
            combo_box.clear()
            combo_box.addItem("选择摄像头")
            for monitor in monitors:
                camera_name = monitor['name']
                combo_box.addItem(camera_name)

            combo_box.currentIndexChanged.connect(lambda idx, cb=combo_box: self.on_camera_selected(idx, cb))

        control_boxes = [
            ui_page.monitorControl1,
            ui_page.monitorControl2,
            ui_page.monitorControl3,
            ui_page.monitorControl4
        ]

        for control_box in control_boxes:
            control_box.currentIndexChanged.connect(
                lambda idx, cb=control_box: self.on_detection_mode_selected(idx, cb))

        # 添加流量显示标签
        if category == "car":
            ui_page.trafficLabel1.setText("车流数量: 0<br>违规人数: 0")
            ui_page.trafficLabel2.setText("车流数量: 0<br>违规人数: 0")
            ui_page.trafficLabel3.setText("车流数量: 0<br>违规人数: 0")
            ui_page.trafficLabel4.setText("车流数量: 0<br>违规人数: 0")
        elif category == "people":
            ui_page.peopleLabel1.setText("行人数量: 0<br>违规车数: 0")
            ui_page.peopleLabel2.setText("行人数量: 0<br>违规车数: 0")
            ui_page.peopleLabel3.setText("行人数量: 0<br>违规车数: 0")
            ui_page.peopleLabel4.setText("行人数量: 0<br>违规车数: 0")

    def check_and_update_camera_status(self, ui_page, category):
        """检查并更新摄像头状态"""
        monitors = self.monitor_manager.get_monitors_by_category("车流" if category == "car" else "人流")
        existing_cameras = {monitor['name'] for monitor in monitors}
        self.used_cameras.clear()

        combo_boxes = [
            ui_page.cameraCombo1,
            ui_page.cameraCombo2,
            ui_page.cameraCombo3,
            ui_page.cameraCombo4
        ]

        labels = [
            self.get_label_by_combobox(ui_page.cameraCombo1),
            self.get_label_by_combobox(ui_page.cameraCombo2),
            self.get_label_by_combobox(ui_page.cameraCombo3),
            self.get_label_by_combobox(ui_page.cameraCombo4)
        ]

        for combo_box, label in zip(combo_boxes, labels):
            current_camera = combo_box.currentText()
            combo_box.blockSignals(True)
            combo_box.clear()
            combo_box.addItem("选择摄像头")

            for monitor in monitors:
                combo_box.addItem(monitor['name'])

            # 检查当前选择的摄像头是否存在于更新后的列表中
            if current_camera in existing_cameras:
                combo_box.setCurrentText(current_camera)
                self.on_camera_selected(current_camera, combo_box)  # 重置下拉框选择
            else:
                print(current_camera)
                self.on_camera_selected(0, combo_box)  # 重置下拉框选择

            combo_box.blockSignals(False)
