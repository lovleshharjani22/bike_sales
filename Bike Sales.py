import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import math
bikes = pd.read_csv(r"C:\Users\lovlesh.n\Downloads\hour.csv")
bikes_prep = bikes.copy()
bikes_prep = bikes_prep.drop(['index', 'date', 'casual', 'registered'], axis=1)
#basic checks
bikes_prep.isnull().sum()
# Histogram
bikes_prep.hist(rwidth=0.9)
plt.tight_layout()
# data visualisation
plt.subplot(2, 2, 1)
plt.title('Temperature Vs Demand')
plt.scatter(bikes_prep['temp'], bikes_prep['demand'], s=2, c='g')

plt.subplot(2, 2, 2)
plt.title('atemp Vs Demand')
plt.scatter(bikes_prep['atemp'], bikes_prep['demand'], s=2, c='b')

plt.subplot(2, 2, 3)
plt.title('Humidity Vs Demand')
plt.scatter(bikes_prep['humidity'], bikes_prep['demand'], s=2, c='r')


plt.subplot(2, 2, 4)
plt.title('Windspeed Vs Demand')
plt.scatter(bikes_prep['windspeed'], bikes_prep['demand'], s=2, c='c')
plt.tight_layout()
colors = ['g', 'r', 'b', 'm']
plt.subplot(3, 3, 1)
plt.title('Average Demand per Year')
cat_list = bikes_prep['year'].unique()
cat_average = bikes_prep.groupby('year').mean()['demand']
plt.bar(cat_list, cat_average, color=colors)

plt.subplot(3, 3, 2)
plt.title('Average Demand per Month')
cat_list = bikes_prep['month'].unique()
cat_average = bikes_prep.groupby('month').mean()['demand']
plt.bar(cat_list, cat_average, color=colors)

plt.subplot(3, 3, 3)
plt.title('Average Demand per Hour')
cat_list = bikes_prep['hour'].unique()
cat_average = bikes_prep.groupby('hour').mean()['demand']
plt.bar(cat_list, cat_average, color=colors)

plt.subplot(3, 3, 4)
plt.title('Average Demand per Holiday')
cat_list = bikes_prep['holiday'].unique()
cat_average = bikes_prep.groupby('holiday').mean()['demand']
plt.bar(cat_list, cat_average, color=colors)

plt.subplot(3, 3, 5)
plt.title('Average Demand per Weekday')
cat_list = bikes_prep['weekday'].unique()
cat_average = bikes_prep.groupby('weekday').mean()['demand']
plt.bar(cat_list, cat_average, color=colors)

plt.subplot(3, 3, 6)
plt.title('Average Demand per Workingday')
cat_list = bikes_prep['workingday'].unique()
cat_average = bikes_prep.groupby('workingday').mean()['demand']
plt.bar(cat_list, cat_average, color=colors)
plt.tight_layout()

# check for outliers
print(bikes_prep['demand'].describe())
print(bikes_prep['demand'].quantile([0.05, 0.1, 0.15, 0.9, 0.95, 0.99]))

# check multiple correlation coefficient
correlation = bikes_prep[['temp', 'atemp', 'humidity', 'windspeed', 'demand']].corr()
bikes_prep = bikes_prep.drop(['atemp', 'weekday', 'year', 'windspeed', 'workingday'], axis=1)
#check the autocorelation
df1 = pd.to_numeric(bikes_prep['demand'], downcast = 'float')
plt.acorr(df1, maxlags=12)
df1 = bikes_prep['demand']
df2 = np.log(df1)
plt.figure()
df1.hist(rwidth=0.9, bins=20)
plt.figure()
df2.hist(rwidth=0.9, bins=20)
bikes_prep['demand'] = np.log(bikes_prep['demand'])