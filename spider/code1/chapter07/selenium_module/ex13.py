"""
前进 - forward()
后退 - back()
"""
import time
from selenium import webdriver


def main():
    browser = webdriver.Chrome()
    browser.get('https://www.baidu.com/')
    browser.get('https://www.taobao.com/')
    browser.get('https://www.python.org/')
    browser.back()
    time.sleep(1)
    browser.forward()
    browser.close()


if __name__ == '__main__':
    main()
