from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd
url = "https://smacoding369.github.io/bss/"
r = requests.get(url)
# r variabl takes withe requests content from web sit ==> but it is not readble
soup = bs(r.content,"html.parser")

images = soup.select("div.ph1 img")
# list for images from div(ph1 is class from div)
#print(images)
all_images = images[0]["src"]
# frist element in list images and has src
print(all_images)
all_images = images[1]["src"]
print(all_images)
full_url = url + all_images
print(full_url)
img_data = requests.get(full_url).content
# variavle takes content from full adreess site
#print(img_data)
with open("sma coding.png","wb") as h:
    h.write(img_data)
with open("logo.png","wb") as h:
    h.write(img_data)