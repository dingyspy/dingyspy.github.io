import json;
import os;
import pip;

try:
    __import__('requests')
except ImportError:
    pip.main(['install', 'requests'])

import requests

def _return(text):
	sn_file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'return.txt'), 'w')
	sn_file.write(text)
	sn_file.close()

	print('file write', text)

	exit()

def return_ip():
    try: 
        response = requests.get('https://checkip.amazonaws.com') 
        return response.text
    except requests.RequestException as e: 
        print(f"Error: {e}") 

file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'auth.txt'), 'r+')
file_read = file.read()

activation_code = file_read.split()[0]
apikey = file_read.split()[1]
apitoken = file_read.split()[2]

file.close()

main_id = '6735327a717d21db02522478'
archive_id = '67353294d163f6af8e4ba72a'

url = "https://api.trello.com/"

headers = {
	"Accept": "application/json"
}

query = {
	'key': apikey,
	'token': apitoken,
}

response = requests.request("GET", url + f'1/search?modelTypes=cards&query=name:"{activation_code}"' + main_id, headers=headers, params=query)
if response.status_code != 200:
	print('err')

_activation_code = json.loads(response.text)['cards'][0]['name']
user = json.loads(response.text)['cards'][0]['desc'].split('\n')[0]
ip = json.loads(response.text)['cards'][0]['desc'].split('\n')[1]
id = json.loads(response.text)['cards'][0]['id']

##

if _activation_code == activation_code:
	print('correct code')

	if ip != 'null':
		print(f'{ip}{return_ip()}')
		if ip == return_ip():
			_return('success')
		else:
			_return('used')
	elif ip == 'null':
		new_query = query
		new_query['desc'] = user + '\n' + return_ip()

		response = requests.request("PUT", url + '1/cards/' + id, headers=headers, params=new_query)
		if response.status_code != 200:
			_return('none')

		_return('success')

print('incorrect code fail')