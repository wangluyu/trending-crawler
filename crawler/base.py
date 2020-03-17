import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import requests
from bs4 import BeautifulSoup
from abc import abstractmethod
from const.common import Header
from const.message import Message

class Base(object):
    def __init__(self, url, methed = 'GET', data = None):
        self.url = url
        self.method = methed
        self.data = data
        self.header = None
        self.__trending_list = []

    def execute(self):
        self.setHeader()
        soup = self.request()
        self.parse(soup)

    @abstractmethod
    def parse(self, soup):
        pass

    def setHeader(self):
        self.header = Header.DEFAULT
    
    def add_trending(self, message):
        self.__trending_list.append(message.to_json())
    
    def get_trending_list(self):
        return self.__trending_list

    def request(self):
        """
        请求 返回bs对象
        """
        if self.method == 'GET':
            r = requests.get(self.url, params = self.data, headers = self.header)
        elif self.method == 'POST':
            r = requests.post(self.url, data = self.data, headers = self.header)
        else:
            return False
        if r.status_code != 200:
            print (r.reason)
            r.raise_for_status()
        soup = BeautifulSoup(r.text, features="lxml")
        return soup
    
    # TODO 数据存redis
    def save(self):
        pass

if __name__ == "__main__":
    url = "https://s.weibo.com/top/summary?cate=realtimehot"
    _base = Base(url)
    _base.execute()
    print(_base.trending_list)