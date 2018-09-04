import requests
import re
from headers import Headers    #导入 headers 类 
from normalize import Normalize
from db import Redis            
from mongo import Mongo
import time
import random
import config

class Spider(object):
    header = Headers()
    headers = header.headers()   #初始化获取随机的请求头
    normalize = Normalize()      #格式化url
    items_fans = {}   #用于存储粉丝列表的字典
    items_self = {}   #用于存储个人信息的字典           
    redis = Redis()
    mongo = Mongo() 
    s_time = 0       #起始时间
    e_time = 0  #程序运行结束时间
    
    flag = 0  #请求头切换标识
    default_time = 20

    def start_url(self):
        #初始链接
        start_urls = ['https://weibo.com/p/1004061537790411?is_hot=1',]
        for start_url in start_urls:
            yield start_url


    def downloader(self, url_item, referer, retries_num=4):
        """
            返回源码
        """
        print("开始下载")
        self.e_time = time.time()  #获取当前时间
        time_dif = self.e_time - self.s_time
        if self.flag == 1:
            time_dif = 400
        flag = 0 
        if time_dif > 300:
            self.headers = self.header.headers()   #获取随机的请求头
            self.s_time = self.e_time

        time.sleep(random.random()*5 + random.random()*5) #+ random.randint(1,5))
        
        if referer:  #判断是否需要防盗链

            self.headers['Referer'] = referer  #添加referer

            url = url_item[0]
            print("待抓取：", url)
            try:
                response = requests.get(url, headers=self.headers, timeout=30)
                #print(self.headers)
                print("状态码：", response.status_code)

                #print(response.text)
                if response.status_code == 200:
                    if len(response.text) > 50000:
                        return response.text
                    else:
                        return None
                else:
                    self.flag = 0  #切换请求头
                    if retries_num > 0:
                        print("第", 4 - retries_num, '次下载')
                        self.downloader(url_item,referer, retries_num-1)
                    else:
                        self.redis.push(url_item)  #下载失败则重新下载
                        return None
            except requests.exceptions.ConnectionError as e:
                print("downloaderrl错误", url)
                print("错误信息：", str(e))
        else:
            response = requests.get(url, headers = self.headers)
            return response.text


    def parse_follow_page(self, html, referer):
        """
            从个人主页提取pageid, 用于构建 关注的人 的链接， 提取关注的人数，粉丝数
        """
        print("解析函数1")
        p1 = r'<title>(.*?[\u4e00-\u9fa5]{0,})的微博_微博</title>'     #用来匹配这是谁的微博
        p3 = r"\$CONFIG\['page_id'\]='(\d.*?)';"   #用于匹配pageid
        p4 = r"(\d{6})"  #用于从 pageid 中匹配pid

        p5 = r'<strong\sclass=\\"W_f12\\">(\d*?)<\\/strong><span\sclass=\\"S_txt2\\">关注<\\/span>'  #关注的人数
        p6 = r'<strong\sclass=\\"W_f12\\">(\d*?)<\\/strong><span\sclass=\\"S_txt2\\">粉丝<\\/span>'  #粉丝数

        self.items_self = {}

        self.items_self['collection'] = re.search(p1, html).group(1)    #谁的主页，用于建立collection
        self.items_self['page_id'] = re.search(p3, html).group(1)       #获得pageid
        self.items_self['pid'] = re.search(p4, self.items_self['page_id']).group(1)  #获得pid
        
        try:
            self.items_self['idol'] = int(re.search(p5, html).group(1))
        except:
            self.items_self['idol'] = '__'     #关注人数不可见，则idol列表不能添加
            print("关注的人数人不可访问")
        
        try:
            self.items_self['fans'] = int(re.search(p6, html).group(1))
        except:
            self.items_self['fans'] = 0
            print("粉丝数人不可访问")

        if self.items_self['fans'] > 50000:  #这是阻尼系数
            self.items_self['damp'] = 1
        else:
            self.items_self['damp'] = 0.5

        print(self.items_self)
        #self.mongo.save(self.items_self)   #存储
        yield self.items_self   #返回结果用于存储
        if isinstance(self.items_self['idol'], int):
            for url in self.normalize.nor_follow(self.items_self['page_id']):  #关注着页面
                url_item = [url, self.parse_detail, referer]
                yield url_item  #只需返回关注页面的链接即可，其他的直接存储
        else:
            yield None


    def parse_detail(self, html, referer):
        """
            提取每个人的关注页面和首页链接
        """

        print("解析函数2")
        self.items_fans = {}

        p1 = r'<title>(.*?[\u4e00-\u9fa5]{0,})的微博_微博</title>'
        p2 = r'<a\starget=\\"_blank\\"\stitle=\\"(.*?[\u4e00-\u9fa5]{0,})\\"\shref=\\"(.*?)\\"\s>'   #用于匹配粉丝列表

        
        try:
            results = re.findall(p2, html)

            for result in results:
                if result:

                    collection = re.search(p1, html).group(1)    #控制表
                    idol_name = result[0]      #关注者的名字
                    link = self.normalize.nor_home(result[1].replace('\\',''))   #关注者的首页链接

                    if re.search(r'\?', link):  #如果能找到 ‘？’ 则存入数据库 
                        self.items_fans = {
                            'collection' : collection,
                            'idol_name' : idol_name,
                            'link' : link,
                            } 
                           
                        print(self.items_fans)
                        #self.mongo.save(self.items_fans)  #存储到数据库
                        yield self.items_fans  #返回结果，用于存储
                        url_item = [self.items_fans['link'], self.parse_follow_page, referer]
                        yield url_item     #将结果返回
                    else:
                        print("链接不符合规定:", link)
                        yield None
        except:
            print("粉丝列表不可访问")

    
    def scheduler(self):
        #初始化
        #self.redis.delete()  #控制是否在爬虫关闭后继续抓取
       
        if self.redis.llen() == 0:
            for url in self.start_url():
                callback = self.parse_follow_page
                referer = "https://weibo.com"
                url_item = [url, callback, referer]
                self.redis.push(url_item)


        while True:
            print("开始执行")
            if not self.redis.llen():

                url_item = self.redis.pop()
                
                url = url_item[0]
                callback = url_item[1]
                referer = url_item[2]

                html = self.downloader(url_item, referer=referer)
                if html is not None:
                    print("html的长度:", len(html))

                    for items in callback(html, url):
                        if isinstance(items, list):
                            print("返回结果是列表")
                            self.redis.push(items)
                        if isinstance(items, dict):
                            print("返回结果是字典")
                            self.mongo.save(items)

                        if items is None:
                            pass               #剔除掉粉丝列表不可看的
                else:
                    print("html的值：", html)
            else:
                break
    
    def run(self):
        self.scheduler()