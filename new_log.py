import numpy as np
import pandas as pd
import time
import os

# Constants
POWER_CONSTANT = 4500
INTERVAL_CONSTANT = 3600

# Function to read and extract EnergyTake value
def extract_energy_take(filename):
    log_file_path = "/home/pi/water_heaters_testings/dcs/build/debug/" + filename

    try:
        df = pd.read_csv(log_file_path)  # Read the CSV file
    except FileNotFoundError:
        print(f"File '{log_file_path}' not found.")
        return None
    
    # Extract EnergyTake value from the 4th column from the back
    EnergyTake_column_index = -4
    
    # Assuming you want the second to the last row and 4th to the last column
    energy_take = df.iloc[-2, EnergyTake_column_index]
    
    return energy_take

# Main loop
while True:
    energy_take_value = extract_energy_take('log.csv')

    if energy_take_value is not None:
        duration = energy_take_value / POWER_CONSTANT  # Calculate duration based on energy take
        power = POWER_CONSTANT
        interval = INTERVAL_CONSTANT
        print("EnergyTake Value:", energy_take_value)
        print("Duration:", duration)
        print("Power:", power)
        print("Interval:", interval)

        # Create a DataFrame with the new data
        data = pd.DataFrame({'EnergyTake': [energy_take_value],
                             'Duration': [duration],
                             'Power': [power],
                             'Interval': [interval]})

        # Specify the file path
        csv_file_path = '/home/pi/client/data.csv'

        # Check if the file exists and delete it
        if os.path.exists(csv_file_path):
            os.remove(csv_file_path)

        # Save the new DataFrame to the CSV file
        data.to_csv(csv_file_path, index=False)
    else:
        print("EnergyTake value extraction failed.")

    time.sleep(60)  # Wait for 1 minute

