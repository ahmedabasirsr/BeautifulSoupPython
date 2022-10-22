from bs4 import BeautifulSoup as bs
import requests
import re

r = requests.get("https://smacoding369.github.io/bss/")
# r variabl takes withe requests content from web sit ==> but it is not readble
soup = bs(r.content,"html.parser")
#print(soup) socials ==> 1 way
links = soup.select("ul.socials a")

#print(soup) socials ==> 2 way
socials_links = [link["href"] for link in links]
print(socials_links)
"""
for link in links:
    print(link["href"])
#print(soup) socials ==> 3 way
ulist = soup.find("ul",attrs={"class":"socials"})
links = ulist.find_all("a")
socials_links = [link["href"] for link in links]
print(socials_links)
"""
#print(soup) socials ==> 4 way
links = soup.select("il.social a")
socials_links = [link["href"] for link in links]
print(socials_links)