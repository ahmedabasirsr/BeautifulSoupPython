from bs4 import BeautifulSoup as bs
import requests
import re

r = requests.get("https://smacoding369.github.io/bss/")
# r variabl takes withe requests content from web sit ==> but it is not readble
soup = bs(r.content,"html.parser")

parg_span = soup.select("p span")
#find every paragraphs whose have span
#print(parg_span)
parg_span1 = soup.select("h2 ~ p")
#print(parg_span1)
parags = soup.select("body > p")
#print(parags)
#for par in parags:
    #select only paragraph which has span
 #   print(par.select("span"))

header1 = soup.find("h1")
print(header1.string)
header2 = soup.find("h2")
print(header2.text)
par = soup.find("p")
print(par.get_text())