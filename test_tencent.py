from spiders import TencentSpider
spider = TencentSpider()
comments = spider.get_comments('https://v.qq.com/x/cover/mzc00200cqecotm/g0042gw1ak3.html',5)
print(comments)