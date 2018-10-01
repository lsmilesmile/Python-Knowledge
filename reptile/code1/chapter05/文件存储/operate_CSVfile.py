"""
CSV - 其文件以特定字符分隔的纯文本形式存储表格数据。
id,name,age
10001,smile,21
10002,felix,21
......
"""
import csv


def main():
    """
    写入
    """
    # 打开csv文件，获得文件句柄
    with open('./data.csv', 'w', newline='') as csvfile:  # newline='' - 不加该参数文件中每行后会多出一个空行
        writer = csv.writer(csvfile)  # writer() - 初始化写入对象，传入该句柄
        writer.writerow(['rid', 'name', 'age'])  # writerow() - 传入每行数据
        writer.writerow(['10001', 'Mike', '21'])
        writer.writerow(['10002', 'Bob', '21'])
        writer.writerow(['10003', 'Jordan', '21'])

    '''
    默认写入的数据是以逗号‘,’分隔的，可以修改 - writer()的delimiter参数
    '''
    with open('./data2.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ')  # 空格分隔
        writer.writerow(['id', 'name', 'age'])  # writerow() - 传入每行数据
        writer.writerow(['10001', 'Mike', '21'])
        writer.writerow(['10002', 'Bob', '21'])
        writer.writerow(['10003', 'Jordan', '21'])

    '''
    writerows(二维列表) - 同时写入多行
    '''
    with open('./data3.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'name', 'age'])
        writer.writerows([['10001', 'Mike', 21], ['10002', 'Bob', 21], ['10003', 'Jordan', 21]])

    '''
    将字典类型的数据写入csv文件
    '''
    with open('./data4.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'name', 'age']  # 定义三个字段
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  # 初始化字典写入对象
        writer.writeheader()  # 写入头信息
        writer.writerow({'id': '10001', 'name': 'Mike', 'age': 21})
        writer.writerow({'id': '10002', 'name': 'Bob', 'age': 21})
        writer.writerow({'id': '10003', 'name':'Jordan', 'age': 21})

    '''
    追加方式写入含有中文的数据
    '''
    with open('./data4.csv', 'a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['id', 'name', 'age']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'id': '10005', 'name': '小明', 'age': 21})

    """
    读取csv文件
    """
    with open('./data4.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)  # 构造Reader对象
        for row in reader:
            print(row)

if __name__ == '__main__':
    main()
