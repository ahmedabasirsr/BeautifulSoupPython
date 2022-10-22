from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
ljob_title = []
l_of_job_links = []
l_job_adress = []
l_date = []

#scraping job title
def job_tit():
    job_title = soup.find_all("h2")
    for jo in job_title:
        ljob_title.append(jo.text.replace("\n", "").strip())
        links_titl = jo.find("a")
    return ljob_title

#scraping links notice
def job_lin():

    job_links = soup.find_all("h2")
    for jl in job_links:
        links_titl = jl.find("a")
        l_of_job_links.append(links_titl["href"].strip())
    return l_of_job_links

#scraping job adresses
def job_adr():
    job_adress = soup.findAll("p", {"class": "uk-margin-remove-bottom"})
    for ja in job_adress:
        l_job_adress.append(ja.text.replace("\n", "").strip())
    return l_job_adress

#scraping date not
def date():
    date = soup.findAll("p", {"class": "uk-margin-remove uk-text-bold"})
    for d in date:
        l_date.append(d.text.replace("\n", "").strip())
    return l_date



key_word =input("Press key word for your notice: ")
namecity =input("Enter Name city: ")
num_pages=int(input("press number of pages: "))

for i in range(1,num_pages+1):
    #respon of regusts(content site)
    r = requests.get(f"https://poslovi.infostud.com/oglasi-za-posao-{key_word}/{namecity}?dist=50&page={i}")
    #creat object of beatufulsoup does access every elements on site
    soup = bs(r.content,"lxml")


# create date frame from listes
    note_pand = pd.DataFrame({"Job Title":job_tit(),"Job Links":job_lin(),
                              "Job Adress":job_adr(),"Date Note":date()})
try:
    #Create Csv file from date frame with pakage pandas
    note_pand.to_csv("note.csv")

    #total number of jobs
    totnum_job = soup.find("span",{"class":"uk-h4 uk-text-muted uk-margin-remove"})
    print(totnum_job.string)
except:
    print("Error of number page")