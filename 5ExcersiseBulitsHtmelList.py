from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd

r = requests.get("https://smacoding369.github.io/bss/")
# r variabl takes withe requests content from web sit ==> but it is not readble
soup = bs(r.content,"html.parser")
#print(soup.prettify())

facts_li = soup.select("ul.facts li")
#ll = [l for l in facts_li]
#creat list ll from facts_li==> how to creat new list in one line
#print(ll)

#print(facts_li)
f_word_of = [f.find(string = re.compile("of")) for f in facts_li]
#re helps to find element whose has word of in list facts_li
print(f_word_of)

for i in f_word_of:
    if i == None :
        f_word_of.remove(None)


print(f_word_of)

