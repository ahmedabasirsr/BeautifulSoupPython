from bs4 import BeautifulSoup as bs
import requests
import re

r = requests.get("https://smacoding369.github.io/bss/")
# r variabl takes withe requests content from web sit ==> but it is not readble
soup = bs(r.content,"html.parser")
#parg = soup.find_all("p",attrs={"id":"para_id"})
# find only paragraphs whose have id: para_id
#print(parg)
word = soup.find_all("h1",string=re.compile("النص"))
# find only one word in header 1
#print(word)
word1 = soup.find_all("p",string=re.compile("is"))
# find only word is in any paragraphs
print(word1)
word2 = soup.find_all("span",string=re.compile("in"))
# find only word(in)in tag span
print(word2)