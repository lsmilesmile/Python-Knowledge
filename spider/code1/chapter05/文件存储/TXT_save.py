# 爬取知乎热门话题的问题、作者、回答，并保存到TXT中
import requests
from pyquery import PyQuery as pq


def main():
    url = 'https://www.zhihu.com/explore'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'
    }
    html = requests.get(url, headers=headers).text
    doc = pq(html)
    items = doc('.explore-feed.feed-item').items()
    for item in items:
        question = item.find('h2').text()
        author = item.find('.author-link-line').text()
        answer = pq(item.find('.content').html()).text()
        with open('./explore.txt', 'a', encoding='utf-8') as f:
            f.write('\n'.join([question, author, answer]))
            f.write('\n' + '=' * 50 + '\n')
            f.close()


if __name__ == '__main__':
    main()
