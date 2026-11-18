#Title: Write a program to plot histograms 
# and pie charts for understanding 
# data distribution and proportions.

import matplotlib.pyplot as plt

marks = [45,56,67,78,89,67,56,23,54]
plt.hist(marks,bins = 5,color = 'skyblue',edgecolor ='black')
plt.title("Distribution of marks")
plt.xlabel('marks')
plt.ylabel('frecuency')
plt.show()

#--------------------------------------------------

languages = ['python','java','C++','C']
students = [45,56,78,23]

plt.pie(students,labels = languages,autopct='%1.1f%%')
plt.title("Subject wise student")
plt.show()
