import numpy as np
import pandas as pd

# Read the 'log.csv' file
try:
    df = pd.read_csv('log.csv')  # Read the CSV file named 'log.csv'
except FileNotFoundError:
    print("File 'log.csv' not found.")
    exit(1)  # Exit the script if the file is not found

# Extract EnergyTake values
EnergyTake = df['EnergyTake'].values

# Print the extracted EnergyTake values
print("EnergyTake Values:", EnergyTake)
