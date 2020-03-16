import base
class Weibo(base.Base):
    def parse(self, soup):
        hot_list = []
        tr_list = soup.find("div", id="pl_top_realtimehot").table.tbody.find_all("tr")
        for tr in tr_list:
            a = tr.find("td", class_="td-02").a
            self.trending_list.append({
                'url': 'https://s.weibo.com/'+a['href'],
                'title': a.string
            })

if __name__ == "__main__":
    url = "https://s.weibo.com/top/summary?cate=realtimehot"
    _wb = Weibo(url)
    _wb.execute()
    print(_wb.trending_list)