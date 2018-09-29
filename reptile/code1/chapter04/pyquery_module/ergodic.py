# 遍历
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
    '''单个节点来说，可以直接打印输出，也可以直接转换成字符串'''
    li = doc('.item-0.active')
    print(li)
    print(str(li))

    '''多个节点的结果，用遍历来获取 - items()'''
    lis = doc('li').items()  # <class 'generator'>
    print(type(lis))
    for li in lis:
        print(li, type(li))


if __name__ == '__main__':
    main()
