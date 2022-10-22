from bs4 import BeautifulSoup as bs
import requests
import re

r = requests.get("https://smacoding369.github.io/bss/")
# r variabl takes withe requests content from web sit ==> but it is not readble
soup = bs(r.content,"lxml")

link = soup.find("a")
print(link["href"])

#para = soup.select("p#para_id")
#print((para))
#print(soup.body.h1.string)
