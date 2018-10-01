from urllib import request, parse, error
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError
from urllib.request import ProxyHandler, urlopen
import http.cookiejar
from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit, urljoin, urlencode, parse_qs, parse_qsl \
    , quote, unquote
from urllib.robotparser import RobotFileParser

import socket


def main():

    """
    urlopen()
    """
    # response = request.urlopen("https://www.python.org")  # 返回一个HTTPResponse类型的对象
    # print(response.read().decode('utf-8'))  # 得到返回网页的内容
    # print(type(response))  # <class 'http.client.HTTPResponse'>
    # print(response.status)  # 返回结果的状态码
    # print(response.getheaders())  # 响应的头信息
    # print(response.getheader('Server'))  # 服务器的值

    """
    urlopen中的data参数
    """
    # bytes方法，第一个参数是字符串，第二个参数是编码格式
    # 先将参数字典转换成字符串，用urlencoding方法；
    # 第二个参数指定编码格式
    # data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf8')
    # response = request.urlopen('http://httpbin.org/post', data=data)
    # print(response.read())

    """
    urlopen的timeout参数，用于设置超时时间，单位是秒，如果请求超出了设置的这个时间，就会抛出异常，如果不指定这个参数就使用
    全局默认时间
    """
    # 超时抛出的URLError异常属于urllib.error模块
    # response = request.urlopen('http://httpbin.org/get', timeout=0.00001)
    # print(response.read())

    # 改进，使用try，except语句处理超时异常
    # try:
    #     response = request.urlopen('http://httpbin.org/get', timeout=0.0001)
    # except error.URLError as e:
    #     if isinstance(e.reason, socket.timeout):  # 判断该异常确实是超时异常
    #         print('TIME OUT')

    """
    更强大的类Request
    """
    # request = request.Request('http://python.org')  # 返回一个Request类型的对象
    # response = request.urlopen(request)
    # print(response.read().decode('utf-8'))

    """
    Request参数的使用
    """
    # 要传递的4个参数
    # url = 'http://httpbin.org/post'
    # headers = {
    #     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    #     'Host': 'httpbin.org'
    # }
    # a_dict = {
    #     'name': 'Germey'
    # }
    # data = bytes(parse.urlencode(a_dict), encoding='utf8')
    # req = request.Request(url=url, data=data, headers=headers, method='POST')

    # 用add_header()来添加headers
    # req = request.Request(url=url, data=data, method='POST')
    # req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
    # response = request.urlopen(req)
    # print(response.read().decode('utf-8'))

    """
    用handler来构建opener
    """
    # username = 'username'
    # password = 'password'
    # url = 'http://localhost:5000/'
    #
    # p = HTTPPasswordMgrWithDefaultRealm()
    # p.add_password(None, url, username, password)  # 添加用户名和密码
    # auth_handler = HTTPBasicAuthHandler(p)  # 实例化HTTPBasicAuthHandler对象，建立了一个处理验证的handler
    # opener = build_opener(auth_handler)  # 利用上面的handler并使用build_opener()方法构建一个Opener，这个Opener在发动请求时
    # 就相当于已经验证成功了

    # try:
    #     result = opener.open(url)
    #     html = result.read().decode('utf-8')
    #     print(html)
    # except URLError as e:
    #     print(e.reason)

    """
    代理
    ProxyHandler:用于设置代理，默认代理为空
    """
    # 在本地搭建代理
    # proxy_handler = ProxyHandler({
    #     'http': 'http://127.0.0.1:9743',
    #     # 一下会出现错误[WinError 10061] 由于目标计算机积极拒绝，无法连接。
    #     # 原因：其实只用设置一种代理IP地址即可，https简单点说就是http的安全版，因此只需设置一种IP。
    #     'https': 'https://127.0.0.1:9743'
    # })
    # opener = build_opener(proxy_handler)
    # try:
    #     response = opener.open('https://www.baidu.com')
    #     print(response.read().decode('utf8'))
    # except URLError as e:
    #     print(e.reason)

    """
    cookies
    """
    # 获取网站的Cookies
    # cookie = http.cookiejar.CookieJar()  # 首先声明CookieJar对象
    # handler = request.HTTPCookieProcessor(cookie)  # 构建一个handler
    # opener = request.build_opener(handler)  # 构建出Opener
    # response = opener.open('http://www.baidu.com')
    # for item in cookie:
    #     print(item.name+'='+item.value)

    # 将cookie输出成文件格式
    filename = 'cookies.txt'
    # cookie = http.cookiejar.MozillaCookieJar(filename)  # 生成文件时用到MozillaCookieJar,是CookieJar的子类，可以用来处理
    # Cookie和文件的相关事件，如读取和保存Cookies，可以将Cookies保存成Mozilla型浏览器的Cookies格式

    # 保存成LWP格式的Cookies文件
    # cookie = http.cookiejar.LWPCookieJar(filename)
    # handler = request.HTTPCookieProcessor(cookie)
    # opener = request.build_opener(handler)
    # response = opener.open('http://www.baidu.com')
    # cookie.save(ignore_discard=True, ignore_expires=True)

    """
    利用上面生成的cookies文件
    """
    # cookie = http.cookiejar.LWPCookieJar()
    # cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)  # load方法读取本地cookie文件
    # handler = request.HTTPCookieProcessor(cookie)
    # opener = request.build_opener(handler)
    # response = opener.open('http://www.baidu.com')
    # print(response.read().decode('utf-8'))

    """
    异常处理
    """
    '''URLError'''
    '''URLError类的使用，来自urllib库的error模块，继承自OSError，有reason属性，返回错误原因'''
    # try:
    #     response = request.urlopen('https://cuiqingcai.com/index.htm')  # 打开一个不存在的页面
    # except error.URLError as e:
    #     print(e.reason)

    '''HTTPError'''
    '''URLError的子类，用来处理HTTP请求错误，3个属性：
    code：返回HTTP状态码
    reason：返回错误原因
    headers：返回请求头
    '''
    # try:
    #     response = request.urlopen('https://cuiqingcai.com/index.htm')
    # except error.HTTPError as e:
    #     print(e.reason, e.code, e.headers, sep='\n')
    #
    # '''HTTPError是URLError的子类，所以先捕获子类，在捕获父类的错误'''
    # try:
    #     response = request.urlopen('https://cuiqingcai.com/index.htm')
    # except error.HTTPError as e:
    #     print(e.reason)
    # except error.URLError as e:
    #     print(e.reason)
    # else:
    #     print('Request Successfully')

    '''reason属性不一定返回字符串，也可能是对象'''
    # try:
    #     response = request.urlopen('https://cuiqingcai.com/index.htm')
    # except error.URLError as e:
    #     print(type(e.reason))
    #     if isinstance(e.reason, socket.timeout):
    #         print('TIME OUT')

    """
    解析链接，主要是urllib库中的parse模块
    它定义了处理URL的标准接口，例如实现URL各部分的抽取，合并以及链接转换
    """
    '''urlparse():urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)'''

    '''实现URL的识别和分段'''
    # result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
    # ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
    #             协议，          域名，                  访问路径，           参数，          查询条件，     锚点
    # 标准链接格式：scheme://netloc/path;params?query#fragment
    # print(type(result), result)

    '''scheme参数，默认协议。如果链接没有带协议信息，就会将这个作为默认协议.只有在URL中不包含scheme信息时才生效'''
    # result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
    # 只有在URL中不包含scheme信息时才生效
    # result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', scheme='https')
    # ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
    # print(result)

    '''allow_fragments:是否忽略fragment。如果是False，fragment部分就会被忽略'''
    # result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
    # print(result)

    '''假设url中不包含params和query，fragment就会被解析为path的一部分'''
    # result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
    # print(result)

    '''ParseResult是一个元祖'''
    # result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
    # print(result.scheme, result[0], result.netloc)

    '''urlunparse()
    它的参数是一个可迭代对象，且长度必须是6，否则会抛出异常。
    '''
    # data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
    # print(urlunparse(data))
    # data也可以是其他数据结构，如元祖

    '''urlsplit()
    和urlparse()很相似，只不过不单独解析参数params部分，它只返回5个结果
    '''
    # result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
    # print(result)
    # 结果：SplitResult(scheme='http', netloc='www.baidu.com', path='/index.html;user', query='id=5', fragment='comment')
    # SplitResult也是一个元祖类型
    # print(result.scheme, result[1])

    '''urlunsplit()
    和urlunparse()相似，将链接的各个部分整合起来，传入可迭代对象，如列表，元祖，只不过长度是5
    '''
    # data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
    # print(urlunsplit(data))  # http://www.baidu.com/index.html?a=6#comment

    '''urljoin()
    第一个参数base_url，将新的链接作为第二个参数，该方法会分析base_url的scheme、netloc、path这三个内容并对新链接确实部分进行补充
    '''
    # print(urljoin('http://www.baidu.com', 'FAQ.html'))
    # print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
    # print(urljoin('http://www.baidu.com/about.html', 'https://caiqingcai.com/FAQ.html'))
    # print(urljoin('http://www.baidu.com', 'https://caiqingcai.com/FAQ.html?question=2'))
    # print(urljoin('http://www.baidu.com?wd=abc', 'https"//cuiqingcai.com/index.php'))
    # print(urljoin('http://www.baidu.com', '?category=2#comment'))
    # print(urljoin('www.baidu,com', '?category=2#comment'))
    # print(urljoin('www.baidu.com#commnet', '?category=2'))
    # base_url提供了三项内容，如果这3项在新的链接里不存在，就补充，否则使用新的链接部分

    '''urlencode()构造GET请求参数时用'''
    # 用字典将参数表示出来
    # params = {
    #     'name': 'smile',
    #     'age': 22
    # }
    # base_url = 'http://www.baidu.com?'
    # url = base_url + urlencode(params)  # 序列化为GET请求参数
    # print(url)

    '''parse_qs()
    和urlencode()方法相反。反序列化，将GET的请求参数转换为字典
    '''
    # query = 'name=germey&age=22'
    # print(parse_qs(query))

    '''parse_qsl()
    将参数转化为元祖组成的列表
    '''
    # query = 'name=germey&age=22'
    # print(parse_qsl(query))

    '''quote()
    将内容转换为URL编码的格式，URL带有中文参数时，可能导致乱码的问题，用该方法将中文字符转换为URL编码
    '''
    # keyword = '壁纸'
    # url = 'https://www.baidu.com/s?wd=' + quote(keyword)
    # print(url)

    '''unquote()
    URL解码
    '''
    # url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
    # print(unquote(url))

    """
    分析Robots协议
    """
    '''
    can_fetch() + read()
    '''
    # rp = RobotFileParser()
    # rp = RobotFileParser('http://www.jianshu.com/robots.txt')
    # rp.set_url('http://www.jianshu.com/robots.txt')
    # rp.read()
    # print(rp.can_fetch('*', 'http://lol.qq.com/web201310/info-heros.shtml'))
    # print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))
    '''
    can_fetch() + parse()
    '''
    # rp = RobotFileParser()
    # rp.parse(urlopen('http://www.jianshu.com/robots.txt').read().decode('utf-8').split('\n'))
    # print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))


if __name__ == '__main__':
    main()
