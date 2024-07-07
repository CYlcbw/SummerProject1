from PyQt5.QtCore import QThread, pyqtSignal
import cv2
from ai.car import vehicle_detect, detect_plate_from_image
from ai.car_and_people import detect_people_and_vehicles
from ai.people import people_detect

class Video(QThread):
    send = pyqtSignal(int, int, int, bytes, object, dict)  # 添加一个参数表示检测到的车辆数或人流量

    def __init__(self, video_path, label, detection_mode, category, target_plate=None):
        super().__init__()
        self.video_path = video_path
        self.label = label
        # 检查video_path是否为数字字符串，如果是则转换为整数
        if video_path.isdigit():
            video_path = int(video_path)
        self.cap = cv2.VideoCapture(video_path)
        self.running = True
        self.detection_mode = detection_mode
        self.category = category
        self.target_plate = target_plate
        self.info = {'car': 0, 'tricycle': 0, 'motorbike': 0, 'bus': 0, 'truck': 0, 'carplate': 0, 'people': 0}

    def run(self):
        """线程运行方法，处理视频帧"""
        print("Starting video processing...")
        while self.cap.isOpened() and self.running:
            ret, frame = self.cap.read()#读取一帧视频
            if not ret:
                print("Failed to read frame.")
                break

            try:
                if self.detection_mode == "开始检测":
                    if self.category == "car":# 车辆检测
                        frame, vehicle_num, vehicle_info = vehicle_detect(frame)
                        self.info.update(vehicle_num)# 更新车辆数量和信息

                        if self.target_plate:# 检测车牌
                            for vehicle in vehicle_info:
                                location = vehicle['location']
                                x1 = location['left']
                                y1 = location['top']
                                x2 = x1 + location['width']
                                y2 = y1 + location['height']
                                car_img = frame[y1:y2, x1:x2]
                                if detect_plate_from_image(car_img, self.target_plate):
                                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0),
                                                  2)  # Blue for the target plate

                    elif self.category == "people":# 人流量检测
                        frame, people_num = people_detect(frame)
                        self.info['people'] = people_num # 更新人员数量

                elif self.detection_mode == "检测违规":# 违规检测，同时检测人流量和车流量
                    frame, vehicle_num, people_num, vehicle_info = detect_people_and_vehicles(frame)
                    self.info.update(vehicle_num)# 更新车辆数量和信息
                    self.info['people'] = people_num# 更新人员数量
                    if self.category == "car" and self.target_plate:# 检测车牌
                        for vehicle in vehicle_info:
                            location = vehicle['location']
                            x1 = location['left']
                            y1 = location['top']
                            x2 = x1 + location['width']
                            y2 = y1 + location['height']
                            car_img = frame[y1:y2, x1:x2]
                            if detect_plate_from_image(car_img, self.target_plate):
                                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)  #设置蓝色矩形框标识目标车牌
                h, w, c = frame.shape# 获取视频帧的高宽和通道数
                img_bytes = frame.tobytes()# 将视频帧转换为字节流
                self.send.emit(h, w, c, img_bytes, self.label, self.info)# 发送信号
                QThread.msleep(33)# 设置线程休眠时间，以防止CPU占用过高
            except Exception as e:
                print(f"Error during frame processing: {e}")
                break
        self.cap.release()# 释放视频流资源
        print("Video processing ended.")

    def stop(self):
        """停止线程运行"""
        self.running = False
        self.quit()
        self.wait()
