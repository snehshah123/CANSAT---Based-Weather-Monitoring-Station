Weather Monitoring System for CANSAT 🛰️
This project details the development of a compact, cost-effective embedded system designed for a CANSAT (a can-sized satellite) to collect and transmit atmospheric data during its descent. The system is built for real-time environmental monitoring in educational and aerospace research.



Key Features

Atmospheric Sensors: The system uses a BMP280 sensor to measure atmospheric pressure and temperature and an IMU (Inertial Measurement Unit) to collect motion and orientation data.



Central Processing Unit: A Raspberry Pi (RPi) serves as the central processing unit for acquiring and managing sensor data.


Data Pipeline: The project utilizes an IoT-based MING pipeline (MQTT, InfluxDB, Node-RED, Grafana) for efficient data processing and visualization.


Node-RED: Deployed on the RPi to process data, integrate sensors, and manage MQTT-based communication.



MQTT: Used for efficient wireless data transmission.



InfluxDB: A time-series database for storing continuous sensor data streams.



Grafana: Provides interactive dashboards for real-time visualization and analysis of weather parameters.



Custom GUI: A custom-built graphical user interface (GUI) allows users to view real-time sensor readings, configure sensors, and control the system.






Data Logging & Storage: The system supports CSV data logging and automatically uploads datasets to Google Drive for cloud-based storage and remote access.



System Architecture
The system's architecture is a clear, sequential flow. Sensors collect data and transmit it to the Raspberry Pi. The RPi then processes the data using Node-RED and stores it in InfluxDB. Finally, the stored data is visualized on Grafana dashboards. Users can interact with the system and its data through the custom GUI.


Setup & Implementation
The project was implemented by integrating the Raspberry Pi with the BMP280 and IMU sensors via I2C protocols for reliable data acquisition. Node-RED was used for real-time sensor integration and data processing. The collected data was stored in InfluxDB and visualized on a Grafana dashboard, providing a clear graphical representation of the weather parameters. The custom GUI enhances user interaction with features like sensor control and data management.





Future Scope
Future improvements for this project include:

AI-based Predictive Analytics: Implement AI models for weather forecasting.

Power Optimization: Improve energy efficiency using low-power microcontrollers or solar energy.

Edge Computing: Incorporate edge computing for faster on-device data processing.

Expanded Sensor Integration: Add more sensors for comprehensive environmental monitoring.

Enhanced Security: Strengthen data security for reliable cloud storage.
