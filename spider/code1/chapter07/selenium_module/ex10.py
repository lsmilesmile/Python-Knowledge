"""
延时等待 - get()方法在网页框架加载结束后结束执行，此时获得page_source可能不是浏览器完全加载完成的页面
"""
from selenium import webdriver
def main():
    '''隐式等待 - implicitly_wait()当查找结点而结点并没有立即出现的时候，隐式等待将等待一段时间再查找DOM'''
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get('https://www.zhihu.com/explore')
    input = browser.find_element_by_class_name('zu-top-add-question')
    print(input)

if __name__ == '__main__':
    main()