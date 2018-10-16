"""
获取id、位置、标签名、大小
WebElement结点的属性：
id - 结点id
location - 结点在页面中的相对位置
tag_name - 标签名称
size - 节点大小
"""
from selenium import webdriver


def main():
    browser = webdriver.Chrome()
    browser.get('https://www.zhihu.com/explore')
    input = browser.find_element_by_class_name('zu-top-add-question')
    print(input.id)
    print(input.location)
    print(input.tag_name)
    print(input.size)


if __name__ == '__main__':
    main()
