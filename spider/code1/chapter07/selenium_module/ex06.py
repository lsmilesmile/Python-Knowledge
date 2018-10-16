"""
模拟运行javascript
"""
from selenium import webdriver


def main():
    browser = webdriver.Chrome()
    browser.get('https://www.zhihu.com/explore')
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    browser.execute_script('alert("To Bottom")')


if __name__ == '__main__':
    main()
