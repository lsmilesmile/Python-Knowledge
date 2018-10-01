"""
正则表达式
"""
import re


def main():

    """
    match() - 传入正则表达式和要匹配的字符串。从字符串的起始位置匹配正则表达式，不匹配的话匹配None
    :return:
    """
    content = 'Hello 1234567 World_This is a Regex Demo'
    # print(len(content))
    # result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
    # print(result)  # 匹配成功的对象
    # print(result.group())
    # print(result.span())  # 匹配成功的范围

    """
    匹配目标
    """
    # result = re.match('^Hello\s(\d+)\sWorld', content)  # (\d+)是子组
    # print(result)
    # print(result.group())
    # print(result.group(1))
    # print(result.span())

    """
    通用匹配:'.'：匹配任意字符（除换行符）；'*'：代表匹配前面的字符无数次
    """
    # content = 'Hello 123 4567 World_This is a Regex Demo'
    # result = re.match('^Hello.*Demo$', content)
    # print(result)
    # print(result.group())
    # print(result.span())

    """
    贪婪与非贪婪
    """
    '''贪婪匹配'''
    # content = 'Hello 1234567 World_This is a Regex Demo'
    # result = re.match('^He.*(\d+).*Demo$', content)
    # print(result)
    # print(result.group())
    # print(result.group(1))
    # 这里我们想匹配到‘1234567’，可是结果就是一个‘7’，在贪婪匹配下，‘.*’会尽可能地匹配更多的字符，‘.*’后面的’\d+‘至少
    # 匹配一个数字，所以’.*‘就把’123456‘给匹配了
    '''非贪婪匹配'''
    # result = re.match('^He.*?(\d+).*Demo$', content)
    # print(result)
    # print(result.group())
    # print(result.group(1))

    """
    修饰符
    """
    # content = '''Hello 1234567 World_This
    # is a Regex Demo'''
    # result = re.match('^He.*?(\d+).*?Demo$', content, re.S)  # ‘.’匹配除了换行符之外的任意字符，所以要加上修饰符‘re.S’
    # print(result.group(1))

    '''转义匹配'''
    # content = '(百度)www.baidu.com'
    # result = re.match('\(百度\)www\.baidu\.com', content)
    # print(result)

    """
    search()：扫描整个字符串，返回第一个成功匹配的结果。没有找到就返回None
    """


    """
    compile()：这个方法可以将正则字符串编译成正则表达式对象，以便在后面的匹配中复用
    """
    content1 = '2016-12-15 12:00'
    content2 = '2016-12-17 13:00'
    content3 = '2016-12-22 13:21'
    pattern = re.compile('\d{2}:\d{2}')
    result = re.sub(pattern, '', content1)
    print(result, len(result))
    print('' in result)



if __name__ == '__main__':
    main()
