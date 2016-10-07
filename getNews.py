#coding=utf-8
'''
Created on 2016-9-30

@author:Guo
'''
import urllib2
import os
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from celery import Celery

celery = Celery('tasks',broker='redis://127.0.0.1:6379/6')

@celery.task
def getNews():
    page_WDYW = urllib2.urlopen('http://news.whu.edu.cn/wdyw.htm')
    BS_WDYW = BeautifulSoup(page_WDYW,"html.parser")
    
    for index in range(0, 25):
        id_li = 'lineu5_' + str(index)
        news = BS_WDYW.find('li', attrs={'id': id_li})
        
        news_title = news.find('a')['title']
        
        news_url = 'http://news.whu.edu.cn/' + news.find('a')['href']
        
        news_date = news.find('div', attrs={'class': 'infodate'}).text.strip()
        
        content = urllib2.urlopen(news_url)
        content_BS = BeautifulSoup(content,"html.parser")
        news_content = content_BS.find_all('div', attrs={'class': 'news_content'})[1].get_text().strip()

        news_type = "武大要闻"
    
        with open('news/武大要闻/'+news_title+'.txt','w') as f:
            file_content = "---\ntitle: %s\ndate: %s\ntags: %s\n---\n%s\n 本条新闻源地址：%s" % (news_title,news_date,news_type,news_content,news_url)
            f.write(file_content)

    
    page_ZHXW = urllib2.urlopen('http://news.whu.edu.cn/zhxw.htm')
    BS_ZHXW = BeautifulSoup(page_ZHXW,"html.parser")
    
    for index in range(0, 25):
        id_li = 'lineu5_' + str(index)
        news = BS_ZHXW.find('li', attrs={'id': id_li})
        
        news_title = news.find('a')['title']
        
        news_url = 'http://news.whu.edu.cn/' + news.find('a')['href']
        
        news_date = news.find('div', attrs={'class': 'infodate'}).text.strip()
        
        content = urllib2.urlopen(news_url)
        content_BS = BeautifulSoup(content,"html.parser")
        news_content = content_BS.find_all('div', attrs={'class': 'news_content'})[1].get_text().strip()

        news_type = "综合新闻"
    
        with open('news/综合新闻/'+news_title+'.txt','w') as f:
            file_content = "---\ntitle: %s\ndate: %s\ntags: %s\n---\n%s\n 本条新闻源地址：%s" % (news_title,news_date,news_type,news_content,news_url)
            f.write(file_content)
        
