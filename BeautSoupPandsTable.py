from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd

r = requests.get("https://smacoding369.github.io/bss/")
# r variabl takes withe requests content from web sit ==> but it is not readble
soup = bs(r.content,"html.parser")

table = soup.select("table")[0]
# select table in soup
#print(table)
columns = table.find_all("th")
# find header columns
#print(columns)
columns_names = [c.string for c in columns]
# variable to save names of header names
#print(headers_name)
table_rows = table.find_all("tr")
#variable to save rows table
#print(rows_table)
l = []
for tr in table_rows:
    td = tr.find_all("td")
    row = [str(tr.get_text()).strip() for tr in td]
    l.append(row)
#print(columns_names)
#print(l)
df = pd.DataFrame(l,columns =columns_names)
print(df)
