"""
类定义实例：学校人事管理系统
"""

#定义两个简单的类：类型和值异常
import datetime
from error import PersonValueError, PersonTypeError


class Person(object):
    _num = 0           #统计在程序运行中建立的人员对象的个数，每当创建这个类的对象就加一

    #公有的属性
    def __init__(self, name, sex, birthday, ident):
        #判断名字的类型和性别的取值是否正确
        if not (isinstance(name, str) and sex in ("女", "男")):
            raise PersonValueError(name, sex)
        try:
            birth = datetime.date(*birthday)   #生成一个日期对象
        except:
            raise PersonValueError('Wrong date:', birthday)
        self._name = name
        self._sex = sex
        self._birthday = birth
        self._id = ident
        Person._num += 1                #实例计数

    def id(self):
        return self._id
    def name(self):
        return self._name
    def sex(self):
        return self._sex
    def birthday(self):
        return self._birthday
    def age(self):
        return (datetime.date.today().year - self._birthday.year)

    def set_name(self, value):    #修改名字
        if not isinstance(self._name, str):
            self._name = value

    def __lt__(self, other):
        if not isinstance(other, Person):
            raise PersonTypeError
        return self._id < other._id

    #类方法，取得类中的人员计数值
    @classmethod
    def num(cls):
        return Person._num

    #输出的方法,__str__提供对象的基本信息，details提供完整细节
    """
    __str__返回的是一个字符串，所以要输出对象的多个属性时，就用join方法把一个元祖或者列表里的几个字符串连接起来就行，
    注意：整型变量要先变成字符串
    """
    def __str__(self):
        return " ".join((self._id,self._name, self._sex, str(self._birthday)))

    def details(self):
        return ",".join(("编号：" + self._id,
                         "姓名：" + self._name,
                         "性别：" + self._sex,
                         "出生日期：" + str(self._birthday)))