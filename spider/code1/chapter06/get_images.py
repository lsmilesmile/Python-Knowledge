from urllib.robotparser import RobotFileParser
import requests
import urllib
import re
import json
import os
import threading

# 全局变量
source_list = []
html_list = []

# 看是否能爬取
def is_allow(robots_url, url):
    rp = RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    result = rp.can_fetch('*', url)
    return result


def get_source(url):
    headers = {
        'Host': 'www.avhao2.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    # 获取html方式一
    # req = urllib.request.Request(url=url, headers=headers)
    # response = urllib.request.urlopen(req)
    # return response.read().decode('utf-8')
    # 获取html方式二
    response = requests.get(url, headers=headers)
    return response

def get_kind_pages():
    global html_list
    base_url = 'http://www.avhao2.com/forum.php?'
    for page in range(1, 2):
        url = base_url + \
            urllib.parse.urlencode(
                {'mod': 'forumdisplay', 'fid': '55', 'page': page})
        html = get_source(url).text
        html_list.append(html)

# 获得一类图片的链接，和该类图片的标题
def get_title_urls():
    # 取得一个页面的html
    html = html_list.pop(0)
    # 使用全局变量
    global source_list
    # 方式一 - 正则表达式
    pattern = re.compile(
        '<li style="width:380px">.*?<h3.*?<a href="(.*?)".*?>(.*?)</a>.*?</li>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        item_temp = str(item[0]).split(';')
        source = (item[1], 'http://www.avhao2.com/' +
                  item_temp[0] + '&' + item_temp[1] + '&' + item_temp[2])
        source_list.append(source)


# \/:*?"<>|
# def test(content):
#     with open('./test.txt', 'a', encoding='utf-8') as f:
#         f.write(json.dumps(content, ensure_ascii=False) + '\n')

def get_images_urls(url):
    # 获得每个标题的图片的页面html
    html = get_source(url).text
    # 获得每张图片的链接
    # 正则表达式
    pattern = re.compile('<ignore_js_op>(.*?)</ignore_js_op>', re.S)
    image_urls = re.findall(pattern, html)
    return html
    

def save_images():
    global source_list
    # 要创建文件夹，所以先检查标题名是否符合文件夹命名规范
    sign = {'"', '\\', '/', '|', '<', '*', '?', '>', ':'}
    one_kind = source_list.pop(0)
    title = one_kind[0]
    url = one_kind[1]
    print(url)
    # if sign & set(title):
    #     for sig in sign & set(title):
    #         title = title.replace(sig, '')
    # if not os.path.exists('./images/' + title):
    #     os.mkdir('./images/' + title)


def main():
    global source_list
    get_kind_pages()
    while html_list:
        get_title_urls()
    # print(source_list)
    # while source_list:
    save_images()



if __name__ == '__main__':
    main()

# http://www.avhao2.com/data/attachment/forum/201802/22/230645kfv6lp9ppnl3ofu7.jpg
