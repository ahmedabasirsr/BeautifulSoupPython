from bs4 import BeautifulSoup as bs
import requests

r = requests.get("https://poslovi.infostud.com/oglasi-za-posao-it/beograd?dist=50&esource=homepage")
# r variabl takes withe requests content from web sit ==> but it is not readble
soup = bs(r.content,"html.parser")

#print(soup.prettify())
"""
name_empl = soup.select("h2") #30
for e in name_empl:
    print(e.text)

links_class_ul = soup.select("img.lazy-load-image") #37
print(len(links_class_ul))

links_class_ul = soup.select("p.uk-margin-remove-bottom") #30
print(len(links_class_ul))

para_id = soup.select("p.job__desc") #19
print(len(para_id))
"""

