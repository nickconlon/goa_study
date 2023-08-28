# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface/ros_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1004, 521)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.run_goa = QtWidgets.QPushButton(self.centralwidget)
        self.run_goa.setGeometry(QtCore.QRect(590, 260, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.run_goa.setFont(font)
        self.run_goa.setObjectName("run_goa")
        self.stop_robot_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_robot_button.setGeometry(QtCore.QRect(110, 260, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.stop_robot_button.setFont(font)
        self.stop_robot_button.setObjectName("stop_robot_button")
        self.start_robot_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_robot_button.setGeometry(QtCore.QRect(20, 260, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.start_robot_button.setFont(font)
        self.start_robot_button.setObjectName("start_robot_button")
        self.go_home_button = QtWidgets.QPushButton(self.centralwidget)
        self.go_home_button.setGeometry(QtCore.QRect(20, 360, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.go_home_button.setFont(font)
        self.go_home_button.setObjectName("go_home_button")
        self.goa_display = QtWidgets.QLabel(self.centralwidget)
        self.goa_display.setGeometry(QtCore.QRect(790, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.goa_display.setFont(font)
        self.goa_display.setFrameShape(QtWidgets.QFrame.Box)
        self.goa_display.setText("")
        self.goa_display.setAlignment(QtCore.Qt.AlignCenter)
        self.goa_display.setObjectName("goa_display")
        self.et_display = QtWidgets.QLabel(self.centralwidget)
        self.et_display.setGeometry(QtCore.QRect(790, 80, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.et_display.setFont(font)
        self.et_display.setFrameShape(QtWidgets.QFrame.Box)
        self.et_display.setText("")
        self.et_display.setAlignment(QtCore.Qt.AlignCenter)
        self.et_display.setObjectName("et_display")
        self.state_display = QtWidgets.QLabel(self.centralwidget)
        self.state_display.setGeometry(QtCore.QRect(20, 40, 241, 111))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.state_display.setFont(font)
        self.state_display.setFrameShape(QtWidgets.QFrame.Box)
        self.state_display.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.state_display.setObjectName("state_display")
        self.write_data_button = QtWidgets.QPushButton(self.centralwidget)
        self.write_data_button.setGeometry(QtCore.QRect(380, 440, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.write_data_button.setFont(font)
        self.write_data_button.setObjectName("write_data_button")
        self.update_goa_value = QtWidgets.QLineEdit(self.centralwidget)
        self.update_goa_value.setGeometry(QtCore.QRect(840, 220, 51, 31))
        self.update_goa_value.setAlignment(QtCore.Qt.AlignCenter)
        self.update_goa_value.setObjectName("update_goa_value")
        self.mq_label = QtWidgets.QLabel(self.centralwidget)
        self.mq_label.setGeometry(QtCore.QRect(590, 80, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.mq_label.setFont(font)
        self.mq_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.mq_label.setObjectName("mq_label")
        self.update_goa = QtWidgets.QPushButton(self.centralwidget)
        self.update_goa.setGeometry(QtCore.QRect(590, 220, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.update_goa.setFont(font)
        self.update_goa.setObjectName("update_goa")
        self.end_sim = QtWidgets.QPushButton(self.centralwidget)
        self.end_sim.setGeometry(QtCore.QRect(20, 440, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.end_sim.setFont(font)
        self.end_sim.setObjectName("end_sim")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 10, 291, 291))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("interface/basemap.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.position_display = QtWidgets.QLabel(self.centralwidget)
        self.position_display.setGeometry(QtCore.QRect(120, 40, 141, 21))
        self.position_display.setObjectName("position_display")
        self.orientation_display = QtWidgets.QLabel(self.centralwidget)
        self.orientation_display.setGeometry(QtCore.QRect(120, 70, 141, 21))
        self.orientation_display.setObjectName("orientation_display")
        self.next_waypoint_display = QtWidgets.QLabel(self.centralwidget)
        self.next_waypoint_display.setGeometry(QtCore.QRect(120, 100, 141, 21))
        self.next_waypoint_display.setObjectName("next_waypoint_display")
        self.time_display = QtWidgets.QLabel(self.centralwidget)
        self.time_display.setGeometry(QtCore.QRect(120, 130, 101, 21))
        self.time_display.setObjectName("time_display")
        self.goal_x_value = QtWidgets.QLineEdit(self.centralwidget)
        self.goal_x_value.setGeometry(QtCore.QRect(190, 180, 31, 31))
        self.goal_x_value.setObjectName("goal_x_value")
        self.goal_y_value = QtWidgets.QLineEdit(self.centralwidget)
        self.goal_y_value.setGeometry(QtCore.QRect(230, 180, 31, 31))
        self.goal_y_value.setObjectName("goal_y_value")
        self.goal_x_label = QtWidgets.QLabel(self.centralwidget)
        self.goal_x_label.setGeometry(QtCore.QRect(190, 150, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.goal_x_label.setFont(font)
        self.goal_x_label.setAlignment(QtCore.Qt.AlignCenter)
        self.goal_x_label.setObjectName("goal_x_label")
        self.goal_y_label = QtWidgets.QLabel(self.centralwidget)
        self.goal_y_label.setGeometry(QtCore.QRect(230, 150, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.goal_y_label.setFont(font)
        self.goal_y_label.setAlignment(QtCore.Qt.AlignCenter)
        self.goal_y_label.setObjectName("goal_y_label")
        self.update_goal_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_goal_button.setGeometry(QtCore.QRect(20, 180, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.update_goal_button.setFont(font)
        self.update_goal_button.setObjectName("update_goal_button")
        self.generate_plan_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_plan_button.setGeometry(QtCore.QRect(20, 220, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.generate_plan_button.setFont(font)
        self.generate_plan_button.setObjectName("generate_plan_button")
        self.sq_label = QtWidgets.QLabel(self.centralwidget)
        self.sq_label.setGeometry(QtCore.QRect(590, 120, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.sq_label.setFont(font)
        self.sq_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.sq_label.setObjectName("sq_label")
        self.sq_display = QtWidgets.QLabel(self.centralwidget)
        self.sq_display.setGeometry(QtCore.QRect(790, 120, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sq_display.setFont(font)
        self.sq_display.setFrameShape(QtWidgets.QFrame.Box)
        self.sq_display.setText("")
        self.sq_display.setAlignment(QtCore.Qt.AlignCenter)
        self.sq_display.setObjectName("sq_display")
        self.exp_label = QtWidgets.QLabel(self.centralwidget)
        self.exp_label.setGeometry(QtCore.QRect(590, 160, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.exp_label.setFont(font)
        self.exp_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.exp_label.setObjectName("exp_label")
        self.exp_display = QtWidgets.QLabel(self.centralwidget)
        self.exp_display.setGeometry(QtCore.QRect(790, 160, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.exp_display.setFont(font)
        self.exp_display.setFrameShape(QtWidgets.QFrame.Box)
        self.exp_display.setText("")
        self.exp_display.setAlignment(QtCore.Qt.AlignCenter)
        self.exp_display.setObjectName("exp_display")
        self.confidence_panel_label = QtWidgets.QLabel(self.centralwidget)
        self.confidence_panel_label.setGeometry(QtCore.QRect(580, 10, 411, 291))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.confidence_panel_label.setFont(font)
        self.confidence_panel_label.setFrameShape(QtWidgets.QFrame.Box)
        self.confidence_panel_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.confidence_panel_label.setObjectName("confidence_panel_label")
        self.confidence_panel_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.confidence_panel_label_2.setGeometry(QtCore.QRect(10, 10, 261, 291))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.confidence_panel_label_2.setFont(font)
        self.confidence_panel_label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.confidence_panel_label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.confidence_panel_label_2.setObjectName("confidence_panel_label_2")
        self.actual_oa_label = QtWidgets.QLabel(self.centralwidget)
        self.actual_oa_label.setGeometry(QtCore.QRect(920, 190, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.actual_oa_label.setFont(font)
        self.actual_oa_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.actual_oa_label.setObjectName("actual_oa_label")
        self.expected_oa_label = QtWidgets.QLabel(self.centralwidget)
        self.expected_oa_label.setGeometry(QtCore.QRect(830, 190, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.expected_oa_label.setFont(font)
        self.expected_oa_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.expected_oa_label.setObjectName("expected_oa_label")
        self.actual_outcome_display = QtWidgets.QLabel(self.centralwidget)
        self.actual_outcome_display.setGeometry(QtCore.QRect(920, 220, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.actual_outcome_display.setFont(font)
        self.actual_outcome_display.setFrameShape(QtWidgets.QFrame.Box)
        self.actual_outcome_display.setText("")
        self.actual_outcome_display.setAlignment(QtCore.Qt.AlignCenter)
        self.actual_outcome_display.setObjectName("actual_outcome_display")
        self.oa_label = QtWidgets.QLabel(self.centralwidget)
        self.oa_label.setGeometry(QtCore.QRect(590, 40, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.oa_label.setFont(font)
        self.oa_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.oa_label.setObjectName("oa_label")
        self.famsec_toggle_button = QtWidgets.QPushButton(self.centralwidget)
        self.famsec_toggle_button.setGeometry(QtCore.QRect(140, 360, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.famsec_toggle_button.setFont(font)
        self.famsec_toggle_button.setObjectName("famsec_toggle_button")
        self.et_goa_toggle_button = QtWidgets.QPushButton(self.centralwidget)
        self.et_goa_toggle_button.setGeometry(QtCore.QRect(260, 360, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.et_goa_toggle_button.setFont(font)
        self.et_goa_toggle_button.setObjectName("et_goa_toggle_button")
        self.test_add_obstacle_button = QtWidgets.QPushButton(self.centralwidget)
        self.test_add_obstacle_button.setGeometry(QtCore.QRect(140, 440, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.test_add_obstacle_button.setFont(font)
        self.test_add_obstacle_button.setObjectName("test_add_obstacle_button")
        self.test_trigger_goa_button = QtWidgets.QPushButton(self.centralwidget)
        self.test_trigger_goa_button.setGeometry(QtCore.QRect(260, 440, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.test_trigger_goa_button.setFont(font)
        self.test_trigger_goa_button.setObjectName("test_trigger_goa_button")
        self.toggle_record_button = QtWidgets.QPushButton(self.centralwidget)
        self.toggle_record_button.setGeometry(QtCore.QRect(380, 360, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.toggle_record_button.setFont(font)
        self.toggle_record_button.setObjectName("toggle_record_button")
        self.teleop_robot_button = QtWidgets.QPushButton(self.centralwidget)
        self.teleop_robot_button.setGeometry(QtCore.QRect(200, 260, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.teleop_robot_button.setFont(font)
        self.teleop_robot_button.setObjectName("teleop_robot_button")
        self.confidence_panel_label_2.raise_()
        self.confidence_panel_label.raise_()
        self.run_goa.raise_()
        self.stop_robot_button.raise_()
        self.start_robot_button.raise_()
        self.go_home_button.raise_()
        self.goa_display.raise_()
        self.et_display.raise_()
        self.state_display.raise_()
        self.write_data_button.raise_()
        self.update_goa_value.raise_()
        self.mq_label.raise_()
        self.update_goa.raise_()
        self.end_sim.raise_()
        self.label.raise_()
        self.position_display.raise_()
        self.orientation_display.raise_()
        self.next_waypoint_display.raise_()
        self.time_display.raise_()
        self.goal_x_value.raise_()
        self.goal_y_value.raise_()
        self.goal_x_label.raise_()
        self.goal_y_label.raise_()
        self.update_goal_button.raise_()
        self.generate_plan_button.raise_()
        self.sq_label.raise_()
        self.sq_display.raise_()
        self.exp_label.raise_()
        self.exp_display.raise_()
        self.actual_oa_label.raise_()
        self.expected_oa_label.raise_()
        self.actual_outcome_display.raise_()
        self.oa_label.raise_()
        self.famsec_toggle_button.raise_()
        self.et_goa_toggle_button.raise_()
        self.test_add_obstacle_button.raise_()
        self.test_trigger_goa_button.raise_()
        self.toggle_record_button.raise_()
        self.teleop_robot_button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1004, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.run_goa.setText(_translate("MainWindow", "Run new Outcome Assessment"))
        self.stop_robot_button.setText(_translate("MainWindow", "Stop"))
        self.start_robot_button.setText(_translate("MainWindow", "Auto"))
        self.go_home_button.setText(_translate("MainWindow", "Go home"))
        self.state_display.setText(_translate("MainWindow", "<html><head/><body><p>Position:</p><p>Orientation:</p><p>Next WP:</p><p>Time:</p></body></html>"))
        self.write_data_button.setText(_translate("MainWindow", "Write data"))
        self.mq_label.setText(_translate("MainWindow", "Model Quality Assessment"))
        self.update_goa.setText(_translate("MainWindow", "Set outcome threshold (sec)"))
        self.end_sim.setText(_translate("MainWindow", "End sim"))
        self.position_display.setText(_translate("MainWindow", "(0.0, 0.0, 0.0)"))
        self.orientation_display.setText(_translate("MainWindow", "(0.0, 0.0, 0.0, 0.0)"))
        self.next_waypoint_display.setText(_translate("MainWindow", "(0.0, 0.0)"))
        self.time_display.setText(_translate("MainWindow", "0.0"))
        self.goal_x_label.setText(_translate("MainWindow", "x"))
        self.goal_y_label.setText(_translate("MainWindow", "y"))
        self.update_goal_button.setText(_translate("MainWindow", "Update goal"))
        self.generate_plan_button.setText(_translate("MainWindow", "Generate plan"))
        self.sq_label.setText(_translate("MainWindow", "Solver Quality Assessment"))
        self.exp_label.setText(_translate("MainWindow", "Experience Assessment"))
        self.confidence_panel_label.setText(_translate("MainWindow", "Robot Self-Confience Assessments"))
        self.confidence_panel_label_2.setText(_translate("MainWindow", "Robot State and Control"))
        self.actual_oa_label.setText(_translate("MainWindow", "Actual"))
        self.expected_oa_label.setText(_translate("MainWindow", "Expected"))
        self.oa_label.setText(_translate("MainWindow", "Outcome Assessment"))
        self.famsec_toggle_button.setText(_translate("MainWindow", "FaMSeC on"))
        self.et_goa_toggle_button.setText(_translate("MainWindow", "Triggering on"))
        self.test_add_obstacle_button.setText(_translate("MainWindow", "Test obstacle"))
        self.test_trigger_goa_button.setText(_translate("MainWindow", "Test Trigger"))
        self.toggle_record_button.setText(_translate("MainWindow", "Record on"))
        self.teleop_robot_button.setText(_translate("MainWindow", "Telop"))
