import datetime
from error import PersonValueError, PersonTypeError
from person import Person

class Student(Person):
    _id_num = 0            #计数器，生成学号

    @classmethod
    #生成学号
    def _id_gen(cls):
        cls._id_num += 1
        year = datetime.date.today().year
        return "1{:04}{:05}".format(year, cls._id_num)

    def __init__(self, name, sex, birthday, department = None):
        super().__init__(name, sex, birthday, Student._id_gen())
        self._department = department              #院系
        self._enroll_date = datetime.date.today()  #报道日期
        self._courses = {}      #空字典，记录课程学习成绩

    def set_course(self, course_name):
        self._courses[course_name] = None

    def set_score(self, course_name, score):
        if course_name not in self._courses:
            raise PersonValueError('No this course selected:', course_name)
        self._courses[course_name] = score
    #给出所有成绩的列表，用一个表描述
    def score(self):
        return [(cname, self._courses[cname]) for cname in self._courses]

    def details(self):
        return '.'.join((Person.details(self),
                         "入学日期：" + str(self._enroll_date),
                         "院系：" + self._department,
                         "课程记录：" + str(self.score())))