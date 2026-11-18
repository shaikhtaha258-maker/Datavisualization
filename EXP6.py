#Title: Write a program to create scatter plots and
#  bubble charts to analyze relationships between variables.


import matplotlib.pyplot as plt

# Sample Data
study_hours = [1, 2, 3, 4, 5, 6]
marks = [35, 45, 55, 65, 75, 90]

# Scatter Plot
plt.scatter(study_hours, marks, color='blue',marker='o', label='Students')

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.legend()
plt.grid()
plt.show()

# Bubble Chart
bubble_size = [100, 200, 300, 400, 500, 600]

plt.scatter(study_hours, marks, s=bubble_size,
            color='green', alpha=0.5, label='Students')

plt.title("Bubble Chart")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.legend()
plt.grid()
plt.show()
