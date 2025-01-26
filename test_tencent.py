from spiders import TencentSpider
spider = TencentSpider()
# comments = spider.get_comments('https://v.qq.com/x/page/i35226tgr75.html',5)
# comments = spider.get_comments('https://v.qq.com/x/cover/mzc0020071dthex/r0042x14y3q.html',15,log=3)
comments = spider.get_comments('https://v.qq.com/x/cover/mzc0020071dthex.html',15,log=3)
print(comments)