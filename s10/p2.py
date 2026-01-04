from bs4 import BeautifulSoup

import requests
url="https://www.amazon.com/"
headers={
    "User-Agent": "Mozilla/5.0"
    }

response=requests.get(url,headers=headers)
print("status code :",response.status_code)
