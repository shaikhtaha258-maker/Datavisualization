#Title: Write a program to visualize numerical data 
# using Line Charts and Bar Charts with proper titles, 
# labels, and legends.


import matplotlib.pyplot as plt

months = ['January','February','March','April','may','June']
sales = [50, 65, 80, 45, 78, 93]

#Line chart

plt.plot(months,sales,marker = 'o',label = 'sales')
plt.title('Monthly Sales')
plt.xlabel('Months')
plt.ylabel('sales')

plt.legend()
plt.grid(True)
plt.show()


#Bar chart 

plt.bar(months,sales,label = 'sales')
plt.title('Monthly sales')
plt.xlabel('Months')
plt.ylabel('sales')

plt.legend()
plt.show()