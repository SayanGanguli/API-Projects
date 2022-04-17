import json
import jsonpath
import requests

url = "https://reqres.in/api/users/2"

with open('..//UpdateUser.json', 'r') as user:
    json_request = json.load(user)

#print(json_request)
response = requests.put(url,json_request)

response_json = json.loads(response.text)
print(response_json)
updated = jsonpath.jsonpath(response_json,'updatedAt')
print (updated)