"""
对网页的节点来说，它可以定义id、class或其他属性。利用XPath或CSS选择器来提取某个节点。
"""
from lxml import etree


def main():
    """
    实例 - XPath解析网页
    :return:
    """
    # text = '''
    # <div>
    # <ul>
    # <li class="item-0"><a href="link1.html">first item</a></li>
    # <li class="item-1"><a href="link2.html">second item</a></li>
    # <li class="item-inactive"><a href="link3.html">third item</a></li>
    # <li class="item-1"><a href="link4.html">fourth item</a></li>
    # <li class="item-0"><a href="link5.html">fifth item</a>
    # </ul>
    # </div>
    # '''
    # html = etree.HTML(text)  # 构造XPath解析对象
    # result = etree.tostring(html)  # 输出修正后的HTML代码，是bytes类型
    # print(result.decode('utf-8'))

    """
    直接读取文本文件进行解析
    """
    # html = etree.parse('./test.html', etree.HTMLParser())
    # result = etree.tostring(html)
    # print(result.decode('utf-8'))

    """
    所有节点
    """
    # html = etree.parse('./test.html', etree.HTMLParser())
    # result = html.xpath('//*')  # '*'代表所有节点，整个HTML文档的所有节点都会被获取。
    # print(result)  # 返回结果是个列表，每个元素都是一个Element对象

    """
    匹配指定节点
    """
    # html = etree.parse('./test.html', etree.HTMLParser())
    # result = html.xpath('//li')  # 选取所有的li节点
    # print(result)
    # print(result[0])  # <Element li at 0x23475f54848>

    """
    子节点
    """
    # 选取li节点的所有直接a子节点
    # html = etree.parse('./test.html', etree.HTMLParser())
    # result = html.xpath('//li/a')
    # # //li用于选中所有li节点，/a用于选中li节点的所有直接子节点a。
    # print(result)

    """
    '/' - 选取直接子节点；'//' - 选取所有子孙节点。如，获取ul节点下的所有子孙a节点
    """
    # html = etree.parse('./test.html', etree.HTMLParser())
    # result = html.xpath('//ul//a')
    # print(result)

    """
    父节点
    """
    # html = etree.parse('./test.html', etree.HTMLParser())
    # 通过parent::来获取父节点
    # result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
    # result = html.xpath('//a[@href="link4.html"]/../@class')  # 找到href属性为link4.html的a节点，再找到其父节点，再取class属性
    # print(result)  # ['item-1']

    """
    属性匹配
    """
    # html = etree.parse('./test.html', etree.HTMLParser())
    # result = html.xpath('//li[@class="item-0"]')
    # print(result)  # [<Element li at 0x2027f51b848>, <Element li at 0x2027f51b888>]

    """
    文本获取 - XPath中的text()方法获取节点中的文本
    """
    # html = etree.parse('./test.html', etree.HTMLParser())
    # result = html.xpath('//li[@class="item-0"]/text()')  # '/'选取直接子节点，是a，
    # print(result)  # ['\r\n']
    # 改进1
    # result = html.xpath('//li[@class="item-0"]/a/text()')  # 先找到直接子节点a，在获取a中的文本  # ['first item', 'fifth item']
    # 改进2
    # result = html.xpath('//li[@class="item-0"]//text()')  # 全部子节点的文本 ['first item', 'fifth item', '\r\n']
    # print(result)

    """
    属性获取 - '@'
    """
    # html = etree.parse('./test.html', etree.HTMLParser())
    # result = html.xpath('//li/a/@href')  # 获取所有li节点下所有a节点的href属性
    # print(result)

    """
    属性多值匹配
    """
    # text = '''
    #     <li class="li li-first"><a href="link.html">first item</a></li>
    #     '''
    # html = etree.HTML(text)
    # result = html.xpath('//li[@class="li"]/a/text()')
    # print(result)  # []

    # 改进 - contains(属性, 属性值)  只要该属性包含所传入的属性值
    # text = '''
    #     <li class="li li-first"><a href="link.html">first item</a></li>
    #     '''
    # html = etree.HTML(text)
    # result = html.xpath('//li[contains(@class, "li")]/a/text()')
    # print(result)

    """
    多属性匹配 - 根据多个属性确定一个节点
    """
    # text = '''
    #     <li class="li li-first" name="item"><a href="link.html">first item</a></li>
    #     '''
    # html = etree.HTML(text)
    # result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
    # result = html.xpath('//li[contains(@class, "li") or @name="item"]/a/text()')
    # print(result)  # ['first item']

    """
    按序选择 - 当某些属性匹配多个节点，但是我们只要其中的第几个节点时,利用括号中传入索引的方法获取特定次序的节点
    """
    # text = '''
    #     <div>
    #     <ul>
    #     <li class="item-0"><a href="link1.html">first item</a></li>
    #     <li class="item-1"><a href="link2.html">second item</a></li>
    #     <li class="item-inactive"><a href="link3.html">third item</a></li>
    #     <li class="item-1"><a href="link4.html">fourth item</a></li>
    #     <li class="item-0"><a href="link5.html">fifth item</a></li>
    #     </ul>
    #     </div>
    #     '''
    # html = etree.HTML(text)
    # result1 = html.xpath('//li[1]/a/text()')  # 不是以0开始的，是从1开始的
    # print(result1)  # ['first item']
    # result2 = html.xpath('//li[last()]/a/text()')  # 最后一个节点
    # print(result2)
    # result3 = html.xpath('//li[position()<3]/a/text()')
    # print(result3)
    # result4 = html.xpath('//li[last()-2]/a/text()')
    # print(result4)

    """
    节点轴选择
    """
    text = '''
        <div>
        <ul>
        <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
        </ul>
        </div>
        '''
    html = etree.HTML(text)

    # ancestor轴 - 选取所有祖先节点，后面跟两个冒号，后面是节点选择器，用‘*’表示匹配所有节点。
    # result1 = html.xpath('//li[1]/ancestor::*')
    # print(result1)

    # ancestor - 选取div这个祖先节点
    # result2 = html.xpath('//li[1]/ancestor::div')
    # print(result2)

    # attribute - 获取li[1]节点的所有属性（attribute）
    # result3 = html.xpath('//li[1]/attribute::*')
    # print(result3)

    # child - 获取所有直接子节点
    # result4 = html.xpath('//li[1]/child::a[@href="link1.html"]')
    # print(result4)

    # descendant轴 - 获取所有子孙节点（descendant - 后裔）
    # result5 = html.xpath('//li[1]/descendant::span')
    # print(result5)

    # following轴 - 选择当前节点之后的所有节点
    # result6 = html.xpath('//li[1]/following::*[2]')  # 选择第二个
    # print(result6)

    # following-sibling - 获取当前节点之后的同级节点
    # result7 = html.xpath('//li[3]/following-sibling::*[3]')  # 选择当前节点之后的所有同级节点中的第三个，显然不存在了
    # print(result7)  # [<Element li at 0x207ba63d6c8>, <Element li at 0x207ba63d7c8>]


if __name__ == '__main__':
    main()
