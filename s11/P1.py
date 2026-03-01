import requests

url="https://jsonplaceholder.typicode.com/users"

response=requests.get(url)
data=response.json()
#print(data)
print(data[0]["name"])
for user in data:
    print('name :',user["name"]," /email :",user["email"])

