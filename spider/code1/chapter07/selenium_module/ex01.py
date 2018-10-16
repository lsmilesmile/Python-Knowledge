from selenium import webdriver
"""
声明浏览器对象
"""


def main():
    '''浏览器对象的初始化，赋值给browser'''
    browser = webdriver.Chrome()  # 谷歌浏览器
    # browser = webdriver.Firefox()  # 火狐
    # browser = webdriver.Edge()  # ie
    # browser = webdriver.PhantomJS()
    # browser = webdriver.Safari()  # 苹果的

    '''访问页面'''
    browser.get('https://www.taobao.com')  # 访问淘宝页面
    print(browser.page_source)  # 返回网页代码
    browser.close()  # 关闭浏览器


if __name__ == '__main__':
    main()
