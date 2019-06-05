import pandas as pd
import os
import matplotlib.pyplot as plt

bosdata = pd.read_csv('housing.data',
                 sep='\s+',
                 header=None)

os.makedirs('plots', exist_ok=True)

bosdata.columns = ['CRIME', 'ZN', 'INDUS', 'CHASRIVER', 'NOX', 'ROOM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'BLK', 'LSTAT', 'MEDV']

print(bosdata.describe().to_string())
print(len(bosdata))


#plotting 1 column line chart
plt.plot(bosdata['CRIME'], color='red')
plt.title('Crime rate')
plt.xlabel('index')
plt.ylabel('crime rate')
plt.savefig(f'plots/crime_rate2.png', format='png')
plt.close()


#plotting 2 features

plt.scatter(bosdata['AGE'], bosdata['MEDV'], color='b')
plt.scatter(bosdata['BLK'], bosdata['MEDV'], color='g')
plt.title('Age and black to median price of house')
plt.xlabel('median price')
plt.ylabel('age and black')
plt.savefig(f'plots/factor_to_price.png', format='png')
plt.close()


