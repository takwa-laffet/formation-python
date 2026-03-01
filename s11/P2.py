import requests

url="https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 2
}
response = requests.get(url, params=params) #https://jsonplaceholder.typicode.com/posts?userId=1
data = response.json()
print(data)