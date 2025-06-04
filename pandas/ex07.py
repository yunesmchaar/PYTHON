import pandas as pd

df=pd.read_csv(r"C:\Users\Yunes\PycharmProjects\TestDeCours\PYTHON\pandas\DATA.csv")
print(df)
print(df.columns)
df.loc[df['Day']==93].head(10)
print(df.loc[df['TodayDeath']==5].head(10))

print(df.loc[df['TodayDeath']==5].head(20))
print(df['TodayDeath'].mode())
print("******************************************************************************************")
print(df['TodayDeath'].value_counts())
