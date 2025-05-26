import pandas as pd

cars={
    'module':["2018","2019","2020","2021","2022","2023"],
    'type':["TOYOTA","MERCIDEC","PORSH","GOLF","audi","FORD"],
    'prix':["200000DH","300000DH","5000000DH","1000000DH","1200000DH","22000000DH"]
}

mycars=pd.DataFrame(cars)
#print(mycars)
#mycars.to_csv('infoCars.csv',index=False)
#mycars.head()
#print(f"{mycars.head()}")
#print(f"{mycars.columns}")
#print(f"{mycars.shape}")
#print(f"{mycars.describe()}")
print(f"{mycars.columns}")
print(mycars.drop(['prix'],axis=1,inplace=True))
print(f"{mycars}")
print(mycars.drop([0,1],axis=0,inplace=True))
print(mycars)
print(mycars.drop([2],axis=0,inplace=True))
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(mycars)
mycars.loc[6]=['2024','TESLA']
print(mycars)
mycars['PRIX']=[10,10,20,30]
print(mycars)
