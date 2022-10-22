from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd
url = "https://smacoding369.github.io/bss/"
r = requests.get(url)
# r variabl takes withe requests content from web sit ==> but it is not readble
soup = bs(r.content,"html.parser")
#print(soup.find("body").find("table").find_all("th")) #1 way with find_all
#print(soup.find("body").select("table.ball tr th")) #2 way with select class ball

tab_head_colum = soup.find("body").find("table").find_all("th")
lis_tab_head_tex = [t.string for t in tab_head_colum]
#creat list of header table in text format
ltht = len(lis_tab_head_tex)
print(lis_tab_head_tex)

tab_dat_row = soup.find("body").select("table.ball tr td")
#print(tab_dat_row)
lis_tab_row_tex = [t.string for t in tab_dat_row]
#creat list in format text
len_lis_tab_tex = len(lis_tab_row_tex)
#print(lis_tab_row_tex,len_lis_tab_tex)

sub_lis_tex = [lis_tab_row_tex[x:x+3] for x in range(0,len_lis_tab_tex,3)]
#create sublists in list (list_tab_row_tex)
sub_lis_tex[0]=list()
# add empty list in 0 position because pandas requires it

#print(tab_head_colum)
#print(sub_lis_tex)
df = pd.DataFrame(sub_lis_tex,columns=lis_tab_head_tex)
# create table with pandas where rows are sub_lis_tex(sublists)
#and columns are list(lis_tab_head_tex)
print(df,"\n")
df1 = df.drop(0)
# delte row 0 ==> none
print(df1,"\n")
df2 = df.drop([0, 3])
print(df2)