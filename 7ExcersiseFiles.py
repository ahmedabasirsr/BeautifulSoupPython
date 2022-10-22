from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd
url = "https://smacoding369.github.io/bss/"
r = requests.get(url)
soup = bs(r.content,"html.parser")
#print(soup.prettify())
tag_files = soup.select("div.block a")
#print(tag_files)
for i in tag_files:
    #print(i["href"])
    url1 = i["href"]
    url_full = url + url1
    page = requests.get(url_full)
    cont_pag = bs(page.content)
    #print(cont_pag)

    word_secret = cont_pag.find("p",attrs={"id":"sccret-word"}).string
    print(word_secret)
