import pymongo
import config

class Mongo(object):
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017")
        self.db = self.client.weibo
        self.weibo = self.db.weibo  #默认数据库，用于存储所有的人员
       
    def save(self, data):
        """
            存储到数据库
        """
        
        if data.get('page_id', False):  #将所有的人存储到数据库
            self.weibo.save(data)

        collection = self.db[data['collection']]
        del data['collection']

        if collection.save(data):
            pass
        else:
            print("存储失败")


        