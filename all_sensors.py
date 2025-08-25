import time
import board
import adafruit_bmp280
import smbus
import math
import RPi.GPIO as GPIO

# Create sensor object using I2C
i2c = board.I2C()  # Uses board.SCL (GPIO3) and board.SDA (GPIO2)
bmp = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)  # Default address

# Correct settings
bmp.sea_level_pressure = 1013.25

# I2C address for the ICM-20948
ICM20948_ADDR = 0x69  # Default I2C address

# Register addresses for ICM-20948
PWR_MGMT_1 = 0x06
GYRO_CONFIG = 0x01
ACCEL_XOUT_H = 0x2D
ACCEL_YOUT_H = 0x2F
ACCEL_ZOUT_H = 0x31
GYRO_XOUT_H = 0x33
GYRO_YOUT_H = 0x35
GYRO_ZOUT_H = 0x37

# Initialize I2C (SMBus)
bus = smbus.SMBus(1)

# Wake up the ICM-20948
bus.write_byte_data(ICM20948_ADDR, PWR_MGMT_1, 0x01)
time.sleep(0.1)

# Set the gyroscope range (±250 degrees per second)
bus.write_byte_data(ICM20948_ADDR, GYRO_CONFIG, 0x00)

# Function to read a 16-bit value from a register
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
        return 0  # Return 0 if read fails

def read_imu_data():
    accel_x = read_word(ACCEL_XOUT_H)
    accel_y = read_word(ACCEL_YOUT_H)
    accel_z = read_word(ACCEL_ZOUT_H)
    gyro_z = read_word(GYRO_ZOUT_H)
    return accel_x, accel_y, accel_z, gyro_z

# Complementary filter variables
gyro_scale = 131.0  # Adjusted scale for gyroscope
yaw = 0
prev_time = time.time()

try:
    while True:
        current_time = time.time()
        dt = current_time - prev_time  # Calculate time difference
        prev_time = current_time

        temperature = bmp.temperature
        pressure = bmp.pressure
        altitude = bmp.altitude 

        accel_x, accel_y, accel_z, gyro_z = read_imu_data()

        # Convert raw values to gyro in degrees/s
        gyro_z = gyro_z / gyro_scale

        # Integrate the gyroscope data
        yaw += gyro_z * dt
        yaw = yaw % 360  # Normalize yaw to be within 0 to 360 degrees

        # Calculate roll and pitch from accelerometer
        roll = math.atan2(accel_y, accel_z) * 180 / math.pi
        pitch = math.atan2(-accel_x, math.sqrt(accel_y**2 + accel_z**2)) * 180 / math.pi

        print("Roll: {:.2f}° | Pitch: {:.2f}° | Yaw: {:.2f}°".format(roll, pitch, yaw))
        print("Temperature: {:.2f} °C | Pressure: {:.2f} hPa | Altitude: {:.2f} m".format(temperature, pressure, altitude))
        
        time.sleep(0.01)
        
except KeyboardInterrupt:
    print("\nProgram stopped by user.")
