python
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load the dataset
file_path = 'Traffic Accident-v3.0 (values) Al Dafrah 2022-2025.xlsx'
data = pd.read_excel(file_path)

# Convert date column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Analyze the number of accidents per year
data['Year'] = data['Date'].dt.year
accidents_per_year = data['Year'].value_counts().sort_index()

# Plot number of accidents per year
plt.figure(figsize=(10, 6))
accidents_per_year.plot(kind='bar', color='skyblue')
plt.title('Number of Traffic Accidents per Year')
plt.xlabel('Year')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Analyze accidents based on weather conditions
weather_accidents = data['Weather Conditions'].value_counts()

# Plot accidents based on weather conditions
plt.figure(figsize=(10, 6))
weather_accidents.plot(kind='bar', color='orange')
plt.title('Number of Accidents Based on Weather Conditions')
plt.xlabel('Weather Condition')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Predict peak accident times
peak_hours = data['Date'].dt.hour.value_counts().sort_index()

# Plot peak accident times
plt.figure(figsize=(10, 6))
peak_hours.plot(kind='line', marker='o', color='red')
plt.title('Peak Hours for Traffic Accidents')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Accidents')
plt.grid(True)
plt.tight_layout()
plt.show()
