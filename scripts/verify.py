import requests
import json
import socket
import os

def _return(text):
	sn_file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'return.txt'), 'w')
	sn_file.write(text)
	sn_file.close()

	exit()

apikey = '58264bfd3840f26cb713df830cb35802'
apitoken = 'ATTAe4d661765247910d78f01b1de0f4d20295070c8c8bf1755a5a6b0f3ac5257707625AD8AF'

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

# main #

file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'auth.txt'), 'r+')
activation_code = file.read()

file.close()

##

response = requests.request("GET", url + f'1/search?modelTypes=cards&query=name:"{activation_code}"' + main_id, headers=headers, params=query)
if response.status_code != 200:
	print('err')

_activation_code = json.loads(response.text)['cards'][0]['name']
user = json.loads(response.text)['cards'][0]['desc'].split('\n')[0]
ip = json.loads(response.text)['cards'][0]['desc'].split('\n')[1]
id = json.loads(response.text)['cards'][0]['id']

##

if _activation_code == activation_code:
	if ip != 'null':
		if ip == socket.gethostbyname(socket.gethostname()):
			_return('success')
		else:
			_return('used')
	elif ip == 'null':
		new_query = query
		new_query['desc'] = user + '\n' + socket.gethostbyname(socket.gethostname())

		response = requests.request("PUT", url + '1/cards/' + id, headers=headers, params=new_query)
		if response.status_code != 200:
			_return('none')

		_return('success')