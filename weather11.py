from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 480)
        MainWindow.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"color:#F0E9D2;\n"
"font: 9pt \"Segoe UI\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.NAMES_WINDOW = QtWidgets.QTextEdit(self.centralwidget)
        self.NAMES_WINDOW.setEnabled(False)
        self.NAMES_WINDOW.setGeometry(QtCore.QRect(20, 10, 201, 101))
        self.NAMES_WINDOW.setStyleSheet("QTextEdit {\n"
"    border: 1px solid white;  /* White border */\n"
"    border-radius: 5px;       /* Rounded corners */\n"
"    padding: 5px;             /* Padding inside the border */\n"
"    color: black;             /* Text color */\n"
"}\n"
"")
        self.NAMES_WINDOW.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.NAMES_WINDOW.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.NAMES_WINDOW.setObjectName("NAMES_WINDOW")
        self.CONTROL_WINDOW = QtWidgets.QWidget(self.centralwidget)
        self.CONTROL_WINDOW.setGeometry(QtCore.QRect(20, 130, 201, 151))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CONTROL_WINDOW.sizePolicy().hasHeightForWidth())
        self.CONTROL_WINDOW.setSizePolicy(sizePolicy)
        self.CONTROL_WINDOW.setStyleSheet("#CONTROL_WINDOW {\n"
"    border: 1px solid rgb(255, 255, 255);  /* Dodger Blue border */\n"
"    border-radius: 5px;         /* Rounded corners */\n"
"    padding: 5px;               /* Padding inside the border */\n"
" /* Light background color */\n"
"}")
        self.CONTROL_WINDOW.setObjectName("CONTROL_WINDOW")
        self.CONTROLS = QtWidgets.QLineEdit(self.CONTROL_WINDOW)
        self.CONTROLS.setEnabled(False)
        self.CONTROLS.setGeometry(QtCore.QRect(30, 10, 151, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CONTROLS.sizePolicy().hasHeightForWidth())
        self.CONTROLS.setSizePolicy(sizePolicy)
        self.CONTROLS.setStyleSheet("border-style:outset;\n"
"font: 75 6pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-width:3px;\n"
"border-radius: 10px;\n"
"border-color: rgb(30, 144, 255);\n"
"color: rgb(0, 0, 0);")
        self.CONTROLS.setAlignment(QtCore.Qt.AlignCenter)
        self.CONTROLS.setObjectName("CONTROLS")
        self.RESET = QtWidgets.QPushButton(self.CONTROL_WINDOW)
        self.RESET.setGeometry(QtCore.QRect(40, 50, 131, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RESET.sizePolicy().hasHeightForWidth())
        self.RESET.setSizePolicy(sizePolicy)
        self.RESET.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RESET.setStyleSheet("QPushButton{\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(228, 29, 82);\n"
"    border-width:2px;\n"
"border-radius:5px;\n"
"border-style:outset;\n"
"    border-color: rgb(228, 29, 82);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.RESET.setObjectName("RESET")
        self.RUN = QtWidgets.QPushButton(self.CONTROL_WINDOW)
        self.RUN.setEnabled(True)
        self.RUN.setGeometry(QtCore.QRect(40, 100, 131, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RUN.sizePolicy().hasHeightForWidth())
        self.RUN.setSizePolicy(sizePolicy)
        self.RUN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RUN.setStyleSheet("QPushButton{\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border-width:2px;\n"
"border-radius:5px;\n"
"border-style:outset;\n"
"border-color:rgb(85, 170, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.RUN.setObjectName("RUN")
        self.SENSOR_WINDOW = QtWidgets.QWidget(self.centralwidget)
        self.SENSOR_WINDOW.setEnabled(True)
        self.SENSOR_WINDOW.setGeometry(QtCore.QRect(590, 10, 291, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SENSOR_WINDOW.sizePolicy().hasHeightForWidth())
        self.SENSOR_WINDOW.setSizePolicy(sizePolicy)
        self.SENSOR_WINDOW.setStyleSheet("#SENSOR_WINDOW {\n"
"    border: 1px solid white;  /* White border */\n"
"    border-radius: 5px;       /* Rounded corners */\n"
"    padding: 5px;             /* Padding inside the border */\n"
"    color: black;             /* Text color */\n"
"}\n"
"")
        self.SENSOR_WINDOW.setObjectName("SENSOR_WINDOW")
        self.SENSOR_CONTROLS = QtWidgets.QLineEdit(self.SENSOR_WINDOW)
        self.SENSOR_CONTROLS.setEnabled(False)
        self.SENSOR_CONTROLS.setGeometry(QtCore.QRect(60, 10, 171, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SENSOR_CONTROLS.sizePolicy().hasHeightForWidth())
        self.SENSOR_CONTROLS.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(6)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.SENSOR_CONTROLS.setFont(font)
        self.SENSOR_CONTROLS.setStyleSheet("border-style:outset;\n"
"font: 75 6pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-width:3px;\n"
"border-radius: 10px;\n"
"border-color: rgb(30, 144, 255);\n"
"color: rgb(0, 0, 0);")
        self.SENSOR_CONTROLS.setAlignment(QtCore.Qt.AlignCenter)
        self.SENSOR_CONTROLS.setObjectName("SENSOR_CONTROLS")
        self.DHT11 = QtWidgets.QTextEdit(self.SENSOR_WINDOW)
        self.DHT11.setGeometry(QtCore.QRect(20, 50, 101, 41))
        self.DHT11.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.DHT11.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.DHT11.setObjectName("DHT11")
        self.BMP280 = QtWidgets.QTextEdit(self.SENSOR_WINDOW)
        self.BMP280.setGeometry(QtCore.QRect(20, 100, 101, 41))
        self.BMP280.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.BMP280.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.BMP280.setObjectName("BMP280")
        self.MQ135 = QtWidgets.QTextEdit(self.SENSOR_WINDOW)
        self.MQ135.setGeometry(QtCore.QRect(20, 150, 101, 41))
        self.MQ135.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.MQ135.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.MQ135.setObjectName("MQ135")
        self.textEdit_4 = QtWidgets.QTextEdit(self.SENSOR_WINDOW)
        self.textEdit_4.setGeometry(QtCore.QRect(20, 200, 101, 41))
        self.textEdit_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_4.setObjectName("textEdit_4")
        self.DHT11_Label = QtWidgets.QTextEdit(self.SENSOR_WINDOW)
        self.DHT11_Label.setEnabled(False)
        self.DHT11_Label.setGeometry(QtCore.QRect(160, 50, 111, 41))
        self.DHT11_Label.setAcceptDrops(False)
        self.DHT11_Label.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.DHT11_Label.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.DHT11_Label.setReadOnly(True)
        self.DHT11_Label.setObjectName("DHT11_Label")
        self.DHT11_SW = QtWidgets.QCheckBox(self.SENSOR_WINDOW)
        self.DHT11_SW.setEnabled(True)
        self.DHT11_SW.setGeometry(QtCore.QRect(170, 60, 41, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DHT11_SW.sizePolicy().hasHeightForWidth())
        self.DHT11_SW.setSizePolicy(sizePolicy)
        self.DHT11_SW.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DHT11_SW.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image: url(:/newPrefix/ICONS/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image: url(:/newPrefix/ICONS/switch-off.png);\n"
"    \n"
"}")
        self.DHT11_SW.setText("")
        self.DHT11_SW.setIconSize(QtCore.QSize(10, 10))
        self.DHT11_SW.setCheckable(True)
        self.DHT11_SW.setChecked(False)
        self.DHT11_SW.setAutoRepeat(False)
        self.DHT11_SW.setObjectName("DHT11_SW")
        self.BMP280_Label = QtWidgets.QTextEdit(self.SENSOR_WINDOW)
        self.BMP280_Label.setEnabled(False)
        self.BMP280_Label.setGeometry(QtCore.QRect(160, 100, 111, 41))
        self.BMP280_Label.setAcceptDrops(False)
        self.BMP280_Label.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.BMP280_Label.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.BMP280_Label.setReadOnly(True)
        self.BMP280_Label.setObjectName("BMP280_Label")
        self.BMP280_SW = QtWidgets.QCheckBox(self.SENSOR_WINDOW)
        self.BMP280_SW.setEnabled(True)
        self.BMP280_SW.setGeometry(QtCore.QRect(170, 110, 41, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BMP280_SW.sizePolicy().hasHeightForWidth())
        self.BMP280_SW.setSizePolicy(sizePolicy)
        self.BMP280_SW.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BMP280_SW.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image: url(:/newPrefix/ICONS/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image: url(:/newPrefix/ICONS/switch-off.png);\n"
"    \n"
"}")
        self.BMP280_SW.setText("")
        self.BMP280_SW.setIconSize(QtCore.QSize(10, 10))
        self.BMP280_SW.setCheckable(True)
        self.BMP280_SW.setChecked(False)
        self.BMP280_SW.setAutoRepeat(False)
        self.BMP280_SW.setObjectName("BMP280_SW")
        self.MQ135_Label = QtWidgets.QTextEdit(self.SENSOR_WINDOW)
        self.MQ135_Label.setEnabled(False)
        self.MQ135_Label.setGeometry(QtCore.QRect(160, 150, 111, 41))
        self.MQ135_Label.setAcceptDrops(False)
        self.MQ135_Label.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.MQ135_Label.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.MQ135_Label.setReadOnly(True)
        self.MQ135_Label.setObjectName("MQ135_Label")
        self.MQ14_SW = QtWidgets.QCheckBox(self.SENSOR_WINDOW)
        self.MQ14_SW.setEnabled(True)
        self.MQ14_SW.setGeometry(QtCore.QRect(170, 160, 41, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MQ14_SW.sizePolicy().hasHeightForWidth())
        self.MQ14_SW.setSizePolicy(sizePolicy)
        self.MQ14_SW.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MQ14_SW.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image: url(:/newPrefix/ICONS/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image: url(:/newPrefix/ICONS/switch-off.png);\n"
"    \n"
"}")
        self.MQ14_SW.setText("")
        self.MQ14_SW.setIconSize(QtCore.QSize(10, 10))
        self.MQ14_SW.setCheckable(True)
        self.MQ14_SW.setChecked(False)
        self.MQ14_SW.setAutoRepeat(False)
        self.MQ14_SW.setObjectName("MQ14_SW")
        self.IMU_Label = QtWidgets.QTextEdit(self.SENSOR_WINDOW)
        self.IMU_Label.setEnabled(False)
        self.IMU_Label.setGeometry(QtCore.QRect(160, 200, 111, 41))
        self.IMU_Label.setAcceptDrops(False)
        self.IMU_Label.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.IMU_Label.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.IMU_Label.setReadOnly(True)
        self.IMU_Label.setObjectName("IMU_Label")
        self.IMU_SW = QtWidgets.QCheckBox(self.SENSOR_WINDOW)
        self.IMU_SW.setEnabled(True)
        self.IMU_SW.setGeometry(QtCore.QRect(170, 210, 41, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IMU_SW.sizePolicy().hasHeightForWidth())
        self.IMU_SW.setSizePolicy(sizePolicy)
        self.IMU_SW.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.IMU_SW.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image: url(:/newPrefix/ICONS/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image: url(:/newPrefix/ICONS/switch-off.png);\n"
"    \n"
"}")
        self.IMU_SW.setText("")
        self.IMU_SW.setIconSize(QtCore.QSize(10, 10))
        self.IMU_SW.setCheckable(True)
        self.IMU_SW.setChecked(False)
        self.IMU_SW.setAutoRepeat(False)
        self.IMU_SW.setObjectName("IMU_SW")
        self.OUTPUT_WINDOW = QtWidgets.QWidget(self.centralwidget)
        self.OUTPUT_WINDOW.setEnabled(True)
        self.OUTPUT_WINDOW.setGeometry(QtCore.QRect(240, 10, 331, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OUTPUT_WINDOW.sizePolicy().hasHeightForWidth())
        self.OUTPUT_WINDOW.setSizePolicy(sizePolicy)
        self.OUTPUT_WINDOW.setStyleSheet("#OUTPUT_WINDOW {\n"
"    border: 1px solid white;  /* White border */\n"
"    border-radius: 5px;       /* Rounded corners */\n"
"    padding: 5px;             /* Padding inside the border */\n"
"    color: black;             /* Text color */\n"
"}\n"
"")
        self.OUTPUT_WINDOW.setObjectName("OUTPUT_WINDOW")
        self.SENSORS_2 = QtWidgets.QLineEdit(self.OUTPUT_WINDOW)
        self.SENSORS_2.setEnabled(False)
        self.SENSORS_2.setGeometry(QtCore.QRect(20, 20, 291, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SENSORS_2.sizePolicy().hasHeightForWidth())
        self.SENSORS_2.setSizePolicy(sizePolicy)
        self.SENSORS_2.setStyleSheet("border-style:outset;\n"
"font: 75 6pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-width:3px;\n"
"border-radius: 10px;\n"
"border-color: rgb(30, 144, 255);\n"
"color: rgb(0, 0, 0);")
        self.SENSORS_2.setAlignment(QtCore.Qt.AlignCenter)
        self.SENSORS_2.setObjectName("SENSORS_2")
        self.frame = QtWidgets.QFrame(self.OUTPUT_WINDOW)
        self.frame.setGeometry(QtCore.QRect(20, 60, 291, 191))
        self.frame.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: #000000;\n"
"background-color: #ffffff;\n"
"    border: 1px solid black;  /* White border with 2px width */\n"
"    border-radius: 5px;       /* Rounded corners with 5px radius */\n"
"    border-style: outset; \n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.MENU_WINDOW = QtWidgets.QWidget(self.centralwidget)
        self.MENU_WINDOW.setGeometry(QtCore.QRect(20, 300, 861, 121))
        self.MENU_WINDOW.setStyleSheet("#MENU_WINDOW {\n"
"    border: 1px solid rgb(255, 255, 255);  /* Dodger Blue border */\n"
"    border-radius: 5px;         /* Rounded corners */\n"
"    padding: 5px;               /* Padding inside the border */\n"
" /* Light background color */\n"
"}")
        self.MENU_WINDOW.setObjectName("MENU_WINDOW")
        self.MENU = QtWidgets.QLineEdit(self.MENU_WINDOW)
        self.MENU.setEnabled(False)
        self.MENU.setGeometry(QtCore.QRect(240, 20, 281, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MENU.sizePolicy().hasHeightForWidth())
        self.MENU.setSizePolicy(sizePolicy)
        self.MENU.setStyleSheet("border-style:outset;\n"
"font: 75 6pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-width:3px;\n"
"border-radius: 10px;\n"
"border-color: rgb(30, 144, 255);\n"
"color: rgb(0, 0, 0);")
        self.MENU.setAlignment(QtCore.Qt.AlignCenter)
        self.MENU.setObjectName("MENU")
        self.DHT11_Label_2 = QtWidgets.QTextEdit(self.MENU_WINDOW)
        self.DHT11_Label_2.setEnabled(False)
        self.DHT11_Label_2.setGeometry(QtCore.QRect(50, 60, 151, 41))
        self.DHT11_Label_2.setAcceptDrops(False)
        self.DHT11_Label_2.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.DHT11_Label_2.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.DHT11_Label_2.setReadOnly(True)
        self.DHT11_Label_2.setObjectName("DHT11_Label_2")
        self.DHT11_Label_3 = QtWidgets.QTextEdit(self.MENU_WINDOW)
        self.DHT11_Label_3.setEnabled(False)
        self.DHT11_Label_3.setGeometry(QtCore.QRect(250, 60, 151, 41))
        self.DHT11_Label_3.setAcceptDrops(False)
        self.DHT11_Label_3.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.DHT11_Label_3.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.DHT11_Label_3.setReadOnly(True)
        self.DHT11_Label_3.setObjectName("DHT11_Label_3")
        self.DHT11_Label_4 = QtWidgets.QTextEdit(self.MENU_WINDOW)
        self.DHT11_Label_4.setEnabled(False)
        self.DHT11_Label_4.setGeometry(QtCore.QRect(450, 60, 151, 41))
        self.DHT11_Label_4.setAcceptDrops(False)
        self.DHT11_Label_4.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.DHT11_Label_4.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.DHT11_Label_4.setReadOnly(True)
        self.DHT11_Label_4.setObjectName("DHT11_Label_4")
        self.DHT11_Label_5 = QtWidgets.QTextEdit(self.MENU_WINDOW)
        self.DHT11_Label_5.setEnabled(False)
        self.DHT11_Label_5.setGeometry(QtCore.QRect(660, 60, 151, 41))
        self.DHT11_Label_5.setAcceptDrops(False)
        self.DHT11_Label_5.setStyleSheet("background-color: #6a5acd;\n"
"color:rgb(255, 255, 255)")
        self.DHT11_Label_5.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.DHT11_Label_5.setReadOnly(True)
        self.DHT11_Label_5.setObjectName("DHT11_Label_5")
        self.DHT11_SW_2 = QtWidgets.QCheckBox(self.MENU_WINDOW)
        self.DHT11_SW_2.setEnabled(True)
        self.DHT11_SW_2.setGeometry(QtCore.QRect(60, 70, 41, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DHT11_SW_2.sizePolicy().hasHeightForWidth())
        self.DHT11_SW_2.setSizePolicy(sizePolicy)
        self.DHT11_SW_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DHT11_SW_2.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image: url(:/newPrefix/ICONS/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image: url(:/newPrefix/ICONS/switch-off.png);\n"
"    \n"
"}")
        self.DHT11_SW_2.setText("")
        self.DHT11_SW_2.setIconSize(QtCore.QSize(10, 10))
        self.DHT11_SW_2.setCheckable(True)
        self.DHT11_SW_2.setChecked(False)
        self.DHT11_SW_2.setAutoRepeat(False)
        self.DHT11_SW_2.setObjectName("DHT11_SW_2")
        self.DHT11_SW_3 = QtWidgets.QCheckBox(self.MENU_WINDOW)
        self.DHT11_SW_3.setEnabled(True)
        self.DHT11_SW_3.setGeometry(QtCore.QRect(260, 70, 41, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DHT11_SW_3.sizePolicy().hasHeightForWidth())
        self.DHT11_SW_3.setSizePolicy(sizePolicy)
        self.DHT11_SW_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DHT11_SW_3.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image: url(:/newPrefix/ICONS/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image: url(:/newPrefix/ICONS/switch-off.png);\n"
"    \n"
"}")
        self.DHT11_SW_3.setText("")
        self.DHT11_SW_3.setIconSize(QtCore.QSize(10, 10))
        self.DHT11_SW_3.setCheckable(True)
        self.DHT11_SW_3.setChecked(False)
        self.DHT11_SW_3.setAutoRepeat(False)
        self.DHT11_SW_3.setObjectName("DHT11_SW_3")
        self.DHT11_SW_4 = QtWidgets.QCheckBox(self.MENU_WINDOW)
        self.DHT11_SW_4.setEnabled(True)
        self.DHT11_SW_4.setGeometry(QtCore.QRect(460, 70, 41, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DHT11_SW_4.sizePolicy().hasHeightForWidth())
        self.DHT11_SW_4.setSizePolicy(sizePolicy)
        self.DHT11_SW_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DHT11_SW_4.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image: url(:/newPrefix/ICONS/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image: url(:/newPrefix/ICONS/switch-off.png);\n"
"    \n"
"}")
        self.DHT11_SW_4.setText("")
        self.DHT11_SW_4.setIconSize(QtCore.QSize(10, 10))
        self.DHT11_SW_4.setCheckable(True)
        self.DHT11_SW_4.setChecked(False)
        self.DHT11_SW_4.setAutoRepeat(False)
        self.DHT11_SW_4.setObjectName("DHT11_SW_4")
        self.DHT11_SW_5 = QtWidgets.QCheckBox(self.MENU_WINDOW)
        self.DHT11_SW_5.setEnabled(True)
        self.DHT11_SW_5.setGeometry(QtCore.QRect(670, 70, 41, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DHT11_SW_5.sizePolicy().hasHeightForWidth())
        self.DHT11_SW_5.setSizePolicy(sizePolicy)
        self.DHT11_SW_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DHT11_SW_5.setStyleSheet("QCheckBox::indicator{\n"
"background-color: #6a5acd;\n"
"width: 42px;\n"
"height: 32px;}\n"
"\n"
"QCheckBox::indicator:checked{image: url(:/newPrefix/ICONS/switch-on.png);\n"
"}\n"
"QCheckBox::indicator:unchecked{image: url(:/newPrefix/ICONS/switch-off.png);\n"
"    \n"
"}")
        self.DHT11_SW_5.setText("")
        self.DHT11_SW_5.setIconSize(QtCore.QSize(10, 10))
        self.DHT11_SW_5.setCheckable(True)
        self.DHT11_SW_5.setChecked(False)
        self.DHT11_SW_5.setAutoRepeat(False)
        self.DHT11_SW_5.setObjectName("DHT11_SW_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 18))
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
        self.NAMES_WINDOW.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600; color:#ffffff;\">SUBJECT: 3EC705CC24 EMBEDDED SYSTEMS</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600; color:#ffffff;\">SPECIAL ASSIGNMENT</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600; color:#ffffff;\">VIDHI RUPARELIA  22BEC143</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600; color:#ffffff;\">SNEH SHAH  22BEC121</span></p></body></html>"))
        self.CONTROLS.setText(_translate("MainWindow", "PROGRAM CONTROLS"))
        self.RESET.setText(_translate("MainWindow", "Reset"))
        self.RUN.setText(_translate("MainWindow", "Run"))
        self.SENSOR_CONTROLS.setText(_translate("MainWindow", "SENSOR CONTROLS"))
        self.DHT11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600;\">DHT11</span></p></body></html>"))
        self.BMP280.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600;\">BMP280</span></p></body></html>"))
        self.MQ135.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600;\">MQ135</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600;\">IMU SENSOR</span></p></body></html>"))
        self.DHT11_Label.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">DHT11</span></p></body></html>"))
        self.BMP280_Label.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">BMP280</span></p></body></html>"))
        self.MQ135_Label.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">MQ135</span></p></body></html>"))
        self.IMU_Label.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">IMU</span></p></body></html>"))
        self.SENSORS_2.setText(_translate("MainWindow", "OUTPUT"))
        self.MENU.setText(_translate("MainWindow", "MENU"))
        self.DHT11_Label_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">CSV</p></body></html>"))
        self.DHT11_Label_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Drive</p></body></html>"))
        self.DHT11_Label_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">MQTT</p></body></html>"))
        self.DHT11_Label_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">DB</p></body></html>"))
import ico_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
