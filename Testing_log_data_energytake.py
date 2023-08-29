#THis code it is use for testing purpose to see if you can extract
#the data from the log.csv file that contains the commodity read

import csv

file_path = "/home/pi/water_heaters_testings/dcs/build/debug/log.csv"

try:
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        last_valid_row = None

        for row in reader:
            # Check if the row has the expected number of columns
            if len(row) == 12:
                last_valid_row = row

        if last_valid_row is not None:
            energy_take = last_valid_row[-4]
            print("Energy Take:", energy_take)
        else:
            print("No valid rows found in the CSV file.")
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
