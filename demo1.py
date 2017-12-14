# -*- coding: utf-8 -*-  
from bs4 import BeautifulSoup#用beautifulsoup爬取网页
import requests
import time
url="https://knewone.com/discover?page="
def get_page(url,data=None):
    wb_data=requests.get(url)#返回一个200的状态码和一个response对象
    print (wb_data)
    soup=BeautifulSoup(wb_data.content,"lxml")#用lxml方式进行解析，并返回一个soup数组
    print (soup)
    imgs=soup.select('a.cover-inner>img')
    titles=soup.select("selection.content > h4 > a")
    links=soup.select("selection.content > h4 > a")
    for img,title,link in zip(imgs,titles,links):
            data={
               'img':img.get('src'),
               'title':title.get('title'),
               'link':link.get('href') 
            }
            print (data).encoding("utf-8")
def get_more_pages(start,end):
    for one in range(start,end):
        get_page(url+str(one))
        time.sleep(2)
get_more_pages(1, 10)

