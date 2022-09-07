import requests
import json
import time

response = requests.get('https://jsonplaceholder.typicode.com/users/3')
#print(response.status_code)
#print(response.json())
output = response.json()

print(type(output))
print(output)