import matplotlib.pyplot as plt

languages = ['Python', 'Java', 'C++', 'JavaScript']
students = [40, 25, 20, 15]

plt.pie(
    students,
    labels=languages,
    autopct='%1.1f%%', #<<<<<<<<<<<<<<<<
    wedgeprops={'width': 0.4}
)

plt.title("Programming Language Preferences")

plt.show()

plt.savefig("mychart.png")