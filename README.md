# Spider

$ celery -A tasks worker --loglevel=info  启动

broker是redis

调试时的问题：
    1.读取除“武大要闻”“媒体武大”“头条新闻”“综合新闻”外的其他分类时，出现列表索引超出范围的问题
    2.使用python2.7中reload函数可以解决编码的问题，在python3.5中没有内建函数reload，目前还没找到3.5的解决方法
