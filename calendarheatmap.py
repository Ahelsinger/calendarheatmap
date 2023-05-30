import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from collections import Counter
import calendar

# Define the data
data = [
    # add the dates here
]

# Convert the dates to datetime objects and extract the date component
dates = []
for date in data:
    if date != "":
        try:
            date_obj = datetime.strptime(date, "%m/%d/%Y %I:%M:%S %p")
        except ValueError:
            date_obj = datetime.strptime(date, "%m/%d/%Y")
        dates.append(date_obj.date())

# Count the occurrences of each date
date_counts = Counter(dates)

# Extract the unique years and months from the dates
years = set(date.year for date in dates)
months = set(date.month for date in dates)

# Determine the number of days in each month
num_days = [calendar.monthrange(year, month)[1] for year in years for month in months]

# Create a square matrix filled with zeros
calendar_matrix = np.full((len(years) * len(months), max(num_days)), 0)

# Populate the calendar matrix with date counts
# Populate the calendar matrix with date counts
for i, year in enumerate(years):
    for j, month in enumerate(months):
        for day in range(1, num_days[j] + 1):
            date = datetime(year, month, day).date()
            count = date_counts.get(date, 0)
            calendar_matrix[i * len(months) + j, day - 1] = count


# Plot the calendar heatmap
fig, ax = plt.subplots(figsize=(10, 6))
im = ax.imshow(calendar_matrix, cmap='YlGnBu')

# Add gridlines
ax.grid(True, which='both', color='black', linewidth=0.5)

# Set the ticks and labels for x-axis
ax.set_xticks(range(max(num_days)))
ax.set_xticklabels(range(1, max(num_days) + 1), rotation=90, fontsize=7)  # Rotate x-axis labels by 45 degrees and set fontsize

# Set the ticks and labels for y-axis
y_labels = [datetime(year, month, 1).strftime("%b, %Y") for year in years for month in months]
ax.set_yticks(range(len(years) * len(months)))
ax.set_yticklabels(y_labels, fontsize=6)  # Set y-axis tick labels fontsize

# Set the title and labels
ax.set_title("Calendar Heatmap", fontsize=12)  # Set the title fontsize
ax.set_xlabel("Day of the Month", fontsize=10)  # Set the x-axis label fontsize
ax.set_ylabel("Month, Year", fontsize=10)  # Set the y-axis label fontsize

# Show the colorbar
cbar = plt.colorbar(im)

# Display the calendar heatmap
plt.tight_layout()
plt.show()
