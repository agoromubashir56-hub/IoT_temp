"""
Python-Based IoT Temperature Monitoring System
LENS-COS 324 Practical Assignment

The program simulates a temperature sensor, saves 50 readings to CSV,
loads the CSV file, validates each reading, calculates the average,
plots valid readings, and warns when a temperature exceeds 35 C.
"""

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path
import matplotlib.pyplot as plt

DATA_FILE = Path("temperature_readings.csv")
GRAPH_FILE = Path("temperature_graph.png")
NUMBER_OF_READINGS = 50
WARNING_LIMIT = 35.0


def simulate_sensor_readings(number_of_readings=NUMBER_OF_READINGS):
    """Return simulated temperature readings with timestamps."""
    readings = []
    start_time = datetime.now() - timedelta(minutes=number_of_readings - 1)

    for index in range(number_of_readings):
        # Simulate normal environmental temperatures between 20 and 40 C.
        temperature = round(random.uniform(20.0, 40.0), 2)
        timestamp = (start_time + timedelta(minutes=index)).isoformat(
            timespec="seconds"
        )
        readings.append({
            "timestamp": timestamp,
            "temperature_c": temperature
        })

    return readings


def save_readings_to_csv(readings, filename=DATA_FILE):
    """Save simulated readings to a CSV file."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=["timestamp", "temperature_c"]
        )
        writer.writeheader()
        writer.writerows(readings)

    print(f"Saved {len(readings)} readings to '{filename}'.")


def load_and_validate_csv(filename=DATA_FILE):
    """
    Read the CSV file and keep only valid numeric temperatures.
    Missing values, non-numeric values, and values outside the
    plausible sensor range (-50 C to 100 C) are rejected.
    """
    valid_readings = []

    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            required_columns = {"timestamp", "temperature_c"}
            if not required_columns.issubset(reader.fieldnames or []):
                raise ValueError(
                    "CSV must contain timestamp and temperature_c columns."
                )

            for row_number, row in enumerate(reader, start=2):
                timestamp = (row.get("timestamp") or "").strip()
                raw_temperature = (row.get("temperature_c") or "").strip()

                if not timestamp or not raw_temperature:
                    print(f"Row {row_number}: missing data - skipped.")
                    continue

                try:
                    temperature = float(raw_temperature)
                except ValueError:
                    print(
                        f"Row {row_number}: invalid temperature "
                        f"'{raw_temperature}' - skipped."
                    )
                    continue

                if not -50.0 <= temperature <= 100.0:
                    print(
                        f"Row {row_number}: temperature {temperature} C "
                        "is outside the accepted sensor range - skipped."
                    )
                    continue

                valid_readings.append({
                    "timestamp": timestamp,
                                  "temperature_c": temperature
                })

    except FileNotFoundError:
        print(f"Error: '{filename}' was not found.")
        return []

    return valid_readings


def display_average(readings):
    """Calculate and display the average of valid readings."""
    if not readings:
        print("No valid temperature readings are available.")
        return None

    temperatures = [item["temperature_c"] for item in readings]
    average = sum(temperatures) / len(temperatures)

    print(f"\nValid readings: {len(temperatures)}")
    print(f"Average temperature: {average:.2f} C")
    return average


def check_temperature_warnings(readings):
    """Display a warning for every reading above 35 C."""
    print(f"\nTemperature warning limit: {WARNING_LIMIT:.1f} C")

    warnings_found = 0
    for item in readings:
        temperature = item["temperature_c"]
        if temperature > WARNING_LIMIT:
            warnings_found += 1
            print(
                f"WARNING: {temperature:.2f} C recorded at "
                f"{item['timestamp']} - above 35 C."
            )

    if warnings_found == 0:
        print("No readings exceeded 35 C.")
    else:
        print(f"Total high-temperature warnings: {warnings_found}")


def create_temperature_graph(readings, filename=GRAPH_FILE):
    """Plot valid temperatures against their reading number."""
    if not readings:
        print("Graph not created because there are no valid readings.")
        return

    temperatures = [item["temperature_c"] for item in readings]
    reading_numbers = list(range(1, len(temperatures) + 1))

    plt.figure(figsize=(10, 5))
    plt.plot(
        reading_numbers,
        temperatures,
        marker="o",
        linestyle="-",
        label="Temperature"
    )
    plt.axhline(
        y=WARNING_LIMIT,
        linestyle="--",
        label="Warning limit (35 C)"
    )
    plt.title("IoT Temperature Monitoring System")
    plt.xlabel("Reading Number")
    plt.ylabel("Temperature (C)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()

    print(f"Temperature graph saved as '{filename}'.")


def main():
    print("=== PYTHON-BASED IoT TEMPERATURE MONITOR ===")

    # Step 1: Simulate at least 50 sensor readings.
    simulated_readings = simulate_sensor_readings()

    # Step 2: Save the readings to CSV.
    save_readings_to_csv(simulated_readings)

    # Step 3: Read the CSV file and validate its contents.
    readings = load_and_validate_csv()

    # Step 4: Calculate and display the average.
    display_average(readings)

    # Step 5: Warn when a reading is above 35 C.
    check_temperature_warnings(readings)

    # Step 6: Create the temperature graph.
    create_temperature_graph(readings)

    print("\nMonitoring process completed.")


if __name__ == "__main__":
    main()