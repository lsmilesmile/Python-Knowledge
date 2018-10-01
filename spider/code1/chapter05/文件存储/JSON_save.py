import json


def main():
    """
    读取JSON
    """
    # JSON的数据需要使用双引号来包围，不能使用单引号
    str = '''
    [{
        "name": "Bob",
        "gender": "male",
        "birthday": "1992-10-18"
    }, {
        "name": "Selina",
        "gender": "female",
        "birthday": "2-12-12-11"
    }]
    '''
    print(type(str))
    data = json.loads(str)  # 将字符串转换成JSON对象
    print(data)
    print(data[0]['gender'], data[0].get('gender'))  # 这两种表示方式效果相同
    print(data[0].get('age'))  # None
    print(data[0].get('age', 34))  # 34（这儿返回默认的34）
    print(type(data))

    '''从JSON文件中读取数据'''
    with open('./data.json', 'r') as f:
        str1 = f.read()
        data = json.loads(str1)
        print(data)

    """
    输出JSON
    """
    # dumps() - 将JSON对象转换成字符串。
    data = [{
        'name': 'Bob',
        'gender': 'male',
        'birthday': '1992-10-12'
    }]
    # 将JSON对象转换成字符串放入文件中
    with open('./data2.json', 'w') as f:
        f.write(json.dumps(data))
    # 将该转换后的字符串保存为JSON格式
    with open('./data3.json', 'w') as f:
        f.write(json.dumps(data, indent=2))

    """
    JSON中包含中文字符
    """
    data = [{
        'name': '王伟',
        'gender': '男',
        'birthday': '1992-12-11'
    }]
    with open('./data4.json', 'w') as f:
        f.write(json.dumps(data, indent=2))  # 这时中文会变成Unicode字符

    # 解决办法
    with open('./data5.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=2, ensure_ascii=False))



if __name__ == '__main__':
    main()
