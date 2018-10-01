# MySQL的一般操作
import pymysql


def main():
    '''声明MySQL的连接对象'''
    db = pymysql.connect(host='localhost', user='root',
                         password='123123', port=3306, db='spiders')
    cursor = db.cursor()

    '''创建一个students表'''
    sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
    cursor.execute(sql)

    '''插入数据 - 方法一'''
    id = '20180001'
    name = 'Bob'
    age = 20
    sql = 'INSERT INTO students(id, name, age) values (%s, %s, %s)'
    # 下面为事务的实现提供支持
    try:
        cursor.execute(sql, (id, name, age))
        db.commit()  # 真正将语句提交到数据库
    except:
        db.rollback()  # 如果执行失败，那么就回滚，相当于啥都没发生过
    '''插入数据 - 方法二,让插入数据变得更灵活'''
    data = {
        'id': '20180001',
        'name': 'Bob',
        'age': 21
    }
    table = 'students'
    keys = ','.join(data.keys())
    values = ','.join(['%s'] * len(data))   # ['%s','%s','%s']
    # INSERT INTO students(id,name,age) VALUES(%s,%s,%s)
    sql = 'INSERT INTO {table}({keys}) VALUES({values})'.format(
        table=table, keys=keys, values=values)
    try:
        if cursor.execute(sql, tuple(data.values())):
            print('Successful')
            db.commit()
    except:
        print('Failed')
        db.rollback()

    '''更新数据 - 方法一'''
    sql = 'UPDATE students SET age = %s WHERE name = %s'
    try:
        cursor.execute(sql, (25, 'Bob'))
        db.commit()
    except:
        db.rollback()

    '''更新数据 - 方法二:数据爬取过程中，我们大部分情况是插入数据
    因此我们关心有没有重复的数据，如果出现重复数据，我们希望更新，而不是重复插入'''
    data = {
        'id': '20180002',
        'name': 'foo',
        'age': 20
    }
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    # ON DUPLICATE KEY UPDATE - 如果主键已经存在，就执行更新操作，否则执行插入操作
    sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(
        table=table, keys=keys, values=values)
    update = ','.join([" {key} = %s".format(key=key) for key in data])
    sql += update
    try:
        if cursor.execute(sql, tuple(data.values()) * 2):
            print('Successful')
            db.commit()
    except:
        print('Failed')
        db.rollback()

    '''删除数据'''
    condition = 'age = 22'
    sql = 'DELETE FROM {table} WHERE ({condition})'.format(
        table=table, condition=condition)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    '''查询数据 - 方法一
    fetchone()和fetchall() - 有个指针偏移。比如使用一次fetchone()指针会向下移动一个，
    当再使用fetchall时，就会从该指针开始继续向下走，所以fetchall()不一定是获取全部数据的
    '''
    sql = 'SELECT * FROM students WHERE age  > 20'

    try:
        cursor.execute(sql)
        print('count:', cursor.rowcount)
        # fetchone() - 获取结果的第一条数据
        one = cursor.fetchone()
        print('one:', one)
        # 获取所有条记录
        results = cursor.fetchall()
        print('results:', results)
        for row in results:
            print(row)
    except:
        print('error')

    '''查询数据 - 方法二：while循环加fetchone()方法'''
    sql = 'SELECT * FROM students WHERE age > 20'
    try:
        cursor.execute(sql)
        row = cursor.fetchone()
        while row:
            print('Row:', row)
            row = cursor.fetchone()
    except:
        print('error')


if __name__ == '__main__':
    main()
