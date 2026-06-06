
import requests
from bs4 import BeautifulSoup
import time 
import pandas as pd



finalboss=[]
for page in range(1,11):
    url=f"https://quotes.toscrape.com/page/{page}/"
    response=requests.get(url)
    soul=BeautifulSoup(response.text,"html.parser")

    segment=soul.find_all("div",class_="quote")

    for i in segment:
        line=i.find("span",class_="text").text
        auth=i.find("small",class_="author").text
        tangs=i.find_all("a",class_="tag")
        new=[]
        for ta in tangs:
            new.append(ta.text)

           

        finalboss.append({"Quote":line,"Author":auth,"Tags":(",".join(new)),"Page":page}) 

    
    print(f"Page {page} done — {len(finalboss)} quotes  collected ")
    time.sleep(1)



df=pd.DataFrame(finalboss)
df.to_csv("quotes_full.csv",index=False)       
