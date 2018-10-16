"""
切换Frame - switch_to_.frame()
网页中有一种节点：iframe，即子Frame，相当于页面的子页面，它的结构和外部网页结构完全一致。
Selenium打开页面后，它默认是在父级Frame里面操作，此时如果页面中还有字Frame，是不能提取到子Frame里面的结点的
"""
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def main():
    browser = webdriver.Chrome()
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    try:
        logo = browser.find_element_by_class_name('logo')
    except NoSuchElementException:
        print('NO LOGO')
    browser.switch_to.parent_frame()
    logo = browser.find_element_by_class_name('logo')
    print(logo)
    print(logo.text)


if __name__ == '__main__':
    main()
