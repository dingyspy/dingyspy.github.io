import requests
import json
import socket

name = 'acnew'


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

print('Getting cards...')
response = requests.request("GET", url + f'1/search?modelTypes=cards&query=name:"{name}"' + main_id, headers=headers, params=query)

user = json.loads(response.text)['cards'][0]['desc'].split('\n')[0]
ip = json.loads(response.text)['cards'][0]['desc'].split('\n')[1]
id = json.loads(response.text)['cards'][0]['id']

##

if ip != 'null':
    pass # write to txt file saying something like "none" for godot
    print('ip already exists')
    exit()

new_query = query
new_query['desc'] = user + '\n' + socket.gethostbyname(socket.gethostname())

response = requests.request("PUT", url + '1/cards/' + id, headers=headers, params=new_query)

# write to txt file saying "success" for godot