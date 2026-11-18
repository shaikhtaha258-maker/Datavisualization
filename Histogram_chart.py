import matplotlib.pyplot as plt

marks = [35, 40, 45, 50, 55, 60, 65, 70,
         75, 80, 85, 90, 95, 55, 65, 75]

plt.hist(marks)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()