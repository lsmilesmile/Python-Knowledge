# 类

> [TOC]
>
> 



## 1 - 面向对象简介（OOP）

### 1.1 万物皆对象

​	面向对象就是通过面向对象分析和设计，建立模型（类或对象）并完成最终的程序设计过程。因此在面向对象编程中，编程的主题就是用类或对象构建模型，并使它们之间可以相互通信以解决实际问题。

### 1.2 好处

- 封装 - 将对象的属性和方法封装起来，需要对外展示的，其他对象才能得到或使用它，而不需要对外展示的细节，则隐藏在对象的颞部。
- 继承 - 通过获取父类的属性和方法，再加上自定义的属性和方法成为一个类的子类。
- 多态 - 对于不同的对象，总能有一定的解决办法，并且能得到想要的结果。



## 2 - 类和对象

### 2.1 定义类

语法形式：

**class <类名>(父类名):**

​    **pass**

在Python3.x中，一般定义的类主要继承object类，所以父类名一般是object。我们可以通过dir()看见从object类继承到的属性和方法：

```Python
class Test(object):
    pass
print(dir(Test))

"""
结果
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
"""
```

可以看到这些继承过来的方法

### 2.2 使用类

​	类在定以后必须先实例化才能使用，类的实例化跟函数的调用雷士，只要使用类名加圆括号的形式就可以实例化一个类。

代码示例：

```Python
class Myclass(object):  #定义一个类
    "Myclass."          #该类只有说明信息没有语句

myclass = Myclass()     #实例化一个类
print(myclass.__doc__)  #输出类实例myclass的属性__doc__的值
print(help(myclass))
"""
结果
Myclass.
Help on Myclass in module __main__ object:

class Myclass(builtins.object)
 |  Myclass.
 |  
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

None
"""
```

### 2.3 类的属性和方法

#### 2.3.1 类的方法

类中的方法定义和调用与函数定义与调用的方式基本相同，区别有：

- 方法的第一个参数必须是self，而且不能省略，**它代指对象本身**；
- 方法的调用需要实例化类，并且以实例名.方法名形式调用；
- 整体进行一个单位的缩进，表示属于类中的内容。

代码实例：

```Python
class People(object):
    def myname(self):
        return 'my name is felix'
    
    def add_fun(self, x, y):
        return(x+y)
    
people = People()
print(people.myname())
print(people.add_fun(1, 1))
"""
my name is felix
2
"""
```

在类定义中可以定义一个特殊的构造方法，\_\_init\_\_()方法，用于类实例化的初始化，**如果这个方法中有参数，那么在实例化时就必须提供**。

代码示例：

```Python
class Test(object):
    def __init__(self, value1, value2):
        self.x = value1
        self.y = value2
    
    def fun(self):
        return self.x * self.y

test = Test(10, 9)
print(test.fun())
"""
90
"""
```

调用本类方法和全局方法：

```Python
def coord_chng(x, y):
    return (abs(x), abs(y))

class Ant(object):
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.disp_point()
        
    def move(self, x, y):
        x, y = coord_chng(x, y)
        self.edit_point(x, y)
        self.disp_point()
    
    def edit_point(self, x, y):
        self.x += x
        self.y += y
        
    def disp_point(self):
        print("当前位置：(%d, %d)" % (self.x, self.y))
        

ant = Ant()
ant.move(2, 4)
ant.move(-9, 6)
"""
当前位置：(0, 0)
当前位置：(2, 4)
当前位置：(11, 10)
"""
```

##### 2.3.1.1 构造方法

```Python
'''
构造方法:在实例化对象时,自动被调用的方法就是构造方法
格式: def __方法名__(self):
def __init__(self):

作用:一般在实例化对象时,给对象的属性进行初始化赋值操作的
构造方法可以放在类的任何位置
'''

class Cat():
    def __init__(self, user, age, color):
        self.user = user
        self.age = age
        self.color = color

    def eat(self):
        return '%s喜欢吃鱼' % self.user

    def func(self):
        print(self.user, self.age, self.color)


bosi = Cat('波斯', 4, 'yellow')
# print(bosi)
print(bosi.eat())
```

##### 2.3.1.2 析构方法

