import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import urllib.request

Names = []
Prices = []
Descp = []



while True:

    URL1 = input("link:")

    if URL1 == URL1:

        for i in URL1[0:15]:

            r = requests.get(URL1)
            #print(r)

            soup = BeautifulSoup(r.text,"lxml")
            #print(soup)

            np = soup.find("a", class_="l1j9v1wn c1ytbx3a dir dir-ltr").get("href")
            #print(np)
            cnp = "https://www.airbnb.co.in" + np
            #print(cnp)

            url = cnp
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "lxml")

            names = soup.find_all("div",class_="t1jojoys dir dir-ltr")
                #print(names)

            for i in names:
                n = i.text
                Names.append(n)

            #print(len(Names))

            prices = soup.find_all("div", class_="_1jo4hgw" )

            for i in prices:
                n = i.text
                Prices.append(n)

            #print(len(Prices))

            descp = soup.find_all("div",class_="g1qv1ctd cb4nyux dir dir-ltr")

            for i in descp:
                n = i.text
                Descp.append(n)

            #print(len(Descp))



    df = pd.DataFrame({input("Names:"):Names,input("Prices:"):Prices,input("Description:"):Descp})
    print(df)

    #df.to_csv("airbnbdata.csv")


























