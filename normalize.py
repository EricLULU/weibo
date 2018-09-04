"""
用于格式化url
"""
class Normalize(object):
    url_base = "https://weibo.com"   #基本的url

    def nor_home(self, link):
        """
            返回主页
        """
        return self.url_base + link

    def nor_follow(self, page_id):
        """
            返回每一页
        """
        #r = "https://weibo.com/p/1004061537790411/follow?page=2"
        
        
        for i in range(1, 6):
            start_url = self.url_base + '/p/' + page_id + '/follow?'
            yield start_url + 'page' + '=' + str(i)