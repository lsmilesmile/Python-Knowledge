# 获取信息：属性、文本
from pyquery import PyQuery as pq


def main():
    html = '''
    <div class="wrap">
    <div id="container">
    <ul class="list">
    <li class="item-0">first item</li>
    <li class="item-1"><a href="link2.html">second item</a></li>
    <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
    <li class="item-1 active"><a href="link4.html">fourth item</a></li>
    <li class="item-0"><a href-"link5.html">fifth item</a></li>
    </ul>
    </div>
    </div>
    '''
    doc = pq(html)
    '''attr() - 获取属性'''
    a = doc('.item-0.active a')
    print(a, type(a))  # <class 'pyquery.pyquery.PyQuery'>
    print(a.attr('href'))
    # print(a.attr.herf)
    # 选中多个元素
    a = doc('a')
    print(a, type(a))
    print(a.attr('href'))  # 只得到第一个节点的属性
    # 遍历获取所有结果的属性
    for item in a.items():
        print(item.attr('href'))

    '''获取文本 - text()'''
    a = doc('.item-0.active a')
    print(a)
    print(a.text())  # 获取内部文本信息，忽略所有的节点内的HTML

    '''获取节点内部的HTML文本 - html()'''
    li = doc('.item-0.active')
    print(li)
    print(li.html())

    '''选中的结果是多个节点的情况'''
    li = doc('li')
    print(li.html())  # 只返回第一个li节点的内部HTML文本
    print(li.text())  # 返回所有li节点内部的纯文本，中间用空格隔开，是一个字符串
    print(type(li.text()))




if __name__ == '__main__':
    main()
