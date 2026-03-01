import requests

url="https://jsonplaceholder.typicode.com/posts"

x =  {
    "userId": 11,
    "id": 1001,
    "title": "laboriosam dolor 123",
    "body": "123doloremque ex facilis sit sint culpa\nsoluta assumenda eligendi non ut eius\nsequi ducimus vel quasi\nveritatis est dolores"
  }
response = requests.post(url, json=x) 
print(response.status_code)
print(response.json)