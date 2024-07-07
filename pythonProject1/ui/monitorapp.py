import sys
from PyQt5.QtWidgets import QApplication
from ui.main_frame import MainDialog

class MonitorApp(QApplication):
    def __init__(self):
        super(MonitorApp, self).__init__(sys.argv)
        self.dialog = MainDialog()
        self.dialog.show()