```Python
'''
析构方法: 程序执行结束后,该方法自动被调用
作用: 就是来释放内存中的数据

'''
class Person:
    def run(self):
        print('我在慢跑')

    def eat(self):
        print('你在吃鸡腿吗?')

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        print(self.weight)

    def __del__(self):
        print('我想知道你什么时候执行')
        print(self.name)

chenhe = Person('陈赫', 200)
```

#### 2.3.2 str与repr

- **区别一**

```Python
'''
str():将值或者对象转换成人所能识别的一种形式
返回值: 返回一个String的形式

repr(): 将值或者对象转换成机器所能识别的一种形式
返回值: 返回一个String的形式

两者之间的区别:
同:数字,列表, 字典, None, 布尔登类型,都具有完全相同的输出.说明机器的理解跟人的思想相同

异:对于字符串,而这输出不一致

'''
str1 = 'gebilaosong'
# print(str(str1))
# print(repr(str1))


float1 = 3.14
print(str(float1))
print(repr(float1))

num1 = 23
print(str(num1))
print(repr(num1))

list1 = [2, 3, 4]
print(str(list1))
print(repr(list1))

dict1 = {'name':'大黄', 'age': 40}
print(str(dict1))
print(repr(dict1))

tuple1 = (1, 2, 3)
print(str(tuple1))
print(repr(tuple1))


none1 = None
print(str(none1))
print(repr(none1))

boolean1 = True
print(str(boolean1))
print(repr(boolean1))
```

- **区别二**

  ```Python
  '''
  __str__:在print(object)时,该方法自动被调用, 这是给用户看的
  __repr__:是给机器查看的.
  '''
  class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age
  
      # 在print(object)时,该方法自动被调用
      # def __str__(self):
      #     return '%s-%d' % (self.name, self.age)
  
      def __repr__(self):
          return '%s-%d' % (self.name, self.age)
  
  
  zhaoliying = Person('赵丽颖', 31)
  '''
  1.如果在类中定义了__str__方法,则输出对象时该方法会被自动的调用
  2.如果在类中没有定义__str__方法,则输出对象就是在内存中的地址
  '''
  print(zhaoliying)
  print(type(zhaoliying))
  ```

#### 2.3.2 类的属性

Python中的类的属性有两类：

- 实例属性
- 类属性

实例属性即同一个类的不同实例，其值是不相关的，也不会互相影响的，定义时使用“self.属性名”，调用时也使用它；类属性则是同一个类的所有实例所共有的，直接在类体中独立定义，引用时要使用“类名.类变量名“的形式来引用。

代码示例：

```Python
class Test(object):
    name = 'Felix'
    
    def __init__(self, value = 'hello'):
        self.name = value
        
    def func1(self):
        return Test.name, self.name
    
    def chg_cname(self, ctemp):
        Test.name = ctemp
        
    def chg_sname(self, stemp):
        self.name = stemp
        
test = Test()
print('修改前的类属性和实例属性：', test.func1())
test.chg_cname('FFF')
test.chg_sname('HHH')
print('修改后的类属性和实例属性：', test.func1()[0], test.func1()[1])

"""
修改前的类属性和实例属性： ('Felix', 'hello')
修改后的类属性和实例属性： FFF HHH
"""
```

实例：

