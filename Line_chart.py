import matplotlib.pyplot as plt

months = ['January','February','March','April','may','June']
sales = [75,100,150,200,90,60]

plt.plot(months,sales,color = 'red',label = 'sales')

plt.title('MONTHLY SALES')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()

#--------------MULTI LINE--------------

# import matplotlib.pyplot as plt

# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

# company_A = [100, 150, 120, 200, 250]
# company_B = [80, 120, 160, 180, 220]

# plt.plot(months, company_A, label='Company A', marker='o')
# plt.plot(months, company_B, label='Company B', marker='s')

# plt.title("Company Sales Comparison")
# plt.xlabel("Months")
# plt.ylabel("Sales")

# plt.legend()
# plt.grid()

# plt.show()