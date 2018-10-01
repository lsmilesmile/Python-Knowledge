"""
Beautiful Soup - Python的一个HTML或XML解析库
"""
from bs4 import BeautifulSoup
import re


def main():

    # test
    # soup = BeautifulSoup('<p>Hello</p>', 'lxml')
    # print(type(soup), soup, soup.p.string)
    """
    type(soup) - <class 'bs4.BeautifulSoup'>
    soup - <html><body><p>Hello</p></body></html>
    soup.p.string - Hello
    """

    """
    基本用法
    """
    # html = """
    #     <html><head><title>The Dormouse's story</title></head>
    #     <body>
    #     <p class="title" name="dormouse"><b>The Dormouse's story</b></p>
    #     <p class="story">Once upon a time there were three little sisters; and their names were
    #     <a href="http://example.com/elsie" class=#BDF6B0"sister" id="link1"><!--Elsie--></a>
    #     <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    #     <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    #     and they lived at the bottom of a well.</p>
    #     <p class="story">...</p>
    #     """
    # soup = BeautifulSoup(html, 'lxml')  # BeautifulSoup对象的初始化，第二个参数是解析器的类型
    # # prettify - 美化,把不标准的HTML字符串以标准的格式输出
    # print(soup.prettify())
    # print(soup.title.string)  # 输出title节点的文本内容#92EFCA

    """
    节点选择器 - 直接调用节点的名称就可以选择节点元素，再调用string属性就可以得到节点内的文本
    """
    '''选择元素'''
    # soup = BeautifulSoup(html, 'lxml')
    # print(soup.title)  # 输出该结点和结点中的文字内容
    # print(type(soup.title))  # <class 'bs4.element.Tag'> - Beautiful Soup中的一种重要数据结构
    # print(soup.title.string)  # 输出该节点中的文本内容
    # '''选择哪个结点就输出该结点和结点中的所有内容'''
    # print(soup.head)
    # print(soup.p)

    """
    提取信息 - 获取节点属性值和结点名
    """
    '''获取名称 - 利用name属性获取节点名称'''
    # soup = BeautifulSoup(html, 'lxml')
    # print(soup.title.name)
    '''获取属性'''
    # attrs:获取所有属性
    # print(soup.p.attrs)  # 获取所有属性，attrs返回的结果是字典，把属性和属性值组合成一个字典
    # 获取特定属性的方法一
    # print(soup.p.attrs['name'])  # 获取特定属性
    # 获取特定属性的方法二
    # print(soup.p['name'], soup.p['class'])  # dormouse ['title'] name属性的值是唯一的，所以返回字符串，而class值可能多个，所以返回列表
    '''获取内容'''
    # print(soup.p.string) # p是第一个p，内容也是第一个p中的文本

    """
    嵌套选择
    """
    # html = """
    # <html><head><title>The Dormouse's story</title></head>
    # <body>
    # """
    # soup = BeautifulSoup(html, 'lxml')
    # print(soup.head.title)  # 找到head后再找其内部的节点
    # print(type(soup.head.title))  # <class 'bs4.element.Tag'>
    # print(soup.head.title.string)

    """
    关联选择 - 有时候不能一步就选到想要的节点元素，可以先选到某一节点元素，然后以它为基准
    选择它的子节点、父节点、兄弟节点等。
    """
    # html = """
    #     <html>
    #     <head>
    #     <title>The Dormouse's story</title>
    #     </head>
    #     <body>
    #     <p class="story">
    #         Once upon a time there were three little sisters; and their names were
    #     <a href="http://example.com/elsie" class=#BDF6B0"sister" id="link1">
    #     <span>Elsie</span>
    #     </a>
    #     <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
    #     and
    #     <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
    #     and they lived at the bottom of a well.
    #     </p>
    #     <p class="story">...</p>
    #     """
    '''contents属性 - 返回直接子节点的列表'''
    # soup = BeautifulSoup(html, 'lxml')
    # print(soup.p.contents)
    '''children属性 - 返回直接子节点的迭代器'''
    # print(soup.p.children)
    # for i, child in enumerate(soup.p.children):
    #     print(i, child)
    '''descensants - 得到所有子孙节点，递归查询所有字节点'''
    # print(soup.p.descendants)  # 返回一个生成器
    # for i, child in enumerate(soup.p.descendants):
    #     print(i, child)
    '''父节点和祖先节点'''
    # html = """
    #     <html>
    #     <head>
    #     <title>The Dormouse's story</title>
    #     </head>
    #     <body>
    #     <p class="story">
    #         Once upon a time there were three little sisters; and their names were
    #     <a href="http://example.com/elsie" class="sister" id="link1">
    #     <span>Elsie</span>
    #     </a>
    #     </p>
    #     <p class="story">...</p>
    #     """
    # soup = BeautifulSoup(html, 'lxml')
    # print(soup.a.parent)
    '''获取所有祖先节点'''
    # html = """
    #     <html>
    #     <head>
    #     <title>The Dormouse's story</title>
    #     </head>
    #     <body>
    #     <p class="story">
    #     <a href="http://example.com/elsie" class="sister" id="link1">
    #     <span>Elsie</span>
    #     </a>
    #     </p>
    #     """
    # soup = BeautifulSoup(html, 'lxml')
    # print(type(soup.a.parents))  # <class 'generator'>
    # print(list(enumerate(soup.a.parents)))  # 所有祖先节点及其内容
    '''兄弟节点'''
    # html = """
    #     <html>
    #     <body>
    #     <p class="story">
    #         Once upon a time there were three little sisters; and their names were
    #     <a href="http://example.com/elsie" class=#BDF6B0"sister" id="link1">
    #     <span>Elsie</span>
    #     </a>
    #                 Hello
    #     <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
    #                 and
    #     <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
    #                 and they lived at the bottom of a well.
    #     </p>
    #     """
    # soup = BeautifulSoup(html, 'lxml')
    # next_sibling - 获取节点的下一个兄弟元素
    # previous_sibling - 获取节点的上一个兄弟元素
    # next_siblings - 返回后面的兄弟节点
    # previous_siblings - 返回前面的兄弟节点
    # print('Next Sibling', soup.a.next_sibling)
    # print('Prev Sibbling', soup.a.previous_sibling)
    # print('Next Siblings', list(enumerate(soup.a.next_siblings)))
    # print('Prev Siblings', list(enumerate(soup.a.previous_siblings)))
    '''提取信息'''
    # html = """
    #     <html>
    #     <body>
    #     <p class="story">
    #         Once upon a time there were three little sisters; and their names were
    #     <a href="http://example.com/elsie" class="sister" id="link1">Bob</a><a href="http://example.com/lacie"
    #     class="sister" id="link2">Lacie</a>
    #     </p>
    #     """
    # soup = BeautifulSoup(html, 'lxml')
    # print('Next Sibling:')
    # print(type(soup.a.next_sibling))
    # print(soup.a.next_sibling)
    # print(soup.a.next_sibling.string)
    # print('Parent:')
    # print(type(soup.a.parents))  # <class 'generator'>
    # print(list(soup.a.parents)[0])
    # # 返货多个节点的生成器，转列表后再取出某个元素，再调用string、attrs等属性
    # print(list(soup.a.parents)[0].attrs['class'])  # ['story']

    """
    方法选择器
    """
    '''find_all() - 查询所有符合条件的元素，返回所有匹配的元素组成的列表
    API:findall(name, attrs, recursive, text, **kwargs)
    '''
    # name - 根据节点名称来查询元素
    # html='''
    # <div class="panel">
    # <div class="panel-heading">
    # <h4>Hello</h4>
    # </div>
    # <div class="panel-body">
    # <ul class="list" id="list-1">
    # <li class="element">Foo</li>
    # <li class="element">Bar</li>
    # <li class="element">Jay</li>
    # </ul>
    # <ul class="list list-small" id="list-2">
    # <li class="element">Foo</li>
    # <li class="element">Bar</li>
    # </ul>
    # </div>
    # </div>
    # '''
    # soup = BeautifulSoup(html, 'lxml')
    # print(type(soup.find_all(name='ul')))  # <class 'bs4.element.ResultSet'>
    # print(soup.find_all(name='ul'))  # 结果列表类型
    # print(type(soup.find_all(name='ul')[0]))  # 每个元素的类型：<class 'bs4.element.Tag'>，所以可以进行嵌套查询
    # 再继续查询内部的li节点
    # for ul in soup.find_all(name='ul'):
    #     print(ul.find_all(name='li'))  # 结果是列表类型，每个元素依然是Tag类型
    #     for li in ul.find_all(name='li'):
    #         print(li.string)
    '''attrs - 该参数类型是字典类型'''
    # html='''
    # <div class="panel">
    # <div class="panel-heading">
    # <h4>Hello</h4>
    # </div>
    # <div class="panel-body">
    # <ul class="list" id="list-1", name="elements">
    # <li class="element">Foo</li>
    # <li class="element">Bar</li>
    # <li class="element">Jay</li>
    # </ul>
    # <ul class="list list-small" id="list-2">
    # <li class="element">Foo</li>
    # <li class="element">Bar</li>
    # </ul>
    # </div>
    # </div>
    # '''
    # soup = BeautifulSoup(html, 'lxml')
    # print(soup.find_all(attrs={'id': 'list-1'}))
    # print(soup.find_all(id="list-1"))
    # print(type(soup.find_all(attrs={'id': 'list-1'})))  # <class 'bs4.element.ResultSet'>
    # print(soup.find_all(attrs={'name': 'elements'}))
    # print(soup.find_all(class_="element"))  # 由于class是Python中的关键字，所以要加’_‘
    '''text - 匹配节点的文本，传入的形式可以是字符串，可以使正则表达式对象'''
    # html = '''
    # <div class="panel">
    # <div class="panel-body">
    # <a>Hello,this is a link</a>
    # <a>Hello,this is a link,too</a>
    # </div>
    # </div>
    # '''
    # soup = BeautifulSoup(html, 'lxml')
    # print(soup.find_all(text=re.compile('link')))  # 返回所有匹配该正则表达式的文本
    '''find() - 返回第一个匹配的元素'''
    # html='''
    # <div class="panel">
    # <div class="panel-heading">
    # <h4>Hello</h4>
    # </div>
    # <div class="panel-body">
    # <ul class="list" id="list-1">
    # <li class="element">Foo</li>
    # <li class="element">Bar</li>
    # <li class="element">Jay</li>
    # </ul>
    # <ul class="list list-small" id="list-2">
    # <li class="element">Foo</li>
    # <li class="element">Bar</li>
    # </ul>
    # </div>
    # </div>
    # '''
    # soup = BeautifulSoup(html, 'lxml')
    # print(soup.find(name='ul'))
    # print(type(soup.find(name='ul')))  # <class 'bs4.element.Tag'>
    # print(soup.find(class_="list"))
    """
    CSS选择器 - 知道调用selected()方法，传入相应的CSS选择器即可
    """
    html='''
    <div class="panel">
    <div class="panel-heading">
    <h4>Hello</h4>
    </div>
    <div class="panel-body">
    <ul class="list" id="list-1">
    <li class="element">Foo</li>
    <li class="element">Bar</li>
    <li class="element">Jay</li>
    </ul>
    <ul class="list list-small" id="list-2">
    <li class="element">Foo</li>
    <li class="element">Bar</li>
    </ul>
    </div>
    </div>
    '''
    soup = BeautifulSoup(html, 'lxml')
    # print(type(soup))  # <class 'bs4.BeautifulSoup'>
    # print(soup.select('.panel .panel-heading'))
    # print(soup.select('ul li'))
    # print(soup.select('#list-2 .element'))
    # print(type(soup.select('ul')[0]))  # <class 'bs4.element.Tag'>
    '''嵌套选择'''
    # for ul in soup.select('ul'):
    #     print(ul.select('li'))
    '''获取属性'''
    # for ul in soup.select('ul'):
    #     print(ul['id'])
    #     print(ul.attrs['id'])
    #     print(ul.attrs)
    # list-1
    # list-1
    # {'class': ['list'], 'id': 'list-1'}
    # list-2
    # list-2
    # {'class': ['list', 'list-small'], 'id': 'list-2'}
    '''获取文本 - 前面的string属性和现在的get_text()方法'''
    for li in soup.select('li'):
        print('Get  Text:', li.get_text())
        print('String:', li.string)


















if __name__ == '__main__':
    main()