```Python
#car类
class Car(object):
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price

    def func(self):
        print('我的功能是作为交通工具')

    def __str__(self):
        return '%s, %s, %d' % (self.brand, self.color, self.price)

    def __del__(self):
        print('我是做清理工作的')


#book类
class Book(object):
    def __init__(self, subject, size, price):
        self.subject = subject
        self.size = size
        self.price = price


    def func(self):
        print('这本书的学科是%s, 价格是%d' % (self.subject, self.price))

    def __del__(self):
        print('我是做清理工作的')

#电脑类
class Computer(object):
    def __init__(self, color, brand, price):
        self.__color = color
        self.__brand = brand
        self.__price = price

    def func(self):
        return '我很喜欢%s的电脑，%s也不错，才%d元' % (self.__brand, self.__color, self.__price)

    def __str__(self):
        return '%s,%s,%d' % (self.__color, self.__brand, self.__price)

    def get_chara(self):
        return (self.__color, self.__brand, self.__price)

    def set_chara(self,value1, value2, value3):
        self.__color = value1
        self.__brand = value2
        self.__price = value3

    def __del__(self):
        print('我是做清理工作的')

#类外部的方法
def add_func(self):
    print('我是要被添加给对象的方法')


car1 = Car('audi', 'black', 3000000) #实例化对象
print(car1)                          #输出对象的属性信息
car1.func()                          #调用对象的方法
car1.length = 3                      #为对象添加属性
print(car1.length)                   #输出添加的属性

#给对象添加方法
import types

car2 = Car('jaguar', 'red', 560000)
car2.add_func = types.MethodType(add_func, car2)  #绑定方法到对象
car2.add_func()


computer1 = Computer('white', 'lenovo', 4555)     #实例化一个对象
print(computer1.func())                           #调用对象的方法
print(computer1)
#print(computer1.__color)                         #直接访问私有属性报错
print(computer1.get_chara())
computer1.set_chara('yellow', 'benchi', 869869)
print(computer1)
#del computer1
#print(computer1)

"""
audi, black, 3000000
我的功能是作为交通工具
3
我是要被添加给对象的方法
我很喜欢lenovo的电脑，white也不错，才4555元
white,lenovo,4555
('white', 'lenovo', 4555)
yellow,benchi,869869
我是做清理工作的
我是做清理工作的
我是做清理工作的
"""
```

- **slots**

  ```Python
  from types import MethodType
  class Person(object):
      # 当一个类中需要创建大量的指定的属性时,我们可以使用__slots__
      # 我们可以通过__slots__来创建指定的属性
      __slots__ = ('user', 'age', 'height', 'run')
  
  
  per = Person()
  # 动态的添加属性
  per.user = '狗蛋'
  print(per.user)
  # 该属性没有添加成功,因为在类内没有指定
  # per.weight = 180
  # print(per.weight)
  
  def pao(object):
      print(object)
      print('我在跑步')
  
  # 动态的讲方法添加到对象中
  # 方式一:没有将方法添加到对象中
  # per.run = pao
  # 使用函数名去调用方法
  # per.run(per)
  
  # 方式二
  per.run = MethodType(pao, per)
  # 使用对象.属性名作为对象的方法去调用该方法
  per.run()
  
  ```

- **@property**

  ```Python
  class Student(object):
      def __init__(self, score):
          self.__score = score
      def get_score(self):
          return self.__score
  
      def set_score(self, value):
          # 分数: 0-150 , 修改私有的属性时要有条件
          if not isinstance(value, int):
              # 不是我们需要的int类型
              print('当前您输入的分数不是int类型')
          elif value < 0 or value > 150:
              print('当前您输入的分数不在我们的区间范围内')
          else:
              self.__score = value
  
  # xiaoming = Student(50)
  # print(xiaoming.get_score())
  # xiaoming.set_score(70)
  # print(xiaoming.get_score())
  
  
  
  class Teacher(object):
      def __init__(self, salary):
          self.__salary = salary
      # 将salary方法当做一个'属性'来访问,访问的属性名就是该方法名
      #  @property表示只读
      @property
      def salary(self):
          return self.__salary
  
      # salary.setter表示既可以读也可以写
      @salary.setter
      def salary(self, value):
          # 分数: 0-150 , 修改私有的属性时要有条件
          if not isinstance(value, int):
              # 不是我们需要的int类型
              print('当前您输入的分数不是int类型')
          elif value < 0:
              print('当前您输入的分数不在我们的区间范围内')
          else:
              self.__salary = value
  
  
  
  dahuang = Teacher(1000)
  # print(dahuang.__salary)
  # print(dahuang.salary)
  
  
  # dahuang.salary(1200)
  # print(dahuang.salary)
  
  
  # 总结: 在使用对象去调用一个私有的属性时,我们一般是通过getter和setter方法来实现
  # 而在类中我们通常是@proterty来设置咱们私有属性
  # dahuang.salary = 1200
  print(dahuang.salary)
  ```

  

#### 2.3.3 类成员方法与静态方法

类的属性有类属性和实例属性之分，类的方法也有不同的种类，有：

- 实例方法
- 类方法
- 静态方法

