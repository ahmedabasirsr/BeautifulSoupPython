from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd
url = "https://smacoding369.github.io/bss/"
r = requests.get(url)
# r variabl takes withe requests content from web sit ==> but it is not readble
soup = bs(r.content,"html.parser")

files = soup.select("div.block a")
# select files in html
relative_files = [f["href"] for f in files]
#print(relative_files)
for f in relative_files:
    full_url = url + f
    page = requests.get(full_url)
    bs_page = bs(page.content)
    secret_word_element = bs_page.find("p",attrs={"id":"secret-word"})
    secret_word = secret_word_element.string
    print(secret_word)
