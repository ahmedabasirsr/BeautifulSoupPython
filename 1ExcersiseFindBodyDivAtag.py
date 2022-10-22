from bs4 import BeautifulSoup as bs
import requests

url = "https://smacoding369.github.io/bss/"
respone = requests.get(url)
soup = bs(respone.content,"lxml")
#lxml is analytic html, every evrement takes own analytic
#print(soup)
#print(soup.prettify())
body = soup.find("body")
#content of body site
#print(body.h1)
# content only h1
#print(body.find_all("h1"))
# content every h1 in body
#print(body.find("div"))
# content of first div in body
#print(body.find_all("div"))
# content every div in body
divs = body.find_all("div")
print(divs[1].string)
# frist div take me text
#print(divs[2].find_all("li"))
# in div2 take me every li
#print(divs[2].find_all("li")[0])
# in div 2 take me in li 0
#print(divs[2].find_all("li")[0].find("a").string)
# in div2 take me in li0 only tag a in format text