静态方法定义时应该使用装饰器@staticmethod进行修饰，没有默认参数。类方法定义时应使用装饰器@classmethod进行修饰，必须有默认参数“cls”，代表本类。它们的调用方式可以直接由类名进行调用，调用前也可以不实例化类，当然也可以用该类的任何一个实例来进行调用。

代码示例：

```Python
class Test(object):
     @staticmethod                  #静态方法装饰器
     def static_test():
         print('this is a static method')
         
     @classmethod                   #类方法装饰器
     def class_test(cls):
         print('this is a class method')
#未实例化
Test.static_test()
Test.class_test()
#实例化
test = Test()
test.static_test()
test.class_test()
"""
this is a static method
this is a class method
this is a static method
this is a class method
"""
```

#### 2.3.4 动态添加属性和方法

```Python
from types import MethodType

class Person(object):
    pass


per = Person()

# 动态的添加属性
per.name = '豆豆'
print(per.name)

def run(self):
    print('跑步')
# 这样动态的添加方法不可以
# per.run()


per.pao = MethodType(run, per)
per.pao()
print(per.pao)
```

#### 2.3.5 运算符重载

在类中，对内置对象（例如，整数和列表）所能做的事，几乎都有相应的特殊名称的重载方法。下表列出其中一些最常用的重载方法。下面的方法格式是：\_\_name\_\_，是由于忘了加转义的\\

| **方法**           | **重载**           | **调用**                                        |
| ------------------ | ------------------ | ----------------------------------------------- |
| **init**           | 构造函数           | 对象建立：X = Class(args)                       |
| **del**            | 析构函数           | X对象收回                                       |
| **add**            | 运算符+            | 如果没有*iadd*,X+Y,X+=Y                         |
| **or**             | 运算符\|(位OR)     | 如果没有*ior*,X\|Y,X\|=Y                        |
| **repr**,**str**   | 打印、转换         | print（X）、repr(X),str(X)                      |
| **call**           | 函数调用           | X(*args,**kargs)                                |
| **getattr**        | 点号运算           | X.undefined                                     |
| **setattr**        | 属性赋值语句       | X.any = value                                   |
| **delattr**        | 属性删除           | del X.any                                       |
| **getattribute**   | 属性获取           | X.any                                           |
| **getitem**        | 索引运算           | X[key],X[i:j],没**iter**时的for循环和其他迭代器 |
| **setitem**        | 索引赋值语句       | X[key] = value,X[i:j] = sequence                |
| **delitem**        | 索引和分片删除     | del X[key],del X[i:j]                           |
| **len**            | 长度               | len(X),如果没有**bool**,真值测试                |
| **bool**           | 布尔测试           | bool(X),真测试                                  |
| **lt**,**gt**,     | 特定的比较         | X < Y,X > Y                                     |
| **le**,**ge**,     |                    | X<=Y,X >= Y                                     |
| **eq**,**ne**      |                    | X == Y,X != Y                                   |
| **radd**           | 右侧加法           | Other+X                                         |
| **iadd**           | 实地（增强的）加法 | X += Y （or else **add**）                      |
| **iter**,**next**  | 迭代环境           | I = iter(X),next(I)                             |
| **contains**       | 成员关系测试       | item in X （任何可迭代的）                      |
| **index**          | 整数值             | hex(X),bin(X),oct(X),O[X],O[X:]                 |
| **enter**,**exit** | 环境管理器         | with obj as var:                                |
| **get**,**set**    | 描述符属性         | X.attr,X.attr = value,del X.attr                |
| **new**            | 创建               | 在**init**之前创建对象                          |

### 2.4 访问权限

```Python
'''
如果不想在类外访问到类内的属性,这时我们应怎么处理?
解决办法:就是给类内的属性前边添加__

只要在类内设置属性时,给属性前边添加下划线,则该属性是属于私有属性.即在类外是没有办法访问的
'''
# 总结:通过设置私有属性来保证你类内的属性不被泄露,这样就保证了程序的安全性
# 在实际项目开发中:定义类时,所有的属性都是私有的
# 但有时根据实际情况来讲,我们需要通过类外来调用私有的属性怎么办?
# 解决办法:可以通过设置的方法解决
```



## 3 类的继承

### 3.1 单继承

