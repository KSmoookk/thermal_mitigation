# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Thermister Tool_v1QhzLAx.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
#tsetesttestt 2test
from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QRect, Qt)
from PySide6.QtGui import (QCursor, QIntValidator, QAction)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton,QStatusBar, QWidget, QMessageBox, QMenu, QMenuBar, QFileDialog)
from datetime import datetime
import os, serial.tools.list_ports, src



class Ui_MainWindow(QMainWindow, QObject):
    
    def __init__(self):
        super().__init__()
        
        self.data = src.data_signal()
        self.data.setlpm_changed.connect(self.terminal_append)
        self.data.gettmu_changed.connect(self.tmu_terminal_append)
        
        
        self.temp_dict={}
        self.level_cause_demical={}
        self.setupUi(self)

        self.cmd_dict = {}
        
#===================================================================================================================================================
#===================================================================================================================================================
  
    def setupUi(self, MainWindow: QMainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(682, 650)
        MainWindow.setStyleSheet(u"background-color:rgb(86, 86, 86)")

        #================================Menu bar config===========================================
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menubar.setStyleSheet("background-color: gray")

        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        
        self.Create_log_file = QAction(MainWindow)
        self.Create_log_file.setObjectName(u"Create_log_file")
        self.Create_log_file.triggered.connect(self.create_log)
        
        self.Open_log_file = QAction(MainWindow)
        self.Open_log_file.setObjectName(u"Create_log_file")
        self.Open_log_file.triggered.connect(self.open_log)
        
        self.Save_log_file = QAction(MainWindow)
        self.Save_log_file.setObjectName(u"Save_log_file")
        self.Save_log_file.triggered.connect(self.save_log)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.Create_log_file)
        self.menu.addAction(self.Open_log_file)
        self.menu.addAction(self.Save_log_file)
        
        #==========================================================================================
        
        self.status = QLineEdit(self.centralwidget)
        self.status.setGeometry(QRect(530, 0, 141, 30))
        self.status.setStyleSheet(u"color: black; background-color:rgb(86, 86, 86); border: 0px")
        self.status.setReadOnly(True)

        
        self.GetTMU_Terminal = QPlainTextEdit(self.centralwidget)
        self.GetTMU_Terminal.setObjectName("GetTMU_Terminal")
        self.GetTMU_Terminal.setGeometry(QRect(342, 110, 332, 500))
        self.GetTMU_Terminal.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.GetTMU_Terminal.setStyleSheet('QPlainTextEdit#GetTMU_Terminal {background-color : black; color : white}')
        self.GetTMU_Terminal.setReadOnly(True)

        self.MCG_SCG = QGroupBox(self.centralwidget)
        self.MCG_SCG.setObjectName(u"MCG_SCG")
        self.MCG_SCG.setGeometry(QRect(170, 10, 93, 91))
        self.MCG_SCG.setStyleSheet(u"color: rgb(255, 255, 255);")
        
        self.MCG = QCheckBox(self.MCG_SCG)
        self.MCG.setObjectName(u"MCG")
        self.MCG.setGeometry(QRect(10, 20, 71, 20))
        self.MCG.stateChanged.connect(self.checkBoxState_mcgscg)
        
        self.SCG = QCheckBox(self.MCG_SCG)
        self.SCG.setObjectName(u"SCG")
        self.SCG.setGeometry(QRect(10, 50, 71, 20))
        self.SCG.stateChanged.connect(self.checkBoxState_mcgscg)
        
        
        self.TempCtrl_Group = QGroupBox(self.centralwidget)
        self.TempCtrl_Group.setObjectName(u"TempCtrl")
        self.TempCtrl_Group.setGeometry(QRect(280, 10, 93, 91))
        self.TempCtrl_Group.setStyleSheet(u"color: rgb(255, 255, 255);")
        
        self.disable = QCheckBox(self.TempCtrl_Group)
        self.disable.setObjectName(u"disable")
        self.disable.setGeometry(QRect(10, 20, 71, 20))
        self.disable.stateChanged.connect(self.checkBoxState_tempctrl)
        
        self.enable = QCheckBox(self.TempCtrl_Group)
        self.enable.setObjectName(u"enable")
        self.enable.setGeometry(QRect(10, 50, 71, 20))
        self.enable.stateChanged.connect(self.checkBoxState_tempctrl)
        
        
        self.Cause_Group = QGroupBox(self.centralwidget)
        self.Cause_Group.setObjectName(u"Cause_Group")
        self.Cause_Group.setGeometry(QRect(390, 10, 131, 91))
        self.Cause_Group.setStyleSheet(u"color: rgb(255, 255, 255);")
        
        self.cool_control = QComboBox(self.Cause_Group)
        self.cool_control.addItem("")
        self.cool_control.addItem("")
        self.cool_control.addItem("")
        self.cool_control.addItem("")
        self.cool_control.addItem("")
        self.cool_control.addItem("")
        self.cool_control.setObjectName(u"cool_control")
        self.cool_control.setGeometry(QRect(10, 20, 111, 22))
        self.cool_control.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""")
        self.cool_control.currentIndexChanged.connect(self.currentindex_cooling)
        
        self.pwr_control = QComboBox(self.Cause_Group)
        self.pwr_control.addItem("")
        self.pwr_control.addItem("")
        self.pwr_control.addItem("")
        self.pwr_control.addItem("")
        self.pwr_control.addItem("")
        self.pwr_control.addItem("")
        self.pwr_control.setObjectName(u"pwr_control")
        self.pwr_control.setGeometry(QRect(10, 60, 111, 22))
        self.pwr_control.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);")
        self.pwr_control.currentIndexChanged.connect(self.currentindex_pwrsaving)
        
        if os.name == 'posix':
            self.serial_open()
            
        if os.name == 'nt':
            
            self.ports_select = QComboBox(self.centralwidget)
            ports = serial.tools.list_ports.comports()
            ports.sort()
            avaliable_ports=[]
            
            for p in ports:
                avaliable_ports.append(p.device)
                
                self.avaliable_ports = (avaliable_ports)
            
            for line in range(len(self.avaliable_ports)+1):
                self.ports_select.addItem("")
            
            self.ports_select.setObjectName(u"ports_select")
            self.ports_select.setGeometry(QRect(20, 70, 65, 22))
            self.ports_select.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);")     
            self.ports_select.currentIndexChanged.connect(self.serial_open)
            

        self.Interval = QLineEdit(self.centralwidget)
        self.Interval.setAlignment(Qt.AlignCenter)
        self.Interval.setPlaceholderText('Duration')
        self.Interval.setObjectName(u"Set Interval")
        
        if os.name == 'posix':
            self.Interval.setGeometry(QRect(30, 70, 111, 22))
        
        if os.name == 'nt':
            self.Interval.setGeometry(QRect(90, 70, 61, 22))
        
        self.Interval.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Interval.setValidator(QIntValidator(self))
        

        self.error_msg_box = QMessageBox()
        self.error_msg_box.setWindowTitle("Error Message")
        self.error_msg_box.setIcon(QMessageBox.Information)
        self.error_msg_box.setText("You have to select Command options")
        self.error_msg_box.setStandardButtons(QMessageBox.Cancel)
        self.error_msg_box.setDefaultButton(QMessageBox.Cancel)
        
        self.error_msg_box2 = QMessageBox()
        self.error_msg_box2.setWindowTitle("Error Message")
        self.error_msg_box2.setIcon(QMessageBox.Information)
        self.error_msg_box2.setText("Set Interval")
        self.error_msg_box2.setStandardButtons(QMessageBox.Cancel)
        self.error_msg_box2.setDefaultButton(QMessageBox.Cancel)
        

        self.send_button = QPushButton(self.centralwidget)
        self.send_button.setObjectName(u"Send_button")
        self.send_button.setGeometry(QRect(530, 30, 141, 30))
        self.send_button.setStyleSheet(u"background-color:rgb(181, 181, 181)")
        self.send_button.clicked.connect(self.send_clicked)
        self.send_button.setDisabled(True)
        self.send_button.setStyleSheet(u"color: black; background-color: red")
        
        
        self.TMU_button = QPushButton(self.centralwidget)
        self.TMU_button.setObjectName(u"TMU_button")
        self.TMU_button.setGeometry(QRect(530, 70, 141, 30))
        self.TMU_button.setStyleSheet(u"color: black; background-color:red")
        self.TMU_button.setCheckable(True)
        self.TMU_button.toggled.connect(self.tmu_clicked)

        
        if os.name == 'nt':
            self.TMU_button.setDisabled(True)
            self.TMU_button.setStyleSheet(u"color: black; background-color:red")
        if os.name =='posix':
            self.TMU_button.setStyleSheet(u"color: yellow; background-color: green")

        self.AT_command = QGroupBox(self.centralwidget)
        self.AT_command.setObjectName(u"AT_command")
        self.AT_command.setGeometry(QRect(20, 10, 131, 51))
        self.AT_command.setStyleSheet(u"color: rgb(255, 255, 255);")
        
        self.AT_select = QComboBox(self.AT_command)
        self.AT_select.addItem("")
        self.AT_select.addItem("")
        self.AT_select.setObjectName(u"AT_select")
        self.AT_select.setGeometry(QRect(10, 20, 111, 22))
        self.AT_select.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""")
        self.AT_select.currentIndexChanged.connect(self.command_select)
        self.AT_select.setDisabled(True)
        

        self.TempCtrl_Group.raise_()
        self.MCG_SCG.raise_()
        #self.GetTMU_Terminal.raise_()
        self.GetTMU_Terminal.raise_()
        self.Cause_Group.raise_()
        self.send_button.raise_()
        self.AT_command.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

          
