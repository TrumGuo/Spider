#coding=utf-8
from celery import Celery

app = Celery('spider', include=['spider.getNews'])

app.config_from_object('spider.config')

if __name__ == '__main__':
    app.start()
