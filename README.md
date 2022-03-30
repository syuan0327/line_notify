# line_notify

## 股票爬蟲
### 介紹
每隔一段時間爬出當前所寫的股票市值，利用linen-notify傳送目前市值給自己。
### 所需工具
這裡不用Heroku的原因是因為Heroku有休息時間，為了讓機器人不休息，所以採用這種方法。
1. python 3.8
2. [Replit](https://replit.com/~) 伺服器用
3. [Uptimerobot](https://uptimerobot.com/dashboard#mainDashboard) 監督伺服器用使其不會停止
4. [基礎爬蟲](https://github.com/syuan0327/Web-Scrapying/blob/main/beautifulsoup/beautifulsoup.md)裡面有一些會用的爬蟲程式碼，可以先練習

### 實作
首先是爬蟲部分的程式碼，以下有幾點需要修改：
1.  這裡採用的寫法是利用自己當時買的股價來減掉現股價，如果不想要這個功能可以直接刪掉`def f_compare()`和`def c_compare()`。
2.  再來是買價的部分，要從`fox_buy`和`cdi_buy`這兩個變數修改。
3.  如果有需要查詢的股價可以更改`news1`和`news2`網址後面的數字。
4.  目前只能有兩種股價判斷，如果需要可依照寫法自行新增。
```python

from bs4 import BeautifulSoup
from numpy import c_
import requests,time

#use request.get() to store web's html
news1=requests.get('https://tw.stock.yahoo.com/quote/改成想要查詢的第一股價號碼.TW')
news2=requests.get('https://tw.stock.yahoo.com/quote/改成想要查詢的第二股價號碼.TW')
#analysis the html code,and build the object
soup1=BeautifulSoup(news1.text,'html.parser')
soup2=BeautifulSoup(news2.text,'html.parser')
#output the html content
#print(soup.prettify())
fbox=[]
cbox=[]
fox_buy=改成你的買價
cdi_buy=改成你的買價
def foxconn():
    news1=requests.get('https://tw.stock.yahoo.com/quote/改成想要查詢的第一股價號碼.TW')
    soup1=BeautifulSoup(news1.text,'html.parser')
    results1=soup1.find_all('div',class_='D(f) Ai(fe) Mb(4px)')#找全部或限制數量
    for result in results1:
        for i in result:
            return i.text
def cdibh():
    news2=requests.get('https://tw.stock.yahoo.com/quote/改成想要查詢的第二股價號碼.TW')
    soup2=BeautifulSoup(news2.text,'html.parser')
    results2=soup2.find_all('div',class_='D(f) Ai(fe) Mb(4px)')#找全部或限制數量
    for result in results2:
        for i in result:
            return i.text
#不想比較就刪掉以下
def f_compare():
    ans=fox_buy-float(foxconn())
    
#可在return內自行更名    
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

```

