import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample weather data (for example purposes)
data = {
    'Date': pd.date_range(start='2023-01-01', periods=7),
    'Temperature': [22, 21, 19, 23, 20, 18, 17],
    'Humidity': [78, 75, 80, 70, 77, 82, 85]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate basic statistics
mean_temp = np.mean(df['Temperature'])
mean_humidity = np.mean(df['Humidity'])

print("Average Temperature:", mean_temp)
print("Average Humidity:", mean_humidity)

# Plot temperature and humidity
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Temperature'], marker='o', label='Temperature (°C)')
plt.plot(df['Date'], df['Humidity'], marker='x', label='Humidity (%)')
plt.title('Weather Data Analysis')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()
