import requests
import re
import logging

from requests.packages import urllib3
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1

def main():

    """
    简单示例
    :return:
    """
    # r = requests.get('https://www.baidu.com/')  # urllib库中的urlopen()以GET方法请求网页，这里直接用get()
    # print(type(r))  # <class 'requests.models.Response'>
    # print(r.status_code)  # 200
    # print(type(r.text))  # <class 'str'>
    # print(r.text)
    # print(r.cookies)  # <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
    '''
    一句话完成请求
    '''
    # r1 = requests.post('http://httpbin.org/post')
    # r2 = requests.put('http://httpbin.org/put')
    # r3 = requests.delete('http://httpbin.org/delete')
    # r4 = requests.head('http://httpbin.org/get')
    # r5 = requests.options('http://httpbin.org/get')

    """
    基本用法
    """

    """
    GET请求
    """
    # r = requests.get('http://httpbin.org/get')
    # print(r.text)
    '''给GET请求添加额外信息：
    1、利用params传参；
    2、直接写'''
    # r = requests.get('http://httpbin.org/get?name=smile&age=22')  # 直接写
    # 利用params传参
    # data = {
    #     'name': 'smile',
    #     'age': 22
    # }
    # r = requests.get('http://httpbin.org/get', params=data)
    # print(r.text)
    '''得到字典格式的返回结果
    网页返回类型是str，是JSON格式的，用json()方法将其解析为字典格式
    '''
    # r = requests.get('http://httpbin.org/get')
    # print(r.text)
    # print(type(r.text))
    # print(r.json())
    # print(type(r.json()))

    '''抓取网页知乎->发现'''
    # headers = {
    #     # 浏览器标识
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    #                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    # }
    # r = requests.get("https://www.zhihu.com/explore", headers=headers)  # 知乎->发现
    # pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
    # titles = re.findall(pattern, r.text)
    # print(titles)

    '''抓取二进制数据github站点图标，音频、视频文件同理'''
    # r = requests.get('https://github.com/favicon.ico')
    # print(r.text)  # 将图片直接用str输出会出现乱码
    # print(r.content)  # 二进制文件
    # 保存图片
    # with open('favicon.ico', 'wb') as f:
    #     f.write(r.content)

    '''添加headers，比如User-Agent信息，否则不能正常请求'''
    # headers = {
    #     # 浏览器标识
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    #                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    # }
    # r = requests.get("https://www.zhihu.com/explore", headers=headers)  # 知乎->发现
    # print(r.text)

    """
    POST请求
    """
    # data = {'name': 'smile', 'age': 22}
    # r = requests.post("http://httpbin.org/post", data=data)
    # print(r.text)

    """
    响应
    """
    r = requests.get('http://www.jianshu.com')
    # print(type(r.status_code), r.status_code)  # 状态码
    # 比较返回的状态码和内置的成功的状态码page128
    # exit() if not r.status_code == requests.codes.ok else print('Request Successfully')
    # print(type(r.headers), r.headers)  # 响应头
    # print(type(r.cookies), r.cookies)  # cookies
    # print(type(r.url), r.url)
    # print(type(r.history), r.history)  # 请求历史

    """
    高级用法
    """

    '''上传文件'''
    # files = {'file': open('favicon.ico', 'rb')}
    # r = requests.post('http://httpbin.org/post', files=files)
    # print(r.text)

    '''获取cookies'''
    # r = requests.get("https://www.baidu.com")
    # print(r.cookies)
    # for key, value in r.cookies.items():
    #     print(key + '=' +value)

    '''用cookie来维持登录状态'''
    # headers = {
    # 登录后获取cookies
    #     'Cookie': 'l_n_c=1; q_c1=e0f1c70edf0146aea964965527bc1569|1537350127000|1537350127000; _xsrf=48e2d1442879145856d2c97989b307ac; r_cap_id="YzkwZTlhNWZkY2ZlNDZlNWE4NTE4OWY5MTYyNzlkN2Q=|1537350127|a26fc3a696d32148217011c553ddb5a816853189"; cap_id="ODYwYmRhYjQ2MDAxNDY3NTg4MWVhZmQ2YTdkYWI2NjQ=|1537350127|b9cfffd5c6fc9808074af53f7bb842a603ae5518"; l_cap_id="NTJjMGZlYWYwYjM4NGE0Y2ExNzRkY2U3ODQ1ZDIyY2E=|1537350127|8be183616949b141b7bc12c9cfef8b1bd5b9e1f7"; n_c=1; d_c0="ALCm5QNhPA6PTtSHf4ZSI6ivPDCTatwxLEo=|1537350132"; __utmc=51854390; _zap=4decb161-7987-42bc-9e62-075193b25e4d; tgw_l7_route=931b604f0432b1e60014973b6cd4c7bc; capsion_ticket="2|1:0|10:1537352625|14:capsion_ticket|44:YTYyN2U5N2I1MjRlNGVjZWIwNzZkM2VlMzA1YWIzYTE=|63804f3809db209bd4cfa4f6cb4b0809f201fcbd6d768efed55f8859d04ecd3b"; z_c0="2|1:0|10:1537352642|4:z_c0|92:Mi4xUUlCRURBQUFBQUFBc0tibEEyRThEaVlBQUFCZ0FsVk53bkdQWEFCVndhT1cydUhrSk1BQ2ZlRFdMUU8xb00yZmxR|fcbdc7e00f9f1b88ee390e6dff2c1a7a9d79473d0213df13363a07db5168bd53"; _xsrf=v3TxRrCQYPcIJXl3pMuTFvMqEbSDL1VS; __utma=51854390.1635380692.1537350237.1537350237.1537352753.2; __utmb=51854390.0.10.1537352753; __utmz=51854390.1537352753.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/signin; __utmv=51854390.100--|2=registration_date=20180919=1^3=entry_date=20180919=1; tst=r',
    #     'Host': 'www.zhihu.com',
    #     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) '
    #                   'AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
    # }
    # r = requests.get('https://www.zhihu.com', headers=headers)
    # print(r.text)  # 输出的登录后的页面结果

    '''会话维持，可以两次设置相同的cookies去请求，但是相当繁琐，用到Session对象,常用语模拟登录后的下一步操作'''
    # s = requests.Session()
    # s.get('http://httpbin.org/cookies/set/number/123456789')  # 设置名为number的cookie，值为123456789
    # r = s.get('http://httpbin.org/cookies')
    # print(r.text)

    '''SSL证书验证,   12306的证书没有被官方CA机构信任'''
    # response = requests.get('https://www.12306.cn')
    # print(response.status_code)  # SSLSError
    # 解决上述证书验证错误，把verify参数设置为False，默认是True
    # response = requests.get('https://www.12306.cn', verify=False)
    # print(response.status_code)
    # 输出
    # C:\Users\lsmil\Desktop\reptile\venv\lib\site-packages\urllib3\connectionpool.py:857:
    # InsecureRequestWarning: Unverified HTTPS request is being made.
    # Adding certificate verification is strongly advised.
    # See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
    #   InsecureRequestWarning)

    '''上面的警告要求我们最好提供指定证书，可以屏蔽警告：urllib3.disable_warnings()'''
    # urllib3.disable_warnings()
    # response = requests.get('https://www.12306.cn', verify=False)
    # print(response.status_code)

    '''捕获警告到日志的方式忽略警告'''
    # logging.captureWarnings(True)
    # response = requests.get('https://www.12306.cn', verify=False)
    # print(response.status_code)

    '''代理设置'''
    # proxies = {
    #     'http': 'http://10.10.1.10:3128',
    #     'https': 'http://10.10.1.10:1080'
    # }
    # r = requests.get('https:www.taobao.com', proxies=proxies)

    '''超时设置'''
    # r = requests.get('https://www.taobao.com', timeout=0.00001)
    # print(r.status_code)
    # 请求分为连接和读取两个阶段，可以为其设置timeout,传入一个元祖
    # r = requests.get('https://www.taobao.com', timeout=(5, 11))
    # print(r.status_code)

    # 不设置超时，永久等待
    # r = requests.get('https://www.taobao.com', timeout=None)
    # r = requests.get('https://www.taobao.com')

    '''身份认证'''
    # requests自带的身份认证功能
    # 用户名和密码正确的话就会自动认证成功
    # r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
    # 或者
    # r = requests.get('http://localhost:5000', auth=('username', 'password'))
    # print(r.status_code)

    # OAuth认证
    # url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    # auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
    #               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
    # requests.get(url, auth=auth)










if __name__ == '__main__':
    main()
