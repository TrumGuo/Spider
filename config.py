#coding=utf-8

CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/5'
BROKER_URL = 'redis://127.0.0.1:6379/6'
CELERY_TIMEZONE = 'Asia/Shanghai'

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
         'task': 'spider.getNews.getNews',
         'schedule': timedelta(secondss=30),
         'args':(16,16)
    },
}
