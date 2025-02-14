import pandas as pd

data = {
    'Object':['машина','кукла','погремушка','самолёт', 'лопата', 'ведро'],
    'Count':[3, 5, 20, 7, 15, 8],
    'Cost':[200, 345, 753, 234, 56, 78]
}

data_fr = pd.DataFrame(data)
print(data_fr)
print()
slice = data_fr['Count']
print(slice)
print()
data_fr['Data'] = ['20.02.2025', '15.03.2024', '18.10.2022', '17.05.2024', '18.11.2020', '19.07.2024']
print(data_fr)
print()
data_fr.drop(5, inplace=True)
print(data_fr)
print()
data_fr['Total'] = data_fr['Count'] * data_fr['Cost']
print(data_fr)
print()