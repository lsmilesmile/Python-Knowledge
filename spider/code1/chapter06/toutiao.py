"""
爬取今日头条街拍图片并保存
"""
import requests
import os
from urllib.parse import urlencode
from hashlib import md5
from multiprocessing.pool import Pool

def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab' 
    }
    base_url = 'https://www.toutiao.com/search_content/?'
    url = base_url + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

# 获得标题和图片的url
def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            if item.get('open_url'):
                title = item.get('title')
                images = item.get('image_list')
                for image in images:
                    yield{
                        'image': 'http:' + image.get('url'),
                        'title': title
                    }

# 保存图片
def save_image(item):
    '''
    os.path.exists() - 看括号中的文件是否存在，括号中可以是文件名，也可以是一个路径
    '''
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        # 请求图片url
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            # 如果请求成功，则创建图片文件，为了去除重复，可以使用图片的MD5值作为名称
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            # 如果该图片文件不存在，则将该图片保存
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            # 如果图片存在则提示已经下载过了
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to save image')

def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)

GROUP_START = 1
GROUP_END = 20

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
 