import pandas as pd

data = pd.read_csv('data.csv', dtype={'zipcode': str})

data=data.drop(range(0,4))  #drop first four rows

#Strip $ and , from amounts and convert to float
data['amount'] = data['amount'].str[1:].str.replace(",","").astype('float')

data.to_csv('cleaned_data.csv', index=False)




