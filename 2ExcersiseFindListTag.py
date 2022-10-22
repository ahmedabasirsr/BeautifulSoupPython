from bs4 import BeautifulSoup as bs
import requests

url = "https://smacoding369.github.io/bss/"
respon = requests.get(url)
soup = bs(respon.content,"lxml")
#print(soup.prettify())
headres1 = soup.find_all("h1")
for i in range(len(headres1)):
    print( headres1[i].string )

