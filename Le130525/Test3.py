import pandas as pd

# Use raw string (r'') or forward slashes
data = pd.read_csv(r'C:\Users\Yunes\PycharmProjects\TestDeCours\Le130525\archive\athlete_events.csv')
print(data.head())  # Show first 5 rows
data.info()      # Column types and missing values
data.describe()  # Summary statistics
import matplotlib.pyplot as plt
data['Age'].plot.hist()
plt.show()