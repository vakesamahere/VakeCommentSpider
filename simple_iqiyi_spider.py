import requests,re,json,random

class QiyiSpider:
    '''
    爬虫类
    '''
    invalid_content_id="invalid_content_id"
    content_id_url = 'https://mesh.if.iqiyi.com/player/lw/lwplay/accelerator.js?apiVer=2'
    comment_url = 'https://sns-comment.iqiyi.com/v3/comment/get_baseline_comments.action'
        # User-agent pool
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (Linux; Android 10; Pixel 3 XL Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/89.0"
    ]
    
    def __init__(self):
        pass

    def get_random_user_agent(self):
        return random.choice(self.user_agents)
    
    def get_content_id(self,referer):
        headers = {
            "Referer": referer,
            "User-Agent": self.get_random_user_agent()
        }
        response = requests.get(self.content_id_url, headers=headers)
        if response.status_code == 200:
            # with open("snapshot/js_snapshot.js", "w", encoding='utf-8') as f:
            #     f.write(response.text)
            # print("文件已保存为 snapshot/js_snapshot.js")
            # 匹配"tvid":xxx
            match = re.search(r'"tvid":(\d+)', response.text)
            if match:
                tvid = match.group(1)
                print("get content_id:", tvid)
                return tvid
            else:
                print("content_id matching failed")
                return self.invalid_content_id
        else:
            print("content_id connecting failed: ", response.status_code)
            return self.invalid_content_id

    def _get_comments(self, url):
        '''
        直接调用
        '''
        tvid = self.get_content_id(url)
        if tvid==self.invalid_content_id:
            return PageComments()
        params = {
            "page_size":40,
            "sort":"HOT",
            "business_type":17,
            "agent_type":30,
            "content_id":eval(tvid)
        }
        try:
            headers = {
                "User-Agent": self.get_random_user_agent()
            }
            response = requests.get(self.comment_url, params=params,headers=headers)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            comments = json.loads(response.text)
        except requests.RequestException as e:
            print(f"Error loading URL: {e}")
            return PageComments()
        return PageComments(comments.get('data').get('comments'))
    
    def get_comments(self,url,rawtext=True):
        '''
        提供选项
        '''
        result = self._get_comments(url)
        if not rawtext:
            return result
        # else
        if result.valid:
            return result.only_content
        # else
        return []

class PageComments:
    '''
    一个页面的评论
    '''
    raw_list = []
    only_content=[]
    valid = False
    def __init__(self,comments_list):
        self.raw_list = comments_list
        try:
            for item in comments_list:
                self.only_content.append(item.get('content'))
        except:
            return
        self.valid = True

if __name__ == '__main__':
    spider = QiyiSpider()
    comments = spider.get_comments('https://www.iqiyi.com/v_19rrjvkzb4.html?vfrmrst=0&vfrm=3&vfrmblk=pca_115_word_enlarge')
    print(comments)