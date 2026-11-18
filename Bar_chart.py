import matplotlib.pyplot as plt 

student = ['A','B','C','D','E','F']
marks = [45,56,67,78,89,90]

plt.bar(student,marks)

plt.title('Student Marks')
plt.xlabel('Student')
plt.ylabel('Marks')

plt.show()