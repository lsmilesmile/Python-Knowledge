# 节点操作 - 对节点进行动态修改，比如添加class等
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
    '''removeClass()、addClass()：动态改变节点的class属性'''
    li = doc('.item-0.active')
    print(li)
    li.removeClass('active')
    print(li)
    li.addClass('active')
    print(li)

    '''attr：操作属性，只传入第一个参数的属性名，则是获取属性，传入第二个参数可以修改属性
    text、html：不传入参数则获取节点内纯本文和HTML文本，传入参数则进行赋值
    '''
    li = doc('.item-0.active')
    print(li)
    li.attr('name', 'link')  # 增加属性name，名为link
    print(li)
    li.text('changed item')  # 改变节点内部的内容，有子节点则删除
    print(li)
    li.html('<span>changed item</span>')
    print(li)

    '''remove() - 移除'''
    html = '''
    <div class="wrap">
        Hello, World
    <p>This is a paragraph.</p>    
    </div>
    '''
    doc = pq(html)
    wrap = doc('.wrap')
    # 找到全部的纯文本
    print(wrap.text())
    # 只要Hello World
    wrap.find('p').remove()
    print(wrap.text())




if __name__ == '__main__':
    main()