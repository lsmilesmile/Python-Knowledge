"""
爬取微博相关信息
"""
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from pymongo import MongoClient
import requests


base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/1192329374',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

# 获得页面数据


def get_page(page):
    params = {
        'type': 'uid',
        'value': '1192329374',
        'containerid': '1076031192329374',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        # 模拟发送Ajax请求
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()  # 将内容转化为json
    except requests.ConnectionError as e:
        print('Error:', e.args)

# 解析页面 - 解析获得的页面信息


def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()  # 将正文中的html标签去掉
            weibo['attitudes'] = item.get('attitutes_count')
            weibo['commnets'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo

# 将数据写入MongoDB数据库
def save_to_mongo(result, collection):
    collection.insert(result)


if __name__ == '__main__':
    client = MongoClient()
    db = client['weibo']
    collection = db['weibo']
    for page in range(2, 11):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            save_to_mongo(result, collection)
        print("Saved to mongo")
