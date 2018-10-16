"""
获取淘宝首页搜索单个节点
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    input_first = browser.find_element_by_id('q')
    input_second = browser.find_element_by_css_selector('#q')
    input_third = browser.find_element_by_xpath('//*[@id="q"]')

    # 通用方法
    input_fourth = browser.find_element(By.ID, 'q')
    print(input_first, input_second, input_third, input_fourth)
    browser.close()


"""
<selenium.webdriver.remote.webelement.WebElement (session="b7273abbc352a3bddce173663459423a", element="0.2959917205777589-1")>
<selenium.webdriver.remote.webelement.WebElement (session="b7273abbc352a3bddce173663459423a", element="0.2959917205777589-1")>
<selenium.webdriver.remote.webelement.WebElement (session="b7273abbc352a3bddce173663459423a", element="0.2959917205777589-1")>
"""


if __name__ == '__main__':
    main()
