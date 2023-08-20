# data-visualization-in-python

# Line Charts
import matplotlib.pyplot as plt
import seaborn as sns

yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]
plt.plot(yield_apples)

# data-visualization-in-python

# Line Charts
import matplotlib.pyplot as plt
import seaborn as sns

yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]
plt.plot(yield_apples)

#sing Seaborn
sns.set_style("whitegrid")
plt.plot(years, apples, marker = 'x')
plt.plot(years, oranges, marker = 'o')

plt.xlabel('Years')
plt.ylabel('Yield(tons per hectare)')

plt.title("Crop Yields in Kanto")
plt.legend(['Apples', 'Oranges'])

#Bar Graphs
years = range(2000, 2006)
apples = [0.35, 0.6, 0.9, 0.8, 0.65, 0.8]
oranges = [0.4, 0.8, 0.9, 0.7, 0.6, 0.8]

plt.bar(years, oranges)
plt.xlabel('years')
plt.ylabel('Yield(tons per hectare)')
plt.title("Crop Yields in Kanto") 
plt.show()

sns.boxplot(x=tips["total_bill"],orient="h")