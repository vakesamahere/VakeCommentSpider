from spiders import BiliSpider
spider = BiliSpider()
try:
    with open('cookies.txt','r',encoding='utf-8') as f:
        cookie = f.read()
    if len(cookie)>0:
        spider.set_cookie(cookie)
except:
    pass
comments = spider.get_comments('https://www.bilibili.com/video/BV1UpwaeNESx/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=6b17401e8473bbe5fa0073fad1c6c38b',3,2000,log=2)
print('b站\n',comments,len(comments))