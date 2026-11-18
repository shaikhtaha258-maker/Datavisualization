#Write a program to generate box plots 
#and violin plots to identify spread and outliers in the marksset.

import numpy as np
import matplotlib.pyplot as plt

marks = [45, 52, 55, 58, 60, 61, 62, 64, 65, 66,
67, 68, 69, 70, 71, 72, 73, 74, 75, 76,
77, 78, 79, 80, 82, 84, 86, 88, 35, 98]
data = np.array(marks)

plt.figure(figsize=(7, 4.5))
plt.boxplot(data,label="Student Marks")
plt.title("Distribution of Student Marks - Box Plot")
plt.xlabel("Dataset")
plt.ylabel("Marks")
plt.grid(axis="y")
plt.show()

plt.figure(figsize=(7, 4.5))
plt.violinplot(data)
# plt.xticks([1], ["Student Marks"])
plt.title("Distribution of Student Marks - Violin Plot")
plt.xlabel("Dataset")

plt.ylabel("Marks")
plt.grid(axis="y")
plt.show()

Q1 = np.percentile(data, 25)
Q2 = np.percentile(data, 50)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR
outliers = data[(data < lower_limit) | (data > upper_limit)]

print("Q1 =", Q1)
print("Median =", Q2)
print("Q3 =", Q3)
print("IQR =", IQR)
print("Potential outliers =", outliers)