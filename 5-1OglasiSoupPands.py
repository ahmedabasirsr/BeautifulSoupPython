from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

#List of title job
ljob_title = []
l_of_job_links = []
l_job_adress = []
l_date = []
for i in range(1,20):
    #respon of regusts(content site)
    r = requests.get(f"https://poslovi.infostud.com/oglasi-za-posao-it/beograd?dist=50&page=19")
    #creat object of beatufulsoup does access every elements on site
    soup = bs(r.content,"lxml")

    #total number of jobs
    totnum_job = soup.find("span",{"class":"uk-h4 uk-text-muted uk-margin-remove"})
    #print(totnum_job.text)


    # content of notice
    job_title = soup.find_all("h2") # 30 titles
    job_adress = soup.findAll("p", {"class": "uk-margin-remove-bottom"}) #30 Adresses
    date =soup.findAll("p", {"class": "uk-margin-remove uk-text-bold"}) # 30 dates

    #print(len(job_title_links))


    for jo,ja,d in zip(job_title,job_adress,date):
        ljob_title.append(jo.text.replace("\n","").strip())
        links_titl = jo.find("a")
        l_of_job_links.append(links_titl["href"].strip())
        l_job_adress.append(ja.text.replace("\n","").strip())
        l_date.append(d.text.replace("\n","").strip())


    note_pand = pd.DataFrame({"Job Title":ljob_title,"Job Links":l_of_job_links,
                                  "Job Adress":l_job_adress,"Date Note":l_date})

#print(note_pand)
note_pand.to_csv("note.csv")


