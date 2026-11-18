#Write a program to visualize multivariate data 
# using pair plots and facet grids.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'branch':['CSE','IT','AIDS','CIVIL','MECH','CSE'],
    'gender':['M','F','M','F','M','F'],
    'marks':[76,78,89,90,98,87],
    'attendance':[70,80,77,87,90,79]
}
df = pd.DataFrame(data)

#Pair plot
sns.pairplot(df,vars=['marks','attendance'],hue = 'branch')
# plt.show()

#Facet grid

g = sns.FacetGrid(df,col='branch')
g.map(sns.histplot,'marks')
g.set_axis_labels('marks','count')
g.fig.suptitle('Marks distributiob by branch')
plt.show()


