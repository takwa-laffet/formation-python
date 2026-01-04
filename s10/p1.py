from bs4 import BeautifulSoup
import requests
url="https://books.toscrape.com/"

response=requests.get(url)
if response.status_code ==200:
    print("OK")
else:
    print("not ok")
print("status code :",response.status_code)
#print(response.text)
#soup
soup=BeautifulSoup(response.text,"html.parser")
#print(soup)
books=soup.find_all("article",class_="product_pod")
#print(books)
for book in books:
    title=book.h3.a["title"]
    prix=book.find("p",class_="price_color").text
   # print("title :",title)
    #print(" price:",prix)