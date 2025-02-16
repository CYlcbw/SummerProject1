# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'people_detection.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PeopleDetectionPage(object):
    def setupUi(self, PeopleDetectionPage):
        PeopleDetectionPage.setObjectName("PeopleDetectionPage")
        PeopleDetectionPage.resize(723, 657)
        self.mainLayout = QtWidgets.QVBoxLayout(PeopleDetectionPage)
        self.mainLayout.setObjectName("mainLayout")
        self.monitorsLayout1 = QtWidgets.QHBoxLayout()
        self.monitorsLayout1.setObjectName("monitorsLayout1")
        self.monitor1 = QtWidgets.QFrame(PeopleDetectionPage)
        self.monitor1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.monitor1.setObjectName("monitor1")
        self.layout1 = QtWidgets.QVBoxLayout(self.monitor1)
        self.layout1.setObjectName("layout1")
        self.topLayout1 = QtWidgets.QHBoxLayout()
        self.topLayout1.setObjectName("topLayout1")
        self.monitorControl1 = QtWidgets.QComboBox(self.monitor1)
        self.monitorControl1.setObjectName("monitorControl1")
        self.monitorControl1.addItem("")
        self.monitorControl1.addItem("")
        self.monitorControl1.addItem("")
        self.topLayout1.addWidget(self.monitorControl1)
        self.layout1.addLayout(self.topLayout1)
        self.monitorDisplay1 = QtWidgets.QLabel(self.monitor1)
        self.monitorDisplay1.setMinimumSize(QtCore.QSize(640, 400))
        self.monitorDisplay1.setStyleSheet("background-color: black; color: white;")
        self.monitorDisplay1.setAlignment(QtCore.Qt.AlignCenter)
        self.monitorDisplay1.setObjectName("monitorDisplay1")
        self.layout1.addWidget(self.monitorDisplay1)
        self.bottomLayout1 = QtWidgets.QHBoxLayout()
        self.bottomLayout1.setObjectName("bottomLayout1")
        self.cameraCombo1 = QtWidgets.QComboBox(self.monitor1)
        self.cameraCombo1.setObjectName("cameraCombo1")
        self.bottomLayout1.addWidget(self.cameraCombo1)
        self.peopleLabel1 = QtWidgets.QLabel(self.monitor1)
        self.peopleLabel1.setObjectName("peopleLabel1")
        self.bottomLayout1.addWidget(self.peopleLabel1)
        self.layout1.addLayout(self.bottomLayout1)
        self.monitorsLayout1.addWidget(self.monitor1)
        self.monitor2 = QtWidgets.QFrame(PeopleDetectionPage)
        self.monitor2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.monitor2.setObjectName("monitor2")
        self.layout2 = QtWidgets.QVBoxLayout(self.monitor2)
        self.layout2.setObjectName("layout2")
        self.topLayout2 = QtWidgets.QHBoxLayout()
        self.topLayout2.setObjectName("topLayout2")
        self.monitorControl2 = QtWidgets.QComboBox(self.monitor2)
        self.monitorControl2.setObjectName("monitorControl2")
        self.monitorControl2.addItem("")
        self.monitorControl2.addItem("")
        self.monitorControl2.addItem("")
        self.topLayout2.addWidget(self.monitorControl2)
        self.layout2.addLayout(self.topLayout2)
        self.monitorDisplay2 = QtWidgets.QLabel(self.monitor2)
        self.monitorDisplay2.setMinimumSize(QtCore.QSize(640, 400))
        self.monitorDisplay2.setStyleSheet("background-color: black; color: white;")
        self.monitorDisplay2.setAlignment(QtCore.Qt.AlignCenter)
        self.monitorDisplay2.setObjectName("monitorDisplay2")
        self.layout2.addWidget(self.monitorDisplay2)
        self.bottomLayout2 = QtWidgets.QHBoxLayout()
        self.bottomLayout2.setObjectName("bottomLayout2")
        self.cameraCombo2 = QtWidgets.QComboBox(self.monitor2)
        self.cameraCombo2.setObjectName("cameraCombo2")
        self.bottomLayout2.addWidget(self.cameraCombo2)
        self.peopleLabel2 = QtWidgets.QLabel(self.monitor2)
        self.peopleLabel2.setObjectName("peopleLabel2")
        self.bottomLayout2.addWidget(self.peopleLabel2)
        self.layout2.addLayout(self.bottomLayout2)
        self.monitorsLayout1.addWidget(self.monitor2)
        self.mainLayout.addLayout(self.monitorsLayout1)
        self.monitorsLayout2 = QtWidgets.QHBoxLayout()
        self.monitorsLayout2.setObjectName("monitorsLayout2")
        self.monitor3 = QtWidgets.QFrame(PeopleDetectionPage)
        self.monitor3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.monitor3.setObjectName("monitor3")
        self.layout3 = QtWidgets.QVBoxLayout(self.monitor3)
        self.layout3.setObjectName("layout3")
        self.topLayout3 = QtWidgets.QHBoxLayout()
        self.topLayout3.setObjectName("topLayout3")
        self.monitorControl3 = QtWidgets.QComboBox(self.monitor3)
        self.monitorControl3.setObjectName("monitorControl3")
        self.monitorControl3.addItem("")
        self.monitorControl3.addItem("")
        self.monitorControl3.addItem("")
        self.topLayout3.addWidget(self.monitorControl3)
        self.layout3.addLayout(self.topLayout3)
        self.monitorDisplay3 = QtWidgets.QLabel(self.monitor3)
        self.monitorDisplay3.setMinimumSize(QtCore.QSize(640, 400))
        self.monitorDisplay3.setStyleSheet("background-color: black; color: white;")
        self.monitorDisplay3.setAlignment(QtCore.Qt.AlignCenter)
        self.monitorDisplay3.setObjectName("monitorDisplay3")
        self.layout3.addWidget(self.monitorDisplay3)
        self.bottomLayout3 = QtWidgets.QHBoxLayout()
        self.bottomLayout3.setObjectName("bottomLayout3")
        self.cameraCombo3 = QtWidgets.QComboBox(self.monitor3)
        self.cameraCombo3.setObjectName("cameraCombo3")
        self.bottomLayout3.addWidget(self.cameraCombo3)
        self.peopleLabel3 = QtWidgets.QLabel(self.monitor3)
        self.peopleLabel3.setObjectName("peopleLabel3")
        self.bottomLayout3.addWidget(self.peopleLabel3)
        self.layout3.addLayout(self.bottomLayout3)
        self.monitorsLayout2.addWidget(self.monitor3)
        self.monitor4 = QtWidgets.QFrame(PeopleDetectionPage)
        self.monitor4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.monitor4.setObjectName("monitor4")
        self.layout4 = QtWidgets.QVBoxLayout(self.monitor4)
        self.layout4.setObjectName("layout4")
        self.topLayout4 = QtWidgets.QHBoxLayout()
        self.topLayout4.setObjectName("topLayout4")
        self.monitorControl4 = QtWidgets.QComboBox(self.monitor4)
        self.monitorControl4.setObjectName("monitorControl4")
        self.monitorControl4.addItem("")
        self.monitorControl4.addItem("")
        self.monitorControl4.addItem("")
        self.topLayout4.addWidget(self.monitorControl4)
        self.layout4.addLayout(self.topLayout4)
        self.monitorDisplay4 = QtWidgets.QLabel(self.monitor4)
        self.monitorDisplay4.setMinimumSize(QtCore.QSize(640, 400))
        self.monitorDisplay4.setStyleSheet("background-color: black; color: white;")
        self.monitorDisplay4.setAlignment(QtCore.Qt.AlignCenter)
        self.monitorDisplay4.setObjectName("monitorDisplay4")
        self.layout4.addWidget(self.monitorDisplay4)
        self.bottomLayout4 = QtWidgets.QHBoxLayout()
        self.bottomLayout4.setObjectName("bottomLayout4")
        self.cameraCombo4 = QtWidgets.QComboBox(self.monitor4)
        self.cameraCombo4.setObjectName("cameraCombo4")
        self.bottomLayout4.addWidget(self.cameraCombo4)
        self.peopleLabel4 = QtWidgets.QLabel(self.monitor4)
        self.peopleLabel4.setObjectName("peopleLabel4")
        self.bottomLayout4.addWidget(self.peopleLabel4)
        self.layout4.addLayout(self.bottomLayout4)
        self.monitorsLayout2.addWidget(self.monitor4)
        self.mainLayout.addLayout(self.monitorsLayout2)

        self.retranslateUi(PeopleDetectionPage)
        QtCore.QMetaObject.connectSlotsByName(PeopleDetectionPage)

    def retranslateUi(self, PeopleDetectionPage):
        _translate = QtCore.QCoreApplication.translate
        PeopleDetectionPage.setWindowTitle(_translate("PeopleDetectionPage", "People Detection Page"))
        self.monitorControl1.setItemText(0, _translate("PeopleDetectionPage", "关闭检测"))
        self.monitorControl1.setItemText(1, _translate("PeopleDetectionPage", "开始检测"))
        self.monitorControl1.setItemText(2, _translate("PeopleDetectionPage", "检测违规"))
        self.peopleLabel1.setText(_translate("PeopleDetectionPage", "人流量：0"))
        self.monitorControl2.setItemText(0, _translate("PeopleDetectionPage", "关闭检测"))
        self.monitorControl2.setItemText(1, _translate("PeopleDetectionPage", "开始检测"))
        self.monitorControl2.setItemText(2, _translate("PeopleDetectionPage", "检测违规"))
        self.peopleLabel2.setText(_translate("PeopleDetectionPage", "人流量：0"))
        self.monitorControl3.setItemText(0, _translate("PeopleDetectionPage", "关闭检测"))
        self.monitorControl3.setItemText(1, _translate("PeopleDetectionPage", "开始检测"))
        self.monitorControl3.setItemText(2, _translate("PeopleDetectionPage", "检测违规"))
        self.peopleLabel3.setText(_translate("PeopleDetectionPage", "人流量：0"))
        self.monitorControl4.setItemText(0, _translate("PeopleDetectionPage", "关闭检测"))
        self.monitorControl4.setItemText(1, _translate("PeopleDetectionPage", "开始检测"))
        self.monitorControl4.setItemText(2, _translate("PeopleDetectionPage", "检测违规"))
        self.peopleLabel4.setText(_translate("PeopleDetectionPage", "人流量：0"))
