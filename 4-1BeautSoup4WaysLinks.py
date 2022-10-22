from bs4 import BeautifulSoup as bs
import requests
import re

r = requests.get("https://poslovi.infostud.com/oglasi-za-posao-it/beograd?dist=50&page=1")
# r variabl takes withe requests content from web sit ==> but it is not readble
soup = bs(r.content,"lxml")

"""
links = soup.find_all("a") #168
print(links[10].attrs)
print(links[10].attrs["href"])
for link in links:
    if "href" and "onclick" and "target" in link.attrs  :
        print(link.attrs)
        print(link.attrs["href"])
"""
# first tag h2
#print(soup.h2.text)
links = soup.find_all("h2") #30
#print(len(links))
for l in links:
    atag = l.find("a")
    print(l.text)
    print(atag["href"])


"""
#print(soup) socials ==> 2 way
socials_links = [link["href"] for link in links]
print(socials_links)

for link in links:
    print(link["href"])
#print(soup) socials ==> 3 way
ulist = soup.find("ul",attrs={"class":"socials"})
links = ulist.find_all("a")
socials_links = [link["href"] for link in links]
print(socials_links)

#print(soup) socials ==> 4 way
links = soup.select("il.social a")
socials_links = [link["href"] for link in links]
print(socials_links)
"""