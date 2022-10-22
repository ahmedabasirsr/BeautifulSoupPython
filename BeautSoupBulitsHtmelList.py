from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd

r = requests.get("https://smacoding369.github.io/bss/")
# r variabl takes withe requests content from web sit ==> but it is not readble
soup = bs(r.content,"html.parser")

facts = soup.select("ul.facts li")
#select bulits text or list htmel
f_w_is = [fact.find(string =re.compile("is")) for fact in facts]
#print(f_w_is)
f_w_is = [fact.find_parent().get_text() for fact in f_w_is if fact]
#This line withot word none in list  
print(f_w_is)