import sys
import csv
import time
import threading
import math
from PyQt5 import QtWidgets, QtCore, QtGui
import board
import adafruit_bmp280
import smbus
import json
import paho.mqtt.client as mqtt

from weather11 import Ui_MainWindow

# Initialize BMP280 sensor
i2c = board.I2C()
bmp = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)
bmp.sea_level_pressure = 1013.25

# I2C setup for IMU (ICM-20948)
ICM20948_ADDR = 0x69
bus = smbus.SMBus(1)

# Register addresses
PWR_MGMT_1 = 0x06
GYRO_CONFIG = 0x01
ACCEL_XOUT_H = 0x2D
ACCEL_YOUT_H = 0x2F
ACCEL_ZOUT_H = 0x31
GYRO_ZOUT_H = 0x37

# Wake up IMU
bus.write_byte_data(ICM20948_ADDR, PWR_MGMT_1, 0x01)
time.sleep(0.1)
bus.write_byte_data(ICM20948_ADDR, GYRO_CONFIG, 0x00)

# Function to read IMU sensor data
def read_word(reg):
    try:
        high = bus.read_byte_data(ICM20948_ADDR, reg)
        low = bus.read_byte_data(ICM20948_ADDR, reg + 1)
        value = (high << 8) + low
        if value >= 0x8000:
            value -= 65536
        return value
    except OSError:
        print("I2C Read Error")
        return 0

def read_imu_data():
    accel_x = read_word(ACCEL_XOUT_H)
    accel_y = read_word(ACCEL_YOUT_H)
    accel_z = read_word(ACCEL_ZOUT_H)
    gyro_z = read_word(GYRO_ZOUT_H)
    return accel_x, accel_y, accel_z, gyro_z

CSV_FILE = "CANSAT_weather_data.csv"

HOST = '192.168.1.68'  # Replace with actual Node-Red IP
PORT = 1883

class WeatherApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_live_data)

        
        # Create a QTableWidget inside the frame
        self.table = QtWidgets.QTableWidget(self.ui.frame)
        self.table.setGeometry(10, 10, 310, 180)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Time", "Value1", "Value2", "Value3"])
        self.table.setStyleSheet("color: black; font-size: 10pt; background-color: white;")
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)

        # Sensor toggles
        self.recording = False  # Data recording state
        self.displaying = False  # CSV Display state
        self.show_bmp280 = False  # Show BMP280 data
        self.show_imu = False  # Show IMU data

        # Connect buttons
        self.ui.RUN.clicked.connect(self.start_recording)
        self.ui.RESET.clicked.connect(self.stop_recording)
        self.ui.DHT11_SW_2.clicked.connect(self.toggle_csv_display)
        self.ui.BMP280_SW.clicked.connect(self.toggle_bmp280)
        self.ui.IMU_SW.clicked.connect(self.toggle_imu)
        

    def start_recording(self):
        """Start recording sensor data to CSV."""
        if not self.recording:
            self.recording = True
            self.data_thread = threading.Thread(target=self.collect_data, daemon=True)
            self.data_thread.start()

    def stop_recording(self):
        """Stop recording sensor data."""
        self.recording = False

    def collect_data(self):
        """Continuously collects sensor data and writes to CSV file (appends data)."""
        with open(CSV_FILE, "a", newline="") as file:  # Append mode
            writer = csv.writer(file)
            writer.writerow(["Time", "Roll", "Pitch", "Yaw", "Temperature", "Altitude", "Pressure"])

        while self.recording:
            try:
                accel_x, accel_y, accel_z, gyro_z = read_imu_data()
                roll = round(math.atan2(accel_y, accel_z) * 180 / math.pi, 2)
                pitch = round(math.atan2(-accel_x, (accel_y**2 + accel_z**2) ** 0.5) * 180 / math.pi, 2)
                yaw = round(gyro_z / 131.0, 2)
                temperature = round(bmp.temperature, 2)
                pressure = round(bmp.pressure, 2)
                altitude = round(bmp.altitude, 2)

                with open(CSV_FILE, "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([time.strftime("%H:%M:%S"), roll, pitch, yaw, temperature, altitude, pressure])

                time.sleep(1)
            except Exception as e:
                print(f"Error: {e}")

    def toggle_csv_display(self):
        """Toggles the display of CSV data (does not start recording)."""
        self.displaying = not self.displaying
        if self.displaying:
            self.update_live_data()  # Update immediately
            self.timer.start(1000)  # Refresh every 1 second
        else:
            self.timer.stop()


    def toggle_bmp280(self):
        """Toggles display of BMP280 data."""
        if self.displaying:
            self.show_bmp280 = not self.show_bmp280
            self.update_live_data()

    def toggle_imu(self):
        """Toggles display of IMU data."""
        if self.displaying:
            self.show_imu = not self.show_imu
            self.update_live_data()

    def update_live_data(self):
        """Update the output window with the last 10 sensor values in table format."""
        try:
            with open(CSV_FILE, "r") as file:
                lines = file.readlines()[1:]  # Skip header
                last_10 = lines[-10:]

            self.table.setRowCount(len(last_10))

            for row_idx, line in enumerate(last_10):
                values = line.strip().split(",")

                time_val = values[0]

                if self.show_bmp280 and not self.show_imu:
                    data_values = [values[4], values[5], values[6]]  # Temp, Alt, Pressure
                    headers = ["Time", "Temp", "Alt", "Pressure"]

                elif self.show_imu and not self.show_bmp280:
                    data_values = [values[1], values[2], values[3]]  # Roll, Pitch, Yaw
                    headers = ["Time", "Roll", "Pitch", "Yaw"]

                elif self.show_bmp280 and self.show_imu:
                    data_values = [values[1], values[2], values[3], values[4], values[5], values[6]]  # All
                    headers = ["Time", "Roll", "Pitch", "Yaw", "Temp", "Alt", "Pressure"]
                else:
                    self.table.setColumnCount(1)
                    self.table.setHorizontalHeaderLabels(["No Data Selected"])
                    return

                self.table.setColumnCount(len(data_values) + 1)
                self.table.setHorizontalHeaderLabels(headers)

                self.table.setItem(row_idx, 0, QtWidgets.QTableWidgetItem(time_val))
                for col_idx, value in enumerate(data_values):
                    item = QtWidgets.QTableWidgetItem(value)
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setItem(row_idx, col_idx + 1, item)

        except Exception as e:
            print("Error updating table:", e)

    def closeEvent(self, event):
        """Handle app closing."""
        self.recording = False
        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())
