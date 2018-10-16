"""
selenium+pyquery+MongoDB
"""
import pymongo
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
KEYWORD = 'iPad'


# 抓取含有商品信息的页面
def index_page(page):
    """
    抓取索引页
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + \
            quote(KEYWORD)  # 函数外面的变量可以拿来用，当时不能直接修改
        # 先打开这个网页
        browser.get(url)
        # 用点击跳转来实现，而不是下一页来实现
        if page > 1:
            # 因为要跳转，所以要重新加载页面，要等到输入页码的框和点击确定的按钮出现
            input = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(EC.element_to_be_clickable(
                By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit'))
        # 加载出输入页码的框后就清空这个框
        input.clear()
        # 在框中输入页码
        input.send_keys(page)
        # 点击跳转按钮
        submit.click()
        # 把让当前页的页码变得高亮 - 等待文本出现在指定节点里面(这儿是高亮节点)
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        # 等待每个信息块都加载出来
        wait.until(EC.presence_of_element_located(
            ((By.CSS_SELECTOR, '.m-itemlist .items .item'))))
        get_products()
    except TimeoutException:
        index_page(page)

# 解析页面，获取商品信息


def get_products():
    """
    抓取商品数据
    """
    # 获取网页源代码
    html = browser.page_source
    # 初始化PyQuery对象
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()  # 有很多节点时用items()
    for item in items:
        product = {
            'images': item.find('.pic .img').attr('data_src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()

        }
        print(product)
        save_to_mongo(product)


# 保存到数据库
MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def save_to_mongo(result):
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('ok')
    except Exception:
        print(failed)


# 遍历每页
MAX_PAGE = 100


def main():
    for i in range(1, MAX_PAGE + 1):
        index_page(i)


if __name__ == '__main__':
    main()
