import time
import json
import board
import adafruit_bmp280
import paho.mqtt.client as mqtt

# MQTT Broker
HOST = 'localhost'
INTERVAL = 2  # Sensor reading interval in seconds

# BMP280 Sensor Setup with Correct Address (0x76)
i2c = board.I2C()  # Uses default I2C pins (SCL, SDA)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)

# Set sea level pressure for altitude calculations (change as needed)
bmp280.sea_level_pressure = 1013.25  

# MQTT Client Setup
sensor_data = {'temperature': 0, 'pressure': 0, 'altitude': 0}
next_reading = time.time()

client = mqtt.Client()
client.connect(HOST, 1883, 60)
client.loop_start()

try:
    while True:
        # Read sensor values
        temperature = round(bmp280.temperature, 2)
        pressure = round(bmp280.pressure, 2)
        altitude = round(bmp280.altitude, 2)

        print(f"Temperature: {temperature}°C, Pressure: {pressure} hPa, Altitude: {altitude} m")

        # Store sensor data
        sensor_data['temperature'] = temperature
        sensor_data['pressure'] = pressure
        sensor_data['altitude'] = altitude

        # Publish to MQTT
        client.publish('bmp280/sensordata', json.dumps(sensor_data), 1)

        # Wait for the next reading
        next_reading += INTERVAL
        sleep_time = next_reading - time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)

except KeyboardInterrupt:
    print("\nStopping...")
    
finally:
    client.loop_stop()
    client.disconnect()
