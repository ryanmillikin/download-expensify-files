import pandas as pd
import requests

list_name = 'Expensify_Receipts.csv'

data = pd.read_csv('Expensify_Receipts.csv',
	dtype = {'Receipt':str, 'file_name':str, 'downloaded':bool})

#print(data)

#data.info()

data.dropna(
	how='all',
	subset=['Receipt'],
	inplace=True)

data = data.loc[(data['downloaded']==False)]



for file_url, file_name in zip(data['Receipt'], data['file_name']):

	file_object = requests.get(file_url)

	#Change path back to /files/ before running
	with open('/Users/ryan.millikin/Desktop/Expensify_Receipts/files/'+ file_name, 'wb') as local_file:
	    local_file.write(file_object.content)

