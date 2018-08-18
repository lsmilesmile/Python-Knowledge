import datetime
from error import PersonValueError, PersonTypeError
from person import Person
class Staff(Person):
    _id_num = 0
    @classmethod
    def _id_gen(cls, birthday):   #实现职工号生成规则
        cls._id_num += 1
        birth_year = datetime.date(*birthday).year
        return "0{:04}{:05}".format(birth_year, cls._id_num)  #0+4位（不够前面用0补齐）+ 5位（不够前面用0补齐）

    def __init__(self, name, sex, birthday, entry_date = None):
        super().__init__(name, sex, birthday,
                         Staff._id_gen(birthday))
        if entry_date:
            try:
                self._entry_date = datetime.date(*entry_date)
            except:
                raise PersonValueError("Wrong date:", entry_date)
        else:
            self._entry_date = datetime.date.today()

        """
        子类的属性不一定都要放到初始化里，因为有些还不确定，所以不必刚创建对象时就初始化完成
        """
        self._salary = 1720           #默认为最低工资
        self._department = "未定"      #另行设定
        self._position = "未定"        #另行设定

    def set_salary(self, amount):
        if not type(amount) is int:
            raise TypeError
        self._salary = amount

    def set_position(self, position):
        self._position = position

    def set_department(self, department):
        self._department = department

    def details(self):
        return '.'.join((super().details(),
                         "入职日期：" + str(self._entry_date),
                         "院系：" + self._department,
                         "职位：" + self._position,
                         "工资：" + str(self._salary)))