import base
import json
from const.message import Message

class Zhihu(base.Base):
    def parse(self, soup):
        hot_list = json.loads(soup.find('script', {'type': 'text/json', 'id': 'js-initialData'}).get_text())['initialState']['topstory']['hotList']
        for item in hot_list:
            msg = Message()
            target = item['target']
            msg.url = target['link']['url']
            msg.title = target['titleArea']['text']
            msg.ext_text = target['metricsArea']['text']
            self.add_trending(msg)

if __name__ == "__main__":
    url = "https://www.zhihu.com/billboard"
    _c = Zhihu(url)
    _c.execute()
    print(_c.get_trending_list())