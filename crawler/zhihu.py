import base
import json
class Zhihu(base.Base):
    def parse(self, soup):
        hot_list = json.loads(soup.find('script', {'type': 'text/json', 'id': 'js-initialData'}).get_text())['initialState']['topstory']['hotList']
        for item in hot_list:
            target = item['target']
            self.trending_list.append({
                'title': target['titleArea']['text'],
                'url': target['link']['url'],
            })

if __name__ == "__main__":
    url = "https://www.zhihu.com/billboard"
    _c = Zhihu(url)
    _c.execute()
    print(_c.trending_list)