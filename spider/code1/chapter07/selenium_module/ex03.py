"""
获取淘宝首页搜索单多个节点 - 
获得淘宝首页左侧导航条的所有条目
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    # find_elements-获取所有节点
    # find_element - 获取第一个节点
    lis = browser.find_elements_by_css_selector('.service-bd li')
    lis1 = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
    print(lis1)
    browser.close()


if __name__ == '__main__':
    main()
