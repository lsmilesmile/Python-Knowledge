"""
显示等待 - 指定要查找的节点，然后指定一个最长等待时间。如果在规定时间内加载出来了这个节点，就返回查找的节点
；如果规定时间内没有加载出来该节点，则抛出异常
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com/')
    wait = WebDriverWait(browser, 10)
    input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
    print(input, button)

if __name__ == '__main__':
    main()