​	子类继承了父类之后，就具有了父类的属性和方法，但是不能继承父类的私有属性和私有方法，子类中还可以重载父类的方法，以实现父类的不同行为和表现或能力。

代码示例1：

```Python
#类继承
class Ant(object):
    
    #构造方法
    def __init__(self, x=0, y=0, color='black'):
        self.x = x
        self.y = y
        self.color = color
    
    #模拟爬行
    def crawl(self, x, y):
        self.x = x
        self.y = y
        print('爬行...')
        self.info()
    
    def info(self):
        print('当前位置：(%d, %d)' % (self.x, self.y))
        
    
    def attack(self):
        print('用嘴咬')

#定义FlyAnt类继承自Ant
class FlyAnt(Ant):
    
    #重写攻击方式
    def attack(self):
        print('用屁股')
        
    #定义方法，模拟飞行
    def fly(self, x, y):
        print('飞行...')
        self.x = x
        self.y = y
        self.info()

flyant = FlyAnt(color='red')
flyant.crawl(3, 5)
flyant.fly(10, 14)
flyant.attack()

"""
爬行...
当前位置：(3, 5)
飞行...
当前位置：(10, 14)
用屁股
"""
```

代码示例2：

```Python
'''
object: 是所有类的基类
1.在类名后边的括号里一般写的是基类的类名
2.子类中继承自父类(基类),则父类的成员属性和成员方法都可以被子类所继承
3.父类中私有的成员属性不能继承给子类的


继承的叫法:  基类(超类,父类)   子类(派生类)


'''
class Animal(object):
    def sleep(self):
        print('动物一般都喜欢躺着睡')

class Person(Animal):
    def __init__(self, user, age, height):
        self.user = user
        self.age = age
        self.height = height

    def eat(self):
        print('我喜欢吃鸡腿')

    def run(self):
        print('我以每秒3米的速度跑向成都')

class GirlFriend(Person):
    pass

cuihua = GirlFriend('翠花', 30, 170)
print(cuihua.user)
cuihua.eat()
cuihua.sleep()
```

代码示例3：

**Person.py**

```Python
class Person(object):
    def __init__(self, user, age, height, money):
        self.user = user
        self._age = age
        self.__height = height
        self.__money = money

    def set_money(self, money):
        self.__money = money
        return self.__money

    def get_money(self):
        return self.__money

    def run(self):
        return '现代社会来讲,健康加运动最重要'
```

**Programmer.py**

```Python
from Person import Person
class Programmer(Person):
    def __init__(self, user, age, height, money, character):
        # super().父级的方法(参数列表)
        super().__init__(user, age, height, money)
        self.__character = character

    def overtime(self):
        # print('加班使我快乐')
        # print(self.__height)
        print(self._age)
```

**Student.py**

```Python
from Person import Person
class Student(Person):
    def __init__(self, user, age, height, money, stuId):
        super().__init__(user, age, height, money)
        self.stuId = stuId

    def love(self):
        print('谈恋爱')

```

**main.py**

```Python
from Person import Person
from Student import Student
from Programmer import Programmer

xiaoming = Student('小明', 18, 175, 1000,  201801001)
# print(xiaoming.user)
# \在子类中不能继承父类的私有属性
# print(xiaoming.__money)
# print(xiaoming.stuId)

# print(xiaoming.get_money())
# print(xiaoming._age)


dahuang = Programmer('大黄', 30, 178, 40, '孤僻')
# print(dahuang._age)
dahuang.overtime()
```



### 3.2 多重继承

​	多重继承的方式是在类定义时的继承父类的括号中，以“,”分隔开要多重继承的父类即可。而多重继承时，继承顺序也是一个很重要的因素，如果继承的多个父类中有相同的方法名，但爱类中使用时未指定父类名，则Python解释器将从左至右搜索。

代码示例1：

