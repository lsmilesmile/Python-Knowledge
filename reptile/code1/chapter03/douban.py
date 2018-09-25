import requests
import re
import json


def get_one_page():
    headers = {
        'User-Agent': 'Mozilla/5.0'
                      ' (Linux; Android 6.0; Nexus 5 Build/MRA58N)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'
    }
    response = requests.get('https://movie.douban.com/chart', headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def parse_page(html):
    pattern = re.compile('<table width="100%" class="">.*?'
                         '<a.*?title="(.*?)">.*?'
                         '<img src="(.*?)".*?'
                         '<p.*?>(\d{4}-\d{2}-\d{2}\(.*?\))(.*?)</p>.*?'
                         '<span.*?rating_nums.*?>(.*?)</span>.*?'
                         '</table>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield{
            '电影名称：': item[0],
            '图片：': item[1],
            '上映时间：': item[2],
            '演员：': item[3],
            '评分：': item[4]
        }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


# 主函数
def main():
    html = get_one_page()
    for item in parse_page(html):
        write_to_file(item)


if __name__ == '__main__':
    main()
