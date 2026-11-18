# Write a program to perform time-series visualization 
# using line plots and trend analysis.


import pandas as pd
import matplotlib.pyplot as plt

# Sample Time-Series Data
data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May',
              'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
    'sales': [100, 120, 110, 140, 150,
              160, 155, 180, 190, 200]
}

df = pd.DataFrame(data)

# Calculate Trend using Moving Average
df['trend'] = df['sales'].rolling(window = 3).mean()

# Line Plot
plt.figure(figsize = (8,5))
plt.plot(df['month'],df['sales'],marker = 'o',label = 'Actual sales')
plt.plot(df['month'],df['trend'],color = 'red',label ='trend')

plt.title('time-series visualization')
plt.xlabel('Months')
plt.ylabel('Sales')

plt.legend()
plt.grid(True)

plt.show()
