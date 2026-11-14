import numpy as np

# Sensor data
sensor_data = np.array([
    24.5, 25.1, 26.3, 27.0, 28.2,
    29.1, 27.8, 26.5, 25.7, 30.2
])

# Display sensor data
print("Sensor Data:", sensor_data)

# Calculate Mean
print("Mean :", round(np.mean(sensor_data), 2))

# Calculate Median
print("Median :", round(np.median(sensor_data), 2))

# Find Minimum
print("Minimum :", np.min(sensor_data))

# Find Maximum
print("Maximum :", np.max(sensor_data))

# Calculate Standard Deviation
print("Std. Dev. :", round(np.std(sensor_data), 2))

# Find values above threshold
threshold = 28.0
high_values = sensor_data[sensor_data > threshold]

print("Values above", threshold, ":", high_values)