from pyquery import PyQuery as pq
import requests


def main():
    doc = pq(url='https://cuiqingcai.com')  # PyQuery对象首先请求该URL，然后用得到的HTML内容完成初始化
    print(doc('title'))
    # 下面的方法也是一样
    doc1 = pq(requests.get('https://cuiqingcai.com').text)
    print(doc1('title'))

    '''文件初始化'''
    doc2 = pq(filename='demo.html')
    print(doc2('li'))


if __name__ == '__main__':
    main()
