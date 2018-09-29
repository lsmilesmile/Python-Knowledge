from pyquery import PyQuery as pq


def main():
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
    # CSS选择器-先取id为container的节点，再取内部的class为list的节点内部的所有li节点
    print(doc('#container .list li'))
    # <class 'pyquery.pyquery.PyQuery'>
    print(type(doc('#container .list li')))


if __name__ == '__main__':
    main()
