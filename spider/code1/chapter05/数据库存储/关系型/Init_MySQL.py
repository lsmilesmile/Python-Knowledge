import pymysql


def main():
    """
    连接数据库
    """
    # 声明MySQL连接对象
    db = pymysql.connect(host='localhost', user='root',
                         passwd='123123', port=3306)
    cursor = db.cursor()  # 获得MySQL的操作游标，利用游标执行sql语句
    cursor.execute('SELECT VERSION()')  # 获取数据库版本
    data = cursor.fetchone()
    print('Database version:', data)
    # 创建数据库
    cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")  # 创建一个数据库
    db.close()


if __name__ == '__main__':
    main()
