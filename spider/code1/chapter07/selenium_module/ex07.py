"""
提取节点信息
"""
from selenium import webdriver


def main():
    '''获取属性 - get_attribute()'''
    browser = webdriver.Chrome()
    url = 'https://www.zhihu.com/explore'
    browser.get(url)
    # 找到节点
    logo = browser.find_element_by_id('zh-top-link-logo')
    # 打印节点
    print(logo)
    # WebElement节点的text属性 - 获取节点文本
    print(logo.text)
    # 打印这个结点的属性
    print(logo.get_attribute('class'))


if __name__ == '__main__':
    main()