#=======================================Test용 Table 구성하는 layer================================================
        self.level1_layer = QLineEdit(self.centralwidget)
        self.level1_layer.setGeometry(QRect(10, 110, 120, 30))
        self.level1_layer.setStyleSheet(u"color: white; background-color:rgb(86, 86, 86); border: 0px")
        self.level1_layer.setText('Level1 Threshold')
        self.level1_layer.setReadOnly(True)
        self.level1 = QLineEdit(self.centralwidget)     
        self.level1.setGeometry(QRect(10, 150, 60 ,30))
        self.level1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""")
        self.level1_cause = QComboBox(self.centralwidget)
        for self.level1_cause_lemical in range(0,6):
            self.level1_cause.addItem("")
        self.level1_cause.setDisabled(True)
        self.level1_cause.setGeometry(QRect(75, 150, 70,30))
        self.level1_cause.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""")
        self.level1_description = QLineEdit(self.centralwidget)
        self.level1_description.setGeometry(QRect(150, 150, 150,30))
        self.level1_description.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""")
        # self.level1_btn = QPushButton(self.centralwidget)
        # self.level1_btn.setGeometry(QRect(270, 150, 60, 30))
        # self.level1_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""")
        
        
        self.level2_layer = QLineEdit(self.centralwidget)
        self.level2_layer.setGeometry(QRect(10, 190, 120, 30))
        self.level2_layer.setStyleSheet(u"color: white; background-color:rgb(86, 86, 86); border: 0px")
        self.level2_layer.setText('Level2 Threshold')
        self.level2_layer.setReadOnly(True)
        self.level2 = QLineEdit(self.centralwidget)      
        self.level2.setGeometry(QRect(10, 230, 60,30))
        self.level2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""")
        self.level2_cause = QComboBox(self.centralwidget)
        for self.level2_cause_line in range(0,6):
            self.level2_cause.addItem("")
        self.level2_cause.setGeometry(QRect(75, 230, 70,30))
        self.level2_cause.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""")
        self.level2_description = QLineEdit(self.centralwidget)
        self.level2_description.setGeometry(QRect(150, 230, 150,30))
        self.level2_description.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""")
        # self.level2_btn = QPushButton(self.centralwidget)
        # self.level2_btn.setGeometry(QRect(270, 240, 60, 30))
        # self.level2_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""")
        
        self.level3_layer = QLineEdit(self.centralwidget)
        self.level3_layer.setGeometry(QRect(10, 270, 120, 30))
        self.level3_layer.setStyleSheet(u"color: white; background-color:rgb(86, 86, 86); border: 0px")
        self.level3_layer.setText('Level3 Threshold')
        self.level3_layer.setReadOnly(True)
        self.level3 = QLineEdit(self.centralwidget)
        self.level3.setGeometry(QRect(10, 310, 60,30))
        self.level3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""")
        self.level3_cause = QComboBox(self.centralwidget)
        for self.level3_cause_line in range(0,6):
            self.level3_cause.addItem("")
        self.level3_cause.setGeometry(QRect(75, 310, 70,30))
        self.level3_cause.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""")
        self.level3_description = QLineEdit(self.centralwidget)
        self.level3_description.setGeometry(QRect(150, 310, 150,30))
        self.level3_description.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""")
        # self.level3_btn = QPushButton(self.centralwidget)
        # self.level3_btn.setGeometry(QRect(270, 330, 60, 30))
        # self.level3_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""")
        
        self.level4_layer = QLineEdit(self.centralwidget)
        self.level4_layer.setGeometry(QRect(10, 350, 120, 30))
        self.level4_layer.setStyleSheet(u"color: white; background-color:rgb(86, 86, 86); border: 0px")
        self.level4_layer.setText('Level4 Threshold')
        self.level4_layer.setReadOnly(True)
        self.level4 = QLineEdit(self.centralwidget)
        self.level4.setGeometry(QRect(10, 390, 60,30))
        self.level4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""")
        self.level4_cause = QComboBox(self.centralwidget)
        for self.level4_cause_line in range(0,6):
            self.level4_cause.addItem("")
        self.level4_cause.setGeometry(QRect(75, 390, 70,30))
        self.level4_cause.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""")
        self.level4_description = QLineEdit(self.centralwidget)
        self.level4_description.setGeometry(QRect(150, 390, 150,30))
        self.level4_description.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""")
        # self.level4_btn = QPushButton(self.centralwidget)
        # self.level4_btn.setGeometry(QRect(270, 420, 60, 30))
        # self.level4_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""")
        
        self.level5_layer = QLineEdit(self.centralwidget)
        self.level5_layer.setGeometry(QRect(10, 430, 120, 30))
        self.level5_layer.setStyleSheet(u"color: white; background-color:rgb(86, 86, 86); border: 0px")
        self.level5_layer.setText('Level5 Threshold')
        self.level5_layer.setReadOnly(True)
        self.level5 = QLineEdit(self.centralwidget)
        self.level5.setGeometry(QRect(10, 470, 60,30))
        self.level5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""")
        self.level5_cause = QComboBox(self.centralwidget)
        self.level5_cause.setDisabled(True)
        for self.level5_cause_line in range(0,6):
            self.level5_cause.addItem("")
        self.level5_cause.setGeometry(QRect(75, 470, 70,30))
        self.level5_cause.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""")
        self.level5_description = QLineEdit(self.centralwidget)
        self.level5_description.setGeometry(QRect(150, 470, 150,30))
        self.level5_description.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""")
        # self.level5_btn = QPushButton(self.centralwidget)
        # self.level5_btn.setGeometry(QRect(270, 510, 60, 30))
        # self.level5_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);\n""")
        
        self.level_table_apply = QPushButton(self.centralwidget)
        self.level_table_apply.setGeometry(QRect(10, 510, 290, 30))
        self.level_table_apply.setStyleSheet(u"background-color: green;\n""color: rgb(0, 0, 0);\n""")
        self.level_table_apply.clicked.connect(self.TPL)
    