```Python
#父类1
class PrntA(object):
    
    namea = 'PrinA'
    
    def set_value(self, a):
        self.a = a
    
    def set_namea(self, namea):
        PrntA.namea = namea
        
    def info(self):
        print('PrinA:%s, %s' % (PrntA.namea, self.a))
#父类2
class PrntB(object):
    nameb = 'PrntB'
    
    def set_nameb(self, nameb):
        PrntB.nameb = nameb
    
    def info(self):
        print('PrntB:%s' % (PrntB.nameb,))
#子类1
class Sub(PrntA, PrntB):
    pass
#子类2
class Sub2(PrntB, PrntA):
    pass
#子类3
class Sub3(PrntA, PrntB):
    
    #重写方法
    def info(self):
        PrntA.info(self)
        PrntB.info(self)
        
print('使用第一个子类：')
sub = Sub()
sub.set_value('aaaa')
sub.info()                   #调用PrntA中的info()
sub.set_nameb('BBBB')
sub.info()                   #还是调用PrntA中的info()
print('-'*15)
"""
使用第一个子类：
PrinA:PrinA, aaaa
PrinA:PrinA, aaaa
"""

print('使用第二个子类：')
sub2 = Sub2()
sub2.set_value('aaaa')       #调用只有PrntA中有的方法
sub2.info()                  #调用在父类列表中前面的PrntB中的info()
sub2.set_nameb('BBBB')
sub2.info()                  #还是调用在父类列表中前面的PrntB中的info()
"""
使用第二个子类：
PrntB:PrntB
PrntB:BBBB
"""

print('使用第三个子类：')
sub3 = Sub3()
sub3.set_value('aaaa')
sub3.info()
sub3.set_nameb('BBBB')
sub3.info()
"""
使用第三个子类：
PrinA:PrinA, aaaa
PrntB:PrntB
PrinA:PrinA, aaaa
PrntB:BBBB
"""
#上面的代都是单独执行的，不是一次全部执行的
```

代码示例2：

```Python
class Animal(object):
    def eat(self):
        return '动物一般喜欢吃肉'

#   驴
class Donkey(Animal):
    def __init__(self, user, age):
        self.user = user
        self.age = age

    def power(self):
        return '驴推磨可以推个十天十夜,都不休息'

    def eat(self):
        return '驴就喜欢吃干草'

#     马
class Horse(Animal):
    def __init__(self, height):
        self.height = height

    def run(self):
        return '汗血宝马可以日行千里'

    def eat(self):
        return '马喜欢吃青草'

# 骡子
# 多继承:在类名后边的括号里可以写多个类名,中间使用,隔开
class Mule(Horse, Donkey):
    pass
    def eat(self):
        return '骡子喜欢吃干青草'

# 在多继承时,参数在最前边的,在实例化对象时,参数是谁就以谁为准
xiaoluo = Mule(1.60)
print(xiaoluo.user)
# print(xiaoluo.eat())

```

代码示例3：

**Father.py**

```Python
class Father(object):
    def __init__(self, money):
        self.money = money

    def play(self):
        return '平时我的父亲喜欢打篮球'

    def make(self):
        return '我父亲挣的钱一般都给了那个阿姨'

    def eat(self):
        return '父亲喜欢吃火锅'
```

**Mather.py**

```Python
class Mother(object):
    def __init__(self, face):
        self.face = face

    def eat(self):
        return '我母亲最喜欢吃的是醋'

    def make(self):
        return '母亲挣的钱都消费了自个'
```

**Son.py**

```Python
from Father import Father
from Mother import Mother

class Son(Father, Mother):
    def __init__(self, money, face):
        Father.__init__(self, money)
        Mother.__init__(self, face)

        print(Father.eat(self))
        print(Mother.eat(self))

    def make(self):
        # 方式一
        # return Father.make(self)
        # 方式二  不常使用
        return super().make()
        # return '我一般挣的钱都给了我老婆,回头被我爸知道了,狠批了我一顿'

xiaoming = Son(100000, '瓜子脸')
# print(xiaoming.money)
# print(xiaoming.face)

print(xiaoming.make())
```



## 4 方法重载

​	当子继承父类时，子类如果想要修改父类的行为，则应该使用方法重载来实现，方法重载的基本方法是在子类中定义一个和所继承的父类中需要重载方法同名的一个方法即可。

代码示例1：

```Python
class Test1(object):
    
    def  func(self):
        return '我是父类的func'

class Test2(Test1):
    
    def func(self):
        return '我是子类的func，我重写了父类的func'

test1 = Test1()
test2 = Test2()
print(test1.func())
print(test2.func())
"""
我是父类的func
我是子类的func，我重写了父类的func
"""
```

