import requests
from bs4 import BeautifulSoup
from abc import abstractmethod

class Base(object):
    def __init__(self, url, methed = 'GET', data = None):
        self.url = url
        self.method = methed
        self.data = data
        self.trending_list = []

    def execute(self):
        soup = self.request()
        self.parse(soup)

    @abstractmethod
    def parse(self, soup):
        pass

    def request(self):
        """
        请求 返回bs对象
        """
        if self.method == 'GET':
            r = requests.get(self.url, params = self.data)
        elif self.method == 'POST':
            r = requests.post(self.url, data = self.data)
        else:
            return False
        if r.status_code != 200:
            print (r.reason)
            r.raise_for_status()
        soup = BeautifulSoup(r.text)
        return soup
    
    # TODO 数据存redis
    def save(self):
        pass

if __name__ == "__main__":
    url = "https://s.weibo.com/top/summary?cate=realtimehot"
    _base = Base(url)
    _base.execute()
    print(_base.trending_list)