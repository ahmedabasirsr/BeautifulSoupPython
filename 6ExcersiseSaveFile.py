from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd
url = "https://smacoding369.github.io/bss/"
r = requests.get(url)
# r variabl takes withe requests content from web sit ==> but it is not readble
soup = bs(r.content,"html.parser")

images = soup.select("div.ph1 img")
# select div with class ph1 and tag img
l = len(images)
for i in range(l):
    url_image = images[i]["src"]
    # url adress image
    image =f"image{i}.png"
    # name of image
    url_images =requests.get(url + url_image).content
    with open(image,"wb") as f:
        f.write(url_images)
    
