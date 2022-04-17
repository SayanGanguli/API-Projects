import json

import jsonpath
import requests

url = "https://reqres.in/api/users"

with open('..//NewUser.json', 'r') as user:
    json_request = json.load(user)

#print(json_request)
response = requests.post(url,json_request)
print(response.content)
print(response.status_code)
print(response.text)
print(response.headers)
print(response.headers.get("Content-Length"))

response_json = json.loads(response.text)
id = jsonpath.jsonpath(response_json,'id')
print (id)