#==============================================================================================================================
        
    # setupUi
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Thermal Mitigation Tool v1.0", None))
        
        ###Top 레이아웃 버튼
        self.MCG_SCG.setTitle(QCoreApplication.translate("MainWindow", u"MCG_SCG", None))
        self.MCG.setText(QCoreApplication.translate("MainWindow", u"MCG(0)", None))
        self.SCG.setText(QCoreApplication.translate("MainWindow", u"SCG(1)", None))
        self.TempCtrl_Group.setTitle(QCoreApplication.translate("MainWindow", u"TempCtrl", None))
        self.disable.setText(QCoreApplication.translate("MainWindow", u"Disable(0)", None))
        self.enable.setText(QCoreApplication.translate("MainWindow", u"Enable(1)", None))
        self.Cause_Group.setTitle(QCoreApplication.translate("MainWindow", u"Cause_Group", None))
        self.cool_control.setItemText(0, QCoreApplication.translate("MainWindow", u"--\ubc1c\uc5f4\uc81c\uc5b4--", None))
        self.cool_control.setItemText(1, QCoreApplication.translate("MainWindow", u"0x100", None))
        self.cool_control.setItemText(2, QCoreApplication.translate("MainWindow", u"0x80", None))
        self.cool_control.setItemText(3, QCoreApplication.translate("MainWindow", u"0x01", None))
        self.cool_control.setItemText(4, QCoreApplication.translate("MainWindow", u"0x36", None))
        self.cool_control.setItemText(5, QCoreApplication.translate("MainWindow", u"0x00", None))

        if os.name == 'nt':
            self.ports_select.setItemText(0, QCoreApplication.translate("MainWindow", u"Port", None))
            for line in range(len(self.avaliable_ports)):
                self.ports_select.setItemText(line+1, QCoreApplication.translate("mainWindow", u"%s" %self.avaliable_ports[line], None))
        
                self.pwr_control.setItemText(0, QCoreApplication.translate("MainWindow", u"--Pwr Saving--", None))
                
        self.pwr_control.setItemText(1, QCoreApplication.translate("MainWindow", u"0x02", None))
        self.pwr_control.setItemText(2, QCoreApplication.translate("MainWindow", u"0x04", None))
        self.pwr_control.setItemText(3, QCoreApplication.translate("MainWindow", u"0x08", None))
        self.pwr_control.setItemText(4, QCoreApplication.translate("MainWindow", u"0x10", None))
        self.pwr_control.setItemText(5, QCoreApplication.translate("MainWindow", u"0x20", None))

        self.send_button.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        # self.level1_btn.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        # self.level2_btn.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        # self.level3_btn.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        # self.level4_btn.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        # self.level5_btn.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.level_table_apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        
        self.TMU_button.setText(QCoreApplication.translate("MainWindow", u"TMU Read", None))
        self.AT_command.setTitle(QCoreApplication.translate("MainWindow", u"AT Command", None))
        self.AT_select.setItemText(0, QCoreApplication.translate("MainWindow", u"----AT Select----", None))
        self.AT_select.setItemText(1, QCoreApplication.translate("MainWindow", u"AT+SETLPM=", None))
        
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.Create_log_file.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.Open_log_file.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.Save_log_file.setText(QCoreApplication.translate("Mainwindow", u'Save', None))
        
        self.level1_cause.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        # self.level1_cause.setItemText(1, QCoreApplication.translate("MainWindow", u"0", None))
        # self.level1_cause.setItemText(2, QCoreApplication.translate("MainWindow", u"1", None))
        # self.level1_cause.setItemText(3, QCoreApplication.translate("MainWindow", u"64", None))
        # self.level1_cause.setItemText(4, QCoreApplication.translate("MainWindow", u"128", None))
        # self.level1_cause.setItemText(5, QCoreApplication.translate("MainWindow", u"256", None))
        self.level2_cause.setItemText(0, QCoreApplication.translate("MainWindow", u"Cause", None))
        self.level2_cause.setItemText(1, QCoreApplication.translate("MainWindow", u"0", None))
        self.level2_cause.setItemText(2, QCoreApplication.translate("MainWindow", u"1", None))
        self.level2_cause.setItemText(3, QCoreApplication.translate("MainWindow", u"64", None))
        self.level2_cause.setItemText(4, QCoreApplication.translate("MainWindow", u"128", None))
        self.level2_cause.setItemText(5, QCoreApplication.translate("MainWindow", u"256", None))
        self.level3_cause.setItemText(0, QCoreApplication.translate("MainWindow", u"Cause", None))
        self.level3_cause.setItemText(1, QCoreApplication.translate("MainWindow", u"0", None))
        self.level3_cause.setItemText(2, QCoreApplication.translate("MainWindow", u"1", None))
        self.level3_cause.setItemText(3, QCoreApplication.translate("MainWindow", u"64", None))
        self.level3_cause.setItemText(4, QCoreApplication.translate("MainWindow", u"128", None))
        self.level3_cause.setItemText(5, QCoreApplication.translate("MainWindow", u"256", None))
        self.level4_cause.setItemText(0, QCoreApplication.translate("MainWindow", u"Cause", None))
        self.level4_cause.setItemText(1, QCoreApplication.translate("MainWindow", u"0", None))
        self.level4_cause.setItemText(2, QCoreApplication.translate("MainWindow", u"1", None))
        self.level4_cause.setItemText(3, QCoreApplication.translate("MainWindow", u"64", None))
        self.level4_cause.setItemText(4, QCoreApplication.translate("MainWindow", u"128", None))
        self.level4_cause.setItemText(5, QCoreApplication.translate("MainWindow", u"256", None))
        self.level5_cause.setItemText(0, QCoreApplication.translate("MainWindow", u"Reboot", None))
        # self.level5_cause.setItemText(1, QCoreApplication.translate("MainWindow", u"0", None))
        # self.level5_cause.setItemText(2, QCoreApplication.translate("MainWindow", u"1", None))
        # self.level5_cause.setItemText(3, QCoreApplication.translate("MainWindow", u"64", None))
        # self.level5_cause.setItemText(4, QCoreApplication.translate("MainWindow", u"128", None))
        # self.level5_cause.setItemText(5, QCoreApplication.translate("MainWindow", u"256", None))
        

        
 
   
    # retranslateUi
