"""
节点交互
send_keys() - 输入文字
clear() - 清空文字
click() - 点击按钮
"""
from selenium import webdriver
import time


def main():
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    input = browser.find_element_by_id('q')  # 找到输入框
    input.send_keys('iPhone')  # 先输入iPhone
    time.sleep(1)
    input.clear()  # 清空输入框
    input.send_keys('iPad')  # 再输入
    button = browser.find_element_by_class_name('btn-search')  # 点击搜索按钮
    button.click()


if __name__ == '__main__':
    main()
