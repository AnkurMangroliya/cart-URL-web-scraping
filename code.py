import pandas as pd
import requests
from bs4 import BeautifulSoup

df = pd.read_excel('Book1.xlsx')

base_url=[]
base_w=[]
a = int(input("Enter starting limit of page : "))
b = int(input("Enter ending limit of page : "))

for i in range(a,b):
    url = df['urls'][i]
    urls = 'https://'+str(url)+'/cart'

    try:
        r = requests.get(urls)
        t = r.status_code
        if t==200 :
            w='YES'
        else:
            w=''
    except:
        w=''
    base_url.append(url)
    base_w.append(w)

    print("page number : ",i)

new_df = pd.DataFrame(base_w,base_url)
new_df.to_csv('total_new_data.csv')
