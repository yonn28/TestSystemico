import requests

response = requests.get('https://randomuser.me/api/?results=100')

print(response.json())