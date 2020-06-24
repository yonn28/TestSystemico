import requests
import json

response = requests.get('https://randomuser.me/api/?results=100')

data = response.json()
results = data.get('results')

male = []
female = []

for info in results:
    if(info.get('gender') == 'male'):
        male.append(info)
    else:
        female.append(info)

def get_age(elem):
    return elem['dob']['age']

def get_email(elem):
    return elem['email']


male.sort(key=get_age)
print(male, end='\n\n')


female.sort(key=get_email,reverse=True)
print(female, end='\n\n')

