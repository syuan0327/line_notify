
from bs4 import BeautifulSoup
from numpy import c_
import requests,time

#use request.get() to store web's html
news1=requests.get('https://tw.stock.yahoo.com/quote/2317.TW/technical-analysis')
news2=requests.get('https://tw.stock.yahoo.com/quote/2883.TW')
#analysis the html code,and build the object
soup1=BeautifulSoup(news1.text,'html.parser')
soup2=BeautifulSoup(news2.text,'html.parser')
#output the html content
#print(soup.prettify())
fbox=[]
cbox=[]
fox_buy=
cdi_buy=
def foxconn():
    results1=soup1.find_all('div',class_='D(f) Ai(fe) Mb(4px)')#找全部或限制數量
    for result in results1:
        for i in result:
            return i.text
def cdibh():
    results2=soup2.find_all('div',class_='D(f) Ai(fe) Mb(4px)')#找全部或限制數量
    for result in results2:
        for i in result:
            return i.text

def f_compare():
    ans=fox_buy-float(foxconn())
    
    if ans<0:
        return('🔴鴻海'+str(0-round(ans,3)))

    elif ans>0:
        return('🟢鴻海'+str(0-round(ans,3)))
def c_compare():
    ans1=cdi_buy-float(cdibh())
    if ans1<0:
        return('🔴開發金'+str(0-round(ans1,3)))

    elif ans1>0:
        return('🟢開發金'+str(0-round(ans1,3)))
