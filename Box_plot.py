import matplotlib.pyplot as plt

marks = [10, 20, 30, 40, 50, 60, 70, 80, 100]

plt.boxplot(marks)

# plt.text(1.05, 25, "Q1")
# plt.text(1.05, 50, "Q2")
# plt.text(1.05, 75, "Q3")

plt.title("Box Plot")
plt.ylabel("Marks")

plt.show()