import matplotlib.pyplot as plt

student = ['A','B','C','D','E','F']
marks = [45,56,67,78,89,51]

plt.scatter(student,marks,color = 'red',label = 'marks')

plt.title("Relation-Ship Between Student and Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.legend()
plt.grid(True)

plt.show()