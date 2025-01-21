from spiders import QiyiSpider
spider = QiyiSpider()
comments = spider.get_comments('https://www.iqiyi.com/v_19rrjvkzb4.html?vfrmrst=0&vfrm=3&vfrmblk=pca_115_word_enlarge')
print(comments)