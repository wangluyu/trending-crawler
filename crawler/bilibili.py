import base
import json
from const.message import Message

class BiliExt():
    def __init__(self):
        self.coins = 0
        self.author = ""
        self.video_review = 0
        self.play = 0
    def to_json(self):
        return {
            "coins": self.coins,
            "author": self.author,
            "video_review": self.video_review,
            "play" : self.play,
        }

class Bilibili(base.Base):
    def parse(self, soup):
        hot_list = []
        js = soup.find('script', {'type': False}).get_text().lstrip('window.__INITIAL_STATE__=').replace(";(function(){var s;(s=document.currentScript||document.scripts[document.scripts.length-1]).parentNode.removeChild(s);}());", "").strip()
        js = json.loads(js)
        for item in js['rankList']:
            msg = Message()
            msg.img = item['pic']
            msg.url = "https://www.bilibili.com/video/av" + item['aid']
            msg.title = item['title']
            ext = BiliExt()
            ext.coins = item['coins']
            ext.author = item['author']
            ext.video_review = item['video_review']
            ext.play = item['play']
            msg.ext = ext.to_json()
            self.add_trending(msg)

if __name__ == "__main__":
    url = "https://www.bilibili.com/ranking"
    _c = Bilibili(url)
    _c.execute()
    print(_c.get_trending_list())