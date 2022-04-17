import json

import jsonpath
import requests

response = requests.get("https://reqres.in/api/users?page=2")
# print(response)
# print( response.content)
# print (response.headers)

json_response = json.loads(response.text)
#print(json_response)
pages = jsonpath.jsonpath(json_response,'total_pages')
print(pages)
assert pages[0] == 2