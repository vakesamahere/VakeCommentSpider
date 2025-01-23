# Author Vake
# env
- python 3.10
- pip install requests
# ps1
## 爱奇艺
可以修改爬虫类中_get_comments方法中的params，其中：
- page_size调整页数(最多不超过40页)
- sort可以用其他字符串，缺省也可
## 腾讯视频
- 输入url，页数默认10页，可以通过page参数指定
## BiliBili
- 输入url，可以指定模式(2是最新评论，3是最热评论，它的数据结构这么写的)，page指定页数。
- 可以设定cookie查看特定用户的的热门评论
# ps2
懒于维护，如果后端逻辑变了导致爬虫失效可以发邮件call一下作者来修改:)
# updates
- 2025/1/23 添加b站评论区爬取，复现了md5加密请求