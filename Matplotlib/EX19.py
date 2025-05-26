import pandas as pd

myClient={
    'noms':["youness","mchaar","abdo","salahden","achraf"],
    'Facture':["N001","N002","N003","N004","N005"],
    'Prix httc':["5000DH","1000DH","2000DH","10000DH","3000DH"]
}
mytabClient = pd.DataFrame(myClient)
#myEtudiant = pd.DataFrame(myClass)
print(mytabClient)
mytabClient.to_csv('myFacture.csv',index=False)

#myEtudiant.to_csv('modules.csv', index=False)