#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data = pd.read_csv("temp_anomalies.csv", skiprows=4, delimiter="\t")
data[['Year', 'TempAnomaly']] = data['Year,Anomaly'].str.split(',', expand=True)
def calculate_yearly_avg(row):
    values = row['TempAnomaly'].split('-')
    values = [float(val) if val else None for val in values]
    values = [val for val in values if val is not None]
    return np.nanmean(values) if values else None
data['YearlyAvg'] = data.apply(calculate_yearly_avg, axis=1)
yearly_avg = data.groupby('Year')['YearlyAvg'].mean()
plt.figure(figsize=(12, 6))
plt.plot(yearly_avg.index, yearly_avg.values, color='orange', marker='o', linestyle='-')
plt.gca().set_facecolor('none')
V = yearly_avg.index.values.reshape(-1, 1)
K = yearly_avg.values
ney = LinearRegression()
ney.fit(V, K)
trendline = ney.predict(V)
plt.plot(yearly_avg.index, trendline, color='green', linestyle=':')
plt.title("Global Temperature Anomalies (1850-2023)")
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")
plt.grid(False)
plt.show()