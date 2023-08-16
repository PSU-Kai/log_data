import numpy as np
import pandas as pd
import time

# Function to read and extract EnergyTake value
def extract_energy_take(filename):
    try:
        df = pd.read_csv(filename)  # Read the CSV file
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

    # Extract EnergyTake value from the 4th column from the back
    EnergyTake_column_index = -4
    energy_take = df.iloc[-1, EnergyTake_column_index]  # Assuming you want the last row

    return energy_take

# Main loop
while True:
    energy_take_value = extract_energy_take('log.csv')
    
    if energy_take_value is not None:
        print("EnergyTake Value:", energy_take_value)
    else:
        print("EnergyTake value extraction failed.")
    
    time.sleep(60)  # Wait for 1 minute
