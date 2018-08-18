from person import Person
from student import Student
from staff import Staff

def main():

    p1 = Person('felix', "男", (1994, 11, 15), '14434216')
    p2 = Person('刘笑', "男", (1993, 4, 5), '14434213')
    p3 = Person('小明', "男", (1994, 5, 15), '14434234')
    p4 = Person('刘红', "女", (1993, 1, 5), '14434201')
    plist = [p1, p2, p3, p4]
    for p in plist:
        print(p)
    #按照编号对人员进行排序
    plist.sort()
    for p in plist:
        print(p.details())

    print('People created:', Person.num(), '\n')

    p5 = Staff("张", "女", (1974, 10, 16))
    print(p5)
    p5.set_department("数学")
    p5.set_position("副教授")
    p5.set_salary(30000)

    print(p5.details())

    p6 = Student("gg", "女", (1994, 11, 15), "计算机")
    print(p6)
    print(p6._enroll_date)
    p6.set_course("微积分")
    print(p6._courses)
    p6.set_course("c")
    print(p6._courses)
    p6.set_score("c", 66)
    print(p6.score())
    print(p6.details())



if __name__ == '__main__':
    main()