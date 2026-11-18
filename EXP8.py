# Write a program to visualize 
# correlation matrices using heatmaps.


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample Dataset
data = {
    'Study Hours': [2, 3, 4, 5, 6],
    'Marks': [40, 50, 60, 70, 80],
    'Sleep Hours': [8, 7, 6, 5, 4]
}

df = pd.DataFrame(data)

# Calculate Correlation Matrix
corr = df.corr()

# Create Heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm')

plt.title("Correlation Matrix Heatmap")
plt.show()
