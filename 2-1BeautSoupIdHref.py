import attrs
from bs4 import BeautifulSoup as bs
import requests
import re

r = requests.get("https://poslovi.infostud.com/")
# r variabl takes withe requests content from web sit ==> but it is not readble
soup = bs(r.content,"lxml")
links = soup.find_all("a")  #150

"""
print(len(links))
i=1
for l in links:
    if l.string !=None:
        print(i,(l.string).strip())
        i+=1


para = soup.find("p",class_="uk-text-muted uk-text-small uk-text-break uk-margin-remove")
print(para)

h2 = soup.find_all("h2") #4
for h in h2:
    print(h.text)
    """

h3 = soup.find_all("h3") #13
for h in h3:
    print(h.text)