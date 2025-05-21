import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas as df

data=pd.read_csv(r'C:\Users\Yunes\PycharmProjects\TestDeCours\PYTHON\cours\archive (1)\athlete_events.csv')
data['Sex']=data['Sex'].map({'F':0,'M':1})
data['Sex'].replace(['F','M'],[0,1])
data['Sex'].astype('category').cat.codes
print(data)
