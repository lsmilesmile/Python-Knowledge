# 关于MongoDB的一些操作
import pymongo
from bson.objectid import ObjectId


def main():
    '''创建MongoDB连接对象'''
    # client = pymongo.MongoClient('mongodb://localhost:27017/')
    client = pymongo.MongoClient(host='localhost', port=27017)

    '''指定数据库'''
    db = client.test
    # db = client['test']

    '''指定集合，声明collection对象'''
    collection = db.students
    # collection = db['students']

    '''插入数据 - insert()'''
    student1 = {
        'id': '20170101',
        'name': 'Jordan',
        'age': 20,
        'gender': 'male'
    }
    # 一次插入一条数据
    # result = collection.insert(student1)  # 返回每一条数据的_id属性
    # print(result)
    # 一次插入多条数据
    student2 = {
        'id': '20170102',
        'name': 'smile',
        'age': 20,
        'gender': 'male'
    }
    student3 = {
        'id': '20180103',
        'name': 'Mike',
        'age': 23,
        'gender': 'male'
    }
    student4 = {
        'id': '20180105',
        'name': 'hello',
        'age': 21,
        'gender': 'female'
    }
    student5 = {
        'id': '20180104',
        'name': 'jack',
        'age': 20,
        'gender': 'male'
    }
    # result = collection.insert([student2, student3, student4, student5])
    # print(result)

    '''插入数据 - insert_one()、insert_many()
    inserted_id,inserted_ids可以获得插入数据的id列表'''
    # 一次插入一条数据
    result = collection.insert_one(student1)
    print(result)
    print(result.inserted_id)
    # 一次插入多条数据
    result = collection.insert_many([student2, student3, student4, student5])
    print(result)
    print(result.inserted_ids)

    # '''查询
    # find_one() - 查询的到的是单个 结果；
    # find() - 返回一个生成器对象
    # '''
    # 查询一条数据
    result = collection.find_one({'name': 'Mike'})
    print(type(result))  # <class 'NoneType'> 不存在返回None
    print(result)  # None
    # 根据ObjectId来查询
    result = collection.find_one({'_id': ObjectId('5bb22257cebd3e29a0059a82')})
    print(result)
    # 查询多条数据 - 年龄等于20的数据
    results = collection.find({'age': 20})
    print(results)  # <pymongo.cursor.Cursor object at 0x000002E2AB6D0FD0>
    for result in results:
        print(result)
    # 查询所有数据
    results = collection.find()
    for result in results:
        print(result)
    # 查询年龄大于20的数据 - $gt：大于
    results = collection.find({'age': {'$gt': 20}})
    print(results)
    for result in results:
        print(result)
    # 正则匹配($regex - 指定正则匹配) - 查询以M开头的学生数据
    results = collection.find({'name': {'$regex': '^M.*'}})
    for result in results:
        print(result)

    # '''计数 - count()'''
    # 统计所有数据
    count = collection.find().count()
    print(count)
    # 统计符合某个条件的数据
    count = collection.find({'age': 20}).count()
    print(count)

    # '''排序 - sort(排序字段, 升降序标志)
    # pymongo.ASCENDING - 升序
    # pymongo.DESCENDING - 降序
    # '''
    results = collection.find().sort('name', pymongo.ASCENDING)
    print([result['name'] for result in results])

    # '''偏移 - skip(nums)：偏移nums个元素，则忽略前nums个元素'''
    results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
    print([result['name'] for result in results])

    # '''指定要提取的结果数 - limit(nums):提取nums个'''
    results = collection.find().sort('name', pymongo.ASCENDING).skip(1).limit(2)
    print([result['name'] for result in results])  # 列表推导式

    # '''更新 - update()'''
    condition = {'name': 'smile'}
    student = collection.find_one(condition)  # 查出符合条件的数据
    print(student)
    student['age'] = 10  # 修改该数据中的一个字段
    result = collection.update(condition, student)  # 传入原始条件和修改后的数据
    print(result)  # {'n': 1, 'nModified': 1, 'ok': 1.0, 'updatedExisting': True} - ok:成功，nModified:影响的条数
    # '''更新 - update_one(),update_many()'''
    # '''update_one()'''
    condition = {'name': 'jack'}  # <class 'dict'>
    student = collection.find_one(condition)
    student['age'] = 12
    result = collection.update_one(condition, {'$set': student})
    print(result, type(result))  # <class 'pymongo.results.UpdateResult'>
    # matched_count:获得匹配的数据条数, modified_count:影响的数据条数
    print(result.matched_count, result.modified_count)

    condition = {'age': {'$gt': 20}}
    result = collection.update_one(condition, {'$inc': {'age': 1}})  # 将第一个符合条件的数据的年龄加1
    print(result)
    print(result.matched_count, result.modified_count)
    '''update_many()'''
    condition = {'age': {'$gt': 20}}
    result = collection.update_many(condition, {'$inc': {'age': 1}})
    print(result)
    print(result.matched_count, result.modified_count)

    '''删除'''
    '''remove()'''
    result = collection.remove({'name': 'smile'})
    print(result)
    '''delete_one()'''
    result = collection.delete_one({'name': 'hello'})
    print(result)
    print(result.deleted_count)
    '''delete_many()'''
    result = collection.delete_many({'age': {'$lt': 23}})
    print(result.deleted_count)







if __name__ == '__main__':
    main()
