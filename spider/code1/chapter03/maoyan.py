"""
抓取猫眼电影排行榜
"""
import requests
import re
import json

'''
抓取首页
'''


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0'
                      ' (Linux; Android 6.0; Nexus 5 Build/MRA58N)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?) \
    </p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    print(items)
    # 字典的格式输出信息
    for item in items:
        yield{
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score': item[5].strip() + item[6].strip()
        }


# 写入文件
def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        print(type(json.dumps(content)))
        # 指定ensure_ascii参数为False，这样可以保证输出结果是中文形式，而不是Unicode编码
        f.write(json.dumps(content, ensure_ascii=False)+'\n')


# 分页爬取
def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)

