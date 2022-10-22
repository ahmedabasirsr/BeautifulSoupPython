from bs4 import BeautifulSoup as bs
import requests
j=1
for i in range(1,15):
    url = f"https://poslovi.infostud.com/oglasi-za-posao-it/beograd?dist=50&page={i}"
    respone = requests.get(url)
    soup = bs(respone.content,"lxml")
#lxml is analytic html, every evrement takes own analytic
#print(soup)
#print(soup.prettify())
    titl_job = soup.select("div h2")                          #30 div h2
    empol_name = soup.find_all("p",class_="uk-h4 uk-margin-remove")
    job_addr = soup.find_all("p", class_="uk-margin-remove-bottom")
    job_det = soup.find_all("p",class_="job__desc")

#,"===",(em.text).strip(),"===",(ja.text).strip() ,empol_name,job_addr,job_det ,em,ja,jd
    for tj in titl_job:
#strip() to delete space in elemente (jd.text).strip()
        print(j,"-",tj.text)
        j = j+1







