"""
查找节点
"""
from pyquery import PyQuery as pq


def main():
    '''子节点 - find():传入CSS选择器，该方法查找范围是所有子孙节点'''
    html = '''
    <div id="container">
    <ul class="list">
    <li class="item-0">first item</li>
    <li class="item-1"><a href="link2.html">second item</a></li>
    <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
    <li class="item-1 active"><a href="link4.html">fourth item</a></li>
    <li class="item-0"><a href-"link5.html">fifth item</a></li>
    </ul>
    </div>
    '''
    doc = pq(html)
    print(type(doc))  # <class 'pyquery.pyquery.PyQuery'>
    items = doc('.list')  # <class 'pyquery.pyquery.PyQuery'>
    print(type(items))
    print(items)
    lis = items.find('li')
    print(type(lis))  # <class 'pyquery.pyquery.PyQuery'>
    print(lis)
    '''children() - 查找子节点'''
    lis1 =  items.children()
    print(type(lis1))
    print(lis1)
    '''筛选符合条件的节点'''
    lis2 = items.children('.active')
    print(lis2)

    '''父节点'''
    html2 = '''
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
    doc = pq(html2)
    # 找到class为list的节点
    items = doc('.list')
    # 再找到它的直接父节点，不会再去找父节点的父节点
    container = items.parent()
    print(type(container))
    # 输出父节点的内容
    print(container)

    '''parents() - 获取所有父节点'''
    parents = items.parents()
    print(type(parents))
    print(parents)
    '''parents(CSS选择器) - 获取指定父节点'''
    some_parent = items.parents('.wrap')
    print(some_parent)

    '''兄弟节点 - siblings()方法'''
    li = doc('.list .item-0.active')
    # 输出该结点的所有兄弟节点
    '''选择所有兄弟节点 - siblings()'''
    print(li.siblings())
    '''选择指定兄弟节点 - siblings(CSS选择器)'''
    print(li.siblings('.active'))



if __name__ == '__main__':
    main()
