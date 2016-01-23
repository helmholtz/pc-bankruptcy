import pandas as pd

data = pd.read_csv('data.csv', dtype={'zipcode': str})

#Convert amounts to numeric values
data['amount'] = data['amount'].str[1:].str.replace(",","")
data['amount'] = pd.to_numeric(data['amount'], errors='coerce')

#Manually add first two claims
claim1 = {'name': 'A James Foxworthy',
         'zipcode': '94118',
         'amount': 469.0}
claim2 = {'name': 'A Woodson Hogge',
         'zipcode': '53562',
         'amount': 949.0}

new_data = pd.DataFrame([claim1,claim2])

data.append(new_data, ignore_index=True)

data.to_csv('cleaned_data.csv', index=False)




