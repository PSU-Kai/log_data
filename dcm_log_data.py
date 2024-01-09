import csv
import time
import pandas as pd

file_path = "/home/pi/water_heaters_testings/dcs/build/debug/log.csv"

# Constants

INTERVAL_CONSTANT = 3600

# Specify the path for the output CSV file
output_csv_file = "/home/pi/client/data.csv"

while True:
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            last_valid_row = None

            for row in reader:
                # Check if the row has the expected number of columns
                if len(row) == 12:
                    last_valid_row = row

            if last_valid_row is not None:
                energy_take_str = last_valid_row[-4]
                energy_take = int(energy_take_str)  # Convert to integer
                power_take_str = last_valid_row[3]
                POWER_CONSTANT = int(power_take_str)

                print("Energy Take:", energy_take)

                # Calculate additional values
                interval = INTERVAL_CONSTANT
                power = POWER_CONSTANT
                duration = power / energy_take

                print("Interval:", interval)
                print("Power:", power)
                print("Duration:", duration)

                # Create a DataFrame with the data
                data = pd.DataFrame({'Energy Take': [energy_take],
                                     'Interval': [interval],
                                     'Power': [power],
                                     'Duration': [duration]})

                # Save the DataFrame to the CSV file
                data.to_csv(output_csv_file, index=False)
                print(f"Data saved to {output_csv_file}")
            else:
                print("No valid rows found in the CSV file.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Wait for 60 seconds before checking again
    time.sleep(30)

