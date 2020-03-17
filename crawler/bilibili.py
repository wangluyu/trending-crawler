import base
from const.message import Message

class Bilibili(base.Base):
    def parse(self, soup):
        hot_list = []
        print(soup)
        # tr_list = soup.find("div", id="pl_top_realtimehot").table.tbody.find_all("tr")
        # for tr in tr_list:
        #     msg = Message()
        #     td = tr.find("td", class_="td-02")
        #     a = td.a
        #     msg.url = 'https://s.weibo.com/'+a['href']
        #     msg.title = a.string
        #     if (td.span != None):
        #         msg.ext_text = td.span.string
        #     if (td.img != None):
        #         msg.ext_img = 'https://s.weibo.com/'+td.img['src']
        #     self.add_trending(msg)

if __name__ == "__main__":
    url = "https://www.bilibili.com/ranking"
    _c = Bilibili(url)
    _c.execute()
    print(_c.get_trending_list())