#===================================================================================================================================================   
#===================================================================================================================================================   

        
    def command_select(self):
        
        if self.AT_select.currentIndex() == 0:
            self.send_button.setDisabled(True)
            self.send_button.setStyleSheet(u"color: black; background-color: red")

        elif self.AT_select.currentIndex() == 1:
            self.send_button.setEnabled(True)
            self.send_button.setStyleSheet(u"color: yellow; background-color:green")
            self.cmd_dict[0] = "AT+SETLPM="
        
        
    def checkBoxState_mcgscg(self):
        if self.MCG.isChecked() == True:                ####SCG 관련 
            self.SCG.setDisabled(True)
            self.cmd_dict[1] = 0
        
        elif self.MCG.isChecked() == False:
            self.SCG.setEnabled(True)
            
        if self.SCG.isChecked() == True:                ####SCG 관련 
            self.MCG.setDisabled(True)
            self.cmd_dict[1] = 1
        
        elif self.SCG.isChecked() == False:
            self.MCG.setEnabled(True)
            
        if self.MCG.isChecked() == False and self.SCG.isChecked() == False:
            self.cmd_dict[1] = None

        
    def checkBoxState_tempctrl(self):
        
        if self.disable.isChecked() == True:                    ####TempCtrl Enable 관련 
            self.enable.setDisabled(True)
            self.cmd_dict[2] = 0
            
        elif self.disable.isChecked() == False:
            self.enable.setEnabled(True)    
            
            
        if self.enable.isChecked() == True:                     ####TempCtrl Disable 관련 
            self.disable.setDisabled(True)
            self.cmd_dict[2] = 1
            
        elif self.enable.isChecked() == False:
            self.disable.setEnabled(True)
        
        
        if self.disable.isChecked() == False and self.enable.isChecked() == False:
            self.cmd_dict[2] = None

        
    def currentindex_cooling(self):
        
        self.pwr_control.setDisabled(True)
        
        cool_control_len = (self.cool_control.count())
        cool_demical = [256,128,1,64,0]
        cool_current_index = self.cool_control.currentIndex()
        
        for i in range(0, cool_control_len):
            if  cool_current_index == 0:
                self.pwr_control.setDisabled(False)
                self.cmd_dict[3] = None
                break
            elif cool_current_index == i:
                self.cmd_dict[3] = cool_demical[i-1]
                break
            else:
                i += 1

        

    def currentindex_pwrsaving(self):
        
        self.cool_control.setDisabled(True)
                   
        pwr_control_len = (self.pwr_control.count())
        pwr_demical = [2,4,8,16,32]
        pwr_current_index = self.pwr_control.currentIndex()
        
        for i in range(0, pwr_control_len):
            
            if  pwr_current_index == 0:
                self.cool_control.setDisabled(False)
                self.cmd_dict[3] = None
                break
            
            elif pwr_current_index == i:
                self.cmd_dict[3] = pwr_demical[i-1]
                break
            
            else:
                i += 1
  
        
    def send_clicked(self):
        
        try:
            self.setlpm= "%s%d,%d,%d\r"%(self.cmd_dict[0],self.cmd_dict[1],
                                            self.cmd_dict[2],self.cmd_dict[3])
            self.ser.write(self.setlpm.encode())
            
        except:
            self.error_msg_box.exec()


            
    def tmu_clicked(self, state):
        
        self.state = state
        
        try:
            #print('hi')
            self.interval_value = self.Interval.text()
            #print(self.interval_value)
            self.interval_value = int(self.interval_value)
            self.Interval.setReadOnly(True)
            #print('hi')
            self.start_thread()

        except:
            self.error_msg_box2.exec()
            self.TMU_button.setChecked(False)

   
                
    def start_thread(self):
        
        self.TMU_button.setText({True: "Stop Read", False: "TMU Read"}[self.state])
        self.TMU_button.setStyleSheet("color: %s; background-color: %s;" %({True:"blue",False:"yellow"}[self.state] ,{True: "yellow", False:"green"}[self.state]))
        

        
        if self.state == True:

            self.AT_select.setEnabled(True)
            print('hi')
            self._thread = src.Process(self.ser, self.data, self.interval_value, self.thermal_policy_table_upstream, self.thermal_policy_table_downstream)
            self._thread.start()

            if os.name == 'nt':
                self.ports_select.setDisabled(True) 
            
            
            
        elif self.state == False:
            
            self._thread.stop_thread = True
            #self.ser.close()
            try:
                if self.fname[0] != None:

                    self.status.setText('Pause Logging...')
            except:
                self.status.setText('Stop')

            if os.name == 'nt':
                self.ports_select.setEnabled(True)
                
            self.MCG.setChecked(False)
            self.SCG.setChecked(False)
            self.disable.setChecked(False)
            self.enable.setChecked(False)
            self.AT_select.setCurrentIndex(0)
            self.cool_control.setCurrentIndex(0)
            self.pwr_control.setCurrentIndex(0)
            self.AT_select.setDisabled(True)
            self.Interval.setReadOnly(False)
            
            
    
    def terminal_append(self, data):
        
        self.terminal_append_data = data
        self.GetTMU_Terminal.appendPlainText(self.terminal_append_data)
        
        try: 
            if self.fname[0] != None:
                
                self.f.write('%s\n' %self.terminal_append_data)

        except:
            pass
        
        
    def tmu_terminal_append(self, data: list):
        
        self.tmu_terminal_append_data = ''.join(data)
        self.GetTMU_Terminal.appendPlainText(self.tmu_terminal_append_data)
        
        try:
            if self.fname[0] != None:
                
                self.f.write('%s\n' %self.tmu_terminal_append_data)
                self.status.setText('logging...')
        except:
            self.status.setText('Without log...')
            pass
                   

    def create_log(self):
        
        nowtime = datetime.now()
        nowtime = nowtime.strftime("%Y.%m.%d_%H-%M")
        
        if os.name == 'posix':
            self.fname = QFileDialog.getSaveFileName(self, 'New File','./log/{}_Thermal_Log.txt'.format(nowtime), 'txt File(*.txt)')
            
        if os.name == 'nt':
            self.fname = QFileDialog.getSaveFileName(self, 'New File','./log/{}_Thermal_Log.txt'.format(nowtime), 'txt File(*.txt)')
        
        if self.fname[0]:
            
            self.f = open(self.fname[0], 'a')
            
    def open_log(self):
        
        if os.name == 'posix':
            self.fname = QFileDialog.getOpenFileName(self, 'Open File', './log', 'txt File(*.txt)')
            
        if os.name == 'nt':
            self.fname = QFileDialog.getOpenFileName(self, 'Open File', './log','txt File(*.txt)')
        
        if self.fname[0]:
            
            self.f = open(self.fname[0], 'a')
        

    def save_log(self):
        
        self.f.close()
        self.fname = ''
        self.status.setText('Save Complete')
            

        

            
    def serial_open(self):

        if os.name == 'posix':
            self.ser = serial.Serial('/dev/ttyMD_cp0',115200, timeout=1)
            
        if os.name == 'nt':
            
            if self.ports_select.currentIndex() == 0:
                self.TMU_button.setDisabled(True)
                self.TMU_button.setStyleSheet(u"color: black; background-color:red")
                self.ser.close()
            
            else:
                serial_len = self.ports_select.count()
                self.TMU_button.setEnabled(True)
                self.TMU_button.setStyleSheet(u"color: yellow; background-color: green")
                
                for i in range(serial_len):
                    if self.ports_select.currentIndex() == i:
                        
                        print('%s' %self.avaliable_ports[i-1])
                        self.com = self.avaliable_ports[i-1]
                        
                self.ser = serial.Serial(self.com,115200, timeout=1)
                
    def level_cause_index(self):
        
        if self.level1_cause.currentIndex() == 0:
            self.level_cause_demical[0] = 0
        elif self.level1_cause.currentIndex() !=0:
            level1_cause = self.level1_cause.currentText()
            self.level_cause_demical[0] = level1_cause
            
        if self.level2_cause.currentIndex() == 0:
            self.level_cause_demical[1] = 0
        elif self.level2_cause.currentIndex() !=0:
            level2_cause = self.level2_cause.currentText()
            self.level_cause_demical[1] = level2_cause
            
        if self.level3_cause.currentIndex() == 0:
            self.level_cause_demical[2] = 0
        elif self.level3_cause.currentIndex() !=0:
            level3_cause = self.level3_cause.currentText()
            self.level_cause_demical[2] = level3_cause
            
        if self.level4_cause.currentIndex() == 0:
            self.level_cause_demical[3] = 0
        elif self.level4_cause.currentIndex() !=0:
            level4_cause = self.level4_cause.currentText()
            self.level_cause_demical[3] = level4_cause
            
        if self.level5_cause.currentIndex() == 0:
            self.level_cause_demical[4] = 0
        elif self.level5_cause.currentIndex() !=0:
            level5_cause = self.level5_cause.currentText()
            self.level_cause_demical[4] = level5_cause
        
            
        
        
    def TPL(self):
        
        self.temp_dict[0] = self.level1.text()
        self.temp_dict[1] = self.level2.text()
        self.temp_dict[2] = self.level3.text()
        self.temp_dict[3] = self.level4.text()
        self.temp_dict[4] = self.level5.text()
        self.level_cause_index()
        
        self.thermal_table_upstream(self.temp_dict, self.level_cause_demical)
        self.thermal_table_downstream(self.temp_dict, self.level_cause_demical)
        
               
                

    def thermal_table_upstream(self, temp_dict, level_cause_demical):
        self.thermal_policy_table_upstream = {
            
            #level 온도까지                          #command적용
            '{}'.format(temp_dict[0])           :'AT+SETLPM=0,0,0',                                    #level1
            '{}'.format(temp_dict[1])           :'AT+SETLPM=0,1,{}'.format(level_cause_demical[1]),    #level2
            '{}'.format(temp_dict[2])           :'AT+SETLPM=0,1,{}'.format(level_cause_demical[2]),    #level3
            '{}'.format(temp_dict[3])           :'AT+SETLPM=0,1,{}'.format(level_cause_demical[3]),    #level4
            '{}'.format(temp_dict[4])           :'reboot'                                              #level5
            
        }
    
    def thermal_table_downstream(self, temp_dict, level_cause_demical):
        self.thermal_policy_table_downstream = {
            
            #level 온도까지                          #command적용
            '{}'.format(int(temp_dict[0])-2)           :'AT+SETLPM=0,0,0',                                    #level1
            '{}'.format(int(temp_dict[1])-3)           :'AT+SETLPM=0,1,{}'.format(level_cause_demical[1]),    #level2
            '{}'.format(int(temp_dict[2])-2)           :'AT+SETLPM=0,1,{}'.format(level_cause_demical[2]),    #level3
            '{}'.format(int(temp_dict[3])-3)           :'AT+SETLPM=0,1,{}'.format(level_cause_demical[3]),    #level4
            '{}'.format(int(temp_dict[4]))           :'reboot'                                                #level5
            
        }
        #print(self.temp_dict)
    
                

if __name__ == "__main__":  
    app = QApplication()
    window = Ui_MainWindow()
    window.show()
    app.exec()
        
