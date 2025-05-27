import pandas as pd
import matplotlib.pyplot as plt

datas= {
    'nom':["A","B","C","D","E","F"],
     'Age':["18","20","29","33","29","40"],
    'CNI':["AB0001","AC000001","AX0001","AV0002","AK000001","AZ10000"]
}
mydatas=pd.DataFrame(datas)

print(f"columns:{mydatas.columns}")
print(f"Header:{mydatas.head()}")
print(f"Shape:{mydatas.shape}")
print(f"descripe:{mydatas.describe()}")
print(f"****************************************************************************")
mydatas.to_csv('InfoDatas.csv',index=True)
mydatas.drop(['Age'],axis=1,inplace=True)
print(mydatas)
mydatas.drop([5],axis=0,inplace=True)
print(mydatas)
mydatas['AGE']=[20,28,17,35,27]
print(mydatas)
mydatas.loc[5]=['F','AF0002','45']
print(mydatas)

#plt.plot(mydatas['nom'],mydatas['AGE'],'o:r',mec='k',mfc='r',label="Data")
plt.pie(mydatas['AGE'],labels=mydatas['nom'],autopct='%1.1f%%')
plt.title("Diagramme de Data")
plt.xlabel("AXE:X")
plt.ylabel("AXE:Y")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
