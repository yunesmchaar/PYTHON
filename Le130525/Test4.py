import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\Yunes\PycharmProjects\TestDeCours\Le130525\archive\athlete_events.csv')
data = data.drop(['Height', 'Weight', 'NOC', 'Games', 'Year', 'Season', 'City', 'Event', 'Medal'], axis=1)
print(data.head())
data.info()

print(data.describe())

data['Age'].plot.hist(bins=30, edgecolor='black', figsize=(10, 6))
plt.title('Distribution of Athlete Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