代码示例2：

```Python
class Father(object):
    user = '大名'
    def __init__(self, face, norse, eye):
        self.face = face
        self.norse = norse
        self.eye = eye

    def work(self, hour):
        return '我的父亲是一个程序猿,他每天上班超过%d小时' % hour

    def play(self):
        return '旅游,唱歌,喝茶,放风,爬山,钓鱼'

class Son(Father):
    user = '小小明'
    def __init__(self, name, age, face, norse, eye ):
        super().__init__(face, norse, eye)
        self.name = name
        self.age = age

    def work(self, hour):
        return '我一般工作%d小时,因为我晚上回家要陪我老婆' % hour


    def play(self):
        # return '公园,酒吧,网吧,迪吧'
        # 如果不想调用子类,想调用父类的怎么办
        # return super().play()


        # 既想调用父类的方法,也想同时实现自己的方法
        print(super().play())
        print('公园,酒吧,网吧,迪吧')
xiaoming = Son('小明', 27, '方脸', '高鼻梁', '一单一双')
# print(xiaoming.name)
# print(xiaoming.eye)

'''
在继承时,并且父类和子类具有相同的成员,在调用时,直接输出的是子类的内容,这就是子类重写了父类的成员
'''
xiaoming.play()

print(xiaoming.user)
```



## 5 - 多态

```Python
'''
多态: 同一种行为具有不同的表现形式

'''
class Animal(object):
    def eat(self):
        pass

class Tiger(Animal):
    def eat(self):
        print('老虎喜欢吃生肉')

class Lion(Animal):
    def eat(self):
        print('狮子喜欢吃老虎')



def active(type):
    type.eat()
dongbeihu = Tiger()
feizhoumao = Lion()

active(dongbeihu)
active(feizhoumao)

```



## 6 - 小结

​	本文档主要介绍了类的定义、类的属性和方法、其中类属性包括实例属性和类属性，类方法包括实例方法、类方法和静态方法，还介绍了类的继承，包括多继承和单继承，以及类方法的重载。



### 小练习

- **人开枪射击子弹**

  分析：

  ```
  人:
  属性": gun
  方法: fire
  
  枪:
  属性: bulletBox子弹夹
  方法:shoot(射击)
  
  子弹夹:
  属性: bulletCount(子弹的数目)
  ```

  **BulletBox.py**

  ```Python
  class BulletBox(object):
      def __init__(self, count):
          self.bulletCount = count
  ```

  **Gun.py**

  ```Python
  class Gun(object):
      def __init__(self, bulletBox):
          self.bulletBox = bulletBox
  
      def shoot(self):
          if  self.bulletBox.bulletCount == 0:
              # 表示没有子弹了
              print('哥们,没子弹了,装呗')
          else:
              # 表示枪里边还有子弹
              self.bulletBox.bulletCount -= 1
              if self.bulletBox.bulletCount == 0:
                  print('哥们,没子弹了,装呗')
              else:
                  print('目前弹夹里边还有%d颗子弹' % self.bulletBox.bulletCount)
  ```

  **Person.py**

  ```Python
  class Person(object):
      def __init__(self, gun):
          self.gun = gun
  
      def fire(self):
         self.gun.shoot()
  
      def fillBullet(self, count):
          self.gun.bulletBox.bulletCount = count
  ```

  **mian.py**

  ```Python
  from Person import Person
  from Gun import Gun
  from BulletBox import BulletBox
  
  # 得到子弹夹
  bulletBox = BulletBox(7)
  
  # 枪对象
  gun = Gun(bulletBox)
  
  # 人
  xiaoming = Person(gun)
  
  xiaoming.fire()
  xiaoming.fire()
  xiaoming.fire()
  xiaoming.fire()
  xiaoming.fire()
  xiaoming.fire()
  xiaoming.fire()
  xiaoming.fire()
  
  
  xiaoming.fillBullet(7)
  xiaoming.fire()
  xiaoming.fire()
  xiaoming.fire()
  xiaoming.fire()
  xiaoming.fire()
  xiaoming.fire()
  xiaoming.fire()
  ```

  