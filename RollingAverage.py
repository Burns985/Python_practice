from collections import defaultdict
from datetime import datetime
import numpy as np

data = [
    ['101', '3/2/2018', 10],
    ['101', '3/3/2018', 20],
    ['101', '3/7/2018', 30],
    ['101', '3/8/2018', 40],
    ['102', '3/5/2018', 10],
    ['102', '3/6/2018', 20],
    ['102', '3/7/2018', 30],
    ['102', '3/8/2018', 40],
    ['102', '3/20/2018', 50]
]

# Create a dictionary to store rolling data for each identifier
rolling_data = defaultdict(list)

# Convert date strings to datetime objects
dates = [datetime.strptime(entry[1], '%m/%d/%Y') for entry in data]

# Sort dates in descending order and select the last 3 dates
last_3_dates = sorted(list(set(dates)), reverse=True)[:3]

# Populate rolling_data dictionary with values from the last 3 dates
for entry in data:
    identifier, date, value = entry
    if datetime.strptime(date, '%m/%d/%Y') in last_3_dates:
        rolling_data[identifier].append(value)

# Flatten the dictionary values into a single list
rolling_data_values = [value for values in rolling_data.values() for value in values]

# Calculate the mean of the rolling data values using numpy
rolling_data_mean = np.mean(rolling_data_values)

# Print the rolling average for the last 3 days
print("Rolling Average:", rolling_data_mean)
