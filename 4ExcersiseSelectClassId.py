from bs4 import BeautifulSoup as bs
import requests

r = requests.get("https://smacoding369.github.io/bss/")
# r variabl takes withe requests content from web sit ==> but it is not readble
soup = bs(r.content,"html.parser")

print(soup.prettify())

links_class_il = soup.select("il.social a")
#print(links_class_il)
links_class_ul = soup.select("ul.socials a")
#print(links_class_ul)
links_class_ul = soup.select("ul.facts li")
#print(links_class_ul) id="para_id"
para_id = soup.select("p#para_id")
#print(para_id)
div_class_a = soup.select("div.block a")
#print(div_class_a)