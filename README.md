
# IoT Temperature Monitoring System

## 1. Project Description
This project is a Python-based simulation of an IoT temperature monitoring system. It generates 50 simulated temperature readings without using a physical sensor.

## 2. Objectives
- Generate 50 temperature readings.
- Save readings in a CSV file.
- Calculate the average temperature.
- Detect missing and invalid data.
- Generate a temperature graph.
- Display warnings when temperature exceeds 35°C.

## 3. Tools and Technologies
- Python 3
- CSV
- Random module
- Datetime module
- Matplotlib
- Visual Studio Code

## 4. Project Files
- `main.py` – Main Python program.
- `temperature_readings.csv` – Stores temperature readings.
- `temperature_graph.png` – Displays the temperature graph.
- `README.md` – Project documentation.

## 5. Installation
Install Matplotlib using:

```bash
python -m pip install matplotlib
```

## 6. How to Run
Open the project folder in VS Code and run:

```bash
python main.py
```

## 7. Data Validation
The program detects missing, non-numeric, and out-of-range temperature readings and skips invalid records.

## 8. IoT Application
A real IoT temperature sensor collects environmental temperature data and sends it to a computer or cloud platform. This project uses Python to simulate the sensor readings.

## 9. Conclusion
This project demonstrates how Python can be used to simulate temperature monitoring, data storage, data validation, average calculation, warning notifications, and graphical visualization.
